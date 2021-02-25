module two_x_onemux(a,b,x,y);

input a,b,x;
output y;
wire q,r,s;

and(q,b,x);
not(r,x);
and(s,r,a);
or(y,q,s);

endmodule