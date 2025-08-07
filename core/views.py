from django.views.generic import TemplateView
from blog.models import Post
from item.models import Item

class LandingPageView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["featured_items"] = Item.objects.filter(is_sold=False)[0:6]
        # context["lastest_blog_posts"] = Post.objects.filter(publish=True).order_by('-published_at')[0:3]

        return context

