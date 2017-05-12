"""
This is script that I replaced the paths with place holders that will download a 
tarball of a data file and extract it to a directory of the user's choosing
This script orginally comes from "Hands On Machine Learning with Scikit-Learn and Tensorflow"
Published by O'Reilly
Again I just replaced all the paths and urls with placeholder in order for other users to 
modify the above to thier needs
"""

import os 
import tarfile
from six.moves import urllib #This library is used as a combatibility wrapper between Python 2 and 3

DOWNLOAD_ROOT = <Url_where the _tarball_is_being_downloaded_from>
HOUSING_PATH = <Directory_where_file_will_extracted_to>
HOUSING_URL = <This varible was the addition of the url and local dir.> #You might not need this depending on your project

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedir(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz") #Join one or more path components intelligently.
    urllib.request.urlretrieve(housing_url, tgz_path) #Copy a network object denoted by a URL to a local file
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()
