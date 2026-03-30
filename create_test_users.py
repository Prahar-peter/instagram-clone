#!/usr/bin/env python3
"""
Create test users for Instagram Clone
"""
import requests
import json

API_BASE_URL = "http://localhost:5000/api"

# Test users to create
TEST_USERS = [
    {
        "username": "alice_johnson",
        "email": "alice@example.com",
        "bio": "Photography enthusiast 📸"
    },
    {
        "username": "bob_smith",
        "email": "bob@example.com",
        "bio": "Loves traveling and adventure 🌍"
    },
    {
        "username": "charlie_brown",
        "email": "charlie@example.com",
        "bio": "Coffee addict ☕"
    },
    {
        "username": "diana_prince",
        "email": "diana@example.com",
        "bio": "Foodie 🍕"
    },
    {
        "username": "eve_watson",
        "email": "eve@example.com",
        "bio": "Tech enthusiast 💻"
    }
]

def create_users():
    """Create test users"""
    print("🚀 Creating test users...\n")
    
    created_users = []
    
    for user_data in TEST_USERS:
        try:
            response = requests.post(
                f"{API_BASE_URL}/users",
                json=user_data,
                timeout=5
            )
            
            if response.status_code == 201:
                user = response.json()
                created_users.append(user)
                print(f"✅ Created: {user['username']} (ID: {user['id']})")
            elif response.status_code == 409:
                print(f"⚠️  User '{user_data['username']}' already exists")
            else:
                print(f"❌ Error creating {user_data['username']}: {response.status_code}")
        except Exception as e:
            print(f"❌ Error: {str(e)}")
    
    print("\n" + "="*50)
    print("📊 CREATED USERS SUMMARY")
    print("="*50 + "\n")
    
    for user in created_users:
        print(f"User ID: {user['id']}")
        print(f"Username: {user['username']}")
        print(f"Email: {user['email']}")
        print(f"Bio: {user['bio']}")
        print("-" * 50)
    
    print(f"\n✨ Total users created: {len(created_users)}")
    print("\n📝 You can now sign up with any of these accounts in the web interface,")
    print("or create your own new account!\n")

if __name__ == "__main__":
    try:
        create_users()
    except Exception as e:
        print(f"❌ Failed to connect to API: {str(e)}")
        print("Make sure the Flask backend is running on http://localhost:5000")
