## seputil

> `/usr/libexec/seputil`

```diff

-880.60.4.0.0
-  __TEXT.__text: 0x15984
-  __TEXT.__auth_stubs: 0xa30
-  __TEXT.__cstring: 0x5e52
-  __TEXT.__const: 0xbf4
-  __TEXT.__oslogstring: 0x5e
+880.62.3.0.0
+  __TEXT.__text: 0x15e7c
+  __TEXT.__auth_stubs: 0xa40
+  __TEXT.__cstring: 0x5f2f
+  __TEXT.__const: 0xc0c
+  __TEXT.__oslogstring: 0x6f
   __TEXT.__gcc_except_tab: 0x274
-  __TEXT.__unwind_info: 0x488
-  __DATA_CONST.__auth_got: 0x520
+  __TEXT.__unwind_info: 0x4a0
+  __DATA_CONST.__auth_got: 0x528
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x140
+  __DATA_CONST.__const: 0x180
   __DATA_CONST.__cfstring: 0x80
-  __DATA.__data: 0xc40
+  __DATA.__data: 0xc60
   __DATA.__common: 0xc
   __DATA.__bss: 0x8f5
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 1E478F25-FEEF-3CE4-B4F5-EE285C430260
-  Functions: 466
-  Symbols:   195
-  CStrings:  728
+  UUID: EFD8A84E-9699-3218-96F0-08A228D43AEB
+  Functions: 472
+  Symbols:   196
+  CStrings:  735
 
Symbols:
+ __os_log_debug_impl
CStrings:
+ "\t\t--reseed-xnu-prng        Reseed XNU's PRNG by getting entropy out of SEP's TRNG"
+ "%s: XNU PRNG reseeding failed: 0x%x\n"
+ "SEPUTIL TRNG: %s"
+ "daemonize-reseed"
+ "daemonize_xpc_reseed"
+ "daemonize_xpc_reseed finished: failure"
+ "daemonize_xpc_reseed finished: success"
+ "daemonize_xpc_reseed running"
- "%s: Executed xnu PRNG reseeding dummy API\n"

```
