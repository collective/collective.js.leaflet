from zope import interface
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ILeafletMapView(interface.Interface):
    """Marker interface"""


class LeafletMapView(BrowserView):
    """XCGUtils an image after being edited on a webservice"""
    interface.implements(ILeafletMapView)
    template = ViewPageTemplateFile('map.pt')

    def __call__(self, **params):
        params = {}
        return self.template(**params)

# vim:set et sts=4 ts=4 tw=80:
