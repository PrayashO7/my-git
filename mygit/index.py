def stage_file(filename, sha):
    with open(".git/index", "a") as index:
        index.write(f"{sha} {filename}\n")

    print("Staged:", filename)
