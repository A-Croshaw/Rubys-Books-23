from django.db import models
#Choice fields

CONDITION = (
    ("new", "New"),
    ("used", "Used"),
)

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    view_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_View_name(self):
        return self.view_name


class Book(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    ISBN = models.CharField(max_length=254, null=True, blank=True)
    author = models.CharField(max_length=254)
    title = models.CharField(max_length=254 )
    link = models.CharField(max_length=254, null=True, blank=True)
    pages = models.PositiveIntegerField(null=True,blank=True)
    first_published = models.PositiveIntegerField(null=True,blank=True)
    this_publication_date = models.PositiveIntegerField(null=True,blank=True)
    condition = models.CharField(max_length=50, choices=CONDITION, default="new")
    description = models.TextField()
    language = models.CharField(max_length=254, null=True,blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

