# Generated by Django 4.2.6 on 2024-03-02 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
       # ("seller_accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("total", models.PositiveIntegerField(default=0)),
                ("ordered", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "profile",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="accounts.profile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("gender_cat", models.CharField(max_length=50, null=True)),
                ("sub_cat", models.CharField(max_length=50, null=True)),
                ("articel_type", models.CharField(max_length=50, null=True)),
                ("market_price", models.PositiveIntegerField()),
                ("discount_price", models.PositiveIntegerField(default=0)),
                ("description", models.TextField()),
                ("brand", models.CharField(max_length=200, null=True)),
                ("color", models.CharField(max_length=200, null=True)),
                ("size", models.CharField(default="S", max_length=5)),
                ("material", models.CharField(max_length=200, null=True)),
                ("completelook", models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Sales",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rate", models.PositiveIntegerField(default=0)),
                ("quantity", models.PositiveIntegerField(default=0)),
                ("subtotal", models.PositiveIntegerField(default=0)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cart.product"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductImagesURL",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image_url", models.URLField(blank=True, max_length=500)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cart.product"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductImagesFiles",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image_file", models.ImageField(blank=True, upload_to="products")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cart.product"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ordered_by", models.CharField(max_length=200)),
                ("shipping_address", models.CharField(max_length=200)),
                ("mob_no", models.CharField(blank=True, max_length=12, null=True)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("subtotal", models.PositiveIntegerField(blank=True, null=True)),
                ("discount", models.PositiveIntegerField(blank=True, null=True)),
                ("total", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "order_status",
                    models.CharField(
                        choices=[
                            ("Order Placed", "Order Placed"),
                            ("Order Processing", "Order Processing"),
                            ("Order Completed", "Order Completed"),
                            ("Order Canceled", "Order Canceled"),
                            ("On the way", "On the way"),
                        ],
                        max_length=50,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "cart",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="cart.cart"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CartProduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rate", models.PositiveIntegerField()),
                ("quantity", models.PositiveIntegerField()),
                ("subtotal", models.PositiveIntegerField()),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cart.cart"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cart.product"
                    ),
                ),
            ],
        ),
    ]
