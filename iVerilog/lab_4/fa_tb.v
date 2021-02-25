module fausingha_test();
wire sum,carry;
reg t_a,t_b,t_c;


fa_using_ha test_gate1(t_a,t_b,t_c,sum,carry);


initial
begin

    
$monitor("a=%b, b=%b, cin=%b | sum=%b, carry=%b", t_a, t_b, t_c, sum, carry);
t_a = 1'b0; t_b = 1'b0; t_c = 1'b0; #10
t_a = 1'b0; t_b = 1'b0; t_c = 1'b1; #10

t_a = 1'b0; t_b = 1'b1; t_c = 1'b0; #10
t_a = 1'b0; t_b = 1'b1; t_c = 1'b1; #10

t_a = 1'b1; t_b = 1'b0; t_c = 1'b0; #10
t_a = 1'b1; t_b = 1'b0; t_c = 1'b1; #10

t_a = 1'b1; t_b = 1'b1; t_c = 1'b0; #10
t_a = 1'b1; t_b = 1'b1; t_c = 1'b1;

end
endmodule
