from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/array')
def array_page():
    return render_template('sections/array.html')

@app.route('/record')
def record_page():
    return render_template('sections/record.html')

@app.route('/recursion')
def recursion_page():
    return render_template('sections/recursion.html')

@app.route('/stack')
def stack_page():
    return render_template('sections/stack.html')

@app.route('/linked_list')
def linked_list_page():
    return render_template('sections/linked_list.html')

@app.route('/queue')
def queue_page():
    return render_template('sections/queue.html')

@app.route('/pointer')
def pointer_page():
    return render_template('sections/pointer.html')

@app.route('/tree')
def tree_page():
    return render_template('sections/tree.html')

@app.route('/graph')
def graph_page():
    return render_template('sections/graph.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
