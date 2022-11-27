import datetime
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from .models import webhook_data, user_data
import json
import pdb


@csrf_exempt
def webhook(request,userid):
    if request.method == 'POST':
        user = user_data.objects.filter(id=userid)[0]
        print("Data received from Webhook is: ", request.body)
        print("json data------>", json.loads(request.body))
        s = webhook_data.objects.create(time=datetime.datetime.now(), data=json.loads(request.body),user_data=user)
        s.save();
        return HttpResponse('data received')


def webhook_receiver(request,userid):
    responses = webhook_data.objects.filter(user_data_id=userid)
    # render function takes argument  - request
    # and return HTML as response
    res_list = []
    for res in responses:
        r = json.dumps(res.data)
        loaded_r = json.loads(r)
        res_list.append(loaded_r)
    return render(request, "index.html",context={'username':userid, 'responses':res_list})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            m = user_data.objects.get(username=request.POST['username'])
            if m.password==request.POST['password']:
                request.session['member_id'] = m.id
                user_id=m.id
                # return render(request, "index.html")
                return redirect('/webhook_receiver/'+str(user_id))
            else:
                return HttpResponse("Your username and password didn't match.")
        except:
            return HttpResponse("Something went wrong check cred")
    else:
        return render(request, "login.html")

