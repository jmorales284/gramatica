start: programa;

programa: (label | instruccion )+;

instruccion:
      tipo_r
    | tipo_i
    | tipo_s
    | tipo_sb
    | tipo_u
    | tipo_uj;

tipo_r: instr_r regname ',' regname ',' regname;

tipo_i: tipo_i_operacion | tipo_i_carga | tipo_i_salto;

tipo_i_operacion: instr_i_oper regname ',' regname ',' imm;
tipo_i_carga: instr_i_carga regname ',' offset;
tipo_i_salto: instr_i_salto regname ',' regname ',' label;

tipo_s: instr_s regname ',' offset;
tipo_sb: instr_sb regname ',' regname ',' label;
tipo_u: instr_u regname ',' imm;
tipo_uj: instr_uj regname ',' label;

offset: imm '\(' regname '\)';

imm: VAL;

VAL: '[0]|(\-|\+)?[1-9][0-9]*';


instr_r: 'add' | 'sub' | 'sll' | 'slt' | 'sltu' | 'xor' | 'or' | 'srl' | 'sra' | 'and';
instr_i_oper: 'addi' | 'xori' | 'ori' | 'andi' | 'slli' | 'srli' | 'srai' | 'slti' | 'sltiu' ;
instr_i_carga: 'lb' | 'lh' | 'lw' | 'lbu' | 'lhu' ;
instr_i_salto: 'jalr';
instr_s: 'sb' | 'sh' | 'sw';
instr_sb: 'beq' | 'bne' | 'blt' | 'bge' | 'bltu' | 'bgeu';
instr_u: 'lui' | 'auipc';
instr_uj: 'jal';

regname: 
    'x0' | 'zero'| 'x1' | 'x2' | 'x3' | 'x4' | 'x5' | 'x6' | 'x7' | 'x8' | 'x9' | 'x10'
  | 'ra' | 'sp' | 'gp' | 'tp' | 't0' | 't1' | 't2' | 't3' | 't4' | 't5' | 't6' | 't7' | 't8' | 't9'
  | 's0' | 's1' | 's2' | 's3' | 's4' | 's5' | 's6' | 's7' | 's8' | 's9' | 's10' | 's11'
  | 'k0' | 'k1' | 'a0' | 'a1' | 'a2' | 'a3' | 'a4' | 'a5' | 'a6' | 'a7'
  | 'x11'| 'x12' | 'x13' | 'x14' | 'x15' | 'x16' | 'x17' | 'x18' | 'x19' | 'x20'
  | 'x21' | 'x22' | 'x23' | 'x24' | 'x25' | 'x26' | 'x27' | 'x28' | 'x29' | 'x30' | 'x31' ;


label: '[a-zA-Z_][a-zA-Z0-9_]+:';

// Definición de comentarios y espacios en blanco
COMMENT: '(;|#)[^\n]*' (%ignore);
WS: '[ \t\r\n]+' (%ignore);
