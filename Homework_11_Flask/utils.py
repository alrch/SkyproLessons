import json


def load_candidates(path):
    """makes a list of all candidates"""
    c_names = []
    with open(path) as file:
        candidates = json.load(file)
    return candidates


def candidate_by_id(candidates, c_id):
    """search for candidate by ID"""
    for candidate in candidates:
        if candidate["pk"] == int(c_id):
            return candidate


def candidates_by_name(candidates, name_of_candidate):
    """search for candidates by name"""
    cand_by_name = []
    for candidate in candidates:
        if name_of_candidate.lower() in candidate["name"].lower().split():
            cand_by_name.append(candidate)
    return cand_by_name


def candidates_by_skill(candidates, name_of_skill):
    """search for candidates by skill"""
    cand_by_skill = []
    for candidate in candidates:
        if name_of_skill.lower() in candidate["skills"].lower().split(", "):
            cand_by_skill.append(candidate)
    return cand_by_skill


def skills_dict(candidates):
    """makes a dictionary of all skills"""
    skills = []
    skills_dictionary = {}
    for candidate in candidates:
        skills += candidate["skills"].lower().split(", ")
    skills = set(skills)
    for skill in skills:
        skills_dictionary[skill] = []
        for candidate in candidates:
            if skill in candidate["skills"].lower().split(", "):
                skills_dictionary[skill].append(candidate["name"])
    return skills_dictionary

