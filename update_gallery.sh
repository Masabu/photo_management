#!/bin/bash

ls

#After adapting the configuration to your needs, put your images in a sub-directory and run sigal build <your images directory>.
#The next time you run sigal build, only the new images will be processed. You can use the -f flag to force the reprocessing of all the images or the -a flag to force only the specified matching albums. Images (resp. videos) that are smaller than the size specified by the img_size (resp. video_size) setting will not be resized.

echo "***********************************"
echo "updating Family Photo Library"
echo "***********************************"

/Library/Frameworks/Python.framework/Versions/3.11/bin/sigal build --debug -c sigal.conf.family.py > "$(date +%Y-%m-%d).photo_index.log"


echo "***********************************"
echo "updating Art Photo Library"
echo "***********************************"

/Library/Frameworks/Python.framework/Versions/3.11/bin/sigal build  --debug -c sigal.conf.art.py >> "$(date +%Y-%m-%d).photo_index.log"


echo "***********************************"
echo "updating Google Photo Library"
echo "***********************************"

/Library/Frameworks/Python.framework/Versions/3.11/bin/sigal build --debug -c sigal.conf.google.py  >> "$(date +%Y-%m-%d).photo_index.log"


# example of updating specific folder
# note; if you deleted or re-organized folder, better to also drop the cache in _buit folder then it will rebuild everything

#/Library/Frameworks/Python.framework/Versions/3.11/bin/sigal build -a '2021'



