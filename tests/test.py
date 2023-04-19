"""
 This library offers an API to use LatchAuth in a python environment.
 Copyright (C) 2023 Telefonica Digital

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
import unittest
from src import latch
from src.latchuser import LatchUser
from dotenv import load_dotenv, dotenv_values

load_dotenv()
ENV_VARS = dotenv_values("./.env")


# .env file has this vars to test de library

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.account_id = ENV_VARS["account_id"]
        self.app_id = ENV_VARS["app_id"]
        self.secret_id = ENV_VARS["secret_id"]
        self.user_id = ENV_VARS["user_id"]
        self.user_secret = ENV_VARS["user_secret"]
        self.api = latch.Latch(self.app_id, self.secret_id)

    def test_app_latch_pair_invalid_token(self):
        response = self.api.pair("fP9zpf")
        assert response.error.get_message() == "Token not found or expired"
        assert response.error.get_code() == 206

    def test_crud_operation(self):
        response = self.api.create_operation(self.app_id, "operation_test_1", "DISABLED", "DISABLED")
        operation_id = response.get_data()['operationId']
        response = self.api.update_operation(operation_id, "operation_test_1_v2", "MANDATORY", "MANDATORY")
        assert response.get_data() == "" and response.get_error() == ""
        response = self.api.create_operation(operation_id, "sub_operation_test_1", "DISABLED", "DISABLED")
        sub_operation_id = response.get_data()['operationId']
        response = self.api.get_operations(operation_id)
        assert response.get_data()['operations'][sub_operation_id]['name'] == "sub_operation_test_1"
        response = self.api.delete_operation(sub_operation_id)
        assert response.get_data() == "" and response.get_error() == ""
        response = self.api.delete_operation(operation_id)
        assert response.get_data() == "" and response.get_error() == ""

    def test_crud_instance(self):
        response = self.api.create_operation(self.app_id, "operation_test_1", "DISABLED", "DISABLED")
        operation_id = response.get_data()['operationId']
        response = self.api.create_instance("Instance1", self.account_id, operation_id)
        instance_id = list(response.get_data()['instances'].keys())[0]
        assert list(response.get_data()['instances'].values())[0] == "Instance1"
        self.api.update_instance(instance_id, self.account_id, operation_id, "instance1_v2", "DISABLED",
                                 "DISABLED")
        response = self.api.get_instances(self.account_id, operation_id)
        assert response.get_data()[instance_id]['two_factor'] == "DISABLED"

        response = self.api.instance_status(instance_id, self.account_id, operation_id, False, False)
        assert response.get_data()['operations'][instance_id]['status'] == 'on'
        self.api.delete_instance(instance_id, self.account_id)
        self.api.delete_operation(operation_id)

    def test_latch_user(self):
        latch_user = LatchUser(self.user_id, self.user_secret)
        response = latch_user.create_application('app2', "DISABLED", "DISABLED", "60000000", "mail@mailfake.com")
        application_id = response.get_data()['applicationId']
        response = latch_user.get_applications()
        assert application_id in response.get_data()['operations'].keys()

    def test_get_status(self):
        response = self.api.status(self.account_id)
        assert response.get_data()['operations'][self.app_id] == {'status': 'on'}


if __name__ == '__main__':
    unittest.main()
