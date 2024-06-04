from fastapi import FastAPI, Query
from pydantic import BaseModel, EmailStr
from typing import Annotated



# App Initialization
app = FastAPI()


class Address(BaseModel):
    street: str
    city: str
    zip: str


class User(BaseModel):
    name: str
    email: EmailStr
    address: Address
    

class Report(BaseModel):
    title: str
    content: str


# Basic Query Param
@app.get('/items/')
def basic_query_param(name: str, category: str, price: int | float):
    query_params = {
        "name": name,
        "category": category,
        "price": price
    }

    return query_params


# Query Param Default and Optional
@app.get('/search/')
def query_default(page: int, size: int | None = None, query: str = 'Diligwe',):
    query_params = {
        "query": query,
        "size": size,
        "page": page
    }

    return query_params


# Request Body with Nested Pydantic Models
@app.post('/users/')
def req_body(user: User):

    return {
        "user": user
    }


# Query Param with String Validation
@app.get('/validate/')
def string_validation(username: Annotated[str, Query(min_length=3, max_length=10, pattern="[a-zA-Z0-9]+")]):
    if username:
        return username
        



# Combined Parameters and Validation
@app.post('/reports/{report_id}')
def combined_param(report_id: int, start_date : Annotated[int, Query(ge=2024)], end_date: Annotated[int, Query(le=2026)], report: Report):
    summary = {
        "Path Parameter": report_id,
        "Query Parameters": {
            "start_date": start_date,
            "end_date": end_date
        },
        "Request Body": report
    }

    return summary











