# VAAlugar-MS-reservar
Repositório do projeto VA'Alugar em Microsserviços (MS) para a gestão das reservas. Para mais informações sobre este projeto, consultar o readme do repositório Gateway: https://github.com/fabioFernandesBR/VAAlugar-MS-gateway/blob/main/README.md.

As funcionalidades disponíveis são Criação de Reservas, na rota /reserva, e Consulta de Reservas, na rota /reserva-usuario.

### ATENÇÃO: rodar na porta 5003.

## Esquema de Fluxo de informações:
Disponibiliza as seguintes rota para comunicação via REST:

### /reserva
Passar um dicionário com o seguinte padrão:
{
  "canoa": int,
  "data": "string",
  "usuario": "string"
}

Exemplo:

{
  "canoa": 14,
  "data": "01/07/2024",
  "usuario": "21999999999"
}

retorna:
{
  "canoa": 14,
  "data": "01/07/2024",
  "id-reserva": 3,
  "usuario": "21999999999"
}

### /reservas-usuario
Passar um dicionário com o seguinte padrão:
{
  "usuario": "string"
}

Exemplo:
{
  "usuario": "string"
}

retorna JSON:
{
  "reservas": [
    {
      "canoa": 1,
      "data": "01/05/2024",
      "id-reserva": 1,
      "usuario": "21999999999"
    },
    {
      "canoa": 20,
      "data": "01/07/2024",
      "id-reserva": 2,
      "usuario": "21999999999"
    },
    {
      "canoa": 1,
      "data": "01/05/2025",
      "id-reserva": 3,
      "usuario": "21999999999"
    },
    {
      "canoa": 4,
      "data": "01/05/2025",
      "id-reserva": 4,
      "usuario": "21999999999"
    },
    {
      "canoa": 4,
      "data": "01/05/2025",
      "id-reserva": 5,
      "usuario": "21999999999"
    },
    {
      "canoa": 4,
      "data": "01/05/2025",
      "id-reserva": 6,
      "usuario": "21999999999"
    },
    {
      "canoa": 1,
      "data": "14/07/2024",
      "id-reserva": 17,
      "usuario": "21999999999"
    },
    {
      "canoa": 1,
      "data": "13/07/2024",
      "id-reserva": 19,
      "usuario": "21999999999"
    },
    {
      "canoa": 1,
      "data": "01/05/2025",
      "id-reserva": 22,
      "usuario": "21999999999"
    },
    {
      "canoa": 1,
      "data": "01/05/2025",
      "id-reserva": 23,
      "usuario": "21999999999"
    }
  ]
}

## Criação do banco de dados: apenas 1 tabela!
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
