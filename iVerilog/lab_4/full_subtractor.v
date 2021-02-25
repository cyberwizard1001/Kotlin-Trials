module full_subtractor();

reg a,b,bin;    

wire z,y,x,w,v,u,t;

xor(z,a,b);
xor(y,z,bin);  //dout
not(x,a);
and(w,x,b);
not(v,z);
and(u,v,bin);
or(t,w,u); //bout


initial
begin
  $monitor("a=%b, b=%b, bin=%b | dout=%b, bout=%b", a, b, bin, x, t);

  a = 0; b = 0; bin = 0; #10;
  a = 0; b = 0; bin = 1; #10;
  a = 0; b = 1; bin = 0; #10;
  a = 0; b = 1; bin = 1; #10;
  a = 1; b = 0; bin = 0; #10;
  a = 1; b = 0; bin = 1; #10;
  a = 1; b = 1; bin = 0; #10;
  a = 1; b = 1; bin = 1; #10;

  $finish;
end
endmodule
