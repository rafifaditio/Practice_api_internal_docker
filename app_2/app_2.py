from fastapi import FastAPI, Request
import uvicorn

items = {'key_1':'val_1',
         'key_2':'val_2',
         'key_3':'val_3'}

app = FastAPI()

@app.get('/')
async def root():
    return('welcome to app 2')

@app.post('/get-items')
async def get_items(req: Request):
    try:
        req_data = await req.json()
        name = req_data.get('name', '')
        keys = req_data.get('keys', '')
        
        if keys in items:
            return {
                'source': 'app_2',
                'status': 'success',
                'requester': name,
                'item': items[keys]
            }
        else:
            return {
                'source': 'app_2',
                'status': 'failed',
                'requester': name,
                'item': 'missing'
            }
    except Exception as e:
        return {'error': str(e)}