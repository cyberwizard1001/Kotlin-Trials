module full_adder();
reg a;
reg b;
reg cin;
wire v;
wire w;     //sum
wire x;
wire y;
wire z;     //cout

xor(v,a,b);
xor(w,v,cin);
and(x,v,cin);
and(y,a,b);
or(z,x,y);

initial
begin
  $monitor("a=%b, b=%b, cin=%b | sum=%b, cout=%b", a, b, cin, w, z);

  a = 0; b = 0; cin = 0; #10;
  a = 0; b = 0; cin = 1; #10;
  a = 0; b = 1; cin = 0; #10;
  a = 0; b = 1; cin = 1; #10;
  a = 1; b = 0; cin = 0; #10;
  a = 1; b = 0; cin = 1; #10;
  a = 1; b = 1; cin = 0; #10;
  a = 1; b = 1; cin = 1; #10;

  $finish;
end
endmodule
