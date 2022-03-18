def fibonacci(quant, sequencia=(0,1)):
    if len(sequencia) >= quant:
        return sequencia
    return fibonacci(quant, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib)