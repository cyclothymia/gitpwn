import os
import requests as r
from dotenv import load_dotenv
from pystyle import *

load_dotenv()

gh_token =  os.getenv('GH_TOKEN')
gh_keys = []
gh_orgs = []
emails_list = {}
valid_emails = []
gh_api = "https://api.github.com/users/"
gh_events = "/events?per_page=100"
gh_headers = {
    'Authorization': 'token ' + gh_token
}

def check_gh_token():
    if (gh_token == None):
        print()
        Write.Print(" [!] GitHub token is not set in .env file. Please set it and try again.", 
                    Colors.red_to_purple, 
                    interval=0.01)
        exit()
    elif (gh_token == ""):
        print()
        Write.Print(" [!] GitHub token is not set in .env file. Please set it and try again.", 
                    Colors.red_to_purple, 
                    interval=0.01)
        exit()
    elif (gh_token == " "):
        print()
        Write.Print(" [!] GitHub token is not set in .env file. Please set it and try again.", 
                    Colors.red_to_purple, 
                    interval=0.01)
        exit()
    else:
        pass

def profile_info(user):
    response = r.get(gh_api + user, headers=gh_headers)
    if r.status_codes == 404:
        print()
        Write.Print(f' [!] {user} not found', Colors.red_to_purple, interval=0.01)
        exit()
    return response.json()

def get_orgs(user):
    response = r.get(gh_api + user + '/orgs', headers=gh_headers)
    return response.json()

def keys(user):
    response = r.get(gh_api + user + '/keys', headers=gh_headers)
    return response.json()

def get_events(user):
    response = r.get(gh_api + user + gh_events, headers=gh_headers)
    return response.json()

def extract_orgs(user):
    orgs = get_orgs(user)
    for org in orgs:
        gh_orgs.append(org['login'])

def extract_events_leaks(user):
    events = get_events(user)
    for data in events:
        try:
            for info in data['payload']['commits']:
                info = {info['author']['email']: info['author']['name']}
                emails_list.update(info)
        except:
            pass

def extract_valid_emails(emails, user_info):
    for email in emails_list:
        if emails[email] == user_info['name']:
            valid_emails.append(email)
