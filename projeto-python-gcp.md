# 🐍 Projeto ETL — Python + SQL Server + GCP

## 📌 Sobre o projeto

Projeto prático de ETL desenvolvido para demonstrar a integração
entre SQL Server, Python e serviços do Google Cloud Platform (GCP).

O processo realiza a extração dos dados, geração de arquivos Parquet,
carga no Google Cloud Storage e posterior processamento no BigQuery.

## 🏗️ Arquitetura

SQL Server  
↓  
Python / PyODBC  
↓  
Arquivo Parquet  
↓  
Google Cloud Storage  
↓  
BigQuery  
↓  
Camada de transformação

## 🛠️ Tecnologias utilizadas

- Python
- Pandas
- PyODBC
- SQL Server
- Parquet
- Google Cloud Storage
- BigQuery
- SQL

## 🔄 Processo ETL

### 1. Extração

Os dados são extraídos do SQL Server utilizando Python e PyODBC.

### 2. Preparação

Os dados extraídos são tratados e armazenados em formato Parquet.

### 3. Carga

Os arquivos Parquet são enviados para um bucket do Google Cloud Storage.

### 4. Transformação

Os dados são processados no BigQuery utilizando SQL.

### 5. Disponibilização

Os dados transformados ficam preparados para utilização em análises
e soluções de Business Intelligence.

## 🎯 Objetivo

Demonstrar conhecimentos práticos em:

- Desenvolvimento de processos ETL
- Python aplicado a dados
- Integração com bancos de dados
- Cloud Computing
- Data Lake
- BigQuery
- Preparação de dados para BI

## 📚 Status do projeto

Projeto desenvolvido como parte do treinamento prático em Python,
ETL, Data Lake e Google Cloud.
