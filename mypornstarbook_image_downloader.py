#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, os, zipfile, shutil, sys, datetime
from pattern.web import URL, DOM


#target url. 1. choose a star. 2. choose a catagory e.g. Softcore, hardocre. copy and paste the url here:

#Examples    
#url=URL("https://www.mypornstarbook.net/pornstars/a/abella_danger/index.php")
#url=URL("https://www.mypornstarbook.net/categories/blowjob/index.php")


url=URL("https://www.mypornstarbook.net/pornstars/n/nicole_aniston/softcore.php")


#this is the path to the working directory. for Windows, C:\\path\\to\\dir\\. THE TRAILING '/' is required 
w_dir = '/path/to/the/working/directory/'

#THATS IT. NOWTHING ELSE TO CHANGE

isExist = os.path.exists(w_dir)
if isExist is False:
    print('directory not present/accessable. Exiting program')
    sys.exit()
    
gal_dir = w_dir + 'gallery'
if isExist is False:
    os.mkdir(gal_dir)
else:
    print('directory exists, creating new directory' )
    gal_dir = w_dir + 'gallery'+ str(datetime.date.today())
    os.mkdir(gal_dir)

rename_dir = w_dir + 'images'

zfile=w_dir +'data.zip'

counter = 0

dom = DOM(url.download())

for anchor in dom.by_tag('a'):
    if "gallery" in anchor.href:
        counter += 1  
        os.chdir(w_dir)
        dl_link = anchor.href.replace("index.php", "images.zip")
        print(dl_link)
        myfile = requests.get(dl_link)
        open(zfile, 'wb').write(myfile.content)
        
        z = zipfile.ZipFile(zfile) # create zipfile object       
        z.extractall(w_dir) # extract file to dir
        z.close() # close file
        os.remove(zfile) # delete zipped file
        #Now rename files
        os.chdir(rename_dir)
        for file in os.listdir():
           dst = str(counter)+"_"+file
           os.rename(file, dst)
        
#       now move files
        for file2 in os.listdir():
            shutil.move(file2, gal_dir) 

os.rmdir(rename_dir)
