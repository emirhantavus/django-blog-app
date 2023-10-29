from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class PostTestCase(TestCase):
      def setUp(self):
            self.client = APIClient()
            
      def test_post_list(self):
            url = reverse('post_list')
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            
      def test_single_post(self):
            post_id = 5 
            url = reverse('single_post', args=[post_id])
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            
      def test_single_post_not_found(self):
            post_id = 1000 #invalid post id
            url = reverse('single_post', args=[post_id])
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)