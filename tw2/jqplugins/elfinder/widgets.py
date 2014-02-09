
import webob
import tw2.core as twc
import logging
from pprint import pprint

from tw2.jqplugins.ui.base import JQueryUIWidget
from . import base

from v2_connector.connector import ElfinderConnector

# just leave this here for the time being -- it'll make life easier
from test_widgets import DemoWebobJSON, DemoTabsWidget

try:
    import simplejson as json
except:
    import json

log = logging.getLogger(__name__)



class elFinderWidget(JQueryUIWidget):

    # demonstrates that you can add styles etc to the div.
    attrs = {'style': 'margin:10px 70px;'}

    resources = [base.elfinder_js, base.elfinder_css]
    template = 'mako:tw2.jqplugins.elfinder.templates.widget'

    elfinder_connector = twc.Param("the elfinder connector object", default=None)

    # controller_prefix -- you may want to add this...?
    options = twc.Param(
        '(dict) A dict of options to pass to the widget', default={})


    @classmethod
    def request(cls, req):

        # so if we declare elf, we seem to be
        # able to get to it here....
        log.info("connector version: %s", cls.elfinder_connector._version)
        log.info("connector commit: %s", cls.elfinder_connector._commit)

        #log.warn( "request : %s", req)
        #log.warn( "you have a: %s", type(cls.elf))
        #pprint (req.environ)
        #log.warn ("remote user: %s", req.remote_user)

        params = req.GET.items()
        # `params` is a nice list of tuples
        log.info( "request parameters: %s", params )
        # gies you GET([(u'cmd', u'open'), (u'target', u''), (u'init', u'1'),
        #        (u'tree', u'1'), (u'_', u'1391791794412')])

        resp = webob.Response(request=req, content_type="application/json")

        # Well, the data returned has to look like this... !
        #data = {"files": [{"dirs": 1, "hash": "llff_Lw", "name": "ElfinderFiles", "read": 1, "volumeid": "llff_", "ts": 1391529220.7605991, "write": 1, "mime": "directory", "locked": 1, "hidden": 0, "size": "unknown"}, {"hash": "llff_SGVpZHlL", "name": "HeidyK", "read": 1, "ts": 1391529232.552599, "write": 1, "mime": "directory", "phash": "llff_Lw", "locked": 0, "hidden": 0, "size": "unknown"}, {"hash": "llff_dGVzdF9zdHVkZW50XzM", "name": "test_student_3", "read": 1, "ts": 1391779717.6250036, "write": 1, "mime": "directory", "phash": "llff_Lw", "locked": 0, "hidden": 0, "size": "unknown"}, {"hash": "llff_TG9va3NMaW5lQW5Pcmdhbi5wZGY", "name": "LooksLineAnOrgan.pdf", "read": 1, "ts": 1391527013.0, "write": 1, "mime": "application/pdf", "phash": "llff_Lw", "locked": 0, "hidden": 0, "size": 109218}, {"hash": "llff_SGFtbW9uZE9yZ2FuLnBkZg", "name": "HammondOrgan.pdf", "read": 1, "ts": 1391527013.6926498, "write": 1, "mime": "application/pdf", "phash": "llff_Lw", "locked": 0, "hidden": 0, "size": 109218}, {"hash": "llff_YWxsX3Rlc3RzLnR4dA", "name": "all_tests.txt", "read": 1, "ts": 1391527366.7286417, "write": 1, "mime": "text/x-python", "phash": "llff_Lw", "locked": 0, "hidden": 0, "size": 161577}, {"dim": "158x204", "hash": "llff_Y2hhcmxpZXdfMS5qcGc", "name": "charliew_1.jpg", "read": 1, "ts": 1391528898.1966066, "write": 1, "tmb": "llff_Y2hhcmxpZXdfMS5qcGc1391528898.2.png", "mime": "image/jpeg", "phash": "llff_Lw", "locked": 0, "hidden": 0, "size": 5383}, {"hash": "llff_dGVzdC50eHQ", "name": "test.txt", "read": 1, "ts": 1391527382.7806413, "write": 1, "mime": "text/plain", "phash": "llff_Lw", "locked": 0, "hidden": 0, "size": 0}], "uplMaxSize": 134217728, "options": {"disabled": [], "copyOverwrite": 1, "separator": "/", "pathUrl": "/media/files/", "url": "/media/files/", "path": "Elfinder files", "tmbUrl": "/media/files/.tmb/", "archivers": {"create": ["application/x-tar", "application/x-bzip2", "application/x-gzip", "application/zip"], "extract": ["application/x-tar", "application/x-bzip2", "application/x-gzip", "application/zip"]}}, "netDrivers": [], "api": "2.0", "cwd": {"dirs": 1, "hash": "llff_Lw", "name": "Elfinder files", "read": 1, "volumeid": "llff_", "ts": 1391529220.7605991, "write": 1, "mime": "directory", "locked": 1, "hidden": 0, "size": "unknown"}}
        data = cls.elfinder_connector.execute(u'open', target=u'llff_Lw', tree=True, init=True)
        resp.body = json.dumps( data )

        return resp


    def prepare(self):

        # the only 'required' parameter is the url to the controller.
        self.options['url'] = "/tw2_controllers/" + self.id

        # The controller has to know where/what to open as root.
        # Essentially this would be the Entity's root directory.
        #self.options['customData'] = {'entity_type':'student',
        #                              'entity_id': 'blahblahblah'}
        # something like this req'd to curtail permissions...
        #self.options['customData'] = {'user_id': 42}

        super(elFinderWidget, self).prepare()


# if you give the widget an id, eg demo-tebs, tw2.core.middleware
# will register the controller you can call tw2_controllers/demo-tabs
# and you'll bump the `request` (so, the href for the tab item would
# have to call this accordingly).  However, by registering the controller
# (as below) the href can call it... (look at it closely and it makes sense)
# this is required here...
#print "I AM REGISTERING THE RESOURCE...."
#twc.register_controller(elFinderWidget, 'elfcontrol')
# see http://toscawidgets.org/documentation/tw2.core/design.html#widgets-as-controllers
#mw = twc.core.request_local()['middleware']
#mw.controllers.register(elFinderWidget, 'mywidget')
