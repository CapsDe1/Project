import os

def check_fold(directories):
    sbjs_sets = []

    for directory in directories:
        sbjs = []
        for file_name in sorted(os.listdir(directory)):
            if not file_name.endswith('.mat'):
                print(f"'{file_name}' is invalid")
                continue

            key = os.path.splitext(file_name)[0]
            sbjs.append(key.split("_")[0])
        sbjs.append(set(sbjs))

    common_keys = set.intersection(*sbjs_sets) if sbjs_sets else set()

    return common_keys