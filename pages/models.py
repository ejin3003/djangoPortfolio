from django.db import models

# Create your models here.


class Profile:
    id: int
    name: str
    job: str
    objective: str
    img: str
    desc: str


class Project:
    id: int
    name: str
    client: str
    desc: str
    icon: str
    gallery: str
