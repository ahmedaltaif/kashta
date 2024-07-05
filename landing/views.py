from django.shortcuts import render

def landing_page(request):
    context = {}  # Add any context data you need for the template
    return render(request, 'landing/landing_page.html', context)
