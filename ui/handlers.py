def encrypt(app):
    text = app.input_text.get("1.0", "end").strip()
    algorithm = app.algorithm_menu.get()
    algo = app.algorithms.get(algorithm)
    key = app.key_entry.get() if algorithm != "Hill" else app.get_matrix_key()

    if algo is None:
        app.set_output("Algorithm not yet implemented")
        return

    try:
        result = algo["encrypt"](text, key)
        app.set_output(result)
        app.run_analysis()

    except Exception as e:
        app.set_output(f"Error: {str(e)}")


def decrypt(app):
    text = app.input_text.get("1.0", "end").strip()
    algorithm = app.algorithm_menu.get()
    algo = app.algorithms.get(algorithm)
    key = app.key_entry.get() if algorithm != "Hill" else app.get_matrix_key()

    if algo is None:
        app.set_output("Algorithm not yet implemented")
        return

    try:
        result = algo["decrypt"](text, key)
        app.set_output(result)
        app.run_analysis()

    except Exception as e:
        app.set_output(f"Error: {str(e)}")


def generate_key(app):
    algorithm = app.algorithm_menu.get()
    algo = app.algorithms.get(algorithm)

    if algo is None:
        app.set_output("Algorithm not yet implemented")
        return

    try:
        if algorithm == "Hill":
            size = int(app.matrix_size.get())
            key = algo["generate_key"](size)
            app.set_matrix_key(key)
        else:
            key = algo["generate_key"]()
            app.set_key_entry(key)

    except Exception as e:
        app.set_output(f"Error: {str(e)}")
