from unicorn.x86_const import *
import os
import sys

from usercorn import syscalls

SYSCALLS = {
    1: ('exit', 1),
    2: ('fork', 0),
    3: ('read', 3),
    4: ('write', 3),
    5: ('open', 3), # variable length args?
    6: ('close', 1),
    7: ('wait4', 4),
    9: ('link', 2),
    10: ('unlink', 1),
    73: ('munmap', 2),
    197: ('mmap', 6),
    199: ('lseek', 3),
}

def syscall(cls):
    def args(n):
        cls.pop()
        return [cls.pop() for i in xrange(n)]

    def call(name, n):
        return getattr(syscalls, name)(cls, *args(n)) or 0

    num = cls.reg_read(X86_REG_EAX)
    params = SYSCALLS.get(num)
    if params:
        ret = call(*params)
        cls.reg_write(X86_REG_EAX, ret)
    else:
        print 'Unsupported syscall:', num
        sys.exit(1)

def interrupt(cls, intno):
    if intno == 0x80:
        syscall(cls)
    else:
        raise NotImplementedError('unhandled interrupt %d' % intno)
