from flask import render_template
from app.modules.communities import communities_bp


@communities_bp.route('/communities', methods=['GET'])
def index():
    return render_template('communities/index.html')
