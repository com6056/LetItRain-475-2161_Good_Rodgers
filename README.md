# LetItRain
**Cloud Storage Positive/Negative Hashing**

## About
This tool will take an account for a cloud storage provider (Google Drive, Dropbox, etc.) and download all available info (current files, deleted files, and file versions) from that provider. The data will be sorted into an easy-to-navigate directory structure, and both positive and negative hashing will be performed with a user-provided hash database. The tool will report with all matching "bad" hashes as well as which files can be safely ignored. Available metadata for each file will be downloaded and stored in an easily accessible format.

---

### Setting Up Your Environment
There are a few initial steps that have to happen before using Let It Rain:

1. Install PyDrive and Dropbox Python libraries
2. Getting access to the provider's API
  * a. Google Drive
  * b. Dropbox
3. Authorize the tool to interrogate the account
  * a. Google Drive
  * b. Dropbox

---

**1. Installing Dependencies**   

This tool was built for Python 3. To install the dependencies using pip, run the following commands (you might need to use pip instead of pip3 depending on how you have Python set up):

```
pip3 install pydrive
pip3 install dropbox
```


**2a. Getting Access to the Google Drive API**

Google Drive, to use the API, requires credentials for the account being accessed. In order to get the necessary client_secrets.json file, there are a few required steps.

* Go [here](https://console.developers.google.com) to the Google API console and create a project tied to a Google Account. The name of the project does not matter.
* Click on the "Create" button.
* This should bring you to the dashboard of that project. Click on the "[+]Enable API" button.
* This should bring you to the "Library" tab. This will have a list of all the available Google APIs. We are concerned with the Google Drive API. Under "Google Apps APIs" select "Drive API". This will bring you to the Google Drive API about page.
* Select the "Enable" button towards the top of the screen. A warning box will appear under the button saying the project cannot be used until credentials are established.
* Go to the credentials tab on the left navigation pane. Click on "Create credentials" and select "Help Me Choose".
* Under the first drop down select "Google Drive API".
* Under the second drop down select "Web Server".
* Select the "User Data" radio button.
* Click on "What credentials do I need?". This should put you to the proper credential creation wizard for OAuth.
* Choose a name for the client. Under "Authorized JavaScript origins" put "http://localhost:8080" and under "Authorized Redirect URIs" put "http://localhost:8080/" and then click "Create client ID".
* Fill in the desired email address for the tool and fill in the product name (e.g. "Let It Rain") for the consent screen information.
* Download the credentials (renaming the file from client_id.json to client_secrets.json) and place the credentials file in the same directory as the LetItRain code whenever you run the tool.

**2b. Getting Access to the Dropbox API**

Similar to the Google Drive API, you must create an account and set up an app to use the Dropbox API. This account should be separate from the one you will be interrogating with the tool.

* Go [here](https://www.dropbox.com/developers/apps/create) and log in or create a new Dropbox account (do not use the account you will be interrogating with the tool).
* For "Choose an API", select the "Dropbox API" option. For "Choose the type of access you need", select the "Full Dropbox" option. Name it whatever you want. Then click "Create app".
* Click "Enable additional users" to the right of "Development users" so that accounts other than the one you used to create the app can access it.
* Save the "App key" and "App secret" as you will need them once you are ready to run the tool.

**3a. Authorizing the Account with the Google Drive Project**

* When you run the tool with a Google Drive account, a link will be presented to the user. Copy and paste that link into a browser window and select "Allow" for the tool to generate an access token for the user.
* Once the access token is generated, it will then save it as "letitrain-creds-gdrive.txt". If you receive any errors about being able to authenticate with Google Drive, make sure you delete that file before you try to authenticate again.

**3b. Authorizing the Account with the Dropbox App**

* When you run the tool with a Dropbox account, it will ask you to enter in the app key and app secret which you should have saved from when you created the Dropbox app. Once you enter those, navigate to the URL it outputs.
* Log into the account that you will be interrogating (it will ask you to log in first if you aren't already or you can log out and log into the correct account through the dropdown at the top right) and then click "Allow" to give the Dropbox app access to the account. It will then output an access token that will need to be pasted into the tool.
* Once the access token is entered into the tool, it will then save it as "letitrain-creds-dbox.txt". If you receive any errors about being able to authenticate with Dropbox, make sure you delete that file before you try to authenticate again.

---
