```python
from google.cloud import storage
from google.cloud import pubsub_v1
import os

# Shared variables
business_plan = None
system_credentials = None

# Shared message names
SystemDeploymentUpdate = "SystemDeploymentUpdate"

# Shared DOM Element IDs
systemDeployment = "systemDeployment"

def designSystemInfrastructure():
    global business_plan
    global system_credentials

    # Create a storage client.
    storage_client = storage.Client()

    # TODO: Replace 'your-bucket-name' with your Cloud Storage bucket name.
    bucket_name = 'your-bucket-name'
    bucket = storage_client.bucket(bucket_name)

    # TODO: Replace 'your-object-name' with the name of the object to be stored in the bucket.
    object_name = 'your-object-name'
    blob = bucket.blob(object_name)

    # Upload the business plan to the bucket.
    blob.upload_from_string(business_plan)

    # Create a publisher client.
    publisher = pubsub_v1.PublisherClient()

    # TODO: Replace 'your-project-id' with your Google Cloud project ID.
    # TODO: Replace 'your-topic-name' with the name of the Pub/Sub topic to be created.
    project_id = 'your-project-id'
    topic_name = 'your-topic-name'
    topic_path = publisher.topic_path(project_id, topic_name)

    # Create the topic.
    topic = publisher.create_topic(request={"name": topic_path})

    # Publish the SystemDeploymentUpdate message.
    publisher.publish(topic_path, SystemDeploymentUpdate.encode('utf-8'))

    # Store the system credentials.
    system_credentials = {
        'bucket_name': bucket_name,
        'object_name': object_name,
        'project_id': project_id,
        'topic_name': topic_name
    }

    # Update the system deployment status.
    updateSystemDeploymentStatus("System infrastructure designed successfully.")

def updateSystemDeploymentStatus(status):
    # TODO: Implement this function to update the system deployment status in the DOM.
    pass

if __name__ == "__main__":
    designSystemInfrastructure()
```