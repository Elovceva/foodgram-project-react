from django.contrib import admin

from .models import (Favorite, Ingredient, Recipe,
                     ShoppingCart, Tag)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Параметры админ зоны рецептов."""
    list_display = ('pk', 'name', 'author', 'favorite')
    list_filter = ('name', 'author', 'tags')

    def favorite(self, obj):
        return obj.favorite.all().count()


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """Параметры админ зоны продуктов."""
    list_display = ('pk', 'name', 'measurement_unit',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Параметры админ зоны тэгов."""
    list_display = ('pk', 'name', 'slug')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """Параметры админ зоны избранных рецептов."""
    list_display = ('pk', 'user', 'recipe')


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    """Параметры админ зоны продуктовой корзины."""
    list_display = ('pk', 'user', 'recipe')
