from django.shortcuts import render

# Create your views here.
def placeholder(request):
    context = {}
    return render(request, 'protoValidation/index.html', context)
