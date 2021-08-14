import slack
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
channel = os.environ['SLACK_NOTICATION_CHANNEL']

class NotifySlack:
    
    def recieve_btc(self, title, btc, usd, hash, customer_email, date, status):
        client.chat_postMessage(channel=channel, text=f'''Issue: {title}
        BTC Amount: {btc} BTC
        USD Amount: ${usd}
        Hash: {hash}
        Customer: {customer_email}
        Date: {date}
        status: {status}
        ''')

    def text(self, message):
        client.chat_postMessage(channel=channel, text=message)


# sample call

slack = NotifySlack();
slack.text('Test again')
# slack.recieve_btc('New Receive BTC Issue', '0.000459945', '90.5', 'dfsadfjlkasdjfklajsdlkjf', 'vinay@gmail.com', 'Aug. 13, 2021', 'pending')