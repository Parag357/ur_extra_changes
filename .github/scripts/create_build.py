from rapyuta_io import SimulationOptions, BuildOptions, CatkinOption
from rapyuta_io.clients.build import Build
from rio_client import get_rio_client
import os
import sys
import yaml

# Authentication

client = get_rio_client()
if not client:
    raise TypeError('error in creating rio client.')

# Create a Build

with open(sys.argv[1], 'r') as read_file:
    create_build_dict = yaml.load(read_file, Loader=yaml.FullLoader)

simulationOptions = None
buildOptions = None
rosDistro = None
isRos = create_build_dict['isRos']

if isRos:
    simulationOptions = SimulationOptions(False)
    buildOptions = BuildOptions(catkinOptions=[CatkinOption()])
    rosDistro = create_build_dict['rosDistro']

repository = os.getenv('GITHUB_SERVER_URL') + '/' + os.getenv('GITHUB_REPOSITORY') + '.git'
build = Build(buildName=create_build_dict['build_name'],
              strategyType=create_build_dict['strategy_type'],
              repository=repository,
              architecture=create_build_dict['architecture'],
              rosDistro=rosDistro,
              isRos=bool(create_build_dict['isRos']),
              contextDir=create_build_dict['contextDir'],
              simulationOptions=simulationOptions,
              buildOptions=buildOptions)

build = client.create_build(build)
build.poll_build_till_ready()
build_id = build.guid
build_details = {"guid": build_id}
with open(".github/app_config/details/build_details.yaml", "w") as write_file:
    yaml.dump(build_details, write_file)
