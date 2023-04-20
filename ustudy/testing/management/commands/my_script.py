from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates initial data'

    def handle(self, *args, **options):

        import django
        django.setup()

        from accounts.models import User
        from testing.models.test import Test
        from testing.models.driving_category import DrivingCategory
        from testing.models.question import Question
        from testing.models.answer import Answer
        from testing.models.city import City
        
        # create driving category
        driving_category = DrivingCategory.objects.create(name='A1')
        city = City.objects.create(name="Алматы")
        # create admin user
        try:
            admin_user = User.objects.create_superuser(username='admin', email='admin@example.com', password='admin', city=city)
        except Exception as e:
            print(e)
        # create tests
        test1 = Test.objects.create(
            name='Rules of the Road Test',
            description='Test your knowledge of the rules of the road',
            driving_category=driving_category
        )

        test2 = Test.objects.create(
            name='Traffic Signs Test',
            description='Test your knowledge of traffic signs and signals',
            driving_category=driving_category
        )

        # add questions and answers to test1
        q1 = Question.objects.create(test=test1, text='What is the speed limit in a residential area?')
        a1 = Answer.objects.create(question=q1, text='25 mph', is_correct=True)
        a2 = Answer.objects.create(question=q1, text='35 mph')
        a3 = Answer.objects.create(question=q1, text='45 mph')

        q2 = Question.objects.create(test=test1, text='When can you make a left turn on a red light?')
        a4 = Answer.objects.create(question=q2, text='When turning from a one-way street onto another one-way street', is_correct=True)
        a5 = Answer.objects.create(question=q2, text='When turning from a two-way street onto a one-way street')
        a6 = Answer.objects.create(question=q2, text='When turning from a one-way street onto a two-way street')

        q3 = Question.objects.create(test=test1, text='What is the penalty for driving under the influence?')
        a7 = Answer.objects.create(question=q3, text='Suspension of license and fine', is_correct=True)
        a8 = Answer.objects.create(question=q3, text='Community service')
        a9 = Answer.objects.create(question=q3, text='Nothing')

        q4 = Question.objects.create(test=test1, text='What should you do when you approach a flashing red traffic light?')
        a10 = Answer.objects.create(question=q4, text='Stop, then proceed with caution', is_correct=True)
        a11 = Answer.objects.create(question=q4, text='Slow down and proceed with caution')
        a12 = Answer.objects.create(question=q4, text='Stop, then proceed only when it is safe')

        # add questions and answers to test2
        q5 = Question.objects.create(test=test2, text='What does this sign mean?')
        a13 = Answer.objects.create(question=q5, text='No U-turn', is_correct=True)
        a14 = Answer.objects.create(question=q5, text='One way street')
        a15 = Answer.objects.create(question=q5, text='No parking')

        q6 = Question.objects.create(test=test2, text='What does this sign mean?')
        a16 = Answer.objects.create(question=q6, text='Stop sign ahead', is_correct=True)
        a17 = Answer.objects.create(question=q6, text='Yield sign ahead')
        a18 = Answer.objects.create(question=q6, text='Speed limit ends')

        q7 = Question.objects.create(test=test2, text='What does this sign mean?')
        a19 = Answer.objects.create(question=q7, text='Railroad crossing', is_correct=True)
        a20 = Answer.objects.create(question=q7, text='School zone')
        a21 =Answer.objects.create(question=q7, text='Hospital zone')

        q8 = Question.objects.create(test=test2, text='What does this sign mean?')
        a22 = Answer.objects.create(question=q8, text='Pedestrian crossing', is_correct=True)
        a23 = Answer.objects.create(question=q8, text='Construction zone')
        a24 = Answer.objects.create(question=q8, text='Bicycle lane')

        test1.questions.add(q1, q2, q3, q4)
        test2.questions.add(q5, q6, q7, q8)

        print('Data has been successfully added to the database.')

        self.stdout.write(self.style.SUCCESS('Data created successfully!'))
