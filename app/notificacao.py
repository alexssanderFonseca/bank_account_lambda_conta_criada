import os
import uuid

import boto3
import qrcode
from PIL import Image

from envio_email import EmailSender, Destinatario
from template_email import TemplateEmail


class ContaCriadaNotificacao:

    def __init__(self, url):
        self.qrcode_file_name = f"qrcode-{uuid.uuid4()}.png"
        self.template_email = TemplateEmail()
        self.url = f"{url}"
        self.s3 = boto3.client(
            "s3",
            region_name="US-EAST-1",
            endpoint_url=self.url
        )

    def executar(self, nome_destinario, email_destinatario):
        self.__criar_qr_code()
        self.__upload_s3()
        self.__apaga_qrcode_file()
        self.template_email.set_values(nome_destinario, self.url)
        self.__apaga_qrcode_file()
        self.__enviar_email(email_destinatario, self.template_email.get_template(), "Conta Criada")

    def __criar_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data('Some data')
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="transparent")
        img.save(f"/tmp/{self.qrcode_file_name}")
        img.get_image()

    def __upload_s3(self):
        self.s3.put_object(Bucket="meubanco", Body=Image.open(f"/tmp/{self.qrcode_file_name}").tobytes(),
                           Key=self.qrcode_file_name)

    def __apaga_qrcode_file(self):
        if os.path.exists(f"/tmp/{self.qrcode_file_name}"):
            os.remove(f"/tmp/{self.qrcode_file_name}")

    def __enviar_email(self, origem, body, assunto):
        email = EmailSender(boto3.client('ses'), origem, Destinatario.formatar(), body, assunto)
        email.enviar()
