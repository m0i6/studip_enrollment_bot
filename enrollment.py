from bs4 import BeautifulSoup

def enroll_in(session, url):
    course_response = session.get(url)
    print(f"✓ Kurs Url existiert")
    course_soup = BeautifulSoup(course_response.text, 'html.parser')

    # get enrollment url
    enrolment_link = course_soup.find('a', {'data-dialog': 'size=big'})
    if enrolment_link:
        enrolment_url = enrolment_link['href']
        print("✓ Enrollment Url gefunden")
    else:
        print("✗ Enrollment Url nicht gefunden")

    # enroll
    if enrolment_url:
        security_token = course_soup.find('input', {'name': 'security_token'})['value']
        enrolment_data = {'security_token': security_token, 'apply': '1'}
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


def group_enroll_in(session, course, url):

    course_response = session.get(url)
    print(f"✓ Kurs Url existiert")
    course_soup = BeautifulSoup(course_response.text, 'html.parser')

    # get enrollment url
    group_enrollment_urls = []
    for a_tag in course_soup.find_all('a'):
        img_tag = a_tag.find('img', class_="icon-role-clickable icon-shape-door-enter")
        if img_tag:
            url_from_a_tag = a_tag.get('href')
            group_enrollment_urls.append(url_from_a_tag)

        group_enrollment_url = group_enrollment_urls[course.group_number - 1]

    if group_enrollment_url:
        enrolment_response = session.post(group_enrollment_url)

        # check for success
        if enrolment_response.status_code == 200:
            print("✓ Anmeldung erfolgreich!!")
        else:
            print("✗ Fehler: Netzwerkfehler")
    else:
        print("✗ Fehler: keine gültige URL gefunden")