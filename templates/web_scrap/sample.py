from curl_cffi import requests
import os
from pydantic import BaseModel
from rich import print

class SearchItem(BaseModel):
    title: str
    url: str

class ItemDetails(BaseModel):
    title: str
    price: str
    description: str

class SearchResponse(BaseModel):
    items: list[SearchItem]

def new_session():
    session = requests.Session(impersonate = "chrome")
    return session

def search_api(session: requests.Session, query: str, start_num: int) -> SearchResponse:
    url = f"https://www.amazon.com"
    resp = session.get(url)
    print(**resp.json())
    resp.raise_for_status()
    search = SearchResponse(**resp.json()['first']['anoher like tea'])

def detail_api(session: requests.Session, url: str) -> ItemDetails:
    resp = session.get(url)
    resp.raise_for_status()
    details = ItemDetails(**resp.json())
    return details


def main():
    session = new_session()
    search = search_api(session, "laptop", 1)
    for item in search.items:

        details = session, item.url
        print(details)

if __name__ == "__main__":
    main()  