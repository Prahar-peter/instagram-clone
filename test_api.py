import pytest
import requests
import json

BASE_URL = "http://localhost:5000/api"

class TestInstagramAPI:
    """Test suite for Instagram Clone API"""
    
    @classmethod
    def setup_class(cls):
        """Setup test data"""
        cls.test_user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "bio": "Test bio"
        }
        cls.test_user_id = None
        cls.test_post_id = None
        cls.test_comment_id = None
        cls.test_like_id = None
    
    # ==================== HEALTH CHECK TESTS ====================
    
    def test_health_check(self):
        """Test that API health check endpoint works"""
        response = requests.get(f"{BASE_URL}/health")
        assert response.status_code == 200
        data = response.json()
        assert data['status'] == 'API is running'
    
    # ==================== USER TESTS ====================
    
    def test_create_user(self):
        """Test creating a new user"""
        response = requests.post(
            f"{BASE_URL}/users",
            json=self.test_user_data
        )
        assert response.status_code == 201
        data = response.json()
        assert data['username'] == self.test_user_data['username']
        assert data['email'] == self.test_user_data['email']
        assert data['bio'] == self.test_user_data['bio']
        assert 'id' in data
        
        # Store user ID for later tests
        TestInstagramAPI.test_user_id = data['id']
    
    def test_create_duplicate_user(self):
        """Test that duplicate username returns error"""
        response = requests.post(
            f"{BASE_URL}/users",
            json=self.test_user_data
        )
        assert response.status_code == 409
        assert 'error' in response.json()
    
    def test_get_user(self):
        """Test retrieving a user by ID"""
        response = requests.get(f"{BASE_URL}/users/{self.test_user_id}")
        assert response.status_code == 200
        data = response.json()
        assert data['id'] == self.test_user_id
        assert data['username'] == self.test_user_data['username']
    
    def test_get_nonexistent_user(self):
        """Test that getting non-existent user returns 404"""
        response = requests.get(f"{BASE_URL}/users/99999")
        assert response.status_code == 404
        assert 'error' in response.json()
    
    def test_update_user(self):
        """Test updating user bio"""
        new_bio = "Updated bio"
        response = requests.put(
            f"{BASE_URL}/users/{self.test_user_id}",
            json={"bio": new_bio}
        )
        assert response.status_code == 200
        data = response.json()
        assert data['bio'] == new_bio
    
    # ==================== POST TESTS ====================
    
    def test_create_post(self):
        """Test creating a new post"""
        post_data = {
            "content": "This is my first post!",
            "image_url": "https://example.com/photo.jpg",
            "user_id": self.test_user_id
        }
        response = requests.post(
            f"{BASE_URL}/posts",
            json=post_data
        )
        assert response.status_code == 201
        data = response.json()
        assert data['content'] == post_data['content']
        assert data['author_id'] == self.test_user_id
        assert 'id' in data
        
        # Store post ID for later tests
        TestInstagramAPI.test_post_id = data['id']
    
    def test_create_post_invalid_user(self):
        """Test creating post with non-existent user"""
        post_data = {
            "content": "Test post",
            "user_id": 99999
        }
        response = requests.post(
            f"{BASE_URL}/posts",
            json=post_data
        )
        assert response.status_code == 404
        assert 'error' in response.json()
    
    def test_get_all_posts(self):
        """Test retrieving all posts"""
        response = requests.get(f"{BASE_URL}/posts")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
    
    def test_get_post(self):
        """Test retrieving a specific post"""
        response = requests.get(f"{BASE_URL}/posts/{self.test_post_id}")
        assert response.status_code == 200
        data = response.json()
        assert data['id'] == self.test_post_id
        assert data['content'] == "This is my first post!"
        assert 'comments' in data
    
    def test_get_nonexistent_post(self):
        """Test getting non-existent post returns 404"""
        response = requests.get(f"{BASE_URL}/posts/99999")
        assert response.status_code == 404
        assert 'error' in response.json()
    
    # ==================== COMMENT TESTS ====================
    
    def test_create_comment(self):
        """Test creating a comment on a post"""
        comment_data = {
            "text": "Great post!",
            "user_id": self.test_user_id,
            "post_id": self.test_post_id
        }
        response = requests.post(
            f"{BASE_URL}/comments",
            json=comment_data
        )
        assert response.status_code == 201
        data = response.json()
        assert data['text'] == comment_data['text']
        assert data['author_id'] == self.test_user_id
        assert data['post_id'] == self.test_post_id
        assert 'id' in data
        
        # Store comment ID for later tests
        TestInstagramAPI.test_comment_id = data['id']
    
    def test_create_comment_invalid_post(self):
        """Test creating comment on non-existent post"""
        comment_data = {
            "text": "Test comment",
            "user_id": self.test_user_id,
            "post_id": 99999
        }
        response = requests.post(
            f"{BASE_URL}/comments",
            json=comment_data
        )
        assert response.status_code == 404
        assert 'error' in response.json()
    
    def test_get_post_with_comments(self):
        """Test that post includes comments"""
        response = requests.get(f"{BASE_URL}/posts/{self.test_post_id}")
        assert response.status_code == 200
        data = response.json()
        assert 'comments' in data
        assert len(data['comments']) > 0
        assert data['comments'][0]['text'] == "Great post!"
    
    # ==================== LIKE TESTS ====================
    
    def test_create_like(self):
        """Test liking a post"""
        like_data = {
            "user_id": self.test_user_id,
            "post_id": self.test_post_id
        }
        response = requests.post(
            f"{BASE_URL}/likes",
            json=like_data
        )
        assert response.status_code == 201
        data = response.json()
        assert data['user_id'] == self.test_user_id
        assert data['post_id'] == self.test_post_id
        assert 'id' in data
        
        # Store like ID for later tests
        TestInstagramAPI.test_like_id = data['id']
    
    def test_duplicate_like(self):
        """Test that duplicating like returns error"""
        like_data = {
            "user_id": self.test_user_id,
            "post_id": self.test_post_id
        }
        response = requests.post(
            f"{BASE_URL}/likes",
            json=like_data
        )
        assert response.status_code == 409
        assert 'error' in response.json()
    
    def test_get_post_likes(self):
        """Test retrieving likes for a post"""
        response = requests.get(f"{BASE_URL}/likes/post/{self.test_post_id}")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
    
    def test_post_includes_like_count(self):
        """Test that post includes like count"""
        response = requests.get(f"{BASE_URL}/posts/{self.test_post_id}")
        assert response.status_code == 200
        data = response.json()
        assert 'likes_count' in data
        assert data['likes_count'] > 0
    
    # ==================== DELETE TESTS ====================
    
    def test_delete_comment(self):
        """Test deleting a comment"""
        response = requests.delete(f"{BASE_URL}/comments/{self.test_comment_id}")
        assert response.status_code == 200
        assert 'message' in response.json()
    
    def test_delete_nonexistent_comment(self):
        """Test deleting non-existent comment returns 404"""
        response = requests.delete(f"{BASE_URL}/comments/99999")
        assert response.status_code == 404
        assert 'error' in response.json()
    
    def test_delete_like(self):
        """Test deleting a like (unlike)"""
        response = requests.delete(f"{BASE_URL}/likes/{self.test_like_id}")
        assert response.status_code == 200
        assert 'message' in response.json()
    
    def test_delete_post(self):
        """Test deleting a post"""
        response = requests.delete(f"{BASE_URL}/posts/{self.test_post_id}")
        assert response.status_code == 200
        assert 'message' in response.json()
    
    def test_delete_nonexistent_post(self):
        """Test deleting non-existent post returns 404"""
        response = requests.delete(f"{BASE_URL}/posts/99999")
        assert response.status_code == 404
        assert 'error' in response.json()


if __name__ == '__main__':
    pytest.main([__file__, '-v', '-s'])
