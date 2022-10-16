from flask import ( Blueprint, render_template)
import json

pets = json.load(open('pets.json'))
bp = Blueprint('pet', __name__ , url_prefix="/pets")

@bp.route('/')
def index():
    return render_template('pets/index.html', pets=pets)

@bp.route('/<int:post_id>')
def showFacts(post_id):
    return render_template('pets/petFacts.html', pet=pets[post_id - 1 ])
