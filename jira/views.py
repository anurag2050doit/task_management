import os
from django.views.generic.base import TemplateView, View
from django.conf import settings
from django.http import HttpResponse, Http404


class IndexView(TemplateView):
    template_name = 'index.html'


class AngularTemplateView(View):
    def get(self, request, item=None, *args, **kwargs):
        print(item)
        static_dir_path = settings.STATICFILES_DIRS[1]
        final_path = os.path.join(static_dir_path, item + ".html")
        print(final_path)
        try:
            html = open(final_path)
            return HttpResponse(html)
        except FileNotFoundError:
            return Http404
