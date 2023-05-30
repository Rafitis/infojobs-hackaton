from fastapi import APIRouter
import requests
import os

from dotenv import load_dotenv

load_dotenv()

AUTH_TOKEN = os.getenv("AUTH_TOKEN")
URL_API = "https://api.infojobs.net/api/9/"

router = APIRouter(
    prefix="/infojobs/data",
    tags=["infojobs"],
)


@router.get("/")
def get_jobs_offers():
    """
    Get jobs description
    """
    response = requests.get(
        f"{URL_API}/offer?category=informatica-telecomunicaciones&maxResults=3",
        headers={"Authorization": f"Basic {AUTH_TOKEN}"},
    )

    return response.json()


@router.get("/offer/{id_offer}/")
def get_job_info(id_offer: str):
    response = requests.get(
        f"{URL_API}/offer/{id_offer}",
        headers={"Authorization": f"Basic {AUTH_TOKEN}"},
    )

    return response.json()
