# VAAlugar-MS-reservar
Repositório do projeto de Microsserviço (MS) que executa reserva de canoa.

ATENÇÃO: Docker configurado para rodar na porta 5003.

## O que este microsserviço faz
Este MS gerencia as reservas.

Disponibiliza uma rota /reservar, para comunicação via REST, usando o método POST. Ao chamar esta rota, informar via JSON: id da canoa, id do usuario e uma data.
O MS vai registrar no banco de dados SQLite (exclusivo deste MS) e retornar a confirmação da reserva ou algum erro.

Também disponibiliza a rota /reservas-usuario, via REST - GET. Ao chamar esta rota, basta informar o id do usuario e será retornada em formato JSON uma lista de todas as reservas realizadas em nome deste usuario.

## Criação de Reserva
http://localhost:5003/reserva

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

 access-control-allow-origin: http://localhost:5003 
 connection: close 
 content-length: 70 
 content-type: application/json 
 date: Sun,23 Jun 2024 00:37:37 GMT 
 server: Werkzeug/3.0.3 Python/3.12.4 
 vary: Origin 

## Consulta de Reserva
http://localhost:5003/reservas-usuario?usuario=21999999999

### Chamada REST:
curl -X 'GET' \
  'http://localhost:5003/reservas-usuario?usuario=21999999999' \
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


## Instalação
Considere as seguintes opções: instalar apenas este microsserviço, diretamente do IDE, como Visual Studio Code; ou instalar todos os microsserviços via Docker Compose.

### Para rodar este MS diretamente do IDE.
No Windows:
1. Faça o clone deste repositório para sua máquina.
2. Crie um ambiente virtual, com o comando "Python -m venv env", diretamente no terminal.
3. Em seguida ative o ambiente virtual, com o comando ".\env\Scripts\activate".
4. Instale as dependências necessárias com o comando "pip install -r requirements.txt".
5. Execute com o comando "flask run --host 0.0.0.0 --port 5003"
Para Mac ou Linux, a lógica é a mesma, mas faça as adaptações necessárias.

### Como executar através do Docker Compose
Para que os microsserviços interajam, é necessário que todos estejam rodando. A forma mais fácil de instalar e executar todos está descrita no link:
https://github.com/fabioFernandesBR/VAAlugar-Docker-Compose/blob/main/README.md
