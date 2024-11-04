def save_meta(meta_path_save, meta):
    with open(meta_path_save, 'w') as file:
        for key, value in meta.items():
            file.write(f"{key}: {value}\n")
            print(f"{key}: {value}")

    print(f"'{meta_path_save}' saved.")