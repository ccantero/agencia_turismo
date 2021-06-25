from django.views.generic import TemplateView


class HomePage(TemplateView):
	template_name = 'index.html'

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['first_option'] = 'Relax'
		context['second_option'] = 'Family'
		context['third_option'] = 'Premium'
		return context	