from zope.traversing.adapters import DefaultTraversable
import os
import sys
import zope

zope.component.provideAdapter(DefaultTraversable, [None])
cwd = os.path.dirname(__file__)

FF2_USERAGENT = "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1.14) " +\
                "Gecko/20080404 Firefox/2.0.0.14"
GENTOO_FF_UA = "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.3) " +\
               "Gecko/20090912 Gentoo Shiretoko/3.5.3"


def get_interfaces(o):
    return [o for o in o.__provides__.interfaces()]


def errprint(msg):
    """Writes 'msg' to stderr and flushes the stream."""
    sys.stderr.write(msg)
    sys.stderr.flush()


def pstriplist(s):
    print '\n'.join([a.rstrip() for a in s.split('\n') if a.strip()])


class Request(zope.publisher.browser.TestRequest):
    def __setitem__(self, name, value):
        self._environ[name] = value
TestRequest = Request


def make_request(url='http://nohost/@@myview', form=None, *args, **kwargs):
    r = Request(environ={'SERVER_URL': url, 'ACTUAL_URL': url},
                form=form, *args, **kwargs)
    zope.interface.alsoProvides(
            r,
            zope.annotation.interfaces.IAttributeAnnotatable)
    return r


# if you have plone.reload out there add an helper to use in doctests while
# programming just use preload(module) in pdb :) it would be neccessary for you
# to precise each module to reload, this method is also not recursive.  eg:
# (pdb) from foo import bar;preload(bar)
def preload(modules_or_module, excludelist=None):
    try:
        modules = modules_or_module
        if not (isinstance(modules_or_module, list)
                or isinstance(modules_or_module, tuple)):
            modules = [modules_or_module]
        if not excludelist:
            excludelist = []
        import sys
        if not modules:
            modules = sys.modules
        from plone.reload.xreload import Reloader
        for module in modules:
            if not module in excludelist:
                try:
                    Reloader(module).reload()
                except Exception, e:
                    pass
    except Exception, e:
        print "Cant reload code: %s " % e

# vim:set et sts=4 ts=4 tw=80:
