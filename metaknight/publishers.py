# -*- coding: utf-8 -*-
from nap import rest
from nap.rest.api import Api
from varlet.publishers import PagePublisher
from varlet.publishers import PageSerialiser


class MKPagePublisher(PagePublisher):
    pass


v1_api = Api('v1')
v1_api.register(MKPagePublisher, name='pages')
rest.api.register('pages', MKPagePublisher)
