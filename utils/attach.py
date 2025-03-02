import allure
import requests


def add_video(session_id, login, access_key):
    browserstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json', auth=(login, access_key)).json()
    video_url = browserstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src={video_url} type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML)
