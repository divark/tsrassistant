from .models import *
from .forms import *

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from teamwork.apps.profiles.forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'profiles/signup.html',
                          {'form': form})

        else:
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password,
                                     email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')

    else:
        return render(request, 'profiles/signup.html',
                      {'form': SignUpForm()})

@login_required
def profile(request, username):
    """
    Public method that takes a request and a username.  Gets an entered 'skill' from the form
    and stores it in lowercase if it doesn't exist already. Renders profiles/profile.html.

    # TODO: fix up return calls, form should be in if
    """
    profile = Profile.objects.get(user=request.user)
    form = SkillsForm(request.POST)
    if request.method == 'POST':        
        if form.is_valid():            
            known = form.cleaned_data.get('known_skill')
            learn = form.cleaned_data.get('learn_skill')
            # if we have an input 
            if known:
                # check if skill is in Skills table, lower standardizes input
                if Skills.objects.filter(skill=known.lower()):
                    # skill already exists, then pull it up  
                    known_skill = Skills.objects.get(skill=known.lower()) 
                else:
                    # we have to add the skill to the table
                    known_skill = Skills.objects.create(skill=known.lower())
                    # save the new object
                    known_skill.save()
                # This is how we can use the reverse of the relationship
                print(known_skill.known.all())
                # add the skill to the current profile
                profile.known_skills.add(known_skill)
                profile.save()
                # This is how we can get all the skills from a user
                print(profile.known_skills.all())

            # same as Known implemenation
            if learn:
                if Skills.objects.filter(skill=learn.lower()):
                    learn_skill = Skills.objects.get(skill=learn.lower())
                else:
                    learn_skill = Skills.objects.create(skill=learn.lower())
                    learn_skill.save()
                # This is how we can use the reverse of the relationship
                print(learn_skill.learn.all())
                profile.learn_skills.add(learn_skill)
                profile.save()
                # This is how we can get all the skills from a user
                print(profile.learn_skills.all())

    page_user = get_object_or_404(User, username=username)
    return render(request, 'profiles/profile.html', {
        'page_user': page_user, 'form':form, 'profile':profile 
        })















