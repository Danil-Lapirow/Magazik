from django.views.generic import TemplateView

from core.models import Product, Tag
from django.http import HttpResponse


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        query = Product.objects.all()
        try:
            price_min = request.GET['price_min']
            context['price_min'] = price_min
            query = query.filter(price__gte=price_min)
        except:
            pass
        try:
            price_max = request.GET['price_max']
            context['price_max'] = price_max
            query = query.filter(price__lte=price_max)
        except:
            pass
        try:
            tags = request.GET.getlist("tags")
            context['checked_tags'] = tags
            print('tags =', tags)
            if len(tags) != 0:
                query = query.filter(tags__in=tags)
        except:
            pass
        context['products'] = query.distinct()

        return self.render_to_response(context)
