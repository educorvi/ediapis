import sys
import smtplib
import requests
from fastapi import HTTPException
from .examples import example_apps, example_services


class EllaServices:

    def get_welcome_page(self, ella_id:str):
        if ella_id == 'ella_example_simple':
            welcome = example_apps.get(ella_id)
            return welcome
        #Your welcome-stuff after this line
        #----------------------------------
        #elif ella_id == 'your_ella_app_id':
        #   do something
        else:
            raise HTTPException(status_code=404, detail="ella_id couldn't be found")

    def get_ella_service(self, ella_id, ella_service):
        welcome_page = self.get_welcome_page(ella_id)
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

    def send_contact_data(self, ella_id, data):
        if ella_id == 'ella_example_simple':
            msg = "Nachricht von: %s %s\r\n" % (data.vorname, data.name)
            msg += data.message
            msg['Subject'] = f'The contents of {textfile}'
            msg['From'] = data.email
            msg['To'] = "your.email@domain.de"
            # Senden der Nachricht über einen SMTP-Server
            try:
                s = smtplib.SMTP('localhost')
                s.send_message(msg)
                s.quit()
                return  {'success':True, 'message': 'Die Nachricht wurde erfolgreich gesendet'}
            except:
                return  {'success':False, 'message': sys.exc_info()[0]}
        raise HTTPExeption(status_code=404, detail="ella_service not found or not allowed in this context")

    #Your service stuff after this line
    #----------------------------------

