import os
def save_upload(filename, data):
    # BUG: path traversal — filename not sanitized before joining
    path = os.path.join("/var/uploads", filename)
    with open(path, "wb") as f:
        f.write(data)
    return path
