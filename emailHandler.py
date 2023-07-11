import yagmail
import os
from dotenv import load_dotenv

load_dotenv()


def sendInfo():
    yag = yagmail.SMTP(os.environ.get("COMEONMAN_EMAIL"), os.environ.get("COMEONMAN_PASSWORD"))
    yag.send(
        to = os.environ.get("RECEIVER_EMAIL"),
        subject = "Server Updated - New Address",
        contents = getEmailContent("192.168.123.112", "12345", "ssh -p 12345 root@255.255.255.255")
    )

def getEmailContent(ip, port, command):
    return f"""
        <div style="font-family: sans-serif; background-color: #10171E; color: #FFFFFF; align-items: center; text-align: center;">
            <img src="{os.environ.get("IMAGE_LINK")}" style="height: 200px; width: 200px; border-radius: 50%; margin: 20px;"/>
            <div style="font-weight: bolder; font-size: 30px;">
                New Address Has Been Published!
            </div>
            <div style="font-weight: bolder; font-size: 22px; margin-top: 30px;">
                IP&nbsp;&nbsp;&nbsp;&nbsp;{ip}
            </div>            
            <div style="font-weight: bolder; font-size: 22px;">
                Port&nbsp;&nbsp;&nbsp;&nbsp;{port}
            </div>
            <div style="font-weight: bolder; font-size: 15px; margin-top: 30px;">
                PC Users Can Use The Following Command
            </div>
            <div style="font-size: 12px;">
                {command}
            </div>            
        </div>
    """

sendInfo()