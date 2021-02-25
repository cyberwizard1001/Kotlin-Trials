module fouroneusingtwoone();


reg i0,i1,i2,i3,a,b;
wire x,y,z;

two_x_onemux mux1(i0,i1,a,x);
two_x_onemux mux2(i2,i3,a,z);
two_x_onemux mux3(x,z,b,y);

initial
begin
  $monitor("S0=%b, S1=%b | Y=%b", a, b, y);
  
  i0 = 1'b0; i1 = 1'b1; i2 = 2'b10; i3 = 2'b11;
  a = 2'b00; b = 2'b00; #10;
  a = 2'b00; b = 2'b01; #10;
  a = 2'b01; b = 2'b00; #10;
  a = 2'b01; b = 2'b01; #10;

  $finish;
end

endmodule
