#!/usr/bin/env python3
"""
Adds the first usage plan and its associated API keys to the
specified API.

Args:
    API_ID and Stage (usually the first and last part of the URL return by
    chalice e.g.
    https://{api_id}.execute-api.eu-west-2.amazonaws.com/{stage}

"""

import sys

import boto3


def associate_stage(api_id, stage):
    client = boto3.client('apigateway')

    resp = client.get_usage_plans()
    if resp['items']:
        usagePlanId = resp['items'][0]['id']
    else:
        raise RuntimeError('Unable to infer usage plan: {}'.format(resp))

    #client.get_usage_plan(usagePlanId=usagePlanId)
    print(f'usagePlanId = {usagePlanId}')
    client.update_usage_plan(usagePlanId=usagePlanId,
                             patchOperations=[{'op':'add',
                                               'path':'/apiStages',
                                               'value':f'{api_id}:{stage}'}])


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'Usage {sys.argv[0]} API_ID STAGE')
        sys.exit(0)

    associate_stage(*sys.argv[1:])


