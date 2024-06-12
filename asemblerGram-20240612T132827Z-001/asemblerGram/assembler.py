import plyplus # Importa la librería plyplus para el análisis sintáctico

# Diccionario para la información de las instrucciones
# Se mapean las instrucciones diccionarios para obtener la func3 y func7
# En el caso de las instrucciones tipo U solo se tiene el opcode

# para las instrucciones tipo R
instrucciones_R = {
    'add': {'funct3': '000', 'funct7': '0000000'},
    'sub': {'funct3': '000', 'funct7': '0100000'},
    'sll': {'funct3': '001', 'funct7': '0000000'},
    'slt': {'funct3': '010', 'funct7': '0000000'},
    'sltu': {'funct3': '011', 'funct7': '0000000'},
    'xor': {'funct3': '100', 'funct7': '0000000'},
    'srl': {'funct3': '101', 'funct7': '0000000'},
    'sra': {'funct3': '101', 'funct7': '0100000'},
    'or': {'funct3': '110', 'funct7': '0000000'},
    'and': {'funct3': '111', 'funct7': '0000000'},
    'addw': {'funct3': '000', 'funct7': '0000000'},
    'subw': {'funct3': '000', 'funct7': '0100000'},
    'sllw': {'funct3': '001', 'funct7': '0000000'},
    'srlw': {'funct3': '101', 'funct7': '0000000'},
    'sraw': {'funct3': '101', 'funct7': '0100000'},
}

# para las instrucciones tipo I
instrucciones_I = {
    'addi': {'funct3': '000', 'funct7': ''},
    'slti': {'funct3': '010', 'funct7': ''},
    'sltiu': {'funct3': '011', 'funct7': ''},
    'xori': {'funct3': '100', 'funct7': ''},
    'ori': {'funct3': '110', 'funct7': ''},
    'andi': {'funct3': '111', 'funct7': ''},
    'slli': {'funct3': '001', 'funct7': '0000000'},
    'srli': {'funct3': '101', 'funct7' : '0000000'},
    'srai': {'funct3': '101', 'funct7': '0100000'},
    'addiw': {'funct3': '000', 'funct7': ''},
    'slliw': {'funct3': '001', 'funct7': '0000000'},
    'srliw': {'funct3': '101', 'funct7': '0000000'},
    'sraiw': {'funct3': '101', 'funct7': '0100000'},
    'sd': {'funct3': '011', 'funct7': ''},
    'ld': {'funct3': '010', 'funct7': ''},
    'lw': {'funct3': '010', 'funct7': ''},
    'lh': {'funct3': '001', 'funct7': ''},
    'lb': {'funct3': '000', 'funct7': ''},
    'lbu': {'funct3': '100', 'funct7': ''},
    'lhu': {'funct3': '101', 'funct7': ''},
    'lwu': {'funct3': '110', 'funct7': ''},
    'jalr': {'funct3': '000', 'funct7': ''},
}

# para las instrucciones tipo S
instrucciones_S = {
    'sb': {'funct3': '000'},
    'sh': {'funct3': '001'},
    'sw': {'funct3': '010'},
}

# para las instrucciones tipo SB
instrucciones_SB = {
    'beq': {'funct3': '000'},
    'bne': {'funct3': '001'},
    'blt': {'funct3': '100'},
    'bge': {'funct3': '101'},
    'bltu': {'funct3': '110'},
    'bgeu': {'funct3': '111'},
}

# Para las instrucciones tipo U solo se tiene el opcode
instrucciones_U = {
    'lui': {'opcode': '0110111'},
    'auipc': {'opcode': '0010111'},
}

# Diccionario para los registros
regNames = {
    'zero': 0, 'x0': 0,
    'ra': 1, 'x1': 1,
    'sp': 2, 'x2': 2,
    'gp': 3, 'x3': 3,
    'tp': 4, 'x4': 4,
    't0': 5, 'x5': 5,
    't1': 6, 'x6': 6,
    't2': 7, 'x7': 7,
    's0': 8, 'fp': 8, 'x8': 8,
    's1': 9, 'x9': 9,
    'a0': 10, 'x10': 10,
    'a1': 11, 'x11': 11,
    'a2': 12, 'x12': 12,
    'a3': 13, 'x13': 13,
    'a4': 14, 'x14': 14,
    'a5': 15, 'x15': 15,
    'a6': 16, 'x16': 16,
    'a7': 17, 'x17': 17,
    's2': 18, 'x18': 18,
    's3': 19, 'x19': 19,
    's4': 20, 'x20': 20,
    's5': 21, 'x21': 21,
    's6': 22, 'x22': 22,
    's7': 23, 'x23': 23,
    's8': 24, 'x24': 24,
    's9': 25, 'x25': 25,
    's10': 26, 'x26': 26,
    's11': 27, 'x27': 27,
    't3': 28, 'x28': 28,
    't4': 29, 'x29': 29,
    't5': 30, 'x30': 30,
    't6': 31, 'x31': 31
}

#_________________________________________________________________________________

# Función para guardar las instrucciones binarias en un archivo
def guardarInstruccionesBinario(instrucciones):
    """
    La función se encarga de guardar las instrucciones en binario en un archivo

    Argumentos:
    instrucciones -- Lista de instrucciones en binario

    Retorna:
    La función no retorna nada, guarda las instrucciones en binario en un archivo
    """
    # Se guarda las instrucciones en un archivo binario
    with open('instrucciones.bin', 'w') as archivoBinario:
        for instruccion in instrucciones:
            archivoBinario.write(instruccion + '\n')

# Función para imprimir el contenido de un archivo en binario
def imprimir_binario(instrucciones_binario):
    """
    La función se encarga de imprimir el contenido de un archivo en binario

    Argumentos:
    instrucciones_binario -- Lista de instrucciones en binario

    Retorna:
    La función no retorna nada, imprime el contenido del archivo en binario

    """
    print("\nInstrucciones en binario:")
    for indice, instruccion in enumerate(instrucciones_binario):
        print(f"{indice + 1:0>2} {instruccion}")

# Función para guardar las instrucciones en hexadecimal en un archivo
def guardar_hexadecimal(instrucciones_binario, nombre_archivo):
    """
    La función se encarga de guardar las instrucciones en hexadecimal en un archivo

    Argumentos:
    instrucciones_binario -- Lista de instrucciones en binario
    nombre_archivo -- Nombre del archivo en el que se guardarán las instrucciones en hexadecimal
    
    Retorna:
    La función no retorna nada, guarda las instrucciones en hexadecimal en un archivo

    """
    # Se obtiene el índice más grande de la lista y el número de dígitos del índice más grande
    # para formatear correctamente las líneas y que queden alineadas
    maximo_indice = len(instrucciones_binario) - 1  # El índice más grande de la lista
    maximo_num_digitos = len(str(maximo_indice))  # Número de dígitos del índice más grande

    with open(nombre_archivo, 'w') as archivo:
        for indice, instruccion in enumerate(instrucciones_binario):
            hexadecimal = convertir_a_hexadecimal(instruccion)
            formato_completo = f"{(indice + 1):>{maximo_num_digitos}} {hexadecimal}"
            archivo.write(formato_completo + '\n')

# Función para convertir un número binario a hexadecimal y se formatea
# para que tenga 8 dígitos y esté separado por espacios en grupos de 2
def convertir_a_hexadecimal(binario):
    """
    La función se encarga de convertir un número binario a hexadecimal y formatearlo

    Argumentos:
    binario -- Número binario a convertir
    
    Retorna:
    La función retorna el número binario convertido a hexadecimal y formateado
    """
    # Convertir binario a hexadecimal
    hexadecimal = f"{int(binario, 2):X}"

    # Se ajusta a 8 dígitos, rellenando con ceros a la izquierda si es necesario
    hexadecimal_formateado = f"{hexadecimal:0>8}"
    
    # Formatear en grupos de dos dígitos
    hexadecimal_formateado = " ".join([hexadecimal_formateado[i:i+2] for i in range(0, len(hexadecimal_formateado), 2)])
    
    return hexadecimal_formateado

#_________________________________________________________________________________
# Clase V transfomer para recorrer el árbol y extraer direcciones y labels
class RecolectorDeEtiquetas(plyplus.STransformer):
    def __init__(self):
        """
        Constructor

        Argumentos:
        La función no recibe argumentos

        Retorna:
        La función no retorna nada
        """
        self.direccion_actual = 0
        self.direcciones = {}
    
    def programa(self, nodo):
        """
        La función se encarga de recorrer el árbol y recolectar las etiquetas y direcciones

        Argumentos:
        nodo -- Nodo del árbol

        Retorna:
        La función retorna un diccionario con las etiquetas y direcciones
        """
        # Se recorre el árbol para recolectar las etiquetas y direcciones
        self.recolectar(nodo)
    
    def recolectar(self, nodo):
        for indice, subnodo in enumerate(nodo.tail):
            if subnodo.head == 'label':
                etiqueta = subnodo.tail[0]  # Suponiendo que el nombre de la etiqueta es el primer hijo
                print(f'Etiqueta: {etiqueta} -> Dirección: {self.direccion_actual}')
                self.direcciones[etiqueta] = self.direccion_actual
            elif subnodo.head == 'instruccion':
                self.direcciones[f'instruccion_{indice}'] = self.direccion_actual
                # Se asume que cada instrucción incrementa la dirección en 4 bytes
                self.direccion_actual += 4
        return self.direcciones


# Clase para transformar las instrucciones a binario usando plyplus
class RISC_V_Transformer(plyplus.STransformer):
    def __init__(self, direcciones):
        """
        Constructor

        Argumentos:
        La función no recibe argumentos

        Retorna:
        La función no retorna nada
        """
        self.direcciones = direcciones
        self.direccion_actual = 0
        self.instrucciones_binarias = []
    
    def tipo_r(self, tree):
        """
        La función se encarga de transformar una instrucción tipo R a binario

        Argumentos:
        tree -- Árbol de la instrucción tipo R

        Retorna:
        La función retorna la instrucción en binario
        """
        self.direccion_actual = self.direcciones.get(f'instruccion_{id(tree)}', self.direccion_actual)
        instruccionTest = "Procesando tipo R en dirección {}".format(self.direccion_actual)
        print(instruccionTest)

        # Se extraen los componentes de la instrucción tipo R
        instruccionAssembler = tree.tail[0].tail[0]
        rd_num = regNames.get(tree.tail[1].tail[0], None)
        rs1_num = regNames.get(tree.tail[2].tail[0], None)
        rs2_num = regNames.get(tree.tail[3].tail[0], None)

        rd = tree.tail[1].tail[0]
        rs1 = tree.tail[2].tail[0]
        rs2 = tree.tail[3].tail[0]

        # Encuentra los códigos binarios correspondientes
        # Se asume que todas las instrucciones tipo R tienen el mismo opcode
        opcode = '0110011'

        # Se obtienen los valores de funct3 y funct7 para la instrucción específica
        if instruccionAssembler in instrucciones_R:
            funct3 = instrucciones_R[instruccionAssembler]['funct3']
            funct7 = instrucciones_R[instruccionAssembler]['funct7']
        else:
            raise ValueError(f"Instrucción no soportada: {instruccionAssembler}")

        # Se construye la representación binaria completa
        binary_instr = self.convertir_a_binarioR(opcode, funct3, funct7, rd_num, rs1_num, rs2_num)
        print(f"{instruccionAssembler} {rd}, {rs1}, {rs2} -> {binary_instr}")
        self.instrucciones_binarias.append(binary_instr)
        self.direccion_actual += 4
        return binary_instr
        
    def convertir_a_binarioR(self, opcode, funct3, funct7, rd, rs1, rs2):
        # Lógica específica para convertir una instrucción tipo R a binario.
        # Convertir los registros a binario
        rd_bin = format(int(rd), '05b')
        rs1_bin = format(int(rs1), '05b')
        rs2_bin = format(int(rs2), '05b')

        # Se construye la representación binaria
        binario = f"{funct7}{rs2_bin}{rs1_bin}{funct3}{rd_bin}{opcode}"
        return binario
    
    def tipo_i_operacion(self, tree):
        """
        La función se encarga de transformar una instrucción tipo I de operación a binario

        Argumentos:
        tree -- Árbol de la instrucción tipo I de operación

        Retorna:
        La función retorna la instrucción en binario
        """
        self.direccion_actual = self.direcciones.get(f'instruccion_{id(tree)}', self.direccion_actual)
        instruccionTest = "Procesando tipo I de operación en dirección {}".format(self.direccion_actual)
        print(instruccionTest)

        # Extrae los componentes de la instrucción tipo I
        instruccionAssembler = tree.tail[0].tail[0]
        rd_num = regNames.get(tree.tail[1].tail[0], None)
        rs1_num = regNames.get(tree.tail[2].tail[0], None)
        inmediato = tree.tail[3].tail[0]

        rd = tree.tail[1].tail[0]
        rs1 = tree.tail[2].tail[0]

        # Se obtienen los valores de funct3 y funct7 para la instrucción específica
        if instruccionAssembler in instrucciones_I:
            funct3 = instrucciones_I[instruccionAssembler]['funct3']
            funct7 = instrucciones_I[instruccionAssembler]['funct7']
        else:
            raise ValueError(f"Instrucción no soportada: {instruccionAssembler}")

        # Se construye la representación binaria completa
        binary_instr = self.convertir_a_binario_i(instruccionAssembler, funct3, funct7, rd_num, rs1_num, inmediato)
        print(f"{instruccionAssembler} {rd}, {rs1}, {inmediato} -> {binary_instr}")
        self.instrucciones_binarias.append(binary_instr)
        self.direccion_actual += 4
        return binary_instr

    def tipo_i_carga(self, tree):
        """
        La función se encarga de transformar una instrucción tipo I de carga a binario

        Argumentos:
        tree -- Árbol de la instrucción tipo I de carga

        Retorna:
        La función retorna la instrucción en binario
        """
        self.direccion_actual = self.direcciones.get(f'instruccion_{id(tree)}', self.direccion_actual)
        instruccionTest = "Procesando tipo I de carga en dirección {}".format(self.direccion_actual)
        print(instruccionTest)

        # Se extraen los componentes de la instrucción tipo I
        instruccionAssembler = tree.tail[0].tail[0]
        rd_num = regNames.get(tree.tail[1].tail[0], None) # Registro destino
        inmediato = tree.tail[2].tail[0].tail[0] # Valor inmediato (parte del offset)
        inm_valor = int(inmediato)
        rs1_num = regNames.get(tree.tail[2].tail[1].tail[0], None) # Registro base

        rd = tree.tail[1].tail[0] # Registro destino
        rs1 = tree.tail[2].tail[1].tail[0] # Registro base

        # Se obtienen los valores de funct3 y funct7 para la instrucción específica
        if instruccionAssembler in instrucciones_I:
            funct3 = instrucciones_I[instruccionAssembler]['funct3']
            funct7 = instrucciones_I[instruccionAssembler]['funct7']
        else:
            raise ValueError(f"Instrucción no soportada: {instruccionAssembler}")

        # Se construye la representación binaria completa
        binary_instr = self.convertir_a_binario_i(instruccionAssembler, funct3, funct7, rd_num, rs1_num, inm_valor)
        print(f"{instruccionAssembler} {rd}, {inmediato}({rs1}) -> {binary_instr}")
        self.instrucciones_binarias.append(binary_instr)
        self.direccion_actual += 4
        return binary_instr
    
    def tipo_i_salto(self, tree):
        """
        La función se encarga de transformar una instrucción tipo I de salto a binario

        Argumentos:
        tree -- Árbol de la instrucción tipo I de salto

        Retorna:
        La función retorna la instrucción en binario
        """
        self.direccion_actual = self.direcciones.get(f'instruccion_{id(tree)}', self.direccion_actual)
        instruccionTest = "Procesando tipo I de salto en dirección {}".format(self.direccion_actual)
        print(instruccionTest)

        # Se extraen los componentes de la instrucción tipo I
        instruccionAssembler = tree.tail[0].tail[0]
        rd_num = regNames.get(tree.tail[1].tail[0], None)
        rs1_num = regNames.get(tree.tail[2].tail[0], None)
        label = tree.tail[3].tail[0] # Label de la instrucción

        rd = tree.tail[1].tail[0]
        rs1 = tree.tail[2].tail[0]

        # Se obtienen los valores de funct3 y funct7 para la instrucción específica
        if instruccionAssembler in instrucciones_I:
            funct3 = instrucciones_I[instruccionAssembler]['funct3']
            funct7 = instrucciones_I[instruccionAssembler]['funct7']
        else:
            raise ValueError(f"Instrucción no soportada: {instruccionAssembler}")

        # Se obtiene la dirección de la etiqueta del diccionario
        direccion_destino = self.direcciones.get(label, None)
        print(f"Dirección destino de la etiqueta {label}: {direccion_destino}")
        if direccion_destino is None:
            raise ValueError(f"La etiqueta {label} no está definida")

        # Se calcula el offset
        offset = direccion_destino - self.direccion_actual
        
        # Se verifica que los registros fuente y destino están en el rango permitido (0-31)
        if not (0 <= int(rd_num) <= 31):
            raise ValueError(f"Registro destino rs1 inválido: {rs1}")
        
        if not (0 <= int(rs1_num) <= 31):
            raise ValueError(f"Registro fuente rs2 inválido: {rs1}")

        # Se construye la representación binaria completa
        binary_instr = self.convertir_a_binario_i(instruccionAssembler, funct3, funct7, rd_num, rs1_num, offset)
        print(f"{instruccionAssembler} {rd}, {rs1}, {offset} -> {binary_instr}")
        self.instrucciones_binarias.append(binary_instr)
        self.direccion_actual += 4
        return binary_instr

    def convertir_a_binario_i(self, instruccionAssembler, funct3, funct7, rd, rs1, imm):
        # Lógica específica para convertir una instrucción tipo I a binario.
        # Convertir los registros a binario

        # Encuentra los códigos binarios correspondientes
        # Se asigna el vaor de opcode dependiendo de la instrucción específica tipo I
        if instruccionAssembler == 'jalr':
            opcode = '1100111'
        elif instruccionAssembler in ['ld', 'lw', 'lh', 'lb', 'lbu', 'lhu', 'lwu']:
            opcode = '0000011'
        else:
            opcode = '0010011'

        if funct7:  # Si funct7 no está vacío
            # Se convierte a binario el valor de imm para poder concatenarlo con funct7
            imm = int(imm)
            imm_temp = format(imm, '05b')
            imm_bin = format(int(funct7 + imm_temp, 2), '012b')
        else:
            # Se ajusta imm a 12 bits
            imm_temp = int(imm)
            imm_bin = format(imm_temp if imm_temp >= 0 else (2**12 + imm_temp), '012b')

        rd_bin = format(int(rd), '05b')
        rs1_bin = format(int(rs1), '05b')

        # Se construye la representación binaria
        binario = f"{imm_bin}{rs1_bin}{funct3}{rd_bin}{opcode}"
        return binario

    def tipo_s(self, tree):
        """
        Se encarga de procesar las instrucciones tipo S y convertirlas a binario

        Argumentos:
        tree -- árbol con los campos de la instrucción a procesar
    
        Retorna:
        La función retorna la instrucción en binario
        """
        self.direccion_actual = self.direcciones.get(f'instruccion_{id(tree)}', self.direccion_actual)
        instruccionTest = "Procesando tipo S en dirección {}".format(self.direccion_actual)
        print(instruccionTest)

        # Se extraen los componentes de la instrucción tipo S
        instruccionAssembler = tree.tail[0].tail[0]
        rs2_num = regNames.get(tree.tail[1].tail[0], None) # Registro fuente
        inm = tree.tail[2].tail[0].tail[0] # Valor inmediato (parte del offset)
        inmediato = int(inm)
        rs1_num =  regNames.get(tree.tail[2].tail[1].tail[0], None) # Registro base

        rs2 = tree.tail[1].tail[0] # Registro fuente
        rs1 =  tree.tail[2].tail[1].tail[0] # Registro base
        
        #Ejemplo 1: sw x5, 4(x10)
        # Se verifica que los registros fuente y destino están en el rango permitido (0-31)
        if not (0 <= int(rs1_num) <= 31):
            raise ValueError(f"Registro destino rs1 inválido: {rs1}")
        
        if not (0 <= int(rs2_num) <= 31):
            raise ValueError(f"Registro fuente rs2 inválido: {rs2}")
    
        # Se verifica que el valor inmediato está en el rango permitido (-2048 a 2047)
        if not (-2048 <= int(inmediato) <= 2047):
            raise ValueError(f"Valor inmediato = {inmediato}. Debe estar entre -2048 y 2047")

        # Se asume que todas las instrucciones tipo S tienen el mismo opcode
        opcode = '0100011'

        # Se obtienen los valores de funct3 para la instrucción específica
        if instruccionAssembler in instrucciones_S:
            funct3 = instrucciones_S[instruccionAssembler]['funct3']
        else:
            raise ValueError(f"Instrucción no soportada: {instruccionAssembler}")
        
        # Se construye la representación binaria completa
        binary_instr = self.convertir_a_binario_s(funct3, rs2_num, rs1_num, inmediato, opcode)
        print(f"{instruccionAssembler} {rs2}, {inmediato}({rs1}) -> {binary_instr}")
        self.instrucciones_binarias.append(binary_instr)
        self.direccion_actual += 4
        return binary_instr

    def convertir_a_binario_s(self, funct3, rs2, rs1, inm, opcode):
        # Se ajusta imm a 12 bits
        inm_bin = format(inm if inm >= 0 else (2**12 + inm), '012b')
        inm_11_5 = inm_bin[0:7]
        inm_4_0 = inm_bin[7:12]
    
        rs1 = format(int(rs1), '05b')
        rs2 = format(int(rs2), '05b')

        # Se construye la representación binaria
        binario = f"{inm_11_5}{rs2}{rs1}{funct3}{inm_4_0}{opcode}"
        return binario

    def tipo_u(self, tree):
        """
        Se encarga de procesar las instrucciones tipo U y convertirlas a binario

        Argumentos:
        tree -- árbol con los campos de la instrucción a procesar
    
        Retorna:
        La función retorna la instrucción en binario
        """
        self.direccion_actual = self.direcciones.get(f'instruccion_{id(tree)}', self.direccion_actual)
        instruccionTest = "Procesando tipo U en dirección {}".format(self.direccion_actual)
        print(instruccionTest)

        # Extrae los componentes de la instrucción tipo U
        instruccionAssembler = tree.tail[0].tail[0]
        rd_num = regNames.get(tree.tail[1].tail[0], None) # Registro destino
        inm = tree.tail[2].tail[0] # Valor inmediato
        inmediato = int(inm)

        rd = tree.tail[1].tail[0] # Registro destino

        # Se verifica que el registro fuente están en el rango permitido (0-31)
        if not (0 <= int(rd_num) <= 31):
            raise ValueError(f"Registro destino rd inválido: {rd}")
    
        # Se verifica que el valor inmediato está en el rango permitido (-4096 y 4096)
        if not (0 <= inmediato <= 1048575):
            raise ValueError(f"Valor inmediato = {inmediato}. Debe estar entre 0 y 1048575")

        # Se obtienen los valores de opcode para la instrucción específica
        if instruccionAssembler in instrucciones_U:
            opcode = instrucciones_U[instruccionAssembler]['opcode']
        else:
            raise ValueError(f"Instrucción no soportada: {instruccionAssembler}")
        
        # Se construye la representación binaria completa
        binary_instr = self.convertir_a_binario_u(opcode, rd_num, inmediato)
        print(f"{instruccionAssembler} {rd}, {inmediato} -> {binary_instr}")
        self.instrucciones_binarias.append(binary_instr)
        self.direccion_actual += 4
        return binary_instr

    def convertir_a_binario_u(self, opcode, rd, inmediato):
        # Se ajusta imm a 20 bits
        imm_bin = format(int(inmediato), '020b')
        rd = format(int(rd), '05b')

        # Se construye la representación binaria
        binario = f"{imm_bin}{rd}{opcode}"
        return binario

#_________________________________________________________________________________

# Función principal
def main():
    # Carga la gramática y parsea el archivo
    with open('riscv.g', 'r') as archivoGramatica:
        #grammar_text = archivoGramatica.read()
        with open('input.asm', 'r') as archivoASM:
            gramatica = plyplus.Grammar(archivoGramatica)
            codigoFuente = archivoASM.read()
            arbolParse = gramatica.parse(codigoFuente)

            # Genera y guarda el árbol en formato PNG
            # arbolParse.to_png_with_pydot(r'arbolParser.png')

            # Se extraen las direcciones de las etiquetas
            # Primera pasada para recolectar etiquetas y direcciones
            recolector = RecolectorDeEtiquetas()
            recolector.transform(arbolParse)
            direcciones = recolector.direcciones

            # Transforma el árbol según las definiciones de RISC_V_Transformer
            convertidorAssembler = RISC_V_Transformer(direcciones) # Instancia del objeto convertidorAssembler
            convertidorAssembler.transform(arbolParse)

            # Se imprimen las instrucciones en binario
            imprimir_binario(convertidorAssembler.instrucciones_binarias)

            # Se guardan las instrucciones en binario en un archivo
            guardarInstruccionesBinario(convertidorAssembler.instrucciones_binarias)

            # Se guardan las instrucciones en hexadecimal en un archivo
            guardar_hexadecimal(convertidorAssembler.instrucciones_binarias, 'out.hex')
            

if __name__ == '__main__':
    main()
