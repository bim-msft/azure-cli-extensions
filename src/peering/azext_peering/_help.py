# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=too-many-lines
# pylint: disable=line-too-long
from knack.help_files import helps  # pylint: disable=unused-import


helps['peering asn'] = """
    type: group
    short-summary: Commands to manage peer asn.
"""

helps['peering asn create'] = """
    type: command
    short-summary: create peer asn.
    examples:
      - name: Create a peer ASN
        text: |-
               az peering asn create --name "peerAsnName" --peer-asn "65000" --peer-name "Contoso"
"""

helps['peering asn update'] = """
    type: command
    short-summary: update peer asn.
"""

helps['peering asn delete'] = """
    type: command
    short-summary: delete peer asn.
    examples:
      - name: Delete a peer ASN
        text: |-
               az peering asn delete --name "peerAsnName"
"""

helps['peering asn list'] = """
    type: command
    short-summary: list peer asn.
"""

helps['peering asn show'] = """
    type: command
    short-summary: show peer asn.
"""

helps['peering'] = """
    type: group
    short-summary: Commands to manage peering.
"""

helps['peering create'] = """
    type: command
    short-summary: create peering.
    examples:
      - name: Create a direct peering
        text: |-
               az peering create --resource-group "rgName" --name "peeringName" --sku-name \\
               "Basic_Direct_Free" --kind "Direct" --peering-location "peeringLocation0" --location \\
               "eastus"
      - name: Create an exchange peering
        text: |-
               az peering create --resource-group "rgName" --name "peeringName" --sku-name \\
               "Basic_Exchange_Free" --kind "Exchange" --peering-location "peeringLocation0" --location \\
               "eastus"
"""

helps['peering update'] = """
    type: command
    short-summary: update peering.
    examples:
      - name: Update peering tags
        text: |-
               az peering update --resource-group "rgName" --name "peeringName"
"""

helps['peering delete'] = """
    type: command
    short-summary: delete peering.
    examples:
      - name: Delete a peering
        text: |-
               az peering delete --resource-group "rgName" --name "peeringName"
"""

helps['peering list'] = """
    type: command
    short-summary: list peering.
"""

helps['peering show'] = """
    type: command
    short-summary: show peering.
"""

helps['peering prefix'] = """
    type: group
    short-summary: Commands to manage prefixes.
"""

helps['peering prefix create'] = """
    type: command
    short-summary: create prefix.
    examples:
      - name: Create or update a prefix for the peering service
        text: |-
               az peering prefix create --resource-group "rgName" --peering-service-name \\
               "peeringServiceName" --name "peeringServicePrefixName" --prefix "192.168.1.0/24"
"""

helps['peering prefix update'] = """
    type: command
    short-summary: update prefix.
"""

helps['peering prefix delete'] = """
    type: command
    short-summary: delete prefix.
    examples:
      - name: Delete a prefix associated with the peering service
        text: |-
               az peering prefix delete --resource-group "rgName" --peering-service-name \\
               "peeringServiceName" --name "peeringServicePrefixName"
"""

helps['peering prefix list'] = """
    type: command
    short-summary: list prefix.
"""

helps['peering prefix show'] = """
    type: command
    short-summary: show prefix.
"""

helps['peering service'] = """
    type: group
    short-summary: Commands to manage peering service.
"""

helps['peering service create'] = """
    type: command
    short-summary: create peering service.
    examples:
      - name: Create a  peering service
        text: |-
               az peering service create --resource-group "rgName" --name "peeringServiceName" \\
               --peering-service-location "state1" --peering-service-provider "serviceProvider1" \\
               --location "eastus"
"""

helps['peering service update'] = """
    type: command
    short-summary: update peering service.
    examples:
      - name: Update peering service tags
        text: |-
               az peering service update --resource-group "rgName" --name "peeringServiceName"
"""

helps['peering service delete'] = """
    type: command
    short-summary: delete peering service.
    examples:
      - name: Delete a peering service
        text: |-
               az peering service delete --resource-group "rgName" --name "peeringServiceName"
"""

helps['peering service list'] = """
    type: command
    short-summary: list peering service.
"""

helps['peering service show'] = """
    type: command
    short-summary: show peering service.
"""
