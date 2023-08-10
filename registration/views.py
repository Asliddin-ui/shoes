from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import RegistrationForm, LoginForm, UpdateForm, AboutForm
from .models import User
from django.contrib.auth import authenticate, login, logout


def main_index(request):
    return render(request, 'main/index.html')


class UserRegistration(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = 'Registratsiya'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('main')
        form = RegistrationForm()
        return render(request, 'main/registration.html', {
            'form': form
        })

    def post(self, request):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            return redirect('login')

        return render(request, 'main/registration.html', {
            'form': form
        })


def user_login(request):
    request.title = 'Login'
    form = LoginForm()
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('main:index')
            form.add_error('password', 'Password yoki Username xato')
    return render(request, 'main/login.html', {
        'form': form,
    })


@login_required(login_url='registration:login')
def user_logout(request):
    logout(request)
    return redirect('registration:login')


@login_required(login_url='registration:login')
def settings(request):
    return render(request, 'main/settings.html')

@login_required(login_url='registration:login')
def update(request, id):
    user = get_object_or_404(User, id=id)
    form = UpdateForm(data=request.POST or None, instance=user)
    if request.method == 'POST':
        data = UpdateForm(data=request.POST)
        print(data)
        if data.is_valid():
            form.save()
            return redirect('registration:login')
    return render(request, 'main/update.html', context={
        'form': form
    })

@login_required(login_url='registration:login')
def about_user(request, id):
    user = get_object_or_404(User, id=id)
    form = AboutForm(data=request.POST or None, instance=user)

    return render(request, 'main/view.html', context={
        'form': form
    })



