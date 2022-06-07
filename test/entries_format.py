from pathlib import Path
from data.exemple import json_data as old_entries_format
import json


entries_format = {}
entries_format.update({
    "students": old_entries_format.get("students"),
    "profs_stage": [
        {
            "name": prof_stage.get("name"),
            "grade": prof_stage.get("grade"),
            "disponibilities": {
                str(displonibility).split()[0]: ["H1", "H2", "H3", "H4", "H5", "H6"] for displonibility in prof_stage.get("disponibilities")
            },
        } for prof_stage in old_entries_format.get("profs_stage")
    ],
    "profs_memoiries": [
        {
            "name": prof_memoirie.get("name"),
            "grade": prof_memoirie.get("grade"),
            "disponibilities": {
                str(displonibility).split()[0]: ["H1", "H2", "H3", "H4", "H5", "H6"] for displonibility in prof_memoirie.get("disponibilities")
            },
        } for prof_memoirie in old_entries_format.get("profs_memoiries")
    ],
    "all_profs": {
        "profs": [
            {
                "name": prof.get("name"),
                "grade": prof.get("grade"),
                "disponibilities": {
                    str(displonibility).split()[0]: ["H1", "H2", "H3", "H4", "H5", "H6"] for displonibility in prof.get("disponibilities")
                },
                "filieres": prof.get("filieres"),
            } for prof in old_entries_format.get("all_profs").get("profs")
        ],
        "total": old_entries_format.get("all_profs").get("total")
    },
    "all_salles": {
        "salles": [
            {
                "name": salle.get("name"),
                "disponibilities": {
                    str(displonibility).split()[0]: ["H1", "H2", "H3", "H4", "H5", "H6"] for displonibility in salle.get("disponibilities")
                },
            } for salle in old_entries_format.get("all_salles").get("salles")
        ],
        "total": old_entries_format.get("all_salles").get("total")
    },
    "all_horaires": old_entries_format.get("all_horaires"),
    "all_grades": old_entries_format.get("all_grades"),
    "thesis_period": old_entries_format.get("thesis_period"),
    "nb_jury_principal": old_entries_format.get("nb_jury_principal"),
    "is_profs_memoiries": old_entries_format.get("is_profs_memoiries"),
    "is_profs_stages": old_entries_format.get("is_profs_stages"),
    "is_equal_thesis_profs": old_entries_format.get("is_equal_thesis_profs"),
    "is_easy_profs_works": old_entries_format.get("is_easy_profs_works"),
    "nb_solutions": old_entries_format.get("nb_solutions"),
    "use_saturday": old_entries_format.get("use_saturday"),
    "president_jury_min_grade": old_entries_format.get("president_jury_min_grade"),
})
path = "{}/{}".format(Path(__file__).parent, "data/entries_format.json")
print("path: ", path)
# print("entries_format: ", entries_format)
with open(path, "w") as f:
    f.write(json.dumps(entries_format, indent=4))