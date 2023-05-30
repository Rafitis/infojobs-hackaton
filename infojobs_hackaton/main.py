from fastapi import FastAPI
from routers import infojobs_api, openai_api, tts
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(infojobs_api.router)
app.include_router(openai_api.router)
app.include_router(tts.router)
