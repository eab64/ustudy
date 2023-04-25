from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates initial data'

    def handle(self, *args, **options):
            
        import django
        django.setup()
        from django.utils import timezone

        from products.models import Subscription, Product, Category, Question, Variant
        print("1")
        subscription = Subscription.objects.create(active_until=timezone.now(), price=10.99)
        print("2")

        # Создаем продукт и связываем его с подпиской
        product = Product.objects.create(name='Тесты по ПДД', subscription=subscription)

        # Создаем две категории и связываем их с продуктом
        category_a1 = Category.objects.create(name='A1', product=product)
        category_b1 = Category.objects.create(name='B1', product=product)

        # Создаем вопросы и связываем их с категориями
        questions_data = [
            {'text': 'Вопрос на русском 1', 'language': 'ru', 'category': category_a1},
            {'text': 'Вопрос на казахском 1', 'language': 'kz', 'category': category_a1},
            {'text': 'Вопрос на русском 2', 'language': 'ru', 'category': category_a1},
            {'text': 'Вопрос на казахском 2', 'language': 'kz', 'category': category_a1},
            {'text': 'Вопрос на русском 3', 'language': 'ru', 'category': category_b1},
            {'text': 'Вопрос на казахском 3', 'language': 'kz', 'category': category_b1},
            {'text': 'Вопрос на русском 4', 'language': 'ru', 'category': category_b1},
            {'text': 'Вопрос на казахском 4', 'language': 'kz', 'category': category_b1},
        ]

        for question_data in questions_data:
            question = Question.objects.create(**question_data)
            
            # Создаем варианты ответов и связываем их с вопросами
            variant1 = Variant.objects.create(text='Вариант 1', is_correct=True, question=question)
            variant2 = Variant.objects.create(text='Вариант 2', is_correct=False, question=question)

        print('Data has been successfully added to the database.')

        self.stdout.write(self.style.SUCCESS('Data created successfully!'))
