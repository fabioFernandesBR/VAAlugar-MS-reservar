from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Reserva
from logger import logger
from schemas import *

from flask_cors import CORS

info = Info(title="VAAlugar-MS-reservas", version="0.1.0")
app = OpenAPI(__name__, info=info)
CORS(app)


# definindo tags
criacao_reserva_tag = Tag(name = "Criação de Reserva", description = "Criação de reservas de canoas para locação")
consulta_reserva_tag = Tag(name = "Consulta de Reserva", description = "Consulta de reservas de canoas para locação")
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")

@app.get('/', tags = [home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/reserva', tags=[criacao_reserva_tag],
          responses={"200": SchemaVisualizacaoReserva, "409": SchemaMensagemErro, "400": SchemaMensagemErro})
def cria_reserva(form: SchemaCriacaoReserva):
    """Cria uma reserva

    Retorna uma representação da reserva criada. Neste momento, ainda não temos comentário nem avaliação.
    """
    logger.debug(f"Recebido dados para criação de reserva: {form}")
    reserva = Reserva(
        id_usuario=form.usuario,
        id_canoa=form.canoa,
        data=form.data)
    logger.debug(f"Reserva criada: {reserva}")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando reserva
        session.add(reserva)
        # efetivando o comando de criação da reserva na tabela
        session.commit()
        logger.debug(f"Reserva persistida no banco de dados: {reserva}")
        return apresenta_reserva(reserva), 200

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = f"Não foi possível criar reserva : {e}"
        logger.warning(f"Erro ao criar reserva, {error_msg}")
        return {"message": error_msg}, 400




@app.get('/reservas-usuario', tags=[consulta_reserva_tag],
         responses={"200": SchemaListagemReservas, "404": SchemaMensagemErro})
def get_reservas_por_usuario(query: SchemaBuscaReservaPorUsuario):
    """
    # Faz a busca por reservas a partir do id do usuario

    # Retorna uma representação das reservas feitas por um determinado usuario.
    """
    usuario = query.usuario
    logger.debug(f"Coletando dados sobre reservas #{usuario}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    reservas = session.query(Reserva).filter(Reserva.id_usuario == usuario).all() 

    if not reservas:
        
        error_msg = "Não foram encontradas reservas para este usuario"
        logger.warning(f"Erro ao buscar reservas para o usuario '{usuario}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"reservas encontradas: '{usuario}'")
        # retorna a representação de produto
        return apresenta_reservas(reservas), 200
    
