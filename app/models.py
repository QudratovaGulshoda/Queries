from django.db import models


# Create your models here.
class CategoryManager(models.Manager):
    def counts(self):
        return super(CategoryManager, self).counts("ads")


class Category(models.Model):
    title = models.CharField(max_length=100)

    objects = CategoryManager()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # class Meta:

    #     abstract=True


class Adds(models.Model):
    name = models.CharField(max_length=100)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="ads")
    viewers = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)



    def __str__(self):
        return self.name
