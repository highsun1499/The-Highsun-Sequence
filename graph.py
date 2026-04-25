import sympy as sp
import ipywidgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt

# 소수 500개 미리 뽑아놓기
primes = list(sp.primerange(1, sp.prime(1000) + 1))

def plot_formula(n):
    a_vals =[]
    # 파이썬의 문자열 합치기 신공(math보다 1000배 빠름)
    for i in range(1, n + 1):
        s = "".join(str(p) for p in reversed(primes[:i]))
        a_vals.append(1.0 / float("0." + s[:17]))
    
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, n + 1), a_vals, '-o', color='gold', markersize=4)
    plt.axhline(y=10.0, color='red', linestyle='--', alpha=0.5)
    plt.axhline(y=1.0, color='red', linestyle='--', alpha=0.5)
    plt.ylim(0, 11)
    plt.xlim(0, n + 1)
    plt.title(f"n={n} Oscillation Graph", color='white')
    ax = plt.gca()
    ax.set_facecolor('#111')
    ax.grid(color='gray', alpha=0.3)
    plt.show()

# 슬라이더 만들기
slider = widgets.IntSlider(value=10, min=1, max=1000, step=1, description='n Value:')
widgets.interact(plot_formula, n=slider)
