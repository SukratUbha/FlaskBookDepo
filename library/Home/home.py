from flask import Blueprint, render_template

import library.utilities.utilities as utilities   #create a utility folder that has functions which get tags and books etc

'''have to modify'''
home_blueprint = Blueprint(
    'home_bp', __name__)


@home_blueprint.route('/', methods=['GET'])
def home():
    return render_template(
        'home/home.html',
        selected_articles=utilities.get_selected_articles(),   #Here I'll get all the books to show
        tag_urls=utilities.get_tags_and_urls()                  #maybe use this to show book names picture and tags etc
    )
