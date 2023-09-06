from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from .models import Product, Cases
from django.core.mail import send_mail

def index(requests):
    prod = Product.objects.all()[0:6]
    case = Cases.objects.all()[0:4]
    context = {
        'prod': prod,
        'case': case,
        "title": "Виробництво трансформаторів, Фільтрів EMI, Котушок під замовлення",
        "title_en": "Production of transformers, EMI filters, Coils to order",
    }
    return render(requests, 'main/index.html', context)

def about(requests):
    if requests.method == 'POST':
        form = ContactForm(requests.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            # здесь можно добавить логику для отправки сообщения
            send_mail(
                "Повідомлення з форми зворотного зв'язку",
                f'Відправник: {name}\nEmail: {email}\nТелефон: {phone}',
                email,  # отправитель
                ['ledstyle2013@gmail.com'],  # получатель или список получателей
                fail_silently=False,
            )
            return render(requests, 'main/about.html')
    else:
        form = ContactForm()
    return render(requests, 'main/about.html', {"title" : "Про нас", 'form': form })

def contact(requests):
    if requests.method == 'POST':
        form = ContactForm(requests.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            # здесь можно добавить логику для отправки сообщения
            send_mail(
                "Повідомлення з форми зворотного зв'язку",
                f'Відправник: {name}\nEmail: {email}\nТелефон: {phone}',
                email,  # отправитель
                ['ledstyle2013@gmail.com'],  # получатель или список получателей
                fail_silently=False,
            )
            return render(requests, 'main/about.html')
    else:
        form = ContactForm()
    return render(requests, 'main/contact.html', {"title" : "Контакти",'form': form })

def projects(requests):
    return render(requests, 'main/projects.html', {"title" : "Наші прєктм" })

def products(request):
    products = Product.objects.all()
    title = "Наша продукція"
    return render(request, 'main/products.html', {'products': products, 'title': title})

def projects(requests):
    case = Cases.objects.all()
    return render(requests, 'main/projects.html', {'cases': case, "title" : "Наші проєкти" })

def show_product(request, post_slug):
    post = get_object_or_404(Product, slug=post_slug)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            # здесь можно добавить логику для отправки сообщения
            send_mail(
                "Повідомлення з форми зворотного зв'язку",
                f'Відправник: {name}\nEmail: {email}\nТелефон: {phone}',
                email,  # отправитель
                ['ledstyle2013@gmail.com'],  # получатель или список получателей
                fail_silently=False,
            )

            context = {
                'post': post,
                'title': post.title,
                'preview': post.preview,
                'content': post.content,
                'photo': post.photo,
                'id': post.id,
                'slug': post.slug,
                'form': form,
                }
        return render(request, 'main/show_product.html', context=context)
    else:
        form = ContactForm()
        context = {
            'post': post,
            'title': post.title,
            'preview': post.preview,
            'content': post.content,
            'photo': post.photo,
            'id': post.id,
            'slug': post.slug,
            'form': form,
        }
    return render(request, 'main/show_product.html', context=context)

    # return HttpResponse(f"Тoвар номер : {post_id}")
# #
def show_case(requests, case_slug):
    case = get_object_or_404(Cases, slug=case_slug)

    context ={
        'post': case,
        'title': case.title,
        'preview': case.preview,
        'content': case.content,
        'photo': case.photo,
        'id': case.id,
        'slug': case.slug

    }
    return render(requests, 'main/show_case.html', context=context)

def news_case(requests, news_slug):
    news = get_object_or_404(News, slug=news_slug)

    context ={
        'post': news,
        'title': news.title,
        'preview': news.preview,
        'content': news.content,
        'photo':news.photo,
        'id': news.id,
        'slug': news.slug

    }
    return render(requests, 'main/show_news.html', context=context)