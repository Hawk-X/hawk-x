from django.core.mail import send_mail
from django.shortcuts import render, render_to_response

from .forms import ContactForm


def home(request):
    # contact_list = Contact.objects.all()
    # context = {'contact_list': contact_list}
    template_name = 'home.html'
    return render_to_response(template_name)


def contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            # Отправка почты тому, кто ввел свои данные.
            # Subject here-Тема письма;Сообщение;От кого;Кому.
            send_mail(
                'Subject here',
                'Here is the message.',
                'from@example.com',
                ['to@example.com'],
                fail_silently=False,
            )
            form.save()
            # Редирект на другую страницу
            return render(request, 'thanks.html')
    else:
        # Заполняем форму
        form = ContactForm()
        # Переходим на опр. странцу
    template_name = 'contact.html'
    return render(request, template_name, {'form': form})
