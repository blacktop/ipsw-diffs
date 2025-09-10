## libsystem_pthread_debug.dylib

> `/System/DriverKit/usr/lib/system/libsystem_pthread_debug.dylib`

```diff

 539.0.0.0.0
-  __TEXT.__text: 0x1bfc4
+  __TEXT.__text: 0x1c018
   __TEXT.__auth_stubs: 0x430
   __TEXT.__const: 0xcc
-  __TEXT.__cstring: 0xbfd
+  __TEXT.__cstring: 0xc10
   __TEXT.__unwind_info: 0x290
   __DATA_CONST.__got: 0x30
   __AUTH_CONST.__auth_got: 0x218
   __DATA.__data: 0x1c
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x18
   __DATA.__common: 0x2
   __DATA_DIRTY.__data: 0x3c
   __DATA_DIRTY.__common: 0x30

   - /System/DriverKit/usr/lib/system/libdyld.dylib
   - /System/DriverKit/usr/lib/system/libsystem_kernel.dylib
   - /System/DriverKit/usr/lib/system/libsystem_platform.dylib
-  UUID: 05345884-348F-3A7D-87B9-881902AB5113
+  UUID: 713B8721-94D8-390B-96B7-1F389CD9E8E0
   Functions: 306
-  Symbols:   425
-  CStrings:  57
+  Symbols:   426
+  CStrings:  58
 
Symbols:
+ _pthread_has_sec_transition
Functions:
~ ___pthread_init : 1684 -> 1732
~ _pthread_stack_frame_decode_np : 116 -> 152
CStrings:
+ "has_sec_transition"

```
