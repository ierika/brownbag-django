"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings
from django.views.i18n import JavaScriptCatalog
from django.views.generic.base import RedirectView

from django.utils.translation   import ugettext as _, ugettext_lazy

import config.settings as settings

#----------------------
# Change admin site title
#----------------------
admin.site.site_title  = ugettext_lazy('ログイン')
admin.site.site_header = ugettext_lazy('Brown Bag 管理画面')
admin.site.index_title = ugettext_lazy('メニュー')

urlpatterns = [
    path('admin/', admin.site.urls),

    # accounts
    path('accounts/', include('django.contrib.auth.urls')),

    path('i18n/', include('django.conf.urls.i18n')),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('favicon\.ico', RedirectView.as_view(url='/static/images/favicon.ico')),

    path('', include('brownbags.urls'), name='brownbags'),
]

"""
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
"""

## https://stackoverflow.com/questions/28007770/how-to-to-make-a-file-private-by-securing-the-url-that-only-authenticated-users/28008035
if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

