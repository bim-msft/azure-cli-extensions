# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-statements
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=unused-argument


def create_internet_analyzer_profile(cmd, client,
                                     profile_name,
                                     name,
                                     location=None,
                                     tags=None,
                                     resource_state=None,
                                     enabled_state=None,
                                     etag=None):
    body = {}
    body['location'] = location  # str
    body['tags'] = tags  # dictionary
    body['resource_state'] = resource_state  # str
    body['enabled_state'] = enabled_state  # str
    body['etag'] = etag  # str
    return client.create_or_update(profile_name=profile_name, resource_group_name=name, parameters=body)


def update_internet_analyzer_profile(cmd, client, body,
                                     profile_name,
                                     name,
                                     location=None,
                                     tags=None,
                                     resource_state=None,
                                     enabled_state=None,
                                     etag=None):
    body = client.get(resource_group_name=name, profile_name=profile_name).as_dict()
    body.location = location  # str
    body.tags = tags  # dictionary
    body.resource_state = resource_state  # str
    body.enabled_state = enabled_state  # str
    body.etag = etag  # str
    return client.create_or_update(profile_name=profile_name, resource_group_name=name, parameters=body)


def list_internet_analyzer_profile(cmd, client,
                                   name):
    if name is not None:
        return client.list_by_resource_group(resource_group_name=name)
    return client.list()


def create_internet_analyzer_experiment(cmd, client,
                                        resource_group,
                                        profile_name,
                                        name,
                                        location=None,
                                        tags=None,
                                        description=None,
                                        endpoint_a_name=None,
                                        endpoint_a_endpoint=None,
                                        endpoint_b_name=None,
                                        endpoint_b_endpoint=None,
                                        enabled_state=None,
                                        resource_state=None):
    body = {}
    body['location'] = location  # str
    body['tags'] = tags  # dictionary
    body['description'] = description  # str
    body.setdefault('endpoint_a', {})['name'] = endpoint_a_name  # str
    body.setdefault('endpoint_a', {})['endpoint'] = endpoint_a_endpoint  # str
    body.setdefault('endpoint_b', {})['name'] = endpoint_b_name  # str
    body.setdefault('endpoint_b', {})['endpoint'] = endpoint_b_endpoint  # str
    body['enabled_state'] = enabled_state  # str
    body['resource_state'] = resource_state  # str
    return client.create_or_update(resource_group_name=resource_group, profile_name=profile_name, experiment_name=name, parameters=body)


def update_internet_analyzer_experiment(cmd, client, body,
                                        resource_group,
                                        profile_name,
                                        name,
                                        location=None,
                                        tags=None,
                                        description=None,
                                        endpoint_a_name=None,
                                        endpoint_a_endpoint=None,
                                        endpoint_b_name=None,
                                        endpoint_b_endpoint=None,
                                        enabled_state=None,
                                        resource_state=None):
    body = client.get(resource_group_name=resource_group, profile_name=profile_name, experiment_name=name).as_dict()
    body.location = location  # str
    body.tags = tags  # dictionary
    body.description = description  # str
    body.endpoint_a.name = endpoint_a_name  # str
    body.endpoint_a.endpoint = endpoint_a_endpoint  # str
    body.endpoint_b.name = endpoint_b_name  # str
    body.endpoint_b.endpoint = endpoint_b_endpoint  # str
    body.enabled_state = enabled_state  # str
    body.resource_state = resource_state  # str
    return client.create_or_update(resource_group_name=resource_group, profile_name=profile_name, experiment_name=name, parameters=body)


def list_internet_analyzer_experiment(cmd, client,
                                      resource_group,
                                      profile_name):
    return client.list_by_profile(resource_group_name=resource_group, profile_name=profile_name)