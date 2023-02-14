import sys
import os
import logging

from src import latch

logging.basicConfig()

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

APP_ID = "<YOUR-APP-ID>"
SECRET_KEY = "<YOUR-SECRET-ID>"

WEB3WALLET = ""
WEB3SIGNATURE = ""

ACCOUNT_ID = ""


def example_pair():
    api = latch.Latch(APP_ID, SECRET_KEY)
    pairing_code = input("Introduce el PAIRING CODE: ")
    response = api.pair(pairing_code, WEB3WALLET, WEB3SIGNATURE)
    if response.get_error() != "":
        logging.error(
            f"Error in PAIR request with error_code: {response.get_error().get_code()} and message: {response.get_error().get_message()}")
    else:
        account_id = response.data.get("accountId")
        logging.info(f"AccountId: {account_id}")
        get_status(api, account_id)
        return account_id


def example_unpair(account_id):
    api = latch.Latch(APP_ID, SECRET_KEY)
    response = api.unpair(account_id)
    logging.info(f"Status after unpair: {response.data}")
    get_status(api, account_id)


def get_status(api, account_id):
    response = api.status(account_id)
    if response.get_error() != "":
        logging.error(
            f"Error in get_status request with error_code: {response.get_error().get_code()} and message: {response.get_error().get_message()}")
    else:
        logging.info(f"Status: {response.data}")


if __name__ == '__main__':
    example_pair()
    # example_unpair(ACCOUNT_ID)
