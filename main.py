from slack_sdk.webhook import WebhookClient

def slack_push(event):
    url = 'https://hooks.slack.com/services/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'
    webhook = WebhookClient(url)
    response = webhook.send(text=event)

    return response

slack_push('asd')