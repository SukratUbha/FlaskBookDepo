from flask import Blueprint, render_template, request
import library.adapters.repository as repo

search_blueprint = Blueprint(
    'search_bp', __name__)


@search_blueprint.route('/search', methods=['GET','POST'])
def search():
    q = request.args.get('q')
    print(q)
    search_output = []
    search_mismatch = []
    for i in repo.books:
        if q.lower() in i.title.lower():
            search_output.append(i)
        else:
            search_mismatch.append(i)
    search_output += search_mismatch
    return render_template('home/home.html', all_books = search_output)
    # return "<h1> Hello </h1>"

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