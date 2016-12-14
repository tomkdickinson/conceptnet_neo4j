# conceptnet_neo4j
A Python script that converts ConceptNets CSV data a CSV input that can be fast imported into Neo4J

Neo4J is a useful graph database for performing complex graph queries, and thus is quite suitable for
a graph database such as ConceptNet.

As Neo4J has a very useful ./neo4j-import tool, converting ConceptNet into a suitable input for this
can enable a user to import ConceptNet in less than a minute.

This script takes in the extracted concept_flat_csv folder, and exports a node.csv and relationship.csv 
 file which can then be imported into Neo4J using ./neo4j-import.
 
After running, you can import it into conceptnet using something like:

./neo4j-import --into "folder you want to store db in" --nodes "nodes.csv" --relationships "relationships.csv" 
