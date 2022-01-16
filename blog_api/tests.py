from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth.models import User


class PostTests(APITestCase):
    
    def test_view_post(self): 
        
        # defining endpoint url  
        url = reverse(viewname='blog_api:list_create')
        # client simulate browser going to url
        response = self.client.get(url, format='json')
        # Testing response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def create_post(self):
        testuser1 = User.objects.create_user(
            username='test_user1',
            password='123456789'
        )
        new_category = Category.objects.create(name='django')
        new_post = {
            'title':'new',
            'slug':'new',
            'author':1,
            'content':'new',
            'status':1
        }
        # defining endpoint url  
        url = reverse(viewname='blog_api:list_create')
        # POST data
        data = new_post
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
