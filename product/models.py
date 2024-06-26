from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    position = models.SmallIntegerField(choices=((0,'bugalter'),(1,'omborchi')))
    tel_number = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.position}'


class CoreModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Category(CoreModel):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'

    def __str__(self):
        return self.name


class Unit(CoreModel):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "O'lchov"
        verbose_name_plural = "O'lchovlar"

    def __str__(self):
        return self.name


class Product(CoreModel):
    class Meta:
        verbose_name = 'Maxsulot'
        verbose_name_plural = 'Maxsulotlar'
        unique_together = ('category_id', 'price', 'name')

    name = models.CharField(max_length=255)
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    unit_id = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True)
    quantity = models.DecimalField(decimal_places=2, max_digits=8)
    password = models.IntegerField(unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    description = models.TextField()
    product_slug = models.SlugField(default=slugify(name))

    def __str__(self):
        return f'{self.name} - {self.price} UZS'
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.product_slug = slugify(f"{self.category_id}-{self.name}-{self.price}-{self.pk}")        
        super(Product, self).save(*args, **kwargs)



class ProductInput(models.Model):
    class Meta:
        verbose_name = 'Kirim'
        verbose_name_plural = 'Kirimlar'

    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    responsible_user_id = models.ForeignKey(User,
                                            on_delete=models.SET_NULL,
                                            null=True,
                                            related_name='product_input')

    def __str__(self):
        return f'{self.product.name}({self.product.category_id}) - Kirim'


class ProductOutput(models.Model):
    class Meta:
        verbose_name = 'Chiqim'
        verbose_name_plural = 'Chiqimlar'

    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    removed_quantity = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    removed_at = models.DateTimeField(auto_now_add=True)
    responsible_user_id = models.ForeignKey(User,
                                            on_delete=models.SET_NULL, null=True,
                                            related_name='product_output')

    def __str__(self):
        return f'{self.product.name}({self.product.category_id}) - Chiqim'
