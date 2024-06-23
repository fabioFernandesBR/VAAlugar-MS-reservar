from pydantic import BaseModel
from typing import Optional, List
from model.reservas import Reserva


class SchemaCriacaoReserva(BaseModel):
    """ 
    Define como uma nova reserva a ser criada deve ser representada, 
    do usuário para a API. 

    Método POST
    """
    usuario: int = 21999999999
    canoa: int = 1
    data: str = "01/05/2024" 

class SchemaBuscaReservaPorUsuario(BaseModel):
    """ 
    Define como deve ser a estrutura que representa a busca, 
    que será feita apenas com base no ID do usuario.

    Método GET
    """
    usuario: int = 21999999999 #Por padrão, sugiro 21999999999    

class SchemaVisualizacaoReserva(BaseModel):
    """ Define como uma nova reserva recém criada deve ser representada, 
    da API para o usuário.
    """
    id_reserva: int = 1
    usuario: int = 21999999999
    canoa: int = 1
    data: str = "01/05/2024"
    

class SchemaListagemReservas(BaseModel): 
    """ Define como uma listagem de reservas será retornada.
    """
    reservas:List[SchemaVisualizacaoReserva]




def apresenta_reserva(reserva: Reserva):
    """ Retorna uma representação da reserva seguindo o schema definido em
        SchemaVisualizacaoReserva.
    """
    return {
        "id-reserva": reserva.id_reserva,
        "usuario": reserva.id_usuario,
        "canoa": reserva.id_canoa,
        "data": reserva.data   
    }

def apresenta_reservas(reservas: list[Reserva]):
    """ Retorna uma representação das reservas seguindo o schema definido em
        SchemaListagemReservas.
    """
    result = []
    for reserva in reservas:
        result.append({
            "id-reserva": reserva.id_reserva,
            "usuario": reserva.id_usuario,
            "canoa": reserva.id_canoa,
            "data": reserva.data  
        })

    return {"reservas": result}