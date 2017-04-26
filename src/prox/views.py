from django.shortcuts import render


from .models import Contact
from .forms import ContactForm


def home(request):
	contact_list = Contact.objects.all()
	context = {'contact_list': contact_list}
	return render(request, 'home.html', context)


def contact(request):
	# if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            # save чтобы сохранилось
            form.save()
            # Rедирект на другую страницу
            return render(request, 'thanks.html')
    else:
    	# Заполняем форму
        form = ContactForm()
        # Переходим на опр. странцу
    return render(request, 'contact.html', {'form': form})