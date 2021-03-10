module twobitadder(a, b, c, d, e, i, f);
input a,b,c,d;
output e,f,i;
wire g,h,j,k;

xorgate gate_one(a,b,e);
andgate gate_two(a,b,g);
xorgate gate_three(c,d,h);
xorgate gate_four(g,h,i);
andgate gate_five(c,d,j);
andgate gate_six(g,h,k);
orgate gate_seven(j,k,f);

//Order of outputs: 

//s0 = e
//s1 = i
//carry = f
endmodule
