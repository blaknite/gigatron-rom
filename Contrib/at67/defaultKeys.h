std::vector<std::string> _defaultKeys =
{
    "                                                                                ",
    "; Keys are editable in 'input_config.ini'                                       ",
    "; If this file is changed, the emulator has to be restarted                     ",
    "; Text cursor and editing is controlled via the mouse                           ",
    "                                                                                ",
    "[Emulator]               ; case sensitive                                       ",
    "RamMode      = CTRL+M    ; toggles between RAM, ROM0 and ROM1                   ",
    "Browse       = CTRL+B    ; file browser                                         ",
    "RomType      = CTRL+R    ; ROM browser                                          ",
    "HexMonitor   = CTRL+X    ; hex monitor                                          ",
    "Disassembler = CTRL+D    ; disassembler, (vCPU or Native based on RamMode)      ",
    "Reset        = CTRL+F1   ; emulator reset                                       ",
    "Execute      = CTRL+F5   ; executes whatever code is present at the load address",
    "ScanlineMode = CTRL+F3   ; toggles scanline modes, Normal, VideoB and VideoBC   ",
    "Help         = CTRL+H    ; toggles help screen on and off                       ",
    "Quit         = CTRL+Q    ; instant quit                                         ",
    "Speed+       = +         ; increases the emulation speed                        ",
    "Speed-       = -         ; decreases the emulation speed                        ",
    "                                                                                ",
    "[Keyboard]               ; case sensitive                                       ",
    "Mode         = CTRL+K    ; toggles between, Giga, PS2, HwGiga and HwPS2         ",
    "Left         = A         ; left input for emulator/hardware depending on Mode   ",
    "Right        = D         ; right input for emulator/hardware depending on Mode  ",
    "Up           = W         ; up input for emulator/hardware depending on Mode     ",
    "Down         = S         ; down input for emulator/hardware depending on Mode   ",
    "Start        = SPACE     ; start input for emulator/hardware depending on Mode  ",
    "Select       = Z         ; select input for emulator/hardware depending on Mode ",
    "A            = .         ; A input for emulator/hardware depending on Mode      ",
    "B            = /         ; B input for emulator/hardware depending on Mode      ",
    "                                                                                ",
    "[Hardware]               ; case sensitive                                       ",
    "Reset        = ALT+F1    ; resets hardware                                      ",
    "Execute      = ALT+F5    ; uploads and excutes .vasm and .gt1 files to hardware ",
    "                                                                                ",
    "[Debugger]               ; case sensitive                                       ",
    "Debug        = CTRL+F6   ; toggles debugging mode, can be used to pause         ",
    "Step         = CTRL+F7   ; single steps debugger based on a watched variable    ",
    "                         ; by default is videoY which changes once per scanline ",
    "                                                                                "
};