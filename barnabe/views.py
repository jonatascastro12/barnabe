# -*- coding: utf-8 -*-
from django.apps import apps
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models.loading import get_models, get_app
from django.forms.widgets import Media
from django.http.response import Http404
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _
from django.views.generic.base import ContextMixin, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, FormView
from django.views.generic.list import ListView
from barnabe.settings import INSTALLED_APPS
from membership.models import BarnabeUser


class DashboardMenu():
    app_list = [apps.get_app_config(app) for app in INSTALLED_APPS if not ("django" in app) and not ("nested" in app) and not ("bootstrap" in app) and not ("sorl" in app)]
    def menu_list(self):
        mlist = []
        mlist.append({'link': '/dashboard', 'app_verbose_name': _('Overview')})
        for app in self.app_list:
            models = get_models(get_app(app.label))
            app_obj = {'app': app, 'app_verbose_name': app.verbose_name,
                       'models': [{'verbose_name': m._meta.verbose_name_plural,
                        'link': m._meta.model_name } for m in models if m._meta.model_name in ['member']]}
            mlist.append(app_obj)
        return mlist

class DashboardView(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        menu = DashboardMenu()
        context['app_list'] = menu.menu_list()
        context['media_css'] = Media()
        context['media_js'] = Media()
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(DashboardView, self).dispatch(request, *args, **kwargs)

class DashboardListView(ListView, DashboardView):
    pass

class DashboardDetailView(DetailView, DashboardView):
    pass

class DashboardFormView(FormView, DashboardView):
    pass

class DashboardUpdateView(UpdateView, DashboardView):
    pass

@login_required
def dashboard(request):
    menu = DashboardMenu()
    return render(request, "dashboard_base.html", {"app_list": menu.menu_list()})

def profile(request):
    menu = DashboardMenu()
    return render(request, "dashboard_base.html", {"app_list": menu.menu_list()})

def logout(request):
    auth.logout(request)
    return redirect('/login')

def login(request):
    if (request.method == 'GET'):
        return render(request, "login.html")
    else:
        next = request.GET.get('next', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if '@' in username:
            user = User.objects.filter(email=username).first()
            if user is not None:
                username = user.username
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                if next:
                    return redirect(next)
                return redirect('/dashboard')
            else:
                return render(request, 'login.html', {'error': "Usuário não está ativo."})
        else:
            return render(request, 'login.html', {'error': "Usuário ou senha inválidos."})