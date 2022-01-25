class TemplateEmail:

    def __init__(self):
        self.template_email = """
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;1,100;1,300;1,400&display=swap" rel="stylesheet">
        </head>
        <body>
            <div style="height:100%; width: 100%;font-family: Roboto;display:flex;
            justify-content:center;flex-direction: column; align-items:center;background-color: e8eaed;">
        
                <div style="width: 80%">  
                    <div style="display:flex;justify-content:center;flex-direction: column; align-items:center;background-color: #dea55f;width: 100%; height: 250px;">
        
                        <div style="display:flex;justify-content:center;flex-direction: column; align-items:center;width: 300px;">
                            <img style="margin-bottom: 30px;" width=70px height=70px src="https://i.ibb.co/wpdnHSy/pngegg.png" alt="check" border="0" />
                            <span style="color: white; font-size: 30px">Parabéns, sua conta MeuBanco foi criada!</span>
                        </div>
                    </div>
        
        
                    <div style="display: flex; flex-direction: column; justify-content: center;text-align:center; align-items:center">
        
                            <p style="font-size: 20px;">Olá,<strong>{nome}</strong></p>
                            <p style="text-align:center">Sua conta foi criada com sucesso, para comecar a utilizá-la é simples:</p>
                            <ol style="text-align:justify;">
                                <li>Acesse nosso aplicativo</li>
                                <li>Clique em <i>Primeiro Acesso</i></li>
                                <li>Leia o QRCODE abaixo</li>
                            </ol>
        
                            <img style="margin-top: 15px;" width=200px height=200px  src="{qrcode}" alt="pngwing-com" border="0" />
                    </div>
        
                </div>
        
        
            </div>
        
        </body>
        </html>
        """

    def set_values(self, nome, qrcode):
        self.template_email = self.template_email.format(nome=nome, qrcode=qrcode)

    def get_template(self):
        return self.template_email
