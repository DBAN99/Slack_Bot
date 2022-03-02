from slack_sdk.webhook import WebhookClient

def slack_push(event):
    url = 'url'
    webhook = WebhookClient(url)
    response = webhook.send(text=event)

    return response