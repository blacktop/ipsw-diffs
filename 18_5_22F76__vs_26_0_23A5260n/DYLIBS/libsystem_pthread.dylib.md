## libsystem_pthread.dylib

> `/usr/lib/system/libsystem_pthread.dylib`

```diff

-536.0.0.0.0
+538.0.0.0.0
   __TEXT.__text: 0xa500
   __TEXT.__auth_stubs: 0x450
   __TEXT.__const: 0x120

   __DATA_CONST.__got: 0x30
   __AUTH_CONST.__auth_got: 0x228
   __DATA.__data: 0x8
-  __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x403c
+  __DATA.__crash_info: 0x148
+  __DATA.__bss: 0x801c
   __DATA.__common: 0x2
   __DATA_DIRTY.__data: 0x40
   __DATA_DIRTY.__common: 0x34
-  __DATA_DIRTY.__bss: 0x4020
+  __DATA_DIRTY.__bss: 0x5020
   - /usr/lib/system/libdyld.dylib
   - /usr/lib/system/libmacho.dylib
   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_platform.dylib
-  UUID: B37430D8-E3AF-33E4-81E1-FAED9EE26E8A
+  UUID: 5AB1DF7E-EDBB-3E57-A126-9704F9D5A885
   Functions: 310
-  Symbols:   600
+  Symbols:   598
   CStrings:  65
 
Functions:
~ __pthread_cond_updateval : 248 -> 244
~ _pthread_cond_broadcast : 788 -> 792

```
