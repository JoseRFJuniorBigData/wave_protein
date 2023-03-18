# wave_protein


This Python script performs the following tasks:

Imports necessary libraries and modules, such as os, requests, BeautifulSoup, airflow, and Neo4jConnection.

Retrieves the Neo4j connection details (URI, user, and password) from the environment variables and initializes a Neo4jConnection instance.

Defines a function called read_xml_and_save_to_neo4j() that does the following:
a. Downloads an XML file from the UniProt database containing information about a protein with accession number P12345.
b. Parses the XML file using BeautifulSoup to extract the protein's accession number, name, protein name, and the organism's scientific name.
c. Uses the Neo4jConnection instance to execute a Cypher query that inserts the protein and organism information into the Neo4j graph database. The query creates a Protein node, an Organism node, and a relationship FOUND_IN between them.

Defines an Airflow Directed Acyclic Graph (DAG) called "uniprot_to_neo4j" with a description, start date, and scheduling settings.

Creates an Airflow PythonOperator task called "read_uniprot_to_neo4j" that executes the read_xml_and_save_to_neo4j() function.

When the script is run as the main module, it sets the AIRFLOW__CORE__DAGS_FOLDER environment variable to the current script's directory, initializes the Airflow database, and starts the Airflow webserver on port 8080.

The script is designed to be used with Airflow, a popular platform for programmatically authoring, scheduling, and monitoring workflows. The main purpose of the script is to download protein information from the UniProt database in XML format, extract relevant data, and store it in a Neo4j graph database.


Make sure to install the required packages before running the script:

Set environment variables in your system:

export NEO4J_URI=bolt://localhost:7687

export NEO4J_USER=neo4j

export NEO4J_PASSWORD=your_password


pip install apache-airflow bs4 neo4j

pip install python-dotenv

pip install requests

