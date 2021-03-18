module eightoneusingtwoone();


reg d0,d1,d2,d3,d4,d5,d6,d7,s0,s1,s2;
wire x,y,z;

twoxonemux mux1(d0,d1,s0,t);
twoxonemux mux2(d2,d3,s0,u);
twoxonemux mux3(d4,d5,s0,v);
twoxonemux mux4(d6,d7,s0,w);
twoxonemux mux5(t,u,s1,x);
twoxonemux mux6(v,w,s1,z);
twoxonemux mux7(x,z,s2,y);

initial
begin
  $monitor("S0=%b, S1=%b, S2=%b, d0=%b, d1=%b, d2=%b, d3=%b, d4=%b, d5=%b, d6=%b, d7=%b  | y=%b", s0, s1, s2, d0, d1, d2, d3, d4, d5, d6, d7, y);

  d0=1;d1=0;d2=0;d3=0;d4=0;d5=0;d6=0;d7=0;
  s0=0;s1=0;s2=0; #10;
  s0=0;s1=0;s2=1; #10;
  s0=0;s1=1;s2=0; #10;
  s0=0;s1=1;s2=1; #10;
  s0=1;s1=0;s2=0; #10;
  s0=1;s1=0;s2=1; #10;
  s0=1;s1=0;s2=0; #10;
  s0=1;s1=0;s2=1; #10;
 
  $finish;
end

endmodule
