from app.modules.community.forms import CommunityForm
from app.modules.community.services import CommunityService
from app.modules.community import community_bp
from app.modules.dataset.models import DataSet
from app import community_members
from app.modules.auth.models import User

from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user

import logging


service = CommunityService()
logger = logging.getLogger(__name__)


@community_bp.route("/community/list", methods=['GET'])
@login_required
def community_list():
    form = CommunityForm()
    communities = service.get_all_by_user(current_user.id)
    return render_template('community/community_list.html', form=form, communities=communities)


@community_bp.route("/community/create", methods=['GET', 'POST'])
@login_required
def create_community():
    form = CommunityForm()

    if form.validate_on_submit():
        result = service.create(name=form.name.data, description=form.description.data, user=current_user)
        return service.handle_service_response(
            result=result,
            errors=form.errors,
            success_url='community.community_list',
            success_msg='Community Succesfully Created',
            error_template='community/create_community.html',
            form=form
        )

        return render_template("community/create_community.html", form=form)


@community_bp.route("/community/show/<int:community_id>", methods=['GET'])
@login_required
def show_community(community_id):
    community = service.get_or_404(community_id)

    has_access = service.is_member(user_id=current_user.id, community_id=community_id)

    if not has_access:
        flash("You do not belong to this community", "error")
        return redirect(url_for('community.index'))

    return render_template("community/show_community.html", community=community)


@community_bp.route("/community/<int:community_id>/datasets", methods=['GET'])
@login_required
def community_datasets(community_id):
    community = service.get_or_404(community_id)
    datasets = (
        DataSet.query.join(User)
        .join(community_members)
        .filter(community_members.c.community_id == community_id)
        .all()
    )

    return render_template("community/community_datasets.html", community=community, datasets=datasets)
