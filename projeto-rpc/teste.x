struct operands{
	int x;
	int y;
};

program SIMP_PROG{
	version SIMP_VERSION{
		int som(operands) = 1;
		int mut(operands) = 2;
		int div(operands) = 3;
		int sub(operands) = 4;
		int mod(operands) = 5;
		int pot(operands) = 6;
		int raz(operands) = 7; 
	} = 1;
} = 0x2fffffff;
