### LATCH PYTHON SDK ###


#### PREREQUISITES ####

* Python.

* Read API documentation (https://latch.elevenpaths.com/www/developers/doc_api).

* To get the "Application ID" and "Secret", (fundamental values for integrating Latch in any application), it’s necessary to register a developer account in Latch's website: https://latch.elevenpaths.com. On the upper right side, click on "Developer area".


#### USING THE SDK IN PYTHON ####

* Import "latch" module.
```
	import latch
```

* Create a Latch object with the "Application ID" and "Secret" previously obtained.
```
	api = latch.Latch("APP_ID_HERE", "SECRET_KEY_HERE")
```

* Optional settings:
```
	latch.Latch.set_proxy("PROXY_HOST_HERE", port)
```

* Call to Latch Server. Pairing will return an account id that you should store for future api calls
```
	response = api.pair("PAIRING_CODE_HERE")
	response = api.status("ACCOUNT_ID_HERE")
	response = api.unpair("ACCOUNT_ID_HERE")
```

* After every API call, get Latch response data and errors and handle them.
```
	responseData = response.get_data()
	responseError = response.get_error()
  ```
