from flask import Flask, render_template, request
from werkzeug import secure_filename
import subprocess
from subprocess import Popen, PIPE
app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      p = Popen(['python', 'autograde.py'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
      out, err = p.communicate()
      out = out.decode('utf-8').strip('\n')
      #p = subprocess.Popen(['python', 'autograde.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      #stdout, stderr = p.communicate()
      return render_template("score.html", result = out)

if __name__ == '_main_':
   app.run(debug = True,host="0.0.0.0")
