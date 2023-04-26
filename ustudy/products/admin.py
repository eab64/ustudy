from django.contrib import admin

# Register your models here.
from products.models.subscription_mock import Subscription
from products.models.product import Product
from products.models.category import Category
from products.models.question import Question
from products.models.variant import Variant

from import_export.admin import ExportMixin
from import_export.admin import ImportExportActionModelAdmin, ImportExportMixin, ImportMixin
from products import resources


class SubscriptionAdmin(ImportExportMixin, ImportExportActionModelAdmin, ImportMixin):
    resource_class = resources.SubscriptionResource
    list_display = ('id', 'active_until', 'price')

class ProductAdmin(ImportExportMixin, ImportExportActionModelAdmin, ImportMixin):
    resource_class = resources.ProductResource
    list_display = ('id', 'name', 'description', 'subscription', 'useful_info', 'paid')

class CategoryAdmin(ImportExportMixin, ImportExportActionModelAdmin, ImportMixin):
    resource_class = resources.CategoryResource
    list_display = ('id', 'name', 'description_ru', 'description_kz', 'time_to_pass', 'max_errors', 'questions_count', 'product')

class QuestionAdmin(ImportExportMixin, ImportExportActionModelAdmin, ImportMixin):
    resource_class = resources.QuestionResource
    list_display = ('id', 'text', 'is_multiple_choice', 'category', 'image', 'language')

class VariantAdmin(ImportExportMixin, ImportExportActionModelAdmin, ImportMixin):
    resource_class = resources.VariantResource
    list_display = ('id', 'text', 'is_correct', 'question')


if not admin.site.is_registered(Subscription):
    admin.site.register(Subscription, SubscriptionAdmin)

# if not admin.site.is_registered(Product):
admin.site.register(Product)

if not admin.site.is_registered(Category):
    admin.site.register(Category, CategoryAdmin)

if not admin.site.is_registered(Question):
    admin.site.register(Question, QuestionAdmin)

if not admin.site.is_registered(Variant):
    admin.site.register(Variant, VariantAdmin)



