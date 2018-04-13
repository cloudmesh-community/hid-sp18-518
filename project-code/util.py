#util.py
#----------
# -*- coding: utf-8 -*-

import yaml
import sys
import logging

#credFile = "./credentials.yml"
credFile = "config/credentials.yml"

try:
    cred = yaml.load(open(credFile))
    #print cred
    azure_tenant_id = cred['azure']['tenant_id']
    azure_subscription_id = cred['azure']['subscription_id']
    azure_key = cred['azure']['key']
    azure_default_region = cred['azure']['DEFAULT_REGION']
    azure_secret = cred['azure']['secret']
#    if azure_tenant_id == "TBD" or azure_subscription_key== "TBD":
#        logging.error('Please save azure credetials in credentials.yml')
#        sys.exit(1)
except:
    logging.error('Please create credentials.yml with credetial info')
    sys.exit(1) 


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


#print getAZUREAccessID()
#print getAZURESecretKey()


