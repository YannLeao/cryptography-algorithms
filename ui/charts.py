import collections
import string
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from config import BACKGROUND_COLOR, BARS_COLOR, TEXT_COLOR


class FrequencyChart:
    def __init__(self, parent, title):
        self.container = parent

        self.label = None
        self.fig, self.ax = plt.subplots(figsize=(4, 3), facecolor=BACKGROUND_COLOR)
        self.canvas = FigureCanvasTkAgg(self.fig, master=parent)

        self._build(title)

    def _build(self, title):
        import customtkinter as ctk

        self.label = ctk.CTkLabel(
            self.container,
            text=title,
            font=("JetBrains Mono", 16, "bold")
        )
        self.label.grid(row=0, column=0, pady=(5, 0))

        self.canvas.get_tk_widget().grid(row=1, column=0, sticky="nsew")

        self.update("")

    def update(self, text):
        self.ax.clear()

        text = "".join(filter(str.isalpha, text.upper()))
        counter = collections.Counter(text)

        alphabet = list(string.ascii_uppercase)
        counts = [counter[letter] for letter in alphabet]

        self.ax.set_facecolor(BACKGROUND_COLOR)
        self.ax.bar(alphabet, counts, color=BARS_COLOR)

        self.ax.tick_params(axis='x', colors=TEXT_COLOR, labelsize=7)
        self.ax.tick_params(axis='y', colors=TEXT_COLOR, labelsize=8)

        for spine in self.ax.spines.values():
            spine.set_color(TEXT_COLOR)
            spine.set_linewidth(0.5)

        if max(counts, default=0) < 10:
            self.ax.set_ylim(0, 10)

        self.canvas.draw()
