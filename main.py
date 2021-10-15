from model.aviso import Aviso
from threading import Thread
# from utils import get_accounts
from model.sheet import Sheet
from properties import POSITIONS_WIN, THREADS

global sh
sh = Sheet()
global accounts
accounts = sh.get_all_accounts()


def init_session(position):
    global accounts
    global sh
    account = accounts.pop(0)
    try:
        driver = Aviso(account, position=position)
        account = driver.run_to_end()
    finally:
        del driver
        accounts.append(account)
        # save info in account to excel
        sh.update_account(account)
        init_session(position)


def init_thread():
    positions = POSITIONS_WIN
    for i in range(THREADS):
        Thread(target=init_session, args=(positions[str(i)],)).start()


if __name__ == "__main__":
    init_thread()
