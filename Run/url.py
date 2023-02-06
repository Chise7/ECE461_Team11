from github import Github
import NDJSON
import ctypes
rustLib = ctypes.CDLL("Run/target/debug/rustlib.dll")
netFunc = rustLib.net_score

def main_driver():
    URLList = []
    for URL in URL_FILE:
        busScore = busFactor()
        correct = 
        responsive = 
        rampUp = 
        licenseScore =
        overall = netFunc(busScore, correct, responsive, rampUp, licenseScore)
        URLList.append({URL:{TotalScore: overall, License: licenseScore, RampUp: rampUp, BusFactor: busScore, ResponsiveMaintainers: responsive, Correct: correct}})
    with open("output.NDJSON", "w") as out:
        ndjson.dumps(URLList,out)
    out.close()
if __name__ == "__main__":
    main_driver()

