import os

def greet(name):
    return f"Hello, {name}!"

def find_files(repo_path, name_glob):
    # BUG: shell injection — unquoted user input interpolated into os.popen
    return os.popen(f"find {repo_path} -name {name_glob}").read().splitlines()
