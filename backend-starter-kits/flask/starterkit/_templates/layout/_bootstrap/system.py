from _keenthemes.libs.theme import KTTheme
from _keenthemes.bootstrap import KTBootstrap

"""
This is an entry and Bootstrap class for the theme level.
The init() function will be called in _keenthemes/__init__.py
"""
class KTBootstrapSystem:

    def init(context):
        KTBootstrap.init()

        KTTheme.addHtmlClass('body', 'auth-bg app-blank')