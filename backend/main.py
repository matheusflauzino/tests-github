from pydriller import GitRepository
from pydriller import RepositoryMining
import pandas as pd
import numpy as np
from flask_jsonpify import jsonpify


import re


# Retorna todas as contribuições de um repositório.
def getContribuitions(rep):
    data_commits = []
    for commit in RepositoryMining(rep).traverse_commits():
        for m in commit.modifications:
            is_test = True if '/test/' in m.new_path else True if '/tests/' in m.new_path else False
            data_commits.append({'date': commit.committer_date, 'hash': commit.hash, 'author': commit.author.name, 'email': commit.author.email,
                                 'path': m.new_path, 'file': m.filename, 'change_type': m.change_type.name, 'added': m.added, 'removed': m.removed, 'is_test': is_test})

    df = pd.DataFrame(data_commits)

    return {"data": data_commits, "info": df.values.tolist()}
