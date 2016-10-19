# -*- coding: utf-8 -*-
from collections import OrderedDict
import argparse
import json

"""@package The csv2json.py is used to convert csv file into json file.
"""

"""@bref parser input argument.
"""
parser = argparse.ArgumentParser()
parser.add_argument("--input",
    help="A csv file that you want to convert into json",
    type=str)
filename = parser.parse_args().input

"""@bref create keys
First line of csv file contain attributes.
We use attributes as dict keys.
"""
with open(filename, 'r') as stream:
    streams = stream.read().splitlines()
    attributes = streams[0].split(',')
    """@bref create dict template for further usage.
    IMPORTANT: Need to keep in the same order.
    """
    template = OrderedDict((attribute, None) for attribute in attributes )
    """@bref create a list to append data
    """
    instance = list()
    for stream in streams[1:]:
        clip = stream.split(',')
        for idx in range(len(clip)):
            template[template.keys()[idx]] = clip[idx]
        instance.append(template)
    """@bref create a file and store json data
    """
    output_filename = filename.split(',')[0]
    with open(output_filename+'.json', 'w') as output:
        json.dump(instance, output, encoding='utf-8', ensure_ascii=False)
