## libunwind.dylib

> `/usr/lib/system/libunwind.dylib`

```diff

-1800.85.0.0.0
-  __TEXT.__text: 0x67b0
+1900.125.0.0.0
+  __TEXT.__text: 0x69ac
   __TEXT.__auth_stubs: 0x110
   __TEXT.__cstring: 0xa7a
-  __TEXT.__unwind_info: 0x168
+  __TEXT.__unwind_info: 0x160
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x310
   __AUTH_CONST.__auth_got: 0x88
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x88
+  __AUTH_CONST.__const: 0x90
   __DATA.__data: 0x1b0
   __DATA.__bss: 0x851
   __DATA_DIRTY.__bss: 0x8

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  Functions: 83
-  Symbols:   109
+  Functions: 77
+  Symbols:   111
   CStrings:  128
 
Symbols:
+ _unw_resume_with_frames_walked

```
