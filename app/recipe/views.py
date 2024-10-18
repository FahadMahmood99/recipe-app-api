"""
Views for thr recipe APIs
"""
from rest_framework import (
    viewsets,mixins
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import (
    Recipe,Tag,Ingredient
)
from recipe import serializers
# Create your views here.


class RecipeViewSets(viewsets.ModelViewSet):
    """View for manage recipe APIs"""
    serializer_class=serializers.RecipeSerializer
    queryset=Recipe.objects.all()
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipes for authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')
     

    def get_serializer_class(self):
        """Return the serailizer class for request"""
        if self.action == 'list':
            return serializers.RecipeSerializer
        
        return self.serializer_class 
    
    def perform_create(self, serializer):
        """Create a anew recipe"""
        serializer.save(user=self.request.user)


class TagViewSets(mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """View for managing tags in database"""
    serializer_class=serializers.TagSerializer
    queryset=Tag.objects.all()
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        """Filter queryset to authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-name')
     


class IngredientViewSets(mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """View for managing ingredients in database"""

    serializer_class=serializers.IngredientSerializer
    queryset=Ingredient.objects.all()
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        """Filter queryset to authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-name')
     



