from app import create_app

app = create_app()

if __name__ == '__main__':
    print("🚀 Instagram Clone API is starting...")
    print("📍 Server running at http://0.0.0.0:5000")
    print("✅ Health check: http://localhost:5000/api/health")
    app.run(debug=True, host='0.0.0.0', port=5000)
