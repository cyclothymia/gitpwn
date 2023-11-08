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
    from multiprocessing import Pool, Process, freeze_support, set_start_method, get_context

except ImportError():
    print(c.r + "Error importing the necessary packages." + c.e)

os.system('cls' if os.name == 'nt' else 'clear')
Anime.Fade(Center.Center(c.banner), Colors.purple_to_blue, Colorate.Vertical, interval=0.04, enter=True)

filename = Write.Input(" [?] Enter the name of the file containing the list of emails: ", Colors.red_to_purple)

def gh_recon(user):
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

def gh_main(line):
    user = line.strip()
    gh_id, gh_user_keys = gh_recon(user)
    json_output = gh_json_output(gh_id, gh_user_keys)
    path = 'results/' + line + '.json'
    with open(path, 'w') as f:
        json.dump(json_output, f, indent=4)
        Write.Print(f' [+] {user} saved output to {path}.', Colors.red_to_purple, interval=0.01)
        f.close()

if __name__ == "__main__":
    freeze_support()
    users = open(f"{filename}")
    lines = users.readlines()
    pool = Pool(processes=10)
    pool.map(gh_main, lines)