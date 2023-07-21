from django.shortcuts import render
from django.views import View


# Create your views here.

class Home(View):

    def get(self, request):
        context = {
            "test": True
        }
        return render(request, "onepage/index.html", context)
