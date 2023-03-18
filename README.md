# wave_protein


# This Python script performs the following tasks:

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

# entry: 
the root element of the document that contains all the information about the protein
# accession: 
the protein's accession number
# name: 
the protein's name
# protein: 
information about the protein, such as its description, function, and molecular weight
# gene: 
information about the gene that encodes the protein, such as its name and location
# organism: 
information about the organism from which the protein is derived, such as its scientific name and taxonomy
# dbReference: 
cross-references to other databases that contain information related to the protein, such as its three-dimensional structure and amino acid sequence.


# Make sure to install the required packages before running the script:

Set environment variables in your system:

export NEO4J_URI=bolt://localhost:7687

export NEO4J_USER=neo4j

export NEO4J_PASSWORD=your_password


pip install apache-airflow bs4 neo4j

pip install python-dotenv

pip install requests

