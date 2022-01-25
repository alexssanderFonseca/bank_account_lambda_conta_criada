class EmailSender:
    def __init__(self, ses_client, origem, destino, body, assunto):
        self.ses_client = ses_client
        self.payload = {
            'Source': origem,
            'Destination': destino,
            'Message': {
                'Subject': {'Data': assunto},
                'Body': {'Html': {'Data': body}}}}

    def enviar(self):
        self.ses_client.send_email(**self.payload)


class Destinatario:

    def __init__(self, to_line, cc_line=None, bcc_line=None):
        self.to_line = to_line
        self.cc_line = cc_line
        self.bcc_line = bcc_line

    def formatar(self):
        svc_format = {'ToAddresses': self.to_line}
        if self.cc_line is not None:
            svc_format['CcAddresses'] = self.cc_line
        if self.bcc_line is not None:
            svc_format['BccAddresses'] = self.bcc_line
        return svc_format
