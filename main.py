from flask import Flask
app = Flask(__name__)


@app.route('/')
def main():
    return """
    This is the homepage! Welcome to your pantry! Here you can add things to your pantry!
    When adding things you can add the name, quantity, par, and expiration date. COOL NOW I HAVE TO LEARN ALL THE HTML/JINJA STUFF!
    """
