from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
#from django.urls import conf
from .models import Question
#from .forms import CustomUserCreationForm, ProfileForm, SurveyForm
from .forms import SurveyForm
#from .utils import searchProfiles, paginationProfiles
#
# Create your views here.
def survey(request):
    form = SurveyForm()

    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            survey = form.save(commit=False)
            #survey.owner = profile
            survey.save()
            messages.success(request, 'Send answer successfully.')
            return redirect('account')


    context = {'form': form}
    return render(request, 'survey/survey_form.html', context)


@login_required(login_url='login')
def takeSurvey(request):
    profile = request.user.profile
    form = SurveyForm()

    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.owner = profile
            survey.save()
            messages.success(request, 'Send answer successfully.')
            return redirect('account')


    context = {'form': form}
    return render(request, 'survey/survey_form.html', context)


