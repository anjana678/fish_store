from django.shortcuts import render,HttpResponse,redirect
from store.models import *
from django.core.files.storage import FileSystemStorage
from django.db.models import Sum
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from .forms import MyForm
from django.core.mail import send_mail
from django.conf import settings
from razorpay import Client
from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.sessions.backends.db import SessionStore
# Create your views here.



def make_payment(request):
        # Get form data
    amount = 5000
    currency="INR"

        # Create Razorpay client object

    razorpay_client = Client(auth=("rzp_test_nk1Mi9EOKURNty", "dmlPjxwpEFxw6BGmunljJJHo"))

        # Create a payment
    order = razorpay_client.order.create({
        "amount": amount,
        "currency": currency,
        'receipt': 'receipt_id'
    })

    # Get the order ID
    order_id = order['id']
    print(order_id)
    print("AHiiiiiiii")

    # out=razorpay_client.order.fetch(order_id)
    # print(out)
    return 'HAi'


def process_form(request):
  if request.method == "POST":

    name = request.POST.get('id')
    print("sssssssssssssssssssssssss",name)
    return JsonResponse({'status':'success'}) 

# ---------------------------------------------------PUBLIC---------------------------------------------------------------------
def findcategoryss(lid):
    sid=customerr.objects.filter(login=lid)
    fname=sid[0].fname

    cat=category.objects.filter(castatus='active')
    result=[]
    ss=fname
    if cat:
        cat_id=cat[0].id
        
        for i in cat:
            row={}
            catt_id=i.id
            print(catt_id)
            subcats=subcategory.objects.filter(category_id=catt_id,cstatus='active')
            row['cat']=i.category
            
            row['subcats'] = subcats
            result.append(row)
          
    return result,ss





def index(request):
    q=services.objects.all()
    q1=product.objects.filter(pstatus='active')
    # q11=product.objects.all()
    q11=product.objects.all().order_by('-id')[:6]
    print('new arrivals',q11)

    # b1=bchild.objects.all().count()
    # print(b1)
    # p=bchild.objects.all()
    # for i in p:
    #     piid=i.product_id
        # b1=product.objects.filter(id=piid)
    # b1=bchild.objects.all().annotate(count=Count('product_id')).filter(product_id__gte=2).distinct()
    b1=  bchild.objects.values('product_id','product__image').distinct()

    print("bs",b1)
  

    return render(request,'index.html',{'q':q,'q1':q1,'b1':b1,'q11':q11})

def signup(request):
    encryptedpassword=make_password("admin")
    print(encryptedpassword)
    # decryptedpassword=check_password("admin",encryptedpassword)
    # print(decryptedpassword)
    return render(request,'signup.html')

def forgot_password(request):
    if request.method=="POST":
        fname=request.POST['fname']
        q=loginn.objects.filter(username=fname)
        if q:
            lid=q[0].id
            eids=q[0].username
            ut=q[0].usertype
            if ut=="customer":
                qq=customerr.objects.filter(login_id=lid)
                if qq:
                    eid=qq[0].email
            elif ut=="seller":
                qq=sellerr.objects.filter(login_id=lid)
                if qq:
                    eid=qq[0].email
            elif ut=="staff":
                qq=staff.objects.filter(login_id=lid)
                if qq:
                    eid=qq[0].email
            elif ut=="pending":
                    return HttpResponse("<script>alert('YOUR ACCOUNT IS NOT VERIFIED !!!!!PLEASE CHECK YOUR MAIL TO VERIFY YOUR ACCOUNT');window.location='/login'</script>" )
            
            subject = 'FORGOT PASSWORD'
            message = f"Sir/Madam,\n Your <a href=http://127.0.0.1:8000/set_password/{lid}/{eid}>click to login here</a>"
            
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [eid]
            send_mail( subject, message, email_from, recipient_list )

            # return HttpResponse("<script>alert('your username verified successfully');window.location='/set_password/%s/%s'</script>" %(lid,eid))
            return HttpResponse("<script>alert('your username verified successfully');alert('please check your mail');window.location='/'</script>")
        else:
            return HttpResponse("<script>alert('Enter your correct username to verify');window.location='/forgot_password'</script>" )
    return render(request,'forgot_password.html')


def set_password(request,id,eid):
    if request.method=="POST":
        cpwd=request.POST['cpwd']
        confirm_encryptedpassword=make_password(cpwd)
        print(confirm_encryptedpassword)
        q=loginn.objects.get(id=id)
        if q:
            q.password=confirm_encryptedpassword
            q.save()
            subject = 'CHANGE PASSWORD'
            message = f"Sir/Madam,\n Your <a href=http://127.0.0.1:8000/login>click to login here</a>"
            
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [eid]
            send_mail( subject, message, email_from, recipient_list )
            return HttpResponse("<script>alert('your password changed successfully');window.location='/login'</script>")


    return render(request,'set_password.html')

# def customer_header(request):
#     cat=category.objects.all()
#     return render(request,'customer_header.html',{'cat':cat})


# Create your views here.
# def home(request):
#    if request.method=="POST":
#       form=MyForm(request.POST)
#       if form.is_valid():
#          print("success")
#       else:
#          print("fail")
#    form=MyForm()
#    print(form)
#    return render(request,"home.html",{"form":form})

def logoutnow(request):
    logout(request)
    request.session.clear()
    return redirect('/')


def logins(request):
    # if 'login_id' in request.session:
    if request.method == "POST":
        forms = MyForm(request.POST)
        if forms.is_valid():
            u=request.POST['uname']
            p=request.POST['pwd']
            # encryptedpassword=make_password(p)
            # print('--------encrypt----------',encryptedpassword)
            try:
                q=loginn.objects.get(username=u)

                decryptedpassword=check_password(p,q.password)
                print('--------Decrypt----------',decryptedpassword)
                if decryptedpassword==True:
                    # process the form
                    # q=loginn.objects.get(username=u,password=encryptedpassword)
                    request.session['login_id']=q.pk
                    if q.usertype=="admin":
                        return HttpResponse("<script>window.location='/adminhome'</script>")
                    elif q.usertype=="seller":            
                        return HttpResponse("<script>window.location='/seller_home'</script>")
                    elif q.usertype=="customer":            
                        return HttpResponse("<script>window.location='/customer_home'</script>")
                    elif q.usertype=="staff":            
                        return HttpResponse("<script>window.location='/staff_home'</script>")
                    elif q.usertype=="reject":            
                        return HttpResponse("<script>alert('your account is blocked');window.location='/login'</script>")
                    elif q.usertype=="pending":            
                        return HttpResponse("<script>alert('your account is on processing');window.location='/login'</script>")
                else:
                    return HttpResponse("<script>alert('Enter Password is not correct');window.location='/login'</script>")
        
            except:
                # else:
                    # show error message
                return HttpResponse("<script>alert('login failed');window.location='/login'</script>")

    else:
        forms = MyForm()
    
    # else:
    #     return redirect('/')
    return render(request, 'login.html', {'form': forms})



# def logins(request):
#     if request.method=="POST":
#         u=request.POST['uname']
#         p=request.POST['pwd']
#         try:
#             q=loginn.objects.get(username=u,password=p)
#             request.session['login_id']=q.pk
#             if q.usertype=="admin":
#                 return HttpResponse("<script>alert('login successfully');window.location='/adminhome'</script>")
#             elif q.usertype=="seller":            
#                 return HttpResponse("<script>alert('login successfully');window.location='/seller_home'</script>")
#             elif q.usertype=="customer":            
#                 return HttpResponse("<script>alert('login successfully');window.location='/customer_home'</script>")
#             elif q.usertype=="staff":            
#                 return HttpResponse("<script>alert('login successfully');window.location='/staff_home'</script>")
#         except:
#             return HttpResponse("<script>alert('login failed');window.location='/login'</script>")


#     return render(request,'login.html')


def seller_register(request):
    if request.method=="POST":
        a=request.POST['a']
        b=request.POST['b']
        c=request.POST['c']
        d=request.POST['d']
        e=request.POST['e']
        f=request.POST['f']        
        g=request.POST['g']
        ls=request.FILES['lll']
        addr=request.POST['address']

        fs=FileSystemStorage()
        fn=fs.save(ls.name,ls)
        encryptedpassword=make_password(g)
        print(encryptedpassword)
        lg=loginn.objects.filter(username=f)
        print(lg)
        if lg:
            return HttpResponse("<script>alert('username already exist');window.location='/seller_register'</script>")
        else:
            le=sellerr.objects.filter(email=e)
            if le:
                return HttpResponse("<script>alert('email already exist!!!Please Try Another Vaild Mail');window.location='/seller_register'</script>")
            else:
                ql=loginn(username=f,password=encryptedpassword,usertype='pending')
                ql.save()
                q=sellerr(firstname=a,lastname=b,place=c,phone=d,email=e,address=addr,license=fn,login=ql)
                q.save()
                subject = 'VERIFICATION'
                message = f"Sir/Madam,\n Your <a href=http://127.0.0.1:8000/acceptseller_username/{ql.id}>verify</a>"
                
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [e]
                send_mail( subject, message, email_from, recipient_list )
            return HttpResponse("<script>alert('registered successfuly');alert('THANK YOU FOR REGISTERED WITH US !!!!!!PLEASE CHECK YOUR MAIL FOR ACCOUNT VERIFICATION');window.location='/login'</script>")

    return render(request,'seller_register.html')


def customer_register(request):
    if request.method=="POST":
        a=request.POST['a']
        b=request.POST['b']
        c=request.POST['c']
        d=request.POST['d']
        e=request.POST['e']
        f=request.POST['f']        
        g=request.POST['g']
        addr=request.POST['address']
        encryptedpassword=make_password(g)
        print(encryptedpassword)
        lg=loginn.objects.filter(username=f)
        print(lg)
        if lg:
            return HttpResponse("<script>alert('username already exist');window.location='/customer_register'</script>")
        else:
            le=customerr.objects.filter(email=e)
            if le:
                return HttpResponse("<script>alert('email already exist!!!Please Try Another Vaild Mail');window.location='/seller_register'</script>")
            else:
                ql=loginn(username=f,password=encryptedpassword,usertype='pending')
                ql.save()
                q=customerr(fname=a,lname=b,place=c,phone=d,email=e,address=addr,login=ql)
                q.save()
                subject = 'VERIFICATION'
                message = f"Sir/Madam,\n Your <a href=http://127.0.0.1:8000/acceptcustomer_username/{ql.id}>verify</a>"
                
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [e]
                send_mail( subject, message, email_from, recipient_list )
                return HttpResponse("<script>alert('registered successfuly');alert('THANK YOU FOR REGISTERED WITH US !!!!!!PLEASE CHECK YOUR MAIL FOR ACCOUNT VERIFICATION');window.location='/login'</script>")
    return render(request,'customer_register.html')

def acceptseller_username(request,id):
    cus=loginn.objects.get(id=id)
    cus.usertype='seller'
    cus.save()
    return HttpResponse("<script>alert('Verified');window.location='/login'</script>")
def acceptcustomer_username(request,id):
    cus=loginn.objects.get(id=id)
    cus.usertype='customer'
    cus.save()
    return HttpResponse("<script>alert('Verified');window.location='/login'</script>")
  
    # return render(request,'adminhome.html',{'cus':cus,'sel':sel,'ser':ser,'bk':bk})


# ---------------------------------------------------PUBLIC---------------------------------------------------------------------
# ---------------------------------------------------ADMIN---------------------------------------------------------------------


def adminhome(request):
    if 'login_id' in request.session:

        # request.session.clear()
        cus=customerr.objects.all().count()
        sel=sellerr.objects.all().count()
        ser=services.objects.all().count()
        bk=booking.objects.all().count()
    else:
        return redirect('/')
    return render(request,'adminhome.html',{'cus':cus,'sel':sel,'ser':ser,'bk':bk})



def admin_sales_report(request):
    from datetime import datetime, timedelta
    if 'login_id' in request.session:
 
            # q=bchild.objects.filter(booking__date__gte=start_date,booking__date__gte=end_date).exclude(booking__status='pending')
            # # q=bchild.objects.filter(start_date__gte=start_date, start_date__lte=end_date)
            # print(q)
        q=bchild.objects.all().exclude(booking__status='pending')

        # if request.method=="POST":
        #     start_date=request.POST['start_date']
        #     end_date=request.POST['end_date']
        #     q = bchild.objects.filter(booking__date__gte=start_date, booking__date__lte=end_date).exclude(booking__status='pending')
        #     print("mmmmm",q)


        # #     q=bchild.objects.filter(booking__date=start_date)
        # # if request.method=="POST":
        # #     start_date_str = request.POST['start_date']
        # #     end_date_str = request.POST['end_date']
        # #     start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        # #     end_date = datetime.strptime(end_date_str, '%Y-%m-%d') 
        # #     # + timedelta(days=1)  # Add one day to include the end date in the range
        # #     print("mmmmm",start_date)
        # #     print("mmend_datemmm",end_date)

        # #     q = bchild.objects.filter(booking__date__gte=start_date, booking__date__lte=end_date).exclude(booking__status='pending')
        # #     print("mmmmm",q)

        # # else:
        # #     q = bchild.objects.exclude(booking__status='pending')

        # if request.method == "POST":
        #     start_date = request.POST.get('start_date')
        #     end_date = request.POST.get('end_date')

        #     # Convert start_date and end_date strings to datetime objects
        #     start_date_obj = datetime.strptime(start_date, '%Y-%m-%d').date()
        #     end_date_obj = datetime.strptime(end_date, '%Y-%m-%d').date()

        #     # Query bchild objects with related bookings in the date range
        #     q = bchild.objects.filter(booking__date__gte=start_date_obj, booking__date__lte=end_date_obj).exclude(booking__status='pending')
        #     print(q)
        # else:
        #     # Query all bchild objects with related bookings
        #     q = bchild.objects.all().exclude(booking__status='pending')
    else:
        return redirect('/')
    return render(request,'admin_sales_report.html',{'q':q})


# -------------------------services===================



def admin_view_srequest(request):
    if 'login_id' in request.session:
        q=srequest.objects.all()
        ss={}

        ss['q']=q
    else:
        return redirect('/')
    return render(request,'admin_view_srequest.html',ss)





def admin_view_sfeedback(request,service_id):
    if 'login_id' in request.session:

 
        
        cus=sfeedback.objects.filter(service_id=service_id)
        ss={}
  
        ss['cus']=cus
    else:
        return redirect('/')
    return render(request,'admin_view_sfeedback.html',ss)


def admin_view_srating(request,service_id):
    if 'login_id' in request.session:


        
        cus=sreview.objects.filter(service_id=service_id)
        ss={}
  
        # ss['firstname']=firstname
        ss['cus']=cus
    else:
        return redirect('/')
    return render(request,'admin_view_srating.html',ss)






def admin_view_feedback(request,id):
    if 'login_id' in request.session:

        cus=feedbacks.objects.filter(product_id=id)
    else:
        return redirect('/')
    return render(request,'admin_view_feedback.html',{'cus':cus})

def admin_view_rating(request,product_id):
    if 'login_id' in request.session:        
        cus=review.objects.filter(product_id=product_id)
        ss={}  
        ss['cus']=cus
    else:
        return redirect('/')
    return render(request,'admin_view_rating.html',ss)

def admin_view_customer(request):
    if 'login_id' in request.session:

        cus=customerr.objects.all()

        if request.method=="POST":
            sname=request.POST['sname']
            cus=customerr.objects.filter(fname=sname)|customerr.objects.filter(lname=sname)|customerr.objects.filter(place=sname)|customerr.objects.filter(phone=sname)|customerr.objects.filter(email=sname)
    else:
        return redirect('/')
    return render(request,'admin_view_customer.html',{'cus':cus})



def admin_view_bk(request,id):
    if 'login_id' in request.session:
        q=booking.objects.filter(customerr_id=id)
        print(q)
    else:
        return redirect('/')
    return render(request,'admin_view_bk.html',{'q':q})

def admin_view_booking_details(request,id):
    if 'login_id' in request.session:

        q=bchild.objects.filter(booking_id=id)
        print(q)
    else:
        return redirect('/')
    return render(request,'admin_view_booking_details.html',{'q':q})



def admin_view_seller(request):
    if 'login_id' in request.session:

        q=sellerr.objects.all()
        if request.method=="POST":
            sname=request.POST['sname']
            q=sellerr.objects.filter(firstname=sname)|sellerr.objects.filter(lastname=sname)|sellerr.objects.filter(place=sname)|sellerr.objects.filter(phone=sname)|sellerr.objects.filter(email=sname)
    else:
        return redirect('/')
    return render(request,'admin_view_seller.html',{'q':q})

def accept_seller(request,id,email):
    q=loginn.objects.get(id=id)
    q.usertype='seller'
    q.save()
    subject = 'verification'
    message = f"Accepted  \n Having Wonderful day"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail( subject, message, email_from, recipient_list )

    return HttpResponse("<script>alert('Verified successfuly');window.location='/admin_view_seller'</script>")

def reject_seller(request,id,email):
    q=loginn.objects.get(id=id)
    q.usertype='reject'
    q.save()
    subject = 'verification'
    message = f"Rejected  \n Having Wonderful day"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("<script>alert('block successfuly');window.location='/admin_view_seller'</script>")

def accept_customer(request,id,email):
    q=loginn.objects.get(id=id)
    q.usertype='customer'
    q.save()
    subject = 'verification'
    message = f"Accepted  \n Having Wonderful day"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("<script>alert('block successfuly');window.location='/admin_view_customer'</script>")

def reject_customer(request,id,email):
    q=loginn.objects.get(id=id)
    q.usertype='reject'
    q.save()

    subject = 'verification'
    message = f"Rejected  \n Having Wonderful day"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("<script>alert('unblock successfuly');window.location='/admin_view_customer'</script>")


def admin_view_services(request,id):
    if 'login_id' in request.session:

        q=services.objects.filter(seller_id=id)
    else:
        return redirect('/')
    return render(request,'admin_view_services.html',{'q':q})






def analysis_chart(request):


    cus=customerr.objects.all().count()
    print(cus)
    sel=sellerr.objects.all().count()
    print(sel)
    sta=staff.objects.all().count()
    print(sta)

    return render(request,'analysis_chart.html',{'cus':cus,'sel':sel,'sta':sta})




def admin_view_products(request,id):
    if 'login_id' in request.session:

        q=product.objects.filter(seller_id=id)
    else:
        return redirect('/')
    return render(request,'admin_view_products.html',{'q':q})
def admin_view_staff(request,id):
    if 'login_id' in request.session:

        q=staff.objects.filter(seller_id=id)
    else:
        return redirect('/')
    return render(request,'admin_view_staff.html',{'q':q})

# ---------------------------------------------------ADMIN---------------------------------------------------------------------
# ---------------------------------------------------SELLER---------------------------------------------------------------------
def seller_home(request):
    if 'login_id' in request.session:
        lid=request.session['login_id']
        sid=sellerr.objects.filter(login=lid)
        if sid: 
            sids=sid[0].id
            firstname=sid[0].firstname
            print("HI")
        cus=product.objects.filter(seller_id=sids).count()
        sel=staff.objects.filter(seller_id=sids).count()
        ser=services.objects.filter(seller_id=sids).count()
        bk=booking.objects.filter(seller_id=sids).count() 
    else:
        return redirect('/')
        # return HttpResponse("<script>alert('profile updated successfully');window.location='/'</script>")
 

    return render(request,'seller_home.html',{'firstname':firstname,'cus':cus,'sel':sel,'ser':ser,'bk':bk})


def seller_update_profile(request):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        sid=sellerr.objects.filter(login=lid)
        sellerid=sid[0].id
        firstname=sid[0].firstname

        print(sellerid)

        up=sellerr.objects.get(id=sellerid)
        if request.method=="POST":
            fn=request.POST['a']
            ln=request.POST['b']
            place=request.POST['c']
            phone=request.POST['d']
            email=request.POST['e']
            addr=request.POST['address']

            up.firstname=fn
            up.lastname=ln
            up.place=place
            up.phone=phone
            up.email=email
            up.address=addr
            up.save()
            return HttpResponse("<script>alert('profile updated successfully');window.location='/seller_update_profile'</script>")
    else:
        return redirect('/')
    
    return render(request,'seller_update_profile.html',{'up':up,'firstname':firstname})


def seller_change_password(request):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        q=loginn.objects.filter(id=lid)
        sid=sellerr.objects.filter(login=lid)
        firstname=sid[0].firstname
        username=q[0].username
        print(username)

        if request.method=="POST":
            np=request.POST['password']
            cp=request.POST['confirm_password']
            confirm_encryptedpassword=make_password(cp)
            print(confirm_encryptedpassword)
            q=loginn.objects.get(id=lid)       
            q.password=confirm_encryptedpassword
            q.save()
            return HttpResponse("<script>alert('password changed successfully');window.location='/login'</script>")
    else:
        return redirect('/')
    return render(request,'seller_change_password.html',{'username':username,'firstname':firstname})





def seller_manage_staff(request):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        sids=sellerr.objects.filter(login=lid)
        sid=sids[0].id
        firstname=sids[0].firstname
        q2=staff.objects.filter(seller_id=sid)

        if request.method=="POST":
            s=request.POST['s']
            q2=staff.objects.filter(seller_id=sid)
            if q2:
                q2=staff.objects.filter(fn=s,seller_id=sid)|staff.objects.filter(ln=s,seller_id=sid)|staff.objects.filter(place=s,seller_id=sid)|staff.objects.filter(phone=s,seller_id=sid)|staff.objects.filter(email=s,seller_id=sid)
            else:
                return HttpResponse("<script>alert('no results found');window.location='/seller_manage_staff'</script>")

    else:
        return redirect('/')

    
    return render(request,'seller_manage_staff.html',{'q2':q2,'firstname':firstname})



def seller_add_staff(request):
    if 'login_id' in request.session:
        lid=request.session['login_id']
        sids=sellerr.objects.filter(login=lid)
        sid=sids[0].id
        firstname=sids[0].firstname

        if request.method=="POST":
            fname=request.POST['fname']
            b=request.POST['b']
            c=request.POST['c']
            d=request.POST['d']
            e=request.POST['e']
            f=request.POST['f']        
            g=request.POST['g']
            encrypt=make_password(g)
            print('=========encrypt office===========',encrypt)
            lg=loginn.objects.filter(username=f)
            print(lg)
            if lg:
                return HttpResponse("<script>alert('username already exist');window.location='/seller_manage_staff'</script>")
            else:
                ql=loginn(username=f,password=encrypt,usertype='staff')
                ql.save()
                qs=staff(fn=fname,ln=b,place=c,phone=d,email=e,login=ql,sstatus='active',seller_id=sid)
                qs.save()
                subject = 'Login Credentials  '
                message = f"Sir/Madam,\n Your Username={f} and Password={g}   \n Having Wonderful day"
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [e]
                send_mail( subject, message, email_from, recipient_list )
                return HttpResponse("<script>alert('added successfuly');window.location='/seller_manage_staff'</script>")
    else:
        return redirect('/')
    
        
    return render(request,'seller_add_staff.html',{'firstname':firstname})



def delete_staff(request,id):
    q=staff.objects.filter(login=id)
    q.delete()
    return HttpResponse("<script>alert('deleted successfuly');window.location='/seller_manage_staff'</script>")



def update_staff(request,id):
    if 'login_id' in request.session:
        lid=request.session['login_id']
        seller_id=sellerr.objects.filter(login=lid)
        sellerid=seller_id[0].id
        firstname=seller_id[0].firstname

        print(sellerid)
        q2=staff.objects.filter(seller_id=sellerid)

        up=staff.objects.get(login=id)
        if request.method=="POST":
            fn=request.POST['a']
            ln=request.POST['b']
            place=request.POST['c']
            phone=request.POST['d']
            email=request.POST['e']
            up.fn=fn
            up.ln=ln
            up.place=place
            up.phone=phone
            up.email=email
            up.save()
            return HttpResponse("<script>alert(' updated successfully');window.location='/seller_manage_staff'</script>")
    else:
        return redirect('/')

    return render(request,'seller_manage_staff.html',{'up':up,'q2':q2,'firstname':firstname})
def staff_active(request,id):
    q=staff.objects.get(id=id)
    q.sstatus='active'
    q.save()
    return HttpResponse("<script>alert('active successfuly');window.location='/seller_manage_staff'</script>")

def staff_deactive(request,id):
    q=staff.objects.get(id=id)
    q.sstatus='deactive'
    q.save()
    return HttpResponse("<script>alert('deactive successfuly');window.location='/seller_manage_staff'</script>")




def seller_manage_product(request):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        seller_id=sellerr.objects.filter(login=lid)
        sid=seller_id[0].id
        firstname=seller_id[0].firstname
        q=product.objects.filter(seller_id=sid)
        if request.method=="POST":
            a=request.POST['a']
            scid=request.POST['scid']
            b=request.POST['b']
            c=request.POST['c']
            e=request.POST['e']
            d=request.FILES['d']
            fs=FileSystemStorage()
            fn=fs.save(d.name,d)
            q=product.objects.filter(product=a,seller_id=sid)
            if q:
                return HttpResponse("<script>alert('This Product is Already added ');window.location='/seller_edit_product'</script>")
            else:
                q=product(product=a,amt=b,quantity=c,image=fn,description=e,pstatus='active',seller_id=sid,subcategory_id=scid)
                q.save()
                return HttpResponse("<script>alert('added successfuly');window.location='/seller_edit_product'</script>")
        cat=category.objects.filter(castatus='active')
        # result=[]
        # ss=fname
        
        subcats=subcategory.objects.all()
    else:
        return redirect('/')
        
    return render(request,'seller_manage_product.html',{'q':q,'cat':cat,'subcats':subcats,'firstname':firstname})



def delete_product(request,id):
    q=product.objects.get(id=id)
    q.delete()
    return HttpResponse("<script>alert('deleted successfuly');window.location='/seller_edit_product'</script>")

def seller_edit_product(request):
    if 'login_id' in request.session:
        lid=request.session['login_id']
        sids=sellerr.objects.filter(login=lid)
        sid=sids[0].id
        firstname=sids[0].firstname
        q=product.objects.filter(seller_id=sid)

        if request.method=="POST":
            s=request.POST['s']
            q=product.objects.filter(seller_id=sid)
            if q:
                q=product.objects.filter(product=s,seller_id=sid)|product.objects.filter(amt=s,seller_id=sid)|product.objects.filter(quantity=s,seller_id=sid)|product.objects.filter(description=s,seller_id=sid)
            else:
                return HttpResponse("<script>alert('no results found');window.location='/seller_edit_product'</script>")
    else:
        return redirect('/')


    
    return render(request,'seller_edit_product.html',{'q':q,'firstname':firstname})






def update_product(request,id):
    lid=request.session['login_id']
    seller_id=sellerr.objects.filter(login=lid)
    sid=seller_id[0].id
    firstname=seller_id[0].firstname

    q=product.objects.filter(seller_id=sid)

    up=product.objects.get(id=id)
    if request.method=="POST":
        a=request.POST['a']
        b=request.POST['b']
        c=request.POST['c']
        d=request.FILES['d']
        e=request.POST['e']
        fs=FileSystemStorage()
        fn=fs.save(d.name,d)
        up.product=a
        up.amt=b
        up.quantity=c
        up.image=fn
        up.description=e
        up.save()
        return HttpResponse("<script>alert(' updated successfully');window.location='/seller_edit_product'</script>")
    return render(request,'seller_edit_product.html',{'up':up,'q':q,'firstname':firstname})

def product_active(request,id):
    q=product.objects.get(id=id)
    q.pstatus='active'
    q.save()
    return HttpResponse("<script>alert('active successfuly');window.location='/seller_edit_product'</script>")

def product_deactive(request,id):
    q=product.objects.get(id=id)
    q.pstatus='deactive'
    q.save()
    return HttpResponse("<script>alert('deactive successfuly');window.location='/seller_edit_product'</script>")

# ===================================services============================================================================

def seller_manage_services(request):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        seller_id=sellerr.objects.filter(login=lid)
        sid=seller_id[0].id
        firstname=seller_id[0].firstname

        qry1=services.objects.filter(seller_id=sid)
        if request.method=="POST":
            sname=request.POST['s']
            qry1=services.objects.filter(seller_id=sid)
            if qry1:
                qry1=services.objects.filter(seller_id=sid,service=sname)|services.objects.filter(seller_id=sid,rate=sname)
            else:
                return HttpResponse("<script>alert('no results found');window.location='/seller_manage_services'</script>")
    else:
        return redirect('/')
    # if request.method=="POST":
    #     c=request.POST['cat']
    #     d=request.POST['det']
    #     q=services.objects.filter(service=c,seller_id=sid)
    #     if q:
    #         return HttpResponse("<script>alert('This Service is Already added ');window.location='/seller_manage_services'</script>")
    #     else:
    #         qry=services(service=c,rate=d,seller_id=sid)
    #         qry.save()
    #         return HttpResponse("<script>alert('added successfully');window.location='/seller_manage_services' ;</script>")
    return render(request,'seller_manage_services.html',{'qry1':qry1,'firstname':firstname})




def seller_edit_service(request):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        seller_id=sellerr.objects.filter(login=lid)
        sid=seller_id[0].id
        firstname=seller_id[0].firstname

        # qry1=services.objects.filter(seller_id=sid,service=sname)|services.objects.filter(seller_id=sid,rate=sname)
        qry1=services.objects.filter(seller_id=sid)

        if request.method=="POST":
            c=request.POST['cat']
            d=request.POST['det']
            de=request.POST['des']
            q=services.objects.filter(service=c,seller_id=sid)
            if q:
                return HttpResponse("<script>alert('This Service is Already added ');window.location='/seller_manage_services'</script>")
            else:
                qry=services(service=c,rate=d,des=de,seller_id=sid)
                qry.save()
                return HttpResponse("<script>alert('added successfully');window.location='/seller_manage_services' ;</script>")
    else:
        return redirect('/')
    
    return render(request,'seller_edit_service.html',{'qry1':qry1,'firstname':firstname})







def delete_services(request,id):
    qry=services.objects.get(id=id)
    qry.delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/seller_manage_services'</script>")



def update_services(request,id):
    lid=request.session['login_id']
    seller_id=sellerr.objects.filter(login=lid)
    sid=seller_id[0].id
    firstname=seller_id[0].firstname

    qry1=services.objects.filter(seller_id=sid)

    up=services.objects.get(id=id)
    if request.method=="POST":
        cat=request.POST['cat']
        d=request.POST['det']
        de=request.POST['des']

        up.service=cat
        up.rate=d
        up.des=de
        up.save()
        return HttpResponse("<script>alert('updated successfully');window.location='/seller_manage_services';</script>")
    return render(request,'seller_manage_services.html',{'up':up,'qry1':qry1,'firstname':firstname})




# ===================================services============================================================================








def seller_manage_category(request):
    if 'login_id' in request.session:

    # lid=request.session['login_id']
    # seller_id=sellerr.objects.filter(login=lid)
    # uid=seller_id[0].id
        qry1=category.objects.all()

        if request.method=="POST":
            c=request.POST['cat']
            q=category.objects.filter(category=c)
            if q:
                return HttpResponse("<script>alert('This category is Already added ');window.location='/seller_manage_category'</script>")
            else:
                qry=category(category=c,castatus='active')
                qry.save()
                return HttpResponse("<script>alert('added successfully');window.location='/seller_manage_category' ;</script>")
    else:
        return redirect('/')
    return render(request,'seller_manage_category.html',{'qry1':qry1})

def delete_category(request,id):
    qry=category.objects.get(id=id)
    qry.delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/seller_manage_category'</script>")



def update_category(request,id):
    # lid=request.session['login_id']
    # seller_id=sellerr.objects.filter(login=lid)
    # sid=seller_id[0].id
    qry1=category.objects.all()
    up=category.objects.get(id=id)
    if request.method=="POST":
        cat=request.POST['cat']
        up.category=cat
        up.save()
        return HttpResponse("<script>alert('updated successfully');window.location='/seller_manage_category';</script>")
    return render(request,'seller_manage_category.html',{'up':up,'qry1':qry1})


def category_active(request,id):
    q=category.objects.get(id=id)
    q.castatus='active'
    q.save()
    return HttpResponse("<script>alert('active successfuly');window.location='/seller_manage_category'</script>")

def category_deactive(request,id):
    q=category.objects.get(id=id)
    q.castatus='deactive'
    q.save()
    return HttpResponse("<script>alert('deactive successfuly');window.location='/seller_manage_category'</script>")


def seller_manage_subcategory(request,id):
    if 'login_id' in request.session:

    # lid=request.session['login_id']
    # seller_id=sellerr.objects.filter(login=lid)
    # uid=seller_id[0].id
        qry1=subcategory.objects.filter(category_id=id)

        if request.method=="POST":
            c=request.POST['cat']
            q=subcategory.objects.filter(subcategory=c)
            if q:
                return HttpResponse("<script>alert('already added ');window.location='/seller_manage_subcategory/%s' ;</script>" % id)
            else:
                qry=subcategory(subcategory=c,category_id=id,cstatus='active')
                qry.save()
                return HttpResponse("<script>alert('added successfully');window.location='/seller_manage_subcategory/%s' ;</script>" % id)
    else:
        return redirect('/')
    return render(request,'seller_manage_subcategory.html',{'qry1':qry1})

def delete_subcategory(request,category_id,id):
    qry=subcategory.objects.get(id=id)
    qry.delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/seller_manage_subcategory/%s'</script>" % category_id)



def update_subcategory(request,category_id,id):
    # lid=request.session['login_id']
    # seller_id=sellerr.objects.filter(login=lid)
    # sid=seller_id[0].id
    qry1=subcategory.objects.filter(category_id=category_id)

    up=subcategory.objects.get(id=id)
    if request.method=="POST":
        cat=request.POST['cat']
        up.subcategory=cat
        up.save()
        return HttpResponse("<script>alert('updated successfully');window.location='/seller_manage_subcategory/%s';</script>" % category_id)
    return render(request,'seller_manage_subcategory.html',{'up':up,'qry1':qry1})

def subcategory_active(request,id,category_id):
    print("Haiiiiiiiiissss")
    q=subcategory.objects.get(id=id,category_id=category_id)
    q.cstatus='active'
    q.save()
    return HttpResponse("<script>alert('active successfully');window.location='/seller_manage_subcategory/%s'</script>" % category_id)

def subcategory_deactive(request,id,category_id):
    print("Haiiiiiiiiiiiiiiiiiii")
    q=subcategory.objects.get(id=id,category_id=category_id)
    q.cstatus='deactive'
    q.save()
    return HttpResponse("<script>alert('deactive successfully');window.location='/seller_manage_subcategory/%s'</script>" % category_id)


def seller_view_product_booking(request):
    if 'login_id' in request.session:
        lid=request.session['login_id']
        seller_id=sellerr.objects.get(login=lid)
        if seller_id:
            sid=seller_id.id

            firstname=seller_id.firstname

        q=booking.objects.filter(seller_id=sid)
        print(q)
    else:
        return redirect('/')
    return render(request,'seller_view_product_booking.html',{'q':q,'firstname':firstname})

def seller_view_booking_details(request,id):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        seller_id=sellerr.objects.filter(login=lid)
        firstname=seller_id[0].firstname

        q=bchild.objects.filter(booking_id=id)
        print(q)
    else:
        return redirect('/')
    return render(request,'seller_view_booking_details.html',{'q':q,'firstname':firstname})




def seller_view_feedback(request,product_id):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        seller_id=sellerr.objects.filter(login=lid)
        firstname=seller_id[0].firstname
        
        cus=feedbacks.objects.filter(product_id=product_id)
        ss={}
  
        ss['firstname']=firstname
        ss['cus']=cus
    else:
        return redirect('/')
    return render(request,'seller_view_feedback.html',ss)


def seller_view_ratings(request,product_id):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        seller_id=sellerr.objects.filter(login=lid)
        firstname=seller_id[0].firstname
        
        cus=review.objects.filter(product_id=product_id)
        ss={}
  
        ss['firstname']=firstname
        ss['cus']=cus
    else:
        return redirect('/')
    return render(request,'seller_view_ratings.html',ss)

# +++++++++++++++++++++service+++++++++++++++++++++++++++++++++++++++




def seller_view_service_feedback(request,service_id):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        seller_id=sellerr.objects.filter(login=lid)
        firstname=seller_id[0].firstname
        
        cus=sfeedback.objects.filter(service_id=service_id)
        ss={}
  
        ss['firstname']=firstname
        ss['cus']=cus
    else:
        return redirect('/')
    return render(request,'seller_view_service_feedback.html',ss)


def seller_view_service_rating(request,service_id):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        seller_id=sellerr.objects.filter(login=lid)
        firstname=seller_id[0].firstname
        
        cus=sreview.objects.filter(service_id=service_id)
        ss={}
  
        ss['firstname']=firstname
        ss['cus']=cus
    else:
        return redirect('/')
    return render(request,'seller_view_service_rating.html',ss)






def seller_view_payment(request,id):
    q=payment.objects.filter(booking__customerr__booking=id)
    print(q)
    return render(request,'seller_view_payment.html',{'q':q})




def seller_assigned_staff_book(request,id):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        seller_id=sellerr.objects.filter(login=lid)
        sid=seller_id[0].id

        firstname=seller_id[0].firstname
        import datetime
        qry1=staff.objects.filter(seller_id=sid)
        cdate=datetime.datetime.now().strftime ("%Y-%m-%d")

        if request.method=="POST":
            c=request.POST['cat']
            qry=assign_staff_book(date=cdate,status='assigned',booking_id=id,staff_id=c)
            qry.save()
            q=booking.objects.get(id=id)
            q.status='assigned staff'
            q.save()
            return HttpResponse("<script>alert('Assigned successfully');window.location='/seller_view_product_booking' ;</script>")
    else:
        return redirect('/')
    return render(request,'seller_assigned_staff_book.html',{'qry1':qry1,'firstname':firstname})




def seller_view_services(request):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        seller_id=sellerr.objects.filter(login=lid)
        sid=seller_id[0].id

        firstname=seller_id[0].firstname

        q=services.objects.filter(seller_id=sid)
        print(q)
    else:
        return redirect('/')
    return render(request,'seller_view_services.html',{'q':q,'firstname':firstname})

def seller_view_srequest(request,id):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        seller_id=sellerr.objects.filter(login=lid)
        sid=seller_id[0].id

        firstname=seller_id[0].firstname
        q=srequest.objects.filter(service_id=id)
        print(q)
    else:
        return redirect('/')
    return render(request,'seller_view_srequest.html',{'q':q,'firstname':firstname})






def seller_accept_req(request,id,service_id,email):
    q=srequest.objects.get(id=id)
    subject = 'SERVICE REQUEST '
    message = f"Sir/Madam,\n Your Booking Accepted Successfully  \n Thank you for connecting with us"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email,]
    send_mail( subject, message, email_from, recipient_list )
    q.status='accept'
    q.save()
    return HttpResponse("<script>alert('accepted successfuly');window.location='/seller_view_srequest/%s'</script>" %service_id)

def seller_reject_req(request,id,service_id,email):
    q=srequest.objects.get(id=id)
    subject = 'SERVICE REQUEST '
    message = f"Sir/Madam,\n Your Booking Rejected Successfully  \n Thank you for connecting with us"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email,]
    send_mail( subject, message, email_from, recipient_list )
    q.status='reject'
    q.save()
    return HttpResponse("<script>alert('rejected successfuly');window.location='/seller_view_srequest/%s'</script>" %service_id)





def seller_assigned_staff(request,id,email):
    if 'login_id' in request.session:

        import datetime
        qry1=staff.objects.all()
        cdate=datetime.datetime.now().strftime ("%Y-%m-%d")

        if request.method=="POST":
            c=request.POST['cat']
            qry=assign_staff_req(date=cdate,status='assigned',srequest_id=id,staff_id=c)
            qry.save()
            q=srequest.objects.get(id=id)
            q.status='assigned staff'
            subject = 'Assign staff Successfully'
            message = f"Sir/Madam,\n Assigned staff Successfully"
            
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
            q.save()
            return HttpResponse("<script>alert('added successfully');window.location='/seller_view_srequest/%s' ;</script>" % id)
    else:
        return redirect('/')
    return render(request,'seller_assigned_staff.html',{'qry1':qry1})



# ---------------------------------------------------SELLER---------------------------------------------------------------------
# ---------------------------------------------------customer---------------------------------------------------------------------
from django.db.models import Count

def customer_home(request):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        ss={}
        categoryss,fname=findcategoryss(lid)
        print(categoryss)

        ss['cat']=categoryss
        ss['fname']=fname
        q=services.objects.all()
        q1=product.objects.filter(pstatus='active')
        # q11=product.objects.all()
        q11=product.objects.all().order_by('-id')[:4]
        print('new arrivals',q11)


        # b1=bchild.objects.all()

        b1=bchild.objects.all().annotate(count=Count('product_id')).filter(product_id__gt=2)
        print(b1)
        # if b1:
        #     img=b1[0].product.image 
        #     print(img,"********")

        # ss['cat']=categoryss
        ss['q']=q
        ss['q1']=q1
        ss['b1']=b1
        ss['q11']=q11
    else:
        return redirect('/')
    return render(request,'customer_home.html',ss)


def customer_update_profile(request):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        sid=customerr.objects.filter(login=lid)
        if sid:
            cid=sid[0].id
            fname=sid[0].fname

        print(cid)

        up=customerr.objects.get(id=cid)

        if request.method=="POST":
            fn=request.POST['a']
            ln=request.POST['b']
            place=request.POST['c']
            phone=request.POST['d']
            email=request.POST['e']
            addr=request.POST['address']
            up.fname=fn
            up.lname=ln
            up.place=place
            up.phone=phone
            up.email=email
            up.address=addr
            up.save()
            return HttpResponse("<script>alert('profile updated successfully');window.location='/customer_update_profile'</script>")
        ss={}
        categoryss,fname=findcategoryss(lid)
        ss['cat']=categoryss
        ss['fname']=fname
        ss['up']=up
    else:
        return redirect('/')    
    return render(request,'customer_update_profile.html',ss)


def customer_change_password(request):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        q=loginn.objects.filter(id=lid)
        username=q[0].username
        sid=customerr.objects.filter(login=lid)
        if sid:
            fname=sid[0].fname

        print(username)

        if request.method=="POST":
            np=request.POST['password']
            cp=request.POST['confirm_password']
            confirm_encryptedpassword=make_password(cp)
            print(confirm_encryptedpassword)
            q=loginn.objects.get(id=lid)       
            q.password=confirm_encryptedpassword
            q.save()
            return HttpResponse("<script>alert('password changed successfully');window.location='/login'</script>")
        ss={}
        categoryss,fname=findcategoryss(lid)
        ss['cat']=categoryss
        ss['fname']=fname
        ss['username']=username
    else:
        return redirect('/')
    return render(request,'customer_change_password.html',ss)




def fetch_search(request):
    if request.method=="POST":
        data=json.loads(request.body)
        key=data.get('key')
        print("***",key)
        cid=data.get('id')
        print("******",cid)
        if int(cid) > 0:
            if key==" ":
                q=product.objects.filter(subcategory_id=cid)
                #q=product.objects.filter(pstatus='active')
            else:
                q=product.objects.filter(product__icontains=key,subcategory_id=cid)
                #q=product.objects.filter(product_name_icontains=key,pstatus='active')|product.objects.filter(sellerdistrict=key,pstatus='active')|product.objects.filter(seller_city=key,pstatus='active')
            print(q,"__")
        else:
            q=product.objects.filter(product__icontains=key)
        if q:
            final = [{"product":obj.product,"id":obj.id,"image":obj.image,"amt":obj.amt,"quantity":obj.quantity,"desc":obj.description,"seller_id":obj.seller_id} for obj in q]
        else:
            final = [{"name":"novalue"} for obj in q]
            
        0

    return JsonResponse({'status': 'success','data':final})



def customer_view_product(request,id):
    if 'login_id' in request.session:

        print(type(id))
        lid=request.session['login_id']
        # sid=customerr.objects.filter(login=lid)
        # if sid:
        #     cid=sid[0].id
        #     fname=sid[0].fname
        #     print(cid)
        if id=="0":
            q=product.objects.all()
        else:
            q=product.objects.filter(subcategory_id=id)
        if request.method=="POST":
            sname=request.POST['sname']
            # print(q)
        
            if int(id)==0:
                print("haiiiiii")
                q=product.objects.filter(product=sname)|product.objects.filter(amt=sname)|product.objects.filter(seller__firstname=sname)
            else:
                q=product.objects.filter(subcategory_id=id,product=sname)|product.objects.filter(subcategory_id=id,amt=sname)|product.objects.filter(seller__firstname=sname,subcategory_id=id,product=sname)
                print(q)

        if 'filter' in request.POST:
            amount=request.POST['amount']
            print("////////////////",amount)
            amts=int(amount)
            if int(id)==0:
                q = product.objects.filter(amt__lte=amts)
                
                print("////////////////",q)

            else:
                q = product.objects.filter(subcategory_id=id,amt__lte=amts)
        ss={}
        categoryss,fname=findcategoryss(lid)
        ss['cat']=categoryss
        ss['fname']=fname
        # ss['cus']=cus
        ss['q']=q
        ss['id']=id
        # print(ss)
    else:
        return redirect('/')
    return render(request,'customer_view_product.html',ss)


def customer_add_wlist(request,id):

    if 'login_id' in request.session:

        lid=request.session['login_id']
        sid=customerr.objects.filter(login=lid)
        if sid:
            cid=sid[0].id
        #     fname=sid[0].fname
        #     print(cid)
        q=wishlist.objects.filter(product_id=id,customerr_id=cid)
        if q:
            # return HttpResponse("<script>alert('Product already added to wishlist');window.location='/customer_view_product/%s'</script>" %id)
            return HttpResponse("<script>alert('Product already added to wishlist');window.location='/customer_view_wlist'</script>" )
        else:
            q=wishlist(product_id=id,customerr_id=cid)
            q.save()
            return HttpResponse("<script>alert('Product added to wishlist');window.location='/customer_view_wlist'</script>" )

    else:
        return redirect('/')

  
def customer_remove_wlist(request,id):
    q=wishlist.objects.filter(id=id)
    q.delete()
    return HttpResponse("<script>alert('Product removed to wishlist');window.location='/customer_view_wlist'</script>" )




def customer_view_wlist(request):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        sid=customerr.objects.filter(login=lid)
        if sid:
            cid=sid[0].id
        #     fname=sid[0].fname
        #     print(cid)
        q=wishlist.objects.filter(customerr_id=cid)
        # if request.method=="POST":
        #     sname=request.POST['sname']
        #     # print(q)
        
        #     if int(id)==0:
        #         print("haiiiiii")
        #         q=product.objects.filter(product=sname)
        #     else:
        #         q=product.objects.filter(subcategory_id=id)
        #         print(q)
        ss={}
        categoryss,fname=findcategoryss(lid)
        ss['cat']=categoryss
        ss['fname']=fname
        # ss['cus']=cus
        ss['q']=q
        # print(ss)
    else:
        return redirect('/')
    return render(request,'customer_view_wlist.html',ss)





def customer_add_cart(request,id,seller_id,product,amt,image,description):
    if 'login_id' in request.session:

        import datetime
        lid=request.session['login_id']
        sid=customerr.objects.filter(login=lid)
        if sid:

            cid=sid[0].id
            fname=sid[0].fname
            print(cid)
        if request.method=="POST":
            tot=request.POST['to']
            rate=request.POST['rate']
            qty=request.POST['qty']
            cdate=datetime.datetime.now().strftime ("%Y-%m-%d")
            q=booking.objects.filter(status='pending',customerr_id=cid,seller_id=seller_id)        
            if q:
                bk_id=q[0].id
                total=q[0].total.split(".")
                print('........',bk_id)
                qqq=bchild.objects.filter(product_id=id,booking_id=bk_id)
                if qqq:
                    bc_id=qqq[0].id
                    bc_qty=qqq[0].qty
                    bc_amt=qqq[0].bamt
                    qq=bchild.objects.get(id=bc_id)
                    qq.qty=int(qty)+int(bc_qty)
                    qq.bamt=int(bc_amt)+int(tot)
                    qq.save()
                    q2=booking.objects.get(id=bk_id)
                    q2.total=int(total[0])+int(tot)
                    q2.save()
                    # return HttpResponse("<script>alert('Product added to cart');window.location='/customer_view_product/%s'</script>" %id)
                    return HttpResponse("<script>alert('Product added to cart');window.location='/customer_my_cart'</script>")

                else:
                    rates=int(qty)*int(rate)
                    qq=bchild(qty=qty,bamt=tot,booking_id=bk_id,product_id=id)
                    qq.save()
                    q1=booking.objects.get(id=bk_id)
                    q1.total=int(total[0])+int(tot)
                    q1.save()
                    # return HttpResponse("<script>alert('Product added to cart');window.location='/customer_view_product/%s'</script>" %id)
                    return HttpResponse("<script>alert('Product added to cart');window.location='/customer_my_cart'</script>")

            else:
                rates=int(qty)*int(rate)
                q=booking(total=tot,date=cdate,status='pending',seller_id=seller_id,customerr_id=cid)
                q.save()
                q1=bchild(qty=qty,bamt=tot,booking=q,product_id=id)
                q1.save()
                # return HttpResponse("<script>alert('Product added to cart ');window.location='/customer_view_product/%s'</script>" %id)
                return HttpResponse("<script>alert('Product added to cart');window.location='/customer_my_cart'</script>")



        ss={}
        categoryss,fname=findcategoryss(lid)
        ss['cat']=categoryss
        ss['fname']=fname
        ss['product']=product
        ss['amt']=amt
        ss['image']=image
        ss['description']=description
    else:
        return redirect('/')
    return render(request,'customer_add_cart.html',ss)


def customer_my_cart(request):

    lid=request.session['login_id']
    sid=customerr.objects.filter(login=lid)
    cid=sid[0].id

    # q = bchild.objects.select_related('booking').filter(booking__status='pending',booking__customerr_id=cid)
    # # q=   bchild.objects.select_related('booking').all()
    # print('inner join',q)
    # if q:
    #     bk_total=q[0].booking__total
    #     print('----------total in bmaster-----------',bk_total)

    q=booking.objects.filter(status='pending',customerr_id=cid)
    print(q)
    if q:
       bk_id=q[0].id 
       bk_total=q[0].total
       bk_status=q[0].status
       print(bk_total)
       q=bchild.objects.filter(booking_id=bk_id)
       if q:
        bc_id=q[0].id

        pid=q[0].product_id
        print('------bc_ids----------',bc_id)
        print('------p_ids----------',pid)
        j=1
        for i in q:
            
            # present_total=bk_total

            # print("----",request.form)
            if request.method=="POST":
                # form = customer_my_cart(request.POST)
                if request.POST.get("update_cart"+str(j)):
                    print("sssssssss"+str(j))
                    qtys=request.POST['qtys'+str(j)]
                    bcid=request.POST['bcid'+str(j)]
                    amtss=request.POST['amtss'+str(j)]
                    print('/////////',qtys) 
                    print('/////////',bcid) 
                    print('/////////',amtss)  
                    # bqty=int(qty)+int(qtys)
                    # print('+++++++++++++',bqty)
                    q1=bchild.objects.get(id=bcid)
                    print("---------q1------------",q1)
                    q1.qty=qtys
                    total=int(qtys)*int(amtss) 
                    print(total)
                    # q1.bamt=0
                    q1.bamt=total
                    q1.save()
                    
                    qq=bchild.objects.filter(booking_id=q1.booking_id).aggregate(Sum('bamt'))
                    print("------qq---------",qq['bamt__sum'])
                    q3=booking.objects.get(id=q1.booking_id)
                    print(q3)
                    q3.total=qq['bamt__sum']
                    q3.save()
                    return HttpResponse("<script>window.location='/customer_my_cart'</script>")
                else:
                    print("Haiiissssssssssssss"+str(j))
                # 
                j=j+1
    else:       
        return HttpResponse("<script>alert('empty cart');window.location='/customer_home'</script>")
    ss={}
    categoryss,fname=findcategoryss(lid)
    ss['cat']=categoryss
    ss['fname']=fname
    ss['q']=q
    # ss['present_total']=present_total
    ss['bk_total']=bk_total
    ss['bk_status']=bk_status
    ss['bk_id']=bk_id
    return render(request,'customer_my_cart.html',ss)



def customer_remove_cart(request,id):
    q=bchild.objects.get(id=id)
    if q:
        qq=booking.objects.get(id=q.booking_id)
        if qq:
            print(type(qq.total))
            print(q.bamt)
            ss=qq.total.split('.')
            total=int(ss[0])-int(q.bamt)
            qq.total=total
            print('//////////',total)
            qq.save()
            q.delete()
            if qq.total==0:
                qw=booking.objects.get(id=q.booking_id)
                qw.delete()
    return HttpResponse("<script>alert('Removed');window.location='/customer_my_cart'</script>")





def customer_view_booking(request):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        q=customerr.objects.filter(login=lid)
        if q:
            cid=q[0].id
            fname=q[0].fname
            q=booking.objects.filter(customerr_id=cid)
            print(q)
        ss={}
        categoryss,fname=findcategoryss(lid)
        ss['cat']=categoryss
        ss['fname']=fname
        ss['q']=q
    else:
        return redirect('/')
    return render(request,'customer_view_booking.html',ss)

def customer_view_booking_details(request,id):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        cid=customerr.objects.filter(login=lid)
        fname=cid[0].fname  
        q=bchild.objects.filter(booking_id=id)
        print(q)
        ss={}
        categoryss,fname=findcategoryss(lid)
        ss['cat']=categoryss
        ss['fname']=fname
        ss['q']=q
    else:
        return redirect('/')
    return render(request,'customer_view_booking_details.html',ss)






def customer_view_assigned_staff(request,id):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        cid=customerr.objects.filter(login=lid)
        if cid:
            fname=cid[0].fname
        q=assign_staff_book.objects.filter(booking_id=id)

        ss={}
        categoryss,fname=findcategoryss(lid)
        ss['cat']=categoryss
        ss['fname']=fname
        ss['q']=q
    else:
        return redirect('/')


    return render(request,'customer_view_assigned_staff.html',ss)




def customer_view_service(request):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        cid=customerr.objects.filter(login=lid)
        if cid:
            fname=cid[0].fname
        q=services.objects.all()
        ss={}
        categoryss,fname=findcategoryss(lid)
        ss['cat']=categoryss
        ss['fname']=fname
        ss['q']=q   
    else:
        return redirect('/')
    return render(request,'customer_view_service.html',ss)



def cus_view_sdetals(request,id):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        cid=customerr.objects.filter(login=lid)
        if cid:
            fname=cid[0].fname
        q=services.objects.filter(id=id)
        ss={}
        categoryss,fname=findcategoryss(lid)
        ss['cat']=categoryss
        ss['fname']=fname
        ss['q']=q   
    else:
        return redirect('/')
    return render(request,'cus_view_sdetals.html',ss)



def customer_send_service_request(request,id,rate):

    import datetime
    cdate=datetime.datetime.now().strftime ("%Y-%m-%d")
    lid=request.session['login_id']
    cid=customerr.objects.filter(login=lid)
    cid=cid[0].id
    qq=srequest.objects.filter(status='pending',service_id=id)
    if qq:
        return HttpResponse("<script>alert('already requested ');window.location='/customer_view_service'</script>")
    else:
        q1=srequest(amount=rate,date=cdate,status='pending',customer_id=cid,service_id=id)
        q1.save()
        return HttpResponse("<script>alert(' request send successfully ');window.location='/customer_view_service'</script>")



def customer_view_service_request(request):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        q=customerr.objects.filter(login=lid)
        if q:
            cid=q[0].id
            fname=q[0].fname
            q=srequest.objects.filter(customer_id=cid)


        ss={}
        categoryss,fname=findcategoryss(lid)
        ss['cat']=categoryss
        ss['fname']=fname
        ss['q']=q
    else:
        return redirect('/')
    return render(request,'customer_view_service_request.html',ss)



# ============================================HISTROY============================================================
def cus_service_histroy(request):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        q=customerr.objects.filter(login=lid)
        if q:
            cid=q[0].id
            fname=q[0].fname
            q=srequest.objects.filter(customer_id=cid)


        ss={}
        categoryss,fname=findcategoryss(lid)
        ss['cat']=categoryss
        ss['fname']=fname
        ss['q']=q
    else:
        return redirect('/')
    return render(request,'cus_service_histroy.html',ss)

def cus_order_histroy(request):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        cid=customerr.objects.get(login=lid)
        if cid:
            fname=cid.fname
            cids=cid.id
            print("pppppppppppppp",cids)  
            q=bchild.objects.filter(booking__customerr_id=cids).exclude(booking__status='pending')
            # q=bchild.objects.filter(booking__customerr_id=cids)
            print(q)
        ss={}
        categoryss,fname=findcategoryss(lid)
        ss['cat']=categoryss
        ss['fname']=fname
        ss['q']=q
    else:
        return redirect('/')
    return render(request,'cus_order_histroy.html',ss)
# ============================================HISTROY============================================================

def customer_make_payment_srequest(request,id,amount):
    lid=request.session['login_id']
    cid=customerr.objects.filter(login=lid)
    if cid:
        fname=cid[0].fname


    ss={}
    categoryss,fname=findcategoryss(lid)
    ss['cat']=categoryss
    ss['fname']=fname
    ss['amount']=amount


    import datetime
    if request.method=="POST":
        
        cdate=datetime.datetime.now().strftime ("%Y-%m-%d")
        # q=req_payment(amount=amount,date=cdate,srequest_id=id)
        # q.save()
        

        # amt=amt
        # today=datetime.date.today()
        # print(">>>>>>>>>>>>>>>>",amount)

        # q=payment(amount=amt,date=today,appoinment_id=id)
        # q.save()
        # up=appoinment.objects.get(id=id)
        # up.status='Paid'
        # up.save()
        amount = amount
        currency="INR"

            # Create Razorpay client object

        razorpay_client = Client(auth=("rzp_test_myOF7jDpkIqeD0", "lGAkCY9inaIl4fS1apPqP7Gi"))

            # Create a payment
        order = razorpay_client.order.create({
            "amount": amount,
            "currency": currency,
            'receipt': 'receipt_id'
        })

        # Get the order ID
        order_id = order['id']
        print(order_id)
        print("AHiiiiiiii")
        q1=srequest.objects.get(id=id)
        q1.status='paid'
        q1.order_id=order_id
        q1.save()
       
        return HttpResponse("<script>alert('Paid Successfully....!!');window.location='/patient_home'</script>")
        return HttpResponse("<script>alert('paid successfully');window.location='/customer_view_service_request'</script>")
    return render(request,'customer_make_payment_srequest.html',ss)




def customer_view_assigned_staff_request(request,id):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        cid=customerr.objects.filter(login=lid)
        if cid:
            fname=cid[0].fname
        q=assign_staff_req.objects.filter(srequest_id=id)

        ss={}
        categoryss,fname=findcategoryss(lid)
        ss['cat']=categoryss
        ss['fname']=fname
        ss['q']=q
    else:
        return redirect('/')
    return render(request,'customer_view_assigned_staff_request.html',ss)





def customer_send_feedback(request,booking_id,product_id):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        cid=customerr.objects.filter(login=lid)
        if cid:
            cus_id=cid[0].id

            fname=cid[0].fname
        qq=feedbacks.objects.filter(customer_id=cus_id,product_id=product_id)

        ss={}
        categoryss,fname=findcategoryss(lid)
        ss['cat']=categoryss
        ss['fname']=fname
        ss['qq']=qq
        import datetime
        cdate=datetime.datetime.now().strftime ("%Y-%m-%d")

        if request.method=="POST":
            feedbackss=request.POST['feedback']
            q=feedbacks(product_id=product_id,customer_id=cus_id,date=cdate,feedback=feedbackss)
            q.save()
        
            return HttpResponse("<script>alert('send successfully');window.location='/customer_view_booking_details/%s'</script> " %booking_id )
    else:
        return redirect('/')
    
    return render(request,'customer_send_feedback.html',ss)



def customer_send_service_feedback(request,service_id):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        cid=customerr.objects.filter(login=lid)
        if cid:
            cus_id=cid[0].id

            fname=cid[0].fname
        qq=sfeedback.objects.filter(customer_id=cus_id,service_id=service_id)

        ss={}
        categoryss,fname=findcategoryss(lid)
        ss['cat']=categoryss
        ss['fname']=fname
        ss['qq']=qq
        import datetime
        cdate=datetime.datetime.now().strftime ("%Y-%m-%d")

        if request.method=="POST":
            feedbackss=request.POST['feedback']
            q=sfeedback(service_id=service_id,customer_id=cus_id,date=cdate,feedback=feedbackss)
            q.save()
        
            return HttpResponse("<script>alert('send successfully');window.location='/customer_send_service_feedback/%s'</script> " %service_id )
    else:
        return redirect('/')
    
    return render(request,'customer_send_service_feedback.html',ss)



# ---------------------------------------------------customer---------------------------------------------------------------------
# ---------------------------------------------------staff---------------------------------------------------------------------
def staff_home(request):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        sid=staff.objects.filter(login=lid)
        if sid:
            # cid=sid[0].id
            fn=sid[0].fn
    else:
        return redirect('/')
    return render(request,'staff_home.html',{'fn':fn})

def staff_update_profile(request):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        sid=staff.objects.filter(login=lid)
        cid=sid[0].id
        fn=sid[0].fn
        print(cid)

        up=staff.objects.get(id=cid)
        if request.method=="POST":
            fn=request.POST['a']
            ln=request.POST['b']
            place=request.POST['c']
            phone=request.POST['d']
            email=request.POST['e']
            up.fname=fn
            up.lname=ln
            up.place=place
            up.phone=phone
            up.email=email
            up.save()
            return HttpResponse("<script>alert('profile updated successfully');window.location='/staff_update_profile'</script>")
    else:
        return redirect('/')
    
    return render(request,'staff_update_profile.html',{'up':up,'fn':fn})


def staff_change_password(request):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        q=loginn.objects.filter(id=lid)
        username=q[0].username
        cid=staff.objects.filter(login=lid)
        fn=cid[0].fn
        print(username)

        if request.method=="POST":
            np=request.POST['password']
            cp=request.POST['confirm_password']
            confirm_encryptedpassword=make_password(cp)
            print(confirm_encryptedpassword)
            q=loginn.objects.get(id=lid)       
            q.password=confirm_encryptedpassword
            q.save()
            return HttpResponse("<script>alert('password changed successfully');window.location='/login'</script>")
    else:
        return redirect('/')
    return render(request,'staff_change_password.html',{'username':username,'fn':fn})



def staff_view_booking(request):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        q=staff.objects.filter(login=lid)
        if q:
            cid=q[0].id
            fn=q[0].fn
            print(cid)
        q=booking.objects.filter(assign_staff_book__staff=cid)
        print(q)
    else:
        return redirect('/')
    return render(request,'staff_view_booking.html',{'q':q,'fn':fn})

def staff_view_bk_details(request,id):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        cid=staff.objects.filter(login=lid)
        fn=cid[0].fn
        q=bchild.objects.filter(booking_id=id)
        print(q)
    else:
        return redirect('/')
    return render(request,'staff_view_bk_details.html',{'q':q,'fn':fn})



def staff_deliver(request,id,email):
    q=booking.objects.get(id=id)
    subject = 'ORDER STATUS'
    message = f"Sir/Madam,\n Your Order Delivered Successfully  \n Thank you for connecting with us"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email,]
    send_mail( subject, message, email_from, recipient_list )
    q.status='delivered'
    q.save()
    return HttpResponse("<script>alert('deliver successfuly');window.location='/staff_view_booking'</script>")


def staff_view_service_req(request):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        q=staff.objects.filter(login=lid)
        print(q,"......................")
        if q:
            cid=q[0].id
            fn=q[0].fn
        q=srequest.objects.filter(assign_staff_req__staff=cid)
    else:
        return redirect('/')
    return render(request,'staff_view_service_req.html',{'q':q,'fn':fn})


def staff_update_status(request,id,email):
    q=srequest.objects.get(id=id)
    subject = 'SERVICE STATUS '
    message = f"Sir/Madam,\n Your Service Completed Successfully  \n Thank you for connecting with us"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email,]
    send_mail( subject, message, email_from, recipient_list )
    q.status='finished'
    q.save()
    return HttpResponse("<script>alert('finished successfuly');window.location='/staff_view_service_req'</script>")



# ==============================================templates===================================================================
import json
from django.http import JsonResponse

def select_change(request):
    if request.method=="POST":
        data=json.loads(request.body)
        id=data.get('selected')
        print("*******",id)

        q=subcategory.objects.filter(category_id=id) 
        print(q)
        # if q:
        #     place_id=q[0].place_id
        #     print('place',place_id) 
        #     p=organizer.objects.filter(place_id=place_id)
        #     # p=place.objects.filter(organizer__id=place_id)
        #     print('///////',p[0].name)

        print(q,"______")

        final = [{"name":obj.subcategory,"id":obj.id} for obj in q]

    return JsonResponse({'status': 'success','data':final})

def change_qty(request):
    outssss=""
    if request.method=="POST":
        data=json.loads(request.body)
        qty=data.get('qty') 
        bcid=data.get('bcid')
        amt=data.get('amt')
        print("*******",qty,"///////////",bcid,"/////////////",amt)
        p = bchild.objects.filter(id=bcid)
        if p:
            pid=p[0].product_id
            qw = product.objects.filter(id=pid)
            if qw:
                stock = qw[0].quantity
                print("((((((((()))))))))",stock,"........",qty)
                if int(qty) > int(stock):
                    print("helloda/")
                    outssss="Quantity Reached"
                    # return HttpResponse("<script>alert('Quantity Reached')</script>")
                else:

                    w=bchild.objects.get(id=bcid)
                    w.qty=qty
                    w.bamt=int(qty)*int(amt)
                    w.save()
                    print(int(qty)*int(amt))

                    x=bchild.objects.filter(id=bcid)
                    if x:
                        bkid=x[0].booking_id

                    # newqry = booking.objects.filter(id=z)
                    # newqry.total=

                    query = bchild.objects.filter(id=bcid)

                    qq=bchild.objects.filter(booking_id=bkid).aggregate(Sum('bamt'))
                    print("------qq---------",qq['bamt__sum'])
                    q3=booking.objects.get(id=bkid)
                    print(q3)
                    q3.total=qq['bamt__sum']
                    q3.save()

        query1 = bchild.objects.filter(id=bcid) 
        # if query1:
        #     vvv=booking.objects.get(id=query1[0].booking_id) 
        #     print("/////////////",vvv)

        final = [{"amt":obj.bamt,"qty":obj.qty,"total":obj.booking.total} for obj in query1]
        print("hello...",final)

    return JsonResponse({'status': 'success','data':final,'outss':outssss})

# ==============================================templates===================================================================
def bill_generate(request,id):
    from datetime import datetime
    import random
    now = datetime.now()
    random_number = random.randint(1000,9999)
    q=bchild.objects.filter(booking_id=id)
    print(q)
    if q:
        qb=booking.objects.get(id=id)
        bstatus=qb.total

    lid=request.session['login_id']
    qq=customerr.objects.filter(login=lid)
    if qq:
        cid=qq[0].id
        # fname=q[0].fname
    # q=event_booking.objects.filter(cbooking__id=id,client_id=cid,status='paid')
    

    return render(request,'bill_generate.html',{'bstatus':bstatus,'q':q,'qq':qq,'current_date': now,'current_time': now,'random_number': random_number})



# ++++++++++++++++++++++++++service bill+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




def cusbk_generate_bill(request,id):
    from datetime import datetime
    import random
    now = datetime.now()
    random_number = random.randint(1000,9999)
    q=srequest.objects.filter(id=id)
    print(q)
    

    lid=request.session['login_id']
    qq=customerr.objects.filter(login=lid)
    if qq:
        cid=qq[0].id
        # fname=q[0].fname
    # q=event_booking.objects.filter(cbooking__id=id,client_id=cid,status='paid')
    

    return render(request,'cusbk_generate_bill.html',{'q':q,'qq':qq,'current_date': now,'current_time': now,'random_number': random_number})









def cus_view_feedback(request,id):
    if 'login_id' in request.session:

        lid=request.session['login_id']
        qq=customerr.objects.get(login=lid)
        if qq:
            cid=qq.id
            # b=bchild.objects.filter(product_id=id)
            # if b:
            #     bid=b[0].booking_id
        cus=feedbacks.objects.filter(customer_id=cid)
        print("kkkkkk",cus)
        ss={}
        categoryss,fname=findcategoryss(lid)
        ss['cat']=categoryss
        ss['fname']=fname
        ss['cus']=cus
    else:
        return redirect('/')
    return render(request,'cus_view_feedback.html',ss)




# ----------------------------------------razor-user-------------------------------------  
# 


def rpay(request):
    print("Haiiiiiiiii")
    
    

    # Get the order ID
    order_id = request.GET['order_id']
    order_id = request.GET['order_id']
    # print(order_id)
    s=booking.objects.get(id=id)
    if s:
        s.status='Shipped'
        # s.order_id=order_id
        s.save() 
    od=booking.objects.filter(booking_id=id)
    print(od)
    if od:
        for i in od:
            pid=i.product_id
            qtys=i.quantity
            print(pid,"....................proid")
            print(qtys,"..................qty")

            pp=product.objects.get(id=pid)
            # print(p,"!!!!!!!!!!!!!!!!!!!!!!!!")
            if pp:
                pro_qty=pp.stock
                print(pro_qty,"############pro_qty")
                pp.stock=int(pro_qty)-int(qtys)
                pp.save()
    return HttpResponse("<script>alert('Payment Completed....!!!');window.location='/customer_view_booking';</script>")
   
    return render(request, 'orders.html',context)


def user_payment_completes(request,id):
    lid=request.session['login_id']
    cid=customerr.objects.filter(login=lid)
    if cid:
        email=cid[0].email
        print(email)
    # # print(order_id)
    # s=booking.objects.get(id=id)
    # if s:
    #     s.status='paid'
    #     s.save() 

    q1=booking.objects.get(id=id)
    if q1:
        q1.status='paid'
        
        # q1.orderid=order_id
        q1.save()



    q2=bchild.objects.filter(booking_id=id)
    for i in q2:
            
            # bid=i.booking_id
            bqty=i.qty
            # print(';;;;;;;;;;;;;-------------------------;;;;;;;;',bid)
            print(';;;;;;;;;;;;;;;;;;;;;',bqty)
            product_id=i.product_id
            print('================',product_id)
            q3=product.objects.get(id=product_id)
            if q3:
                p_qty=q3.quantity
                q3.quantity=int(p_qty)-int(bqty)
                q3.save()
                
    subject = 'Order Placed'
    message = f"Sir/Madam,\n Your Payment Completed Successfully  \n Thank you for connecting with us"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email,]
    send_mail( subject, message, email_from, recipient_list )

    return HttpResponse("<script>alert('Payment Completed....!!!');window.location='/customer_view_booking';</script>")






def customer_make_payment(request,id,total):

    lid=request.session['login_id']
    cid=customerr.objects.filter(login=lid)
    if cid:
        fname=cid[0].fname
        email=cid[0].email
        print(email)
        
    # ss={}
 
    # ss['total']=total
    # ss['ids']=id

    return render(request,'customer_make_payment.html',{'total':total,'ids':id,'fname':fname})
#   # ----------------------------------------razor-user--------order-----------------------------    
#   # ----------------------------------------razor-user-booking-------------------------------------    


def user_payment_complete(request,id):
    lid=request.session['login_id']
    cid=customerr.objects.filter(login=lid)
    if cid:
        fname=cid[0].fname
        email=cid[0].email
        print(email)



    q1=srequest.objects.get(id=id)
    q1.status='paid'
    # q1.orderid=order_id
    subject = 'Service  Payment Status'
    message = f"Sir/Madam,\n Your Payment Completed Successfully  \n Thank you for connecting with us"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email,]
    send_mail( subject, message, email_from, recipient_list )
    q1.save()
    return HttpResponse("<script>alert('Payment Completed....!!!');window.location='/customer_view_service_request';</script>")


def customer_make_payment_srequest(request,id,total):
    from datetime import datetime,date
    today=date.today()
    print(today)
    lid=request.session['login_id']
    cid=customerr.objects.filter(login=lid)
    if cid:
        fname=cid[0].fname
    print(">>>>>>>>>>>>>>>>",total)


       
    ss={}
   
    ss['total']=total
    return render(request,'customer_make_payment_srequest.html',{'total':total,'ids':id,'fname':fname})





def customer_add_ratings(request,id):
    from datetime import date
    today=date.today()
    print(today)

    lid=request.session['login_id']

    c=customerr.objects.filter(login_id=lid)
    if c:
        cid=c[0].id 
        print(cid)


    if request.method=="POST":
        rate=request.POST['r']
        re=request.POST['review']
        q=review(rate=rate,reviews=re,date=today,customer_id=cid,product_id=id)
        q.save()
        return HttpResponse("<script>alert('Added....!!!');window.location='/customer_view_booking';</script>")
    
    qq=review.objects.filter(customer_id=cid,product_id=id)
    ss={}
    lid=request.session['login_id']
    categoryss,fname=findcategoryss(lid)
    ss['cat']=categoryss
    ss['fname']=fname
    ss['qq']=qq
    return render(request,'customer_add_ratings.html',ss)



def customer_add_service_rating(request,service_id):
    from datetime import date
    today=date.today()
    print(today)

    lid=request.session['login_id']

    c=customerr.objects.filter(login_id=lid)
    if c:
        cid=c[0].id 
        print(cid)


    if request.method=="POST":
        rate=request.POST['r']
        re=request.POST['review']
        q=sreview(rate=rate,reviews=re,date=today,customer_id=cid,service_id=service_id)
        q.save()
        return HttpResponse("<script>alert('Added....!!!');window.location='/customer_add_service_rating/%s';</script>" %service_id)
    
    qq=sreview.objects.filter(customer_id=cid,service_id=service_id)
    ss={}
    lid=request.session['login_id']
    categoryss,fname=findcategoryss(lid)
    ss['cat']=categoryss
    ss['fname']=fname
    ss['qq']=qq
    return render(request,'customer_add_service_rating.html',ss)