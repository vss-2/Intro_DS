# CTypes
## Usando C++ para acelerar o Python

### Como usar
```py
from total import *
import numpy as np
n = 1000
x = np.arrange(n, dtype=double)
totalCtypes(x, n)
```

### Compilando usando o GCC
```gcc -fPIC -02 -c fib.c```

### Isso vai gerar o ```fib.o```
```gcc -shared fib.o -o _fib.so```

### Por fim, para efeito de comparação, comente o código  e rode:
### Normal, com Numpy e com CTypes
```time python3 fib.py```


