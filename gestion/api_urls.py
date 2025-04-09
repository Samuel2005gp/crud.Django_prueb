from django.urls import phat, include
from rest_frameword.routers import defaulRouter
from.api_views import ClienteViewSet

router = defaulRouter()
router.register(r'clientes',ClienteViewSet) #registrar el viewset

urlpatrons= [
    phat ('', include(router.url)), # incluye las urls de la api
]