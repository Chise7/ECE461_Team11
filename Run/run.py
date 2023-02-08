import url
import build
import install
import sys

if __name__ == "__main__":
    if(sys.argv[1] == "build"):
        build.run_build()
    elif(sys.argv[1] == "install"):
        install.run_install()
    else:
        url.parser_driver() # Subject to Change