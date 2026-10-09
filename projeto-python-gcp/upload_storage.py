from google.cloud import storage
from pathlib import Path


def upload_parquet(bucket_name, arquivo_local, destino_bucket):
    client = storage.Client()

    bucket = client.bucket(bucket_name)

    blob = bucket.blob(destino_bucket)

    blob.upload_from_filename(arquivo_local)

    print("\nUpload realizado com sucesso!")
    print(f"Bucket : {bucket_name}")
    print(f"Destino: {destino_bucket}")


if __name__ == "__main__":

    ROOT = Path(__file__).resolve().parent.parent

    arquivo = ROOT / "parquet" / "clientes.parquet"

    if not arquivo.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {arquivo}")

    upload_parquet(
        bucket_name="contoso-datalake-saulo",
        arquivo_local=str(arquivo),
        destino_bucket="rz/clientes.parquet"
    )