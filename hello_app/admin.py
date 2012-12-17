from django.contrib import admin
from hello_app.models import *
from django.conf import settings
import os
from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site

from django.contrib.admin.sites import AdminSite
from hello_app.forms import *

#admin.site.register(Feedback)

class MyAdminWithReCaptcha(AdminSite):
    login_form = MyAdminLoginForm
    login_template = os.path.join(settings.TEMPLATES_PATH, 'my_admin_login.html')


my_admin = MyAdminWithReCaptcha()
my_admin.register(Feedback)
my_admin.register(User)
my_admin.register(Group)
my_admin.register(Site)