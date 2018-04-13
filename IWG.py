# -*- coding: utf-8 -*-
"""
Spyder Editor
@author Mateusz Rechnio

IWG - Intelligent Word Generator
This program creates matrix of dependencies based on list of words from input.
Made for experiment purposes. Uses structures like Marcov's chains.
"""

import os, pickle
import WordGen

#Methods used in user interface and file loading

def DictionaryContains(dictionary, letter):
    """
    Checks if list of letters contains specific letter
    """
    for i in dictionary:
        if(i == letter.lower()):
            return True
    return False

def FillDictionary(dictionary, path):
    """
    Fills Dictionary with letters from file
    """
    words_file = open(path, "r")
    word = words_file.readline()
    
    while(word != "."):
        for letter in word:
            letter = letter.lower()
            if(DictionaryContains(dictionary, letter) == False and letter != "\n"):
                dictionary.append(letter)
        word = words_file.readline()
    words_file.close()

def ClearConsole():
    """
    Clears console
    Waits for any input
    """
    input("\nPress Enter")
    os.system("cls")

#------------------------------------------------------------------------------

def main():
	#Loading data from saved matrix or file containing list of words
    while(True):
        print("[f] Read words from file and create new matrix")
        print("[m] Load saved matrix")
        matrix_file = input("Your choice? ->\t\t")
        if(matrix_file == "f"):
            try:
                path = input("\nPath to file:\t\t")
                os.system("cls")
                dictionary = []
                FillDictionary(dictionary, path)
                dict_w_val = []
                dict_w_val.append(WordGen.CharValueStruct("", 0))
                for letter in dictionary:
                    dict_w_val.append(WordGen.CharValueStruct(letter, 0))
                dep_matrix = WordGen.DependenciesMatrix(dict_w_val)
                dep_matrix.CreateDependencis(path)
            except:
                print("INVALID PATH\nTry again :)")
                ClearConsole()
            else:
                break
            
        elif(matrix_file == "m"):
            try:
                path = input("\nPath to matrix:\t\t")
                os.system("cls")
                loading = open(path, "rb")
                dep_matrix = pickle.load(loading)
                loading.close()
            except:
                print("INVALID PATH\nTry again :)")
                ClearConsole()
            else:
                break
        else:
            os.system("cls")
            print("There is no such option")
            ClearConsole()
    
    word_gen = WordGen.WordGenerator(dep_matrix)
    
	#Main menu
    while(True):
        print("These are your symbols:\n")
        for i in dep_matrix.dictionary_with_value:
            print(i.char, "", end="")
        print("\n\nChoose letter in bracket -> []")
        print("[a] Generate word")
        print("[b] Show dependecy matrix")
        print("[s] Save current matrix")
        print("[x] Exit Program")
        try:
            choice = input("Your choice? ->\t\t").lower()
        except:
            os.system("cls")
        else:
            if(choice == "a"):
                while(True):
                    os.system("cls")
                    print("<<GENERATING WORD>>")
                    try:
                        length = int(input("What max length should it have?\t\t"))
                    except:
                        os.system("cls")
                    else:
                        new_word = word_gen.GenerateWordUsingDiscreetVariable(length)
                        print("\nGenerated word:\n")
                        print("=" * len(new_word))
                        print(new_word)
                        print("=" * len(new_word))
                        print()
                        print("Is this word correct?")
                        print("[y] Yes")
                        print("[c] It is close and I want to correct it")
                        print("[Enter] Generate another one")
                        print("[x] Exit Generating words")
                        
                        choice_word = input("Your choice? ->\t\t")
                        if(choice_word == "y"):
                            os.system("cls")
                            dep_matrix.UpdateDependencies(new_word)
                            print(">>Matrix updated<<")
                            ClearConsole()
                        elif(choice_word == "c"):
                            os.system("cls")
                            print("\nGenerated word:\n")
                            print("=" * len(new_word))
                            print(new_word)
                            print("=" * len(new_word))
                            print()
                            corrected_word = str(input("Give me correct form:\t\t"))
                            dep_matrix.UpdateDependencies(corrected_word)
                            os.system("cls")
                            print(">>Matrix updated<<")
                            ClearConsole()
                        elif(choice_word == "x"):
                            os.system("cls")
                            break
                        elif(choice_word == ""):
                            pass
                        else:
                            os.system("cls")
                            print("There is no such option")
                            ClearConsole()
            elif(choice == "b"):
                os.system("cls")
                print("This is your dependency matrix\n")
                for i in range(len(dep_matrix.matrix)):
                    print(str(dep_matrix.dictionary_with_value[i]) + ": ", end = "")
                    print(dep_matrix.matrix[i])
                ClearConsole()
            elif(choice == "s"):
                os.system("cls")
                print("Saving can create new file\nAnd it can override other files\n")
                try:
                    path = input("Path where you want to save matrix:\t\t")
                    name = input("Name of new file:\t\t")
                except:
                    os.system("cls")
                    print("Can't save in such file")
                    ClearConsole()
                else:
                    saving = open(path + "\\" + name, "wb")
                    pickle.dump(dep_matrix, saving)
                    saving.close()
                    os.system("cls")
                    print(">>Matrix saved<<")
                    ClearConsole()
            elif(choice == "x"):
                break
            else:
                os.system("cls")
                print("There is no such option")
                ClearConsole()
main()