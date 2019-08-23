Vanilla buffer overflow fuzzing and exploit scripts with the process and workflow built in to speed up the exploit process.
Delete sections of code as the workflow progresses and you are left with a working exploit PoC.

The exploit script requires the user to update certain constants such as overflow lengths and constants but will automtatically calculate lengths for the buffer and payload at each stage based on these input.

Using `bad_chars.py` the exploit script will automatically generate and fetch all characters to be passed to application in debug mode for bad character analysis. Analysis will still be a manual process.

`pattern.py` will automagically generate a non-repeating string to pass to the application. Once the program has crashed and you have copied the hex value of EIP you will need to manually run the below command in order to return the offset loction. 

`root@kali:~# python /opt/pattern.py -l 2800 -q 396C4438`

`[!] Pattern found at: 2606 bytes`

This will need to be entered as the value for the `OVERFLOW_LEN` constant.
`CRASH_LEN` will be the value of the length of the buffer that crashed the program during fuzzing.

NOTE:
1. The exploit script will look for the pattern creation and offset location script (`pattern.py`) and `bad_chars.py` in `/opt` by default.
2. Modify exact paths and arguments based on application in question.
3. `bad_chars.py`  has the following hex characters removed by default: `\x00\x0a\x0d`.
4. `pattern.py` is just a combined python implementation of MSF's `pattern_create.rb` and `pattern_offset.rb` which I just found to be annoyingly slow.
