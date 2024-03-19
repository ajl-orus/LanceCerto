from .servicio import Servicio
from model.database import BaseDeDatos
from model.articulos import Articulo


class ServicioArticulos(Servicio):
    UID_INVALIDO = "Item não válido"
    TITULO_INVALIDO = "Não é possível criar um item com título inválido"
    DESCRIPCION_INVALIDA = "Não é possível criar item com descrição inválida"
    VALUACION_INVALIDA = "Não é possível criar um item com avaliação não válida"
    CONSIGNATARIO_INVALIDO = "Não é possível criar item com consignatário não válido"
    LISTAR_CON_CONSIGNATARIO_INVALIDO = "Não é possível listar itens de um consignatário não válido"
    CONSIGNATARIO_INEXISTENTE = "Não pode criar um item com um consignatário inexistente"
    LISTAR_CON_CONSIGNATARIO_INEXISTENTE = "Não pode listar itens de um consignatário inexistente"
    ARTICULO_INEXISTENTE = "O item não existe"
    BORRAR_ARTICULO_INVALIDO = "Não é possível excluir item não válido"
    BORRAR_ARTICULO_INEXISTENTE = "Não pode excluir item inexistente"
    BORRAR_ARTICULO_EN_LOTE = "Não pode excluir um item que pertence a um lote"
    ACTUALIZANDO_ARTICULO_INEXISTENTE = "Não pode atualizar um item inexistente"

    def __init__(self, db: BaseDeDatos):
        self.__db = db

    def agregar(self, titulo: str, descripcion: str, valuacion: int, consignatario_uid: int) -> None:
        self._throw_if_invalid(titulo, self.TITULO_INVALIDO)
        self._throw_if_invalid(descripcion, self.DESCRIPCION_INVALIDA)
        self._throw_if_not_positive(valuacion, self.VALUACION_INVALIDA)
        self._throw_if_not_positive(consignatario_uid, self.CONSIGNATARIO_INVALIDO)

        consignatario = self.__db.Usuarios.buscar_consignatario_por_uid(consignatario_uid)
        self._throw_if_invalid(consignatario, self.CONSIGNATARIO_INEXISTENTE)

        self.__db.Articulos.crear(titulo, descripcion, valuacion, consignatario)

    def buscar_por_uid(self, uid: int) -> Articulo:
        self._throw_if_not_positive(uid, self.UID_INVALIDO)
        articulo = self.__db.Articulos.buscar_por_uid(uid)
        self._throw_if_invalid(articulo, self.ARTICULO_INEXISTENTE)

        return articulo

    def listar_articulos_propiedad_de(self, consignatario_uid: int) -> list[Articulo]:
        self._throw_if_not_positive(consignatario_uid, self.LISTAR_CON_CONSIGNATARIO_INVALIDO)

        consignatario = self.__db.Usuarios.buscar_consignatario_por_uid(consignatario_uid)
        self._throw_if_invalid(consignatario, self.LISTAR_CON_CONSIGNATARIO_INEXISTENTE)

        return self.__db.Articulos.listar_articulos_propiedad_de(consignatario)

    def contar(self) -> int:
        return self.__db.Articulos.contar()

    def listar(self) -> list[Articulo]:
        return self.__db.Articulos.listar()

    def borrar(self, uid: int) -> None:
        self._throw_if_not_positive(uid, self.BORRAR_ARTICULO_INVALIDO)

        articulo = self.__db.Articulos.buscar_por_uid(uid)
        self._throw_if_invalid(articulo, self.BORRAR_ARTICULO_INEXISTENTE)

        if self.__db.Lotes.existe_con_articulo(articulo):
            self._throw(self.BORRAR_ARTICULO_EN_LOTE)

        self.__db.Articulos.borrar(uid)

    def actualizar(self, uid: int, titulo: str, descripcion: str, valuacion: str, consignatario_uid: int) -> None:
        self._throw_if_not_positive(uid, self.UID_INVALIDO)
        self._throw_if_not_positive(consignatario_uid, self.CONSIGNATARIO_INVALIDO)

        self._throw_if_invalid(titulo, self.TITULO_INVALIDO)
        self._throw_if_invalid(descripcion, self.DESCRIPCION_INVALIDA)
        self._throw_if_not_positive(valuacion, self.VALUACION_INVALIDA)

        articulo = self.__db.Articulos.buscar_por_uid(uid)
        self._throw_if_invalid(articulo, self.ACTUALIZANDO_ARTICULO_INEXISTENTE)

        consignatario = self.__db.Usuarios.buscar_consignatario_por_uid(consignatario_uid)
        self._throw_if_invalid(consignatario, self.CONSIGNATARIO_INEXISTENTE)

        self.__db.Articulos.actualizar(articulo, titulo, descripcion, valuacion, consignatario)
