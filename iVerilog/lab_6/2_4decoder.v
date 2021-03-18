module decoder( out, A, B, enable );

output [0:3] out; 
input A, B, en;
input ;
wire NA, NB, NE;

not Gate1 (NA, A); 
not Gate2 (NB, B);
not Gate3 (NE, en);

nand G4 (D[0], NA, NB, NE );
nand G5 (D[1], NA, B, NE );
nand G6 (D[2], A, NB, NE );
nand G7 (D[3], A, B, NE );

initial
begin
     $monitor("Enable=%b, A=%b, B=%b, Y0=%b, Y1=%b, Y2=%b, Y3=%b", en, A, B, D[0], D[1], D[2], D[3]);

     $display("This is when the enable input is 1");

     e = 1;w1 = 0;w0 = 0; #10;
     e = 1;w1 = 0;w0 = 1; #10;
     e = 1;w1 = 1;w0 = 0; #10;
     e = 1;w1 = 1;w0 = 1; #10;

     $display("This is when the enable input is 0 ");

     e = 0;w1 = 0;w0 = 0; #10;
     e = 0;w1 = 0;w0 = 1; #10;
     e = 0;w1 = 1;w0 = 0; #10;
     e = 0;w1 = 1;w0 = 1; #10;
     $finish;
end

endmodule