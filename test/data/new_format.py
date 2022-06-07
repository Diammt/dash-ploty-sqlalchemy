json_data = {
    "students": {
        "name": [
            "etudiant_60",
            "etudiant_59",
            "etudiant_58",
            "etudiant_57",
            "etudiant_56",
            "etudiant_55",
            "etudiant_54",
            "etudiant_53",
            "etudiant_52",
            "etudiant_51",
            "etudiant_50",
            "etudiant_49",
            "etudiant_48",
            "etudiant_47",
            "etudiant_46",
            "etudiant_45",
            "etudiant_44",
            "etudiant_43",
            "etudiant_42",
            "etudiant_41",
            "etudiant_40",
            "etudiant_39",
            "etudiant_38",
            "etudiant_37",
            "etudiant_36",
            "etudiant_35",
            "etudiant_34",
            "etudiant_33",
            "etudiant_32",
            "etudiant_31",
            "etudiant_30",
            "etudiant_29",
            "etudiant_28",
            "etudiant_27",
            "etudiant_26",
            "etudiant_25",
            "etudiant_24",
            "etudiant_23",
            "etudiant_22",
            "etudiant_21",
            "etudiant_20",
            "etudiant_19",
            "etudiant_18",
            "etudiant_17",
            "etudiant_16",
            "etudiant_15",
            "etudiant_14",
            "etudiant_13",
            "etudiant_12",
            "etudiant_11",
            "etudiant_10",
            "etudiant_9",
            "etudiant_8",
            "etudiant_7",
            "etudiant_6",
            "etudiant_5",
            "etudiant_4",
            "etudiant_3",
            "etudiant_2",
            "etudiant_1"
        ],
        "filieres": [
            "SIRI",
            "SIRI",
            "IM",
            "SI",
            "SI",
            "SI",
            "SI",
            "SI",
            "SIRI",
            "GL",
            "SI",
            "SIRI",
            "GL",
            "SIRI",
            "GL",
            "GL",
            "SI",
            "SI",
            "GL",
            "IM",
            "SI",
            "SI",
            "SI",
            "GL",
            "SI",
            "GL",
            "IM",
            "GL",
            "SI",
            "GL",
            "GL",
            "GL",
            "GL",
            "GL",
            "IM",
            "GL",
            "GL",
            "GL",
            "GL",
            "GL",
            "GL",
            "SI",
            "IM",
            "GL",
            "GL",
            "SI",
            "GL",
            "IM",
            "SI",
            "SI",
            "SI",
            "SI",
            "SI",
            "IM",
            "SI",
            "IM",
            "GL",
            "GL",
            "SI",
            "GL"
        ],
        "total": 60
    },
    "profs_stage": [
        {
            "name": "enseignant_25",
            "grade": "DOCTEUR",
            "disponibilities": {
                    "21/03/2022": ["H1", "H2", "H3"],
                    "22/03/2022": ["H1", "H5", "H6"]
                }
        },
        {
            "name": "enseignant_26",
            "grade": "DOCTEUR",
            "disponibilities": {
                    "21/03/2022": ["H1", "H2", "H3"],
                    "22/03/2022": ["H1", "H5", "H6"]
                }
        }
    ],
    "profs_memoiries": [
        {
            "name": "enseignant_25",
            "grade": "DOCTEUR",
            "disponibilities": {
                    "21/03/2022": ["H1", "H2", "H3"],
                    "22/03/2022": ["H1", "H5", "H6"]
                }
        },
        {
            "name": "enseignant_26",
            "grade": "DOCTEUR",
            "disponibilities": {
                    "21/03/2022": ["H1", "H2", "H3"],
                    "22/03/2022": ["H1", "H5", "H6"]
                }
        }
    ],
    "all_profs": {
        "profs": [
            {
                "name": "enseignant_4",
                "grade": "INGENIEUR/MASTER",
                "filieres": [
                    "IM",
                    "SI",
                    "GL",
                    "SIRI"
                ],
                "disponibilities":{
                    "21/03/2022": ["H1", "H2", "H3"],
                    "22/03/2022": ["H1", "H5", "H6"]
                }
            },
            {
                "name": "enseignant_4",
                "grade": "INGENIEUR/MASTER",
                "filieres": [
                    "IM",
                    "SI",
                    "GL",
                    "SIRI"
                ],
                "disponibilities": {
                    "21/03/2022": ["H1", "H2", "H3"],
                    "22/03/2022": ["H1", "H5", "H6"]
                }
            },
        ],
        "total": 34
    },
    "all_salles": {
        "salles": [
            {
                "name": "salle_1",
                "disponibilities": {
                    "21/03/2022": ["H1", "H2", "H3"],
                    "22/03/2022": ["H1", "H5", "H6"]
                }
            },
            {
                "name": "salle_2",
                "disponibilities": {
                    "21/03/2022": ["H1", "H2", "H3"],
                    "22/03/2022": ["H1", "H5", "H6"]
                }
            },
        ],
        "total": 6
    },
    "all_horaires": [
        "H1",
        "H2",
        "H3",
        "H4",
        "H5",
        "H6",
    ],
    "all_grades": [
        "LICENCE",
        "INGENIEUR/MASTER",
        "DOCTEUR",
        "ASSISTANT",
        "MAITRE ASSISTANT",
        "MAITRE DE CONFERENCES",
        "PROFESSEUR TITULAIRE"
    ],
    "thesis_period": [
        "21/03/2022-08/04/2022"
    ],
    "nb_jury_principal": 2,
    "is_profs_memoiries": 1,
    "is_profs_stages": 0,
    "is_equal_thesis_profs": 1,
    "is_easy_profs_works": 0,
    "nb_solutions": 1,
    "use_saturday": False,
    "president_jury_min_grade": "DOCTEUR",  # le grade minimum du président du jury
}

### NB:
# - remplacer la contrainte sur le président par la contrainte qui utilise: 'president_jury_min_grade'


### NOTES:
# - le format de retour devra spécifié pour chaque programmation :
#   - si un autre est devenu le président le cas échéant
#       - fonction pour réordonner la position des membres du jury + booléen qui dit si le président est le maitre mémoire
#   - si il y a de conflit. Le cas échéant les programmations avec lesquelles il y a de conflits
