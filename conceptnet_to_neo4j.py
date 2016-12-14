"""
 This script takes in as a parameter, the location of ConceptNets CSV dump, and generates a CSV file that can be
 imported into a Neo4J database.

 ConceptNet's csv dump can be found: http://conceptnet5.media.mit.edu/downloads/current/
"""
import csv
import os

# Path to ConceptNets extracted folder (which contains assertions)
conceptnet_location = "data"
# Location for the output nodes.csv file
nodes_location = "nodes.csv"
# Location of the relationships.csv file
relationship_location = "relationships.csv"

nodes = set()
relationships = []

for file in os.listdir("%s/assertions/" % conceptnet_location):

    with open("%s/assertions/%s" % (conceptnet_location, file), "r") as f:
        rows = csv.reader(f, delimiter="\t")
        # Get total rows
        total = 0
        print("Reading %s" % file)
        for i, row in enumerate(rows):
            rel = row[1]
            start = row[2]
            end = row[3]
            if start.starts_with("/c/") and end.starts_with("/c/") and rel.starts_with("/r/"):
                nodes.add(start)
                nodes.add(end)
                relationships.append([start, end, rel])

with open("nodes.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["uri:ID",":LABEL"])
    for n in nodes:
        writer.writerow([n, "Concept"])

with open("relationships.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow([":START_ID",":END_ID",":TYPE"])
    for r in relationships:
        writer.writerow(r)

