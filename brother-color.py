#!/usr/bin/python
# This  script is Designed to  find the toner levels of brother printers.
# It finds the toner levels by scrapping the webpage of the printers and 
# then formats and displays that text in a webpage. 
#  
# To use this script install python, pip, and use pip to install requests,
# urllib3, and bs4. Make sure your ip_list.txt file is in the same Directory
# as your script. The script will then generate a HTML page and save the page 
# in the Directory you have listed in the path.txt file or if that file  does 
# not exist it will place it in the same directory as the python script.
# 
# The following models have been tested in my environment
#
# - MFC-9340CDW
# - MFC-L8900CDW series
# - MFC-9330CDW
# - MFC-L3770CDW series
# - MFC-L2750DW series
# - HL-3170CDW series
# - HL-L5200DW series
# - MFC-L2740DW series
# - DCP-L2540DW series 
#
# More models can be added to the script as needed
# If you have a model you want added please send me the
# toner status and contact pages

import requests
import sys
import os
import urllib3.request
import time
import datetime
from bs4 import BeautifulSoup




with open('Color_Printers.list') as f:
    Color_Printers = f.readlines()

f.close()
# you may also want to remove whitespace characters like `\n` at the end of each line
Color_Printers = [x.strip() for x in Color_Printers] 

with open('Monochrome_Printers.list') as f:
    Monochrome_Printers = f.readlines()
f.close
# you may also want to remove whitespace characters like `\n` at the end of each line
Monochrome_Printers = [x.strip() for x in Monochrome_Printers]

log_Message = " "
try: 
	f=open("path.txt", "r")
	dirpath =f.read()
	dirpath =dirpath.strip()
except IOError:
	dirpath = os.getcwd()
	print("current directory is : " + dirpath)
	foldername = os.path.basename(dirpath)
	print("Directory name is : " + foldername)

write_out = open(dirpath +'/printers.html','w')

message = """<html>
<head><link rel='stylesheet' href='styles.css'/><meta http=equiz='refresh' content='1800'></head>
<body><h1>Brother Printer Status Page</h1> """

currentDT = datetime.datetime.now()
currenttime = currentDT.strftime("%a, %b %d, %Y, %H:%M")
message = message + '<h1>'+ currenttime +'</h1>'
message = message + "<table border='1'><tr>"
try:

	log=open("printers.log","w")
except:
	print "Error Opening Log"

with open('ip_list.txt') as f:
        content = f.readlines()

content = [x.strip('\n') for x in content]
print "Processing Please Wait"
Number_of_Cells = 0
for x in content:
        url='http://' + x +'/general/status.html'
	try :
        	response = requests.get(url)
	except:
		log_Message = log_Message + x + " is not alive skipping ip\n"
		
		continue
        soup = BeautifulSoup(response.text, "html.parser")
	Model = soup.find('title').text


	Office =  soup.find('li',{'class':'location'}).get_text()
	Office = Office.replace(u'\xa0', u' ')
	if Office == "Location:":
	
		Office = "Location:N/A"

	Black_Remaining = None
	Cyan_Remaining = None
	Magenta_Remaining = None
	Yellow_Remaining = None

	if Model in Color_Printers:

		table = soup.find('table',{'id':'inkLevel'})
		Toner = table.find_all('img',{'class':'tonerremain'})
		Black = Toner[0].get('height')
		Bheight = Black.strip('px')
		Bheight = float(Bheight)
		Bprecent = (Bheight/56) * 100
		Black_Remaining = round(Bprecent,0)

		Cyan = Toner[1].get('height')
		Cheight = Cyan.strip('px')
		Cheight = float(Cheight)
		Cprecent = (Cheight/56) * 100
		Cyan_Remaining = round(Cprecent,0)

		Magenta = Toner[2].get('height')
		Mheight = Magenta.strip('px')
		Mheight = float(Mheight)
		Mprecent = (Mheight/56) * 100
		Magenta_Remaining = round(Mprecent,0)

		Yellow = Toner[3].get('height')
		Yheight = Yellow.strip('px')
		Yheight = float(Yheight)
		Yprecent = (Yheight/56) * 100
		Yellow_Remaining = round(Yprecent,0)
		
		log_Message = log_Message + x + " completed " + "B: " +str(Black_Remaining) + " C: " + str(Cyan_Remaining) + " M: " + str(Magenta_Remaining) + " Y: " + str(Yellow_Remaining) +"\n"

                        
	if Model in Monochrome_Printers:

		Bheight = soup.find('img',{'class':'tonerremain'}).get('height')
               	Bheight = Bheight.strip('px')
                Bheight = float(Bheight)
                Bprecent = (Bheight/56) * 100
                Black_Remaining = round(Bprecent,0)

		log_Message = log_Message + x + " completed " + "B: " +str(Black_Remaining) +"\n"


	if Number_of_Cells == 3:

		message = message + "<tr>"
		Number_of_Cells = 0

	Order_Link = " "

	if Model == "Brother MFC-9340CDW" or Model == "Brother MFC-9330CDW" or Model == "Brother HL-3170CDW series":
		Order_Link = "<a href='https://www.amazon.com/s?k=TN225&i=office-products&ref=nb_sb_noss_2' target='_blank'> Order TN221 </a>"
	if Model == "Brother MFC-L8900CDW series":
		Order_Link = "<a href='https://www.amazon.com/s?k=MFC-L8900CDW+Toner&i=office-products&ref=nb_sb_noss' target='_blank'> Order TN436 </a>"
	if Model == "Brother MFC-L3770CDW series":
		Order_Link = "<a href='https://www.amazon.com/s?k=TN+227&i=office-products&ref=nb_sb_noss_2' target='_blank'> Order TN227 </a>"
	if Model =="Brother MFC-L2750DW series":
		Order_Link = "<a href='https://www.amazon.com/s?k=TN760&i=office-products&ref=nb_sb_noss_2' target='_blank'> Order TN760 </a>"
	if Model =="Brother HL-L5200DW series":
		Order_Link = "<a href='https://www.amazon.com/s?k=TN850&i=office-products&ref=nb_sb_noss_2' target='_blank'> Order TN850 </a>"
	if Model =="Brother MFC-L2740DW series" or Model == "Brother DCP-L2540DW series":
		Order_Link = "<a href='https://www.amazon.com/s?k=tn660&i=office-products' target='_blank'> Order TN660 </a>"

	message = message +  "<td><p>Model: " + Model + "</p>"
	message = message +   Office + "</p>"
	message = message +  "<p>IP Address: <a href='http://" + x + "'target='_blank'>"+x+"</a></p>"
	message = message + "<p>======Toner Remaining======</p>"
	if Black_Remaining is not None:
		if Black_Remaining < 15.0:

                        message = message + "<progress class='black blinking' min='0' max='100' value='" + str(Black_Remaining) + "'></progress><b class='blinking'> Toner LOW </b><br>"

		else:
			message = message + "<progress class='black' min='0' max='100' value='" + str(Black_Remaining) + "'></progress><b>"+ str(Black_Remaining) +"</b><br>"
	if Cyan_Remaining is not None:
		if Cyan_Remaining < 15.0:
			message = message + "<progress class='black blinking' min='0' max='100' value='" + str(Cyan_Remaining) + "'></progress><b class='blinking'> Toner LOW </b><br>"

		else:
			message = message + "<progress class='Cyan' min='0' max='100' value='" + str(Cyan_Remaining) + "'></progress><b>"+ str(Cyan_Remaining) +"</b><br>"
	if Magenta_Remaining is not None:
		if Magenta_Remaining < 15.0:
			message = message +  "<progress class='black blinking' min='0' max='100' value='" + str(Magenta_Remaining) + "'></progress><b class='blinking'> Toner LOW </b><br>"

		else:
			message = message +  "<progress class='Magenta' min='0' max='100' value='" + str(Magenta_Remaining) + "'></progress><b>"+ str(Magenta_Remaining) +"</b><br>"
	if Yellow_Remaining is not None:
		if Yellow_Remaining < 15.0:
			message = message +  "<progress class='black blinking' min='0' max='100' value='" + str(Yellow_Remaining) + "'></progress><b class='blinking'> Toner LOW </b><br>"
		else:
			message = message +  "<progress class='Yellow' min='0' max='100' value='" + str(Yellow_Remaining) + "'></progress><b>"+ str(Yellow_Remaining) +"</b><br>"

	message = message + "</ul><p>" + Order_Link + "</p></td>"
	Number_of_Cells = Number_of_Cells + 1
message = message + "<tr><table></body></html>"
write_out.write (message)
write_out.close()
log.write(log_Message)
log.close()
print "Processing Complete"
