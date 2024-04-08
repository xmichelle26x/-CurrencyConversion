# CurrencyConversion
## Test Cases for Currency Conversion API

### Test Case 1: Retrieving exchange rate for a specific source and target currency on a given date.<br>
**Precondition:** Set up API with exchange rate data for various currency pairs, effective start dates, and exchange rates.<br>
**Input parameters:** A valid source currency, a valid target currency and a valid date are provided. USD -> EUR, 2024-04-01.<br>
**Expected output:** The exchange rate from source currency to target currency on date is expected.<br>
**Steps:** <br>
a. Send GET request to the API with input parameters. <br>
b. Assert that the response contains expected output or appropriate error message.<br>
**Expected result:** Successfully retrieves exchange rate for USD to EUR on 2024-04-01.<br>

### Test Case 2: Retrieving exchange rate when there is no direct conversion between currencies.<br>
**Precondition:** Set up API with exchange rate data for direct conversions from USD to an intermediate currency (e.g., USD -> EUR via USD -> GBP), effective start dates, and exchange rates.<br>
**Input parameters:** A valid source currency, a valid target currency, and a valid date are provided. USD -> EUR, 2024-04-01.<br>
**Expected output:** Exchange rate (or similar value) obtained through a triangular conversion if the indirect conversion is available. If no indirect conversion exists, an appropriate error message should be returned.<br>
**Steps:** <br>
a. Send GET request to the API with input parameters. <br>
b. Assert that the response contains expected output or appropriate error message.<br>
**Expected result:** If an indirect conversion is available, successfully retrieves exchange rate for USD to EUR on 2024-04-01 using a triangular conversion. If no indirect conversion exists, returns an appropriate error message.<br>

### Test Case 3: Retrieving exchange rate for a date with missing exchange rates.<br>
**Precondition:** Set up API with some exchange rate data, but not for the specific date and currency pair in question.<br>
**Input parameters:** A valid source currency, a valid target currency, and a valid date are provided where no exchange rate exists for source currency to target currency on a date. (e.g., source currency 'GBP', target currency 'USD', date '2021-10-01').<br>
**Expected output (for triangular conversion):** If no direct exchange rate exists for the given date, the API should try to find the closest effective start date and use that exchange rate.<br>
**Steps:** <br>
a. Send GET request to the API with input parameters. <br>
b. If no direct exchange rate exists for the given date, assert that the API tries to find the closest effective start date and uses that exchange rate. <br>
c. Assert that the response contains expected output or appropriate error message.<br>
**Expected result:** If there is a closest effective start date with exchange rates, the API successfully retrieves the exchange rate for the desired currencies on the specified date using that data. If no exchange rates exist with the source and target currency pair, the API should return an appropriate error message.<br>

### Test Case 4: Retrieving exchange rate for a future date.<br>
**Precondition:** Set up API with exchange rate data for various currency pairs, effective start dates, and exchange rates.<br>
**Input parameters:** Choose a source currency, target currency, and a future date (e.g., source currency 'EUR', target currency 'USD', date '2024-11-01').<br>
**Expected output:** If the exchange rate for the given currency pair and date is not available, the API should return an appropriate error message.<br>
**Steps:** <br>
   a. Send GET request to the API with input parameters.<br>
   b. Assert that the response contains expected output or appropriate error message.<br>
**Expected result:** If no exchange rate exists for the specified date, the API should return an appropriate error message or, if configured differently, try to find the closest available exchange rate before returning an error.<br>

### Test Case 5: Retrieving exchange rate using incorrect input parameters.<br>
**Precondition:** Set up API with exchange rate data for various currency pairs, effective start dates, and exchange rates.<br>
**Input parameters:** Choose incorrect input parameters, such as an invalid source or target currency code, or a non-numeric date (e.g., source currency 'XXX', target currency 'YUM', date ' 2024-04-01').<br>
**Expected output:** The API should return an appropriate error message indicating that the input parameters are invalid.<br>
**Steps:** <br>
   a. Send GET request to the API with incorrect input parameters.<br>
   b. Assert that the response contains an appropriate error message.<br>
**Expected result:** The API successfully handles incorrect input parameters and returns an appropriate error message.<br>

### Test Case 6: Retrieving exchange rate with invalid date format.<br>
**Precondition:** Set up API with exchange rate data for various currency pairs, effective start dates, and exchange rates.<br>
**Input parameters:** Choose a source currency, target currency, and a date with an invalid format (e.g., source currency 'EUR', target currency 'USD', date '2024-30-10').<br>
**Expected output:** The API should return an appropriate error message indicating that the date format is invalid.<br>
**Steps:** <br>
   a. Send GET request to the API with input parameters containing an invalid date format.<br>
   b. Assert that the response contains an appropriate error message.<br>
**Expected result:** The API successfully handles the invalid date format and returns an appropriate error message.<br>


### Test Case 7: Retrieving exchange rate for an unsupported currency pair.<br>
**Precondition:** Set up API with exchange rate data for various currency pairs, effective start dates, and exchange rates.<br>
**Input parameters:** Choose a source currency (e.g., 'ZAR') and target currency (e.g., 'JPY') that are not supported by the API or do not have exchange rates loaded.<br>
**Expected output:** The API should return an appropriate error message indicating that the currency pair is unsupported, or no exchange rate data is available.<br>
**Steps:** <br>
   a. Send GET request to the API with unsupported source and target currency parameters.<br>
   b. Assert that the response contains an appropriate error message.<br>
**Expected result:** The API successfully handles unsupported currency pairs and returns an appropriate error message.<br>

### Test Case 8: API returns error when no exchange rates exist.<br>
**Precondition:** Set up API with exchange rate data for various currency pairs, effective start dates, and exchange rates.<br>
**Input parameters:** Choose a source currency, target currency, and a date for which there are no direct or indirect exchange rates available (e.g., source currency 'GBP', target currency 'USD', date '2024-04-01').<br>
**Expected output:** The API should return an appropriate error message indicating that no exchange rate data is available for the specified date or currency pair.<br>
**Steps:** <br>
   a. Send GET request to the API with input parameters for which no exchange rate data is available.<br>
   b. Assert that the response contains an appropriate error message.<br>
**Expected result:** The API successfully handles cases where no exchange rate data is available and returns an appropriate error message.<br>

### Test Case 9: API handles errors gracefully and returns appropriate status codes.<br>
**Precondition:** Set up API with exchange rate data for various currency pairs, effective start dates, and exchange rates.<br>
**Any input parameters:** (invalid or valid): The API should handle errors gracefully and return appropriate status codes for any given input.<br>
**Expected output:** When an error occurs, the API should return a 400-level HTTP status code (e.g., 400 Bad Request, 404 Not Found).<br>
**Steps:** <br>
   a. Send various GET requests to the API with different input parameters (valid or invalid).<br>
   b. For each request, check the HTTP status code received in the response header.<br>
**Expected result:** The API gracefully handles errors and returns appropriate HTTP status codes for any given input, indicating successful processing or error conditions.<br>
