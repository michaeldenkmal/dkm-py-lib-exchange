# no unit test
import os
from dataclasses import dataclass

import settings_local
from dkm_lib_exchange import exchange_util, exchg_item_util


def main_save_item_test():
    login_data = settings_local.get_login_data()
    account =exchange_util.connect_to_exchange_std_ret_account(login_data)
    inbox =exchange_util.get_inbox_from_account(account)
    temp_folder = os.path.join(os.environ["TEMP"],"exchange_util_test")
    if not os.path.exists(temp_folder):
        #    os.remove(temp_folder)
        os.mkdir(temp_folder)
    cnt=0
    for item in exchange_util.iter_folder_items(inbox):
        email_info = exchg_item_util.get_simple_email_info(item)
        print (email_info)
        item_path = os.path.join(temp_folder, "%s.eml" % cnt)
        exchg_item_util.save_item_as_elm(item, item_path)
        cnt +=1
        if cnt >10:
            break
    print(temp_folder)


def main_move_item_test():
    login_data = settings_local.get_login_data()
    account =exchange_util.connect_to_exchange_std_ret_account(login_data)
    exchange_util.refresh_folder_cache(account)
    inbox =exchange_util.get_inbox_from_account(account)
    print(f"inbox.path = ${inbox.absolute}")
    BACKUP_SENDER_EMAIL="altaro@dkmdomw19.denkmal.at"

    for item in exchange_util.iter_folder_items(inbox):
        sender_email = exchg_item_util.get_sender_smtp_email(item)
        if sender_email == BACKUP_SENDER_EMAIL:
            backup_logs= exchange_util.get_sub_folder(exchange_util.get_mailbox_root_folder(account), "BackupLogs")
            exchg_item_util.move_item_to_folder(item, backup_logs)
            break



main_move_item_test()

