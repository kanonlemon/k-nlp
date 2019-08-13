# -*- coding: utf-8 -*-
"""
Convert any character to number 
"""
import os
import csv

default_character_dict = os.path.join(os.path.split(os.path.realpath(__file__))[0], "character.dict") 

class TextConverter(object):
    
    
    def __init__(self, dictionary=None, dictpath=None, encoding='utf8', delimiter="\t", *args, **kwargs):
        """
        input file must be csv file
        and the first column is the value(character integer index)
        and the second column is the key(character)
        """
        if dictionary:
            self._dict = dictionary
        else:
            self._dict = self.load_csv_dict(dictpath, encoding, delimiter)
        return super().__init__(*args, **kwargs)


    def load_csv_dict(self, dictpath=None, encoding='utf8', delimiter="\t"):
        if not dictpath:
            dictpath = default_character_dict
        _dict = {}
        with open(dictpath, encoding=encoding) as fi:
            csv_reader = csv.reader(fi, delimiter=delimiter)
            for row in csv_reader:
                if row:
                    _dict[row[1]] = int(row[0])
        return _dict


    def text2number(self, text, defaultValue=-1, padding=0, dropIfNotExist=True):
        results = []
        for character in text:
            res = self._dict.get(character, None)
            if res != None:
                results.append(res) 
            elif dropIfNotExist:
                continue
            else:
                results.append(defaultValue)
        if padding > 0:
            if len(results) >= padding:
                results = results[0:padding]
            else:
                results = results + [defaultValue] * (padding - len(results))   
        return results


