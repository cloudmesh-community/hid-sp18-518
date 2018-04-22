import connexion
import six

from swagger_server.models.googlevm import GOOGLEVM  # noqa: E501
from swagger_server import util

from googleVM import createGoogleVM, stopVM, startVM, deleteVM,listVM
from json import dumps

def create_google_vm(name, size, image_name, location):  # noqa: E501
    """create_google_vm

    Create a new VM # noqa: E501

    :param name: Name of VM
    :type name: str
    :param size: Size of VM
    :type size: str
    :param image_name: Source Image to create VM
    :type image_name: str
    :param location: Name of the location/region
    :type location: str

    :rtype: GOOGLEVM
    """
    out=createGoogleVM(name,size,image_name,location)
    #print out
    return dumps("VM Created Successfully")


def delete_google_vm(vmname, location):  # noqa: E501
    """delete_google_vm

    Deletes the virtual machine # noqa: E501

    :param vmname: Name of the VM
    :type vmname: str
    :param location: Name of the vm location
    :type location: str

    :rtype: GOOGLEVM
    """
    deleteVM(vmname,location)
    return 'VM deleted Successfully!'


def list_google_vm():  # noqa: E501
    """list_google_vm

    List all the VM&#39;s # noqa: E501


    :rtype: List[GOOGLEVM]
    """
    vms = []
    nodes = listVM()
    for node in nodes:
        gglvm = GOOGLEVM( vmname=node.name, 
                      image_name=node.image)
        vms.append(gglvm)
    return vms


def start_google_vm(vmname):  # noqa: E501
    """start_google_vm

    Starts the virtual machine # noqa: E501

    :param vmname: Name of the VM
    :type vmname: str

    :rtype: GOOGLEVM
    """
    startVM(vmname)
    return 'VM Started Successfully!'


def stop_google_vm(vmname, location):  # noqa: E501
    """stop_google_vm

    Stops the virtual machine # noqa: E501

    :param vmname: Name of the VM
    :type vmname: str
    :param location: Name of the VM location
    :type location: str

    :rtype: GOOGLEVM
    """
    stopVM(vmname,location)
    return 'VM Stopped Successfully!'
