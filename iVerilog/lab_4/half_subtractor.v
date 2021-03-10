module half_subtractor();

reg a,b;
wire x,y,z; 

//x = diff
//z = borrow

xor(x,a,b);
not(y,a);
and(z,y,b);

initial
begin
  $monitor("a=%b, b=%b, | diff=%b, borrow=%b", a, b, x,z);

  a = 0; b = 0; #10;
  a = 0; b = 0; #10;
  a = 0; b = 1; #10;
  a = 0; b = 1; #10;
  a = 1; b = 0; #10;
  a = 1; b = 0; #10;
  a = 1; b = 1; #10;
  a = 1; b = 1; #10;

  $finish;
end

endmodule
