from django.contrib import admin

# Register your models here.
from products.models import Subscription
from products.models import Product
from products.models import Category
from products.models import Question
from products.models import Variant

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


# check if the Subscription model is already registered
if not admin.site.is_registered(Subscription):
    admin.site.register(Subscription, SubscriptionAdmin)

# check if the Product model is already registered
# if not admin.site.is_registered(Product):
admin.site.register(Product)

# check if the Category model is already registered
if not admin.site.is_registered(Category):
    admin.site.register(Category, CategoryAdmin)

# check if the Question model is already registered
if not admin.site.is_registered(Question):
    admin.site.register(Question, QuestionAdmin)

# check if the Variant model is already registered
if not admin.site.is_registered(Variant):
    admin.site.register(Variant, VariantAdmin)



