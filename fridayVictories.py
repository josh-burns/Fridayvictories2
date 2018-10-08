import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sys
from slackclient import SlackClient
from keys import (token, clientSecret)
import time

# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


# Any print() will be written to the HTML file
sys.stdout = open('file.html', 'w')

print("<link href=\"https://fonts.googleapis.com/css?family=Lato\" rel=\"stylesheet\"> ")
print("<style> body { background-image: url(\"https://www.goodlord.co/images/hp_burst.jpg\"); "
      "font: normal 15px Verdana, Arial, sans-serif; font-family:'Lato'; color: black} "
      ".response {background-color: #bfbfbf; border-radius: 15px 50px 15px; z-index: 2; "
      "max-width:700px; padding:40px; opacity:80%; "
      "margin: 15 auto; display:flex; opacity: 30%;}"
      ".title {width 300px; margin: 30 auto; color: #d8d8d8; border-radius: 15px 50px 15px; "
      "max-width:700px; padding:50px; "
      "opacity:80%; margin: 15 auto; font-family:'Lato'; background-color: grey;}"
      ".photo{ width: 192px; display:inline-block; order: 1; margin: 60px;}"
      ".text_body {order: 2; margin: 10 auto; background-color: #d8d8d8; "
      "border-radius: 15px 50px 15px; max-width:700px; padding: 30px;}"
      ".title_text {vertical-align:center; text-align: center;}"
      "</style>"
      "<div class=\"title\"> <h1> <div class=\"title_text\"> Friday Victories </h1> </div> </div>"
      )


def html_work_and_personal_vics():
    print("<i><b> Work Victory:</b> </i> <br>")
    print(workVictory[count], "<br> <br>")
    print("<i><b> Personal Victory: </b> </i> <br>")
    print(persVictory[count], "</div>")
    print("</div>", '</div>')


def print_slack_photo_and_real_name():
    # api call to slack to obtain user info, based on email address of responder
    userPhoto.insert(0, sc.api_call("users.lookupByEmail", email=emailAddress[count]))
    print("<div class=\"response\">")
    print("<div class = \"photo\" >", "<img src= \" ", userPhoto[0]['user']['profile']['image_192'], "\">",
          '</div>' "<br>")
    print("<div class=\"text_body\">", "<b> <h2> ", userPhoto[0]['user']['real_name'], " </b> </h2>")


def print_dog_picture_and_email_address():
    userPhoto.insert(0, "https://cdn.shopify.com/s/files/1/1429/4170/articles/Four_easy_dog_calming_tips_Cropped_1_a6703117-eb49-49bc-8b27-b2a73c599299_grande.jpg?v=1516848931")
    print("<div class=\"response\">")
    print("<div class = \"photo\" >", "<img src= \" ", userPhoto[0], "\">", '</div>' "<br>")
    print("<div class=\"text_body\">", "<b>", emailAddress[count], "</b>", "<br>", "<br>")


# Google forms/sheets API/WebHook integration
CLIENT_SECRET = clientSecret
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
client = gspread.authorize(creds)
sheet = client.open('AutomatedFridayVictoriesResponses').sheet1


# slack token
slack_token = token
sc = SlackClient(slack_token)
slackUsers = sc.api_call("users.list")

# val checks if the timestamp field of the response spreadsheet is populated or not, to check whether to progress
val: str = sheet.acell('A2').value
emailAddress = list()
userPhoto = []
workVictory = []
persVictory = []
displayName =[]
responsesIngested = 0
count = 0

# write responses to list, and remove each row in spreadsheet so it is ready for next use
while val is not "":
    val = sheet.acell('a2').value
    emailAddress.append(sheet.acell('b2').value)
    workVictory.append(sheet.acell('c2').value)
    persVictory.append(sheet.acell('d2').value)
    sheet.delete_row(2)
    time.sleep(1)
    count += 1

else:
    responsesIngested += 1
    emailAddress = emailAddress[:-1]
    count -= 2

# populate a list with slack photos corresponding to each email address

while responsesIngested is not 0:
    while count > 0:
        try:
            print_slack_photo_and_real_name()
            html_work_and_personal_vics()
            count -= 1

        except KeyError or TypeError:
            print_dog_picture_and_email_address()
            html_work_and_personal_vics()
            count -= 1
    else:
        try:
            print_slack_photo_and_real_name()
            html_work_and_personal_vics()
            count -= 1
            responsesIngested -= 1

        except KeyError or TypeError:
            print_dog_picture_and_email_address()
            html_work_and_personal_vics()
            count -= 1
            responsesIngested -= 1

    print("<div class=\"title\">", "<h1> <div class=\"title_text\">", "This week,", (len(workVictory) - 1),
          " people filled in their Friday victories!", "</div>", "</div>")

