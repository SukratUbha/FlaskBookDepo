from flask import Blueprint, render_template, request
import library.adapters.repository as repo
from library.adapters.repository import AbstractRepository

search_blueprint = Blueprint(
    'search_bp', __name__)


@search_blueprint.route('/search', methods=['GET','POST'])
def search():
    q = request.args.get('q')

    search_result = filter_books(q, repo.repo_instance)

    # print(a)
    # search_output = []
    # search_mismatch = []
    # for i in repo.books:
    #     if q.lower() in i.title.lower():
    #         search_output.append(i)
    #     elif q in i.authors:
    #         search_output.append(i)
    #     elif q in str(i.release_year):
    #         search_output.append(i)
    #     else:
    #         search_mismatch.append(i)
    # search_output += search_mismatch
    return render_template('home/home2.html', all_books = search_result)


    # return "<h1> Hello </h1>"
def filter_books(q, rep: AbstractRepository):  #put in the repo
    a = rep.search_filter(q)
    return a

# def s(q):
#     # q = request.args.get('q')
#
#     search_output = []
#     search_mismatch = []
#     for i in books:
#         if i.title.__contains__(str(q)):
#             search_output.append(i)
#         else:
#             search_mismatch.append(i)
#
#     return search_output
#     # return "<h1> Hello </h1>"
#
#
# s("swich")