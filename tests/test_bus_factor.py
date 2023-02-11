from ..src.url.bus_factor import *
import os
def test_busFactor():
    #high bus score
    if bus_factor("apache","superset",os.getenv("GITHUB_TOKEN")) != 100: return 1
    #medium bus score
    if bus_factor("serenity-bdd","serenity-bdd",os.getenv("GITHUB_TOKEN")) != 75: return 1
    #low bus score
    if bus_factor("Chise7","ECE461_Team11",os.getenv("GITHUB_TOKEN")) != 0: return 1
    return 0