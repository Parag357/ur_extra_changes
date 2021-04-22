import os
from rapyuta_io import Client


def get_rio_client():
    client = None
    auth_token = os.getenv('AUTH_TOKEN', default=None)
    project_id = os.getenv('PROJECT_ID', default=None)
    if not (auth_token and project_id):
        return client
    client = Client(auth_token=auth_token, project=project_id)
    return client
