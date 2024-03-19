# venta.py
#
# crear(puja)
# listar_compras_para(licitante)
from abc import ABC, abstractmethod
from model.pujas import Puja
from model.serialization import Serializable
from model.usuarios import Licitante


class Venta(Serializable):
    def __init__(self, uid: int, puja: Puja, precio_final: float, comision: float, pago_a_consignatario: float):
        self.__uid = uid
        self.__puja = puja
        self.__precio = precio_final
        self.__comision = comision
        self.__pago_a_consignatario = pago_a_consignatario

    def obtener_uid(self) -> int:
        return self.__uid

    def obtener_titulo_lote(self) -> str:
        return self.__puja.obtener_lote().obtener_titulo_articulo()

    def obtener_ganador(self) -> Licitante:
        return self.__puja.obtener_licitante()

    def obtener_precio_final(self) -> float:
        return self.__precio

    def obtener_comision(self) -> float:
        return self.__comision

    def obtener_pago_a_consignatario(self) -> float:
        return self.__pago_a_consignatario

    def serialize(self):
        return {"id": self.__uid, "titulo": self.obtener_titulo_lote(), "ganhador": self.obtener_ganador().obtener_nombre(),
                "preço": self.obtener_precio_final(), "comissão": self.obtener_comision(),
                "pago consignatario": self.obtener_pago_a_consignatario()}


class LibroDiario(ABC):
    @abstractmethod
    def crear(self, puja: Puja, precio_final: float, comision: float, pago_a_consignatario: float) -> Venta:
        pass

    @abstractmethod
    def buscar_por_uid(self, uid: int) -> Venta:
        pass

    @abstractmethod
    def listar_compras_de(self, licitante: Licitante) -> list[Venta]:
        pass
