from pathlib import Path
from google.cloud import bigquery
from config import PROJECT_ID


PROJECT = PROJECT_ID


def executar_sql(caminho_sql):

    print(f"Arquivo informado : {caminho_sql}")
    print(f"Arquivo existe?   : {caminho_sql.exists()}")

    sql = caminho_sql.read_text(encoding="utf-8")

    print(f"Tamanho do SQL: {len(sql)} caracteres")
    print("----- INÍCIO DO SQL -----")
    print(sql)
    print("------ FIM DO SQL -------")

    client = bigquery.Client(project=PROJECT)

    job = client.query(sql)
    job.result()

    print("Transformação concluída.")


def executar_pasta(caminho_pasta):
    """
    Executa todos os arquivos .sql existentes em uma pasta.
    """

    caminho_pasta = Path(caminho_pasta)

    print(f"\nPasta: {caminho_pasta}")

    for arquivo in sorted(caminho_pasta.glob("*.sql")):
        print(f"\nExecutando: {arquivo.name}")
        executar_sql(arquivo)