# -*- coding: utf-8 -*-
# # Copyright (c) 2016-2020 educorvi GmbH & Co. KG
# # lars.walther@educorvi.de

import requests
from .models import Welcome, ServiceDescription, ServiceButton, FormDescription, UISchema, GroupServiceDescription
from .carousel import carousel

songtext = u"""\
<h2>Strophe 1</h2>
<p>Es ist wie eine Art Fröhlichkeit, wie ein Lächeln<br/>
Irgendwas liegt in dieser Stimme,<br/>
Das uns zu sagen scheint: "Komm!"<br/>
Das uns ein seltsames Wohlgefühl verschafft<br/>
Es ist wie die ganze Geschichte der Schwarzen,<br/>
Die immer zwischen Liebe und Verzweiflung schwankt.<br/>
Wie etwas, das in dir drin tanzt<br/>
Wenn du es hast, dann hast du’s.<br/>
</p>
<h2>Strophe 2</h2>
<p>Ella hat es.<br/>
Dieses gewisse Etwas,<br/>
Das andere nicht haben<br/>
Das uns in diesen seltsamen Zustand versetzt.<br/>
Ella hat es.<br/>
Ella hat es.<br/>
Dieses seltsame Etwas in ihrer Stimme<br/>
Diese Wonne darin<br/>
Diese Himmelsgabe,<br/>
Die sie so schön macht.<br/>
Ella hat es.<br/>
Ella hat es.<br/>
</p>
"""

steckbrief = """\
<p>France Gall war eine französische Pop- und Schlagersängerin. Nach einem erfolgreichen
Karrierestart in Frankreich gewann sie 1965 für Luxemburg den Grand Prix Eurovision
mit dem Titel Poupée de cire, poupée de son.</p>
<ul>
<li><strong>Geboren:</strong> 9. Oktober 1947, Paris, Frankreich</li>
<li><strong>Gestorben:</strong> 7. Januar 2018, Amerikanisches Krankenhaus Paris,
                                Neuilly-sur-Seine, Frankreich</li>
<li><strong>Ehepartner:</strong> Michel Berger (verh. 1976–1992)</li>
<li><strong>Kinder:</strong> Raphaël Hamburger, Pauline Hamburger</li>
<li><strong>Musikgruppe:</strong> Les Enfoirés (1993 – 1994)</li>
</ul>
"""

formfields = {u'vorname':{u'description':u'Dein Vorname', u'type':u'string'},
              u'name':{u'description':u'Dein Name', u'type':'string'},
              u'age':{u'description':u'Dein Alter', u'type':'number', u'minimum':18, u'maximum':67},
              u'geschmack':{u'description':u'Dein Musikgeschmack',u'type':u'array',
                           u'enum':['Pop','Rock','Klassik','Jazz'], u'uniqueItems':True}
             }

reqfields = ['name', 'age', 'geschmack']

def get_five(url):
    url = url + "/schema-view"
    fiverules = requests.get(url, headers={'Accept': 'application/json'})
    data = fiverules.json()
    retdict = dict()
    retdict['title'] = data.get('title')
    retdict['description'] = data.get('description')
    retdict['props'] = data.get('properties')
    retdict['req'] = data.get('required')
    return retdict

def get_five_ui(url):
    url = url + "/ui-schema-view"
    ui = requests.get(url, headers={'Accept': 'application/json'})
    data = ui.json()
    return data

def get_welcome():
    url = "https://new-etem-praev.bg-kooperation.de/anwendungen/5-sicherheitsregeln/5-sicherheitsregeln"
    ui = requests.get(url, headers={'Accept': 'application/json'})
    html = ui.json()
    text = html.get('text')
    title = html.get('title')
    return {'title':title, 'text':text.get('data')}

def get_bodytext(url):
    body = requests.get(url, headers={'Accept': 'application/json'})
    html = body.json()
    text = html.get('text')
    title = html.get('title')
    description = html.get('description')
    return {'title':title, 'description':description, 'text':text.get('data')}

url1 = "https://new-etem-praev.bg-kooperation.de/anwendungen/5-sicherheitsregeln/elektrohandwerk/arbeiten-an-schaltanlagen-in-der-niederspannung"
url2 = "https://new-etem-praev.bg-kooperation.de/anwendungen/5-sicherheitsregeln/elektrohandwerk/elektrohandwerk-arbeiten-an-ns-unterverteilungen" 
url3 = "https://new-etem-praev.bg-kooperation.de/anwendungen/5-sicherheitsregeln/elektrohandwerk/elektrohandwerk-arbeiten-an-endstromkreisen"
url_impressum = "https://new-etem-praev.bg-kooperation.de/anwendungen/5-sicherheitsregeln/impressum"

fb1 = get_five(url = url1)
fb2 = get_five(url = url2)
fb3 = get_five(url = url3)

ui1 = get_five_ui(url = url1)
ui2 = get_five_ui(url = url2)
ui3 = get_five_ui(url = url3)

impressum = get_bodytext(url = url_impressum)

additional = {
  "type": "object",
  "properties": {
    "erlaubnis": {
      "title": "Erlaubnis zur Speicherung über 48 Tage.",
      "type": "boolean",
    },
    "datenschutz": {
      "title": "Datenschutz gelesen und einverstanden.",
      "type": "boolean"
    }
  },
  "required": ["erlaubnis", "datenschutz"]
}

def format_single(artikel):
    startseite = """<div class="card mb-3">"""
    if artikel.get('img'):
        startseite += """<img src="%s" class="card-img-top" alt="Titelbild der App">""" % artikel.get('img')
    startseite += """<div class="card-body">
    <h5 class="card-title">%s</h5>
    %s
  </div>
</div>
""" % (artikel.get('title'), artikel.get('text'))
    return startseite

def format_pages(artikel):
    startseite = format_single(artikel[0])
    navigation = """\
<nav aria-label="Navigation">
  <ul class="pagination justify-content-center">
    <li class="page-item active"><a class="page-link" href="#/services/%s">1</a></li>""" % artikel[0].get('id')
    page = 2
    for i in artikel[1:]:
        navigation += """<li class="page-item"><a class="page-link" href="#/services/%s">%s</a></li>""" % (i.get('id'), str(page))
        page += 1
    navigation += """</ul></nav>"""
    startseite = startseite + navigation
    return startseite

def get_newwelcome():
    url = "https://new-etem-praev.bg-kooperation.de/anwendungen/5-sicherheitsregeln/ueber-diese-app-1/ella-view"
    result = requests.get(url, headers={'Accept': 'application/json'})
    artikel = result.json()
    text = format_single(artikel[0])
    if len(artikel) > 1:
        text = format_pages(artikel)
    title = artikel[0].get('title')
    description = artikel[0].get('description')
    img = artikel[0].get('img')
    return {'title':title, 'description':description, 'text':text, 'img':img}

newwelcome = get_newwelcome()

example_group_services = {
                    'fragen1': GroupServiceDescription(name = u"fragen1",
                        title = u"Fragebogen-1",
                        description = u"Das ist ein Beispiel",
                        type = u"service",
                        ui = UISchema(type = "VerticalLayout", elements = ui1),
                        form = FormDescription(name = u"S143",
                            title=u"Arbeiten an Schaltanlagen in der Niederspannung, Trafostationen (unterspannungsseitig)",
                            description=u"",
                            type = u"object",
                            properties = fb1['props'],
                            required = fb1['req']),
                            formactions = [ServiceButton(name=u"pdf", title=u"Drucken", cssclass=u"info",
                                                         method=u"POST")]),
                    'fragen2': GroupServiceDescription(name = u"fragen2",
                        title = u"Fragebogen-2",
                        description = u"Das ist ein weiteres Beispiel",
                        type = u"service",
                        ui = UISchema(type = "VerticalLayout", elements = ui2),
                        form = FormDescription(name = u"S144",
                            title=u"Arbeiten an Unterverteilungen in der Niederspannung",
                            description=u"",
                            type = u"object",
                            properties = fb2['props'],
                            required = fb2['req']),
                            formactions = [ServiceButton(name=u"pdf", title=u"Drucken", cssclass=u"info",
                                                         method=u"POST")])
                    }

def create_navigations(artikel):
    naventries = []
    page = 1
    for i in artikel:
        naventries.append("""<li class="page-item edi_active"><a class="page-link" href="#/services/%s">%s</a></li>""" % (i.get('id'), str(page)))
        page += 1
    navs = []
    for i in range(len(artikel)):
        navigation = """\
<nav aria-label="Navigation">
  <ul class="pagination justify-content-center">"""
        for k in range(len(naventries)):
            naventry = naventries[k]
            if i == k:
                naventry = naventry.replace(u'edi_active', u'active')
            else:
                naventry = naventry.replace(u'edi_active', u'')
            navigation += naventry    
        navigation += """</ul></nav>"""
        navs.append(navigation)
    return navs


def get_hilfen():
    url = "https://new-etem-praev.bg-kooperation.de/anwendungen/5-sicherheitsregeln/ueber-diese-app-1/ella-view"
    result = requests.get(url, headers={'Accept': 'application/json'})
    artikel = result.json()
    navigations = create_navigations(artikel)
    hilfen = []
    for art, nav in zip(artikel, navigations):
        groupentry = GroupServiceDescription(name = art.get('id'),
                         title = art.get('title'),
                         description = art.get('description'),
                         type = u"page",
                         text = (format_single(art) + nav))
        hilfen.append(groupentry)
    return hilfen

example_services = {'ella_simple_page': ServiceDescription(name = u"ella_simple_page",
                        title = u"Steckbrief France Gall",
                        description = u"Wichtige biografische Stationen der Sängerin France Gall",
                        type = u"page",
                        text = steckbrief),
                    'ella_simple_service': ServiceDescription(name = u"ella_simple_service",
                        title = u"Fragebogen Musikinteresse",
                        description = u"Mit diesem Fragebogen teilst Du Dein Musikinteresse mit uns.",
                        type = u"service",
                        form = FormDescription(name = u"ella_simple_service",
                            title = u"Fragebogen Musikinteresse",
                            description =u"Mit diesem Fragebogen teilst Du Dein Musikinteresse mit uns.",
                            type = u"object",
                            properties = formfields,
                            required = reqfields),
                        formactions = [ServiceButton(name=u"pdf", title=u"Drucken", cssclass=u"btn btn-primary",
                                                         method=u"POST")]),
                    'evu': ServiceDescription(name = u"evu",
                        title = u"Energieversorgungsunternehmen",
                        description = u"Gruppe mit Services",
                        type = u"group",
                        services = [example_group_services['fragen1'], example_group_services['fragen2']]),
                    'pwa': ServiceDescription(name = u"pwa",
                        title = u"Über diese App",
                        description = u"Hilfen zur Bedienung",
                        type = u"group",
                        services = get_hilfen()),
                    'impressum': ServiceDescription(name = u"impressum",
                        title = impressum['title'],
                        description = impressum['description'],
                        type = u"page",
                        text = impressum['text']),
                    'fb1' : ServiceDescription(name = u"fb1",
                        title = fb1['title'],
                        description = fb1['description'],
                        type = u"service",
                        ui = UISchema(type = "VerticalLayout", elements = ui1),
                        form = FormDescription(name = u"S143",
                            title=u"Arbeiten an Schaltanlagen in der Niederspannung, Trafostationen (unterspannungsseitig)",
                            description=u"",
                            type = u"object",
                            properties = fb1['props'],
                            required = fb1['req']),
                            formactions = [
                                ServiceButton(name=u"pdf", title=u"Drucken", cssclass=u"info",method=u"POST"),
                                ServiceButton(name=u"mail", title=u"E-Mail", cssclass=u"secondary",method=u"POST", additional=additional)
                                ]
                            ),
                    'fb2' : ServiceDescription(name = u"fb2",
                        title = fb2['title'],
                        description = fb2['description'],
                        type = u"service",
                        ui = UISchema(type = "VerticalLayout", elements = ui2),
                        form = FormDescription(name = u"S144",
                            title=u"Arbeiten an Schaltanlagen in der Niederspannung, Trafostationen (unterspannungsseitig)",
                            description=u"",
                            type = u"object",
                            properties = fb2['props'],
                            required = fb2['req']),
                            formactions = [ServiceButton(name=u"pdf", title=u"Drucken", cssclass=u"info",
                                                         method=u"POST")]),
                    'fb3' : ServiceDescription(name = u"fb3",
                        title = fb3['title'],
                        description = fb3['description'],
                        type = u"service",
                        ui = UISchema(type = "VerticalLayout", elements = ui3),
                        form = FormDescription(name = u"S145",
                            title=u"Arbeiten an Endstromkreisen",
                            description=u"",
                            type = u"object",
                            properties = fb3['props'],
                            required = fb3['req']),
                            formactions = [ServiceButton(name=u"pdf", title=u"Drucken", cssclass=u"info",
                                                         method=u"POST")])
                  }


example_apps = {'ella_example_simple': Welcome(name = u"ella_example_simple",
                    title = newwelcome['title'],
                    description = newwelcome['description'],
                    bodytext = newwelcome['text'],
                    services=[
                        example_services['fb1'],
                        example_services['fb2'],
                        example_services['fb3'],
                        example_services['evu'],
                        example_services['pwa'],
                        example_services['impressum'],
                            ])
               }
