
import tw2.core as twc
import tw2.forms as twf
from tw2.jqplugins.ui import TabsWidget

import webob
import time
from tg import request as tgrequest

try:
    import simplejson as json
except:
    import json



class DemoWebobJSON(twf.TextField):
    '''and even more usefully, you can frame the response as json
    '''
    @classmethod
    def request(cls, req):

        print " ------ request environ -----"
        print tgrequest.environ
        print " ----------------------------"
        time.sleep(1.5)
        response = webob.Response(request=req, content_type="application/json")
        data = {'myval': "The answer (of course): %d" % (req*2) }
        response.body = json.dumps( data )
        return response


    def prepare(self):

        resp = self.request(21)

        print "----- response----------------------------"
        print resp
        print tgrequest.environ
        print "--------------------------------------"
        resp_dict = json.loads(resp.body)
        self.value = resp_dict['myval']

        super(DemoWebobJSON, self).prepare()



some_items = [
('Section 1','<p>section1</p>'),
('Section 2','<p>section2</p>'),
('Section 3','<p>section3</p>'),
('Section 4','<p>section4</p>'),
]


ajaxified_tabs_items = [{'label': v[0], 'content': v[1]} for v in some_items]
ajaxified_tabs_items[2]['label'] += ' (via ajax)'
#ajaxified_tabs_items[2]['href'] = '/tw2_controllers/ajaxtab/'
ajaxified_tabs_items[2]['href'] = '/tw2_controllers/xyz/'
del ajaxified_tabs_items[2]['content']


class DemoTabsWidget(TabsWidget):
    #id = 'demo-tabs'
    items = ajaxified_tabs_items

    @classmethod
    def request(cls, req):
        # You could, of course, use other controllers
        # (say a tg2 controller)
        import time
        import webob
        time.sleep(1)
        resp = webob.Response(request=req, content_type="text/html")
        resp.body = "<p>wow.. this came via <h4>ajax!</h4></p>"
        return resp

# if you give the widget an id, eg demo-tebs, tw2.core.middleware
# will register the controller you can call tw2_controllers/demo-tabs
# and you'll bump the `request` (so, the href for the tab item would
# have to call this accordingly).  However, by registering the controller
# (as below) the href can call it... (look at it closely and it makes sense)
# this is required here...
twc.register_controller(DemoTabsWidget, 'ajaxtab')
