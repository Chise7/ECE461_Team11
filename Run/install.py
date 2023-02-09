import subprocess
def run_install():
    subprocess.run(["pip", "install", "PyGithub"])
    subprocess.run(["pip", "install", "regex"])
    # subprocess.run(["cargo", "add", "serde"])
    # subprocess.run(["cargo", "add", "reqwest"])
    print("Install Complete.")
