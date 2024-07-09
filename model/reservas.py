from sqlalchemy import Column, String, Integer



from  model import Base


class Reserva(Base):
    __tablename__ = 'reservas'

    id_reserva = Column(Integer, primary_key = True)
    id_canoa = Column(Integer)
    id_usuario = Column(String(256))
    data = Column(String(50))
    


    def __init__(self, id_usuario, id_canoa, data):
        """
        Cria uma Reserva!

        Arguments:
            id_usuario
            id_canoa
            data: quando a canoa será alugada
        """
        self.id_usuario = id_usuario
        self.id_canoa = id_canoa
        self.data = data

        