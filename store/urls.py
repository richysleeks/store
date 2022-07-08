from django.urls import path
from .views import( home, product, checkout, cart)


app_name = 'store'

urlpatterns = [
	#Leave as empty string for base url
	path('', home, name="home"),
	path('product/<int:id>', product, name="product"),
	path('cart/', cart, name="cart"),
	path('checkout/', checkout, name="checkout"),

	# path('update_item/', views.updateItem, name="update_item"),
	# path('process_order/', views.processOrder, name="process_order"),

]