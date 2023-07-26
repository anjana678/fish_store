from django.db import models

# Create your models here.
class loginn(models.Model):
    username=models.CharField(max_length=225)
    password=models.CharField(max_length=225)
    usertype=models.CharField(max_length=225)


class customerr(models.Model):
    login=models.ForeignKey(loginn,on_delete=models.CASCADE)
    fname=models.CharField(max_length=225)
    lname=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    address=models.CharField(max_length=225)

class sellerr(models.Model):
    login=models.ForeignKey(loginn,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=225)
    lastname=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    address=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    license=models.CharField(max_length=1000)

class category(models.Model):
    category=models.CharField(max_length=225)
    castatus=models.CharField(max_length=225)
    
class subcategory(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    subcategory=models.CharField(max_length=225)
    cstatus=models.CharField(max_length=225)

class product(models.Model):
    seller=models.ForeignKey(sellerr,on_delete=models.CASCADE)
    subcategory=models.ForeignKey(subcategory,on_delete=models.CASCADE)
    product=models.CharField(max_length=225)
    amt=models.CharField(max_length=225)
    quantity=models.CharField(max_length=225)
    image=models.CharField(max_length=1000)
    description=models.CharField(max_length=2000)
    pstatus=models.CharField(max_length=225)

class wishlist(models.Model):
    customerr=models.ForeignKey(customerr,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    
class booking(models.Model):
    customerr=models.ForeignKey(customerr,on_delete=models.CASCADE)
    seller=models.ForeignKey(sellerr,on_delete=models.CASCADE)
    total=models.CharField(max_length=225)
    date=models.CharField(max_length=225)
    status=models.CharField(max_length=225)
    order_id=models.CharField(max_length=225)

class bchild(models.Model):
    booking=models.ForeignKey(booking,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    qty=models.CharField(max_length=225)
    bamt=models.CharField(max_length=225)

class staff(models.Model):
    login=models.ForeignKey(loginn,on_delete=models.CASCADE)
    seller=models.ForeignKey(sellerr,on_delete=models.CASCADE)
    fn=models.CharField(max_length=225)
    ln=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    sstatus=models.CharField(max_length=225)

class services(models.Model):
    seller=models.ForeignKey(sellerr,on_delete=models.CASCADE)
    service=models.CharField(max_length=225)
    rate=models.CharField(max_length=225)
    des=models.CharField(max_length=225)



class srequest(models.Model):
    customer=models.ForeignKey(customerr,on_delete=models.CASCADE)
    service=models.ForeignKey(services,on_delete=models.CASCADE)
    amount=models.CharField(max_length=225) 
    date=models.CharField(max_length=225)    
    status=models.CharField(max_length=225)

class payment(models.Model):
    booking=models.ForeignKey(booking,on_delete=models.CASCADE)
    amount=models.CharField(max_length=225) 
    date=models.CharField(max_length=225)    



class req_payment(models.Model):
    srequest=models.ForeignKey(srequest,on_delete=models.CASCADE)
    amount=models.CharField(max_length=225) 
    date=models.CharField(max_length=225)    

class assign_staff_book(models.Model):
    booking=models.ForeignKey(booking,on_delete=models.CASCADE)
    staff=models.ForeignKey(staff,on_delete=models.CASCADE)
    date=models.CharField(max_length=225)    
    status=models.CharField(max_length=225)


class assign_staff_req(models.Model):
    srequest=models.ForeignKey(srequest,on_delete=models.CASCADE)
    staff=models.ForeignKey(staff,on_delete=models.CASCADE)
    date=models.CharField(max_length=225)    
    status=models.CharField(max_length=225)

# class feedback(models.Model):
#     product=models.ForeignKey(product,on_delete=models.CASCADE)

#     customer=models.ForeignKey(customerr,on_delete=models.CASCADE)
#     feedback=models.CharField(max_length=225)
#     date=models.CharField(max_length=225)    

class feedbacks(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)

    customer=models.ForeignKey(customerr,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=225)
    date=models.CharField(max_length=225) 

class review(models.Model):
    customer=models.ForeignKey(customerr,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    rate=models.CharField(max_length=50)
    reviews=models.CharField(max_length=50)
    date=models.CharField(max_length=50)


class sfeedback(models.Model):
    service=models.ForeignKey(services,on_delete=models.CASCADE)
    customer=models.ForeignKey(customerr,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=225)
    date=models.CharField(max_length=225) 

class sreview(models.Model):
    customer=models.ForeignKey(customerr,on_delete=models.CASCADE)
    service=models.ForeignKey(services,on_delete=models.CASCADE)
    rate=models.CharField(max_length=50)
    reviews=models.CharField(max_length=50)
    date=models.CharField(max_length=50)