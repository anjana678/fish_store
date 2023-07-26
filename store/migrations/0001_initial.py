# Generated by Django 4.1.5 on 2023-03-11 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.CharField(max_length=225)),
                ('date', models.CharField(max_length=225)),
                ('status', models.CharField(max_length=225)),
                ('order_id', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=225)),
                ('castatus', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='customerr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=225)),
                ('lname', models.CharField(max_length=225)),
                ('place', models.CharField(max_length=225)),
                ('address', models.CharField(max_length=225)),
                ('phone', models.CharField(max_length=225)),
                ('email', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='loginn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=225)),
                ('password', models.CharField(max_length=225)),
                ('usertype', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=225)),
                ('amt', models.CharField(max_length=225)),
                ('quantity', models.CharField(max_length=225)),
                ('image', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=2000)),
                ('pstatus', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='sellerr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=225)),
                ('lastname', models.CharField(max_length=225)),
                ('place', models.CharField(max_length=225)),
                ('address', models.CharField(max_length=225)),
                ('phone', models.CharField(max_length=225)),
                ('email', models.CharField(max_length=225)),
                ('license', models.CharField(max_length=1000)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.loginn')),
            ],
        ),
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=225)),
                ('rate', models.CharField(max_length=225)),
                ('des', models.CharField(max_length=225)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.sellerr')),
            ],
        ),
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customerr')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.CharField(max_length=225)),
                ('cstatus', models.CharField(max_length=225)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
                
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fn', models.CharField(max_length=225)),
                ('ln', models.CharField(max_length=225)),
                ('place', models.CharField(max_length=225)),
                ('phone', models.CharField(max_length=225)),
                ('email', models.CharField(max_length=225)),
                ('sstatus', models.CharField(max_length=225)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.loginn')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.sellerr')),
            ],
        ),
        migrations.CreateModel(
            name='srequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=225)),
                ('date', models.CharField(max_length=225)),
                ('status', models.CharField(max_length=225)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customerr')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.services')),
            ],
        ),
        migrations.CreateModel(
            name='req_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=225)),
                ('date', models.CharField(max_length=225)),
                ('srequest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.srequest')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.sellerr'),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.subcategory'),
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=225)),
                ('date', models.CharField(max_length=225)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.booking')),
            ],
        ),

        migrations.AddField(
            model_name='customerr',
            name='login',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.loginn'),
        ),
        
        migrations.AddField(
            model_name='booking',
            name='customerr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customerr'),
        ),
        migrations.AddField(
            model_name='booking',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.sellerr'),
        ),
        migrations.CreateModel(
            name='bchild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.CharField(max_length=225)),
                ('bamt', models.CharField(max_length=225)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.booking')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='assign_staff_req',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=225)),
                ('status', models.CharField(max_length=225)),
                ('srequest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.srequest')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.staff')),
            ],
        ),
        migrations.CreateModel(
            name='assign_staff_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=225)),
                ('status', models.CharField(max_length=225)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.booking')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.staff')),
            ],
        ),
    ]
