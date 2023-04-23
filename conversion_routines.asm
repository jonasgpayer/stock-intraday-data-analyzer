section .data
section .text

global convert_to_pesos
global convert_to_euros

; Función convert_to_pesos
; Recibe en xmm0 el valor de la criptomoneda en dólares
; Recibe en xmm1 la tasa de cambio de USD a pesos
; Devuelve en xmm0 el resultado de la conversión a pesos
convert_to_pesos:
    push rbp
    mov rbp, rsp

    mulsd xmm0, xmm1

    mov rsp, rbp
    pop rbp
    ret

; Función convert_to_euros
; Recibe en xmm0 el valor de la criptomoneda en dólares
; Recibe en xmm1 la tasa de cambio de USD a euros
; Devuelve en xmm0 el resultado de la conversión a euros
convert_to_euros:
    push rbp
    mov rbp, rsp

    mulsd xmm0, xmm1

    mov rsp, rbp
    pop rbp
    ret
