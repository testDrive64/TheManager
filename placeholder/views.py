from django.shortcuts import render

# Create your views here.
def placeholder(request):
    context = {}
    return render(request, 'placeholder/index.html', context)
