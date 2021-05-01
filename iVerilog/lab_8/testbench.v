module testbench(opcode, functionCode,IorD,MemRead,MemWrite,MemtoReg,IRWrite,PCSource,ALUSrcB,ALUSrcA,RegWrite,RegDst,PCWrite,PCWriteCond,ALUOp,instruction,register_one,register_two,register_three);
input [31:0]instruction;
  input wire [5:0]opcode;
  input wire [5:0]functionCode; 
  output register_two,register_one,register_three;
  output [2:0]aluOP;
  output IorD,MemRead,MemWrite,MemtoReg,IRWrite,PCSource,ALUSrcB,ALUSrcA,RegWrite,RegDst,PCWrite,PCWriteCond,ALUOp;
  reg[2:0]aluOP;
  reg IorD,MemRead,MemWrite,MemtoReg,IRWrite,PCSource,ALUSrcB,ALUSrcA,RegWrite,RegDst,PCWrite,PCWriteCond,ALUOp;

  reg register_one;
  reg register_two;
  reg register_three;

  instructionfetch obj(opcode, functionCode,IorD,MemRead,MemWrite,MemtoReg,IRWrite,PCSource,ALUSrcB,ALUSrcA,RegWrite,RegDst,PCWrite,PCWriteCond,ALUOp,instruction);

 initial 

  begin 

     

      instruction = 32'b00000010001100101001100000100010;

      opcode = instruction/10000000000000000000000000;

      functionCode =  instruction%10000000000000000000000000;

      $monitor("32bit code=%b, opcode=%b functionCode=%b", instruction,opcode,functionCode);      
     
  end
  endmodule
  