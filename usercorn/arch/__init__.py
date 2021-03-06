import arm
import arm64
import mips
import x64
import x86

ARCH_MAP = {
    'aarch64': 'arm64',
    'i386': 'x86',
    'x86_64': 'x64',
}

def map(arch):
    arch = arch.lower()
    return ARCH_MAP.get(arch, arch)

ARCH = {
    'arm': arm,
    'arm64': arm64,
    'mips': mips,
    'x64': x64,
    'x86': x86,
}

def find(arch, os):
    arch = ARCH.get(map(arch))
    return arch, arch.OS.get(os)
