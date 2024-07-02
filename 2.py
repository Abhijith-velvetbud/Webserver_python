from flask import Flask, render_template_string

app = Flask(__name__)

# Define a route for the default URL, which loads the page
@app.route('/')
def home():
    name = "Your Name"  # Replace with the desired name
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Display Name</title>
    </head>
    <body>
        <h1>Hello, {{ name }}!</h1>
    </body>
    </html>
    '''
    return render_template_string(html_content, name=name)

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
