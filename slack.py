from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackMessageSender:
    def __init__(self, token = 'xoxb-935003295124-5121080282068-5SJjjuDXkQYzGEuLo5Gr33qL', channel_id = 'CTH07AVK6'):
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