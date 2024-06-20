# VAAlugar-MS-reservar
Repositório do projeto de Microsserviço (MS) que executa reserva de canoa.

## O que este microsserviço faz
Este MS disponibiliza uma rota /reservar, para comunicação via REST, usando o método POST.
Ao chamar esta rota, informar via JSON: id da canoa, id do usuario e uma data.
O MS vai registrar no banco de dados SQLite (exclusivo deste MS) e retornar a confirmação da reserva ou algum erro.

### Criação do banco de dados: apenas 1 tabela!
CREATE TABLE reservas (
    id_reserva INTEGER PRIMARY KEY,
    id_canoa   INTEGER NOT NULL,
    id_usuario INTEGER NOT NULL,
    data       INTEGER NOT NULL
);


