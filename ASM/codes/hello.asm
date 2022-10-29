.include "/home/dell/assembly/m328Pdef.inc"                                             Start:                                       
  ldi r30,0b11111000;     \\identifying input pins 8,9,10 
  out DDRB,r30;            \\declaring pins as input
  ldi r30,0b11111111;
  out PORTB,r30;            \\activating internal pullup resistors
  in r30,PINB                                 
  ldi r16,0b00111100;        \\identifying output pins
  out DDRD,r16;                               
  ldi r17,0b00000001                          
  ldi r18,0b00000001
  ldi r19,0b00000001
  
  AND r17,r30          ;r17=z
  LSR  r30
  AND r18,r30          ;r18=y                
  LSR r30
  AND r19,r30          ;r19=x

  ldi r23,0b00000001                          
  eor r23,r17           ;r23=z'
  ldi r24,0b00000001                          
  eor r24,r18           ;r24=y'               
  ldi   r25,0b00000001                          
  eor r25,r19           ;r25=x'
                                             
  mov r0,r19            ;r0=x                 
  AND r0,r18            ;r0=xy
  MOV r1,r25            ;r1=x'
  AND r1,r24            ;r1=x'y'              
  AND r2,r24            ;r2=y'                
  AND r2,r17            ;r2=y'z
  OR  r2,r1
  OR  r2,r0             ;r2=xy+x'y'+y'z      

LSL r2               ;r2=000000y0
LSL r2               ;r2=00000y00
out PortD,r2
rjmp Start
