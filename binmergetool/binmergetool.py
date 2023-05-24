import logging


class BinMergeTool:
    def __init__(
        self, data1: bytes, data2: bytes, offset: int, padding_symbol: bytes = b"\xff"
    ) -> None:
        """
        Creates a BinMergeTool instance.
        Provide the class with a logger and read input binary files files.

        Args:
            - data1: First file (beginning of output)
            - data2: Second file (end of output)
            - offset: Byte at which the second file should start
            - padding_symbol: Space between file1 and file2 will be padded with this
            symbol.
        """

        self.logger = logging.getLogger(__name__)

        if len(data1) > offset:
            raise ValueError("Offset is smaller than first binary.")

        if len(padding_symbol) > 1:
            raise ValueError("Padding symbol should be a single byte.")

        self.data1 = data1
        self.data2 = data2

        self.offset = offset
        self.padding_symbol = padding_symbol

    def merge(self) -> bytes:
        """
        Merge the two input binaries.

        Returns:
            The bytes of the merged binaries
        """

        output = self.data1

        while len(output) < self.offset:
            output += self.padding_symbol

        output += self.data2

        return output
