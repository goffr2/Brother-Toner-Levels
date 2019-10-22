# Brother-Toner-Levels
Scripts and files used to generate a html page of Brother Toner Levels and thier locations. 
This  script is Designed to  find the toner levels of brother printers.
It finds the toner levels by scrapping the webpage of the printers and 
then formats and displays that text in a webpage. 
  
To use this script install python, pip, and use pip to install requests,
urllib3, and bs4. Make sure your ip_list.txt file is in the same Directory
as your script as well as the Monochrome_Printers.list and Color_Printers.list files.
The script will then generate a HTML page and save the page 
in the Directory you have listed in the path.txt file or if that file  does 
not exist it will place it in the same directory as the python script.
 
The following models have been tested in my environment

- MFC-9340CDW
- MFC-L8900CDW series
- MFC-9330CDW
- MFC-L3770CDW series
- MFC-L2750DW series
- HL-3170CDW series
- HL-L5200DW series
- MFC-L2740DW series
- DCP-L2540DW series

More models can be added to the script as needed
If you have a model you want added please send me the
toner status page
