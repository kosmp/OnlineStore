from django.shortcuts import render, get_object_or_404
from .models import ProductType, Product, ModelType
from cart.forms import CartAddProductForm
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .forms import ProductForm
from django.core.exceptions import PermissionDenied
import requests

def product_list(request, product_type_name = None):
    product_type = None
    types = ProductType.objects.all()
    products = Product.objects.all();

    if product_type_name:
        product_type = get_object_or_404(ProductType, name = product_type_name)
        products = products.filter(type = product_type)

    sort = request.GET.get('sort')
    if sort == 'ascending':
        products = products.order_by('cost')
    elif sort == 'descending':
        products = products.order_by('-cost')

    return render(request, 'store/product/list.html',
                  {
                      'type': product_type,
                      'types': types,
                      'products': products,
                  })


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    cart_product_form = CartAddProductForm()
    joke = requests.get('https://official-joke-api.appspot.com/jokes/programming/random').json()[0]

    return render(request, 'store/product/detail.html', {'product': product,
                                                   'cart_product_form': cart_product_form,
                                                   'joke': joke['setup'] + joke['punchline']})


 
# сохранение данных в бд
def product_create(request):
    if not request.user.is_staff:
        raise PermissionDenied("You do not have access to this page.")

    form = ProductForm()

    if request.method == "POST":
        
        product = Product.objects.create(name=request.POST.get('name'),
                                         model=ModelType.objects.get(id=request.POST.get('model')),
                                         cost=request.POST.get('cost'),
                                         type=ProductType.objects.get(id=request.POST.get('type')),
                                         quantity=0,
                                         description=request.POST.get('description'),
                                         image=request.FILES.get('image'),
                                         produced=request.POST.get('produced'))

        product.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "store/product/create.html", {"form" : form})
    
 
# изменение данных в бд
def product_edit(request, id):
    if not request.user.is_staff:
        raise PermissionDenied("You do not have access to this page.")

    try:
        product = Product.objects.get(id=id)
        form = ProductForm(initial={'name':product.name, 'model':product.model,
                                    'cost':product.cost, 'type':product.type, 
                                    'description':product.description, 'image':product.image,
                                    'produced':product.produced})

        if request.method == "POST":
            product.model=ModelType.objects.get(id=request.POST.get('model'))
            product.cost=request.POST.get('cost')
            product.type=ProductType.objects.get(id=request.POST.get('type'))
            product.description=request.POST.get('description')
            if request.FILES.get('image') != None:
                product.image=request.FILES.get('image')
            if(request.POST.get('produced') == None): 
                product.produced=False
            else:
                product.produced=True

            product.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "store/product/edit.html", {"product": product, "form" : form})
    except product.DoesNotExist:
        return HttpResponseNotFound("<h2>product not found</h2>")
     
# удаление данных из бд
def product_delete(request, id):
    if not request.user.is_staff:
        raise PermissionDenied("You do not have access to this page.")

    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/")
    except product.DoesNotExist:
        return HttpResponseNotFound("<h2>product not found</h2>")
