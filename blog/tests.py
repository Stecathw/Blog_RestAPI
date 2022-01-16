from unicodedata import category
from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category


# Create your tests here.

class Test_Create_Post(TestCase):
    
    @classmethod
    
    # Set up data for the whole TestCase
    def setUpTestData(cls):
        
        testuser1 = User.objects.create_user(
            username='test_user1',
            password='123456789'
        )
        test_category = Category.objects.create(name='django')
        test_post = Post.objects.create(
            category=Category.objects.get(id=1),
            title='Post Title',
            slug='post-slug',
            author=User.objects.get(id=1),
            content='Post Content',
            status=1
        )
    
    
    def test_blog_content(self):
        
        post = Post.publicpostobjects.get(id=1)
        cat = Category.objects.get(id=1)
        user = User.objects.get(id=1)
        
        self.assertEqual(f'{post.author}', user.username)
        self.assertEqual(f'{post.title}', 'Post Title')
        self.assertEqual(f'{post.content}', 'Post Content')
        self.assertEqual(f'{post.slug}', 'post-slug')
        self.assertEqual(post.status, 1)
        self.assertEqual(f'{post.category}', cat.name)
        
        self.assertEqual(str(post), post.title)
        self.assertEqual(str(cat), cat.name)