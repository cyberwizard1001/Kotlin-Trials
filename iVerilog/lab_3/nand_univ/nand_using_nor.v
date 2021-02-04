module gatelevel_nand_using_nor();
reg a;
reg b;
wire c;
wire d;
wire y;
wire z;

nor(c,a,a);
nor(d,b,b);
nor(y,c,d);
nor(z,y,y);

initial
begin
  $monitor("a=%b, b=%b, y=%b", a, b, z);

  a = 0; b = 0; #10;
  a = 0; b = 1; #10;
  a = 1; b = 0; #10;
  a = 1; b = 1; #10;
  $finish;
end
endmodule
