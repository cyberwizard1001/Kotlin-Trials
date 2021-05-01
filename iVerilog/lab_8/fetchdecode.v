module instructionfetch(opcode, functionCode,IorD,MemRead,MemWrite,MemtoReg,IRWrite,PCSource,ALUSrcB,ALUSrcA,RegWrite,RegDst,PCWrite,PCWriteCond,ALUOp,instruction);
input [31:0]instruction;
  input wire [5:0]opcode;
  input wire [5:0]functionCode; 
  output [2:0]aluOP;
  output IorD,MemRead,MemWrite,MemtoReg,IRWrite,PCSource,ALUSrcB,ALUSrcA,RegWrite,RegDst,PCWrite,PCWriteCond,ALUOp;
  reg[2:0]aluOP;
  reg IorD,MemRead,MemWrite,MemtoReg,IRWrite,PCSource,ALUSrcB,ALUSrcA,RegWrite,RegDst,PCWrite,PCWriteCond,ALUOp;
  
  

  always @(opcode[5:0] or functionCode[5:0])
  begin

  
	IorD=1'b0; MemRead=1'b0; MemWrite=1'b0; MemtoReg=1'b0; IRWrite=1'b0; PCSource=1'b0;
	ALUSrcB=2'b00; ALUSrcA=1'b0; RegWrite=1'b0; RegDst=1'b0; PCWrite=1'b0; PCWriteCond=1'b0; ALUOp=2'b00;


  opcode = inputCode/10000000000000000000000000;

  functionCode =  inputCode%10000000000000000000000000;

  $monitor("32bit code=%b, opcode=%b functionCode=%b", functionCode,opcode,functionCode);

    begin
      MemRead = 1'b1;
      IRWrite = 1'b1;
      ALUSrcB = 2'b01;
      PCWrite = 1'b1;
    end

end
  
endmodule

//100011 - LW
//101011 - SW