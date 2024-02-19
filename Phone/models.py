from django.db import models
from colorfield.fields import ColorField

# Create your models here.
class BaseModel(models.Model):
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)



class Category(BaseModel):
    name = models.CharField(max_length =250)
    image = models.ImageField(upload_to="Category")

    def __str__(self) -> str:
        return self.name
    

class Product(BaseModel):
    name = models.CharField(max_length=250)
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    guarantee = models.CharField(max_length=250)
    delivery = models.CharField(max_length=250)
    pickup = models.CharField(max_length=250)
    life_time = models.CharField(max_length=250)
    made_by = models.CharField(max_length=250)
    category = models.ForeignKey(Category)
    
    def __str__(self):
        return self.name



class Service(BaseModel):
        title = models.CharField(max_length=250)
        price = models.CharField(max_length=250)
        time = models.CharField(max_length=250)
        product = models.ForeignKey(Product , on_delete=models.PROTECT)

        def __str__(self) -> str:
            return self.title
        

class Forma(BaseModel):
        full_name = models.CharField(max_length=250)
        phone_number = models.CharField(max_length=250)

        def __str__(self) -> str:
            return self.full_name
        
class ServiceApplication(BaseModel):
       service = models.ForeignKey(Service, on_delete=models.PROTECT)
       full_name = models.CharField(max_length=250)
       phone_number = models.CharField(max_length=250)
    #    yana bitta ustun bolishi kk

       def __str__(self) -> str:
        return self.full_name
       

class Client(BaseModel):
      image = models.ImageField(upload_to="Client/")
      full_name = models.CharField(max_length=250)
      position = models.CharField(max_length=250)
      type = models.CharField(max_length=250 , choices=[("1","Stars"),("2","Company")])

      def __str__(self) -> str:
        return self.full_name

class FAQ(BaseModel):
     question = models.CharField(max_length = 250)
     answer = models.TextField()

     def __str__(self) -> str:
        return self.question
     

class Post(BaseModel):
     title = models.CharField(max_length = 250)
     description = models.TextField()
     image = models.ImageField(upload_to="Post/")

     def __str__(self) -> str:
        return self.title
     


class EmailAccount(BaseModel):
     email = models.EmailField(max_length = 254)

     def __str__(self) -> str:
        return self.email
     


class ProductInfoType(BaseModel):
     name = models.CharField(max_length =250)

     def __str__(self) -> str:
        return self.name
     

class ProductInfo(BaseModel):
     product = models.ForeignKey(Product ,on_delete=models.PROTECT)
     key = models.CharField(max_length =250)
     value = models.CharField(max_length =250)
     type = models.ForeignKey(ProductInfoType , on_delete=models.PROTECT)

     def __str__(self) -> str:
        return self.key
     

class ProductImages(BaseModel):
    product = models.ForeignKey(Product, on_delete = models.PROTECT)
    color = ColorField(default='black')
    image1 = models.ImageField(upload_to='product_images1/')
    image2 = models.ImageField(upload_to='product_images2/')
    image3 = models.ImageField(upload_to='product_images3/')
    price = models.DecimalField(max_digits=6 , decimal_places=2)

    def __str__(self) -> str:
        return self.product
class ProductPrice(BaseModel):
    product = models.ForeignKey(Product, on_delete = models.PROTECT)
    price = models.DecimalField(max_digits=6 , decimal_places=2)
    memory = models.CharField(max_digits=25)
    

