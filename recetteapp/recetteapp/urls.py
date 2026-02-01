from django.contrib import admin
from django.urls import path
from recettes.views import home, supprimer_recette

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path('supprimer/<int:id>/', supprimer_recette, name='delete_recette'),
]
