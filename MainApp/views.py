from django.shortcuts import render

from .models import *

# Create your views here.


def stat(request):
    return render(request, "admin/base_site.html",
                  {
                      'incidents_cnt': len(Incident.objects.all()),
                      'communications_cnt': len(Communications.objects.all())
                  })
