from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, OrderItem, Order, Review
from django.contrib.auth.decorators import login_required

def add_to_cart(request, id):
  #پیدا کردن محصولی که کاربر انتخاب کرده
  product = get_object_or_404(Product, id=id)

  product_id = str(product.id)

  cart = request.session.get('cart',{})

  cart[product_id] = cart.get(product_id, 0) + 1

  request.session['cart'] = cart

  cart = request.session.get('cart', {})

  return redirect('cart')


def update_cart(request, id):
  #دریافت سبد خرید 
  cart = request.session.get('cart', {})

  #تبدیل ID محصول به string
  product_id = str(id)

  quantity = int(request.POST.get('quantity', 1))

  #اگر تعداد صفر یا کمتر بود محصول حذف شود 
  if quantity <= 0:
    cart.pop(product_id, None)
  else:
    cart[product_id] = quantity

  #ذخیره سبد جدید 
  request.session['cart'] = cart

  return redirect('cart')

def product_detail(request, id):
  #پیدا کردن محصول مورد نظر اگر وجود نداشت خطای 404 نمایش داده میشود
  product = get_object_or_404(Product, id=id)
  #دریافت محصولات فعال از همان دسته بندی
  #حداکثر 4 محصول برای بخش <<شما همچنان شاید دوست داشته باشین
  related_products = Product.objects.filter(
     category=product.category,
     is_active=True
  ).exclude(id=product.id)[:4]
  return render(request, 'products/product-details.html', {'product':product, 'related_products':related_products})

def products(request):
  products = Product.objects.all()
  return render(request, 'products/products.html', {"products":products})

def cart(request):
  #دریافت سبد خرید از session
  cart = request.session.get('cart', {})

  #گرفتن ID محصولات موجود در سبد
  product_ids = cart.keys()

  #پیدا کردن محصولات از دیتابیس 
  products = Product.objects.filter(id__in=product_ids)

  #محاسبه قیمت کل سبد 
  total_price = 0

  for product in products:
    #گرفتن تعداد محصول از session
    quantity = cart.get(str(product.id), 0)

    #محاسبه قیمت محصول 
    total_price += product.final_price * quantity

  return render(request, 'products/cart.html', {'cart':cart, 'products':products, 'total_price':total_price})

def remove_from_cart(request, id):
  cart = request.session.get('cart', {})

  product_id = str(id)

  if product_id in cart:
    del cart[product_id]

  request.session['cart'] = cart

  return redirect('cart')

def checkout(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        full_name = f'{first_name} {last_name}'

        cart = request.session.get('cart', {})

        products = Product.objects.filter(id__in=cart.keys())

        total_price = 0

        for product in products:
            quantity = cart.get(str(product.id), 0)
            total_price += product.final_price * quantity

        order = Order.objects.create(
           user=request.user if request.user.is_authenticated else None,
            name=full_name,
            phone=phone,
            address=address,
            total_price=total_price
        )

        for product in products:
            quantity = cart.get(str(product.id), 0)

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.final_price
            )

        request.session['cart'] = {}

        return redirect('order_success')

    return render(request, 'products/checkout.html')


@login_required
def my_orders(request):

   #دریافت سفارش های کاربر
   orders = Order.objects.filter(user=request.user).order_by('-created_at')
   return render(request, 'products/my-orders.html', {'orders':orders})

@login_required
def order_detail(request, id):
   order = get_object_or_404( Order, id=id, user=request.user)
   return render(request, 'products/order-detail.html', {'order':order})

def order_success(request):
   return render(request, 'products/order-success.html')


@login_required
def add_review(request, id):
   #پیدا کردن محصولی که کاربر میخواهد برای آن ثبت نظر کند
   product = get_object_or_404(Product, id=id)

   if request.method == 'POST':
      #دریافت امتیاز و متن
      rating = int(request.POST.get('rating', 5))
      comment = request.POST.get('comment')

      #ذخیره در دیتابیس
      Review.objects.create(
         product=product,
         user=request.user,
         rating=rating,
         comment=comment
      )

      return redirect('product_detail', id=product.id)
   return redirect('product_detail', id=product.id)



@login_required
def edit_review(request, id):

   #پیدا کردن نظر مورد نظر براساس ID
   #فقط صاحب همان نظر اجازه ویرایش آن را دارد
   review = get_object_or_404(
      Review,
      id=id,
      user=request.user
   )

   if request.method == 'POST':

      #دریافت امتیاز و متن جدید از فرم
      review.rating = int(request.POST.get('rating', 5))
      review.comment = request.POST.get('comment')

      #ذخیره تغییرات در دیتابیس
      review.save()

      return redirect(
         'product_detail',
         id=review.product.id
      )

   return render(request, 'products/edit-review.html', {'review':review})


@login_required
def delete_review(request, id):
   
   #پیدا کردن نظر مورد نظر
   #فقط صاحب همان نظر اجازه ویرایش آن را دارد
   review = get_object_or_404(
      Review,
      id=id,
      user=request.user
   )

   product_id = review.product.id

   if request.method == 'POST':
      review.delete()

   return redirect('product_detail', id=product_id)