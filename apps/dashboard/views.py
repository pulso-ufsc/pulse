from django.utils.translation import gettext as _
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Dashboard"
        context["page_description"] = _("Bienvenido ao Pulso Tech")
        return context
