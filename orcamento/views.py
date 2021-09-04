from django.shortcuts import render


def dashboard(request):

    return render(request, "orcamento/dashboard.html")