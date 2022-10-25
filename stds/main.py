# Leave these lines untouched
__winc_id__ = "8c2e6882503c4baa9ce2e050497c3f2f"
__human_name__ = "stds"

# Your code here

import sys

def main():
    # TODO: read text from stdin
    List=[]
    file1 =sys.stdin
    for line in file1:
    # TODO: Filter character given as an argument from the text
        strNew = line.replace(sys.argv[1], "")
    # TODO: Print the result to stdoutcat random.txt | python main.py a | head -n 1
        sys.stdout.write(strNew)
    # TODO: Print the total number of removed characters to stderr
        List.append(len(line)-(len(strNew)))
    sys.stderr.write(str(sum(List)))
    ...


if __name__ == "__main__":
    main()
