# -*- coding: utf-8 -*-
# # Copyright (c) 2016-2020 educorvi GmbH & Co. KG
# # lars.walther@educorvi.de
from .models import Welcome, ServiceDescription, GroupServiceDescription, FormDescription, UISchema, ServiceButton

def createForm(form):
    ella_form = FormDescription(
            name = form.get('name'),
            title = form.get('title'),
            description = form.get('description'),
            type = 'object',
            properties = form.get('properties'),
            required = form.get('required'),
            )
    return ella_form

def createServiceButtons(formactions):
    ella_buttons = []
    for button in formactions:
        ella_button = ServiceButton(
                name = button.get('name'),
                title = button.get('title'),
                cssclass = button.get('cssclass'),
                method = button.get('method'))
        if button.get('additional'):
            ella_button.additional = button.get('additional')
        ella_buttons.append(ella_button)
    return ella_buttons

def createFormService(service):
    ella_service = ServiceDescription(
            name = service.get('name'),
            title = service.get('title'),
            description = service.get('description'),
            type = 'service',
            form = createForm(service.get('form')),
            ui = UISchema(type = "VerticalLayout", elements = service.get('ui')),
            formactions = createServiceButtons(service.get('formactions'))
            )
    return ella_service

def createPageService(service):
    ella_service = ServiceDescription(
            name = service.get('name'),
            title = service.get('title'),
            description = service.get('description'),
            type = 'page',
            text = service.get('text')
            )
    return ella_service

def createGroupFormService(service):
    ella_service = GroupServiceDescription(
            name = service.get('name'),
            title = service.get('title'),
            description = service.get('description'),
            type = 'service',
            form = createForm(service.get('form')),
            ui = UISchema(type = "VerticalLayout", elements = service.get('ui')),
            formactions = createServiceButtons(service.get('formactions'))
            )
    return ella_service

def createGroupPageService(service):
    ella_service = GroupServiceDescription(
            name = service.get('name'),
            title = service.get('title'),
            description = service.get('description'),
            type = 'page',
            text = service.get('text')
            )
    return ella_service   

def createGroupService(service):
    ella_subservices = list()
    subservices = service.get('services')
    for subservice in subservices:
        typ = subservice.get('type')
        if typ == 'service':
            ella_subservices.append(createGroupFormService(subservice))
        else:
            ella_subservices.append(createGroupPageService(subservice))
    ella_service = ServiceDescription(
            name = service.get('name'),
            title = service.get('title'),
            description = service.get('description'),
            type = 'group',
            services = ella_subservices
            )
    return ella_service

def ellaview2welcome(raw):
    services = raw.get('services')
    ella_services = list()
    for service in services:
        typ = service.get('type')
        if typ == 'group':
            ella_services.append(createGroupService(service))
        elif typ == 'service':
            ella_services.append(createFormService(service))
        elif typ == 'page':
            ella_services.append(createPageService(service))
    ella_welcome = Welcome(
        name = raw.get('name'),
        title = raw.get('title'),
        description = raw.get('description'),
        bodytext = raw.get('bodytext'),
        services = ella_services
        )
    return ella_welcome
