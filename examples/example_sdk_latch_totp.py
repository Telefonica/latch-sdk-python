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
import json

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
sys.path.append('./')

from src import latch

logging.basicConfig(
    level=logging.INFO,  # Nivel de logging
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato del mensaje
)
console_handler = logging.StreamHandler()

APP_ID = "<YOUR-APP-ID>"
SECRET_KEY = "<YOUR-SECRET-ID>"
ACCOUNT_ID = "<ACCOUNT-ID>"

def example_create_totp():
    api = latch.Latch(APP_ID, SECRET_KEY)
    id = input("Enter the name displayed for the totp: ")
    name = input("Enter name ")
    response = api.create_totp(id, name)
    if response.get_error() != "":
        logging.error(
            f"Error in PAIR request with error_code: {response.get_error().get_code()}"
            f" and message: {response.get_error().get_message()}")
    else:
        totp_id = response.data.get("totpId")
        qr = response.data.get("qr")
        logging.info(f"Response: {response.data}")
        logging.info(f"Totp Id (Save it, you'll need it later): {totp_id}")
        logging.info(f"QR (Show the QR to the user, you can open it with any browse): {qr}")

def example_validate_totp():
    console_handler.flush()
    api = latch.Latch(APP_ID, SECRET_KEY)
    totp_id = input("Enter the identifier for the totp: ")
    code = input("Enter the code generated ")
    response = api.validate_totp(totp_id,code)
    if response.get_error() != "":
        logging.error(
            f"Error in PAIR request with error_code: {response.get_error().get_code()}"
            f" and message: {response.get_error().get_message()}")
    else:
        logging.info(f"IThere was no error so the code is valid")

if __name__ == '__main__':
    example_create_totp()
    example_validate_totp()
    # example_validate_totp()
