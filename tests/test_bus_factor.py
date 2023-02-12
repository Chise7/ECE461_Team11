import bus_factor
import os
def test_busFactor():
    #high bus score
    assert bus_factor.bus_factor("apache","superset",os.getenv("GITHUB_TOKEN")) == 1.0
    #medium bus score
    assert bus_factor.bus_factor("serenity-bdd","serenity-bdd",os.getenv("GITHUB_TOKEN")) == 0.75
    #low bus score
    assert bus_factor.bus_factor("Chise7","ECE461_Team11",os.getenv("GITHUB_TOKEN")) == 0.0