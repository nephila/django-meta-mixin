# -*- coding: utf-8 -*-
from django.views.generic import DetailView

from .models import Post


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['meta'] = self.get_object().as_meta()
        return context
