from .servicio import Servicio
from model.database import BaseDeDatos


class ServicioPuja(Servicio):
    PUJAR_SIN_LOTE = "Não pode licitar sem lote"
    PUJAR_SIN_LICITANTE = "Não pode licitar sem um licitante"
    PUJAR_SIN_PUJA = "Não pode licitar sem um monto"
    LOTE_INEXISTENTE = "Não pode licitar em um lote inexistente"
    LOTE_INVALIDO = "Não pode licitar em um lote não válido"
    LICITANTE_INEXISTENTE = "Não pode licitar com um licitante inexistente"
    PUJA_BAJA = "Não pode oferecer um lance inferior ao último lance"
    PUJA_MENOR_QUE_BASE = "Não pode oferecer um lance inferior a base"
    MONTO_INVALIDO = "Não é possível licitar valores inferiores ou iguais a zero"

    def __init__(self, db: BaseDeDatos):
        super().__init__()
        self.__db = db

    def agregar(self, lote_uid: int, licitante_uid: int, monto: int) -> None:
        self._throw_if_not_positive(lote_uid, self.PUJAR_SIN_LOTE)
        self._throw_if_not_positive(licitante_uid, self.PUJAR_SIN_LICITANTE)
        self._throw_if_invalid(monto, self.PUJAR_SIN_PUJA)

        lote = self.__db.Lotes.buscar_por_uid(lote_uid)
        self._throw_if_invalid(lote, self.LOTE_INEXISTENTE)

        licitante = self.__db.Usuarios.buscar_licitante_por_uid(licitante_uid)
        self._throw_if_invalid(licitante, self.LICITANTE_INEXISTENTE)

        if monto <= 0:
            self._throw(self.MONTO_INVALIDO)

        puja = self.__db.Pujas.buscar_ultima_puja(lote)
        if not puja:
            if monto < lote.obtener_precio_base():
                self._throw(self.PUJA_MENOR_QUE_BASE)
        elif puja.obtener_monto() >= monto:
            self._throw(self.PUJA_BAJA)

        self.__db.Pujas.agregar(licitante, lote, monto)

    def listar(self, lote_uid: int) -> None:
        self._throw_if_not_positive(lote_uid, self.LOTE_INVALIDO)

        lote = self.__db.Lotes.buscar_por_uid(lote_uid)
        self._throw_if_invalid(lote, self.LOTE_INEXISTENTE)

        return self.__db.Pujas.buscar_por_lote(lote)
