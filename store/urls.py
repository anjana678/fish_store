# """fish URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path,include
# from .import views
# urlpatterns = [
#     path('',views.index),
#     path('login',views.logins),
#     path('seller_register',views.seller_register),
#     path('customer_register',views.customer_register),
#     path('signup',views.signup),
#     # =====================ADMIN==============================================================================================
#     path('adminhome',views.adminhome),
#     path('admin_view_customer',views.admin_view_customer),
#     path('admin_view_bk/<id>',views.admin_view_bk),
#     path('admin_view_seller',views.admin_view_seller),
#     path('accept_seller/<id>',views.accept_seller),
#     path('reject_seller/<id>',views.reject_seller),
#     path('admin_view_services/<id>',views.admin_view_services),
#     path('admin_view_booking_details/<id>',views.admin_view_booking_details),
#     # =====================ADMIN===============================================================================================


# # -----------------------------------------SELLER-------------------------------------------------------------------------------------------------------
# path('seller_home',views.seller_home),



# # -----------------------------------------SELLER-------------------------------------------------------------------------------------------------------


# ]
"""fish URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index),
    # path('home',views.home),
    path('login',views.logins),
    path('seller_register',views.seller_register),
    path('customer_register',views.customer_register),
    path('signup',views.signup),
    path('forgot_password',views.forgot_password),
    path('set_password/<id>/<eid>',views.set_password),
    path('acceptseller_username/<id>',views.acceptseller_username),
    path('acceptcustomer_username/<id>',views.acceptcustomer_username),




    path('process_form/',views.process_form), 

        # =====================report==============================================================================================
    path('admin_sales_report',views.admin_sales_report), 


    # =====================ADMIN==============================================================================================
    path('adminhome',views.adminhome),
    path('admin_view_customer',views.admin_view_customer),
    path('accept_customer/<id>/<email>',views.accept_customer),
    path('reject_customer/<id>/<email>',views.reject_customer),
    path('admin_view_bk/<id>',views.admin_view_bk),
    path('admin_view_booking_details/<id>',views.admin_view_booking_details),
    path('admin_view_seller',views.admin_view_seller),
    path('accept_seller/<id>/<email>',views.accept_seller),
    path('reject_seller/<id>/<email>',views.reject_seller),

    
    path('admin_view_feedback/<id>',views.admin_view_feedback),
    path('admin_view_rating/<product_id>',views.admin_view_rating),

    path('admin_view_services/<id>',views.admin_view_services),
    path('admin_view_products/<id>',views.admin_view_products),
    path('admin_view_staff/<id>',views.admin_view_staff),




path('admin_view_srequest',views.admin_view_srequest),
path('admin_view_sfeedback/<service_id>',views.admin_view_sfeedback),
path('admin_view_srating/<service_id>',views.admin_view_srating),




    
    # =====================ADMIN===============================================================================================


# -----------------------------------------SELLER-------------------------------------------------------------------------------------------------------
path('seller_home',views.seller_home),



path('seller_update_profile',views.seller_update_profile),

path('seller_change_password',views.seller_change_password),



path('seller_manage_staff',views.seller_manage_staff),
path('seller_add_staff',views.seller_add_staff),
path('update_staff/<id>',views.update_staff),
path('delete_staff/<id>',views.delete_staff),

path('staff_active/<id>',views.staff_active),
path('staff_deactive/<id>',views.staff_deactive),


path('seller_edit_product',views.seller_edit_product),
path('seller_manage_product',views.seller_manage_product),
path('delete_product/<id>',views.delete_product),
path('update_product/<id>',views.update_product),

path('product_active/<id>',views.product_active),
path('product_deactive/<id>',views.product_deactive),



path('seller_edit_service',views.seller_edit_service),
path('seller_manage_services',views.seller_manage_services),
path('delete_services/<id>',views.delete_services),
path('update_services/<id>',views.update_services),

path('seller_manage_category',views.seller_manage_category),
path('delete_category/<id>',views.delete_category),
path('update_category/<id>',views.update_category),
path('category_active/<id>',views.category_active),
path('category_deactive/<id>',views.category_deactive),



path('seller_manage_subcategory/<id>',views.seller_manage_subcategory),
path('delete_subcategory/<category_id>/<id>',views.delete_subcategory),
path('update_subcategory/<category_id>/<id>',views.update_subcategory),
path('subcategory_active/<id>/<category_id>',views.subcategory_active),
path('subcategory_deactive/<id>/<category_id>',views.subcategory_deactive),

path('seller_view_product_booking',views.seller_view_product_booking),

path('seller_view_product_booking',views.seller_view_product_booking),
path('seller_view_booking_details/<id>',views.seller_view_booking_details),
path('seller_view_payment/<id>',views.seller_view_payment),

path('seller_view_ratings/<product_id>',views.seller_view_ratings),



path('seller_assigned_staff_book/<id>/<email>',views.seller_assigned_staff_book),


path('seller_view_services',views.seller_view_services),

path('seller_view_srequest/<id>',views.seller_view_srequest),
path('seller_accept_req/<id>/<service_id>/<email>',views.seller_accept_req),
path('seller_reject_req/<id>/<service_id>/<email>',views.seller_reject_req),


path('seller_assigned_staff/<id>/<email>',views.seller_assigned_staff),

path('seller_view_service_feedback/<service_id>',views.seller_view_service_feedback),
path('seller_view_service_rating/<service_id>',views.seller_view_service_rating),


# -----------------------------------------SELLER-------------------------------------------------------------------------------------------------------
# -----------------------------------------customer-------------------------------------------------------------------------------------------------------



path('customer_home',views.customer_home),
path('customer_update_profile',views.customer_update_profile),
path('customer_change_password',views.customer_change_password),


path('cus_view_sdetals/<id>',views.cus_view_sdetals),
path('customer_view_product/<id>',views.customer_view_product),
path('customer_add_cart/<id>/<seller_id>/<product>/<amt>/<image>/<description>',views.customer_add_cart),

path('customer_my_cart',views.customer_my_cart),
path('customer_remove_cart/<id>',views.customer_remove_cart),


path('customer_add_wlist/<id>',views.customer_add_wlist),
path('customer_view_wlist',views.customer_view_wlist),
path('customer_remove_wlist/<id>',views.customer_remove_wlist),




path('customer_view_booking',views.customer_view_booking),
path('customer_view_booking_details/<id>',views.customer_view_booking_details),
# path('customer_make_payment/<bk_id>/<bk_total>',views.customer_make_payment),
path('customer_view_assigned_staff/<id>',views.customer_view_assigned_staff),


path('customer_view_service',views.customer_view_service),
path('customer_send_service_request/<id>/<rate>',views.customer_send_service_request),
path('customer_view_service_request',views.customer_view_service_request),
# path('customer_make_payment_srequest/<id>/<amount>',views.customer_make_payment_srequest),
path('customer_view_assigned_staff_request/<id>',views.customer_view_assigned_staff_request),
path('customer_send_feedback/<booking_id>/<product_id>',views.customer_send_feedback),
path('bill_generate/<id>',views.bill_generate),
path('cusbk_generate_bill/<id>',views.cusbk_generate_bill),

# path('cus_view_feedback/<product_id>',views.cus_view_feedback),
path('cus_view_feedback/<id>',views.cus_view_feedback),
path('seller_view_feedback/<product_id>',views.seller_view_feedback),

path('customer_add_ratings/<id>',views.customer_add_ratings),


path('customer_send_service_feedback/<service_id>',views.customer_send_service_feedback),
path('customer_add_service_rating/<service_id>',views.customer_add_service_rating),



# -----------------------------------------customer-------------------------------------------------------------------------------------------------------
# -----------------------------------------staff-------------------------------------------------------------------------------------------------------


path('staff_home',views.staff_home),
path('staff_update_profile',views.staff_update_profile),
path('staff_change_password',views.staff_change_password),

path('staff_view_booking',views.staff_view_booking),
path('staff_view_bk_details/<id>',views.staff_view_bk_details),
path('staff_deliver/<id>/<email>',views.staff_deliver),


path('staff_view_service_req',views.staff_view_service_req),

path('staff_update_status/<id>/<email>',views.staff_update_status),
path('fetch_search/',views.fetch_search),
path('analysis_chart',views.analysis_chart),


# -----------------------------------------staff-------------------------------------------------------------------------------------------------------


path('select_change/',views.select_change) ,
path('change_qty/',views.change_qty) ,

# ----------------------------------------razor-user-order-------------------------------------  
   path('customer_make_payment/<id>/<total>',views.customer_make_payment),
    path('user_payment_completes/<id>',views.user_payment_completes),
    path('rpay',views.rpay,name='rpay'),
    path('logoutnow',views.logoutnow,name='logoutnow'),

path('cus_service_histroy',views.cus_service_histroy) ,
path('cus_order_histroy',views.cus_order_histroy) ,



# ----------------------------------------razor-user-bookings-------------------------------------  


   path('customer_make_payment_srequest/<id>/<total>',views.customer_make_payment_srequest),
    path('user_payment_complete/<id>',views.user_payment_complete),
]
