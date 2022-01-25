import json

from notificacao import ContaCriadaNotificacao


def lambda_handler(event, context):
    notificao_conta_criada = ContaCriadaNotificacao("http://host.docker.internal:4566")
    payload = event["Records"][0]["Sns"]["Message"]
    payload_dic = json.loads(payload)
    return {
        "statusCode": 200,
        "body": notificao_conta_criada.executar(event, payload_dic["nome"], payload_dic["email"]),
    }
