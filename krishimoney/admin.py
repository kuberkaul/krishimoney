from django.contrib import admin
from django.shortcuts import render_to_response
from django.template import RequestContext



def adminForm(request):
    return render_to_response("admin_form.html", {'title': 'Admin Form'},
                              RequestContext(request, {}))
admin.site.register_view("admin_form", view=adminForm)
