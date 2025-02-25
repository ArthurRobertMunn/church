from django.shortcuts import render

from .models import Person

from django.http import HttpResponseRedirect

from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "prayers/index.html", {
        "people":  Person.objects.all()
    })

def create(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        prayer = request.POST["prayer"] 

        person = Person(name=name, email=email, prayer=prayer)
        person.save()

        return HttpResponseRedirect(reverse("index"))

    return render(request, "prayers/create.html")

def details(request, person_id):
    person = Person.objects.get(pk=person_id)
    return render(request, "prayers/details.html", {
        "person": person
    })

def update(request, person_id):
    if request.method == "POST":
        person = Person.objects.get(pk=person_id)

        person.name = request.POST["name"]
        person.email = request.POST["email"]
        person.prayer = request.POST["prayer"]
        
        person.save()

        return HttpResponseRedirect(reverse("index"))
    
    return render(request, "prayers/update.html", {
        "person": Person.objects.get(pk=person_id)
    })

def delete(request, person_id):
    person = Person.objects.get(pk=person_id)
    person.delete()
    return HttpResponseRedirect(reverse("index"))

def search(request):
    query = request.GET["query"]
    if query:
        people = Person.objects.filter(name__icontains=query)
    else:
        people = Person.objects.none()  # Return empty queryset if no search term
    return render(request, "prayers/search.html", {
        "people": people
    })