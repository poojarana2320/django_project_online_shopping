from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

""" Registration page"""


def Registration_View(request):
    if request.method == 'POST':
        error = ""
        form = Registration_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirmpassword = form.cleaned_data['confirmpassword']
            mobileno = form.cleaned_data['mobileno']
            address = form.cleaned_data['address']
            country = form.cleaned_data['country']
            if password == confirmpassword:
                obj = User.objects.create(
                    username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                reg = Registration.objects.create(
                    user_id=obj, mobileno=mobileno, address=address, country=country)
                obj.set_password(password)
                obj.save()
                reg.save()
                login(request, obj)
                return redirect('/User/product')
            else:
                error = "Password not match"
        return render(request, 'User_Profile/registration__form.html', {'form': form, 'error': error})
    else:
        form = Registration_form()
        return render(request, 'User_Profile/registration__form.html', {'form': form})

""" Login page """


def Login_View(request):
    try:
        if request.method == 'POST':
            form = login_form(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = User.objects.get(email=email)
                if not user:
                    error = "invalid user"
                else:
                    if check_password(password, user.password):
                        login(request, user)
                        return redirect('/User/product')
                    else:
                        error = "invalid password"
                        return render(request, 'User_Profile/login_form.html', {'form': form, 'error': error})
            return render(request, 'User_Profile/login_form.html', {'form': form, 'error': error})
        else:
            if request.user.is_authenticated():
                return redirect('/User/product')
            else:
                form = login_form()
                return render(request, 'User_Profile/login_form.html', {'form': form})
    except User.DoesNotExist:
        form = login_form()
        error = "user DoesNotExist"
        return render(request, 'User_Profile/login_form.html', {'form': form, 'error': error})
    except Exception as e:
        form = login_form()
        error = "Something went wrong"
        print(e)
        return render(request, 'User_Profile/login_form.html', {'form': form, 'error': error})

""" For logout """


def log_out(request):
    logout(request)
    return redirect('/User/login')

""" View profile page """


@csrf_exempt
def view_profile(request):
    return render(request, 'User_Profile/view.html')

""" Update image """


def Update_View(request):
    try:
        if request.method == 'POST':
            form = Update_form(request.POST, request.FILES)
            if form.is_valid():
                request_user = User.objects.get(username=request.user.username)
                user = Registration.objects.get(user_id=request_user)
                user._oldimage = user.profile_image
                user.profile_image = form.cleaned_data['profile_image']
                user.save()
                return redirect('/User/view')
            else:
                return HttpResponse("Invalid form")
        else:
            form = Update_form(request.FILES)
            return render(request, 'User_Profile/update_form.html', {'form': form})
    except Exception as e:
        print (str(e))
        return render(request, 'User_Profile/updated.html')


""" Delete user account """


def delete_account(request):
    delete_user = User.objects.get(username=request.user.username)
    delete_user.delete()
    if delete_user is not None:
        return HttpResponse("Delete account successfully")
    else:
        return HttpResponse("Not deleted")

""" Product page """


@login_required(login_url='/User/product')
def product_detail(request):
    product_info = Product.objects.all()
    return render(request, 'User_Profile/product.html', {'product_info': product_info})

""" View cart page """


@login_required(login_url='/User/product')
def view_carts(request, product_id):
    cart, created = Cart.objects.get_or_create(user=request.user, state='d')
    if created:
        cart.save()
    products = Product.objects.get(id=product_id)
    cartitem, cart_created = CartItem.objects.get_or_create(
        item=products, cart_id=cart)
    if cartitem:
        cartitem.save()
        cart.total += products.price
        cart.save()
    return redirect('/User/showcart')

""" Cart details """


@login_required(login_url='/User/product')
def cart_details(request):
    try:
        add_to_cart = Cart.objects.get(user=request.user, state='d')
        if add_to_cart is not None:
            cart_list = CartItem.objects.filter(cart_id=add_to_cart)
            if not cart_list:
                return render(request, 'User_Profile/empty.html')
            else:
                return render(request, 'User_Profile/view_cart.html', {'cart_list': cart_list, 'total': add_to_cart.total})
        else:
            return render(request, 'User_Profile/empty.html')
    except ObjectDoesNotExist:
        return render(request, 'User_Profile/empty.html')

""" Remove item from cart """


@login_required(login_url='/User/product')
def remove_item(request):

    cartitem_id = request.POST.get('cartitem_id')
    print cartitem_id
    delete_item = CartItem.objects.get(id=cartitem_id)
    cart = Cart.objects.get(user=request.user, state='d')
    delete_item.delete()
    cart.total -= delete_item.item.price
    if delete_item is not None:
        return JsonResponse({'status': 'success', 'total': cart.total})
    else:
        return JsonResponse({'status': 'fail'})

""" Update quantity"""


@login_required(login_url='/User/product')
def update_quantity(request):

    cartitem_id = request.POST.get('cartitem_id')
    operation = request.POST.get('operation')
    cart = Cart.objects.get(user=request.user, state='d')
    update_q = CartItem.objects.get(id=cartitem_id)

    if operation == "up":
        update_q.quantity += 1
        update_q.save()
        cart.total += update_q.item.price
        cart.save()

    elif operation == "down":
        update_q.quantity -= 1
        update_q.save()
        cart.total -= update_q.item.price
        cart.save()
    cart = Cart.objects.get(user=request.user, state='d')
    return JsonResponse({'status': 'success', 'id': update_q.id, 'total': cart.total})

""" Checkout page """


@login_required(login_url='/User/product')
def Checkout(request):
    cart = Cart.objects.get(user=request.user, state='d')
    cart.save()
    return render(request, 'User_Profile/checkout.html', {'cart': cart})

""" Payment page """


@login_required(login_url='/User/product')
def payment(request, cart_id):
    cart = Cart.objects.get(user=request.user, state='d')
    cart.state = "c"
    cart.save()
    return render(request, 'User_Profile/payment.html', {'cart': cart})
