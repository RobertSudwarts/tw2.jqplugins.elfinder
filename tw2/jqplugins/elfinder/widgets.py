
# tw2-proper imports
import tw2.core as twc

from tw2.jqplugins.ui import base as jquibase
import base as elfbase


class elFinderWidget(jquibase.JQueryUIWidget):

    resources = [jquibase.jquery_ui_js,
                 elfbase.elfinder_css,
                 elfbase.elfinder_js
                 ]

    url = twc.params.Param('Connector URL', default=twc.params.Required)
    template = 'tw2.jqplugins.elfinder.templates.widget'

    def prepare(self):

        if 'url' not in self.options:
            assert hasattr(self, 'url'), 'No url provided.   Please supply the url parameter'
            self.options['url'] = self.url

        super(elFinderWidget, self).prepare()
