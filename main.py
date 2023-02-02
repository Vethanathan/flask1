from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    file = request.files["file"]
    file.save(file.filenme)
@app.route('/download/<filename>')
def download(filename):
    try:
        path = filename
        print(path)
        return send_file(path, as_attachment=True)
    except Exception as e:
        return str(e)

