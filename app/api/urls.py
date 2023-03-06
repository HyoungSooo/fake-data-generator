from ninja import NinjaAPI
from django.urls import path,include
from . import views
from api.router import router as faker_router

api = NinjaAPI()

api.add_router("/single_value/",faker_router)

urlpatterns = [
    path('', api.urls),
]
