# wave_protein


# This Python script performs the following tasks:

This script is designed to read an XML file containing information about a protein and store that data in a Neo4j graph database. The script first defines a connection to the Neo4j database using the Neo4jConnection class, which reads connection details from environment variables.

The read_xml_and_save_to_neo4j function is then defined, which uses the ElementTree library to parse the XML file and extract the relevant data. Specifically, the function searches for the gene name and GO terms associated with the protein, and stores them in a list. It then uses the Neo4jConnection object to run a Cypher query to create or update nodes in the Neo4j database. The query merges a new Gene node with the given name, and then for each GO term found in the XML file, it merges a new GO_Term node with the given ID and creates a relationship between the Gene node and the GO_Term node using the "HAS_GO_TERM" relationship type.

Finally, a DAG (Directed Acyclic Graph) is defined to run the read_xml_and_save_to_neo4j function as a task using the PythonOperator class. The DAG is scheduled to run once and is not set to catch up on missed runs.

When the script is executed, it first sets the AIRFLOW__CORE__DAGS_FOLDER environment variable to the directory containing the script. It then runs two shell commands to initialize the Airflow database and start the Airflow webserver on port 8080.

1 - Necessary modules:

os: allows you to access operating system functionality.
datetime: provides classes for working with dates and times.
ElementTree from xml.etree: provides a way to parse XML data.
DAG and PythonOperator from airflow: provide classes for defining and scheduling Airflow tasks.
Neo4jConnection from neo4j_connection: provides a class for connecting to a Neo4j graph database.

2 - Define the connection to the Neo4j database by setting the values for uri, user, and password using environment variables.

3 - Define a function called read_xml_and_save_to_neo4j that:

Parses an XML file called Q9Y261.xml.
Finds the gene name and GO terms from the XML file.
Creates nodes and relationships in the Neo4j database based on the gene name and GO terms.

4 - Define a DAG called uniprot_to_neo4j with the following properties:

description: a string describing the purpose of the DAG.
start_date: a datetime object indicating the start date of the DAG.
schedule_interval: a string indicating the schedule interval for the DAG (in this case, set to None to indicate that it will not be scheduled).
catchup: a boolean indicating whether to backfill DAG runs that were missed while the DAG was inactive.

5 - Define a task called read_uniprot_to_neo4j_task that:

Has a task ID of "read_uniprot_to_neo4j".
Calls the read_xml_and_save_to_neo4j function.
Provides context to the function.
Is associated with the uniprot_to_neo4j DAG.

6 - If the script is executed directly (as opposed to being imported as a module), set the AIRFLOW__CORE__DAGS_FOLDER environment variable to the directory where the script is located, initialize the Airflow database using airflow initdb, and start the Airflow webserver on port 8080 using airflow webserver --port 8080.

# Q9Y261.xml x Model

![Example Data Model](./img/example_data_model.png)

From the image, we can identify that the data model has nodes of type "Protein" and "Organism", and that these nodes are connected by a "FOUND_IN" relationship. Additionally, there is a node of type "Annotation" connected to the "Protein" node by a "HAS_ANNOTATION" relationship, and a node of type "Gene" connected to the "Protein" node by a "HAS_GENE" relationship.

Analyzing the XML file, we can identify that the root element "entry" contains information about a specific protein. The protein information is stored in the "protein" element, including the description, function, molecular weight, and other information. The "gene" element contains information about the gene that codes for the protein, such as its name and location. The "organism" element contains information about the organism from which the protein is derived, such as its scientific name and taxonomy.

Based on this, we can establish the following relationships between the data model in the image and the information in the XML file:

The node of type "Protein" corresponds to the "protein" element in the XML.
The node of type "Organism" corresponds to the "organism" element in the XML.
The "FOUND_IN" relationship corresponds to the information contained in the "organism" element in the XML, which indicates the organism from which the protein is derived.
The node of type "Gene" corresponds to the "gene" element in the XML.
The "HAS_GENE" relationship corresponds to the information contained in the "gene" element in the XML, which indicates the gene that codes for the protein.
The node of type "Annotation" does not have a clear correspondence with the elements in the XML. It may refer to other information related to the protein that is not specifically described by the elements present in the XML file.


The XML file contains information about a specific protein and is composed of various elements, including:

entry: 
the root element of the document that contains all the information about the protein
accession: 
the protein's accession number
name: 
the protein's name
protein: 
information about the protein, such as its description, function, and molecular weight
gene: 
information about the gene that encodes the protein, such as its name and location
organism: 
information about the organism from which the protein is derived, such as its scientific name and taxonomy
dbReference: 
cross-references to other databases that contain information related to the protein, such as its three-dimensional structure and amino acid sequence.


# Make sure to install the required packages before running the script:

Set environment variables in your system:

export NEO4J_URI=bolt://localhost:7687

export NEO4J_USER=neo4j

export NEO4J_PASSWORD=your_password


pip install apache-airflow bs4 neo4j

pip install python-dotenv

pip install requests

