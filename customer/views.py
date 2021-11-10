from django.shortcuts import redirect, render
from django.http import HttpResponse
from customer.forms import LogForm
from customer.models import Customer
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
def home(request):
    return render(request,'index.html', {})

def cusAdd(request):
    form = LogForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect("cusAll")
        else:
            return render(request, "cusAdd.html", {"form": form})
    else:
        return render(request, "cusAdd.html", {"form": form})

def cusAll(request):
    messages = Customer.objects.order_by("-dob")
    return render(request, "cusAll.html", {"message_list": messages})

def searchAjax(request, q):
    try:
        messagesList = Customer.objects.filter(dob=q)
        if (len(messagesList) > 0):
            out="<table><tr><th>Fname</th><th>Email</th><th>DoB</th><th>Address</th></tr>"
            for x in messagesList:
                dob = x.dob.strftime('%d %B, %Y')
                out += "<tr><td>"+ x.fname + "</td><td>" + x.email +"</td><td>" + dob + "</td><td>" + x.address + "</td></tr>"
            out += "</table>"
        else:
            out="no matching results"
    except:
        out = "invalid date format"
    return HttpResponse(out)

def cusJson(request):
    messagesList = Customer.objects.all()
    res = "["
    if (len(messagesList) > 0):
        for x in messagesList:
            res += json.dumps({ 'id': x.id, 'fname': x.fname, 'email': x.email, 'dob': x.dob, 'address': x.address}, indent=2, cls=DjangoJSONEncoder)
            res += ","
        res = res[:-1]
        res += "]"
    else:
        res = json.dumps([{ 'error' : 'no customers found'}])
    return HttpResponse(res, content_type='text/json')

def cusDelete(request, cusid):
    row = Customer.objects.filter(id=cusid)
    if (row):
        row.delete()
        return HttpResponse("delete successful")
    else:
        return HttpResponse("customer not found at id " + cusid)

def recordAsJSON(request,i):
    try:
        message = Customer.objects.get(id=i)
        res = json.dumps([{ 'id': message.id, 'fname': message.fname, 'email': message.email, 'dob': message.dob, 'address': message.address}], indent=2, cls=DjangoJSONEncoder)
    except:
        res = json.dumps([{ 'error' : 'customer id does not exist'}])
    return HttpResponse(res, content_type='text/json')