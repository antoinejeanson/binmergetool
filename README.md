# binmergetool
Simple tool for merging two binary files together.

# Install

    pip install binmergetool

# Usage

## Example: merging Arduino bootloader with application code

In this example, we'll add the Arduino bootloader to a compiled binary file for one-step flashing of microcontrollers.
Application code starts at 0x2000 so we set this as the offset.

    python -m binmergetool bootloader.bin application.bin 0x2000 0xFF application_with_bootloader.bin

