from django.db import models

# Create your models here.
class identifacion_type(models.Model):
    type=models.CharField(max_length=150)
    abrev=models.CharField(max_length=4)
    created_at=models.DateTimeField()
    update_at=models.DateTimeField()
    delated_at=models.DateTimeField()




class country(models.Model):
    code=models.CharField(max_length=100)
    name=models.CharField(max_length=150)
    abrev=models.CharField(max_length=4)
    status=models.BooleanField()
    created_at=models.DateTimeField()
    update_at=models.DateTimeField()
    delated_at=models.DateTimeField()





class city(models.Model):

    code=models.CharField(max_length=10)
    Name=models.CharField(max_length=150)
    abrev=models.CharField(max_length=4)
    id_conutry=models.ForeignKey(country,null=True,blank=True,on_delete=models.CASCADE)
    status=models.BooleanField()
    created_at=models.DateTimeField()
    update_at=models.DateTimeField()
    delated_at=models.DateTimeField()
    

class user(models.Model) :

    first_name =models.CharField(max_length=200)
    last_name =models.CharField(max_length=200)
    id_identification_type=models.ForeignKey(identifacion_type,null=True,blank=True,on_delete=models.CASCADE)
    number_id =models.IntegerField()
    id_city=models.ForeignKey(city,null=True,blank=True,on_delete=models.CASCADE)
    email =models.CharField(max_length=200)
    passwork=models.CharField(max_length=200)
    status=models.BooleanField()
    created_at=models.DateTimeField()
    update_at=models.DateTimeField()
    delated_at=models.DateTimeField()




class session(models.Model):  
    identificador=models.CharField(max_length=200)
    id_user=models.ForeignKey(user,null=True,blank=True,on_delete=models.CASCADE)
    status=models.BooleanField()
    created_at=models.DateTimeField()
    update_at=models.DateTimeField()
    delated_at=models.DateTimeField()




class type(models.Model):
    code=models.CharField(max_length=100)
    name=models.CharField(max_length=150)
    abrev=models.CharField(max_length=4)
    status=models.BooleanField()
    created_at=models.DateTimeField()
    update_at=models.DateTimeField()
    delated_at=models.DateTimeField()




class race(models.Model):
    code=models.CharField(max_length=100)
    name=models.CharField(max_length=150)
    abrev=models.CharField(max_length=4)
    status=models.BooleanField()
    created_at=models.DateTimeField()
    update_at=models.DateTimeField()
    delated_at=models.DateTimeField()


    

class pet(models.Model):
    code=models.CharField(max_length=10)
    name=models.CharField(max_length=150)
    id_user=models.ForeignKey(user,null=True,blank=True,on_delete=models.CASCADE)
    identifacion_type=models.ForeignKey(type,null=True,blank=True,on_delete=models.CASCADE)
    id_race=models.ForeignKey(race,null=True,blank=True,on_delete=models.CASCADE)
    status=models.BooleanField()
    created_at=models.DateTimeField()
    update_at=models.DateTimeField()
    delated_at=models.DateTimeField()