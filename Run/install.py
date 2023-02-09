import subprocess
def run_install():
<<<<<<< HEAD
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
=======
    subprocess.run(["pip", "install", "PyGithub", "-q"])
    subprocess.run(["pip", "install", "regex","-q"])
    subprocess.run(["pip", "install", "ndjson","-q"])
    # subprocess.run(["cargo", "add", "serde"])
    # subprocess.run(["cargo", "add", "reqwest"])
    # print("Install Complete.")

if __name__ == "__main__":
    run_install()
>>>>>>> 132f4b7d610234b0c6d858546aaf6f0550d40b37
