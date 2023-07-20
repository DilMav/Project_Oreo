from django.shortcuts import render, redirect
from . import forms
from .models import *
from .handlers import bot

# Create your views here.
def home_page(request):
    search_bar = forms.SearchForm()
    # Собираем названия всех продуктов
    product_info = Product.objects.all()
    # Собираем название всех категорий
    category_info = Category.objects.all()

    #Передаём данные на фронт
    context = {
        'form': search_bar,
        'product': product_info,
        'category': category_info}

    return render(request, 'index.html', context)

def search_product(request):
    if request.method == 'POST':
        get_product = request.POST.get('search_product')
        try:
            exact_product = Product.objects.get(product_name__icontains=get_product)
            return redirect(f'product/{exact_product.id}')
        except:
            return redirect('/')
def product_page(request, pk):
    product_info = Product.objects.get(id=pk)

    if request.method == "POST":
        Cart.objects.create(user_id=request.user.id,
                            user_product=product_info,
                            user_product_amount=request.POST.get('product_amount'))
    #Передаём данные на кнопки
    context = {'product': product_info}
    return render(request, 'about_products.html', context)

def category_page(request, pk):
    category_info = Category.objects.get(id=pk)
    product_info = Product.objects.filter(product_category=category_info)

    #Передаём данные на фронт
    context = {'products': product_info}

    return render(request, 'about_category.html', context)

def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = forms.RegisterForm()
        return render(request, 'registration/register.html', {'form': form})

def get_user_cart(request):
    user_cart = Cart.objects.filter(user_id=request.user.id)

    if request.method == 'POST':
        main_text = 'Новый заказ!\n\n'

        for i in user_cart:
            main_text += f'Товар: {i.user_product}\nКоличество: {i.user_product_amount}'

        bot.send_message(5844602799, main_text)
        user_cart.delete()
        return redirect('/')
    return render(request, 'user_cart.html', {'cart': user_cart})

def del_from_cart(request):
    cart = Cart.objects.filter(user_id=request.user.id, user_product=pk)
    cart.delete()
    return redirect('/')

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    return render(request, 'contacts.html')