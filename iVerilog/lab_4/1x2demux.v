module onextwo_demux();
reg a, b;
wire u,v,y1,y0;

not(u,a);
not(v,u);
and(y1,v,b);
and(y0,u,b);

initial
begin
  $monitor("a=%b, b=%b | Y0=%b, Y1=%b", a, b, y0, y1);

  a = 0; b = 0; #10;
  a = 0; b = 1; #10;
  a = 1; b = 0; #10;
  a = 1; b = 1; #10;

  $finish;
end
endmodule
