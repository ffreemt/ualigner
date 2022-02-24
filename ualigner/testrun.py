"""Testrun model_s clas-l-user.

python -c "from model_pool import load_model_s; model_s=load_model_s
(); print(model_s.encode('a').shape)"  

python -c "from model_pool import load_model; clas=load_model('clas-l-user'); print(clas('make', ['made', 'machen', 'machten']))"
"""
# pylint: disable=line-too-long, trailing-whitespace

from time import perf_counter
from icecream import ic
from model_pool import load_model_s, load_model

model_s = load_model_s()
clas = load_model("clas-l-user")


def main():
    """Run main."""
    then = perf_counter()
    ic(model_s.encode('a').shape)
    print(f"time elapsed: {perf_counter() - then:.2f}s")
    then = perf_counter()
    ic(clas('make', ['made', 'machen', 'machten']))
    print(f"time elapsed: {perf_counter() - then:.2f}s")


if __name__ == "__main__":
    main()
