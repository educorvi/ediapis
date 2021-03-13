# -*- coding: utf-8 -*-
# # Copyright (c) 2016-2020 educorvi GmbH & Co. KG
# # lars.walther@educorvi.de

from .models import Welcome, ServiceDescription, ServiceButton, FormDescription, FormData
from .models import EllaContact, ContactResponse, ResponseData
from .services import EllaServices
from fastapi import FastAPI

app = FastAPI(
    title="ELLA",
    description="OpenApi für 'Fire and Forget' Applikationen",
    version="0.9",
)
services = EllaServices()

@app.get("/")
def read_root():
    """'Ella, elle l'a' (France Gall) Die OpenApi für Deine ella_app ist online."""
    return(u"'Ella, elle l'a' (France Gall) Die OpenApi für Deine ella_app ist online.")


@app.get("/{ella_id}", response_model=Welcome)
def read_ella_root(ella_id:str):
    """ Liefert die Welcome-Page Deiner ella_app zurück. Das folgende Beispiel kannst Du
        ausprobieren:
        - ella_id = ella_example_simple
    """
    return services.get_welcome_page(ella_id)


@app.get("/{ella_id}/{ella_service}", response_model=ServiceDescription)
def read_ella_service(ella_id:str, ella_service:str):
     """ Liefert den gewünschten Service für Deine ella_app zurück. Folgende Beispiele kannst Du
         ausprobieren:
         - ella_id = ella_example_simple
         - ella_service:
             - ella_simple_page
             - ella_simple_service
             - ella_simple_group
     """
     return services.get_ella_service(ella_id, ella_service)


@app.post("/{ella_id}/{ella_service}/pdf", response_model=ResponseData)
def get_pdf(ella_id:str, ella_service:str, data:FormData):
    """Die ella Applikation sendet die Daten passend zu einer Servicebeschreibung. Es wird ein
       PDF-Dokument zurückgesendet.
    """
    return services.get_pdfexample(ella_id, ella_service, data)

@app.post("/{ella_id}/{ella_service}/mail", response_model=ResponseData)
def get_pdf(ella_id:str, ella_service:str, data:FormData):
    """Die ella Applikation sendet die Daten passend zu einer Servicebeschreibung.
    """
    return services.get_mailexample(ella_id, ella_service, data)

@app.post("/{ella_id}/{ella_service}/link", response_model=ResponseData)
def get_pdf(ella_id:str, ella_service:str, data:FormData):
    """Die ella Applikation sendet die Daten passend zu einer Servicebeschreibung.
    """
    return services.get_linkexample(ella_id, ella_service, data)

@app.post("/{ella_id}/contact/send", response_model=ContactResponse)
def get_data(ella_id:str, data:EllaContact):
    """Die ella Applikation sendet die Daten passend zum EllaContact Formular. Die Daten werden
       angenommen und weitergeleitet.
    """
    return services.send_contact_data(ella_id, data)
