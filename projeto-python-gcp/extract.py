
import pyodbc
import pandas as pd
from pathlib import Path

# ===============================
# Configurações
# ===============================

from config import SERVER, DATABASE
CONNECTION = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

def ler_sql(caminho_sql: Path) -> str:
    """
    Lê um arquivo SQL e devolve seu conteúdo.
    """
    return caminho_sql.read_text(encoding="utf-8")

#def executar():
def executar(sql_file, parquet_file):
    #print("Conectando ao SQL Server...")
    from logger_config import logger

    logger.info("Conectando ao SQL Server...")

    ROOT = Path(__file__).resolve().parent.parent

 #   caminho_sql = ROOT / "sql" / "rz" / "clientes.sql"
    caminho_sql = ROOT / "sql" / "rz" / sql_file

    sql = ler_sql(caminho_sql)

    conn = pyodbc.connect(CONNECTION)

    df = pd.read_sql(sql, conn)

  
    conn.close()

    print(f"Foram encontrados {len(df)} registros.")
    print(df.head())

    ROOT = Path(__file__).resolve().parent.parent

    pasta_parquet = ROOT / "parquet"
    pasta_parquet.mkdir(exist_ok=True)

    arquivo = pasta_parquet / parquet_file

    df.to_parquet(arquivo, index=False)

    print(f"Arquivo criado: {arquivo.resolve()}")

    return arquivo


if __name__ == "__main__":
    executar()
