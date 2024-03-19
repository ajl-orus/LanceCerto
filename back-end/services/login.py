from .servicio import Servicio
from .email_sender import EmailSender
from model.database import BaseDeDatos


class ServicioLogin(Servicio):
    SIN_USUARIO = "Não pode entrar sem nome de usuário"
    SIN_CLAVE = "Não pode entrar sem senha"
    LOGIN_INVALIDO = "Nome de usuário ou senha não válidos"
    RECORDAR_SIN_MAIL = "Não pode lembrar uma senha sem e-mail"
    RECORDAR_SIN_SENDER = "Não pode lembrar uma chave sem remetente"

    def __init__(self, db: BaseDeDatos):
        self.__db = db

    def login(self, usuario: str, clave: str) -> None:
        self._throw_if_invalid(usuario, self.SIN_USUARIO)
        self._throw_if_invalid(clave, self.SIN_CLAVE)

        usuario = self.__db.Usuarios.buscar(usuario, clave)
        self._throw_if_invalid(usuario, self.LOGIN_INVALIDO)

    def recordar(self, email: str, sender: EmailSender) -> None:
        self._throw_if_invalid(email, self.RECORDAR_SIN_MAIL)
        self._throw_if_invalid(sender, self.RECORDAR_SIN_SENDER)

        usuario = self.__db.Usuarios.buscar_por_email(email)
        if usuario:
            sender.enviar_mail_a(usuario, f"Recordatorio: Sua chave é {usuario.obtener_clave()}")
