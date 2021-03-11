import yaml
from rapyuta_io import Client


def get_rio_client():
    client = None
    try:
        with open('.github/app_config/rio-auth.yaml', 'r') as read_file:
            auth_details = yaml.load(read_file, Loader=yaml.FullLoader)
        client = Client(auth_token=auth_details['auth_token'], project=auth_details['project_id'])
    except IOError:
        print("File containing auth details is not accessible.")
    return client



