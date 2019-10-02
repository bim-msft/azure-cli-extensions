# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from knack.arguments import CLIArgumentType
from azure.cli.core.commands.parameters import (
    tags_type,
    get_three_state_flag,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group


def load_arguments(self, _):
    name_arg_type = CLIArgumentType(options_list=('--name', '-n'), metavar='NAME')

    with self.argument_context('managednetwork create') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('name', id_part=None, help='The name of the Managed Network.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('tags', tags_type)
        c.argument('scope', id_part=None, help='The collection of management groups, subscriptions, virtual networks, and subnets by the Managed Network. This is a read-only property that is reflective of all ScopeAssignments for this Managed Network')

    with self.argument_context('managednetwork update') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('name', id_part=None, help='The name of the Managed Network.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('tags', tags_type)
        c.argument('scope', id_part=None, help='The collection of management groups, subscriptions, virtual networks, and subnets by the Managed Network. This is a read-only property that is reflective of all ScopeAssignments for this Managed Network')

    with self.argument_context('managednetwork delete') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('name', id_part=None, help='The name of the Managed Network.')

    with self.argument_context('managednetwork list') as c:
        c.argument('resource_group', resource_group_name_type)

    with self.argument_context('managednetwork show') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('name', id_part=None, help='The name of the Managed Network.')

    with self.argument_context('managednetwork create') as c:
        c.argument('parameters', id_part=None, help='undefined')
        c.argument('scope', id_part=None, help='The base resource of the scope assignment to create. The scope can be any REST resource instance. For example, use \'/subscriptions/{subscription-id}/\' for a subscription, \'/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}\' for a resource group, and \'/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider}/{resource-type}/{resource-name}\' for a resource.')
        c.argument('name', id_part=None, help='The name of the scope assignment to create.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('assigned_managed_network', id_part=None, help='The managed network ID with scope will be assigned to.')

    with self.argument_context('managednetwork update') as c:
        c.argument('parameters', id_part=None, help='undefined')
        c.argument('scope', id_part=None, help='The base resource of the scope assignment to create. The scope can be any REST resource instance. For example, use \'/subscriptions/{subscription-id}/\' for a subscription, \'/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}\' for a resource group, and \'/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider}/{resource-type}/{resource-name}\' for a resource.')
        c.argument('name', id_part=None, help='The name of the scope assignment to create.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('assigned_managed_network', id_part=None, help='The managed network ID with scope will be assigned to.')

    with self.argument_context('managednetwork delete') as c:
        c.argument('scope', id_part=None, help='The base resource of the scope assignment to create. The scope can be any REST resource instance. For example, use \'/subscriptions/{subscription-id}/\' for a subscription, \'/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}\' for a resource group, and \'/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider}/{resource-type}/{resource-name}\' for a resource.')
        c.argument('name', id_part=None, help='The name of the scope assignment to create.')

    with self.argument_context('managednetwork list') as c:
        c.argument('scope', id_part=None, help='The base resource of the scope assignment to create. The scope can be any REST resource instance. For example, use \'/subscriptions/{subscription-id}/\' for a subscription, \'/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}\' for a resource group, and \'/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider}/{resource-type}/{resource-name}\' for a resource.')

    with self.argument_context('managednetwork show') as c:
        c.argument('scope', id_part=None, help='The base resource of the scope assignment to create. The scope can be any REST resource instance. For example, use \'/subscriptions/{subscription-id}/\' for a subscription, \'/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}\' for a resource group, and \'/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider}/{resource-type}/{resource-name}\' for a resource.')
        c.argument('name', id_part=None, help='The name of the scope assignment to create.')

    with self.argument_context('managednetwork managed-network-group create') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('managed_network_name', id_part=None, help='The name of the Managed Network.')
        c.argument('name', id_part=None, help='The name of the Managed Network Group.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('management_groups', id_part=None, help='The collection of management groups covered by the Managed Network')
        c.argument('subscriptions', id_part=None, help='The collection of subscriptions covered by the Managed Network')
        c.argument('virtual_networks', id_part=None, help='The collection of virtual nets covered by the Managed Network')
        c.argument('subnets', id_part=None, help='The collection of  subnets covered by the Managed Network')
        c.argument('kind', arg_type=get_enum_type(['Connectivity']), id_part=None, help='Responsibility role under which this Managed Network Group will be created')

    with self.argument_context('managednetwork managed-network-group update') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('managed_network_name', id_part=None, help='The name of the Managed Network.')
        c.argument('name', id_part=None, help='The name of the Managed Network Group.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('management_groups', id_part=None, help='The collection of management groups covered by the Managed Network')
        c.argument('subscriptions', id_part=None, help='The collection of subscriptions covered by the Managed Network')
        c.argument('virtual_networks', id_part=None, help='The collection of virtual nets covered by the Managed Network')
        c.argument('subnets', id_part=None, help='The collection of  subnets covered by the Managed Network')
        c.argument('kind', arg_type=get_enum_type(['Connectivity']), id_part=None, help='Responsibility role under which this Managed Network Group will be created')

    with self.argument_context('managednetwork managed-network-group delete') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('managed_network_name', id_part=None, help='The name of the Managed Network.')
        c.argument('name', id_part=None, help='The name of the Managed Network Group.')

    with self.argument_context('managednetwork managed-network-group list') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('managed_network_name', id_part=None, help='The name of the Managed Network.')

    with self.argument_context('managednetwork managed-network-group show') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('managed_network_name', id_part=None, help='The name of the Managed Network.')
        c.argument('name', id_part=None, help='The name of the Managed Network Group.')

    with self.argument_context('managednetwork managed-network-peering-policy create') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('managed_network_name', id_part=None, help='The name of the Managed Network.')
        c.argument('name', id_part=None, help='The name of the Managed Network Peering Policy.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('_type', options_list=['--type'], arg_type=get_enum_type(['HubAndSpokeTopology', 'MeshTopology']), id_part=None, help='Gets or sets the connectivity type of a network structure policy')
        c.argument('hub', id_part=None, help='Gets or sets the hub virtual network ID')
        c.argument('spokes', id_part=None, help='Gets or sets the spokes group IDs')
        c.argument('mesh', id_part=None, help='Gets or sets the mesh group IDs')

    with self.argument_context('managednetwork managed-network-peering-policy update') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('managed_network_name', id_part=None, help='The name of the Managed Network.')
        c.argument('name', id_part=None, help='The name of the Managed Network Peering Policy.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('_type', options_list=['--type'], arg_type=get_enum_type(['HubAndSpokeTopology', 'MeshTopology']), id_part=None, help='Gets or sets the connectivity type of a network structure policy')
        c.argument('hub', id_part=None, help='Gets or sets the hub virtual network ID')
        c.argument('spokes', id_part=None, help='Gets or sets the spokes group IDs')
        c.argument('mesh', id_part=None, help='Gets or sets the mesh group IDs')

    with self.argument_context('managednetwork managed-network-peering-policy delete') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('managed_network_name', id_part=None, help='The name of the Managed Network.')
        c.argument('name', id_part=None, help='The name of the Managed Network Peering Policy.')

    with self.argument_context('managednetwork managed-network-peering-policy list') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('managed_network_name', id_part=None, help='The name of the Managed Network.')

    with self.argument_context('managednetwork managed-network-peering-policy show') as c:
        c.argument('resource_group', resource_group_name_type)
        c.argument('managed_network_name', id_part=None, help='The name of the Managed Network.')
        c.argument('name', id_part=None, help='The name of the Managed Network Peering Policy.')
