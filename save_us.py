from prefect import flow
from prefect.artifacts import create_markdown_artifact

import time


@flow
def save_us():
    """
    A flow that saves the United States from a zombie apocalypse by
    uploading an artifact to Prefect Cloud.
    """
    # Sleep for a bunch of time to simulate a long-running flow
    for _ in range(100):
        time.sleep(30)
    create_markdown_artifact(
        markdown="Antidote",
        key="antidote"
    )
