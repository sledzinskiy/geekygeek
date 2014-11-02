from django.shortcuts import render_to_response


def home(request):
    return render_to_response('home.html')


def myprofile(request):
    return render_to_response('myprofile.html')


def groups(request):
    return render_to_response('groups.html')


def group(request):
    return render_to_response('group.html')


def geeks(request):
    return render_to_response('geeks.html')


def news(request):
    return render_to_response('news.html')


def newsdetail(request):
    return render_to_response('newsdetail.html')


def about(request):
    return render_to_response('about.html')