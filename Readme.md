##  Python feeding on Apis
Python can feed on apis(I mean interacting with apis). This is made possible by using the Requests library.
 ### Guide
 1. Define the API endpoint you want to fetch data from. In this example, I use the Random User API.
 2. Make a GET request to the API using the requests.get() function.
 3. Check if the request was successful by checking the HTTP status code. A status code of 200 indicates success.
 4. Parse the JSON response using the response.json() method
 5. Access the data you're interested in.
 6. Run the script.
 - The requests lib is easy to use for how it handles the response object.