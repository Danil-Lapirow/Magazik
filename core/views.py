from django.views.generic import TemplateView, DetailView
from django.shortcuts import redirect
from core.models import Product, Tag
from django.http import HttpResponse


# Create your views here.
class ProductView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        # print(request.POST.keys())
        # print(dir(request.POST.values()))

        import stripe
        stripe.api_key = "sk_test_RvB7B7pNntx1lzJ8rEXXn118"

        stripe.Charge.create(
            amount=int(request.POST['price']),
            currency="usd",
            source=request.POST['stripeToken'],  # obtained with Stripe.js
            description=request.POST['title']
        )
        print("Created")
        return redirect('.')

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.method == "POST":
            return self.post(request, *args, **kwargs)
        elif request.method == "GET":
            return self.get(request, )

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['products'] = Product.objects.all()

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        query = Product.objects.all()
        try:
            price_min = request.POST['price_min']
            context['price_min'] = price_min
            query = query.filter(price__gte=price_min)
        except:
            pass
        try:
            price_max = request.POST['price_max']
            context['price_max'] = price_max
            query = query.filter(price__lte=price_max)
        except:
            pass
        try:
            tags = request.POST.getlist("tags")
            context['checked_tags'] = tags
            if len(tags) != 0:
                query = query.filter(tags__in=tags)
        except:
            pass
        try:
            age = request.POST['age']
            context['age'] = age
            query = query.filter(age=age)
        except:
            try:
                age_min = request.POST['age_min']
                context['age_min'] = age_min
                query = query.filter(age__gte=age_min)
            except:
                pass
            try:
                age_max = request.POST['age_max']
                context['age_max'] = age_max
                query = query.filter(age__lte=age_max)
            except:
                pass

        context['products'] = query.distinct()

        return self.render_to_response(context)
