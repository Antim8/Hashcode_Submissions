def create_output_file(projects: list, submission: char) -> None:
    with open(os.path.join(os.path.dirname(__file__), "output", submission), "w") as f:
        solution = str(len(projects))
        for i in projects:
            for j in i:
                solution += "\n{}".format(j)
                
        f.write(solution)