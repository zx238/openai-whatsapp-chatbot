from .whatsapp_app import app
def main():
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
    # app.run()