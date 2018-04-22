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
    
    
    azure_tenant_id = cred['azure']['tenant_id']
    azure_subscription_id = cred['azure']['subscription_id']
    azure_key = cred['azure']['key']
    azure_default_region = cred['azure']['DEFAULT_REGION']
    azure_secret = cred['azure']['secret']

    google_service_account_name = cred['google']['service_account_name']
    google_key_file_name = cred['google']['key_file_name']
    google_project = cred['google']['project']

    
    if aws_access_id == "TBD" or aws_secret_key=="TBD":
        logging.error('Please save aws credetials in credentials.yml')
        sys.exit(1)
        
    if azure_tenant_id == "TBD" or azure_subscription_id == "TBD":
        logging.error('Please save azure credetials in credentials.yml')
        sys.exit(1)

    if google_service_account_name == "TBD" or google_key_file_name=="TBD" or google_project == "TBD":
        logging.error('Please save google cloud credetials in credentials.yml')
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

def getAZUREtenantID():
    return azure_tenant_id

def getAZURESubscriptionid():
    return azure_subscription_id

def getAZUREkey():
    return azure_key

def getAZUREDefRegion():
    return azure_default_region

def getAZUREsecret():
    return azure_secret

def getGoogleSA():
    return google_service_account_name

def getGoogleKeyFile():
    return google_key_file_name

def getGoogleProject():
    return google_project


