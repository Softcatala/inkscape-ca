
def _get_file_handle(file_num):
    fn = f"part-{file_num}.po"
    fh_out = open(fn, "w")                
    print(f"writting '{fn}'")
    return fh_out

def main():
    
    file_num = 1
    lines = 0
    with open("ca.po") as fh_in:
        fh_out = _get_file_handle(file_num)
        for line in fh_in.readlines():
            if lines > 10000: 
                if len(line.strip()) == 0:
                    lines = 0
                    file_num += 1
                    fh_out = _get_file_handle(file_num)

            fh_out.write(line)
            lines += 1
if __name__ == "__main__":
    main()
