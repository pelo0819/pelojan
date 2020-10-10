# -*- coding: utf-8 -*-
from importlib.abc import Loader, MetaPathFinder
from importlib.machinery import ModuleSpec
from typing import Dict, List, Optional
from types import ModuleType
from pathlib import Path
import sys

## for old version
# class PeloImporter():
#     def __init__(self, module_code : str):
#         print("__init__()")
#         self.current_module_code = module_code
    
#     def find_module(self, fullname, path = None):
#         return self
    
#     def load_module(self, name):
#         print("name=%s" % name)
#         module = ModuleType(name)
#         exec(self.current_module_code, module.__dict__)
#         sys.modules[name] = module
#         return module


class ModuleImporter(Loader, MetaPathFinder):
    def __init__(self, callback):
        print("ModuleImporter.init")
        self.callback = callback

    def find_spec(self, fullname: str, path = None, 
            target: ModuleSpec = None) -> Optional[ModuleSpec]:
        self.name = fullname
        self.current_module_code = self.callback("modules/%s" % self.name)
        print("ModuleImporter.find_spec")
        return ModuleSpec(fullname, self)

    def create_module(self, spec : ModuleSpec) -> Optional[ModuleType]:
        print("ModuleImporter.create_module")
        module = ModuleType(self.name)
        exec(self.current_module_code, module.__dict__)
        sys.modules[self.name] = module
        return module
    
    def exec_module(self, module: ModuleType):
        pass
