Win32 buffer overflow fuzzing and exploit scripts with the process and workflow built in to speed up the exploit process.
Delete sections of code the workflow progresses and you are left with a working (hopefully) PoC.

Th exploit script requires the user to update certain constants such as overflow lengths and constants but will automtatically calculate lengths for the buffer and payload at each stage based on these input.
