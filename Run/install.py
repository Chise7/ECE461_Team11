import subprocess
def run_install():
    subprocess.run(["pip", "install", "PyGithub"])
    subprocess.run(["pip", "install", "regex"])
    subprocess.run(["pip", "install", "base64"])
    subprocess.run(["pip", "install", "ctypes"])
    subprocess.run(["pip", "install", "requests"])
    subprocess.run(["pip", "install", "ndjson"])
    subprocess.run(["pip", "install", "GitPython"])
    # subprocess.run(["cargo", "add", "serde"])
    # subprocess.run(["cargo", "add", "reqwest"])
    print("Install Complete.") 