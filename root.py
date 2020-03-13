import fileinput

def main():
    lines = []
    for line in fileinput.input():
        cleaned = line.replace('\n', '') ## REVIEW: problem if any field is allowed to have \n
        lines.append(cleaned)

    print(lines)

if __name__== "__main__":
    main()
