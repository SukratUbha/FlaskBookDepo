from flask import Blueprint, render_template, request
import library.adapters.repository as repo
from library.adapters.repository import AbstractRepository

search_blueprint = Blueprint(
    'search_bp', __name__)


@search_blueprint.route('/search', methods=['GET','POST'])
def search():
    q = request.args.get('q')

    search_result = filter_books(q, repo.repo_instance)
    return render_template('home/home2.html', all_books = search_result)


def filter_books(q, rep: AbstractRepository):  #put in the repo
    a = rep.search_filter(q)
    return a