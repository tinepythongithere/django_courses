from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import QuestionnaireEnergieForm
from .models import QuestionnaireEnergie
from .utils import group_required
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


def profile_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name="user_carbon").exists():
            return view_func(request, *args, **kwargs)
        raise PermissionDenied
    return wrapper

@login_required
@group_required('user_carbone')
def home(request):

    return render(request, 'carboneapp/home.html')

def login_view(request):

    if 'login_submit' in request.POST:
        email = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('carboneapp:home')
        else:
            messages.error(request, 'User introuvable')
    return render(request, 'carboneapp/login.html')


def logout_view(request):
    logout(request)

    return redirect('carboneapp:login')

@login_required
@profile_required
def questionnaire_energie(request):
    energy_model = QuestionnaireEnergie.objects.filter(entite=request.user).first()

    if request.method == 'POST':
        form = QuestionnaireEnergieForm(request.POST, instance=energy_model)
        if form.is_valid():
            form_ = form.save(commit=False)
            form_.entite = request.user
            form_.save()
            messages.success(request, 'Le questionnaire ernergy est enregistré avec succès.')
            return HttpResponseRedirect(reverse('carboneapp:energy_form'))
    else:
        form = QuestionnaireEnergieForm(instance=energy_model)

    return render(request, 'carboneapp/energy_form.html', context={'form': form})