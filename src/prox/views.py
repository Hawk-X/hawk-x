from django.core.exceptions import ImproperlyConfigured
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from .forms import ContactForm


class HomeView(TemplateView):
    """A view that renders a template.  This view will also pass into the context
    any keyword arguments passed by the URLconf."""
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_template_names(self):
        """
        Returns a list of template names to be used for the request. Must return
        a list. May not be called if render_to_response is overridden.
        """
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            return [self.template_name]


class ContactFormView(FormView):
    """Simple CBV FormView"""
    form_class = ContactForm
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        """Handles GET requests and instantiates a blank version of the form."""
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = self.get_form()
        if form.is_valid():
            send_mail(
                'Subject here',
                'Here is the message.',
                'from@example.com',
                ['to@example.com'],
                fail_silently=False,
            )
            form.save()
            return render(request, 'thanks.html')
        else:
            return self.form_invalid(form)