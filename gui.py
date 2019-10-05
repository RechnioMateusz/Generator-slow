import tkinter as tk
from tkinter import filedialog

from generator.word_gen import DependenciesMatrix, WordGenerator
from generator.utils import split_text


class App(tk.Tk):
    DEF_GRID = {
        "sticky": tk.NSEW,
        "padx": 5,
        "pady": 5,
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._dependencies_matrix = DependenciesMatrix()
        self._word_generator = None

        self._set_parameters()
        self._create_widgets()

        self.mainloop()

    def _set_parameters(self):
        self.title("Word Generator")
        self.geometry("500x300")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)
        self.rowconfigure(4, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=1)

    def _create_widgets(self):
        self.btn_load_text = tk.Button(
            master=self, text="Load Text", command=self._load_text
        )
        self.btn_load_text.grid(row=1, column=1, **self.DEF_GRID)

        self.btn_gen_word = tk.Button(
            master=self, text="Generate Word", command=self._generate_word
        )
        self.btn_gen_word.grid(row=1, column=2, **self.DEF_GRID)

        self.scale_prop = tk.Scale(
            master=self, from_=0, to=1, resolution=.001,
            label="Propability Between Next Chars", orient=tk.HORIZONTAL
        )
        self.scale_prop.grid(row=2, column=1, **self.DEF_GRID)

        self.scale_length = tk.Scale(
            master=self, from_=0, to=100, resolution=1,
            label="Word Max Length", orient=tk.HORIZONTAL
        )
        self.scale_length.grid(row=2, column=2, **self.DEF_GRID)

        self.entry_word = tk.Entry(master=self, width=60)
        self.entry_word.grid(row=3, column=1, columnspan=2, **self.DEF_GRID)

    def _load_text(self):
        file_path = filedialog.askopenfilename(
            initialdir="/", title="Select Text File",
            filetypes=(("All", "*.*"), )
        )
        if not file_path:
            return

        with open(file_path, "r") as text_file:
            text = text_file.read()

        for word in split_text(text=text):
            self._dependencies_matrix.add_word(word=word)

        prop_matrix = self._dependencies_matrix.get_propabilities_matrix()
        self._word_generator = WordGenerator(propabilities_matrix=prop_matrix)

    def _generate_word(self):
        word = self._word_generator.generate_word(
            char_possibility=self.scale_prop.get(),
            max_length=self.scale_length.get()
        )
        self.entry_word.delete(0, tk.END)
        self.entry_word.insert(0, word)


if __name__ == "__main__":
    App()
