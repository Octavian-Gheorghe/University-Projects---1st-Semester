bits 32
global start        

extern exit               
import exit msvcrt.dll    
;1/a + 200*b - c/(d+1) + x/a - e
; doubleword/word + word*word - byte/(byte+1) + quadword/word - doubleword
; word + doubleword - byte + doubleword - doubleword
segment data use32 class=data
    a dw 5
    b dw 300
    c db 10
    d db 5
    e dd 10
    x dq 304
segment code use32 class=code
    start:
        mov ax, 1
        cwd; dx:ax = 1
        div word [a]; 1/a, remainder is inside dx and quotient inside ax
        mov bx, ax; bx = 1/a

        mov ax, 200
        mul word [b]; dx:ax = 200*b
        mov cx, 0; cx:bx = 1/a
        add bx, ax
        adc cx, dx; cx:bx 1/a + 200*b

        mov al, [c]; al = c
        mov ab, 0; we convert c to word, ax = c
        mov dl, [d]; dl = d
        add dl, 1; dl = d + 1
        div dl; c/(d+1), remainder is inside ah and quotient inside al
        mov ah, 0; we convert c/(d+1) into a word
        mov dx, 0; we convert c/(d+1) into a doubleword
        add bx, ax
        adc cx, dx; cx:bx = 1/a + 200*b - c/(d+1)

        sub bx, word [e]
        sbb cx, word [e+2]; cx:bx = c/(d+1) + 1/a + 200*b - e

        push cx, bx; we store c/(d+1) + 1/a + 200*b - e on the stack

        mov eax, [x]
        mov edx, [x+4]; edx:eax = x
        mov bx, [a];
        mov cx, 0; cx:bx = a
        push cx, bx
        pop ebx; ebx = a
        div ebx; x/a, remainder is inside edx and quotient is inside eax
        mov ecx, eax; ecx = x/a
        pop ebx; ebx = c/(d+1) + 1/a + 200*b - e
        add ecx, ebx; ecx = c/(d+1) + 1/a + 200*b - e + x/a

        push    dword 0      
        call    [exit]       