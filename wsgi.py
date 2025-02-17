from app import app  # Import your Flask app instance

if __name__ == "__main__":
    app.run()  # This is for local development only

# The following line is essential for Gunicorn:
application = app  # This is what Gunicorn looks for