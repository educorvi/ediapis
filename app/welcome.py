# -*- coding: utf-8 -*-
from fastapi import HTTPException
from .examples import example_apps

class WelcomePages:

    def get_welcome_page(self, ella_id:str):
        if ella_id == 'ella_example_simple':
            welcome = example_apps.get(ella_id)
            return welcome
        #elif ella_id == 'your_ella_app_id':
        #   do something 
        else:
            raise HTTPException(status_code=404, detail="ella_id couldn't be found")
