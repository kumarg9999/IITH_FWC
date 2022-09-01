.include "/home/kumar/kumar1/m328Pdef.inc" 

Start:
 ldi r30,0b11000000;     \\identifying input pins 8,9,10,11,12,13
 out DDRB,r30;            \\declaring pins as input
 ldi r30,0b11111111;
 out PORTB,r30;            \\activating internal-pullup for pins 2,3,4,5
 in r30,PINB
 ldi r16,0b00000100;        \\identifying output pin 2
 out DDRD,r16;
 ldi r17,0b00000001
 ldi r18,0b00000001
 ldi r19,0b00000001
 ldi r20,0b00000001
 ldi r21,0b00000001
 ldi r22,0b00000001
 

 AND r17,r30          ;r17=a
 LSR  r30
 AND r18,r30           ;r18=b
 LSR r30
 AND r19,r30           ;r19=c
 LSR r30
 AND r20,r30          ;r20=d
 LSR r30
 AND r21,r30          ;r21=e
 LSR r30
 AND r22,r30          ;r22=f

 ldi r23,0b00000001
 eor r23,r17           ;r23=a'
ldi r24,0b00000001
 eor r24,r18           ;r24=b'

 ldi r25,0b00000001
 eor r25,r19           ;r25=c'

 ldi r26,0b00000001
 eor r26,r20           ;r26=d'

 ldi r27,0b00000001
 eor r27,r21           ;r27=e'

 ldi r28,0b00000001
 eor r28,r22           ;r28=f'

 mov r0,r17            ;r0=a
 AND r0,r27            ;r0=ae'
 AND r0,r28            ;r0=ae'f'
 MOV r1,r18            ;r1=b
 AND r1,r27            ;r1=be'
 AND r1,r22            ;r1=be'f
 AND r2,r19            ;r2=c
 AND r2,r21            ;r2=ce
 AND r2,r28            ;r2=cef'
 AND r3,r20            ;r3=d
 AND r3,r21            ;r3=de
 AND r3,r22            ;r3=def
 OR  r3,r2            
 OR  r3,r1
 OR  r3,r0 

LSL r3               ;r3=000000y0
LSL r3               ;r3=00000y00
out PortD,r3

rjmp Start
