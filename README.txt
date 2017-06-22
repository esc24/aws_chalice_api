Hello world serverless app generated using chalice:

    chalice new-project helloworld

Modified to require API keys. The project also includes a helper script
that uses AWS Python SDK (boto3) to add a usage plan with any associated
API keys (a prerequisite) to the generated serverless API.

Usage:

    > chalice deploy
    Initial creation of lambda function.
    Updating IAM policy.
    Creating deployment package.
    Initiating first time deployment...
    Deploying to: dev
    https://70fqt5ohxl.execute-api.eu-west-2.amazonaws.com/dev/

    > python associate_stage.py 70fqt5ohxl dev
    usagePlanId = zqcza9

    > http https://70fqt5ohxl.execute-api.eu-west-2.amazonaws.com/dev/ x-api-key:myapikey
    ...
    ...
    {
        "hello": "world"
    }

    > chalice delete


