#include <avr/io.h> 
#include <util/delay.h> 
#include <stdbool.h> 
int main (void) 
 
{ 
bool x,y,z,F,A,B,C; 
 
DDRB=0b11111000; 
PORTB=0b00000111; 
 
DDRD=0b00111100; 
 
while(1) 
{ 
 
 x = (PINB & (1 << PINB2)) == (1 << PINB2); 
 y = (PINB & (1 << PINB1)) == (1 << PINB1); 
 z = (PINB & (1 << PINB0)) == (1 << PINB0); 
 
 F=(x&y)|(!x&!y)|(!y&z);
 A=0;
 B=0;
 C=0; 
 
 PORTD |= (F << 2); 
 PORTD |= (A << 3);
 PORTD |= (B << 4);
 PORTD |= (C << 5);
} 
return 0; 
}
