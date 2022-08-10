from doit.tools import Interactive


def task_build_public_doc():
    return {"actions": ["sphinx-build doc/source public"]}


DOIT_CONFIG = {"action_string_formatting": "new"}


def task_check_code():
    return {
        "actions": [
            "black {pos}",
            "mypy {pos}",
            "pylint {pos}",
        ],
        "verbosity": 2,
        "doc": "run all linters and code checkers",
        "pos_arg": "pos",
    }


def task_serve_doc():
    return {"actions": [Interactive("sphinx-autobuild doc/source doc/build")]}
