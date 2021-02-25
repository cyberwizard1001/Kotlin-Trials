module fa_using_ha(a,b,c,sum,carry);

input a,b,c;
output sum, carry;
wire sum1,carry1,sum2,carry2;

halfadder ha1(a,b,sum1,carry1);

halfadder ha2(sum1,c,sum,carry2);

or(carry,carry1,carry2);




endmodule