import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from neo4j_connection import Neo4jConnection

# Define the Neo4j connection
uri = os.environ["NEO4J_URI"]
user = os.environ["NEO4J_USER"]
password = os.environ["NEO4J_PASSWORD"]
neo4j_conn = Neo4jConnection(uri, user, password)

# Read XML and store data in Neo4j
def read_xml_and_save_to_neo4j(**kwargs):
    url = "https://www.uniprot.org/uniprot/P12345.xml"
    response = requests.get(url)
    content = response.text

    soup = BeautifulSoup(content, "xml")
    entry = soup.find("entry")

    accession = entry.find("accession").text
    name = entry.find("name").text
    protein_name = entry.find("fullName").text
    organism_name = entry.find("name", {"type": "scientific"}).text

    neo4j_conn.run_query(
        """
        MERGE (p:Protein {accession: $accession, name: $name, protein_name: $protein_name})
        MERGE (o:Organism {name: $organism_name})
        MERGE (p)-[:FOUND_IN]->(o)
        """,
        {"accession": accession, "name": name, "protein_name": protein_name, "organism_name": organism_name}
    )

# Define the DAG
dag = DAG(
    "uniprot_to_neo4j",
    description="Read Uniprot protein XML and save data to Neo4j graph database",
    start_date=datetime(2023, 3, 18),
    schedule_interval=None,
    catchup=False,
)

# Define the task
read_uniprot_to_neo4j_task = PythonOperator(
    task_id="read_uniprot_to_neo4j",
    python_callable=read_xml_and_save_to_neo4j,
    provide_context=True,
    dag=dag,
)

if __name__ == "__main__":
    os.environ["AIRFLOW__CORE__DAGS_FOLDER"] = os.path.dirname(os.path.abspath(__file__))
    os.system("airflow initdb")
    os.system("airflow webserver --port 8080")
