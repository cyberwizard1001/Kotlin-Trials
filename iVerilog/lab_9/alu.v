module alu (op,a,b,func_code,opcode);
output reg [31:0] op;
input [4:0] a,b; 
input [5:0] func_code,opcode;
 always @(*)
 begin
     if(opcode==000000)
     begin
        case (func_code)
 6'b100000 : begin op = a + b; $display("Addition operation"); end
 6'b100010 : begin op = a - b; $display("Subtraction operation"); end
 6'b100100 : begin op = a & b; $display("Logical AND operation"); end
 6'b100101: begin op = a | b; $display("Logical OR operation"); end
 6'b100111: begin op = ~(a | b); $display("Logical NOR operation"); end
 default:op = 6'b000000;
endcase         
     end

     if(opcode==001000)
     begin
         op = a+b; $display("Immediate ADD operation");
     end

     if(opcode==001100)
     begin
         op = a&b; $display("Immediate AND operation");
     end
 
end
endmodule
