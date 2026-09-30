## kernel

> `/System/Library/Kernels/kernel`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA.__data`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__assert`
- `__DATA_CONST.__kern_brk_desc`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__got`
- `__KLDDATA.__init`
- `__KLDDATA.__const`

```diff

-12377.161.13.0.0
-  __TEXT.__text: 0x8cdcf0
+12377.161.14.0.0
+  __TEXT.__text: 0x8ce1c0
   __TEXT.__const: 0x44d90
   __TEXT.__os_log: 0x47cfb
-  __TEXT.__cstring: 0x9efab
+  __TEXT.__cstring: 0x9f03b
   __TEXT.__eh_frame: 0x118
   __DATA.__lock_grp: 0x15f10
   __DATA.__data: 0x83520
   __DATA.__percpu: 0x3de8
-  __DATA.__common: 0x1bcd80
-  __DATA.__bss: 0x7e8a0
-  __DATA_CONST.__const: 0xa0f58
+  __DATA.__common: 0x1bcda0
+  __DATA.__bss: 0x7e8c0
+  __DATA_CONST.__const: 0xa1098
   __DATA_CONST.__kalloc_type: 0x17140
   __DATA_CONST.__kalloc_var: 0x7c60
   __DATA_CONST.__assert: 0x974
   __DATA_CONST.__kern_brk_desc: 0x60
   __DATA_CONST.__sdt_cstring: 0x6e50
-  __DATA_CONST.__sdt: 0xeb20
+  __DATA_CONST.__sdt: 0xeb80
   __DATA_CONST.__mod_init_func: 0x2c8
   __DATA_CONST.__got: 0x58
   __KLDDATA.__init: 0x22ac0
-  __KLDDATA.__init_entry_set: 0x132a8
+  __KLDDATA.__init_entry_set: 0x13308
   __KLDDATA.__const: 0x8ff0
   __KLDDATA.__static_ifinit: 0x8
   __KLDDATA.__cstring: 0x79c

   __PRELINK_TEXT.__text: 0x0
   __PRELINK_INFO.__info: 0x0
   __LINKINFO.__symbolsets: 0x4d6d4
-  __CTF.__ctf: 0xdd94f
-  Functions: 26460
-  Symbols:   23786
-  CStrings:  25541
+  __CTF.__ctf: 0xdd9a2
+  Functions: 26461
+  Symbols:   23791
+  CStrings:  25546
 
Symbols:
+ _memory_object_mark_read_only
+ _vm_object_readonly_copy_overwrite
+ _vm_object_readonly_fault
+ _vm_object_readonly_fault_page
+ _vm_object_readonly_iopl_request
CStrings:
+ "VM object is read-only (decmpfs?)\n"
+ "object_readonly_copy_overwrite"
+ "object_readonly_fault"
+ "object_readonly_fault_page"
+ "object_readonly_iopl_request"
```
