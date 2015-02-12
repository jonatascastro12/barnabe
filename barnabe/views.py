# -*- coding: utf-8 -*-
import imghdr
import json
import os
from PIL import Image
from django.apps import apps
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.temp import NamedTemporaryFile
from django.db.models.loading import get_models, get_app
from django.forms.widgets import Media
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _
from django.views.generic.base import ContextMixin, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, FormView
from django.views.generic.list import ListView
from barnabe import errors
from barnabe.settings import INSTALLED_APPS, MEDIA_ROOT, MEDIA_URL


class DashboardMenu():
    app_list = [apps.get_app_config(app) for app in INSTALLED_APPS if not ("django" in app) and not ("nested" in app) and not ("bootstrap" in app) and not ("sorl" in app)]

    menu = [
        {'name': 'overview', 'verbose_name': _('Overview'), 'link': '/overview'},
        {'name': 'churchship', 'verbose_name': _('Churchship'), 'perm': 'churchship', 'children':
            [
                {'name': 'chuch', 'verbose_name': _('Church'), 'link': '/churchship/church', 'perm': 'churchship.change_church'}
            ]
        },
        {'name': 'membership', 'verbose_name': _('Membership'), 'perm': 'membership', 'children':
            [
                {'name': 'members', 'verbose_name': _('Members'), 'link': '/membership/members', 'perm': 'membership.change_member'},
            ]
        },
        {'name': 'discipleship', 'verbose_name': _('Discipleship'),}
    ]

    def render(self, request=None, permission=None):
        output = u'<ul class="nav nav-sidebar">'
        for item in self.menu:
            active = 'active-app' if ('link' in item and '/dashboard' + item['link'] in request.path_info) or (item['name'] in request.path_info) else ''
            link = ('/dashboard' + item['link'] if 'link' in item else '#')
            verbose_name = item['verbose_name'] if 'verbose_name' in item else item['name']
            if(not 'perm' in item) or ('perm' in item and request.user.has_module_perms(item['perm'])):
                output += u'<li class="{0}"><a href="{1}">{2}</a>'.format(active, link, verbose_name)
            if 'children' in item:
                output += u'<ul class="nav subnav{0}">'.format(' open' if active != '' else '')
                for child_item in item['children']:
                    link = ('/dashboard' + child_item['link'] if 'link' in child_item else '#')
                    active = 'active' if ('link' in child_item and ('/dashboard' + child_item['link']) in request.path_info) else ''
                    current = u'<span class="sr-only">(current)</span>' if True else ''
                    if request.user.has_perm(child_item['perm']):
                        output += u'<li class="{0}"><a href="{1}">{2}{3}</a></li>'.format(active, link, child_item['verbose_name'], current)
                output += u'</ul>'
                output += u'</li>'
        output += u'</ul>'
        return output

    def menu_list(self):
        mlist = []
        ''' mlist.append({'link': '/dashboard', 'app_verbose_name': _('Overview')})
        for app in self.app_list:
            models = get_models(get_app(app.label))
            app_obj = {'app': app, 'app_verbose_name': app.verbose_name,
                       'models': [{'verbose_name': m._meta.verbose_name_plural,
                        'link': m._meta.model_name } for m in models if m._meta.model_name in ['member', 'church']]}
            mlist.append(app_obj)
        '''
        return mlist

class DashboardView(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        menu = DashboardMenu()
        context['app_list'] = menu.menu_list()
        context['dashboard_menu'] = menu.render(self.request)
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
    return render(request, "dashboard_base.html", {"dashboard_menu": menu.render(request)})

def profile(request):
    menu = DashboardMenu()
    return render(request, "dashboard_base.html", {"dashboard_menu": menu.render(request)})

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
                return redirect('/dashboard/overview')
            else:
                return render(request, 'login.html', {'error': "Usuário não está ativo."})
        else:
            return render(request, 'login.html', {'error': "Usuário ou senha inválidos."})

def image_upload(request):
    upload_to = ''
    if 'upload_to' in request.POST:
        upload_to = request.POST['upload_to']

    if request.POST and 'photo_crop_data' in request.POST and 'photo_original' in request.POST:

        im = Image.open(os.path.join(os.path.dirname(os.path.dirname(__file__)), request.POST['photo_original'].lstrip('/').replace('/','\\')))

        crop_data = json.loads(request.POST['photo_crop_data'])
        img_ratio = im.size[0]/float(crop_data["bounds"][0])

        crop_params = (int(round(crop_data['selectionPosition']['left']*img_ratio)),
                       int(round(crop_data['selectionPosition']['top']*img_ratio)),
                       int(round(crop_data['selectionPosition']['left']*img_ratio))+int(round(crop_data['selectionSize']*img_ratio)),
                       int(round(crop_data['selectionPosition']['top']*img_ratio))+int(round(crop_data['selectionSize']*img_ratio))
        )

        thumb_posfix = '_thumb_512'

        original_name, extension = os.path.splitext(im.filename)
        cropped_img = im.crop(crop_params)
        cropped_img.thumbnail((512, 512), Image.ANTIALIAS)
        cropped_img.save(original_name + thumb_posfix + extension)

        filename = os.path.splitext(os.path.split(im.filename)[1])[0]
        newfilename = filename + thumb_posfix + extension

        return HttpResponse(os.path.join(os.path.join(MEDIA_URL, upload_to), newfilename))


    if request.FILES and 'photo' in request.FILES:
        upload_full_path = os.path.join(MEDIA_ROOT, upload_to)

        if not os.path.exists(upload_full_path):
            os.makedirs(upload_full_path)
        upload = request.FILES['photo']
        original_name, extension = os.path.splitext(upload.name)
        f = NamedTemporaryFile(mode='w+b')
        upload.name = str(original_name) + '_' + os.path.split(f.name)[1] + str(extension)

        while os.path.exists(os.path.join(upload_full_path, upload.name)):
            f = NamedTemporaryFile(mode='w+b')
            upload.name = str(original_name) + '_' + os.path.split(f.name)[1] + str(extension)

        dest = open(os.path.join(upload_full_path, upload.name), 'wb')

        for chunk in upload.chunks():
            dest.write(chunk)
        dest.close()

        try:
            ext = imghdr.what(os.path.join(upload_full_path, upload.name))
            if ext not in ('jpeg', 'jpg', 'png'):
                return HttpResponse(status=406, content=errors.ImageNotJpgOrPngError().response_error())
            im = Image.open(os.path.join(upload_full_path, upload.name))
            if (im.size <= (512,512)):
                return HttpResponse(status=406, content=errors.ImageLessThan512().response_error())
        except IOError:
            return HttpResponse(status=406, content=errors.ImageNotRecognized().response_error())

        return HttpResponse(os.path.join(os.path.join(MEDIA_URL, upload_to), upload.name))
    return HttpResponse(status=405, content_type='application/json', content=errors.GetRequestNotPermitted.response_error())