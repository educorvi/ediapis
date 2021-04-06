# -*- coding: utf-8 -*-
# # Copyright (c) 2016-2020 educorvi GmbH & Co. KG
# # lars.walther@educorvi.de
import base64
import sys
import smtplib
import requests
from fastapi import HTTPException
from .examples import example_apps, example_services
from .models import ResponseData
from .converter import ellaview2welcome
from .private import BASE_URL, USER, PW, APPS
from printfiverules.pdfprinter import PdfPrinter
from .persistance import writeDocToDatabase, readDocFromDatabase

class EllaServices(object):

    def __init__(self):
        session = requests.Session()
        session.auth = (USER, PW)
        session.headers.update({'Accept': 'application/json'})
        self.session = session

    def get_welcome_page(self, ella_id:str):
        if ella_id == 'ella_example_simple':
            welcome = example_apps.get(ella_id)
            return welcome
        elif ella_id in APPS:
            url = APPS.get(ella_id) + '/ella-view'
            rawwelcome = self.session.get(url)
            rawwelcome = rawwelcome.json()
            welcome = ellaview2welcome(rawwelcome)
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

    def get_ellapdf(self, ella_id, ella_service, data):
        ellaprinter = PdfPrinter()
        pdfprint = getattr(ellaprinter, ella_service)
        printdata = dict()
        printdata['data'] = data.form
        docid = writeDocToDatabase(data.form)
        printdata['docid'] = docid
        print(printdata)
        pdfstring = pdfprint(printdata)
        filepath = '/tmp/%s.pdf' % docid
        content = open(filepath, 'rb')
        filedata = base64.b64encode(content.read())
        filename = '%s.pdf' % ella_service
        return ResponseData(type = 'file',
                content = filedata,
                encoding = 'base64',
                filename = filename,
                mimeType = 'application/pdf')

    def get_ellamail(self, ella_id, ella_service, data):
        docid = writeDocToDatabase(data.form)
        url = 'https://ella.uv-kooperation.de/%s/%s/docprinter/%s' % (ella_id, ella_service, docid)
        return ResponseData(type = 'email',
                content = url,
                encoding = 'utf-8')

    def get_ellaprint(self, ella_id, ella_service, doc_id):
        ellaprinter = PdfPrinter()
        pdfprint = getattr(ellaprinter, ella_service)
        document = readDocFromDatabase(doc_id)
        printdata = dict()
        printdata['data'] = document
        printdata['docid'] = doc_id
        pdfstring = pdfprint(printdata)
        filepath = '/tmp/%s.pdf' % doc_id
        filename = '%s.pdf' % ella_service
        return {'filedata':filepath, 'filename':filename}

    def get_ellalink(self, ella_id, ella_service, data):
        if ella_id == 'ella_example_simple':
            return ResponseData(type = 'link',
                content = 'mailto:subject=Beispiel-Fragebogen&body=http://www.bgetem.de',
                encoding = 'utf-8')
        else:
            raise HTTPException(status_code=404, detail="ella_service not found or not allowed in this context")        
