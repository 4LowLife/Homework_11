from flask import Flask, render_template
from utils import *


app = Flask(__name__)


@app.route("/")
def main_page():
    candidates: list[dict] = load_candidates_from_json()
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:id>")
def candidate_page(id):
    candidate: dict = get_candidate(id)
    if not candidate:
        return "Кандидат не найден"
    return render_template("single.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def search_candidates_by_name_page(candidate_name):
    candidates: list[dict] = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates)


@app.route("/skill/<skill_name>")
def skill_candidates_by_skill_page(skill_name):
    candidates: list[dict] = get_candidates_by_skill(skill_name)
    return render_template("skill.html", skill=skill_name, candidates=candidates)


app.run()
