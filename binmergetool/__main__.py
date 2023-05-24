from binmergetool.binmergetool import BinMergeTool
import argparse

if __name__ == "__main__":
    """
    Entry point when running the program as a module
    """
    
    parser = argparse.ArgumentParser()
    parser.add_argument("file1", help="First file")
    parser.add_argument("file2", help="Second file")
    parser.add_argument("offset", help="Offset at which the second file should start")
    parser.add_argument("padding_symbol", help="Padding symbol between file1 and file2")
    parser.add_argument("outfile", help="Output file")
    args = parser.parse_args()

    with open(args.file1, "rb") as f:
        data1 = f.read()

    with open(args.file2, "rb") as f:
        data2 = f.read()

    # TODO add padding symbol parsing

    bmt = BinMergeTool(data1=data1, data2=data2, offset=int(args.offset))

    with open(args.outfile, "wb") as f:
        f.write(bmt.merge())
