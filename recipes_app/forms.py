from .models import Comment, Recipe, Category
from django_summernote.widgets import SummernoteWidget
from django import forms


# Query to get the categories created in the admin panel
category = Category.objects.all().values_list('name', 'name')
category_list = []
# Add to category_list
for item in category:
    category_list.append(item)


class CommentForm(forms.ModelForm):
    """
    Create a Comment Form
    """
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    """
    Add a Recipe Form
    """
    class Meta:
        model = Recipe
        fields = [
            'title',
            'category',
            'description',
            'difficulty',
            'serves',
            'prep_time',
            'cooking_time',
            'ingredients',
            'method',
            'featured_image',
        ]

        widgets = {
            'category': forms.Select(choices=category_list),
            'method': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
        }

        def __init__(self, *args, **kwargs):
            super(RecipeForm, self).__init__(*args, **kwargs)
