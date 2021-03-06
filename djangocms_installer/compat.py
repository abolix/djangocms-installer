import subprocess


def clean(value):
    if value and isinstance(value, str):
        return value.strip()
    else:
        return value


if "check_output" not in dir(subprocess):

    def f(*popenargs, **kwargs):
        if "stdout" in kwargs:
            raise ValueError("stdout argument not allowed, it will be overridden.")
        process = subprocess.Popen(stdout=subprocess.PIPE, *popenargs, **kwargs)
        output, unused_err = process.communicate()
        retcode = process.poll()
        if retcode:
            cmd = kwargs.get("args")
            if cmd is None:
                cmd = popenargs[0]
            raise subprocess.CalledProcessError(retcode, cmd)
        return output

    subprocess.check_output = f
