from model.usuarios import Usuario
from abc import ABC, abstractmethod


class EmailSender(ABC):
    @abstractmethod
    def enviar_mail_a(self, usuario: Usuario, mensaje: str) -> None:
        pass


class RealEmailSender(EmailSender):
    def enviar_mail_a(self, usuario: Usuario, mensaje: str) -> None:
        """
        código para enviar mensagem para o email do usuário
        """
