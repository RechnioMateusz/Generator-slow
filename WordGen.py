# -*- coding: utf-8 -*-
"""
@author Mateusz Rechnio

File containing structures used to create matrix of dependencies
and generating new words.
"""

import random

class CharValueStruct(object):
    """
    This is container for the letter and value 
    representing amount of every letter occurrences
    """
    def __init__(self, char, value):
        """
        char = single letter
        value = amount of occurrences
        """
        self.char = char.lower()
        self.value = value
        
    def IncrementValue(self):
        """
        Increments amount of occurrences
        """
        self.value += 1
        
    def __str__(self):
        """
        Converts to nicely formated string
        """
        return str(self.char) + "(" + str(self.value) + ")"

#==============================================================================

class DependenciesMatrix(object):
    """
    Class representing matrix of dependencies between every loaded letter
    """
    def __init__(self, dictionary_with_value):
        """
        Creates matrix of dependencies based on dictionary (letters + values)
        """
        self.dictionary_with_value = dictionary_with_value
        self.matrix = [[0 for i in range(len(self.dictionary_with_value))] for i in range(len(self.dictionary_with_value))]
    
    def __str__(self):
        formatted_matrix = ""
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                temp = 0
                if(self.dictionary_with_value[i].value != 0):
                    temp = self.matrix[i][j] / self.dictionary_with_value[i].value
                
                    formatted_matrix += str(temp) + ", "
            formatted_matrix += "\n"
                    
        return formatted_matrix
    
    def __FindIndexOfLetter__(self, letter):
        """
        Finds index of letter in dictionary (letters + values)
        """
        for i in range(len(self.dictionary_with_value)):
            if(self.dictionary_with_value[i].char == letter.lower()):
                return i
        return 0
    
    def DictionaryContainsLetter(self, letter):
        """
        Check if letter is in dictionary with value
        """
        for i in self.dictionary_with_value:
            if(letter.lower() == i.char):
                return True
        return False
    
    def CreateDependencis(self, path):
        """
        Fills in matrix of dependencies
        """
        words_file = open(path, "r")
        word = words_file.readline()
        while(word != "."):
            current_letter_id = 0
            for letter in word:
                if(letter != "\n"):
                    next_letter_id = self.__FindIndexOfLetter__(letter)
                    self.matrix[current_letter_id][next_letter_id] += 1
                    self.dictionary_with_value[current_letter_id].IncrementValue()
                    current_letter_id = next_letter_id
            word = words_file.readline()
        
        words_file.close()
        
    def __MatrixExtension__(self):
        """
        Extends matrix with new signs / letters
        """
        new_matrix = [[0 for i in range(len(self.dictionary_with_value))] for i in range(len(self.dictionary_with_value))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                new_matrix[i][j] = self.matrix[i][j]
        self.matrix = new_matrix
        
    def UpdateDependencies(self, word):
        """
        Updates dependencis depending on generated words
        """
        current_letter_id = 0
        for letter in word:
            if(self.DictionaryContainsLetter(letter) == False):
                self.dictionary_with_value.append(CharValueStruct(letter, 0))
                self.__MatrixExtension__()
                
            next_letter_id = self.__FindIndexOfLetter__(letter)
            self.matrix[current_letter_id][next_letter_id] += 1
            self.dictionary_with_value[current_letter_id].IncrementValue()
            current_letter_id = next_letter_id

#==============================================================================

class WordGenerator(object):
    """
    Class containing methods generating words
    """
    def __init__(self, dependency_matrix):
        """
        Uses only matrix of dependiences
        """
        self.dependency_matrix = dependency_matrix
    
    def GenerateWordUsingList(self, length):
        """
        Generates word using list.
        Fills in list with letters. For example:
        Starting from letter 'a'
        after 'a' there was 3 x 'b' and 1 x 'c'
        So it means list = [a, a, a, c]
        Then random choice is made
        HIGHER MEMORY USAGE
        LOWER CPU USAGE
        """
        new_word = []
        current_letter_id = 0
        for counter in range(length):
            letters_list = []
            for i in range(len(self.dependency_matrix.matrix[current_letter_id])):
                letters_amount = self.dependency_matrix.matrix[current_letter_id][i]
                for counter in range(letters_amount):
                    letters_list.append(self.dependency_matrix.dictionary_with_value[i].char)
            
            if(len(letters_list) != 0):
                rand = random.randint(0, len(letters_list) - 1)
                new_word.append(letters_list[rand])
                current_letter_id = self.dependency_matrix.__FindIndexOfLetter__(letters_list[rand])
            else:
                break
            
        word_string = ""
        for i in new_word:
            word_string += i
            
        return word_string
    
    def GenerateWordUsingDiscreetVariable(self, length):
        """
        Generates word using discreet value
        LOWER MEMORY USAGE
        HIGHER CPU USAGE
        """
        new_word = []
        current_letter_id = 0
        
        for i in range(length):
            current_letter = self.dependency_matrix.matrix[current_letter_id]
            
            if(sum(current_letter) != 0):
                rand = random.randint(1, sum(current_letter))
                next_letter_id = 0
                for j in range(len(current_letter)):
                    if(current_letter[j] != 0):
                        next_letter_id = j
                        rand -= current_letter[j]
                    
                    if(rand <= 0):
                        new_word.append(self.dependency_matrix.dictionary_with_value[next_letter_id].char)
                        current_letter_id = next_letter_id
                        break
            else:
                break
                
        word_string = ""
        for i in new_word:
            word_string += i
            
        return word_string