module xnorgate(a,b,y);
input a,b;
output y;
assign y = !((a&!b) | (b&!a));
endmodule
