from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Recipe
from .forms import CommentForm, RecipeForm


class RecipeHome(generic.ListView):
    """
    Home page
    """
    def get(self, request):
        recipes = Recipe.objects.filter(status=1).order_by('-created_on')[:6]
        context = {
                "recipes": recipes,
                }
        return render(request, 'index.html', context)


class RecipeList(generic.ListView):
    """
    List all recipes
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipes.html'
    paginate_by = 6


class RecipeDetail(View):
    """
    Recipe details
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Post method to submit comment
        """
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class RecipeLike(View):
    """
    Like or unlike recipes
    """
    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class AddRecipe(LoginRequiredMixin, CreateView):
    """
    Add a new recipe
    """
    model = Recipe
    template_name = 'add_recipe.html'
    form_class = RecipeForm
    success_url = reverse_lazy('recipes')
    pk_url_kwarg = 'pk'

    def form_valid(self, form):
        messages.success(self.request,
                         "Recipe added successfully and pending approval")
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)


class EditRecipe(LoginRequiredMixin, UpdateView):
    """
    Edit a recipe
    """
    model = Recipe
    template_name = 'edit_recipe.html'
    form_class = RecipeForm
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('recipes')

    def form_valid(self, form):
        messages.success(self.request, "Recipe updated successfully")
        form.instance.author = self.request.user
        return super(UpdateView, self).form_valid(form)

    def test_func(self):
        recipe = self.get_object()
        return recipe.author == self.request.user
