# -*- coding: utf-8 -*-
"""
Convert any character to number 
"""
import sys
import os

default_character_dict = os.path.join(sys.path[0], "character.dict") 

class Converter(object):
    def __init__(self, dictpath=None, dictionary=None):
        if dictionary:
            self._dict = dictionary
        else:
            self._dict = self.load_dict(dictpath)


    def load_dict(self, dictpath=None, encoding='utf8'):
        if not dictpath:
            dictpath = default_character_dict
        fi = open(dictpath, encoding=encoding)
        _dict = {}
        for row in fi.readlines():
            if row:
                splited = row.replace("\n", "").split("\t")
                _dict[splited[1]] = splited[0]
        return _dict


    def text2number(self, text, dropIfNotExist=True, defaultValue=-1):
        results = []
        for character in text:
            res = self._dict.get(character, None)
            if res != None:
                results.append(res) 
            elif dropIfNotExist:
                continue
            else:
                results.append(defaultValue)
        return results


if __name__ == "__main__":
    converter = Converter()
    print(converter.text2number("你好呀!"))     
        
