import datetime
from dataclasses import dataclass

from exchangelib.items import Item


@dataclass
class SimpleEmailData:
    subject:str
    html_body:str
    text_body:str
    sent_on:datetime.datetime
    sender_smtp_adr:str

def get_subject(item:Item)->str:
    return item.subject


def get_text_body(item:Item)->str:
    return item.text_body


def get_body(item:Item)->str:
    return item.body


def get_sent_on(item:Item)->datetime.datetime:
    return item.datetime_sent


def get_sender_smtp_email(item:Item)->str:
    return item.author.email_address


def get_simple_email_info(item:Item)->SimpleEmailData:
    return SimpleEmailData(
        subject = item.subject,
        html_body = item.body,
        text_body = item.text_body,
        sent_on = item.datetime_sent,
        sender_smtp_adr = get_sender_smtp_email(item)
    )


def save_item_as_elm(item:Item, file_path:str):
    with open(file_path,"w",newline='') as f:
        data =item.mime_content.decode("utf-8")
        f.write(data)