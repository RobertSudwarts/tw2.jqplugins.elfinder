
import webob
import tw2.core as twc

from tw2.jqplugins.ui.base import JQueryUIWidget
from . import base

from v2_connector.connector import ElfinderConnector

# just leave this here for the time being -- it'll make life easier
from test_widgets import DemoWebobJSON, DemoTabsWidget


class elFinderWidget(JQueryUIWidget):

    resources = [base.elfinder_js, base.elfinder_css]
    template = 'mako:tw2.jqplugins.elfinder.templates.widget'
    jqmethod = "elfinder" # used by the template

    options = twc.Param(
        '(dict) A dict of options to pass to the widget', default={})

    # @classmethod
    # def request(cls, req):
    #     # You could, of course, use other controllers (say a tg2 controller)
    #     resp = webob.Response(request=req, content_type="text/html")
    #     resp.body = "<p>wow.. this came via <h4>ajax!</h4></p>"
    #     return resp


    def prepare(self):

        # we need to know the connector...
        #self.elf = ElfinderConnector(self.opts, session=None)

        #  You need some sort of assert to insist on `option`
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
