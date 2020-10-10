API's der educorvi GmbH
=======================

Dieses Projekt umfasst die API-Schnittstellen für die Software-Projekte der educorvi GmbH & Co. KG. Das Projekt basiert auf FastApi und uvicorn.

Installation
------------

- git clone https://github.com/educorvi/ediapis.git
- cd ediapis
- python3 -m venv env
- source ./env/bin/activate
- pip install -r requirements.txt
- pip install -r dev-requirements.txt

Starten und Stoppen des API-Servers
-----------------------------------

uvicorn app.main:app --reload
