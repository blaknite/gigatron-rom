; do *NOT* use register4 to register7 during time slicing
xreset              EQU     register0
xcount              EQU     register1
ycount              EQU     register2
treset              EQU     register3
breset              EQU     register8
top                 EQU     register9
bot                 EQU     register10
vramAddr            EQU     register11
evenAddr            EQU     register12
clsAddress          EQU     register13
varAddress          EQU     register13
    

%SUB                resetVars
resetVars           LDI     0
                    DOKE    varAddress
                    INC     varAddress
                    INC     varAddress
                    LD      varAddress
                    XORI    giga_One                            ; end of user vars
                    BNE     resetVars
                    RET
%ENDS

%SUB                resetVideoFlags
resetVideoFlags     LDI     giga_CursorX                        ; cursor x start
                    STW     cursorXY
                    LDWI    ON_BOTTOM_ROW_MSK
                    ANDW    miscFlags
                    STW     miscFlags                           ; reset on bottom row flag
                    RET
%ENDS

%SUB                resetVideoTable
                    ; resets video table pointers
resetVideoTable     PUSH
                    LDI     8
                    STW     vramAddr
                    LDWI    giga_videoTable
                    STW     evenAddr
    
resetVT_loop        CALL    realTimeStubAddr
                    LDW     vramAddr
                    DOKE    evenAddr
                    INC     evenAddr
                    INC     evenAddr
                    INC     vramAddr
                    LD      vramAddr
                    SUBI    giga_yres + 8
                    BLT     resetVT_loop
                    
                    LDWI    resetVideoFlags
                    CALL    giga_vAC                    
                    POP
                    RET
%ENDS   
    
%SUB                initClearFuncs
initClearFuncs      PUSH
                    LDWI    resetVideoFlags
                    CALL    giga_vAC
            
                    LD      fgbgColour
                    ST      giga_sysArg0
                    ST      giga_sysArg0 + 1
                    ST      giga_sysArg2
                    ST      giga_sysArg2 + 1                    ; 4 pixels of fg colour
    
                    LDWI    SYS_Draw4_30                        ; setup 4 pixel SYS routine
                    STW     giga_sysFn
                    POP
                    RET
%ENDS   

%SUB                clearScreen
                    ; clears the viewable screen, (unrolled 4 times with a SYS call doing 4 pixels, so 16 pixels per loop)
clearScreen         PUSH
                    LDWI    initClearFuncs
                    CALL    giga_vAC
                    
                    LDW     clsAddress
                    STW     giga_sysArg4
                    LDWI    (giga_yres - 1) * 256
                    ADDW    clsAddress
                    STW     clsAddress                          ; end address

clearS_loop         CALL    realTimeStubAddr
                    LD      giga_sysArg4
                    SYS     30
                    ADDI    0x04
                    ST      giga_sysArg4
                    SYS     30
                    ADDI    0x04
                    ST      giga_sysArg4
                    SYS     30
                    ADDI    0x04
                    ST      giga_sysArg4
                    SYS     30
                    ADDI    0x04
                    ST      giga_sysArg4
                    SUBI    giga_xres
                    BLT     clearS_loop
    
                    LDI     0
                    ST      giga_sysArg4
                    INC     giga_sysArg4 + 1                    ; next top line
                    LDW     giga_sysArg4
                    SUBW    clsAddress
                    BLE     clearS_loop
                    POP
                    RET
%ENDS   

%SUB                clearVertBlinds
                    ; clears the viewable screen using a vertical blinds effect
clearVertBlinds     PUSH
                    LDWI    initClearFuncs
                    CALL    giga_vAC

                    LDWI    giga_vram
                    STW     giga_sysArg4
                    LD      giga_sysArg4 + 1
                    ST      top
    
clearVB_loop        CALL    realTimeStubAddr
                    LD      top
                    ST      giga_sysArg4 + 1                    ; top line
                    SYS     30
    
                    LDWI    giga_yres - 1 + 16
                    SUBW    top
                    ST      giga_sysArg4 + 1                    ; bottom line
                    SYS     30
    
                    LD      giga_sysArg4
                    ADDI    0x04
                    ST      giga_sysArg4
                    SUBI    giga_xres
                    BLT     clearVB_loop
    
                    LDI     0
                    ST      giga_sysArg4
                    INC     top                                 ; next top line
                    LD      top
                    SUBI    giga_yres / 2 + 8
                    BLT     clearVB_loop
                    POP
                    RET
%ENDS
