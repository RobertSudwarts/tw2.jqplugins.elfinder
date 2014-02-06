
import webob

# tw2-proper imports
import tw2.core as twc
import tw2.forms as twf

from tw2.jqplugins.ui import base as jquibase
import base as elfbase

from v2_connector.connector import ElfinderConnector

# just leave this here for the time being -- it'll make life easier
from test_widgets import DemoWebobJSON, DemoTabsWidget


class elFinderWidget(jquibase.JQueryUIWidget):

    resources = [jquibase.jquery_ui_js,
                 elfbase.elfinder_css,
                 elfbase.elfinder_js
                 ]

    opts = twc.params.Param('elfinder options', default=twc.params.Required)
    template = 'tw2.jqplugins.elfinder.templates.widget'

    @classmethod
    def request(cls, req):
        # You could, of course, use other controllers (say a tg2 controller)
        resp = webob.Response(request=req, content_type="text/html")
        resp.body = "<p>wow.. this came via <h4>ajax!</h4></p>"
        return resp


    def prepare(self):

        # we need to know the connector...
        self.elf = ElfinderConnector(self.opts, session=None)

        self.options = {'URL':'/'}

        #if 'url' not in self.options:
        #    assert hasattr(self, 'url'), 'No url provided.   Please supply the url parameter'
        #    self.options['url'] = self.url

        super(elFinderWidget, self).prepare()


# if you give the widget an id, eg demo-tebs, tw2.core.middleware
# will register the controller you can call tw2_controllers/demo-tabs
# and you'll bump the `request` (so, the href for the tab item would
# have to call this accordingly).  However, by registering the controller
# (as below) the href can call it... (look at it closely and it makes sense)
# this is required here...
#print "I AM REGISTERING THE RESOURCE...."
#twc.register_controller(elFinderWidget, 'someurl')
