from datadog import initialize, api
import os

# Initialize the Datadog client
options = {
    'api_key': os.environ.get('DD_API_KEY')
}

initialize(**options)

def send_log(message, source="python", service="test-service"):
    api.Event.create(
        title="Log Message",
        text=message,
        source_type_name=source,
        tags=[f"service:{service}"]
    )

if __name__ == "__main__":
    # Example usage
    send_log("This is a test log message")
