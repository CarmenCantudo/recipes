from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeHome.as_view(), name='home'),
    path('recipes/', views.RecipeList.as_view(), name='recipes'),
    path('add_recipe/', views.AddRecipe.as_view(), name='add_recipe'),
    path('edit_recipe/<int:pk>', views.EditRecipe.as_view(), name='edit_recipe'
         ),
    path('delete_recipe/<int:pk>', views.DeleteRecipe.as_view(),
         name='delete_recipe'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>/', views.RecipeLike.as_view(), name='recipe_like'),
    path('comment/<int:pk>/edit', views.EditComment.as_view(),
         name='edit_comment'),
    path('comment/<int:pk>/delete', views.DeleteComment.as_view(),
         name='delete_comment'),
]
