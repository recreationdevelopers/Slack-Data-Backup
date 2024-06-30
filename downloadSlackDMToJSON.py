import requests
import json

# Uncomment the following section if you're getting HTTPS warnings
"""
import urllib3

# Suppress only the single InsecureRequestWarning from urllib3 needed for the requests module
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
"""

# Replace with your actual Slack User token
slack_user_token = 'slack user token goes here'
# Replace with your actual DM channel ID
channel_id = 'dm channel id goes here'
json_file_name = 'slack_dm_with_threads.json'

headers = {
    'Authorization': f'Bearer {slack_user_token}',
}

params = {
    'channel': channel_id,
    'limit': 1000  # Adjust as needed, max is 1000
}

def fetch_conversation_history():
    url = 'https://slack.com/api/conversations.history'
    response = requests.get(url, headers=headers, params=params, verify=False)
    data = response.json()

    if not data.get('ok'):
        error_message = data.get('error')
        if error_message == 'channel_not_found':
            print("Error: The specified channel ID was not found. Please verify the channel ID.")
        elif error_message == 'not_in_channel':
            print("Error: The bot is not a member of the channel. Please add the bot to the channel.")
        elif error_message == 'invalid_auth':
            print("Error: Invalid authentication token. Please check your token.")
        else:
            print(f"Error retrieving messages: {error_message}")
        return []

    return data['messages']

def fetch_thread_replies(channel_id, thread_ts):
    url = 'https://slack.com/api/conversations.replies'
    thread_params = {
        'channel': channel_id,
        'ts': thread_ts,
        'limit': 1000
    }
    response = requests.get(url, headers=headers, params=thread_params, verify=False)
    data = response.json()

    if not data.get('ok'):
        print(f"Error retrieving thread replies: {data.get('error')}")
        return []

    # Exclude the first message as it is the thread parent
    return data['messages'][1:]

def fetch_all_messages(channel_id):
    messages = fetch_conversation_history()
    all_messages = []

    for message in messages:
        all_messages.append(message)
        if 'thread_ts' in message:
            thread_ts = message['thread_ts']
            replies = fetch_thread_replies(channel_id, thread_ts)
            all_messages.extend(replies)
    
    return all_messages

all_messages = fetch_all_messages(channel_id)

# Save messages to a file
with open(json_file_name, 'w') as file:
    json.dump(all_messages, file, indent=4)

print(f"Messages saved to {json_file_name}")