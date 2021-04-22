module d_ff(input wire Clock,input wire D,input Rst,output reg Q);
always @(negedge Rst or posedge Clock )
begin
if (!Rst)
Q = 0;
else
Q = D;
end
endmodule


module shift_register;
reg Clock;
reg D;
reg Rst;
wire Q;
integer i;
d_ff ob(Clock,D,Rst,Q);
initial begin
D = 0;
D = Q;

    always @ (posedge Clock)
        begin
        Q= Q>>1; 
        end



initial begin
Clock = 0;
for ( i =0; i <=10; i= i+1)
#10 Clock = ~Clock;
end


initial begin
$monitor("Clock=%d,D=%d,Q=%d \n",Clock,D,Q);
end
endmodule

