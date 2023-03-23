# https://ecederstrand.github.io/exchangelib/
from dataclasses import dataclass
from typing import Generator

from exchangelib import DELEGATE, IMPERSONATION, Account, Credentials, Configuration, Folder
from exchangelib.items import Item


@dataclass
class LoginData:
    user_name:str
    pwd:str
    domain:str
    email_adr:str
    server_url:str


def connect_to_exchange_std_ret_account(loginData:LoginData)->Account:
    dom_and_usr = "%s\\%s" % (loginData.domain,loginData.user_name)
    credentials = Credentials(username=dom_and_usr, password=loginData.pwd)
    config = Configuration(server=loginData.server_url, credentials=credentials)
    return Account(loginData.email_adr, config=config, access_type=DELEGATE)


def get_inbox_from_account(account:Account)->Folder:
    return account.inbox


def iter_folder_items(folder:Folder):
    for item in folder.all():
        yield item


def get_sub_folder(root_folder:Folder, sub_folder_name:str)->Folder:
    return root_folder / sub_folder_name


def get_account_root_folder(account:Account)->Folder:
    return account.root


def refresh_folder_cache(a:Account):
    a.root.refresh()
    #a.public_folders_root.refresh()
    #a.archive_root.refresh()


def get_mailbox_root_folder(account:Account)->Folder:
    return account.inbox.parent
