import sys
import os


current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from src import error, latch, latchapp, latchauth, latchresponse, latchuser

APP_ID = "<APP_ID>"
SECRET_KEY = "<SECRET_ID>"

WEB3WALLET = "<WEB3WALLET>"
WEB3SIGNATURE = "<WEB3SIGNATURE>"
# ACCOUNT_ID = ""


def test_sdk_latch():
    print(f'Try SDK latch')

    api = latch.Latch(APP_ID, SECRET_KEY)

    # PAIR
    pairing_code = input("Introduce el PAIRING CODE: ")
    response = api.pair(pairing_code, WEB3WALLET, WEB3SIGNATURE)
    ACCOUNT_ID = response.data.get("accountId")
    print(f"AccountId: {ACCOUNT_ID}")

    # GET STATUS
    response = api.status(ACCOUNT_ID)
    print(f"Status: {response.data}")

    # UNPAIR
    # response = api.unpair(ACCOUNT_ID)


if __name__ == '__main__':
    test_sdk_latch()
