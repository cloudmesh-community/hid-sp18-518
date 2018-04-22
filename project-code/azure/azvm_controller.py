import connexion
import six

from swagger_server.models.azurevm import AZUREVM  # noqa: E501
from swagger_server import util

from azureCompute import createAzureVM, startAzureVM, stopAzureVM, deleteAzureVM,listAzureVM
from json import dumps

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


    :rtype: List[AZUREVM]
    """
    vms = []
    nodes = listAzureVM()
    for node in nodes:
        azvm = AZUREVM( vmname=node.name, 
                      image_name=node.image)
        vms.append(azvm)
    return vms


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
