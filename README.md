# wave_protein


This Python script performs the following tasks:

1 - Imports necessary libraries and modules, such as os, requests, BeautifulSoup, airflow, and Neo4jConnection.

2 - Retrieves the Neo4j connection details (URI, user, and password) from the environment variables and initializes a Neo4jConnection instance.

3 - Defines a function called read_xml_and_save_to_neo4j() that does the following:
a. Downloads an XML file from the UniProt database containing information about a protein with accession number P12345.
b. Parses the XML file using BeautifulSoup to extract the protein's accession number, name, protein name, and the organism's scientific name.
c. Uses the Neo4jConnection instance to execute a Cypher query that inserts the protein and organism information into the Neo4j graph database. The query creates a Protein node, an Organism node, and a relationship FOUND_IN between them.

4 - Defines an Airflow Directed Acyclic Graph (DAG) called "uniprot_to_neo4j" with a description, start date, and scheduling settings.

6 - Creates an Airflow PythonOperator task called "read_uniprot_to_neo4j" that executes the read_xml_and_save_to_neo4j() function.

6 - When the script is run as the main module, it sets the AIRFLOW__CORE__DAGS_FOLDER environment variable to the current script's directory, initializes the Airflow database, and starts the Airflow webserver on port 8080.

The script is designed to be used with Airflow, a popular platform for programmatically authoring, scheduling, and monitoring workflows. The main purpose of the script is to download protein information from the UniProt database in XML format, extract relevant data, and store it in a Neo4j graph database.

This is just a general representation of how the schema structure can be mapped onto a Neo4j graph:

The root element of the schema, "schema", is represented as a node with the properties "targetNamespace" and "elementFormDefault".
The "element" elements that define the elements that can appear in an XML document are represented as nodes with the properties "name", "type", "substitutionGroup", "abstract", "nillable", "minOccurs", "maxOccurs" and "default", and an edge leaving the "schema" node for the corresponding element node.
The "complexType" elements that define complex data types are represented as nodes with the properties "name", "mixed", "abstract", "final", "block", and an edge leaving the "schema" node for the corresponding data type node.
The "attribute" elements that define attributes for an element are represented as nodes with the properties "name", "type", "use", "default" and "fixed", and an edge leaving the corresponding element node for the corresponding attribute node.
The "simpleType" elements that define simple data types are represented as nodes with the properties "name", "final" and "restriction", and an edge leaving the "schema" node for the corresponding data type node.
The "restriction" elements that define restrictions for a data type are represented as nodes with the properties "base", "enumeration", "fractionDigits", "length", "maxExclusive", "maxInclusive", "maxLength", "minExclusive", "minInclusive", "minLength", "pattern", "totalDigits" and "whiteSpace", and an edge leaving the corresponding simple data type node for the corresponding restriction node.
The "enumeration" elements that define possible values for a restricted data type are represented as nodes with the properties "value" and "id", and an edge leaving the corresponding restriction node for the corresponding enumeration node.


Make sure to install the required packages before running the script:

Set environment variables in your system:

export NEO4J_URI=bolt://localhost:7687

export NEO4J_USER=neo4j

export NEO4J_PASSWORD=your_password


pip install apache-airflow bs4 neo4j

pip install python-dotenv

pip install requests

