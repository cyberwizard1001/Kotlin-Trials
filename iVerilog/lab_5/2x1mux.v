module twoxonemux(a,b,x,y);

input a,b,x;    
wire q,r,s;
output y;

and(q,b,x);
not(r,x);
and(s,r,a);
or(y,q,s);

endmodule
