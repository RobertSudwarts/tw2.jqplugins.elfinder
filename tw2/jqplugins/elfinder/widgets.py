
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

    #connector_options = twc.Param(
    #    '(dict) A dict of options to pass to the widget', default={})

    #elfinder_connector = None
    elfinder_connector = twc.Param(
        'the elfinder connector object', default=None)

    # controller_prefix -- you may want to add this...?
    options = twc.Param(
        '(dict) A dict of options to pass to the widget', default={})


    @classmethod
    def request(cls, req):

        log.info("your connector is: %s", cls.elfinder_connector)

        if req.method == 'GET':
            req_items = req.GET.items()
            # `params` is a nice list of tuples -- but you're better off with req.params
            #log.info( "request parameters: %s", req_items )

            try:
                cmd = req.params['cmd']
            except KeyError:
                cmd = 'open'

            args = {}
            # build args appropriate for the command/cmd
            for name in cls.elfinder_connector.commandArgsList(cmd):
                if name == 'request':
                    args['request'] = req
                elif name == 'FILES':
                    args['FILES'] = req.FILES
                elif name == 'targets':
                    args[name] = req.params['targets[]']
                else:
                    arg = name
                    if name.endswith('_'):
                        name = name[:-1] # gets rid of timestamp
                    if name in req.params:
                        try:
                            args[arg] = req.params[name].strip()
                        except:
                            args[arg] = req.params[name]
                args['debug'] = req.params['debug'] if 'debug' in req.params else False

            # wait just a second... it works....!
            # so why are you getting those errors????

            #data = cls.elfinder_connector.execute(cmd, **args)

            # the first time you run, nothing seems to get passed....
            # so you NEED this line until you've sorted it out.
            data = cls.elfinder_connector.execute(u'open', target=u'llff_Lw', tree=True, init=True)

            resp = webob.Response(request=req, content_type="application/json")

            resp.body = json.dumps( data )

            return resp

        elif req.method == 'POST':
            #  for uploads...
            log.warn("You got a POST")

        else:
            log.warn("req.method=%s : unhandled", req.method)




    def prepare(self):

        #self.elfinder_connector = ElfinderConnector(opts=self.connector_options)
        log.info("prepare: your connector is: %s", self.elfinder_connector)

        # the only 'required' parameter is the url to the controller, see
        # https://github.com/Studio-42/elFinder/wiki/Client-configuration-options
        self.options['url'] = "/tw2_controllers/" + self.id
        self.options['rememberLastDir'] = False
        self.options['lang'] = 'en'
        self.options['resizable'] = False
        # you may require this later
        #self.options['customData']= {'entity_type':'student',
        #                            'entity_id': 'blahblahblah'}


        super(elFinderWidget, self).prepare()
        #self.elfinder_connector = ElfinderConnector(opts=self.connector_options)


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
