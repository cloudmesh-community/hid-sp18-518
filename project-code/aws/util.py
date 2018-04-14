# -*- coding: utf-8 -*-

import yaml
import sys
import logging

#credFile = "credentials.yml"
credFile = "config/credentials.yml"

try:
    cred = yaml.load(open(credFile))
    aws_access_id = cred['aws']['ACCESS_ID']
    aws_secret_key = cred['aws']['SECRET_KEY']
    aws_default_size_id = cred['aws']['DEFAULT_SIZE_ID']
    aws_default_region = cred['aws']['DEFAULT_REGION']
    aws_default_ami = cred['aws']['DEFAULT_AMI']
    download_dir = cred['aws']['DOWNLOAD_DIR']
    if aws_access_id == "TBD" or aws_secret_key=="TBD":
        logging.error('Please save aws credetials in credentials.yml')
        sys.exit(1)
except OSError:
    logging.error('Please create credentials.yml with credential info')
    sys.exit(1) 


def getAWSAccessID():
    return aws_access_id

def getAWSSecretKey():
    return aws_secret_key

def getAWSDefSize():
    return aws_default_size_id

def getAWSDefRegion():
    return aws_default_region

def getAWSDefAMI():
    return aws_default_ami

def getDownloadDir():
    return download_dir

