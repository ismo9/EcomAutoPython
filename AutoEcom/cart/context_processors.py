from .cart import Cart

# Create context processor so our cart can work on all pages 
def cart(request):
    return {'cart': Cart(request) }
