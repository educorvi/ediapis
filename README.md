ELLA - OpenApi für Fire and Forget Anwendungen
==============================================
Ella, elle l'a, Sängerin: France Gall, 1987
-------------------------------------------
deutsche Übersetzung: "Ella hat es."

Mit diesem Projekt wird ein OPEN-API-Contract zwischen einer Frontend-Applikation (z.B.: einer Progressive Webapp, einer App, einer
Website oder einer Unternehmens-Software) und den dafür benötigten Backend-Systemen geschlossen. Als Backends kommen in Frage:

Frontend-Applikationen (wir sprechen von der **ella_app**) können sein:

- eine Progressive Webapp (PWA)
- eine Website oder eine in die Seite eingebette Applikation
- eine Unternehmens-Software auf der Kundenseite

Backend-Applikationen (wir sprechen von **ella_backends**) können sein:

- ein Datenbank-Management-System
- ein Content-Management-System
- die Unternehmenssoftware des Anbieters
- ein CRM-System

ELLA ist die Komponente zwischen den Welten. Die Aufgabe von ELLA besteht darin, die verschiedenen internen Schnittstellen zu
kapseln und nach aussen OPEN-API's anzubieten wie die folgende Abbildung verdeutlichen soll.


Funktionsweise
--------------




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

Entwicklung:

uvicorn app.main:app --reload

Produktion:

gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornH11Worker&

