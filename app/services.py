import requests
from fastapi import HTTPException
from .welcome import WelcomePages
from .examples import example_services

welcome = WelcomePages()

class EllaServices:

    def get_ella_service(self, ella_id, ella_service):
        welcome_page = welcome.get_welcome_page(ella_id)
        allowed = []
        for i in welcome_page.services:
            allowed.append(i.name)
        if ella_service not in allowed:
            raise HTTPExeption(status_code=404, detail="ella_service not found or not allowed in this context")
        if ella_service.startswith('ella_simple'):
            if ella_service in example_services:
                return example_services[ella_service]
            else:
                raise HTTPExeption(status_code=404, detail="ella_service not found")
        #Your Service stuff after this Line
        #----------------------------------
