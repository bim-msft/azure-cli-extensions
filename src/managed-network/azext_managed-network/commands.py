# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals
from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from ._client_factory import cf_managed_networks
    managed-network_managed_networks = CliCommandType(
        operations_tmpl='azure.mgmt.managednetwork.operations.managed_networks_operations#ManagedNetworksOperations.{}',
        client_factory=cf_managed_networks)
    with self.command_group('managed-network', managed-network_managed_networks, client_factory=cf_managed_networks) as g:
        g.custom_command('create', 'create_managed_network')
        g.generic_update_command('update', custom_func_name='update_managed_network')
        g.command('delete', 'delete')
        g.custom_command('list', 'list_managed_network')
        g.show_command('show', 'get')

    from ._client_factory import cf_scope_assignments
    managed-network_scope_assignments = CliCommandType(
        operations_tmpl='azure.mgmt.managednetwork.operations.scope_assignments_operations#ScopeAssignmentsOperations.{}',
        client_factory=cf_scope_assignments)
    with self.command_group('managed-network', managed-network_scope_assignments, client_factory=cf_scope_assignments) as g:
        g.custom_command('create', 'create_managed_network')
        g.generic_update_command('update', custom_func_name='update_managed_network')
        g.command('delete', 'delete')
        g.custom_command('list', 'list_managed_network')
        g.show_command('show', 'get')

    from ._client_factory import cf_managed_network_groups
    managed-network_managed_network_groups = CliCommandType(
        operations_tmpl='azure.mgmt.managednetwork.operations.managed_network_groups_operations#ManagedNetworkGroupsOperations.{}',
        client_factory=cf_managed_network_groups)
    with self.command_group('managed-network managed-network-group', managed-network_managed_network_groups, client_factory=cf_managed_network_groups) as g:
        g.custom_command('create', 'create_managed_network_managed_network_group')
        g.generic_update_command('update', custom_func_name='update_managed_network_managed_network_group')
        g.command('delete', 'delete')
        g.custom_command('list', 'list_managed_network_managed_network_group')
        g.show_command('show', 'get')

    from ._client_factory import cf_managed_network_peering_policies
    managed-network_managed_network_peering_policies = CliCommandType(
        operations_tmpl='azure.mgmt.managednetwork.operations.managed_network_peering_policies_operations#ManagedNetworkPeeringPoliciesOperations.{}',
        client_factory=cf_managed_network_peering_policies)
    with self.command_group('managed-network managed-network-peering-policy', managed-network_managed_network_peering_policies, client_factory=cf_managed_network_peering_policies) as g:
        g.custom_command('create', 'create_managed_network_managed_network_peering_policy')
        g.generic_update_command('update', custom_func_name='update_managed_network_managed_network_peering_policy')
        g.command('delete', 'delete')
        g.custom_command('list', 'list_managed_network_managed_network_peering_policy')
        g.show_command('show', 'get')
