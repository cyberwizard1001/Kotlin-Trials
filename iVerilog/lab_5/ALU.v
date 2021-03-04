module ALU();
reg a,b,c,d;

wire e,f;



initial
begin
  $monitor("a=%b, b=%b, y=%b", a, b, y);

  a = 0; b = 0; #10;
  a = 0; b = 1; #10;
  a = 1; b = 0; #10;
  a = 1; b = 1; #10;
  $finish;
end
endmodule
