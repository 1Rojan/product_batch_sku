from django.db import models


class Batch(models.Model):
    SHOE_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    SHOE_COLOR = (
        ('Blk', 'Black'),
        ('Wht', 'White'),
        ('Gry', 'Gray')
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    size = models.CharField(max_length=1, choices=SHOE_SIZES)
    color = models.CharField(max_length=3, choices=SHOE_COLOR)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'batches'


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media', default='default.png')
    batch_info = models.ForeignKey(Batch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']


class Sku(models.Model):
    sku_number = models.CharField(max_length=8)
    created = models.DateTimeField(auto_now_add=True)
    product_info = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.sku_number

    class Meta:
        ordering = ['created']
