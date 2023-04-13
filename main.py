from flask import Flask, render_template
# import templates
# import utils
app = Flask(__name__)


@app.route('/')
def main():
    return render_template("base.html",
                           the_title='Dungeon Menu',
                           the_header='Welcome to the Dungeon!')


app.run()