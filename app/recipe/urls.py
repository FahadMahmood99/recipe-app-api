"""
Url mapping for recipe app.
"""

from django.urls import(path,include,)

from rest_framework.routers import DefaultRouter
from recipe import views

router =DefaultRouter()
router.register('recipes',views.RecipeViewSets)
router.register('tags',views.TagViewSets)
router.register('ingredients',views.IngredientViewSets)


app_name='recipe'

urlpatterns=[
    path('',include(router.urls)), 
]
