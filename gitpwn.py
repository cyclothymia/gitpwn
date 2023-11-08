class c:
    r     = '\033[1;31m[-]\033[1;m'
    g     = '\033[1;32m'
    b     = '\033[94m'
    e     = '\033[1;m'
    info  = '\033[1;33m[!]\033[1;m'
    start = ' \033[1;31m[\033[0m'
    stop  = '\033[1;31m]\033[0m'
    banner = """
  ______   __    __      _______                                           __ 
 /      \ /  |  /  |    /       \                                         /  |
/$$$$$$  |$$/  _$$ |_   $$$$$$$  | __   __   __  _______    ______    ____$$ |
$$ | _$$/ /  |/ $$   |  $$ |__$$ |/  | /  | /  |/       \  /      \  /    $$ |
$$ |/    |$$ |$$$$$$/   $$    $$/ $$ | $$ | $$ |$$$$$$$  |/$$$$$$  |/$$$$$$$ |
$$ |$$$$ |$$ |  $$ | __ $$$$$$$/  $$ | $$ | $$ |$$ |  $$ |$$    $$ |$$ |  $$ |
$$ \__$$ |$$ |  $$ |/  |$$ |      $$ \_$$ \_$$ |$$ |  $$ |$$$$$$$$/ $$ \__$$ |
$$    $$/ $$ |  $$  $$/ $$ |      $$   $$   $$/ $$ |  $$ |$$       |$$    $$ |
 $$$$$$/  $$/    $$$$/  $$/        $$$$$/$$$$/  $$/   $$/  $$$$$$$/  $$$$$$$/ 
                                                                              
                  [mason - https://github.com/cyclothymia]                        
                                                                              
                           
                          [Press ENTER to BEGIN]                              
                                                                              
"""

try:
    import re, os, json, fade, rich, requests
    
    from modules         import module as gh
    from time            import sleep
    from pystyle         import *
    from colorama        import *
    from rich.console    import Console
    from rich.table      import Table

except ImportError():
    print(c.r + "Error importing the necessary packages." + c.e)

def gh_single_recon(user):
    gh.check_gh_token()
    gh_id = gh.profile_info(user)
    gh.extract_orgs(user)
    gh_user_keys = gh.keys(user)
    gh.extract_events_leaks(user)
    gh.extract_valid_emails(gh.emails_list, gh_id)
    return gh_id, gh_user_keys

def gh_json_output(gh_id, gh_user_keys):
    json_output = {}
    json_output["username"] = gh_id["login"]
    json_output["name"] = gh_id["name"]
    json_output["user_id"] = gh_id["id"]
    json_output["node_id"] = gh_id["node_id"]
    json_output["email"] = gh_id["email"]
    json_output["location"] = gh_id["location"]
    json_output["bio"] = gh_id["bio"]
    json_output["company"] = gh_id["company"]
    json_output["blog"] = gh_id["blog"]
    json_output["twitter"] = gh_id["twitter_username"]
    json_output["gravatar"] = gh_id["gravatar_id"]
    json_output["hireable"] = gh_id["hireable"]
    json_output["user_type"] = gh_id["type"]
    json_output["admin_status"] = gh_id["site_admin"]
    json_output["public_repos"] = gh_id["public_repos"]
    json_output["public_gists"] = gh_id["public_gists"]
    json_output["followers"] = gh_id["followers"]
    json_output["following"] = gh_id["following"]
    json_output["created_at"] = gh_id["created_at"]
    json_output["updated_at"] = gh_id["updated_at"]
    json_output['urls'] = {}
    json_output['urls']['url'] = gh_id["url"]
    json_output['urls']['html_url'] = gh_id["html_url"]
    json_output['urls']['avatar_url'] = gh_id["avatar_url"]
    json_output['urls']['followers_url'] = gh_id["followers_url"]
    json_output['urls']['following_url'] = gh_id["following_url"]
    json_output['urls']['gists_url'] = gh_id["gists_url"]
    json_output['urls']['starred_url'] = gh_id["starred_url"]
    json_output['urls']['subscriptions_url'] = gh_id["subscriptions_url"]
    json_output['urls']['organizations_url'] = gh_id["organizations_url"]
    json_output['urls']['repos_url'] = gh_id["repos_url"]
    json_output['urls']['events_url'] = gh_id["events_url"]
    json_output['urls']['received_events_url'] = gh_id["received_events_url"]
    json_output['keys'] = []
    if gh_user_keys:
        for key in gh_user_keys:
            data = {'id': (key['id']), 'key': (key['key'])}
            json_output['keys'].append(data)
    json_output['leaked_emails'] = []
    for email in gh.valid_emails:
        json_output['leaked_emails'].append(email)
    return json_output

def gh_result(gh_id, gh_user_keys):
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    
    username = str(gh_id["login"])
    name = str(gh_id["name"])
    user_id = str(gh_id["id"])
    node_id = str(gh_id["node_id"])
    url = gh_id["url"]
    email = gh_id["email"]
    location = gh_id["location"]
    bio = str(gh_id["bio"])
    company = str(gh_id["company"])
    blog = str(gh_id["blog"])
    twitter = str(gh_id["twitter_username"])
    gravatar = str(gh_id["gravatar_id"])
    hireable = str(gh_id["hireable"])
    user_type = str(gh_id["type"])
    admin_status = str(gh_id["site_admin"])
    public_repos = str(gh_id["public_repos"])
    public_gists = str(gh_id["public_gists"])
    followers = str(gh_id["followers"])
    following = str(gh_id["following"])
    created_at = str(gh_id["created_at"])
    updated_at = str(gh_id["updated_at"])

    avatar_url = gh_id["avatar_url"]
    html_url = gh_id["html_url"]
    followers_url = gh_id["followers_url"]
    following_url = gh_id["following_url"]
    gists_url = gh_id["gists_url"]
    starred_url = gh_id["starred_url"]
    subscriptions_url = gh_id["subscriptions_url"]
    organizations_url = gh_id["organizations_url"]
    repos_url = gh_id["repos_url"]
    events_url = gh_id["events_url"]
    received_events_url = gh_id["received_events_url"]

    print(Center.XCenter("GitHub Report for " + username))

    Write.Print(f"""
              [+] Information [+]
    [+] Username:             {username} 
    [+] Name:                 {name}
    [+] User ID:              {user_id}
    [+] Node ID:              {node_id}
    [+] Email:                {email}
    [+] Location:             {location}
    [+] Bio:                  {bio}
    [+] Company:              {company}
    [+] Blog:                 {blog}
    [+] Twitter:              {twitter}
    [+] Gravatar:             {gravatar}
    [+] Hireable:             {hireable}
    [+] Type:                 {user_type}
    [+] Is Admin?:            {admin_status}
    [+] Public Repos:         {public_repos}
    [+] Public Gists:         {public_gists}
    [+] Followers:            {followers}
    [+] Following:            {following}
    [+] Created At:           {created_at}
    [+] Updated At:           {updated_at}
    """, Colors.red_to_purple, interval=0.005)

    Write.Print(f"""
                 [+] URLs [+]
    [+] URL:                  {url}
    [+] HTML URL:             {html_url}
    [+] Avatar URL:           {avatar_url}
    [+] Followers URL:        {followers_url}
    [+] Following URL:        {following_url}
    [+] Gists URL:            {gists_url}
    [+] Starred URL:          {starred_url}
    [+] Subscriptions URL:    {subscriptions_url}
    [+] Organizations URL:    {organizations_url}
    [+] Repos URL:            {repos_url}
    [+] Events URL:           {events_url}
    [+] Received Events URL:  {received_events_url}
    
    """, Colors.green_to_blue, interval=0.005)
    
    if gh_user_keys:
        Write.Print('              [+] SSH Keys: [+]' + "\n", Colors.red_to_green, interval=0.01)
        for key in gh_user_keys:
            Write.Print('    [+] ID: ' + str(key["key"]) + "\n", Colors.red_to_green, interval=0.01)
            Write.Print('    [+] Key: ' + str(key["id"]) + "\n", Colors.red_to_green, interval=0.01)
    
    print()

    Write.Print("                    [+] Emails: [+]" + "\n", Colors.red_to_blue, interval=0.01)
    for email in gh.valid_emails:
        Write.Print('    [+] ' + str(email) + "\n", Colors.red_to_blue, interval=0.01)
    
    print("""


    """)

def save_output(json_output):
    path = 'results/' + user + '.json'
    with open(path, 'w') as f:
        json.dump(json_output, f, indent=4)
        Write.Print(f' [+] Saved output to {path}', Colors.red_to_purple, interval=0.01)

os.system('cls' if os.name == 'nt' else 'clear')
Anime.Fade(Center.Center(c.banner), Colors.purple_to_blue, Colorate.Vertical, interval=0.04, enter=True)

user = Write.Input(" [?] Enter a GitHub username -> ", Colors.red_to_purple, interval=0.005)

gh_id, gh_user_keys = gh_single_recon(user)
gh_result(gh_id, gh_user_keys)
json_data = gh_json_output(gh_id, gh_user_keys)
save_output(json_data)
