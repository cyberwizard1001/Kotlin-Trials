
module alu_tb;
reg [4:0] a,b;
reg [5:0] func_code,opcode;
wire [31:0] op;
alu u1 (op,a,b,func_code,opcode);
 initial
 begin

      $monitor("A=%b, B=%b | op = %b", a, b, op);
 
 a=5'b01010;
 b=5'b00101;
 func_code=6'b000000;
 opcode = 6'b001000;
 #100;
 
 a=5'b00110;
 b=5'b00011;
 func_code=6'b100000;
 opcode = 6'b000000;
 #100;
 
 a=5'b01100;
 b=5'b00100;
 func_code=6'b000000;
 opcode = 6'b001100;
 #100;
 
 a=5'b01001;
 b=5'b00100;
 func_code=6'b100000;
 opcode = 6'b000000;
 #100;

 a=4'b0111;
 b=4'b1001;
 func_code=6'b100010;
 opcode = 6'b000000;
 #100;
 
  end 
 endmodule