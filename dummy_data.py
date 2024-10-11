import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


from faker import Faker
from posts.models import Post, Category
from django.contrib.auth.models import User
import random

def seed_users(n):
    fake = Faker()
    
    for _ in range(n):
        User.objects.create(
            username=fake.user_name(),
            password="MoH.1822"
        )


def seed_categories(n):
    fake = Faker()
    
    for _ in range(n):
        Category.objects.create(
            name=fake.name()
        )
    

def seed_posts(n):
    fake = Faker()
    
    images = ['01.jpg', '02.jpg', '03.jpg', '04.jpg', '05.jpg',
              '06.jpg', '07.jpg', '08.jpg', '09.jpg', '10.jpg']
    
    users = User.objects.all()
    
    categories = Category.objects.all()
    
    for _ in range(n):
        Post.objects.create(
            title=fake.name(),
            content=fake.text(max_nb_chars=2000),
            draft=False,
            # tags="veggi",
            image=random.choice(images),
            author=random.choice(users),
            category=random.choice(categories)
        )


seed_users(8)
# seed_categories(10)
seed_posts(50)