from django.shortcuts import render

def tour_page(request):
    return render(request, 'tour/tour_page.html')