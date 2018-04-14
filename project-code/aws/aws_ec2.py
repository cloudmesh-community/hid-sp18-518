#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 23:24:21 2018

@author: sushant
"""
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
import util

ACCESS_ID = util.getAWSAccessID()
SECRET_KEY = util.getAWSSecretKey()

DEFAULT_SIZE_ID = util.getAWSDefSize()
DEFAULT_REGION = util.getAWSDefRegion()
DEFAULT_AMI = util.getAWSDefAMI()

def getEC2Driver(region):
    cls = get_driver(Provider.EC2)

    if region == "":
        driver = cls(ACCESS_ID, SECRET_KEY)
    else:
        driver = cls(ACCESS_ID, SECRET_KEY,region=region)
    
    return driver

def createVM (vmname, vmsize, vmimage, vmregion):
            
    if (vmregion == ""):
        vmregion = DEFAULT_REGION

    driver = getEC2Driver(vmregion)
    
    sizes = driver.list_sizes()
    images = driver.list_images()
    
    if vmsize == "":
        vmsize = DEFAULT_SIZE_ID
    
    size = [s for s in sizes if s.id == vmsize][0]
    
    image = ""
    if vmimage == "":
        image = images[0]
    else:
        image = [i for i in images if i.id == vmimage][0]

    print("image--",image)
    
    try:
        node = driver.create_node(name=vmname, image=image, size=size)
        print ("node created")
        return node
    except Exception, err:
        print Exception, err
        #print("VM create error:", sys.exc_info()[0])
        return None

def getVMByRegion (vmregion):
    driver = getEC2Driver(vmregion)
    nodes = driver.list_nodes()
    return nodes

def getVMByName (vmname, vmregion):
    nodes = getVMByRegion(vmregion)
    node = [i for i in nodes if i.name == vmname][0]
    return node

def stopVM(node):
    driver = getEC2Driver(DEFAULT_REGION)
    return driver.ex_stop_node(node)
    
def startVM(node):
    driver = getEC2Driver(DEFAULT_REGION)
    return driver.ex_start_node(node)

def terminateVM(node):
    driver = getEC2Driver(DEFAULT_REGION)
    return driver.destroy_node(node)


#node = createVM("myVM","",DEFAULT_AMI,DEFAULT_REGION)
#print ("node-", node)

#nodes = getVMByRegion(DEFAULT_REGION)
#print nodes
"""
for node in nodes:
    print node.name
    print node.state
    print node.size
    print node.image
    print node.driver
    #print ("start node--->",startVM(node))
"""
