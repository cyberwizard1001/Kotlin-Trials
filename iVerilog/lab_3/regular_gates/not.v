module gatelevelnot();
reg a;
wire y;

not(y,a);

initial
begin
  $monitor("a=%b, y=%b", a,y);

  a = 0; #10;
  a = 1;
  $finish;

end
endmodule
