from django.test import TestCase

# Create your tests here.
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        # Create a test post
        Post.objects.create(title="Test Post", content="This is a test.")
    
    def test_post_content(self):
        # Get the post we just created (don't assume id=1)
        post = Post.objects.get(title="Test Post")
        expected_object_name = f'{post.title}'
        self.assertEqual(expected_object_name, 'Test Post')
        
    def test_post_creation(self):
        # Test that a post was actually created
        self.assertEqual(Post.objects.count(), 1)

class PostListViewTest(TestCase):
    def setUp(self):
        Post.objects.create(title="Another Post", content="More content.")
    
    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'myblog/post_list.html')
    
    def test_view_contains_post_data(self):
        response = self.client.get('/')
        self.assertContains(response, 'Another Post')

