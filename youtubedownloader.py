from tkinter import *
from pytube import YouTube
import requests
import json
import os

# For UI Creation and design
dwnld = Tk()
dwnld.geometry('500x300')
dwnld.resizable(0,0)
dwnld.title("Youtube Video Downloader")
Label(dwnld,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()

#get data from API
url = "http://smartgsc.rannlabprojects.com/api/CMS/SearchAdvertisement"
payload="{ \r\n\"ID\":\"\",\r\n\"VideoUrl\":\"\"\r\n}\r\n"
headers = {
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)
responseJson = response.json()
jsonLoads = json.loads(responseJson);

##select link
link = StringVar()
Label(dwnld, text = 'Select your Link From Here:', font = 'arial 15 bold').place(x= 160 , y = 60)

listforOption = []

for jsonLoad in jsonLoads:
	listforOption.append(jsonLoad["VideoUrl"])

w = OptionMenu(dwnld, link, *listforOption  ).place(x=100 , y=100)

#function to download video
def Downloader():
    url =YouTube(str(link.get()))
    name="defauleName"
    for jsonLoad in jsonLoads:
    	if link.get() == jsonLoad["VideoUrl"]:
    		name=jsonLoad["ID"]
    		break

    name = str(name) + '.mp4'
    video = url.streams.first()
    video.download()
    os.rename(url.streams.first().default_filename, name)
    Label(dwnld, text = 'DOWNLOADED', font = 'arial 15').place(x= 200 , y = 220)  
Button(dwnld,text = 'Download', font = 'arial 15 bold' ,bg = 'grey', padx = 3, command = Downloader).place(x=180 ,y = 150)

dwnld.mainloop()