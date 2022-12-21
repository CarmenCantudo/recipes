from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Recipe status
STATUS = ((0, "Draft"), (1, "Published"))
LEVEL = ((0, "Easy"), (1, "Medium"), (2, "Hard"))


class Recipe(models.Model):
    """
    Recipe Model
    Modified from I think therefore I blog, Code Institute
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_posts")
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True,
                                   help_text="Describe the recipe")
    difficulty = models.IntegerField(choices=LEVEL, default=1)
    prep_time = models.CharField(blank=True, max_length=20)
    cooking_time = models.CharField(blank=True, max_length=20)
    ingredients = models.TextField()
    method = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='recipe_likes', blank=True)

    class Meta:
        """
        Orders recipes in descending order
        """
        ordering = ["-created_on"]

    def __str__(self):
        """
        Returns a string method (The Magic method)
        """
        return self.title

    def number_of_likes(self):
        """
        Returns the number of likes on a recipe
        """
        return self.likes.count()


class Comment(models.Model):
    """
    Comments Model
    Modified from I think therefore I blog, Code Institute
    """
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80, unique=True)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Order the comments in ascending order (oldest first)
        """
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
