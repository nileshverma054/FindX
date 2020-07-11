from flask import Flask, render_template, url_for, request, redirect, jsonify
from evaluate import infer
from create_hist import Embeddings

app = Flask(__name__)
app.secret_key = 'hey mrnk'
#search setup
depth = 15
d_type = 'd1'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('assets/welcome.html')


@app.route('/get_results', methods=['GET','POST'])
def get_results():
    if request.method == 'POST':
        q_img = request.files['image']
        print(q_img)        
        obj = Embeddings()
        q_hist = obj.make_hist(q_img)
        results = infer(q_hist, depth=depth, d_type=d_type)
    return render_template('results.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)