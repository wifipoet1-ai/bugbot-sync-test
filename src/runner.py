import subprocess
def run_cmd(user_input):
    # BUG: shell=True with user input -> command injection
    return subprocess.call(user_input, shell=True)
