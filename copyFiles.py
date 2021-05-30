"""
Using Google Takeout to download photos from Google Photos we get album names as directories with file in them. Sometimes it's needed
explode all files in those directories into one directory, for example so that they can be used for import to another systems.
This script helps with this task.
"""

import os
import sys
from pathlib import Path
import shutil

from pathlib import Path

if len(sys.argv) != 3:
    print("Source and target directories are required")
    exit()

source = Path(sys.argv[1])
target = Path(sys.argv[2])

if not os.path.isdir(source):
    os.mkdir(source)

if not os.path.isdir(target):
    os.mkdir(target)

print("source directory: " + str(source))
print("target directory: " + str(target))
print()

count = 0

for root, dirs, files in os.walk(source):
    for file in files:
        if(file.lower().endswith("jpg") or file.lower().endswith("mp4")):
            count += 1

            """
            In different sub-folders we can have same file names, for example 2018/DS01.JPG and 2019/DS01.JPG.
            If such case was encountered, first DS01.JPEG would be copied, and then second one would override it. To
            fix this brake up file name and insert count after its name, so the new file names becomes DS01-1.JPG and
            DS01-23.JPG
            """

            targetFile = target.joinpath(file[:-4] + "-" + str(count) + ".mp4")

            if file.lower().endswith("jpg"):
                targetFile = target.joinpath(file[:-4] + "-" + str(count) + ".jpg")

            print(targetFile)

            shutil.copy(os.path.join(root, file), targetFile)

print("\n\rCopied {fileCount} to directory {targetDir}".format(fileCount=count, targetDir=target))
