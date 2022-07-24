# Part1: Scrapping news headlines(Hacker news to be exact)
# Part2: Sending an email for the same

#  Required libraries

import requests
from bs4 import BeautifulSoup as bs
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime as dt

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
          cnt += ((str(i+1)+' :: '+ '<a href="' + tag.a.get('href') + '">' + tag.text + '</a>' + "\n" + '<br>') if tag.text != 'More' else '')
          # print(tag.prettify) #find_all('span',attrs={'class':'sitestr'}))
     
     return(cnt)