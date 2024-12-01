#!/bin/bash

# 2024-12-01
# drive backup using rsync
# * primary : primary HDD
# * secondary : back up 1
# 

## example of partial syncs
#rsync -av --delete /Volumes/Primary/Art_Photos/A* /Volumes/Secondary/Art_Photos/ 
#rsync -av --delete /Volumes/Primary/GooglePhotos /Volumes/Secondary/


## sync entire drive
#rsync -av --delete --dry-run --exclude '.*' /Volumes/Primary/ /Volumes/Secondary/ > "$(date +%Y-%m-%d).log"

rsync -av --delete --exclude '.*' /Volumes/Primary/ /Volumes/Secondary/ > "$(date +%Y-%m-%d).log"





