module xorgate_test;
wire t_y;
reg t_a,t_b;

xorgate test_gate(t_a,t_b,t_y);

initial
begin
$monitor(t_a,t_b,t_y);
t_a = 1'b0;
t_b = 1'b0;

#5

t_a = 1'b0;
t_b = 1'b1;

#5


t_a = 1'b1;
t_b = 1'b0;

#5


t_a = 1'b1;
t_b = 1'b1;

end
endmodule
