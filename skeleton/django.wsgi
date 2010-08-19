import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

sys.path.append('/home/user/www/domain/project/')
sys.path.append('/home/user/www/domain/')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

