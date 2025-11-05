## libunwind.dylib

> `/usr/lib/system/libunwind.dylib`

```diff

-1800.85.0.0.0
-  __TEXT.__text: 0x67b8
+1900.125.0.0.0
+  __TEXT.__text: 0x69b4
   __TEXT.__auth_stubs: 0x110
   __TEXT.__cstring: 0xa7a
-  __TEXT.__unwind_info: 0x168
+  __TEXT.__unwind_info: 0x160
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x310
   __AUTH_CONST.__auth_got: 0x88
-  __AUTH_CONST.__const: 0x88
+  __AUTH_CONST.__const: 0x90
   __DATA.__data: 0x1b0
   __DATA.__bss: 0x859
   - /usr/lib/system/libcompiler_rt.dylib

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  UUID: BEFBB85F-B46E-3C52-9A92-2F8EE957E3D9
-  Functions: 83
-  Symbols:   121
+  UUID: 44BBA430-6949-3963-9603-BEF7A7A24D1C
+  Functions: 77
+  Symbols:   123
   CStrings:  128
 
Symbols:
+ __ZN9libunwind12UnwindCursorINS_17LocalAddressSpaceENS_15Registers_arm64EE15setWalkedFramesEj
+ __ZN9libunwind15Registers_arm648returntoEj
+ ___unw_resume_with_frames_walked
+ _unw_resume_with_frames_walked
- __ZN9libunwind15Registers_arm6411setRegisterEiy
- __ZNK9libunwind15Registers_arm6411getRegisterEi

```
