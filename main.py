from flask import Flask, render_template, request

import utils

# import templates
# import utils
app = Flask(__name__)


@app.route('/')
def main():
    return render_template("base.html",
                           the_title='Dungeon Menu',
                           the_header='Welcome to the Dungeon!')


def log_request(reg, res):
    with open('./log.txt', 'a') as f:
        print(reg.__dict__, res, file=f)


@app.route('/odd', methods=['POST'])
def odd():
    return render_template('entry1.html', the_title='Enter range limits:')


@app.route('/even', methods=['POST'])
def even():
    return render_template('entry2.html', the_title='Enter range limits:')


@app.route('/simple', methods=['POST'])
def simple():
    return render_template('entry3.html', the_title='Enter range limits:')


@app.route('/square', methods=['POST'])
def square():
    return render_template('entry4.html', the_title='Enter range limits:')


@app.route('/odd_results', methods=['POST'])
def odd_result():
    start = request.form['start']
    end = request.form['end']
    plist = utils.odd_list_create(int(start), int(end))
    title = f'All odd numbers in range {start}-{end}:'
    return render_template('results.html',
                           the_title=title,
                           the_result=plist)


@app.route('/even_results', methods=['POST'])
def even_result():
    start = request.form['start']
    end = request.form['end']
    plist = utils.even_list_create(int(start), int(end))
    title = f'All even numbers in range {start}-{end}:'
    return render_template('results.html',
                           the_title=title,
                           the_result=plist)


@app.route('/simple_results', methods=['POST'])
def simple_result():
    start = request.form['start']
    end = request.form['end']
    plist = utils.simple_list_create(int(start), int(end))
    title = f'All prime numbers in range {start}-{end}:'
    return render_template('results.html',
                           the_title=title,
                           the_result=plist)


@app.route('/square_results', methods=['POST'])
def square_result():
    start = request.form['start']
    end = request.form['end']
    plist = utils.square_list_create(int(start), int(end))
    title = f'All second roots of numbers in range {start}-{end}:'
    return render_template('results.html',
                           the_title=title,
                           the_result=plist)


@app.route('/go_back', methods=['POST'])
def go_back():
    return render_template("base.html",
                           the_title='Dungeon Menu',
                           the_header='Welcome to the Dungeon!')


app.run()