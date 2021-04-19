from update_package_build import update_and_return_manifest
import sys
import yaml
from rio_client import get_rio_client

# Authentication

client = get_rio_client()
if not client:
    raise TypeError('error in creating rio client.')

# Get Package Details

package_manifest = update_and_return_manifest(sys.argv[1], sys.argv[2])

# Create a Package
package_details = client.create_package(package_manifest)
package_id = package_details['packageId']
package = client.get_package(package_id)


# Write package details to a file

package_version = package.packageVersion
package_plan_id = package.plans[0].planId
package_id = package.packageId
package_details = {'package_id': package_id, 'package_plan_id': package_plan_id, 'package_version': package_version}
with open(".github/app_config/details/package_details.yaml", "w") as write_file:
    yaml.dump(package_details, write_file)
