import subprocess
def run_install():
    subprocess.run(["pip", "install", "PyGithub", "-q"])
    subprocess.run(["pip", "install", "regex", "-q"])
    subprocess.run(["pip", "install", "base64", "-q"])
    subprocess.run(["pip", "install", "ctypes", "-q"])
    subprocess.run(["pip", "install", "requests", "-q"])
    subprocess.run(["pip", "install", "ndjson", "-q"])
    subprocess.run(["pip", "install", "GitPython", "-q"])
    # print("Install Complete.")  #to log file eventually

if __name__ == "__main__":
    run_install()