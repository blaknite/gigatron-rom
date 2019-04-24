import asm

asm.defun('@globals')
asm.glob('ht')
asm.dw(0)
asm.glob('ha')
asm.dw(0)
asm.glob('pvpc')
asm.dw('vPC')
asm.glob('sp')
asm.dw(0x06fe)
asm.glob('rv')
asm.dw(0)
asm.glob('thunk0')
asm.dw('@thunk0')
asm.glob('thunk1')
asm.dw('@thunk1')
asm.glob('thunk2')
asm.dw('@thunk2')
asm.glob('enter')
asm.dw('@enter')
asm.glob('leave')
asm.dw('@leave')
asm.glob('ldloc')
asm.dw('@ldloc')
asm.glob('stloc')
asm.dw('@stloc')
asm.glob('pusha')
asm.dw('@pusha')
asm.glob('lsh')
asm.dw('@lsh')
asm.glob('rsh')
asm.dw('@rsh')
asm.glob('mul')
asm.dw('@mul')
asm.glob('mod')
asm.dw(0)
asm.glob('div')
asm.dw(0)
asm.glob('blkcopy')
asm.dw('@blkcopy')
asm.glob('stlocb')
asm.dw('@stlocb')
asm.glob('ldlocb')
asm.dw('@ldlocb')

asm.defun('@start')
asm.ldwi('_main')
asm.call('vAC')
asm.label('halt')
asm.ldwi('halt')
asm.jr()

asm.defun('@ldloc')
asm.addw('sp')
asm.deek()
asm.ret()

asm.defun('@ldlocb')
asm.addw('sp')
asm.peek()
asm.ret()

asm.defun('@stloc')
asm.addw('sp')
asm.stw('ht')
asm.ldw('ha')
asm.doke('ht')
asm.ret()

asm.defun('@stlocb')
asm.addw('sp')
asm.st('ht')
asm.ld('ha')
asm.poke('ht')
asm.ret()

asm.defun('@thunk0')
asm.stw('ht')
asm.inc('vLRH')
asm.ldi(0)
asm.st('vLR')
asm.ldw('ht')
asm.ret()

asm.defun('@thunk1')
asm.stw('ht')
asm.inc('vLRH')
asm.ldi(0xa0)
asm.st('vLR')
asm.ldw('ht')
asm.ret()

asm.defun('@thunk2')
asm.stw('ht')
asm.ldwi(0x08a0)
asm.stw('vLR')
asm.ldw('ht')
asm.ret()

# vAC = bitmask of registers to save. The highest-order bit represents r15.
asm.defun('@enter')
asm.stw('ha')
asm.ldi('r15')
asm.stw('ht')
asm.ldw('ha')
asm.label('loop')
asm.jeq('done')
asm.jgt('next')
asm.ldw('ht')
asm.deek()
asm.doke('sp')
asm.ldw('sp')
asm.subi(2)
asm.stw('sp')
asm.label('next')
asm.ldw('ht')
asm.subi(2)
asm.stw('ht')
asm.ldw('ha')
asm.addw('ha')
asm.stw('ha')
asm.ldwi('loop')
asm.jr()
asm.label('done')
asm.ret()

# vAC = bitmask of registers to restore. The highest-order bit represents r1.
asm.defun('@leave')
asm.stw('ha')
asm.ldi('r1')
asm.stw('ht')
asm.ldw('ha')
asm.label('loop')
asm.jeq('done')
asm.jgt('next')
asm.ldw('sp')
asm.addi(2)
asm.stw('sp')
asm.deek()
asm.doke('ht')
asm.label('next')
asm.inc('ht')
asm.inc('ht')
asm.ldw('ha')
asm.addw('ha')
asm.stw('ha')
asm.ldwi('loop')
asm.jr()
asm.label('done')
asm.ret()

# vAC = value to push
asm.defun('@pusha')
asm.doke('sp')
asm.ldw('sp')
asm.subi(2)
asm.stw('sp')
asm.ret()

# vAC = shift amount, r1 = value to shift
asm.defun('@lsh')
asm.andi(0x0f)
asm.jeq('done')
asm.label('loop')
asm.stw('ha')
asm.ldw('r1')
asm.lslw()
asm.stw('r1')
asm.ldw('ha')
asm.subi(1)
asm.jne('loop')
asm.label('done')
asm.ldw('r1')
asm.ret()

# vAC = shift amount, r1 = value to shift
asm.defun('@rsh')
asm.andi(0x0f)
asm.jeq('done')
asm.stw('ha')
asm.ldw('sysFn')
asm.stw('ht')
asm.ldwi(0x0600)
asm.stw('sysFn')
asm.ldw('ha')
asm.label('loop')
asm.stw('ha')
asm.ldw('r1')
asm.sys(0xff)
asm.stw('r1')
asm.ldw('ha')
asm.subi(1)
asm.jne('loop')
asm.ldw('ht')
asm.stw('sysFn')
asm.label('done')
asm.ldw('r1')
asm.ret()

# r1 = a, vAC = b
# rv = product, ha = addend, ht = bitmask
asm.defun('@mul')
asm.stw('ha')
asm.ldi(0)
asm.stw('rv')
asm.ldi(1)
asm.label('loop')
asm.stw('ht')
asm.andw('r1')
asm.jeq('next')
asm.ldw('rv')
asm.addw('ha')
asm.stw('rv')
asm.label('next')
asm.ldw('ha')
asm.lslw()
asm.stw('ha')
asm.ldw('ht')
asm.lslw()
asm.jne('loop')
asm.ret()

# r1 = dest, ha = src, vAC = size
asm.defun('@blkcopy')
asm.label('loop')
asm.stw('ht')
asm.ldw('ha')
asm.peek()
asm.poke('r1')
asm.ldw('ha')
asm.addi(1)
asm.stw('ha')
asm.ldw('r1')
asm.addi(1)
asm.stw('r1')
asm.ldw('ht')
asm.subi(1)
asm.jne('loop')
asm.ret()
