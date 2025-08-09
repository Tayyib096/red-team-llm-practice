import os
import requests
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


load_dotenv()
DREADNODE_API_KEY = os.getenv("DREADNODE_API_KEY")

CHALLENGE = "bear1"
CRUCIBLE_URL = "https://platform.dreadnode.io"
CHALLENGE_URL = "https://bear1.platform.dreadnode.io"
ARTIFACT_FILES = ['bear.csv']


def download():
    for artifact in ARTIFACT_FILES:
        url = f"{CRUCIBLE_URL}/api/artifacts/{CHALLENGE}/{artifact}"
        headers={"X-API-Key": DREADNODE_API_KEY}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open(f"./bear-1-files/{artifact}", "wb") as file:
                file.write(response.content)
            print(f"{artifact} was successfully downloaded")
        else:
            print(f"Failed to download {artifact}")


df = pd.read_csv('./bear-1-files/bear.csv')

# Grouping by 'bear' type and taking the top entry for each group based on 'tune' value
top_bears = df.sort_values('tune', ascending=False).groupby('bear').head(1)
top_bears = top_bears.sort_values('bear')  # Sorting by bear type for easier visualization


def query(input_data):
    response = requests.post(
        f"{ CHALLENGE_URL }/score",
        headers={"X-API-Key": DREADNODE_API_KEY},
        json={"data": input_data}
    )
    return response.json()

response = query('BAMBOO')


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

flag = response['flag']
submit_flag(flag)