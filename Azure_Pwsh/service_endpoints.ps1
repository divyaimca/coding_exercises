
#Variables
$region = 'eastus'
$rg = Read-Host -Prompt "Enter resource group name: "
$vnetName = Read-Host -Prompt "Enter virtual network name: "
$credential = Get-Credential -Message "Provide username and password for the VM"
$storage = Read-Host -Prompt "Enter name a unique name for storage account: "
$storageAccountName = $storage + "fxstore"

#Create resource group
New-AzResourceGroup -Name $rg -Location $region

#Create subnet
$workloadSubnet = New-AzVirtualNetworkSubnetConfig `
  -Name "default" `
  -AddressPrefix 192.168.0.0/24

#Create virtual network
$vnet = New-AzVirtualNetwork `
  -ResourceGroupName $rg `
  -Location $region `
  -Name $vnetName `
  -AddressPrefix 192.168.0.0/16 `
  -Subnet $workloadSubnet

#Create VM
New-AzVM -Name "vm-0a" `
    -ResourceGroupName $rg `
    -Location $region `
    -Size 'Standard_B1s' `
    -Image UbuntuLTS `
    -VirtualNetworkName $vnetName `
    -SubnetName "default" `
    -Credential $credential

#Create storage account
New-AzStorageAccount -ResourceGroupName $rg `
  -Name $storageAccountName `
  -Location $region `
  -SkuName Standard_LRS `
  -Kind StorageV2
