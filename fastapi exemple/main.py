import json
from fastapi import Depends, FastAPI

import requests

from authentication import verify_token

app = FastAPI()
"""
uvicorn main:app --reload
"""



@app.get("/names/websites", dependencies=[Depends(verify_token)])
def read_items():
    dado = requests.get("https://jsonplaceholder.typicode.com/users")
    response = json.loads(dado.content)
    websites = list(map(lambda x: {'website': x.get('website')}, response))
    return {"websites": websites}


@app.get("/names/detail", dependencies=[Depends(verify_token)])
def read_items():
    dado = requests.get("https://jsonplaceholder.typicode.com/users")
    response = json.loads(dado.content)
    users = list(map(lambda x:
                     {
                         'name': x.get('name'),
                         'email': x.get('email'),
                         'company': x.get('company').get('name')
                     }

                     , response))
    return {"users": users}
