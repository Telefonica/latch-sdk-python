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

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from src import latch

import logging

logging.basicConfig(
    level=logging.INFO,  # Nivel de logging
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato del mensaje
)

APP_ID = "<YOUR-APP-ID>"
SECRET_KEY = "<YOUR-SECRET-ID>"

def example_pair():
    pairing_code = input("Enter the pairing code: ")
    common_name = input("Enter alias for user: ")
    response = api.pair(pairing_code, None, None, common_name)
    if response.get_error() != "":
        logging.error(
            f"Error in PAIR request with error_code: {response.get_error().get_code()}"
            f" and message: {response.get_error().get_message()}")
    else:
        account_id = response.data.get("accountId")
        logging.info(f"AccountId: {account_id}")
        return account_id


def example_unpair(account_id):
    response = api.unpair(account_id)
    logging.info(f"Status after unpair: {response.data}")
    example_get_status(account_id)

def example_lock(account_id):
    response = api.lock(account_id)
    if response.get_error() != "":
        logging.error(
            f"Error in lock request with error_code: {response.get_error().get_code()}"
            f" and message: {response.get_error().get_message()}")

def example_unlock(account_id):
    response = api.unlock(account_id)
    if response.get_error() != "":
        logging.error(
            f"Error in unlock request with error_code: {response.get_error().get_code()}"
            f" and message: {response.get_error().get_message()}")

def example_get_status(account_id):
    response = api.status(account_id)
    if response.get_error() != "":
        logging.error(
            f"Error in get_status request with error_code: {response.get_error().get_code()}"
            f" and message: {response.get_error().get_message()}")
    else:
        if response.get_data()['operations'][APP_ID]['status'] == 'on':
            logging.info(f"your latch is open and you are able to perform action")
        elif response.get_data()['operations'][APP_ID]['status'] == 'off':
            logging.info(f"Your latch is lock and you can not be allowed to perform action")
        else:
            logging.info(f"Error processing  the response")


if __name__ == '__main__':
    api = latch.Latch(APP_ID, SECRET_KEY)
    account_id = example_pair()
    example_get_status(account_id)
    example_lock(account_id)
    example_get_status(account_id)
    example_unlock(account_id)
    example_get_status(account_id)
    example_unpair(account_id)