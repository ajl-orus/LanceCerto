from abc import ABC, abstractmethod
from model.usuarios import Licitante
from model.serialization import Serializable
from model.lotes import Lote


class Puja(Serializable):
    def __init__(self, uid: int, licitante: Licitante, lote: Lote, monto: int):
        self.__uid = uid
        self.__monto = monto
        self.__licitante = licitante
        self.__lote = lote

    def obtener_uid(self) -> int:
        return self.__uid

    def obtener_monto(self) -> int:
        return self.__monto

    def obtener_licitante(self) -> Licitante:
        return self.__licitante

    def obtener_lote(self) -> Lote:
        return self.__lote

    def serialize(self):
        return {"monto": self.__monto, "lote": self.__lote.obtener_uid(), "licitante": self.__lote.obtener_uid()}


class Pujas(ABC):
    @abstractmethod
    def agregar(self, licitante: Licitante, lote: Lote, monto: int):
        pass

    @abstractmethod
    def buscar_ultima_puja(self, lote: Lote) -> Puja:
        pass

    @abstractmethod
    def buscar_por_uid(self, uid: int) -> Puja:
        pass

    @abstractmethod
    def buscar_por_lote(self, lote: Lote) -> list[Puja]:
        pass
