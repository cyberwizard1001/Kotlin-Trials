module twoxonemux();

reg a,b,x;    

wire y,q,r,s;

and(q,b,x);
not(r,x);
and(s,r,a);
or(y,q,s);



initial
begin
  $monitor("a=%b, b=%b, sel=%b | y=%b", a, b, x, y);

  a = 0; b = 0; x = 0; #10;
  a = 0; b = 0; x = 1; #10;
  a = 0; b = 1; x = 0; #10;
  a = 0; b = 1; x = 1; #10;
  a = 1; b = 0; x = 0; #10;
  a = 1; b = 0; x = 1; #10;
  a = 1; b = 1; x = 0; #10;
  a = 1; b = 1; x = 1; #10;

  $finish;
end
endmodule
