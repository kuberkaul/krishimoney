def adminForm(request, id):
    return HttpResponse("You're looking at question %s." % question_id)

def adminPagesubmitted(request, id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

