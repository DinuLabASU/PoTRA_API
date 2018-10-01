import requests
import re
import pandas as pd
from pandas import DataFrame
import os
import sys
##  Example usage: python PoTRA_API_Client.py primarysite=kidney
primarysite = str(sys.argv[1]) 

api_portion = 'http://localhost:8000/webservice?'
api_url = api_portion + primarysite
response=requests.get(api_url)
data=response.text
print(data)