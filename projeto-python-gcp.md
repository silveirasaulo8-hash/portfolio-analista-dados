# 🐍 Projeto ETL — Python + SQL Server + GCP

## 📌 Sobre o projeto

Projeto prático de ETL desenvolvido para demonstrar a construção de um pipeline de dados utilizando Python, SQL Server e serviços do Google Cloud Platform (GCP).

O projeto realiza a extração de dados de um banco SQL Server, geração de arquivos em formato Parquet, armazenamento no Google Cloud Storage e transformação dos dados no BigQuery.

O fluxo foi desenvolvido como laboratório prático de integração de dados e conceitos de Data Lake, Cloud e preparação de dados para Business Intelligence.

---

## 🏗️ Arquitetura

```text
┌─────────────────────┐
│      SQL Server     │
│   Fonte dos dados   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│       Python        │
│      PyODBC         │
│      Pandas         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│       Parquet       │
│   Formato de dados  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Google Cloud        │
│ Storage             │
│ Data Lake           │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      BigQuery       │
│ Transformação SQL   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Dados preparados    │
│ para análise e BI   │
└─────────────────────┘
```

---

## 🛠️ Tecnologias utilizadas

### Linguagem e processamento

- Python
- Pandas
- PyODBC
- SQL
- Parquet

### Banco de dados

- SQL Server

### Google Cloud Platform

- Google Cloud Storage
- BigQuery

### Conceitos

- ETL
- Data Lake
- Cloud Computing
- Processamento de dados
- Integração de dados
- Preparação de dados para BI

---

## 🔄 Processo ETL

### 1. Extração

Os dados são extraídos do SQL Server utilizando Python e PyODBC.

O processo utiliza uma consulta SQL para obter os dados da fonte relacional.

**Script principal:** `extract.py`

### 2. Preparação dos dados

Após a extração, os dados são tratados utilizando Python e Pandas.

Os dados são armazenados em formato Parquet, permitindo uma estrutura adequada para o armazenamento e processamento posterior.

### 3. Carga no Data Lake

Os arquivos Parquet são enviados para um bucket do Google Cloud Storage.

O Cloud Storage representa a camada de armazenamento do Data Lake utilizada neste laboratório.

**Script principal:** `upload_storage.py`

### 4. Transformação

Após o armazenamento dos dados, o BigQuery é utilizado para executar as transformações necessárias utilizando SQL.

O processo contempla a criação e transformação das estruturas de dados para disponibilização posterior para análises.

**Script principal:** `transform.py`

### 5. Orquestração do pipeline

O fluxo das etapas do ETL é organizado através do `main.py`.

O script coordena a execução das diferentes etapas do processo, permitindo executar o pipeline de forma estruturada.

**Script principal:** `main.py`

---

## 📂 Estrutura do projeto

```text
projeto-python-gcp/
│
├── extract.py
├── upload_storage.py
├── transform.py
└── main.py
```

### Responsabilidade dos scripts

| Script | Responsabilidade |
|---|---|
| `extract.py` | Extração dos dados do SQL Server |
| `upload_storage.py` | Upload dos arquivos para o Cloud Storage |
| `transform.py` | Transformação dos dados no BigQuery |
| `main.py` | Orquestração do pipeline |

---

## 🎯 Objetivos do projeto

Este projeto foi desenvolvido para praticar e demonstrar conhecimentos em:

- Desenvolvimento de processos ETL
- Python aplicado a dados
- Integração com bancos de dados
- Manipulação de arquivos Parquet
- Data Lake
- Google Cloud Platform
- Google Cloud Storage
- BigQuery
- SQL
- Automação e orquestração de processos
- Preparação de dados para Business Intelligence

---

## 📊 Possíveis evoluções

O pipeline pode ser evoluído futuramente com:

- Agendamento automático do pipeline
- Monitoramento das execuções
- Tratamento de erros
- Logging
- Controle de qualidade dos dados
- Incrementalização da carga
- Camadas adicionais no Data Lake
- Integração com Power BI
- Orquestração utilizando serviços gerenciados de Cloud

---

## 📚 Status do projeto

Projeto prático desenvolvido como parte do treinamento de Python, ETL, Data Lake e Google Cloud Platform.

O projeto representa um laboratório de aprendizagem e demonstração técnica das tecnologias utilizadas.
