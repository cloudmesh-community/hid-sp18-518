#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 23:37:23 2018

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
#    driver = ComputeEngine('libcloud@bigdata-200417.iam.gserviceaccount.com',
 #                          'BigData-b66aec8f211e.json',
  #                         project='bigdata-200417')
    driver = ComputeEngine(service_account,key_file_name,project=project)
    return driver



def createVol(volname,volsize,location):
    driver = getGoogleDriver()
    try:
        driver.create_volume(volsize, volname, location=location, 
                     snapshot=None, image=None, use_existing=True, 
                     ex_disk_type='pd-standard', ex_image_family=None)
        print("Storage volume created Successfully!")
    except:
		print("Unexpected error occurred, contact cloud admin", sys.exc_info())


def createVolSnap(snapname,volname):
    driver = getGoogleDriver()    
    try:
        volume=driver.ex_get_volume(volname)
        driver.create_volume_snapshot(volume,snapname)
        print("Storage volume snapshot created Successfully!")
    except:
        print("Unexpected error occurred, contact cloud admin", sys.exc_info())



def destroyVol(volname):
    driver = getGoogleDriver() 
    try:
        volume=driver.ex_get_volume(volname)
        driver.destroy_volume(volume)
        print("Storage volume deleted Successfully!")
    except:
		print("Unexpected error occurred, contact cloud admin", sys.exc_info())

def destroyVolSnap(snapname):
    driver = getGoogleDriver() 
    try:
        volsnap=driver.ex_get_snapshot(snapname)
        driver.destroy_volume_snapshot(volsnap)
        print("Storage snapshot destroyed Successfully!")
    except:
        print("Unexpected error occurred, contact cloud admin", sys.exc_info())

