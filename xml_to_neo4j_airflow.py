import os
from datetime import datetime
from xml.etree import ElementTree as ET
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
    tree = ET.parse("Q9Y261.xml")
    root = tree.getroot()
    gene_name = root.find(".//{http://uniprot.org/uniprot}gene/{http://uniprot.org/uniprot}name").text
    go_terms = []
    for db_ref in root.findall(".//{http://uniprot.org/uniprot}dbReference"):
        if db_ref.get("type") == "GO":
            go_terms.append(db_ref.get("id"))
    if go_terms:
        neo4j_conn.run_query(
            """
            MERGE (g:Gene {name: $gene_name})
            FOREACH (go_term IN $go_terms |
                MERGE (t:GO_Term {id: go_term})
                MERGE (g)-[:HAS_GO_TERM]->(t)
            )
            """,
            {"gene_name": gene_name, "go_terms": go_terms}
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
