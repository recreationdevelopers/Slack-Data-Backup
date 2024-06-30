# Slack Data Backup

Script to backup a DM from a Slack subdomain. Use the code at your own risk and please do due diligence before running it.

## Pre-Requisites

1. You might require a Slack subscription that grants you access to the entire message history. **This code has been tested on a trial version of Slack Pro in June 2024.**
2. You need to have the necessary access to the Slack subdomain that should grant you permissions to create and install apps to your Slack Workspace. Please check with an admin before proceeding, if you aren't one.

### Creating the Slack app

1.  Visit [Slack API's app page](https://api.slack.com/apps) and click on _Create New App_
2.  Choose _From Scratch_ in the pop up that shows next.
3.  Give the app an identifiable name and choose the workspace that the app should be associated with.
4.  The click on _Create App_. This will take you to the settings section of the app.
5.  In the left panel, under the _Features_ category, choose _OAuth & Permissions_.
6.  Scroll down to the _Scopes_ section and under _User Token Scopes_, click on _Add an OAuth Scope_. This will show a dropdown with a list of possible permissions.
7.  Choose _im:history_ and _users:read_ permissions from this, one by one.
8.  Ensure that see you these added to the _User Token Scopes_ section.
9.  Scroll up to the _OAuth Tokens for Your Workspace_ section and click on _Install to Workspace_. This will take you to a permission-request page, where you can confirm the categories and click _Allow_.
10. You'll be taken back to the _OAuth & Permissions_ page.

### Getting the Slack User Token:

1. In the _OAuth & Permissions_ page, scroll down to the _OAuth Tokens for Your Workspace section_.
2. You should see a new _User OAuth Token_ added. Click _copy_ next to it so you can use this in the python script for the variable _slack_user_token_. **Make sure to keep this token private.**

### Getting the Channel ID of the DM:

1. Open the DM in Slack, preferably in a browser.
2. In the URL, you’ll see something like https://app.slack.com/client/T12345678/D12345678
3. Here D12345678 is the channel ID for the DM. Copy it so you can use it in python script's _channel_id_ variable.

## Python Script

The python file, [downloadSlackDMToJSON.py](downloadSlackDMToJSON.py) has the following placeholders:

-   _slack_user_token_
-   _channel_id_
-   _json_file_name_ - You can choose the name of the JSON file that will be created in the same directory.

Ensure that you have _requests_, _json_ & optionally _urllib3_ python modules installed. If not, use _pip_ to install them.

In case you're getting HTTPS warnings, you can uncomment the section in the code that uses _urllib3_.

**Note**:

1. For files uploaded to the DM, you'll see _url_private_ & _url_private_download_ properties in the generated JSON. You can write another script to download them, although it can get tricky and might require additional bot token scopes or user token scopes permissions.
2. Anytime you add an OAuth Scope to either _Bot Token Scopes_ or _User Token Scopes_, you'll need to scroll up to the _OAuth Tokens for Your Workspace_ section and click on _Reinstall to Workspace_ for those permissions to come into effect.
