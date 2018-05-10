import nist_lookup.xraydb_plugin as xdb
import csv
import sys

writer = csv.writer(sys.stdout)
writer.writerow(["energy", "delta", "beta", "attenuation_length"])
for energy in range(10, 160):
    delta, beta, atlen = xdb.xray_delta_beta("C", 1.95, energy * 1e3)
    writer.writerow([energy, delta, beta, atlen])
