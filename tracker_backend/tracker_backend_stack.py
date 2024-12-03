from aws_cdk import (
    # Duration,
    Stack,
    aws_dynamodb as dynamodb,
    # aws_sqs as sqs,
)
from constructs import Construct
from tracker_backend.models import TrackerDevice, LocationRecord, User

class TrackerBackendStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # Create DynamoDB table for TrackerDevice
        tracker_device_table = dynamodb.Table(
            self, "TrackerDeviceTable",
            partition_key=dynamodb.Attribute(
                name="tracker_id",
                type=dynamodb.AttributeType.STRING
            )
        )

        # Create DynamoDB table for LocationRecord
        location_record_table = dynamodb.Table(
            self, "LocationRecordTable",
            partition_key=dynamodb.Attribute(
                name="tracker_id",
                type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(
                name="timestamp",
                type=dynamodb.AttributeType.STRING
            ),
            time_to_live_attribute="ttl"
        )

        # Create DynamoDB table for User
        user_table = dynamodb.Table(
            self, "UserTable",
            partition_key=dynamodb.Attribute(
                name="user_id",
                type=dynamodb.AttributeType.STRING
            )
        )

        # example resource
        # queue = sqs.Queue(
        #     self, "TrackerBackendQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
