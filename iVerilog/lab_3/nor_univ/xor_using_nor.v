module xor_using_nor();
reg a;
reg b;
wire y;

nor(x,a,b);
nor(y,a,a);
nor(z,b,b);
nor(d,y,z);
nor(e,x,d);

initial
begin
 $monitor("a=%b b=%b\ty=%b", a, b, e);

 a = 0; b = 0; #10;
 a = 0; b = 1; #10;
 a = 1; b = 0; #10;
 a = 1; b = 1; #10;
 $finish;
end
endmodule
