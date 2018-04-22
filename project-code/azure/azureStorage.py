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



def createAzureVol(volname,volsize,location,resource_group,ex_account_type): 

	try:

		loc=driver._to_location(location)
		driver.create_volume(volsize, volname, location=loc, snapshot=None, ex_resource_group=resource_group, ex_account_type=ex_account_type, ex_tags=None)
		print("Storage volume created Successfully!")
	except:
		print("Unexpected error occurred, contact cloud admin", sys.exc_info())


def createAzureVolSnap(snapname,volname,resource_group,location):

        try:
		volid='/subscriptions/'+subscription_id+'/resourceGroups/'+resource_group+'/providers/Microsoft.Compute/disks/'+volname

                volume=driver.ex_get_volume(volid)
                loc=driver._to_location(location)
                driver.create_volume_snapshot(volume=volume,name=snapname,location=loc,ex_resource_group=resource_group,ex_tags=None)
                print("Storage volume snapshot created Successfully!")
        except:
                print("Unexpected error occurred, contact cloud admin", sys.exc_info())



def destroyAzureVol(volname,resource_group):

	try:
                volid='/subscriptions/'+subscription_id+'/resourceGroups/'+resource_group+'/providers/Microsoft.Compute/disks/'+volname

                volume=driver.ex_get_volume(volid)

		driver.destroy_volume(volume)
		print("Storage volume destroyed Successfully!")
	except:
		print("Unexpected error occurred, contact cloud admin", sys.exc_info())

def destroyAzureVolSnap(snapname,resource_group):

        try:
                snapid='/subscriptions/'+subscription_id+'/resourceGroups/'+resource_group+'/providers/Microsoft.Compute/disks/'+snapname

                snap=driver.ex_get_snapshot(snapid)

                snapshot=driver.ex_get_snapshot(snap)
                driver.destroy_volume(snapshot)
                print("Storage snapshot destroyed Successfully!")
        except:
                print("Unexpected error occurred, contact cloud admin", sys.exc_info())


