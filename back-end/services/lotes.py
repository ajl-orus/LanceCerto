from .servicio import Servicio
from model.database import BaseDeDatos
from model.lotes import Lote


class ServicioLote(Servicio):
    LOTE_SIN_SUBASTA = "Não pode adicionar um lote sem leilão"
    ARTICULO_NULO_EN_SUBASTA = "Não pode adicionar um item nulo no leilão"
    LOTE_SUBASTA_INEXISTENTE = "Não pode adicionar um lote num leilão inexistente"
    ARTICULO_INEXISTENTE = "Não pode adicionar um item inexistente no leilão"
    BUSCAR_SIN_SUBASTA = "Não pode procurar lote sem leilão"
    CONTAR_SUBASTA_INEXISTENTE = "Não pode contar lotes de um leilão inexistente"
    CONTAR_SIN_SUBASTA = "Não pode contar lotes sem leilão"
    SUBASTA_INEXISTENTE = "Não pode  não pode leiloar lote de um leilão inexistente"
    LOTE_INEXISTENTE = "Lote inexistente"
    BASE_INVALIDA = "Não pode agregar item con base não válida"
    ORDEN_INVALIDO = "Não pode agregar item con ordem não válido"
    LISTAR_SIN_SUBASTA = "Não pode listar lote de leilão não válido"
    LISTAR_CON_SUBASTA_INEXISTENTE = "Não pode listar lote de leilão inexistente"

    def __init__(self, db: BaseDeDatos):
        super().__init__()
        self.__db = db

    def agregar(self, subasta_uid: int, articulo_uid: str, base: int, orden: int) -> None:
        self._throw_if_not_positive(subasta_uid, self.LOTE_SIN_SUBASTA)
        self._throw_if_not_positive(articulo_uid, self.ARTICULO_NULO_EN_SUBASTA)
        self._throw_if_not_positive(base, self.BASE_INVALIDA)
        self._throw_if_invalid(orden, self.ORDEN_INVALIDO)

        subasta = self.__db.Subastas.buscar_por_uid(subasta_uid)
        self._throw_if_invalid(subasta, self.LOTE_SUBASTA_INEXISTENTE)

        articulo = self.__db.Articulos.buscar_por_uid(articulo_uid)
        self._throw_if_invalid(articulo, self.ARTICULO_INEXISTENTE)

        self.__db.Lotes.agregar(subasta, articulo, base, orden)

    def contar_lotes_en(self, subasta_uid: int) -> int:
        self._throw_if_not_positive(subasta_uid, self.CONTAR_SIN_SUBASTA)

        subasta = self.__db.Subastas.buscar_por_uid(subasta_uid)
        self._throw_if_invalid(subasta, self.CONTAR_SUBASTA_INEXISTENTE)

        return self.__db.Lotes.contar_lotes(subasta)

    def obtener(self, subasta_uid: int, orden: int) -> Lote:
        self._throw_if_not_positive(subasta_uid, self.BUSCAR_SIN_SUBASTA)

        subasta = self.__db.Subastas.buscar_por_uid(subasta_uid)
        self._throw_if_invalid(subasta, self.SUBASTA_INEXISTENTE)

        if orden < 1:
            self._throw(self.LOTE_INEXISTENTE)

        lote = self.__db.Lotes.obtener(subasta, orden)
        if not lote:
            self._throw(self.LOTE_INEXISTENTE)

        return lote

    def listar(self, subasta_uid: int) -> list[Lote]:
        self._throw_if_not_positive(subasta_uid, self.LISTAR_SIN_SUBASTA)

        subasta = self.__db.Subastas.buscar_por_uid(subasta_uid)
        self._throw_if_invalid(subasta, self.LISTAR_CON_SUBASTA_INEXISTENTE)

        return self.__db.Lotes.listar(subasta)
