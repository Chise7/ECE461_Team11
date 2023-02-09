import subprocess
def run_install():
    subprocess.run(["pip", "install", "PyGithub", "-q"])
    subprocess.run(["pip", "install", "regex","-q"])
    subprocess.run(["pip", "install", "ndjson","-q"])
    # subprocess.run(["cargo", "add", "serde"])
    # subprocess.run(["cargo", "add", "reqwest"])
    # print("Install Complete.")

if __name__ == "__main__":
    run_install()