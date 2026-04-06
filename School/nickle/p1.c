#include "iloc.h"
#include "stdio.h"

const size_t PROGRAM_USER_REGS = 32;
const size_t PROGRAM_MEM_SIZE  = 65536;

const data_desc_t STATIC_DATA[] = {
};

const size_t STATIC_COUNT = sizeof(STATIC_DATA) / sizeof(STATIC_DATA[0]);

void iloc_main(cpu_t* cpu) {
    iloc_loadI(cpu, 10, 10);
    iloc_loadI(cpu, 65, 12);
    iloc_loadI(cpu, 90, 13);
    iloc_loadI(cpu, 97, 14);
    iloc_loadI(cpu, 122, 15);
    iloc_loadI(cpu, 32, 16);
    iloc_loadI(cpu, 0, 0);
    iloc_p_str(cpu, get_r_argv_idx(cpu));
    iloc_p_char(cpu, 10);
    iloc_i2i(cpu, get_r_argv_idx(cpu), 2);

loop:
    iloc_cload(cpu, 2, 3);
    iloc_cmp_EQ(cpu, 3, 0, 4);
    if (get_reg(cpu,4)) goto end; else goto process;

process:
    iloc_cmp_GE(cpu, 3, 12, 5);
    iloc_cmp_LE(cpu, 3, 13, 6);
    iloc_and(cpu, 5, 6, 7);
    if (get_reg(cpu,7)) goto to_lower; else goto check_lower;

to_lower:
    iloc_add(cpu, 3, 16, 3);
    goto print_char;

check_lower:
    iloc_cmp_GE(cpu, 3, 14, 8);
    iloc_cmp_LE(cpu, 3, 15, 9);
    iloc_and(cpu, 8, 9, 11);
    if (get_reg(cpu,11)) goto to_upper; else goto print_char;

to_upper:
    iloc_sub(cpu, 3, 16, 3);

print_char:
    iloc_p_char(cpu, 3);
    iloc_addI(cpu, 2, 1, 2);
    goto loop;

end:
    iloc_p_char(cpu, 10);
    iloc_halt(cpu);
}
