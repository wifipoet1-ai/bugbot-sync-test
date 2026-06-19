import os

UPLOAD_DIR = "/var/uploads"


def save_upload(filename, data):
    safe_name = os.path.basename(filename)
    if not safe_name or safe_name in (".", "..") or "\0" in safe_name:
        raise ValueError("Invalid filename")

    upload_root = os.path.realpath(UPLOAD_DIR)
    path = os.path.realpath(os.path.join(UPLOAD_DIR, safe_name))
    if not (path == upload_root or path.startswith(upload_root + os.sep)):
        raise ValueError("Invalid filename")

    with open(path, "wb") as f:
        f.write(data)
    return path
