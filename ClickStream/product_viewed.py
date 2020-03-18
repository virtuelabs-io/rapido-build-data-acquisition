import logging
import uuid
from helpers.cloud_utils import CloudUtils as cu

logging.basicConfig(level=logging.INFO)

class ProductViewedEventProcessor(object):

    def __init__(self):
        self.log = logging.getLogger(__name__)

    def process_event(self, event=None, context=None):
        print("[INFO] Processing event")
        # TODO: Process event
        message = event["body"]
        return self.push_event(message)

    def push_event(self, message):
        print("[INFO] Calling Publish")
        return cu.publishMessageToFirehose(message)


def fun(event=None, context=None):
    print("[INFO] Initializing execution")
    # TODO: remove before going live
    print('Event:\n', event, '\ncontext:\n', context)
    processor = ProductViewedEventProcessor()
    return processor.process_event(event)


if __name__ == "__main__":
# Sample imput event
    sample_product_viewed_event = {
        "body": {
            "header": {
                "eventId": str(uuid.uuid4()),
                "sessionId": str(uuid.uuid4()),
                "customerId": str(uuid.uuid4()),
                "country": "GB",
                "url": "/products/8/product-description",
                "eventTime": "2019-01-01 10:20:35.23432",
                "eventType": "ProductView",
                "pageLoadTime": 8.5,
                "client": "chrome",
                "commit": "34dgf57"
            },
            "consent": {
                "personalise": True,
                "cookiePermission": True
            },
            "ProductView": {
                "productId": 5,
                "price": 10.45
            }
        }
    }

    fun(sample_product_viewed_event)
