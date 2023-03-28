# enum = '''
#     UC_MODE_LITTLE_ENDIAN = 0,    // little-endian mode (default mode)
#     UC_MODE_BIG_ENDIAN = 1 << 30, // big-endian mode

#     // arm / arm64
#     UC_MODE_ARM = 0,        // ARM mode
#     UC_MODE_THUMB = 1 << 4, // THUMB mode (including Thumb-2)
#     // Depreciated, use  with uc_ctl instead.
#     UC_MODE_MCLASS = 1 << 5,  // ARM's Cortex-M series.
#     UC_MODE_V8 = 1 << 6,      // ARMv8 A32 encodings for ARM
#     UC_MODE_ARMBE8 = 1 << 10, // Big-endian data and Little-endian code.
#                               // Legacy support for UC1 only.

#     // arm (32bit) cpu types
#     // Depreciated, use with uc_ctl instead.
#     UC_MODE_ARM926 = 1 << 7,  // ARM926 CPU type
#     UC_MODE_ARM946 = 1 << 8,  // ARM946 CPU type
#     UC_MODE_ARM1176 = 1 << 9, // ARM1176 CPU type

#     // mips
#     UC_MODE_MICRO = 1 << 4,    // MicroMips mode (currently unsupported)
#     UC_MODE_MIPS3 = 1 << 5,    // Mips III ISA (currently unsupported)
#     UC_MODE_MIPS32R6 = 1 << 6, // Mips32r6 ISA (currently unsupported)
#     UC_MODE_MIPS32 = 1 << 2,   // Mips32 ISA
#     UC_MODE_MIPS64 = 1 << 3,   // Mips64 ISA

#     // x86 / x64
#     UC_MODE_16 = 1 << 1, // 16-bit mode
#     UC_MODE_32 = 1 << 2, // 32-bit mode
#     UC_MODE_64 = 1 << 3, // 64-bit mode

#     // ppc
#     UC_MODE_PPC32 = 1 << 2, // 32-bit mode
#     UC_MODE_PPC64 = 1 << 3, // 64-bit mode (currently unsupported)
#     UC_MODE_QPX =
#         1 << 4, // Quad Processing eXtensions mode (currently unsupported)

#     // sparc
#     UC_MODE_SPARC32 = 1 << 2, // 32-bit mode
#     UC_MODE_SPARC64 = 1 << 3, // 64-bit mode
#     UC_MODE_V9 = 1 << 4,      // SparcV9 mode (currently unsupported)

#     // riscv
#     UC_MODE_RISCV32 = 1 << 2, // 32-bit mode
#     UC_MODE_RISCV64 = 1 << 3, // 64-bit mode
# '''.split()
# for i in enum:
#     if "UC_" in i:
#         print(f'    printf("{i} : 0x%x\\n",{i});')
# enum1 = '''
#     UC_ARCH_ARM, = 1, // ARM architecture (including Thumb, Thumb-2)
#     UC_ARCH_ARM64,   // ARM-64, also called AArch64
#     UC_ARCH_MIPS,    // Mips architecture
#     UC_ARCH_X86,     // X86 architecture (including x86 & x86-64)
#     UC_ARCH_PPC,     // PowerPC architecture
#     UC_ARCH_SPARC,   // Sparc architecture
#     UC_ARCH_M68K,    // M68K architecture
#     UC_ARCH_RISCV,   // RISCV architecture
#     UC_ARCH_S390X,   // S390X architecture
#     UC_ARCH_TRICORE, // TriCore architecture
#     UC_ARCH_MAX,'''.split()

enum1 = '''typedef enum uc_x86_reg {
    UC_X86_REG_INVALID = 0,
    UC_X86_REG_AH,
    UC_X86_REG_AL,
    UC_X86_REG_AX,
    UC_X86_REG_BH,
    UC_X86_REG_BL,
    UC_X86_REG_BP,
    UC_X86_REG_BPL,
    UC_X86_REG_BX,
    UC_X86_REG_CH,
    UC_X86_REG_CL,
    UC_X86_REG_CS,
    UC_X86_REG_CX,
    UC_X86_REG_DH,
    UC_X86_REG_DI,
    UC_X86_REG_DIL,
    UC_X86_REG_DL,
    UC_X86_REG_DS,
    UC_X86_REG_DX,
    UC_X86_REG_EAX,
    UC_X86_REG_EBP,
    UC_X86_REG_EBX,
    UC_X86_REG_ECX,
    UC_X86_REG_EDI,
    UC_X86_REG_EDX,
    UC_X86_REG_EFLAGS,
    UC_X86_REG_EIP,
    UC_X86_REG_ES = UC_X86_REG_EIP + 2,
    UC_X86_REG_ESI,
    UC_X86_REG_ESP,
    UC_X86_REG_FPSW,
    UC_X86_REG_FS,
    UC_X86_REG_GS,
    UC_X86_REG_IP,
    UC_X86_REG_RAX,
    UC_X86_REG_RBP,
    UC_X86_REG_RBX,
    UC_X86_REG_RCX,
    UC_X86_REG_RDI,
    UC_X86_REG_RDX,
    UC_X86_REG_RIP,
    UC_X86_REG_RSI = UC_X86_REG_RIP + 2,
    UC_X86_REG_RSP,
    UC_X86_REG_SI,
    UC_X86_REG_SIL,
    UC_X86_REG_SP,
    UC_X86_REG_SPL,
    UC_X86_REG_SS,
    UC_X86_REG_CR0,
    UC_X86_REG_CR1,
    UC_X86_REG_CR2,
    UC_X86_REG_CR3,
    UC_X86_REG_CR4,
    UC_X86_REG_CR8 = UC_X86_REG_CR4 + 4,
    UC_X86_REG_DR0 = UC_X86_REG_CR8 + 8,
    UC_X86_REG_DR1,
    UC_X86_REG_DR2,
    UC_X86_REG_DR3,
    UC_X86_REG_DR4,
    UC_X86_REG_DR5,
    UC_X86_REG_DR6,
    UC_X86_REG_DR7,
    UC_X86_REG_FP0 = UC_X86_REG_DR7 + 9,
    UC_X86_REG_FP1,
    UC_X86_REG_FP2,
    UC_X86_REG_FP3,
    UC_X86_REG_FP4,
    UC_X86_REG_FP5,
    UC_X86_REG_FP6,
    UC_X86_REG_FP7,
    UC_X86_REG_K0,
    UC_X86_REG_K1,
    UC_X86_REG_K2,
    UC_X86_REG_K3,
    UC_X86_REG_K4,
    UC_X86_REG_K5,
    UC_X86_REG_K6,
    UC_X86_REG_K7,
    UC_X86_REG_MM0,
    UC_X86_REG_MM1,
    UC_X86_REG_MM2,
    UC_X86_REG_MM3,
    UC_X86_REG_MM4,
    UC_X86_REG_MM5,
    UC_X86_REG_MM6,
    UC_X86_REG_MM7,
    UC_X86_REG_R8,
    UC_X86_REG_R9,
    UC_X86_REG_R10,
    UC_X86_REG_R11,
    UC_X86_REG_R12,
    UC_X86_REG_R13,
    UC_X86_REG_R14,
    UC_X86_REG_R15,
    UC_X86_REG_ST0,
    UC_X86_REG_ST1,
    UC_X86_REG_ST2,
    UC_X86_REG_ST3,
    UC_X86_REG_ST4,
    UC_X86_REG_ST5,
    UC_X86_REG_ST6,
    UC_X86_REG_ST7,
    UC_X86_REG_XMM0,
    UC_X86_REG_XMM1,
    UC_X86_REG_XMM2,
    UC_X86_REG_XMM3,
    UC_X86_REG_XMM4,
    UC_X86_REG_XMM5,
    UC_X86_REG_XMM6,
    UC_X86_REG_XMM7,
    UC_X86_REG_XMM8,
    UC_X86_REG_XMM9,
    UC_X86_REG_XMM10,
    UC_X86_REG_XMM11,
    UC_X86_REG_XMM12,
    UC_X86_REG_XMM13,
    UC_X86_REG_XMM14,
    UC_X86_REG_XMM15,
    UC_X86_REG_XMM16,
    UC_X86_REG_XMM17,
    UC_X86_REG_XMM18,
    UC_X86_REG_XMM19,
    UC_X86_REG_XMM20,
    UC_X86_REG_XMM21,
    UC_X86_REG_XMM22,
    UC_X86_REG_XMM23,
    UC_X86_REG_XMM24,
    UC_X86_REG_XMM25,
    UC_X86_REG_XMM26,
    UC_X86_REG_XMM27,
    UC_X86_REG_XMM28,
    UC_X86_REG_XMM29,
    UC_X86_REG_XMM30,
    UC_X86_REG_XMM31,
    UC_X86_REG_YMM0,
    UC_X86_REG_YMM1,
    UC_X86_REG_YMM2,
    UC_X86_REG_YMM3,
    UC_X86_REG_YMM4,
    UC_X86_REG_YMM5,
    UC_X86_REG_YMM6,
    UC_X86_REG_YMM7,
    UC_X86_REG_YMM8,
    UC_X86_REG_YMM9,
    UC_X86_REG_YMM10,
    UC_X86_REG_YMM11,
    UC_X86_REG_YMM12,
    UC_X86_REG_YMM13,
    UC_X86_REG_YMM14,
    UC_X86_REG_YMM15,
    UC_X86_REG_YMM16,
    UC_X86_REG_YMM17,
    UC_X86_REG_YMM18,
    UC_X86_REG_YMM19,
    UC_X86_REG_YMM20,
    UC_X86_REG_YMM21,
    UC_X86_REG_YMM22,
    UC_X86_REG_YMM23,
    UC_X86_REG_YMM24,
    UC_X86_REG_YMM25,
    UC_X86_REG_YMM26,
    UC_X86_REG_YMM27,
    UC_X86_REG_YMM28,
    UC_X86_REG_YMM29,
    UC_X86_REG_YMM30,
    UC_X86_REG_YMM31,
    UC_X86_REG_ZMM0,
    UC_X86_REG_ZMM1,
    UC_X86_REG_ZMM2,
    UC_X86_REG_ZMM3,
    UC_X86_REG_ZMM4,
    UC_X86_REG_ZMM5,
    UC_X86_REG_ZMM6,
    UC_X86_REG_ZMM7,
    UC_X86_REG_ZMM8,
    UC_X86_REG_ZMM9,
    UC_X86_REG_ZMM10,
    UC_X86_REG_ZMM11,
    UC_X86_REG_ZMM12,
    UC_X86_REG_ZMM13,
    UC_X86_REG_ZMM14,
    UC_X86_REG_ZMM15,
    UC_X86_REG_ZMM16,
    UC_X86_REG_ZMM17,
    UC_X86_REG_ZMM18,
    UC_X86_REG_ZMM19,
    UC_X86_REG_ZMM20,
    UC_X86_REG_ZMM21,
    UC_X86_REG_ZMM22,
    UC_X86_REG_ZMM23,
    UC_X86_REG_ZMM24,
    UC_X86_REG_ZMM25,
    UC_X86_REG_ZMM26,
    UC_X86_REG_ZMM27,
    UC_X86_REG_ZMM28,
    UC_X86_REG_ZMM29,
    UC_X86_REG_ZMM30,
    UC_X86_REG_ZMM31,
    UC_X86_REG_R8B,
    UC_X86_REG_R9B,
    UC_X86_REG_R10B,
    UC_X86_REG_R11B,
    UC_X86_REG_R12B,
    UC_X86_REG_R13B,
    UC_X86_REG_R14B,
    UC_X86_REG_R15B,
    UC_X86_REG_R8D,
    UC_X86_REG_R9D,
    UC_X86_REG_R10D,
    UC_X86_REG_R11D,
    UC_X86_REG_R12D,
    UC_X86_REG_R13D,
    UC_X86_REG_R14D,
    UC_X86_REG_R15D,
    UC_X86_REG_R8W,
    UC_X86_REG_R9W,
    UC_X86_REG_R10W,
    UC_X86_REG_R11W,
    UC_X86_REG_R12W,
    UC_X86_REG_R13W,
    UC_X86_REG_R14W,
    UC_X86_REG_R15W,
    UC_X86_REG_IDTR,
    UC_X86_REG_GDTR,
    UC_X86_REG_LDTR,
    UC_X86_REG_TR,
    UC_X86_REG_FPCW,
    UC_X86_REG_FPTAG,
    UC_X86_REG_MSR, // Model-Specific Register
    UC_X86_REG_MXCSR,
    UC_X86_REG_FS_BASE, // Base regs for x86_64
    UC_X86_REG_GS_BASE,
    UC_X86_REG_FLAGS,
    UC_X86_REG_RFLAGS,
    UC_X86_REG_FIP,
    UC_X86_REG_FCS,
    UC_X86_REG_FDP,
    UC_X86_REG_FDS,
    UC_X86_REG_FOP,
    UC_X86_REG_ENDING // <-- mark the end of the list of registers
} uc_x86_reg;'''.split()
for i in enum1:
    if "UC_" in i:
        if i[-1] == ',':
            print(f'    printf("{i[:-1]} : 0x%x\\n",{i[:-1]});')
        else:
            print(f'    printf("{i[:-1]} : 0x%x\\n",{i});')