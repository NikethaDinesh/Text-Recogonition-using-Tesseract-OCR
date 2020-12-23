from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import main

UPLOAD_FOLDER = '/static/uploads/'

# allow files of a specific type
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD FOLDER'] = UPLOAD_FOLDER

# function to check the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# route and function to handle the upload page
@app.route('/', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):
            # call the OCR function on it
            file = secure_filename(file.filename)
            extracted_text = main.ocr_main(file)

            # extract the text and display it
            return render_template('upload.html', msg='Successfully processed', extracted_text=extracted_text)

    elif request.method == 'GET':
        return render_template('upload.html')


if __name__ == '__main__':
    app.run()
