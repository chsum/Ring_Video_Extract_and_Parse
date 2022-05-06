# Extract contents of all .zip files in folders and sub-folders
# created to extract contents of Ring video downloands
#
# Using code provided in:
#     (1) Recursively iterated over folders - https://stackoverflow.com/questions/2212643/python-recursive-folder-read
#     (2) Get directory from full file path - https://www.delftstack.com/howto/python/get-directory-from-path-in-python/
#     (3) Extract contents of zip files - https://stackoverflow.com/questions/3451111/unzipping-files-in-python

# import required modules

import datetime
import os
import zipfile
import glob
from pathlib import Path


print("start")

# https://stackoverflow.com/questions/2212643/python-recursive-folder-read
root_dir = "D:\\Folder\\SubFolder\\" 






# root_dir needs a trailing slash (i.e. /root/dir/)
for filename in glob.iglob(root_dir + '**/*.zip', recursive=True):
     dirname = os.path.dirname(filename) # https://www.delftstack.com/howto/python/get-directory-from-path-in-python/
     print(filename)

     dirname_out = dirname + '_out'  # create an folder to dump extracted files to.

     # extract contents of zip - https://stackoverflow.com/questions/3451111/unzipping-files-in-python
     with zipfile.ZipFile(filename, 'r') as zip_ref:
         zip_ref.extractall(dirname_out)


print("done")
