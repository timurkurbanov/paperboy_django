from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from paperboy.models import Paperboy

def home(request):
    earnings = "{:10.2f}".format(Paperboy.total_earnings())
    context = {'paperboys': Paperboy.objects.all(), 'total_papers': Paperboy.total_papers(), 'total_earnings': earnings}
    return HttpResponse(render(request, 'index.html', context))

def deliver(request, id):
    pb = get_object_or_404(Paperboy, id=id)
    ad1 = request.POST['address1']
    ad2 = request.POST['address2']
    pb.deliver(int(ad1), int(ad2))
    return HttpResponseRedirect('/')

def paperboy_details(request, id):
    pd = Paperboy.objects.get(pk=id)
    context = {'pd': pb}
    html_response = render(request, 'details.html', context)
    return HttpResponse(html_response)