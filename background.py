# Wallpaper changer on Mac
from requests import get
from datetime import datetime
from urllib.request import urlopen
from getpass import getuser
from appscript import *


# Open the specified URL and get the URL after redirects 
response = urlopen('https://source.unsplash.com/1440x900/').geturl() # you may specify your own resolutions where 1440x900 is 
url = response
response = get(url)                       # get request
time = str(datetime.now())                # get current computer time 
username = getuser()                      # get current username on machine

# If the get request was successful, save the image as the current time in jpg format in the downloads directory
if (response.status_code == 200):
    with open('/Users/' + username + '/Downloads/' + time + '.jpg', 'wb') as f:
        f.write(response.content)

    # Set the desktop background picture to the saved image
    app('Finder').desktop_picture.set(mactypes.File('/Users/' + username + '/Downloads/' + time + '.jpg'))


