from model.pujas import Puja
from .servicio import Servicio
from model.database import BaseDeDatos
from model.libro_diario import Venta


class ServicioLibroDiario(Servicio):
    PUJA_INVALIDA = "Não pode vender um lance não válido"
    PUJA_INEXISTENTE = "Não pode vender a um lance inexistente"
    SIN_CLAVE = "Não pode entrar sem senha"
    LOGIN_INVALIDO = "Nome de usuário ou senha não válidos"
    LICITANTE_INVALIDO = "Não pode listar compras de um licitante não válido"
    LICITANTE_INEXISTENTE = "Não pode listar compras de um licitante inexistente"
    CERRAR_LOTE_INVALIDO = "Não pode fechar um lote não válido"
    CERRAR_LOTE_INEXISTENTE = "Não pode fechar um lote inexistente"

    COMISION_POR_VENTA = 0.1
    PRECIO_FINAL_MAS_IMPUESTOS = 1.12
    COMISION_A_CONSIGNATARIO = 0.97

    def __init__(self, db: BaseDeDatos):
        self.__db = db

    def convertir_en_venta(self, puja_uid: int) -> Venta:
        self._throw_if_not_positive(puja_uid, self.PUJA_INVALIDA)

        puja = self.__db.Pujas.buscar_por_uid(puja_uid)
        self._throw_if_invalid(puja, self.PUJA_INEXISTENTE)

        return self._vender_a(puja)

    def listar_compras_de(self, licitante_uid: int) -> list[Venta]:
        self._throw_if_not_positive(licitante_uid, self.LICITANTE_INVALIDO)

        licitante = self.__db.Usuarios.buscar_licitante_por_uid(licitante_uid)
        self._throw_if_invalid(licitante, self.LICITANTE_INEXISTENTE)

        return self.__db.Ventas.listar_compras_de(licitante)

    def registrar_venta_en(self, lote_uid: int) -> Venta:
        self._throw_if_not_positive(lote_uid, self.CERRAR_LOTE_INVALIDO)

        lote = self.__db.Lotes.buscar_por_uid(lote_uid)
        self._throw_if_invalid(lote, self.CERRAR_LOTE_INEXISTENTE)

        puja = self.__db.Pujas.buscar_ultima_puja(lote)
        if not puja:
            return None

        return self._vender_a(puja)

    def _vender_a(self, puja: Puja) -> Venta:
        comision = round(puja.obtener_monto() * self.COMISION_POR_VENTA, 2)
        precio_final = round((puja.obtener_monto() + comision) * self.PRECIO_FINAL_MAS_IMPUESTOS, 2)
        pago_consignatario = round(puja.obtener_monto() * self.COMISION_A_CONSIGNATARIO, 2)

        return self.__db.Ventas.crear(puja, precio_final, comision, pago_consignatario)
