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
<head><link rel='stylesheet' href='styles.css'/></head>
<body><h1>Brother Printer Status Page</h1> """

currentDT = datetime.datetime.now()
currentDT.strftime("%a, %b %d, %Y")
message = message + '<h1>'+ currentDT.strftime("%a, %b %d, %Y")+'</h1>'
message = message + "<table border='1'><tr>"

with open('ip_list.txt') as f:
        content = f.readlines()

content = [x.strip('\n') for x in content]
print "Processing Please Wait"
Number_of_Cells = 0
for x in content:
        url='http://' + x +'/general/status.html'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
	Model = soup.findAll('h1')[0].text


	Office =  soup.find('li',{'class':'location'}).get_text()
	Office = Office.replace(u'\xa0', u' ')
	if Office == "Location:":
	
		Office = "Location:N/A"

	Black_Remaining = None
	Cyan_Remaining = None
	Magenta_Remaining = None
	Yellow_Remaining = None

	if Model == "MFC-9340CDW" or Model =="MFC-L8900CDW series" or Model == "MFC-9330CDW" or Model == "MFC-L3770CDW series":

		try:
			Black = soup.findAll('img')[1]
                	Bheight = Black ['height']
                	Bheight = Bheight.strip('px')
                	Bheight = float(Bheight)
                	Bprecent = (Bheight/56) * 100
                	Black_Remaining = round(Bprecent,0)

			Cyan = soup.findAll('img')[2]
        		Cheight = Cyan ['height']
        		Cheight = Cheight.strip('px')
        		Cheight = float(Cheight)
        		Cprecent = (Cheight/56) * 100
        		Cyan_Remaining = round(Cprecent,0)

                	Magenta = soup.findAll('img')[3]
                	Mheight = Magenta ['height']
                	Mheight = Mheight.strip('px')
                	Mheight = float(Mheight)
                	Mprecent = (Mheight/56) * 100
                	Magenta_Remaining = round(Mprecent,0)

                	Yellow = soup.findAll('img')[4]
                	Yheight = Yellow ['height']
                	Yheight = Yheight.strip('px')
                	Yheight = float(Yheight)
                	Yprecent = (Yheight/56) * 100
                	Yellow_Remaining = round(Yprecent,0)
		
		except KeyError:

                        Black = soup.findAll('img')[2]
                        Bheight = Black ['height']
                        Bheight = Bheight.strip('px')
                        Bheight = float(Bheight)
                        Bprecent = (Bheight/56) * 100
                        Black_Remaining = round(Bprecent,0)

                        Cyan = soup.findAll('img')[3]
                        Cheight = Cyan ['height']
                        Cheight = Cheight.strip('px')
                        Cheight = float(Cheight)
                        Cprecent = (Cheight/56) * 100
                        Cyan_Remaining = round(Cprecent,0)

                        Magenta = soup.findAll('img')[4]
                        Mheight = Magenta ['height']
                        Mheight = Mheight.strip('px')
                        Mheight = float(Mheight)
                        Mprecent = (Mheight/56) * 100
                        Magenta_Remaining = round(Mprecent,0)

                        Yellow = soup.findAll('img')[5]
                        Yheight = Yellow ['height']
                        Yheight = Yheight.strip('px')
                        Yheight = float(Yheight)
                        Yprecent = (Yheight/56) * 100
                        Yellow_Remaining = round(Yprecent,0)

	if Model == "MFC-L2750DW series" or Model == "HL-3170CDW series" or Model == "HL-L5200DW series"or Model == "MFC-L2740DW series":
		
		try:
	                Black = soup.findAll('img')[2]
        	        Bheight = Black ['height']
               		Bheight = Bheight.strip('px')
                	Bheight = float(Bheight)
                	Bprecent = (Bheight/56) * 100
                	Black_Remaining = round(Bprecent,0)

		except KeyError:
			Black = soup.findAll('img')[1]
                	Bheight = Black ['height']
                	Bheight = Bheight.strip('px')
               		Bheight = float(Bheight)
                	Bprecent = (Bheight/56) * 100
                	Black_Remaining = round(Bprecent,0)




	if Number_of_Cells == 3:

		message = message + "<tr>"
		Number_of_Cells = 0

	Order_Link = " "

	if Model == "MFC-9340CDW" or Model == "MFC-9330CDW" or Model == "HL-3170CDW series":
		Order_Link = "<a href='https://www.amazon.com/s?k=TN225&i=office-products&ref=nb_sb_noss_2' target='_blank'> Order TN221 </a>"
	if Model == "MFC-L8900CDW series":
		Order_Link = "<a href='https://www.amazon.com/s?k=MFC-L8900CDW+Toner&i=office-products&ref=nb_sb_noss' target='_blank'> Order TN436 </a>"
	if Model == "MFC-L3770CDW series":
		Order_Link = "<a href='https://www.amazon.com/s?k=TN+227&i=office-products&ref=nb_sb_noss_2' target='_blank'> Order TN227 </a>"
	if Model =="MFC-L2750DW series":
		Order_Link = "<a href='https://www.amazon.com/s?k=TN760&i=office-products&ref=nb_sb_noss_2' target='_blank'> Order TN760 </a>"
	if Model =="HL-L5200DW series":
		Order_Link = "<a href='https://www.amazon.com/s?k=TN850&i=office-products&ref=nb_sb_noss_2' target='_blank'> Order TN850 </a>"
	if Model =="MFC-L2740DW series":
		Order_Link = "<a href='https://www.amazon.com/s?k=tn660&i=office-products' target='_blank'> Order TN660 </a>"

	message = message +  "<td><p>Model: " + Model + "</p>"
	message = message +   Office + "</p>"
	message = message +  "<p>IP Address: <a href='http://" + x + "'target='_blank'>"+x+"</a></p>"
	message = message + "<p>=========================</p>"
	message = message + "<p>======Toner Remaining======</p>"
	message = message + "<p>=========================</p><ul>"
	if Black_Remaining is not None:
		if Black_Remaining < 15.0:
			message = message + "<li>Black Toner Remaining: <b class='blinking'>" + str(Black_Remaining) + "</b></li>"
		else:
			message = message + "<li>Black Toner Remaining: " + str(Black_Remaining) + "</li>"
	if Cyan_Remaining is not None:
		if Cyan_Remaining < 15.0:
			message = message + "<li>Cyan Toner Remaining: <b class='blinking'>" + str(Cyan_Remaining) + "</b></li>"
		else:
			message = message + "<li>Cyan Toner Remaining: " + str(Cyan_Remaining) + "</li>"
	if Magenta_Remaining is not None:
		if Magenta_Remaining < 15.0:
			message = message +  "<li>Magenta Toner Remaining: <b class='blinking'>" + str(Magenta_Remaining) + "</b></li>"
		else:
			message = message +  "<li>Magenta Toner Remaining: " + str(Magenta_Remaining) + "</li>"
	if Yellow_Remaining is not None:
		if Yellow_Remaining < 15.0:
			message = message +  "<li>Yellow Toner Remaining: <b class='blinking'>" + str(Yellow_Remaining) + "</b></li>"
		else:
			message = message +  "<li>Yellow Toner Remaining: " + str(Yellow_Remaining) + "</li>"

	message = message + "</ul><p>" + Order_Link + "</p></td>"
	Number_of_Cells = Number_of_Cells + 1
message = message + "<tr><table></body></html>"
write_out.write (message)
write_out.close()
print "Processing Complete"
