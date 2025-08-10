import os
from dotenv import load_dotenv
import numpy as np
import requests


load_dotenv()
DREADNODE_API_KEY = os.getenv("DREADNODE_API_KEY")

CHALLENGE = "bear2"
CRUCIBLE_URL = "https://platform.dreadnode.io"
CHALLENGE_URL = "https://bear2.platform.dreadnode.io"




def query(input_data):
    payload = {"data": input_data}
    headers = {"X-API-Key": DREADNODE_API_KEY}
    response = requests.post(
        f"{CHALLENGE_URL}/score",
        headers=headers,
        json=input_data
    )

    return response.json()


# input_data = {"coef": 0.1}
# response = query(input_data)
# print(response)

# results = {} # Store the results from the endpoint here

# for h in range(101):
#     response = query({"hunger": h})
#     results[h] = response['outputs'][0]

# print(results)

# import pandas as pd # For data analysis
# import matplotlib.pyplot as plt

# df = pd.DataFrame(list(results.items()), columns=['Hunger', 'Happiness'])

# # Plotting Hunger vs. Happiness
# plt.figure(figsize=(10, 6))
# plt.scatter(df['Hunger'], df['Happiness'], alpha=0.6)
# plt.title('Hunger vs. Happiness Analysis')
# plt.xlabel('Hunger Level')
# plt.ylabel('Happiness Score')
# plt.grid(True)
# plt.show()

# from sklearn.linear_model import  LinearRegression

# lr = LinearRegression() # Create a simple linear regression model

# lr.fit(df[['Hunger']], df['Happiness'])

# print(lr.coef_)

# coef_data = {"coef": "-0.5"}

# result = query(coef_data)
# print(result)

import requests


def submit_flag(flag):
    url = f"{CRUCIBLE_URL}/api/challenges/{CHALLENGE}/submit-flag"
    headers = {"X-API-Key": DREADNODE_API_KEY}
    payload = {"challenge": CHALLENGE, "flag": flag}
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        if response.json().get("correct") is True:
            print("The flag was correct. Congrats!")
        else:
            print("The flag was incorrect. Keep trying!")
    else:
        print("There was an error submitting your flag")
        print(response.text)

flag = 'gAAAAABomKRoADp-8Dfe2tlRTyJ08ZNPFsA62bovWBOnif0jAnZys4fdqFfT7k1Xvkd6VmRJf8upTf0NVtoOC9m1BvLdkY3Ppg-E7aQ8d_EJnLN4hs-_Nf70EiYQwJ-bIRLKe9aVPN-PZMvuBgY6IzGqK3gTKXLngDvOqU3_YyBRyq2wK-7NLX94mVCugG1NbowforYbL-sH'
submit_flag(flag)