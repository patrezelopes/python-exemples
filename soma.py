from random import randint
import time
from plotnine import ggplot, aes, geom_line
import pandas as pd


def get_time(method):
    def alg_time(*args, **kwargs):
        start = time.time()
        result = method(*args, **kwargs)
        end = time.time()
        timestamp = end - start

        return result, timestamp

    return alg_time


@get_time
def tem_soma(vetor, target):
    vetor = set(vetor)
    vetor = tuple(vetor)
    complemtento = {
    }

    for i in range(len(vetor)):
        x = vetor[i]

        if x in complemtento:
            return (complemtento[x], i)
        elif x < target:
            complemtento[target - x] = i

    return (-1, -1)


@get_time
def tem_soma_bb(vetor, target):
    vetor = set(vetor)
    vetor = sorted(vetor)
    vetor = tuple(vetor)
    com = {}

    i = 0

    while vetor[i] < target:
        x = vetor[i]
        y = target - x

        if x in com:
            return (y, x)
        else:
            com[y] = x

        i += 1

    return None


metricas = {
    "algoritmo": [],
    "amostra": [],
    "tempo (s)": []
}

for i in range(10 ** 6, 41 * 10 ** 6, 10 ** 6):
    vetor = [randint(11, 100) for i in range(i)]
    vetor += [1, 8]
    vetor2 = vetor.copy()

    _, timestamp_tem_soma_1 = tem_soma(vetor, 9)
    _, timestamp_tem_soma_2 = tem_soma_bb(vetor2, 9)

    metricas["algoritmo"] += ["soma", "soma_bb"]
    metricas["amostra"] += [i, i]
    metricas["tempo (s)"] += [timestamp_tem_soma_1, timestamp_tem_soma_2]

    print(i, "soma", timestamp_tem_soma_1)
    print(i, "soma_bb", timestamp_tem_soma_2)

df = pd.DataFrame(metricas)
fig = ggplot(df, aes(x="amostra", y="tempo (s)", colour="algoritmo")) + geom_line()

fig.save("metricas.png")