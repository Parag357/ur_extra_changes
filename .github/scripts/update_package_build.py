import yaml


def update_and_return_manifest(build_file, manifest_file):
    with open(build_file, 'r') as read_file:
        build_object = yaml.load(read_file, Loader=yaml.FullLoader)
    build_guid = build_object['guid']
    with open(manifest_file, 'r') as read_file:
        manifest = yaml.load(read_file, Loader=yaml.FullLoader)
    manifest['plans'][0]['components'][0]['executables'][0]['buildGUID'] = build_guid
    return manifest


'''
thank you
'''
