# Azure CLI Module Creation Report

## managednetwork

### managednetwork create

create a managednetwork.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--name**|str|The name of the scope assignment to create.|scope_assignment_name|scopeAssignmentName|
|--scope|str|The base resource of the scope assignment to create. The scope can be any REST resource instance. For example, use '/subscriptions/{subscription-id}/' for a subscription, '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}' for a resource group, and '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider}/{resource-type}/{resource-name}' for a resource.|scope|scope|
|--location|str|The geo-location where the resource lives|/location|/location|
|--assigned-managed-network|str|The managed network ID with scope will be assigned to.|/assigned_managed_network|/properties/assignedManagedNetwork|

**Example: ScopeAssignmentsPut**

```
managednetwork create --scope subscriptions/subscriptionC
        --name subscriptionCAssignment
        --assigned-managed-network subscriptions/subscriptionA/resourceGroups/myResourceGroup/providers/Microsoft.ManagedNetwork/managedNetworks/myManagedNetwork
```
### managednetwork update

update a managednetwork.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--name**|str|The name of the scope assignment to create.|scope_assignment_name|scopeAssignmentName|
|--scope|str|The base resource of the scope assignment to create. The scope can be any REST resource instance. For example, use '/subscriptions/{subscription-id}/' for a subscription, '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}' for a resource group, and '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider}/{resource-type}/{resource-name}' for a resource.|scope|scope|
|--location|str|The geo-location where the resource lives|/location|/location|
|--assigned-managed-network|str|The managed network ID with scope will be assigned to.|/assigned_managed_network|/properties/assignedManagedNetwork|
### managednetwork delete

delete a managednetwork.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--name**|str|The name of the scope assignment to create.|scope_assignment_name|scopeAssignmentName|
|--scope|str|The base resource of the scope assignment to create. The scope can be any REST resource instance. For example, use '/subscriptions/{subscription-id}/' for a subscription, '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}' for a resource group, and '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider}/{resource-type}/{resource-name}' for a resource.|scope|scope|

**Example: ScopeAssignmentsDelete**

```
managednetwork delete --scope subscriptions/subscriptionC
        --name subscriptionCAssignment
```
### managednetwork list

list a managednetwork.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|--scope|str|The base resource of the scope assignment to create. The scope can be any REST resource instance. For example, use '/subscriptions/{subscription-id}/' for a subscription, '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}' for a resource group, and '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider}/{resource-type}/{resource-name}' for a resource.|scope|scope|
### managednetwork show

show a managednetwork.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--name**|str|The name of the scope assignment to create.|scope_assignment_name|scopeAssignmentName|
|--scope|str|The base resource of the scope assignment to create. The scope can be any REST resource instance. For example, use '/subscriptions/{subscription-id}/' for a subscription, '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}' for a resource group, and '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider}/{resource-type}/{resource-name}' for a resource.|scope|scope|
## managednetwork managed-network-group

### managednetwork managed-network-group create

create a managednetwork managed-network-group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--managed-network-name**|str|The name of the Managed Network.|managed_network_name|managedNetworkName|
|**--name**|str|The name of the Managed Network Group.|managed_network_group_name|managedNetworkGroupName|
|--location|str|The geo-location where the resource lives|/location|/location|
|--management-groups|list|The collection of management groups covered by the Managed Network|/management_groups|/properties/managementGroups|
|--subscriptions|list|The collection of subscriptions covered by the Managed Network|/subscriptions|/properties/subscriptions|
|--virtual-networks|list|The collection of virtual nets covered by the Managed Network|/virtual_networks|/properties/virtualNetworks|
|--subnets|list|The collection of  subnets covered by the Managed Network|/subnets|/properties/subnets|
|--kind|str|Responsibility role under which this Managed Network Group will be created|/kind|/kind|

**Example: ManagementNetworkGroupsPut**

```
managednetwork managed-network-group create --resource-group myResourceGroup
        --managed-network-name myManagedNetwork
        --name myManagedNetworkGroup1
```
### managednetwork managed-network-group update

update a managednetwork managed-network-group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--managed-network-name**|str|The name of the Managed Network.|managed_network_name|managedNetworkName|
|**--name**|str|The name of the Managed Network Group.|managed_network_group_name|managedNetworkGroupName|
|--location|str|The geo-location where the resource lives|/location|/location|
|--management-groups|list|The collection of management groups covered by the Managed Network|/management_groups|/properties/managementGroups|
|--subscriptions|list|The collection of subscriptions covered by the Managed Network|/subscriptions|/properties/subscriptions|
|--virtual-networks|list|The collection of virtual nets covered by the Managed Network|/virtual_networks|/properties/virtualNetworks|
|--subnets|list|The collection of  subnets covered by the Managed Network|/subnets|/properties/subnets|
|--kind|str|Responsibility role under which this Managed Network Group will be created|/kind|/kind|
### managednetwork managed-network-group delete

delete a managednetwork managed-network-group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--managed-network-name**|str|The name of the Managed Network.|managed_network_name|managedNetworkName|
|**--name**|str|The name of the Managed Network Group.|managed_network_group_name|managedNetworkGroupName|

**Example: ManagementNetworkGroupsDelete**

```
managednetwork managed-network-group delete --resource-group myResourceGroup
        --managed-network-name myManagedNetwork
        --name myManagedNetworkGroup1
```
### managednetwork managed-network-group list

list a managednetwork managed-network-group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--managed-network-name**|str|The name of the Managed Network.|managed_network_name|managedNetworkName|
### managednetwork managed-network-group show

show a managednetwork managed-network-group.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--managed-network-name**|str|The name of the Managed Network.|managed_network_name|managedNetworkName|
|**--name**|str|The name of the Managed Network Group.|managed_network_group_name|managedNetworkGroupName|
## managednetwork managed-network-peering-policy

### managednetwork managed-network-peering-policy create

create a managednetwork managed-network-peering-policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--managed-network-name**|str|The name of the Managed Network.|managed_network_name|managedNetworkName|
|**--name**|str|The name of the Managed Network Peering Policy.|managed_network_peering_policy_name|managedNetworkPeeringPolicyName|
|**--type**|str|Gets or sets the connectivity type of a network structure policy|/type|/properties/type|
|--location|str|The geo-location where the resource lives|/location|/location|
|--hub|dict|Gets or sets the hub virtual network ID|/hub|/properties/hub|
|--spokes|list|Gets or sets the spokes group IDs|/spokes|/properties/spokes|
|--mesh|list|Gets or sets the mesh group IDs|/mesh|/properties/mesh|

**Example: ManagedNetworkPeeringPoliciesPut**

```
managednetwork managed-network-peering-policy create --resource-group myResourceGroup
        --managed-network-name myManagedNetwork
        --name myHubAndSpoke
        --type HubAndSpokeTopology
```
### managednetwork managed-network-peering-policy update

update a managednetwork managed-network-peering-policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--managed-network-name**|str|The name of the Managed Network.|managed_network_name|managedNetworkName|
|**--name**|str|The name of the Managed Network Peering Policy.|managed_network_peering_policy_name|managedNetworkPeeringPolicyName|
|**--type**|str|Gets or sets the connectivity type of a network structure policy|/type|/properties/type|
|--location|str|The geo-location where the resource lives|/location|/location|
|--hub|dict|Gets or sets the hub virtual network ID|/hub|/properties/hub|
|--spokes|list|Gets or sets the spokes group IDs|/spokes|/properties/spokes|
|--mesh|list|Gets or sets the mesh group IDs|/mesh|/properties/mesh|
### managednetwork managed-network-peering-policy delete

delete a managednetwork managed-network-peering-policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--managed-network-name**|str|The name of the Managed Network.|managed_network_name|managedNetworkName|
|**--name**|str|The name of the Managed Network Peering Policy.|managed_network_peering_policy_name|managedNetworkPeeringPolicyName|

**Example: ManagedNetworkPeeringPoliciesDelete**

```
managednetwork managed-network-peering-policy delete --resource-group myResourceGroup
        --managed-network-name myManagedNetwork
        --name myHubAndSpoke
```
### managednetwork managed-network-peering-policy list

list a managednetwork managed-network-peering-policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--managed-network-name**|str|The name of the Managed Network.|managed_network_name|managedNetworkName|
### managednetwork managed-network-peering-policy show

show a managednetwork managed-network-peering-policy.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--managed-network-name**|str|The name of the Managed Network.|managed_network_name|managedNetworkName|
|**--name**|str|The name of the Managed Network Peering Policy.|managed_network_peering_policy_name|managedNetworkPeeringPolicyName|