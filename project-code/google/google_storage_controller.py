import connexion
import six

from swagger_server.models.googlestorage import GOOGLESTORAGE  # noqa: E501
from swagger_server import util

from googleStorage import createVol, createVolSnap, destroyVol, destroyVolSnap
from json import dumps

def create_google_vol(volname, volsize, location):  # noqa: E501
    """create_google_vol

    Create google Storage Vol # noqa: E501

    :param volname: Name of Storage Volume
    :type volname: str
    :param volsize: Size of Storage Vol
    :type volsize: str
    :param location: Locaton or region
    :type location: str

    :rtype: GOOGLESTORAGE
    """
    createVol(volname,volsize,location)
    return dumps("Volume Snapshot Created Successfully")


def create_google_vol_snap(volname, snapname):  # noqa: E501
    """create_google_vol_snap

    Create google Storage Vol Snapshot # noqa: E501

    :param volname: Name of Storage Volume
    :type volname: str
    :param snapname: Name of Storage Vol Snapshot
    :type snapname: str

    :rtype: GOOGLESTORAGE
    """
    createVolSnap(snapname,volname)
    return dumps("Volume Snapshot Created Successfully")


def del_google_volsnap(snapname):  # noqa: E501
    """del_google_volsnap

    Delete google Storage Vol snap # noqa: E501

    :param snapname: Name of Storage Volume Snapshot
    :type snapname: str

    :rtype: GOOGLESTORAGE
    """
    destroyVolSnap(snapname)
    return dumps("Volume Snapshot Deleted Successfully")


def delete_google_vol(volname):  # noqa: E501
    """delete_google_vol

    Delete google Storage Vol # noqa: E501

    :param volname: Name of Storage Volume
    :type volname: str

    :rtype: GOOGLESTORAGE
    """
    destroyVol(volname)
    return dumps("Volume Deleted Successfully")
