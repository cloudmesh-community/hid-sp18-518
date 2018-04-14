import connexion
import six

from swagger_server.models.azurestorage import AZURESTORAGE  # noqa: E501
from swagger_server.models.azurevm import AZUREVM  # noqa: E501
from swagger_server import util

from azureCompute import createAzureVM, startAzureVM, stopAzureVM, deleteAzureVM,listAzureVM
from json import dumps
from azureStorage import createAzureVol, createAzureVolSnap, destroyAzureVol, de
stroyAzureVolSnap



def create_vol(volname, volsize, loation, resource_group, ex_account_type):  # noqa: E501
    """create_vol

    Create Azure Storage Vol # noqa: E501

    :param volname: Name of Storage Volume
    :type volname: str
    :param volsize: Size of Storage Vol
    :type volsize: str
    :param loation: Locaton or region
    :type loation: str
    :param resource_group: Name of the resource group
    :type resource_group: str
    :param ex_account_type: Storage Account Type
    :type ex_account_type: str

    :rtype: AZURESTORAGE
    """
    #return 'do some magic!'
    createAzureVol(volname,volsize,location,resource_group,ex_account_type)
    return dumps("Volume Snapshot Created Successfully")



def create_vol_snap(volname, snapname, resource_group, loation):  # noqa: E501
    """create_vol_snap

    Create Azure Storage Vol Snapshot # noqa: E501

    :param volname: Name of Storage Volume
    :type volname: str
    :param snapname: Name of Storage Vol Snapshot
    :type snapname: str
    :param resource_group: Name of Resource Group
    :type resource_group: str
    :param loation: Locaton or region
    :type loation: str

    :rtype: AZURESTORAGE
    """
    #return 'do some magic!'
    createAzureVolSnap(snapname,volname,resource_group,location)
    return dumps("Volume Snapshot Created Successfully")


def createvm(name, size, image_name, resource_group, storage_account, network_intf, blob_container):  # noqa: E501
    """createvm

    Create a new VM # noqa: E501

    :param name: Name of VM
    :type name: str
    :param size: Size of VM
    :type size: str
    :param image_name: Source Image to create VM
    :type image_name: str
    :param resource_group: Name of the resource group
    :type resource_group: str
    :param storage_account: Storage Account
    :type storage_account: str
    :param network_intf: Network interface name
    :type network_intf: str
    :param blob_container: Storage blob container name
    :type blob_container: str

    :rtype: AZUREVM
    """
    out=createAzureVM(name,size,image_name,resource_group,storage_account,network_intf,blob_container)
    #print out
    return dumps("VM Created Successfully")
    #return dumps(out)
    #return 'do some magic!'


def del_volsnap(snapname, resource_group):  # noqa: E501
    """del_volsnap

    Create Azure Storage Vol # noqa: E501

    :param snapname: Name of Storage Volume Snapshot
    :type snapname: str
    :param resource_group: Name of Resource Group
    :type resource_group: str

    :rtype: AZURESTORAGE
    """
    #return 'do some magic!'
    destroyAzureVolSnap(snapname)
    return dumps("Volume Snapshot Deleted Successfully")


def delete_vol(volname, resource_group):  # noqa: E501
    """delete_vol

    Create Azure Storage Vol # noqa: E501

    :param volname: Name of Storage Volume
    :type volname: str
    :param resource_group: Name of Resource Group
    :type resource_group: str

    :rtype: AZURESTORAGE
    """
    #return 'do some magic!'
    destroyAzureVol(volname)
    return dumps("Volume Deleted Successfully")


def deletevm(vmname, resource_group):  # noqa: E501
    """deletevm

    Deletes the virtual machine # noqa: E501

    :param vmname: Name of the VM
    :type vmname: str
    :param resource_group: Name of the resource group
    :type resource_group: str

    :rtype: AZUREVM
    """
    deleteAzureVM(vmname,resource_group)
    return 'VM deleted Successfully!'


def listvm():  # noqa: E501
    """listvm

    List all the VM&#39;s # noqa: E501


    :rtype: AZUREVM
    """
    return listAzureVM()
    #return 'do some magic!'


def startvm(vmname, resource_group):  # noqa: E501
    """startvm

    Starts the virtual machine # noqa: E501

    :param vmname: Name of the VM
    :type vmname: str
    :param resource_group: Name of the resource group
    :type resource_group: str

    :rtype: AZUREVM
    """
    startAzureVM(vmname,resource_group)
    return 'VM Started Successfully!'


def stopvm(vmname, resource_group):  # noqa: E501
    """stopvm

    Stops the virtual machine # noqa: E501

    :param vmname: Name of the VM
    :type vmname: str
    :param resource_group: Name of the resource group
    :type resource_group: str

    :rtype: AZUREVM
    """
    stopAzureVM(vmname,resource_group)
    return 'VM Stopped Successfully!'
    #return 'do some magic!'

