from django.db import models

# Create your models here.
 
class Brand(models.Model):
    brand_id = models.CharField(max_length=8)
    brand_name = models.CharField(max_length=32)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=11)
    manager_id  = models.CharField(max_length=8)
    def __str__(self):
        return self.brandName
class User(models.Model):
    brand_id = models.CharField(max_length=8)
    user_id = models.CharField(max_length=8)
    password = models.CharField(max_length=32)
    role = models.IntegerField()
    name = models.CharField(max_length=300)
    day_of_birth = models.DateTimeField('date published')
    phone_number = models.CharField(max_length=11)
    address = models.TextField(max_length=500)
    specialize = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Customer(models.Model):
    brand_id = models.CharField(max_length=8)
    customer_id = models.CharField(max_length=8)
    customer_name = models.CharField(max_length=32)
    day_of_birth = models.DateTimeField('date published')
    phone_number = models.CharField(max_length=11)
    address = models.TextField(max_length=500)
    source = models.TextField(max_length=500)
    fingerprint = models.TextField(max_length=500)
    medical_biography = models.TextField(max_length=500)
    def __str__(self):
        return self.customerName
class Relationship(models.Model):       
    customer_id_1 = models.CharField(max_length=8)
    customer_id_2 = models.CharField(max_length=8)
    relationship = models.CharField(max_length=32)
class Calendar_dentist(models.Model):  
    brand_id =  models.CharField(max_length=8)
    user_id = models.CharField(max_length=8)
    day = models.DateTimeField('date published')
    shift = models.IntegerField()
class Calendar_appointment(models.Model):  
    brand_id = models.CharField(max_length=8)
    user_id =  models.CharField(max_length=8)
    customer_id =  models.CharField(max_length=8)
    day = models.DateTimeField('date published')
    estimated_time = models.IntegerField()
    estimated_difficulty = models.IntegerField() 
    content = models.TextField(max_length=500)
    status = models.TextField(max_length=500)
    note = models.TextField(max_length=500)
    def __str__(self):
        return self.userID
class Treatment(models.Model):    
    brand_id = models.CharField(max_length=8)
    user_id = models.IntegerField()
    customer_id = models.IntegerField()
    treatment_id = models.IntegerField()
    time =  models.DateTimeField('date published')
    describe = models.TextField(max_length=500)
    total_payment =  models.IntegerField()

class Treatment_detail(models.Model):
    treatment_id = models.CharField(max_length=8)
    treatment_detail_id = models.CharField(max_length=8)
    time = models.DateTimeField('date published')
    content = models.TextField(max_length=500)
    price  = models.IntegerField()

class Invoice(models.Model):
    brand_id = models.CharField(max_length=8)
    user_id = models.CharField(max_length=8)
    customer_id = models.CharField(max_length=8)
    treatment_id = models.CharField(max_length=8)
    invoice_id = models.CharField(max_length=8)
    pay = models.IntegerField()

class Inventory(models.Model):
    brand_id = models.CharField(max_length=8)
    item_id = models.CharField(max_length=8)
    item_name = models.IntegerField()
    unit = models.CharField(max_length=32)
    quantity = models.IntegerField()

class Labo(models.Model):    
    brand_id = models.CharField(max_length=8)
    labo_name = models.CharField(max_length=100)
    address =  models.TextField(max_length=500)
    phone_number =  models.CharField(max_length=11)

class Treatment_detail_labo   (models.Model):
    labo_id = models.CharField(max_length=8)
    treatment_id = models.CharField(max_length=8)
    send_day = models.DateTimeField('date published')
    received_day = models.DateTimeField('date published')
    price = models.IntegerField()

