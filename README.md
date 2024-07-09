# VAAlugar-MS-reservar
Repositório do projeto de Microsserviço (MS) que executa reserva de canoa.

ATENÇÃO: Docker configurado para rodar na porta 5001.

## O que este microsserviço faz
Este MS gerencia as reservas.

Disponibiliza uma rota /reservar, para comunicação via REST, usando o método POST. Ao chamar esta rota, informar via JSON: id da canoa, id do usuario e uma data.
O MS vai registrar no banco de dados SQLite (exclusivo deste MS) e retornar a confirmação da reserva ou algum erro.

Também disponibiliza a rota /reservas-usuario, via REST - GET. Ao chamar esta rota, basta informar o id do usuario e será retornada em formato JSON uma lista de todas as reservas realizadas em nome deste usuario.

## Criação de Reserva
http://localhost:5001/reserva

### Chamada REST:
curl -X 'POST' \
  'http://localhost:5001/reserva' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'canoa=14' \
  -F 'data=01/07/2024' \
  -F 'usuario="21999999999"'

### Resposta JSON:
{
  "canoa": 14,
  "data": "01/07/2024",
  "id-reserva": 3,
  "usuario": "21999999999"
}

 access-control-allow-origin: http://localhost:5001 
 connection: close 
 content-length: 70 
 content-type: application/json 
 date: Sun,23 Jun 2024 00:37:37 GMT 
 server: Werkzeug/3.0.3 Python/3.12.4 
 vary: Origin 

## Consulta de Reserva
http://localhost:5001/reservas-usuario?usuario=21999999999

### Chamada REST:
curl -X 'GET' \
  'http://localhost:5001/reservas-usuario?usuario=21999999999' \
  -H 'accept: application/json'

### Resposta JSON:
{
  "reservas": [
    {
      "canoa": 1,
      "data": "01/05/2024",
      "id-reserva": 1,
      "usuario": 21999999999
    },
    {
      "canoa": 20,
      "data": "01/07/2024",
      "id-reserva": 2,
      "usuario": 21999999999
    },
    {
      "canoa": 14,
      "data": "01/07/2024",
      "id-reserva": 3,
      "usuario": 21999999999
    }
  ]
}

 access-control-allow-origin: * 
 connection: close 
 content-length: 224 
 content-type: application/json 
 date: Sun,23 Jun 2024 00:45:27 GMT 
 server: Werkzeug/3.0.3 Python/3.12.4 


### Criação do banco de dados: apenas 1 tabela!
CREATE TABLE reservas (
    id_reserva INTEGER PRIMARY KEY,
    id_canoa   INTEGER NOT NULL,
    id_usuario TEXT    NOT NULL,
    data       TEXT    NOT NULL
);


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
docker build -t ms-reservas .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```
docker run -d -p 5001:5001 ms-reservas
```

Uma vez executando, para acessar a API, basta abrir o [http://localhost:5001/]no navegador.
