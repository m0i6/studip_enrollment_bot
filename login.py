from bs4 import BeautifulSoup

def do_login(session, username, password):
    
    login_url = "https://elearning.hs-flensburg.de/index.php?login=1"
    response = session.get(login_url)

    soup = BeautifulSoup(response.text, 'html.parser')

    # extract hidden tokens
    security_token = soup.find('input', {'name': 'security_token'})['value']
    login_ticket = soup.find('input', {'name': 'login_ticket'})['value']
    resolution = soup.find('input', {'name': 'resolution'})['value']

    # create POST-data
    login_data = {
        'loginname': username,
        'password': password,
        'security_token': security_token,
        'login_ticket': login_ticket,
        'resolution': resolution
    }

    # POST-request
    login_response = session.post(login_url, data=login_data)

    # login check!!
    if "dispatch.php/start" in login_response.url:
        print("✓ Login")
    else:
        print("✗ Login")
        exit()