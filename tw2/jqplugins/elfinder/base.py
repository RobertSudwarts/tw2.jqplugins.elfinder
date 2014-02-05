
# TW2 proper imports
import tw2.core as twc
from tw2.core.resources import encoder

# tw2.jquery & tw2.japlugins.ui imports
from tw2.jquery import base as jqbase
from tw2.jqplugins.ui import base as jquibase

# import from *this* package
from tw2.jqplugins.elfinder import defaults

modname = 'tw2.jqplugins.elfinder'
### Resources

dict_img = dict(name=defaults._elfinder_name_,
                version=defaults._elfinder_version_,
                subdir="img"
                )

elfinder_images = jqbase.DirLink(
    modname=modname,
    filename=defaults._plugin_css_dirname_ % dict_img
    )

elfinder_css = jqbase.jQueryPluginCSSLink(
    resources=[elfinder_images], name=defaults._elfinder_name_,
    basename='%s.%s' % (defaults._elfinder_basename_, defaults._elfinder_debug_),
    version=defaults._elfinder_version_,
    modname = modname,
    )

elfinder_js = jqbase.jQueryPluginJSLink(
    name=defaults._elfinder_name_,
    basename='%s.%s' % (defaults._elfinder_basename_, defaults._elfinder_debug_),
    version=defaults._elfinder_version_,
    modname = modname,
    )




