from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin
from krishimoney import views
from adminplus.sites import AdminSitePlus

admin.site = AdminSitePlus()
admin.autodiscover()

urlpatterns = patterns("",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^aboutUs/", TemplateView.as_view(template_name="aboutUs.html"),name="aboutUs"),
    url(r"^adminForm/", views.adminForm),
    url(r"^adminPageSubmitted/", views.adminForm)
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
