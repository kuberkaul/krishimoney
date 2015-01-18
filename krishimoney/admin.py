from django.contrib import admin
from django.shortcuts import render_to_response

def my_view(request):
   return render_to_response('krishimoney/template/admin_form.html')

admin.site.register_view('admin_form',my_view , 'AdminForm')
print 'abcd'
