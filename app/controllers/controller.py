from app import app
from flask import render_template
# from app.models.todo_list import tasks
from app.models.shopping_list import lists

# @app.route('/')
# def index():
#     return "List of all orders!"

@app.route('/lists')
def index():
    return render_template('order.html', title="Online Shop", orders= lists)


    
    
