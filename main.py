from src import latch

port = 22
APP_ID_HERE = "dnPkvKpzC2xkYrvEQcW7"
SECRET_KEY_HERE = "sCg8zvdrPEXieApzUXpmbiiw8gtwcjbJ9FaW7bZB"
api = latch.Latch(APP_ID_HERE, SECRET_KEY_HERE)

response = api.pair("fP9zpf")
responseData = response.get_data()
responseError = response.get_error()


accountId = "gThX4zCTYCifvRi8mn8xwsCQVVKE8NfANnLLRGw2zVfYCYsU2BHCJgvxbUikU4TK"

response = api.status(accountId)
print(response)