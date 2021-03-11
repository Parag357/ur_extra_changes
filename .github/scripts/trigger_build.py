from rapyuta_io.utils.error import BuildOperationFailed
import yaml
import sys
from rio_client import get_rio_client

# Authentication

client = get_rio_client()
if not client:
    raise TypeError('error in creating rio client.')

# Get Build guid 

with open(sys.argv[1], 'r') as read_file:
    trigger_build_object = yaml.load(read_file, Loader=yaml.FullLoader)
build_guid = trigger_build_object['guid']

# Trigger a Build

build = client.get_build(build_guid)
try:
    build.trigger()
except BuildOperationFailed as e:
    print e
build.poll_build_till_ready()
