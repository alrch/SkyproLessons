import utils
from flask import Flask, render_template

app = Flask(__name__)

all_candidates = utils.load_candidates("candidates.json")


@app.route('/')
def page_names():
    return render_template('name_list.html', candidates=all_candidates)


@app.route('/candidate/<pk>/')
def page_profile(pk):
    return render_template('profile.html', candidate=utils.candidate_by_id(all_candidates, pk))


@app.route('/search/<name>/')
def page_search_by_name(name):
    return render_template(
        'candidate_by_name.html',
        candidates=utils.candidates_by_name(all_candidates, name),
        len=len(utils.candidates_by_name(all_candidates, name))
    )


@app.route('/skill/<skill>/')
def page_search_by_skill(skill):
    candidates = utils.candidates_by_skill(all_candidates, skill)
    return render_template('candidate_by_skill.html', candidates=candidates, len=len(candidates), skill_name=skill)

app.run()



