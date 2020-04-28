# CTypes
## Usando c++ para acelerar o Python

### Como usar
```$ from total import *```
```$ import numpy as np```
```$ n = 1000```
```$ x = np.arrange(n, dtype=double)```
```$ totalCtypes(x, n)```
```4970```

### Compilando usando o GCC
```gcc -fPIC -02 -c fib.c```

### Isso vai gerar um ```fib.o```
```gcc -shared fib.o -o _fib.so```

### Por fim, para efeito de comparação, comente o código  e rode:
### Normal, com Numpy e com CTypes
```time python3 fib.py```


