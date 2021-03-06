
from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns("",
    ("^admin/", include(admin.site.urls)),
    url("", include("core.urls")),
    url("", include("social_auth.urls")),
    ("^%s/(?P<path>.*)$" % settings.MEDIA_URL.strip("/"),
        "django.views.static.serve", {"document_root":  settings.MEDIA_ROOT}),
)
