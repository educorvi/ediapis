ELLA - OpenApi für "Fire and Forget" Applikationen
==================================================
Ella, elle l'a, Sängerin: France Gall, 1987 (deutsch: "Ella hat es.")
---------------------------------------------------------------------

Mit diesem Projekt wird ein OpenApi-Kontrakt zwischen einer Frontend-Applikation (**ella_app**) und 
einem oder mehreren Backend-Systemen (**ella_backend**) geschlossen. 

**ella_apps** sind Anwendungen, die nach dem "Fire and Forget" Prinzip funktionieren. Beispiele sind:

- Umfragen (Surveys) zu bestimmten Themenstellungen,
- Checklisten mit einfachen Auswertungen,
- Einfache Formulare für Anträge, Abonnements, Kontaktinformationen, Beschwerdemanagement,
- Online-Quizzes

Solche Anwendungen stehen heute in ganz verschiedenen Umgebungen für diverse Endgeräte zur Verfügung:

- als App oder Progressive Webapp (PWA)
- als Bestandteil einer Website bzw. als eine in die Seite eingebette Applikation (z.B. Umfragen auf Spiegel-Online)
- als Teil einer Unternehmens-Anwendung bzw. als Service im Intranet (Büromaterialbestellung, Büro-CheckIn, etc.)

**ella_backends** sind die Systeme zur Bereitstellung der Informationen und Formulare für die **ella_app** 
oder zum Empfang bzw.zur Auswertung der Daten und Informationen. Beispiele sind:

- ein Content-Management-System (CMS)
- ein E-Mailserver 
- eine Datenbank
- die Branchensoftware des Service-Anbieters
- ein CRM-System

Was ELLA ist
------------

ELLA ist die Komponente zwischen den beiden Welten. Die Aufgabe von ELLA besteht darin, die verschiedenen internen Schnittstellen zu
kapseln und nach aussen OpenApi-Kontrakte anzubieten wie die folgende Abbildung zeigt:

![ELLA-Konfiguration](./doc/images/ella_konfig.jpg "Ella-Konfiguration")

- ELLA ist die praktische Anwendung des OpenApi Standards für "Fire and Forget" Applikationen
- ELLA ist eine Sammlung von Klassendefinitionen und Funktionen, die eine Realisierung solcher Anwendungen erleichtern sollen
- ELLA ist ein dokumentiertes "HowTo" für Einsteiger in die Entwicklung von python-basierten Web-Applikationen
- ELLA bietet funktionale Beispiel-Apis für die Entwickler von Apps und Progressive Webapps
- ELLA ist Programmcode und Dokumentation auf dem Rücken eines kleinen Giganten - dem Python-Microframework FastAPI 
  (https://fastapi.tiangolo.com/) - vielen Dank #@tiangolo - Sebastian Ramirez (https://github.com/tiangolo)

Was ELLA nicht ist
------------------

- ELLA ist kein technischer oder fachlicher Framework
- ELLA selbst persistiert keine Daten, wenn Daten gespeichert werden müssen erfolgt das in einem **ella_backend**
- ELLA erhebt keinen Anspruch auf Vollständigkeit und Richtigkeit im Hinblick auf den Funktionsumfang oder die angewendeten
  Programmiertechniken - es gibt so viele bessere Programmierer...

Funktionsweise
--------------

### Fire and Forget Applikationen

Mit ELLA werden leichtgewichtige "Fire and Forget" Applikationen mit OpenApi's versorgt. Damit sollen Front-End-Entwickler
in die Lage versetzt werden, standardisiert und schnell zugleich eine kleine App oder Progressive Webapp (PWA) zu entwickeln,
die auf den folgenden Prinzipien beruht:

- Eine **Welcome** - Seite mit Richtext (z.B. HTML, Markdown, Restructured Text...). Mit der Welcome-Page wird eine Liste 
  von **Services** ausgeliefert, die dem Benutzer beispielsweise über ein Hamburger Menü angeboten werden können.
- **Services** können sein:
    - eine Seite (type=page) mit weiteren Informationen
    - ein formularbasierter Service (type=service)
    - eine Gruppe von Services (Seiten oder Formulare)
- **Aktions** werden durch Buttons repräsentiert. Sie dienen der Annahme, Weiterleitung oder Verarbeitung der Daten über die
  formularbasierten Services. Da ELLA selbst keine Daten speichert handelt es sich um "Fire and Forget" Aktionen, wie z.B.
    - das Senden bzw. die Weiterleitung an einen Backend per Schnittstelle oder E-Mail
    - das Drucken von Daten in ein PDF-Formular (auch in Kombination mit dem Senden)
    - das Teilen von Informationen (z.B. auf einer Website oder in sozialen Netzwerken)
    - die Überprüfung bzw. Validierung von Daten (z.B. Validierung einer Checkliste oder eines Quizzes)

Die folgende Abbildung zeigt den Aufbau einer "Fire and Forget" Applikation auf Basis des ELLA OpenApi-Kontrakts.

![Aufbau einer Fire and Forget Applikation](./doc/images/ella_template.jpg "Aufbau einer Fire an Forget Applikation")

### OpenApi-Kontrakt für Web-Formulare

Mit ELLA ist ein Python-Entwickler sehr schnell in der Lage, einen OpenAPI-Kontrakt für den Empfang von Daten aus einem
Web-Formular zu entwickeln.

 

- Ein Impressum
- 




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

