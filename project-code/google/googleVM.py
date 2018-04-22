#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 22:41:40 2018

@author: sushant
"""
import sys
import util

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver


service_account=util.getGoogleSA()
key_file_name="config/"+util.getGoogleKeyFile()
project=util.getGoogleProject()

def getGoogleDriver():
    ComputeEngine = get_driver(Provider.GCE)

    driver = ComputeEngine(service_account,key_file_name,project=project)
                          

#    driver = ComputeEngine('libcloud@bigdata-200417.iam.gserviceaccount.com',
 #                          'BigData-b66aec8f211e.json',
  #                         project='bigdata-200417')
    return driver


# Note that the 'PEM file' argument can either be the JSON format or
# the P12 format.

def createGoogleVM(vmname, size, image, location):
    driver = getGoogleDriver()
    try:
        node = driver.create_node(vmname, size, image, 
                       ex_disk_auto_delete=True,ex_network='default', 
                       ex_subnetwork=None,location=location)
        print ("vm created")
        return node
    except Exception, err:
        print Exception, err
        #print("VM create error:", sys.exc_info()[0])
        return None

def stopVM(vmname, location):
    driver = getGoogleDriver()
    try:
        driver.ex_stop_node(driver.ex_get_node(vmname, zone=location))
        print ("VM Stopped")
    except:
		print("Unexpected error occurred, contact cloud admin", sys.exc_info())
        
def startVM(vmname):
    driver = getGoogleDriver()
    try:
        driver.ex_start_node(driver.ex_get_node(vmname))
        print ("VM Started")
    except:
		print("Unexpected error occurred, contact cloud admin", sys.exc_info())


def deleteVM(vmname, location):
    driver = getGoogleDriver()
    try:
        driver.destroy_node(driver.ex_get_node(vmname, zone=location), 
                    destroy_boot_disk=False)
        print ("VM Deleted")
    except:
		print("Unexpected error occurred, contact cloud admin", sys.exc_info())

def listVM():
    driver = getGoogleDriver()
    try:
        return driver.list_nodes(ex_zone='all',ex_use_disk_cache=True)
    except:
		print("Unexpected error occurred, contact cloud admin", sys.exc_info())


