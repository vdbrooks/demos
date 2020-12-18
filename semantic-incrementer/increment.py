import semantic_version
import click
import logging

class Versioner(object):
    def __init__(self):
        pass

    def patch_version(self, latest_tag):
        try:
            pass
            current_version = semantic_version.Version(latest_tag)
            new_version = current_version.next_patch()
        except StandardError as e:
            logging.error('Could not increment version number due to the following: ${0} ' .format(e))
        return str(new_version)

    def minor_version(self, latest_tag):
        try:
            pass
            current_version = semantic_version.Version(latest_tag)
            new_version = current_version.next_minor()
        except StandardError as e:
            logging.error('Could not increment version number due to the following: ${0} ' .format(e))
        return str(new_version)

    def major_version(self, latest_tag):
        try:
            pass
            current_version = semantic_version.Version(latest_tag)
            new_version = current_version.next_major()
        except StandardError as e:
            logging.error('Could not increment version number due to the following: ${0} ' .format(e))
        return str(new_version)


@click.command()
@click.option('--vtype', help='The type of version bump, patch, minor, or major', required=True)
@click.option('--tag', help='The latest tag on the reepo', required=True)
def main(vtype,tag):
    update_type = vtype
    latest_tag = tag.replace("v","")
    latest_tag = tag.replace("-beta","")
    
    v = Versioner()

    if update_type == 'patch':
        new_tag = v.patch_version(latest_tag)
    if update_type == 'minor':
        new_tag = v.minor_version(latest_tag)
    if update_type == 'major':
        new_tag = v.major_version(latest_tag)
    print (new_tag)
    
if __name__ == '__main__':
    main()
