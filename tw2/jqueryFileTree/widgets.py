
import base
import tw2.core as twc
from tw2.core.resources import encoder
from tw2.jquery import jquery_js

class FileTreeWidget(twc.Widget):

    resources = [jquery_js, 
                 base.filetree_js, 
                 base.filetree_css
                 ] + base.image_links

    template = "mako:tw2.jqueryFileTree.templates.filetree"

    options = twc.Param(
        '(dict) A dict of options to pass to the widget', default={})


    def prepare(self):

        if self.options is not None and not isinstance(self.options, dict):
            raise ValueError, 'Options parameter must be a dict'

        self.options = encoder.encode(self.options)