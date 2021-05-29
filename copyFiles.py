"""
Using Google Takeout to download photos from Google Photos we get album names as directories. Sometimes it's needed to
explode all files in those directories into one folder, for example so that they can be used for import in another systems.
This script helps with this task.
"""

import os
import sys
import shutil

from pathlib import Path

if len(sys.argv) != 2:
    print("Source directory of photos is required")
    exit()

source = sys.argv[1]

target = Path.home().joinpath("photos3")

if(not target.exists()):
    os.mkdir(target)

count = 0
for root, dirs, files in os.walk(source):
    for file in files:
        if(file.lower().endswith("jpg")):
            count += 1

            """
            In different sub-folders we can have same file names, for example 2018/DS01.JPG and 2019/DS01.JPG.
            If such case was encountered, first DS01.JPEG would be copied, and then second one would override it. To
            fix this brake up file name and insert count after its name, so the new file names becomes DS01-1.JPG and
            DS01-23.JPG
            """
            targetFile = target.joinpath(file[:-4] + "-" + str(count) + ".jpg")

            shutil.copy(os.path.join(root, file), targetFile)

print("\n\rCopied {fileCount} to directory {targetDir}".format(fileCount=count, targetDir=target))
