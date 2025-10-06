from django.shortcuts import render

# Create your views here.
def show_moderator_main_page(request):
    return render(request, 'moderator/moderator_main_page.html')