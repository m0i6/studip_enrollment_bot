import requests
from bs4 import BeautifulSoup
from login import do_login
from courses import my_courses, my_course_names

session = requests.Session()

do_login(session)

course_count = 0

for my_course in my_courses:
    course_url = my_course
    course_response = session.get(course_url)
    course_soup = BeautifulSoup(course_response.text, 'html.parser')

    print(my_course_names[course_count])
    course_count = course_count + 1

    enrolment_link = course_soup.find('a', {'data-dialog': 'size=big'})
    if enrolment_link:
        enrolment_url = enrolment_link['href']
        print("✓ Link")
    else:
        print("✗ Link")

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
                print("✓ Anmeldung erfolgreich")
        else:
            print("✗ Fehler: Netzwerkfehler")
    else:
        print("✗ Fehler: keine gültige URL gefunden")

session.close()
