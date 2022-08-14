from urllib.parse import urlparse
import json
import socket
import IP2Location
import os
import re
from requests import get
from .utils import is_valid_hostname

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


#Assign the IP2LOCATION database LITE
database = IP2Location.IP2Location(os.path.join("data", "IP2LOCATION-LITE-DB11.BIN"))

def home(request):
    # In the Home page return the User Public IP informations
    my_ip = get('https://api.ipify.org').text
    rec = database.get_all(my_ip)
    data = json.loads(json.dumps(rec.__dict__))
    context = {"data": data}
    return render(request, "index.html", context)


def getIpInfo(request):

    # Get posted link
    link = request.POST.get("link")

    # create RegEx to test if link is an IP address
    ip_regEx = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

    # Check if the posted link is in IPv4 format
    test = ip_regEx.match(link)
    if test:
        rec = database.get_all(link)
        if (rec.country_short == "-"):
            data = {
                "err_txt": " We didn't found your IP address in the Database, may it's a local IP Address!"
            }
        else:
            data = json.loads(json.dumps(rec.__dict__))
            return JsonResponse({'data': data})
    
    # Check if the posted link is in a Domain format using is_valid_hostname() method
    elif is_valid_hostname(link):

        try:
            ip = socket.gethostbyname(link)
            rec = database.get_all(ip)
            data = json.loads(json.dumps(rec.__dict__))
            return JsonResponse({'data': data})
        except:
            data = {
                "err_txt": " We didn't found your website / IP address in the Database, may you mistyped it!"
                }
            return JsonResponse({'data': data})
    
    # Otherwise the posted link is in URL format or mistyped at all
    else:
        try:
            domain = urlparse(link)
            ip = socket.gethostbyname(domain.hostname)
            rec = database.get_all(ip)
            data = json.loads(json.dumps(rec.__dict__))
            return JsonResponse({'data': data})
        except:
            data = {
                "err_txt": " We didn't found your domain in the Database, may you mistyped your link!"
            }
    
    # Finaly return the data Json
    return JsonResponse({'data': data})

