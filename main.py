import requests
from bs4 import BeautifulSoup
from login import do_login
from courses import my_courses
from dotenv import load_dotenv
from os import getenv


load_dotenv()
session = requests.Session()
do_login(session, getenv("FLENS_USERNAME"), getenv("FLENS_PASSWORD"))

for my_course, my_url in my_courses.items():
    print("")
    print(f"{my_course}:")
    try:
        course_response = session.get(my_url)
        print(f"✓ Kurs Url existiert")
        course_soup = BeautifulSoup(course_response.text, 'html.parser')

        enrolment_link = course_soup.find('a', {'data-dialog': 'size=big'})
        if enrolment_link:
            enrolment_url = enrolment_link['href']
            print(enrolment_url)
            print("✓ Enrollment Url gefunden")
        else:
            print("✗ Enrollment Url nicht gefunden")

        if enrolment_url:
            security_token = course_soup.find('input', {'name': 'security_token'})['value']
            enrolment_data = {
                'security_token': security_token,
                'apply': '1',
            }

            enrolment_response = session.post(enrolment_url, data=enrolment_data)

            # check for success
            if enrolment_response.status_code == 200:
                soup = BeautifulSoup(enrolment_response.text, 'html.parser')
                page_text = soup.get_text()
                time_out_message = "nicht innerhalb des Anmeldezeitraums"
                if time_out_message in page_text:
                    print("✗ Fehler: außerhalb des Anmeldezeitraums")
                else:
                    print("✓ Anmeldung erfolgreich!!")
            else:
                print("✗ Fehler: Netzwerkfehler")
        else:
            print("✗ Fehler: keine gültige URL gefunden")

    except requests.exceptions.RequestException as e:
        print(f"✗ Url")

    except Exception as e:
        print(f"✗ unbekannter Fehler")

session.close()
