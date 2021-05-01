module execute(opcode, functionCode,IorD,MemRead,MemWrite,MemtoReg,IRWrite,PCSource,ALUSrcB,ALUSrcA,RegWrite,RegDst,PCWrite,PCWriteCond,ALUOp,instruction,register_one,register_two,register_three);
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

  always @(opcode[5:0] or functionCode[5:0])
  begin

   opcode = inputCode/10000000000000000000000000;

   functionCode =  inputCode%10000000000000000000000000;


	IorD=1'b0; MemRead=1'b0; MemWrite=1'b0; MemtoReg=1'b0; IRWrite=1'b0; PCSource=1'b0;
	ALUSrcB=2'b00; ALUSrcA=1'b0; RegWrite=1'b0; RegDst=1'b0; PCWrite=1'b0; PCWriteCond=1'b0; ALUOp=2'b00;

begin
    if(opcode==6'b000000)
    begin
        register_three = register_one+register_two;
    end

    if(opcode==6'b100011)
    begin
        $monitor("1000,1004+(4x4)=1020");
    end

    if(opcode==6'b101011)
    begin
        $monitor("1000+(8x4)=1032");
    end
end
  endmodule