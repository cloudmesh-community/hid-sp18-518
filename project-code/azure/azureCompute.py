import sys
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

from libcloud.compute.base import Node, NodeDriver, NodeLocation, NodeSize

import util

tenant_id=util.getAZUREtenantID()
subscription_id=util.getAZURESubscriptionid()
key=util.getAZUREkey()
secret=util.getAZUREsecret()
region=util.getAZUREDefRegion()

cls = get_driver(Provider.AZURE_ARM)
driver = cls(tenant_id=tenant_id,
         subscription_id=subscription_id,
         key=key, secret=secret,region=region)



def createAzureVM(vmname,vmsize,image_name,resource_group,storage_account,nw_intf,blob_container): 

#print region

	urn='Canonical:UbuntuServer:16.04-LTS:latest'

	image=driver.get_image(urn, location=None)

	print image

	vmSize = NodeSize('Standard_B1s','Standard_B1s',1,127,'None','0.0211',1,'Shared')

	try:

		#driver.create_node(auth='',name=vmname,size=vmSize,image=image,location=None,ex_resource_group='libcloud',ex_storage_account='libclouddiag209',ex_network='libcloud-vnet',ex_blob_container='test123')
		driver.create_node(auth='',name=vmname,size=vmSize,image=image,location=None,ex_resource_group=resource_group,ex_storage_account=storage_account,ex_network=nw_intf,ex_blob_container=blob_container)
	#nic=driver.ex_create_network_interface('libcloudVM-net', subnet='10.0.0.0',resource_group='libcloud', location=None)
		print("Virtual Machine created Successfully!")
		#return "Virtual Machine created Successfully!"
	except:
		print("Unexpected error occurred, contact cloud admin", sys.exc_info())



def startAzureVM(vmname,resource_group):

	nodefullStr='/subscriptions/'+subscription_id+'/resourceGroups/'+resource_group+'/providers/Microsoft.Compute/virtualMachines/'+vmname

	try:
		nodename=driver.ex_get_node(nodefullStr)
		driver.ex_start_node(nodename)
		print("Virtual Machine started Successfully!")
	except:
		print("Unexpected error occurred, contact cloud admin", sys.exc_info())


def stopAzureVM(vmname,resource_group):

	nodefullStr='/subscriptions/'+subscription_id+'/resourceGroups/'+resource_group+'/providers/Microsoft.Compute/virtualMachines/'+vmname

	#print nodefullStr

	try:
		nodename=driver.ex_get_node(nodefullStr)
		#print nodename
		driver.ex_stop_node(nodename)
		print("Virtual Machine stopped successfully!")
	except:
		print("Unexpected error occurred, contact cloud admin", sys.exc_info())


def deleteAzureVM(vmname,resource_group):
        nodefullStr='/subscriptions/'+subscription_id+'/resourceGroups/'+resource_group+'/providers/Microsoft.Compute/virtualMachines/'+vmname

	try:
		nodename=driver.ex_get_node(nodefullStr)
		driver.destroy_node(nodename)
		print("Virtual Machine deleted Successfully!")
	except:
		print("Unexpected error occurred, contact cloud admin", sys.exc_info())


def listAzureVM():

        try:
		return driver.list_nodes(ex_resource_group=None, ex_fetch_nic=True, ex_fetch_power_state=True)
        except:
                print("Unexpected error occurred, contact cloud admin", sys.exc_info())


