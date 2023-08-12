import valclient
import json
import time

# Get region from user
region = "AP"

try:
    client = valclient.Client(region.lower())
    client.activate()
except Exception as e:
    print(e)
    print("No Client Active !!")
    exit()

agents = json.load(open("agents.json"))

seen_matches = []
lock_delay = 1
    
def locker(selected_agent):
    try:
        time.sleep(1)
        valorantInfo = client.fetch_presence(client.puuid)
        sessionState = valorantInfo['sessionLoopState']
        if (sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in seen_matches):
            print('Agent Select Found')
            time.sleep(5)
            client.pregame_select_character(agents[selected_agent])
            time.sleep(lock_delay)
            client.pregame_lock_character(agents[selected_agent])
            seen_matches.append(client.pregame_fetch_match()['ID'])
            print('Successfully Locked ' + selected_agent.capitalize())
    except Exception as e:
        print(e)
        pass