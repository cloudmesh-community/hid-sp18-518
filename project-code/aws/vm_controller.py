import connexion
import six

from swagger_server.models.awsvm import AWSVM  # noqa: E501
from swagger_server import util
import aws_ec2

def create_vm(body):  # noqa: E501
    """create a new ec2 vm instance

     # noqa: E501

    :param body: VM object that needs to be added
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = AWSVM.from_dict(connexion.request.get_json())  # noqa: E501
        
    node = aws_ec2.createVM (body.name, body.size, body.image, body.region)
    
    if node is None:
        return "VM Creation Failed"
    else:
        return 'VM Created'


def get_vm_by_name(vmname, region):  # noqa: E501
    """Find vm by Name

    Returns a single vm # noqa: E501

    :param vmname: vm name
    :type vmname: str
    :param region: region
    :type region: str

    :rtype: AWSVM
    """
    if region == "" or vmname == "":
        return "Please provide region and vmname"
    else:
        node = aws_ec2.getVMByName(vmname,region)
        awsvm = AWSVM( vm_id=node.id, 
                          name=node.name, 
                          image=node.image, 
                          region=region, 
                          size=node.size, 
                          status=node.state)
        return awsvm
 

def start_vm(vmname, region):  # noqa: E501
    """start ec2 vm instance

     # noqa: E501

    :param vmname: vm name
    :type vmname: str
    :param region: region
    :type region: str

    :rtype: None
    """
    if region == "" or vmname == "":
        return "Please provide region and vmname"
    else:
        node = aws_ec2.getVMByName(vmname,region)
        isStarted = aws_ec2.startVM(node)
        if isStarted:
            return "VM Started"
        else:
            return "VM already running or terminated"


def stop_vm(vmname, region):  # noqa: E501
    """stop ec2 vm instance

     # noqa: E501

    :param vmname: vm name
    :type vmname: str
    :param region: region
    :type region: str

    :rtype: None
    """
    if region == "" or vmname == "":
        return "Please provide region and vmname"
    else:
        node = aws_ec2.getVMByName(vmname,region)
        isStoped = aws_ec2.stopVM(node)
        if isStoped:
            return "VM Stopped"
        else:
            return "VM already stopped or terminated"


def terminate_vm(vmname, region):  # noqa: E501
    """terminate ec2 vm instance

     # noqa: E501

    :param vmname: vm name
    :type vmname: str
    :param region: region
    :type region: str

    :rtype: None
    """
    if region == "" or vmname == "":
        return "Please provide region and vmname"
    else:
        node = aws_ec2.getVMByName(vmname,region)
        isTerminated = aws_ec2.terminateVM(node)
        if isTerminated:
            return "VM Terminated"
        else:
            return "VM already terminated"

def find_by_region(region):  # noqa: E501
    """find_by_region

    Returns list on VMs # noqa: E501

    :param region: region
    :type region: str

    :rtype: List[AWSVM]
    """
    vms = []
    if region == "":
        return "Please provide AWS EC2 region"
    else:
        nodes = aws_ec2.getVMByRegion(region)
        for node in nodes:
            awsvm = AWSVM( vm_id=node.id, 
                          name=node.name, 
                          image=node.image, 
                          region=region, 
                          size=node.size, 
                          status=node.state)
            vms.append(awsvm)
        return vms
