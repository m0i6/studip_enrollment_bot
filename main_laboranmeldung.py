import requests
from login import do_login
from courses import my_courses
from enrollment import enroll_in, group_enroll_in
from dotenv import load_dotenv
from os import getenv

load_dotenv()
session = requests.Session()
do_login(session, getenv("FLENS_USERNAME"), getenv("FLENS_PASSWORD"))

for my_course in my_courses:
    print("")
    print(f"{my_course.name}:")
    try:
        # Vorlesungsanmeldung
        print("Vorlesung:")
        enroll_in(session, my_course.url_v)

        # Laboranmeldung
        if (my_course.enrollment_in_groups):
            print("Gruppe:")
            group_enroll_in(session, my_course, my_course.url_l)
        else:
            print("Labor:")
            enroll_in(session, my_course.url_l)

    except requests.exceptions.RequestException as e:
        print(f"✗ Url")

    except Exception as e:
        print(f"✗ unbekannter Fehler")

session.close()
