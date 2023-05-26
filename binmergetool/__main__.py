from binmergetool.binmergetool import BinMergeTool
import argparse
import struct

if __name__ == "__main__":
    """
    Entry point when running the program as a module
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("file1", help="First file")
    parser.add_argument("file2", help="Second file")
    parser.add_argument("offset", help="Offset at which the second file should start")
    parser.add_argument(
        "padding_symbol", help="Padding symbol between file1 and file2", default="0xFF"
    )
    parser.add_argument("outfile", help="Output file", default="merged.bin")
    args = parser.parse_args()

    with open(args.file1, "rb") as f:
        data1 = f.read()

    with open(args.file2, "rb") as f:
        data2 = f.read()

    offset = int(args.offset, 16)
    padding_symbol = struct.pack("B", int(args.padding_symbol, 16))

    bmt = BinMergeTool(
        data1=data1, data2=data2, offset=offset, padding_symbol=padding_symbol
    )

    with open(args.outfile, "wb") as f:
        f.write(bmt.merge())
