struct operands{
	int x;
	int y;
};

program SIMP_PROG{
	version SIMP_VERSION{
		int SOM(operands) = 1;
		int MUT(operands) = 2;
		int DIVI(operands) = 3;
		int SUB(operands) = 4;
		int MOD(operands) = 5;
		int POT(operands) = 6;
		int RAIZ(operands) = 7; 
	} = 1;
} = 0x2fffffff;