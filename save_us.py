from prefect import flow
from prefect.artifacts import create_markdown_artifact


@flow
def save_us():
    """
    A flow that saves the United States from a zombie apocalypse by
    uploading an artifact to Prefect Cloud.
    """
    create_markdown_artifact(
        markdown="Antidote",
        key="antidote"
    )
