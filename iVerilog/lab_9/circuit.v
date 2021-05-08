module circuit(x,y,z,o);

input x,y,z;
output o;

reg a,b,c,d,e,f,g,h;


not(a,x);
or(b,a,y);
not(c,z);
and(d,x,c);
nor(e,y,d);
and(f,b,e);
nand(g,z,y);
and(h,x,g);
or(o,h,f);

endmodule