from __future__ import absolute_import, unicode_literals
from django.views.generic.base import TemplateView


class Home(TemplateView):

    template_name = 'teasing/home.html'

    def get_context_data(self, *args, **kwargs):

        context = super(Home, self).get_context_data(*args, **kwargs)

        return context
