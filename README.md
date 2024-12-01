# photo_management

The goal is to archive my personal and family photos, 

## dependency

* sigal static photo generator https://sigal.saimon.org/en/latest/  
* bash
* rsync

### scripts

* sigal.conf.art.py	: sigal configuration files
* sigal.conf.google.py : sigal configuration files
* sigal.conf.family.py : sigal configuration files
* update_gallery.sh : shell script to run for above

* clean_up.py  : clean up redundant, or garbage files		 	
* duplicate.sh : rsync code to copy back up of the drive

## Workflow

1. Clean up garbage files using `clean_up.py`
1. run `update_gallery.sh` to update photo gallery
1. run `duplicate.sh` to mirror `primary` to `secondary` or `tertiary`
