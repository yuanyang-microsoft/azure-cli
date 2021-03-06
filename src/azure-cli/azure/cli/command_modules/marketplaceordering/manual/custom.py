# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines


def term_accept(client,
                publisher,
                product,
                plan):
    offerDetail = client.get(offer_type="virtualmachine",
                             publisher_id=publisher,
                             offer_id=product,
                             plan_id=plan)
    if offerDetail is None:
        from azure.cli.core.azclierror import ValidationError
        raise ValidationError(
            'cannot find offer with publisher {}, product {} and plan {}.'.format(publisher, product, plan))
    parameters = {}
    parameters['publisher'] = publisher
    parameters['product'] = product
    parameters['plan'] = plan
    parameters['license_text_link'] = offerDetail.license_text_link
    parameters['privacy_policy_link'] = offerDetail.privacy_policy_link
    parameters['marketplace_terms_link'] = offerDetail.marketplace_terms_link
    parameters['retrieve_datetime'] = offerDetail.retrieve_datetime
    parameters['signature'] = offerDetail.signature
    parameters['accepted'] = True
    return client.create(offer_type="virtualmachine",
                         publisher_id=publisher,
                         offer_id=product,
                         plan_id=plan,
                         parameters=parameters)
