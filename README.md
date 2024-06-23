# VAAlugar-MS-reservar
Repositório do projeto de Microsserviço (MS) que executa reserva de canoa.

ATENÇÃO: Docker configurado para rodar na porta 5001.

## O que este microsserviço faz
Este MS gerencia as reservas.

Disponibiliza uma rota /reservar, para comunicação via REST, usando o método POST. Ao chamar esta rota, informar via JSON: id da canoa, id do usuario e uma data.
O MS vai registrar no banco de dados SQLite (exclusivo deste MS) e retornar a confirmação da reserva ou algum erro.

Também disponibiliza a rota /reservas-usuario, via REST - GET. Ao chamar esta rota, basta informar o id do usuario e será retornada em formato JSON uma lista de todas as reservas realizadas em nome deste usuario.

### Chamada REST:


### Resposta JSON:



### Criação do banco de dados: apenas 1 tabela!
CREATE TABLE reservas (
    id_reserva INTEGER PRIMARY KEY,
    id_canoa   INTEGER NOT NULL,
    id_usuario INTEGER NOT NULL,
    data       STRING NOT NULL
);./env


Para instalar:
use o arquivo requirements.txt para instalar os módulos. No windows:
pip install -r requirements.txt
Recomendo instalação em um ambiente virtual

Para executar localmente, em ambiente Windows:
flask run --host 0.0.0.0 --port 5000 --reload


## Como executar através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal.
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
$ docker build -t rest-api .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```
$ docker run -p 5000:5000 rest-api
```

Uma vez executando, para acessar a API, basta abrir o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador.