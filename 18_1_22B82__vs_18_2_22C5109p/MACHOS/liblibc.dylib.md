## liblibc.dylib

> `/System/ExclaveKit/usr/lib/system/liblibc.dylib`

```diff

-363.40.2.0.0
-  __TEXT.__text: 0x16958
+365.60.20.0.0
+  __TEXT.__text: 0x15fec
   __TEXT.__auth_stubs: 0x60
-  __TEXT.__cstring: 0x28bc
+  __TEXT.__cstring: 0x28f6
   __TEXT.__const: 0x1aaac
   __TEXT.__unwind_info: 0xd0
   __DATA.__auth_got: 0x30

   __DATA.__data: 0x10
   __DATA.__thread_vars: 0xa8
   __DATA.__thread_bss: 0x70
-  __DATA.__bss: 0x2c0
+  __DATA.__bss: 0x2c8
   __DATA.__common: 0x734
   - /System/ExclaveKit/usr/lib/system/libdyld.dylib
   - /System/ExclaveKit/usr/lib/system/libsystem_m.dylib
   - /System/ExclaveKit/usr/lib/system/libsystem_malloc.dylib
-  Functions: 759
-  Symbols:   523
-  CStrings:  333
+  Functions: 764
+  Symbols:   527
+  CStrings:  336
 
Symbols:
+ _arc4random_uniform
+ _backtrace_shift_sym_from_fp
+ _pthread_key_init_np
+ _tss_init_np
CStrings:
+ "arc4random_uniform"
+ "bound > 1"
+ "src/libc/stdlib/arc4random.c"

```
