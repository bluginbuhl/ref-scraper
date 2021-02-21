# Reference Link Scraper

This simple Python tool takes a list of references `refs.txt` (from a journal manuscript, for instance) and scrapes the web for URLs using the [RapidAPI Google Search](https://rapidapi.com/apigeek/api/google-search3/endpoints) tool. In order to use this script, you will need your own RapidAPI account and an API key for the Google Search tool (see the [RapidAPI](#rapidapi) section below).

Running the script will produce a `refs-links.csv` file that will contain 3 columns: `ref_full`, `title`, `link`.

The values for `link` will be one of three options:

1. A URL for the reference
2. The string `'no link found'` if the request was successful, but no link was found
3. The string `'request failed` if there was a connection error during the request

## Usage & Setup

*Note:* This tool was built using `python 3.9.1`, but it should work with older versions as well (not `2.x`)

Clone the repository onto your machine, then navigate to that directory.

### Create a virtual environment using [Pipenv](https://pipenv.pypa.io/en/latest/)

If you have `pip` already installed, you can install Pipenv using `$ pip install --user pipenv`.

`~/ref-scraper $ pipenv install && pipenv shell`

### Create the `refs.txt` file

See the `refs-example.txt` file for formatting. Each reference should be on its own line, and should include the full title of the text that you'd like to find a link for.

### RapidAPI

In order to use the `ref_scraper.py` script, you will need to create your own API key and edit the file to include it. Create an account with RapidAPI, and then navigate to the Google Search tool. Once there, you should see a button that says "Subscribe to Test". Click on the button, then choose the free option, which will provide 600 requests per month. Once you've done this, you should be redirected to the API page, and in the "Code Snippets" window on the right, there should be a field labelled `"x-rapidapi-key"`. Copy the string value of the key and paste it into `ref_scraper.py` for the `RAPID_API_KEY` variable.

### Run the script

*Note:* By default, the script runs silently, and takes quite a bit of time to finish, depending on the size of your `refs.txt` file. If you want to see some output, you can uncomment the `print` statements in `ref_scraper.py` in the `get_request_data` function. This will print every title and link that is found while the script runs.

In your terminal with the virutal environment activated, run the script by calling `$ python ref_scraper.py`.

When the script is finished, it will save a new file `refs-links.csv` and will print the total time in seconds that it took to run.