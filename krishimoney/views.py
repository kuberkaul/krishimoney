from django.http import HttpResponse
from django.template import RequestContext
from krishimoney.forms import AdminForm
from django.shortcuts import render
from django.http import HttpResponseRedirect

def adminForm(request, id):
    return HttpResponse("You're looking at question %s." % question_id)

def adminPageSubmitted(request):
    print "Hi" + str(request.POST['cropName'])
    return HttpResponse("You're looking at question")

def adminForm(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print "Entered request is POST"
        # create a form instance and populate it with data from the request:
        form = AdminForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print form.cleaned_data['cropName']
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AdminForm()

    return render(request, 'admin_form.html', {'form': form})
