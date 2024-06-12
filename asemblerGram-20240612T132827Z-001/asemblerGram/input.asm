	addi    x10, x0, 0 ; Instrucción tipo I de operación inmediata
    	lw      x8, -32(x2) # Instrucción tipo I de carga con inmediato negativo
    	lw      x1, 28(x2) # Instrucción tipo I de carga con inmediato positivo
    	addi    x2, sp, 32 ; Instrucción tipo I de operación inmediata
	addi    x2, x7, -32
    	add ra, x2, gp ; Instrucción tipo R
		lui a0, 1000 # Instrucción tipo U de carga con inmediato
		sw x1, 28(sp) # Instrucción tipo S de almacenamiento con inmediato positivo

