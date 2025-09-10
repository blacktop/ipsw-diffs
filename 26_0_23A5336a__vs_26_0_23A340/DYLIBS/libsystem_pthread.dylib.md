## libsystem_pthread.dylib

> `/usr/lib/system/libsystem_pthread.dylib`

```diff

 539.0.0.0.0
-  __TEXT.__text: 0xa4e4
+  __TEXT.__text: 0xa524
   __TEXT.__auth_stubs: 0x450
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0xdaa
+  __TEXT.__cstring: 0xdbd
   __TEXT.__unwind_info: 0x340
   __DATA_CONST.__got: 0x30
   __AUTH_CONST.__auth_got: 0x228
   __DATA.__data: 0x8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x801c
+  __DATA.__bss: 0x8024
   __DATA.__common: 0x2
   __DATA_DIRTY.__data: 0x40
   __DATA_DIRTY.__common: 0x34

   - /usr/lib/system/libmacho.dylib
   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_platform.dylib
-  UUID: BDD625F0-F441-32A2-BD93-D5A169D972DC
+  UUID: 187BDC44-7AB8-3BC2-9973-DEBC0798EAA4
   Functions: 311
-  Symbols:   600
-  CStrings:  66
+  Symbols:   601
+  CStrings:  67
 
Symbols:
+ _pthread_has_sec_transition
Functions:
~ ___pthread_init : 1144 -> 1184
~ _pthread_stack_frame_decode_np : 36 -> 60
CStrings:
+ "has_sec_transition"

```
