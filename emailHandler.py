import yagmail
import os
from dotenv import load_dotenv

load_dotenv()


def sendInfo():
    yag = yagmail.SMTP(os.environ.get("COMEONMAN_EMAIL"), os.environ.get("COMEONMAN_PASSWORD"))
    yag.send(
        to = os.environ.get("RECEIVER_EMAIL"),
        subject = "First Python Email",
        contents = "This is a test!"
    )

sendInfo()