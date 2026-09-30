## libauditd.0.dylib

> `/usr/lib/libauditd.0.dylib`

```diff

 89.0.0.0.0
-  __TEXT.__text: 0x18b0
+  __TEXT.__text: 0x18b4
   __TEXT.__auth_stubs: 0x500
   __TEXT.__cstring: 0x40d
-  __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__got: 0x10
+  __TEXT.__unwind_info: 0xb0
+  __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0xa0
   __AUTH_CONST.__auth_got: 0x280
   __DATA.__data: 0x8
   __DATA.__bss: 0x110
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  UUID: 659FC7B7-6C96-3C1D-A129-892A611A4959
+  UUID: B026E2C4-1D0C-3104-A331-053D245A12F1
   Functions: 19
   Symbols:   105
   CStrings:  45
Functions:
~ _auditd_expire_trails : 1364 -> 1344
~ _auditd_read_dirs : 888 -> 896
~ _auditd_set_evcmap : 228 -> 236
~ _auditd_swap_trail : 540 -> 528
~ _auditd_gen_record : 468 -> 480
~ _auditd_new_curlink : 736 -> 740
~ _audit_quick_stop : 364 -> 368

```
