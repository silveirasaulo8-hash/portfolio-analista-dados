from pathlib import Path

from extract import executar
from storage import upload
from bigquery import carregar
from transform import executar_sql
from pipelines import PIPELINES

def main():

 for pipeline in PIPELINES:

    print("-" * 40)
    print(f"Pipeline: {pipeline['nome']}")
    print("-" * 40)

    print("\nEtapa 1 - Extração")
    arquivo = executar(
        pipeline["sql"],
        pipeline["parquet"]
)
    print("\nEtapa 2 - Upload")
    #upload(arquivo)
    #upload( arquivo,  f"rz/{pipeline['parquet']}" )
    upload(arquivo,   pipeline["storage_path"] )

    print("\nEtapa 3 - BigQuery")
    carregar(pipeline["storage_path"], pipeline["dataset"], pipeline["bq_table"])
    # CZ
    print("\nEtapa 4 - Transformação CZ")

    arquivo_cz = (
        Path(__file__).resolve().parent.parent
        / "sql"
        / "cz"
        / pipeline["cz_sql"]
    )

    executar_sql(arquivo_cz)

    # SZ
    print("\nEtapa 5 - Transformação SZ")

    arquivo_sz = (
        Path(__file__).resolve().parent.parent
        / "sql"
        / "sz"
        / pipeline["sz_sql"]
    )

    executar_sql(arquivo_sz)

    print("\nPipeline concluído com sucesso!")


if __name__ == "__main__":
    main()