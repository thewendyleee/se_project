from django.shortcuts import render

# Create your views here.
def rent(request):
    return render(request, "rent.html")


def report(request):
    return render(request, "report.html")