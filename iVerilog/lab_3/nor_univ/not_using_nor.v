module gatelevel_not_using_nor();
reg a;
wire y;


not(y,a,a);

initial
begin
  $monitor("a=%b, y=%b", a,y);

  a = 0; #10;
  a = 1;
  $finish;

end
endmodule
