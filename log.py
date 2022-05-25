import subprocess as sp
from concurrent.futures import ThreadPoolExecutor

def log_popen_pipe(p, stdfile):

    with open("/log/owa.log", "w") as f:

        while p.poll() is None:
            f.write(stdfile.readline())
            f.flush()

        # Write the rest from the buffer
        f.write(stdfile.read())

with sp.Popen(
    ["python3", "-m" , "flask", "run", "--host=0.0.0.0"],stdout=sp.PIPE,stderr=sp.PIPE,text=True,
) as p:

    with ThreadPoolExecutor(2) as pool:
        r1 = pool.submit(log_popen_pipe, p, p.stdout)
        r2 = pool.submit(log_popen_pipe, p, p.stderr)
        r1.result()
        r2.result()
