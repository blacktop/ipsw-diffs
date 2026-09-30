## kernel

> `System/Library/Kernels/kernel`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA.__data`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__assert`
- `__DATA_CONST.__sdt`
- `__DATA_CONST.__got`
- `__KLDDATA.__init`
- `__KLDDATA.__const`
- `__CTF.__ctf`

```diff

   __TEXT.__text: 0x8cf360
   __TEXT.__const: 0x44db0
   __TEXT.__os_log: 0x47d4b
-  __TEXT.__cstring: 0x9f0bb
+  __TEXT.__cstring: 0x9f07b
   __TEXT.__eh_frame: 0x118
   __DATA.__lock_grp: 0x15f10
   __DATA.__data: 0x83520
   __DATA.__percpu: 0x3de8
   __DATA.__common: 0x1bcda0
-  __DATA_CONST.__const: 0xa1468
+  __DATA_CONST.__const: 0xa1098
   __DATA_CONST.__kalloc_type: 0x17140
   __DATA_CONST.__kalloc_var: 0x7c60
   __DATA_CONST.__assert: 0x974

   __DATA_CONST.__mod_init_func: 0x2c8
   __DATA_CONST.__got: 0x58
   __KLDDATA.__init: 0x22ac0
-  __KLDDATA.__init_entry_set: 0x13428
+  __KLDDATA.__init_entry_set: 0x13308
   __KLDDATA.__const: 0x8ff0
   __KLDDATA.__static_ifinit: 0x8
   __KLDDATA.__cstring: 0x79c

   __CTF.__ctf: 0xddaa5
   Functions: 26465
   Symbols:   23791
-  CStrings:  25551
+  CStrings:  25549
 
CStrings:
- "Perf level 2 topology and cache geometry parameters"
- "perflevel2"
```
