import json
import urllib.request
import requests
import os

tempDir = "./temp/"

##file load and save stuff

def fileSave(fileName,config):
    print("Saving")
    f = open(fileName, 'w') #opens the file your saving to with write permissions
    f.write(json.dumps(config,sort_keys=True, indent=4 ) + "\n") #writes the string to a file
    f.close() #closes the file io

def fileLoad(fileName):#loads files
    with open(fileName, 'r') as handle:#loads the json file
        config = json.load(handle) 
    return config

#download
def download(url,fileName,directory): #downloads the file given
    # Download the file from `url` and save it locally under `file_name`:
    urllib.request.urlretrieve(url,"{0}{1}".format(directory,fileName))
    print("done")

#



config = fileLoad("config.json") #loads the config file

#check if the temp directory exists
if os.path.isdir(tempDir) == False:
    os.mkdir(tempDir)


mainData = config["data"]

for key,val in mainData.items(): #Looking through the data dictionary and cycling through it
    if val["type"] == "github": #if its a file from github where the latest release downloads the json formatting for stuff
        r = requests.get(val["url"])
        data = r.json() #outputs the format as json
        for key in data["assets"]: #sorts through the json till it finds the download that matches the file we want
            if key["name"] == val["file"]:
                download(key["browser_download_url"],val["fileName"],tempDir)
        #fileSave(val["fileName"],data["assets"])
    else: #regular download
        download(val["url"],val["fileName"],tempDir)
    source="{0}{1}".format(tempDir,val["fileName"])
    destination="Z:\\User\\Documents\\My_Files\\Development_Stuff\\Python\\downloadTests\\downloaded\\{0}".format(val["fileName"])
    if os.path.isfile(destination) == True: #checks to see if the file already exists
        os.remove(destination)#if so delete the file
    os.rename(source,destination)#moves the output file to the correct location.

        
