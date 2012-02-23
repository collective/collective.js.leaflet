import logging
from zope.i18nmessageid import MessageFactory
MessageFactory = collectivejsleafletMessageFactory = MessageFactory('collective.js.leaflet') 
logger = logging.getLogger('collective.js.leaflet')
def initialize(context):
    """Initializer called when used as a Zope 2 product.""" 
