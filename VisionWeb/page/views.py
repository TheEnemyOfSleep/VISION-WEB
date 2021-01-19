from django.views.generic import ListView

from page.models import Block


class BlockView(ListView):
    template_name = 'index.html'
    context_object_name = 'block_list'

    def get_queryset(self):
        return Block.objects.exclude(root__isnull=False).order_by('sorting')
