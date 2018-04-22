import connexion
import six

from swagger_server.models.azurestorage import AZURESTORAGE  # noqa: E501
from swagger_server import util
from azureStorage import createAzureVol, createAzureVolSnap, destroyAzureVol, destroyAzureVolSnap
from json import dumps

def create_vol(volname, volsize, location, resource_group, ex_account_type):  # noqa: E501
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


def create_vol_snap(volname, snapname, resource_group, location):  # noqa: E501
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
    destroyAzureVolSnap(snapname, resource_group)
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
    destroyAzureVol(volname, resource_group)
    return dumps("Volume Deleted Successfully")
