# Part1: Scrapping news headlines(Hacker news to be exact)
# Part2: Sending an email for the same
# For part2 do not forget to allow less secure app access on your gmail account 'on'

#  Required libraries

import requests
from bs4 import BeautifulSoup as bs
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime as dt
from From_to_mails import Sender_mails, Reciever_mails

now = dt.datetime.now()

content = '' # For Email's Body

# Function to extract news

def extract_news(url):
     print('Extracting Hacker News Stories...')
     cont = ''
     cont += ('<b>HN Top Stories:</b>\n' + '<br>' + '-' * 50 + '<br>')
     response = requests.get(url)
     conten = response.content
     soup = bs(conten,'html.parser')
     
     for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
          cont += ((str(i+1)+' :: '+ '<a href="' + tag.a.get('href') + '">' + tag.text + '</a>' + "\n" + '<br>') if tag.text != 'More' else '')
          # print(tag.prettify) #find_all('span',attrs={'class':'sitestr'}))
     
     return(cont)

conten = extract_news('https://news.ycombinator.com/')
content += conten
content += ('<br>----------</br>')
content += ('<br></br>Rnd of doc')


# Mailing component

SERVER = 'smtp.gmail.com'     # SMTD Server
PORT = 587                    # Port number, can be customized
FROM = Sender_mails[0]['username']
TO = Reciever_mails[0]
PASS = Sender_mails[0]['password']

print(FROM)
print(TO)

msg = MIMEMultipart()

msg['Subject'] = 'Top News Stories HN [Automated Email]' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))



# Server Initialization time here

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print("Done with this stuff \
     Mail has been sent \
     Time to go home")

server.quit()