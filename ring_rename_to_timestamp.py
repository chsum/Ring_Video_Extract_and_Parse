# Rename bulk downloaded Ring videos to include a human readable timestamp 
#
# Using code provided in:
#     (1) Recursively iterated over folders - https://stackoverflow.com/questions/2212643/python-recursive-folder-read 
#     (1.1) Specificially, this response - https://stackoverflow.com/questions/2212643/python-recursive-folder-read/62814658#62814658
#     (2) Get directory from full file path - https://www.delftstack.com/howto/python/get-directory-from-path-in-python/
#     (3) Covert obfuscated timestamp in Bulk ring downloads to %Y-%m-%d_%H-%M-%S https://community.ring.com/t/how-to-interpret-the-timestamp-in-filename-in-downloaded-files/13514/3
#         See also : https://community.ring.com/t/rename-downloaded-ring-videos-to-include-timestamp/55425
#     (4) rename, ensuring we handle any duplicates https://stackoverflow.com/questions/13852700/create-file-but-if-name-exists-add-number


# import required modules
from os import listdir
from os.path import isfile, join
import datetime
import os
import zipfile
import glob
from pathlib import Path

def ConvertDingIdToDateTime(dingId):    
  bits = format(dingId, '0>42b')
  MSB = bits[0:31]
  dingDateTime = datetime.datetime.fromtimestamp(int(MSB,2))

  return dingDateTime

print("here")

refnum = "12345" # to add to front of file as a prefix
root_dir = "D:\\Folder\\SubFolder_extracted\\"  # Make sure this path contains the videos you want to convert the filenames of


for filepath in glob.iglob(root_dir + '**/**', recursive=True):
     #print(filepath)
     dirname = os.path.dirname(filepath) # https://www.delftstack.com/howto/python/get-directory-from-path-in-python/

     f = os.path.basename(filepath) # Extract filename from filepath - https://www.delftstack.com/howto/python/get-directory-from-path-in-python/
     #print(f)

     # only files 
     if isfile(filepath):

         # only files starting with Ring_
         if "Ring_" in f:
             # Assumes files are in this format: Ring_542630117_2003_7087594292252300189.mp4   
             # Removes everything before the third underscore
             # Removes everything after the .
             # Converts datetime to string in yyyy-mm-dd_hh_mm_ss format
             # Prepends path and appends .mp4 extension
             old_file_name = filepath
             new_file_name_start = f.split('_', 3)[0] + '_' + f.split('_', 3)[1] + '_' + f.split('_', 3)[2] 
             new_file_name_start = new_file_name_start.replace("Ring","CCTV")
             try:
                 converteddate = ConvertDingIdToDateTime(int(f.split('_', 3)[-1].split('.', 1)[0])).strftime("%Y-%m-%d_%H-%M-%S")
             except:
                 print("error converting filename")

             new_file_name = dirname + '\\' + refnum + '_' + converteddate + '_' + new_file_name_start + '.mp4'
             #print(converteddate)

             root, ext = os.path.splitext(new_file_name)

             i = 0
             while os.path.exists(new_file_name):
                 print("**************** found duplicated file ****************")
                 i += 1
                 # print root and ext
                 # of the specified path
                 #print("root part of '% s':" % root)
                 #print("ext part of '% s':" % ext)
                 new_file_name = root + '_' + str(i) + ext               
                 print("updated new filename:" + new_file_name)

             print("old file name:" + old_file_name)
             print("new filename:" + new_file_name)

             os.rename(old_file_name, new_file_name)  
