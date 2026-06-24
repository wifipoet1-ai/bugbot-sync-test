import yaml
def parse(data):
    # BUG: yaml.load without SafeLoader -> arbitrary object construction
    return yaml.load(data)
