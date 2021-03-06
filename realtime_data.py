#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 01:11:35 2020

@author: wei
"""

from node import Node
from config import config

data = {}

def _make_system_nodes_shell():
    for i, name in enumerate(config["System"]["node"], 1):
        data[f"{name}"] = Node(name, i)

_make_system_nodes_shell()

def _make_system_attr_shell():
    for name in config["System"]["attribute"]:
        data[f"{name}"] = 0

_make_system_attr_shell()

def _make_other_system_nodes_shell():
    for name in config["OtherSystem"]["node"]:
        for attr in config["OtherSystem"]["node"][f"{name}"]:
            data[f"{name}_{attr}"] = 0

_make_other_system_nodes_shell()

def _make_other_field():
    data["count"] = 0
    data["time"] = 0
    data["timestamp"] = 0

_make_other_field()

if __name__ == "__main__":
    print(data)