from flask import Blueprint, render_template, redirect, url_for, session, jsonify
import os
import psutil
from config import Config

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))
    return render_template("index.html")
