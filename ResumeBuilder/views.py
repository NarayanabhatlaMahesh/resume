from django.shortcuts import render, HttpResponse
from .models import EducationForm as Education
from django.contrib.sessions.models import Session

# Create your views here.
def homepage(request):
    print(request.session)
    # del request.session['user']
    s=Session.objects.get(pk=request.session.session_key)
    print(s.get_decoded())
    print(request.session.get_expiry_age())
    if request.method == "POST":
        form = Education(request.POST)
        if form.is_valid():
            print("saving ..")
            print(request.POST)
            f=form.save()
            return HttpResponse("yea")
    else:
        form = Education()
    return render(request, "home.html", {"form" : form})