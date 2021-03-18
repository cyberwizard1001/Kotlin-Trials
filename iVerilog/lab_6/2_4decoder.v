module decoder( out, A, B, enable );

output [0:3] out; 
input A, B, en;
input ;
wire NA, NB, NE;

not Gate1 (NA, A); 
not Gate2 (NB, B);
not Gate3 (NE, en);

nand Gate4 (D[0], NA, NB, NE );
nand Gate5 (D[1], NA, B, NE );
nand Gate6 (D[2], A, NB, NE );
nand Gate7 (D[3], A, B, NE );

initial
begin
     $monitor("Enable=%b, A=%b, B=%b, Y0=%b, Y1=%b, Y2=%b, Y3=%b", en, A, B, D[0], D[1], D[2], D[3]);

     $display("EN=1");

     en = 1;B = 0;A = 0; #10;
     en = 1;B = 0;A = 1; #10;
     en = 1;B = 1;A = 0; #10;
     en = 1;B = 1;A = 1; #10;

     $display("EN=0");

     en = 0;B = 0;A = 0; #10;
     en = 0;B = 0;A = 1; #10;
     en = 0;B = 1;A = 0; #10;
     en = 0;B = 1;A = 1; #10;
     $finish;
end

endmodule