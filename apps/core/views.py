from django.shortcuts import render


def homepage(request):
    return render(request, 'core/home.html')

def our_story(request):
    return render(request, 'includes/our_story.html')