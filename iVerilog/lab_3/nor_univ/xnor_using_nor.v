module xnor_using_nor();
reg a;
reg b;
wire y;

nor(c,a,b);
nor(d,a,c);
nor(e,b,c);
nor(y,d,e);

initial
begin
 $monitor("a=%b b=%b\ty=%b", a, b, y);

 a = 0; b = 0; #10;
 a = 0; b = 1; #10;
 a = 1; b = 0; #10;
 a = 1; b = 1; #10;
 $finish;
end
endmodule
