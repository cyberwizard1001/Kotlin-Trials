module half_adder();
reg a;
reg b;
wire y;
wire z;

and(z,a, b);
xor(y,a,b);

initial
begin
  $monitor("a=%b, b=%b | sum=%b, carry=%b", a, b, y, z);

  a = 0; b = 0; #10;
  a = 0; b = 1; #10;
  a = 1; b = 0; #10;
  a = 1; b = 1; #10;

  $finish;
end
endmodule
