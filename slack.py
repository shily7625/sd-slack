from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackMessageSender:
    def __init__(self):
        with open('token.txt', 'r') as f:
            token = f.readline().strip()
        with open('channel-id.txt', 'r') as f:
            channel_id = f.readline().strip()
        self.client = WebClient(token=token)
        self.channel_id = channel_id
        
    def send_message(self, text: str):
        try:
            response = self.client.chat_postMessage(
                channel=self.channel_id,
                text=text
            )
            print("메시지 전송 완료:", response)
        except SlackApiError as e:
            print("Error sending message: {}".format(e))