#Azure compute
#create VM
curl -X GET "http://localhost:8080/cloudmesh/compute/azure/createvm?name=AZ1&size=Standard_B1s&image_name=UbuntuServer&resource_group=libcloud&storage_account=libclouddiag209&network_intf=libcloud-vnet&blob_container=test123" -H  "accept: application/json"

#stop VM
curl -X GET "http://localhost:8080/cloudmesh/compute/azure/stopvm?vmname=AZ1&resource_group=libcloud" -H  "accept: application/json"

#start VM
curl -X GET "http://localhost:8080/cloudmesh/compute/azure/startvm?vmname=AZ1&resource_group=libcloud" -H  "accept: application/json"

#delete VM
curl -X GET "http://localhost:8080/cloudmesh/compute/azure/deletevm?vmname=AZ1&resource_group=libcloud" -H  "accept: application/json"

#listvm
curl -X GET "http://localhost:8080/cloudmesh/compute/azure/listvm" -H "accept: application/json"

#Azure storage
#create vol
curl -X GET "http://localhost:8080/cloudmesh/storage/azure/createVol?volname=newvol1&volsize=1&location=eastus&resource_group=libcloud&ex_account_type=Standard_LRS" -H  "accept: application/json"

#create vol snap
curl -X GET "http://localhost:8080/cloudmesh/storage/azure/createVolSnap?volname=newvol&snapname=newsnap&resource_group=libcloud&location=eastus" -H  "accept: application/json"

#delete vol snap
curl -X GET "http://localhost:8080/cloudmesh/storage/azure/deleteVolSnap?snapname=ttestsnap" -H  "accept: application/json"

#delete vol
curl -X GET "http://localhost:8080/cloudmesh/storage/azure/deleteVol?volname=newvol" -H  "accept: application/json"

