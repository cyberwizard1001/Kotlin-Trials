module sci(opcode, functionCode, regDst, aluSrc, memToReg, regWrite, memRead, memWrite, branch, aluOP);
  input [5:0]opcode;
  input [5:0]functionCode; 
  output [1:0]aluOP;
  output regDst, aluSrc, memToReg, regWrite, memRead, memWrite, branch;
  reg[1:0]aluOP;
  reg regDst, aluSrc, memToReg, regWrite, memRead, memWrite, branch; 


  always @(opcode[5:0] or functionCode[5:0])
  begin
  if(opcode == 6'b000000)
  begin
    if(functionCode == 6'b100010)
    begin
      regDst=1'b1;
      aluSrc=1'b0;
      memToReg=1'b0;
      regWrite=1'b1;
      memRead=1'b0;
      memWrite=1'b0;
      branch=1'b0;
      aluOP=2'b10;
    end
  end
  $monitor("regDst : %b , aluSrc : %b , memToReg : %b,regWrite: %b , memRead : %b ,memWrite: %b, branch : %b, aluOP :%b ", regDst, aluSrc, memToReg,regWrite, memRead,memWrite, branch,aluOP); 
  end
endmodule

module IO;
  reg [5:0]opcode;
  reg [5:0]functionCode; 
  reg [31:0] inputCode;

  wire [1:0]aluOP;
  wire regDst, aluSrc, memToReg, regWrite, memRead, memWrite, branch;

  sci ob(opcode, functionCode, regDst, aluSrc, memToReg, regWrite, memRead, memWrite, branch, aluOP);

  initial 
  begin 

      inputCode = 32'b00000010001100101001100000100100;

      opcode = inputCode/10000000000000000000000000;

      functionCode =  inputCode%10000000000000000000000000;

      $display("a=%b, b=%b c=%b", inputCode,opcode,functionCode);

  end
  endmodule