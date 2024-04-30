from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    position = models.CharField(max_length=100)
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


class Product(CoreModel):
    class Meta:
        verbose_name = 'Maxsulot'
        verbose_name_plural = 'Maxsulotlar'

    name = models.CharField(max_length=255)
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    unit = models.CharField(max_length=30)
    quantity = models.DecimalField(decimal_places=2, max_digits=8)
    password = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    description = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.price} UZS'


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
        verbose_name = 'Chqiqm'
        verbose_name_plural = 'Chiqimlar'

    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    removed_at = models.DateTimeField(auto_now_add=True)
    responsible_user_id = models.ForeignKey(User,
                                            on_delete=models.SET_NULL, null=True,
                                            related_name='product_output')

    def __str__(self):
        return f'{self.product.name}({self.product.category_id}) - Chiqim'
