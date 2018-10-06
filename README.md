# Friday Victories 

A tool designed for companies to receive and broadcast staff-members' responses to the following questions: 

* "*What is your **professional** victory this week?*"
* "*What is your **personal** victory this week?*"


# Installation 


#### Requirements 

This tool uses the following libraries: 
* Gspread 
* Oath2Client
* Sys 
* Time

A client_secret.json file is required for the Google Sheets integration ([See more here](https://developers.google.com/sheets/api/guides/authorizing)), with the following information:

```json
{
  "type": "",
  "project_id": "",
  "private_key_id": "",
  "private_key": "",
  "client_email": "",
  "client_id": "",
  "auth_uri": "",
  "token_uri": "",
  "auth_provider_x509_cert_url": "",
  "client_x509_cert_url": ""
}

```

A keys.py file is required for the Slack integration, with the following information:

```
token = "TOKEN-RECIEVED-FROM-SLACK"

clientSecret = 'notasecret' 
```



### To Do 

* Sanitise email address to remove domain to just  have "Josh" instead of "josh@company.co"
* Add unit tests and error handling

