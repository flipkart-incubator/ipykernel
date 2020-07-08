"""Entry point for launching an IPython kernel.

This is separate from the ipykernel package so we can avoid doing imports until
after removing the cwd from sys.path.
"""

import sys

if __name__ == '__main__':
    # Remove the CWD from sys.path while we load stuff.
    # This is added back by InteractiveShellApp.init_path()
    if sys.path[0] == '':
        del sys.path[0]

    from ipykernel.kernelapp import IPKernelApp
    from ipykernel.readonly_pythonkernel import ReadOnlyKernel

    IPKernelApp.launch_instance(kernel_class=ReadOnlyKernel)
