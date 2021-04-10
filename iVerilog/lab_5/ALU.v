module ALU();


reg a,b,c,d;
wire e,f,g,h,i,j,k;

not(e,a);
not(f,b);
not(g,c);
not(h,d);

and(i,e,f,c,d);
and(p,a,f,c,d);
and(q,a,b,g,h);
and(r,a,b,c,h);
and(s,a,b,c,d);
or(l,i,p,q,r,s);      //l

and(m,e,f,g,d);
and(n,e,f,c,d);
and(o,e,b,g,d);
and(t,k,e,b,c,h);

or(m,n,o,k);    //t

initial
begin
  $monitor("A=%b, B=%b, C=%b, D=%b | o1=%b, o2=%b", a, b, c, d, l, t);

  a = 1'b0; b = 1'b0; c = 1'b0; d = 1'b0; #10
a = 1'b0; b = 1'b0; c = 1'b0; d = 1'b1; #10
a = 1'b0; b = 1'b0; c = 1'b1; d = 1'b0; #10
a = 1'b0; b = 1'b0; c = 1'b1; d = 1'b1; #10

a = 1'b0; b = 1'b1; c = 1'b0; d = 1'b0; #10
a = 1'b0; b = 1'b1; c = 1'b0; d = 1'b1; #10
a = 1'b0; b = 1'b1; c = 1'b1; d = 1'b0; #10
a = 1'b0; b = 1'b1; c = 1'b1; d = 1'b1; #10

a = 1'b1; b = 1'b0; c = 1'b0; d = 1'b0; #10
a = 1'b1; b = 1'b0; c = 1'b0; d = 1'b1; #10
a = 1'b1; b = 1'b0; c = 1'b1; d = 1'b0; #10
a = 1'b1; b = 1'b0; c = 1'b1; d = 1'b1; #10

a = 1'b1; b = 1'b1; c = 1'b0; d = 1'b0; #10
a = 1'b1; b = 1'b1; c = 1'b0; d = 1'b1; #10
a = 1'b1; b = 1'b1; c = 1'b1; d = 1'b0; #10
a = 1'b1; b = 1'b1; c = 1'b1; d = 1'b1;  


  $finish;
end
endmodule
