int total(double *x, int n);

int total(double *x, int n){
	double resposta = 0;
	for(int i = 0; i < n; i++){
		resposta += x[i];
	}
	return resposta;
}
