from datetime import date
from .servicio import Servicio
from model.tipo_usuario import TipoDeUsuario
from model.database import BaseDeDatos
from services.email_sender import EmailSender


class ServicioUsuario(Servicio):
    SIN_NOMBRE = "Não pode criar um usuario sem nome"
    SIN_APELLIDO = "Não pode criar um usuario sem sobrenome"
    SIN_EMAIL = "Não pode criar um usuario sem email"
    SIN_USUARIO = "Não pode criar um usuario sem usuario"
    SIN_CLAVE = "Não pode criar um usuario sem senha"
    SIN_NACIMIENTO = "Não pode criar um usuario sem data de nacimento"
    CUENTA_YA_EXISTE = "A conta já existe"
    USUARIO_UID_INVALIDO = "Não pode atualizar um usuário não válido"
    USUARIO_INVALIDO = "Não pode usar um usuário não válido"
    EMAIL_INVALIDO = "Não pode usar um email não válido"
    CLAVE_INVALIDA = "Não pode usar uma senha não válida"
    USUARIO_INEXISTENTE = "Não pode atualizar um usuário inexistente"
    USUARIO_YA_EXISTE = "Nome de usuário já existe"
    CONTACTO_SIN_NOMBRE = "Não pode entrar em contato com o leiloeiro sem nome"
    CONTACTO_SIN_EMAIL = "Não pode entrar em contato com o leiloeiro sem email"
    CONTACTO_SIN_ASUNTO = "Não pode entrar em contato com o leiloeiro sem asunto"
    CONTACTO_SIN_TEXTO = "Não pode entrar em contato com o leiloeiro sem texto"
    MARTILLERO_INEXISTENTE = "Não é possível enviar mensagem ao leiloeiro no momento"
    SENDER_INVALIDO = "Não pode entrar em contato com o leiloeiro sem remetente"

    def __init__(self, db: BaseDeDatos):
        self.__db = db

    def agregar(self, nombre: str, apellido: str, email: str, usuario: str, clave: str, nacimiento: date,
                tipo: TipoDeUsuario) -> None:
        self._throw_if_invalid(nombre, self.SIN_NOMBRE)
        self._throw_if_invalid(apellido, self.SIN_APELLIDO)
        self._throw_if_invalid(email, self.SIN_EMAIL)
        self._throw_if_invalid(usuario, self.SIN_USUARIO)
        self._throw_if_invalid(clave, self.SIN_CLAVE)
        self._throw_if_invalid(nacimiento, self.SIN_NACIMIENTO)

        self._throw_if_true(self.__db.Usuarios.existe(usuario), self.CUENTA_YA_EXISTE)
        self._throw_if_true(self.__db.Usuarios.buscar_por_email(email), self.CUENTA_YA_EXISTE)
        self.__db.Usuarios.agregar(nombre, apellido, email, usuario, clave, nacimiento, tipo)

    def actualizar(self, usuario_uid: int, usuario: str, email: str, clave: str) -> None:
        self._throw_if_not_positive(usuario_uid, self.USUARIO_UID_INVALIDO)
        self._throw_if_invalid(usuario, self.USUARIO_INVALIDO)
        self._throw_if_invalid(email, self.EMAIL_INVALIDO)
        self._throw_if_invalid(clave, self.CLAVE_INVALIDA)

        cuenta = self.__db.Usuarios.buscar_usuario_por_uid(usuario_uid)
        self._throw_if_invalid(cuenta, self.USUARIO_INEXISTENTE)

        if cuenta.obtener_usuario() != usuario and self.__db.Usuarios.existe(usuario):
            self._throw(self.USUARIO_YA_EXISTE)

        self.__db.Usuarios.actualizar(cuenta, usuario, email, clave)

    def contactar(self, nombre: str, email: str, asunto: str, texto: str, sender: EmailSender) -> None:
        self._throw_if_invalid(nombre, self.CONTACTO_SIN_NOMBRE)
        self._throw_if_invalid(email, self.CONTACTO_SIN_EMAIL)
        self._throw_if_invalid(asunto, self.CONTACTO_SIN_ASUNTO)
        self._throw_if_invalid(texto, self.CONTACTO_SIN_TEXTO)
        self._throw_if_invalid(sender, self.SENDER_INVALIDO)

        martillero = self.__db.Usuarios.buscar_martillero()
        self._throw_if_invalid(martillero, self.MARTILLERO_INEXISTENTE)

        sender.enviar_mail_a(martillero, f"{nombre} enviou um email com o título {asunto}. {texto}. Responde a {email}")
