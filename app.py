from flask import Blueprint

# Define the 'main' Blueprint
main = Blueprint('main', __name__)

# Example route (you can add more as needed)
@main.route('/')
def index():
    return {"message": "Welcome to the Superhero API"}
