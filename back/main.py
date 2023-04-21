from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import openai

app = FastAPI()

# CORS 설정
origins = ["http://localhost:8080"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

saved_value = ""

@app.post("/api/get_api_key")
async def get_api_key(input_api_key: dict):
    global saved_value
    saved_value = input_api_key['inputValue']
    return {"message": 'Input saved successfully'}

@app.get('/api/get_input')
def get_input():
    global saved_value
    return {'savedValue': saved_value}

@app.get('/api/get_resp')
def get_resp():
    openai.api_key = saved_value
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[{"role": "user", "content": "Please print Hello World Mantha AI!"}]
    )
    response = completion.choices[0].message.content
    return {'response': response}