"""
 This library offers an API to use LatchAuth in a python environment.
 Copyright (C) 2013 Telefonica Digital España S.L.

 This library is free software you can redistribute it and/or
 modify it under the terms of the GNU Lesser General Public
 License as published by the Free Software Foundation either
 version 2.1 of the License, or (at your option) any later version.

 This library is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 Lesser General Public License for more details.

 You should have received a copy of the GNU Lesser General Public
 License along with this library if not, write to the Free Software
 Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
"""
import sys
import os
import logging

from src import latch, latchuser


logging.basicConfig()

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

APP_ID = "<YOUR APP_ID>"
SECRET_KEY = "<YOUR SECRET"

USER_ID = "LCy9wDL8dDuaXjbp3BFN"
USER_SECRET = "E7rfHd4NqDtBrVXjYpwwuwLVaNjgYUjC2ZyX98Fw"

WEB3WALLET = ""
WEB3SIGNATURE = ""

ACCOUNT_ID = ""


def example_pair():
    api = latch.Latch(APP_ID, SECRET_KEY)
    pairing_code = input("Enter the pairing code: ")
    response = api.pair(pairing_code, WEB3WALLET, WEB3SIGNATURE)
    if response.get_error() != "":
        logging.error(
            f"Error in PAIR request with error_code: {response.get_error().get_code()}"
            f" and message: {response.get_error().get_message()}")
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


def example_create_web3_app():
    api = latchuser.LatchUser(USER_ID, USER_SECRET)
    SIGNATURE = "0xb68aba645ac21573034546a92f164022619639526e5c6e2b8a491dedfe4291445cc6bc9a862674c87731aa944a5b5d4c303c21a5bc43164fcce5c4bf41171ebc1c"
    NAME = "app_sdk2"
    WALLET = "0x7fd12f68757721e7671979db0eef8a8ddcfd69db"
    SC_ADDRESS = "0xCa13E35b0921a08Bf0eCC0152a21fA5FE5E2A96d"
    MESSAGE = "message"
    api.create_web3_app(NAME, WALLET, SIGNATURE, SC_ADDRESS, MESSAGE)


def get_status(api, account_id):
    response = api.status(account_id)
    if response.get_error() != "":
        logging.error(
            f"Error in get_status request with error_code: {response.get_error().get_code()}"
            f" and message: {response.get_error().get_message()}")
    else:
        logging.info(f"Status: {response.data}")


if __name__ == '__main__':
    # example_pair()
    example_create_web3_app()
    # example_unpair(ACCOUNT_ID)
