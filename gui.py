import time

from generator.word_gen import DependenciesMatrix, WordGenerator


if __name__ == "__main__":
    # TODO: Add GUI and it's good to go :)
    dm = DependenciesMatrix()

    path = r"C:\Users\mateu\Desktop\inżynierka\tests\vector_tests.py"
    with open(path, "r") as file_:
        text = file_.read()

    for line in text.split("\n"):
        list_of_words = line.split(" ")
        for word in list_of_words:
            dm.add_word(word=word.replace("\t", ""))
    print(dm)

    pm = dm.get_propabilities_matrix()
    print(pm)

    wg = WordGenerator(propabilities_matrix=pm)

    input()
    while True:
        print(wg.generate_word(char_possibility=.2, max_length=100))
        time.sleep(.5)
