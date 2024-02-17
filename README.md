## Overview
This Python script can be used to generate finite space filling curves and convert them to tikz code. Currently there is only a hilbert curve implementation, and it can be casted by calling the script with `sys.argv[1]` as the depth `n` of the hilbert curve you want. For instance:

```console
foo@bar:~$ python sfc.py n > output.tikz
```

Note that `n` must be an integer between `1` and `13`.

## Requirements
- Python 3.x