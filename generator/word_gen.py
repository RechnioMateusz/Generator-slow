import copy
import random

from .errors import (
    DependenciesMatrixError,
    PropabilityMatrixError,
    WordGenMatrixError
)
from .utils import (
    check_if_char,
    check_if_word,
    check_if_list_of_chars,
    check_if_matrix_of_numbers,
)


class WordGenMatrix:
    def __init__(self):
        self._matrix = list()  # ! Y is starting char and X is ending char
        self._chars = list()

    @property
    def dim(self):
        return len(self._chars)

    @property
    def chars(self):
        return copy.deepcopy(self._chars)

    @chars.setter
    def chars(self, value):
        check_if_list_of_chars(param=value)
        self._chars = value

    @chars.deleter
    def chars(self):
        self._chars = list()
        self._matrix = list()

    @property
    def matrix(self):
        return copy.deepcopy(self._matrix)

    @matrix.setter
    def matrix(self, value):
        check_if_matrix_of_numbers(param=value)
        self._matrix = value

    @matrix.deleter
    def matrix(self):
        self._matrix = list()
        self._chars = list()

    def get_random_char(self):
        if not self._chars:
            raise WordGenMatrixError(
                msg="Cannot get random char from empty list"
            )
        return random.choice(self._chars)

    def __str__(self):
        data = f"+---{'+---' * self.dim}+\n"
        data += f"|:::|{'|'.join(f'{char:^3}' for char in self._chars)}|\n"
        for i, row in enumerate(self._matrix):
            data += f"|{self._chars[i]:^3}|"
            data += f"{'|'.join(f'{value:^3}' for value in row)}|\n"
        data += f"+---{'+---' * self.dim}+\n"

        return data


class DependenciesMatrix(WordGenMatrix):
    def __init__(self):
        super().__init__()

    def add(self, char):
        check_if_char(param=char)

        if char not in self._chars:
            self._chars.append(char)               # * Add new char
            self._matrix.append([0, ] * self.dim)  # * Add new row for char
            for i in range(self.dim - 1):
                self._matrix[i].append(0)          # * Extend old rows
        else:
            char_id = self._chars.index(char)
            raise DependenciesMatrixError(
                msg="Char already exist. Use \'increment\' instead",
                desc=f"Char {char} already exist in index {char_id}"
            )

    def char_exists(self, char):
        check_if_char(param=char)

        return char in self._chars

    def increment(self, char, next_char):
        check_if_char(param=char)
        check_if_char(param=next_char)

        if char not in self._chars:
            raise DependenciesMatrixError(
                msg="Char does not exist. Use \'add\' instead"
            )

        char_id = self._chars.index(char)
        next_char_id = self._chars.index(next_char)
        self._matrix[char_id][next_char_id] += 1

    def add_word(self, word):
        check_if_word(param=word)

        word = word.lower()
        for char in word:
            if not self.char_exists(char=char):
                self.add(char=char)

        for i in range(len(word) - 1):
            self.increment(char=word[i], next_char=word[i + 1])

    def get_propabilities_matrix(self):
        return PropabilitiesMatrix(chars=self.chars, matrix=self.matrix)


class PropabilitiesMatrix(WordGenMatrix):
    def __init__(self, chars, matrix):
        super().__init__()
        self.chars = chars
        self.matrix = matrix

        for row in self._matrix:
            starts_from_char = sum(row)
            if starts_from_char > 0:
                for i, value in enumerate(row):
                    row[i] = value / starts_from_char

    def get_propability(self, char, next_char):
        check_if_char(param=char)
        check_if_char(param=next_char)

        if char not in self._chars:
            raise PropabilityMatrixError(msg="Char does not exist")

        char_id = self._chars.index(char)
        next_char_id = self._chars.index(next_char)
        self._matrix[char_id][next_char_id] += 1

    def get_possible_chars(self, char, treshold=.5):
        check_if_char(param=char)

        if char not in self._chars:
            raise PropabilityMatrixError(msg="Char does not exist")

        char_id = self._chars.index(char)
        possible_chars = list()
        for i, propability in enumerate(self._matrix[char_id]):
            if propability > treshold:
                possible_chars.append(self._chars[i])

        return possible_chars


class WordGenerator:
    def __init__(self, propabilities_matrix):
        self.matrix = propabilities_matrix

    def generate_word(self, char_possibility, max_length):
        word = self.matrix.get_random_char()
        for _ in range(max_length):
            possible_chars = self.matrix.get_possible_chars(
                char=word[-1], treshold=char_possibility
            )
            if possible_chars:
                word += random.choice(possible_chars)
            else:
                break

        return word
