module twobitadder_test();
wire sum1,sum2,carry;
reg t_a,t_b,t_c,t_d;


twobitadder test_gate(t_a,t_b,t_c,t_d,sum1,sum2,carry);


initial
begin

    
$monitor("a0=%b, a1=%b, b0=%b, b1=%b | s0=%b, s1=%b, carry=%b", t_a, t_b, t_c, t_d, sum1, sum2, carry);
t_a = 1'b0; t_b = 1'b0; t_c = 1'b0; t_d = 1'b0; #10
t_a = 1'b0; t_b = 1'b0; t_c = 1'b0; t_d = 1'b1; #10
t_a = 1'b0; t_b = 1'b0; t_c = 1'b1; t_d = 1'b0; #10
t_a = 1'b0; t_b = 1'b0; t_c = 1'b1; t_d = 1'b1; #10

t_a = 1'b0; t_b = 1'b1; t_c = 1'b0; t_d = 1'b0; #10
t_a = 1'b0; t_b = 1'b1; t_c = 1'b0; t_d = 1'b1; #10
t_a = 1'b0; t_b = 1'b1; t_c = 1'b1; t_d = 1'b0; #10
t_a = 1'b0; t_b = 1'b1; t_c = 1'b1; t_d = 1'b1; #10

t_a = 1'b1; t_b = 1'b0; t_c = 1'b0; t_d = 1'b0; #10
t_a = 1'b1; t_b = 1'b0; t_c = 1'b0; t_d = 1'b1; #10
t_a = 1'b1; t_b = 1'b0; t_c = 1'b1; t_d = 1'b0; #10
t_a = 1'b1; t_b = 1'b0; t_c = 1'b1; t_d = 1'b1; #10

t_a = 1'b1; t_b = 1'b1; t_c = 1'b0; t_d = 1'b0; #10
t_a = 1'b1; t_b = 1'b1; t_c = 1'b0; t_d = 1'b1; #10
t_a = 1'b1; t_b = 1'b1; t_c = 1'b1; t_d = 1'b0; #10
t_a = 1'b1; t_b = 1'b1; t_c = 1'b1; t_d = 1'b1;  

end
endmodule
