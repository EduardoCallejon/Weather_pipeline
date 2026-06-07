# Crio esse projeto com fins de simular um cenário real de  dados <br>

## Planejando

Primeiro precisamos entender qual o processo, estrutura e ferramentas serão utilizadas

A stack do projeto será local  📍 para isso será necessário utilizar:

* Linguagem de programação **Python**
* Orquestração: **Airflow** 
* Docker para encapsular
* Supabase banco destino

<image> 'Imagem'

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








# Weather_pipeline
