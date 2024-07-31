from fastapi import FastAPI, Request
import uvicorn
import requests

app = FastAPI()

@app.get('/')
def root():
    return('welcome to app 1')

@app.get('/connect-app2')
async def ping_app2():
    URL = "http://app_2:8800/"

    r = requests.get(URL)
    return {'staus':'success',
            'source':'app_1',
            'message':r.json()}

@app.post('/get-from-app2')
async def get_from_app2(req: Request):
    try:
        param = await req.json()
        URL = "http://app_2:8800/get-items"  # Correct service name
        r = requests.post(URL, json=param)
        r.raise_for_status()  # Raise an exception for HTTP errors
        return r.json()
    except requests.RequestException as e:
        return {"error": str(e)}