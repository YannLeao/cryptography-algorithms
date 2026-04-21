import customtkinter as ctk

from config import ALGORITHMS, THEME_PATH
from ui.charts import FrequencyChart
from ui.handlers import encrypt, decrypt, generate_key

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme(str(THEME_PATH))


class CryptoApp(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title("Crypto Algorithm")
        self.geometry("1200x750")

        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.right_panel = ctk.CTkFrame(self, fg_color="transparent")
        self.right_panel.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.right_panel.grid_columnconfigure(0, weight=1)
        self.right_panel.grid_rowconfigure(0, weight=1)
        self.right_panel.grid_rowconfigure(1, weight=1)
        analysis_title = ctk.CTkLabel(
            self.right_panel,
            text="Frequency Analysis",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        analysis_title.grid(row=0, column=0, pady=(10, 20))

        chart_in_container = ctk.CTkFrame(self.right_panel, fg_color="transparent")
        chart_in_container.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        chart_in_container.grid_rowconfigure(0, weight=1)
        chart_in_container.grid_columnconfigure(0, weight=1)

        chart_out_container = ctk.CTkFrame(self.right_panel, fg_color="transparent")
        chart_out_container.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
        chart_out_container.grid_rowconfigure(0, weight=1)
        chart_out_container.grid_columnconfigure(0, weight=1)

        self.algorithm_menu = None
        self.input_text = None
        self.key_frame = None
        self.output_text = None
        self.matrix_container = None
        self.matrix_size = None
        self.key_entry = None
        self.key_dynamic = None
        self.matrix_entries = None

        self.algorithms = ALGORITHMS

        self.create_widgets()
        self.chart_in = FrequencyChart(chart_in_container, "Input char")
        self.chart_out = FrequencyChart(chart_out_container, "Output char")

    def create_widgets(self):
        # Main frame
        main_frame = ctk.CTkScrollableFrame(
            self,
            corner_radius=15,
            height=550
        )
        main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        main_frame.grid_columnconfigure(0, weight=1)

        # Title
        title = ctk.CTkLabel(
            main_frame,
            text="Classical Cryptography",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.grid(row=0, column=0, pady=(10, 20))

        # Algorithm selection
        self.algorithm_menu = ctk.CTkOptionMenu(
            main_frame,
            values=list(ALGORITHMS.keys())
        )
        self.algorithm_menu.grid(row=1, column=0, pady=10)
        self.algorithm_menu.configure(command=self.on_algorithm_change)

        # Input text field
        input_container = ctk.CTkFrame(main_frame, fg_color="transparent")
        input_container.grid(row=2, column=0, sticky="ew", padx=10)
        input_container.grid_columnconfigure(0, weight=1)

        input_label = ctk.CTkLabel(
            input_container,
            text="Input Text",
            font=ctk.CTkFont(size=16, weight="bold"),
            anchor="w"
        )
        input_label.grid(row=0, column=0, sticky="w", pady=(0, 5))

        self.input_text = ctk.CTkTextbox(
            input_container,
            height=120,
            corner_radius=10,
            border_width=2
        )
        self.input_text.grid(row=1, column=0, sticky="ew")

        # Key field
        self.key_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        self.key_frame.grid(row=4, column=0, sticky="ew", padx=10, pady=(10, 5))
        self.key_frame.grid_columnconfigure(0, weight=1)

        key_label = ctk.CTkLabel(
            self.key_frame,
            text="Key",
            font=ctk.CTkFont(size=16, weight="bold"),
            anchor="w"
        )
        key_label.grid(row=0, column=0, sticky="w", pady=(0, 5))

        self.key_dynamic = ctk.CTkFrame(self.key_frame, fg_color="transparent")
        self.key_dynamic.grid(row=1, column=0, sticky="ew")

        self.key_entry = ctk.CTkEntry(
            self.key_dynamic,
            placeholder_text="Enter the encryption key",
            corner_radius=10
        )
        self.key_entry.pack(fill="x")

        generate_btn = ctk.CTkButton(self.key_frame, text="Generate Key", command=lambda: generate_key(self))
        generate_btn.grid(row=2, column=0, pady=10)

        # Buttons
        button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        button_frame.grid(row=5, column=0, pady=10)

        encrypt_btn = ctk.CTkButton(button_frame, text="Encrypt", command=lambda: encrypt(self))
        encrypt_btn.grid(row=0, column=0, padx=10)

        decrypt_btn = ctk.CTkButton(button_frame, text="Decrypt", command=lambda: decrypt(self))
        decrypt_btn.grid(row=0, column=1, padx=10)

        swap_btn = ctk.CTkButton(button_frame, text="⇄", width=40, command=self.swap_text)
        swap_btn.grid(row=0, column=2, padx=5)

        # Output text field
        output_container = ctk.CTkFrame(main_frame, fg_color="transparent")
        output_container.grid(row=6, column=0, sticky="ew", padx=10, pady=(10, 0))
        output_container.grid_columnconfigure(0, weight=1)

        output_label = ctk.CTkLabel(
            output_container,
            text="Result",
            font=ctk.CTkFont(size=16, weight="bold"),
            anchor="w"
        )
        output_label.grid(row=0, column=0, sticky="w", pady=(0, 5))

        self.output_text = ctk.CTkTextbox(
            output_container,
            height=120,
            state="disabled",
            corner_radius=10,
            border_width=2,
        )
        self.output_text.grid(row=1, column=0, sticky="ew")

    def set_output(self, text):
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", str(text))
        self.output_text.configure(state="disabled")

    def set_key_entry(self, key):
        self.key_entry.delete(0, "end")
        self.key_entry.insert(0, str(key))

    def swap_text(self):
        output_text = self.output_text.get("1.0", "end").strip()

        self.input_text.delete("1.0", "end")
        self.input_text.insert("1.0", output_text)
        self.set_output("")

    def render_key_input(self, algorithm):
        for widget in self.key_dynamic.winfo_children():
            widget.destroy()

        if algorithm == "Hill":
            self.render_hill_matrix_input()

        else:
            self.key_entry = ctk.CTkEntry(
                self.key_dynamic,
                placeholder_text="Enter the encryption key",
                corner_radius=10
            )
            self.key_entry.pack(fill="x")

    def on_algorithm_change(self, choice):
        self.render_key_input(choice)

    def render_hill_matrix_input(self):
        size_frame = ctk.CTkFrame(self.key_dynamic, fg_color="transparent")
        size_frame.pack(fill="x", pady=5)

        ctk.CTkLabel(size_frame, text="Matrix Size:").pack(side="left")

        self.matrix_size = ctk.CTkOptionMenu(
            size_frame,
            values=[str(num) for num in list(range(2, 7))]
        )
        self.matrix_size.pack(side="left", padx=10)

        generate_btn = ctk.CTkButton(
            size_frame,
            text="Generate Matrix",
            command=self.generate_matrix_fields
        )
        generate_btn.pack(side="left", padx=10)

        self.matrix_container = ctk.CTkFrame(self.key_dynamic)
        self.matrix_container.pack(pady=10, anchor="center")

    def generate_matrix_fields(self):
        for widget in self.matrix_container.winfo_children():
            widget.destroy()

        size = int(self.matrix_size.get())
        self.matrix_entries = []

        for i in range(size):
            row_entries = []
            for j in range(size):
                entry = ctk.CTkEntry(self.matrix_container, width=60)
                entry.grid(row=i, column=j, padx=5, pady=5)
                row_entries.append(entry)
            self.matrix_entries.append(row_entries)

    def get_matrix_key(self):
        matrix = []
        for row in self.matrix_entries:
            matrix.append([int(entry.get()) for entry in row])
        return matrix

    def set_matrix_key(self, matrix):
        size = len(matrix)

        if not hasattr(self, "matrix_entries") or len(self.matrix_entries) != size:
            self.matrix_size.set(str(size))
            self.generate_matrix_fields()

        for i in range(size):
            for j in range(size):
                self.matrix_entries[i][j].delete(0, "end")
                self.matrix_entries[i][j].insert(0, str(matrix[i][j]))

    def run_analysis(self):
        input_val = self.input_text.get("1.0", "end")
        output_val = self.output_text.get("1.0", "end")

        self.chart_in.update(input_val)
        self.chart_out.update(output_val)
