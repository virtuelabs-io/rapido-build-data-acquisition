import boto3
import logging
import os
import json
from .constants import PackageConstants as pc


logging.basicConfig(level=logging.INFO)

class CloudUtils(object):

    @staticmethod
    def getFirehoseClient(resource='firehose'):
        if pc.AWS_REGION not in os.environ:
            os.environ[pc.AWS_REGION] = 'eu-west-2'
        return boto3.client(resource)

    @staticmethod
    def publishMessageToFirehose(message):
        log = logging.getLogger(__name__)
        if pc.DELIVERY_STREAM not in os.environ:
            raise ValueError("Environment variable DELIVERY_STREAM not found")
        print("Deliverying message to Firehose with id: {0}".format(message['header']['eventId']))
        response = CloudUtils.getFirehoseClient().put_record(
            DeliveryStreamName=os.environ[pc.DELIVERY_STREAM],
            Record={
                'Data': str(message) + '\n'
            }
        )
        log.info(response)
        return {
            "statusCode": 201
        }
