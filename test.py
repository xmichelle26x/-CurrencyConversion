import requests

def test_currency_conversion_api():
    # Input parameters
    source_currency = 'USD'
    target_currency = 'EUR'
    date = '2024-04-01'
    
    # API endpoint
    url = f'https://api.currencyconverter.com/{date}?from={source_currency}&to={target_currency}'
    
    # Send GET request to the API
    response = requests.get(url)
    
    # Assert status code
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    
    # Parse response
    data = response.json()
    
    # Assert exchange rate is returned
    assert 'exchange_rate' in data, "Exchange rate not found in response"
    
    # Assert the correctness of the exchange rate
    expected_exchange_rate = 0.9  # Example expected exchange rate for USD to EUR on 2024-04-01
    assert data['exchange_rate'] == expected_exchange_rate, f"Expected exchange rate {expected_exchange_rate}, but got {data['exchange_rate']}"
    
    print("Test passed successfully")

# Run the test
test_currency_conversion_api()
