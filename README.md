# Arquitetura de Dados Weather 📊 <br>

## 📖 Visão Geral
Este projeto tem como objetivo a construção de um pipeline de dados robusto e local para extração, transformação e carga (ETL) de dados meteorológicos. O foco é a implementação de arquitetura de dados moderna utilizando contêinerização e orquestração de alta performance.


## Planejando

Primeiro precisamos entender qual o processo, estrutura e ferramentas serão utilizadas

**🛠 Stack Tecnológica**

* Linguagem: Python 3.x
* Orquestração: Apache Airflow (Taskflow API)
* Contêineres: Docker & Docker Compose
* Gerenciamento de Pacotes: uv (Alta performance em resolução de dependências)
* Armazenamento: Supabase (PostgreSQL)

<img width="1426" height="520" alt="Image" src="https://github.com/user-attachments/assets/efc22944-8ddf-45f9-b61d-bf577542c57e" />

🏗 Estrutura do Projeto
O projeto segue uma arquitetura modular para garantir legibilidade e manutenção:

Weather/
├── dags/           # Definição das DAGs do Airflow
├── src/            # Lógica de negócio (ETL)
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── data/           # Armazenamento temporário local
├── logs/           # Logs de execução do Airflow
├── .env            # Variáveis de ambiente (API_KEY, Credenciais)
└── requirements.txt

## Prática

Começamos criando as dependências do projeto, criando a base as pastas, instalando dependências e configurando o ambiente.

OBS - > Estou utilizando o gereciador de pacotes 'UV', que é mais rápido e prático que o pip e vem trazendo agilidades nos processos!

* Criar o ambiente virtual "UV VENV"
* Criar conjunto de pastas 'MKDIR 'dags','data','logs','src'
* Criação de arquivos > Weather/src/'Extract.py','Trasnform.py','Load.py'
* Criação do arquivo 'Requeriments' para conter as bibliotecas utilizadas
* instalar as dependências do projeto "UV pip install -r requeriments.txt'

ir ao site [text](https://openweathermap.org/users/sign_in)
Extrair uma 'API_KEY', inclui-la em '.env'

Dentro da pasta **SRC**, criar os arquivos ['extract','transform','load'], que são os processos necessários para o pipeline
### Para esse projeto não será necessário atualização incremental

## Testes

Após a criação dos códigos, funções, é hora de testar todo o processo e verificar se está enviando so dados corretos para o banco.

## Montar a estrutura do airflow

Neste projeto vou utilizar a imagem oficial do airflow, facilitando o processo de configuração.

Iniciar a configuração da **DAG** e utilizando o método de **Taskflow** método mais moderno e eficiente. 


🔗 Referências
@vbluiza