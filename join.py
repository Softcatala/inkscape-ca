import os.path


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def main():

    header_len = file_len("header.po")
    start_line = 0
    
    with open("ca-translated.po", "w") as fh_out:
        for file_num in range(1, 20):        
            fn = f"part-{file_num}.po"
            if not os.path.isfile(fn):
                break
                
            if file_num > 1:
                start_line = header_len

            with open(fn, "r") as fh_in:
                for line in fh_in.readlines()[start_line:]:
                    fh_out.write(line)
                    
                print(f"Read {fn}")  
                
    
if __name__ == "__main__":
    print("Joins multiple parts into a single file")
    main()
