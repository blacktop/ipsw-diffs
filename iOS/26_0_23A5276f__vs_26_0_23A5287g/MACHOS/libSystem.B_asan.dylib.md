## libSystem.B_asan.dylib

> `/usr/lib/libSystem.B_asan.dylib`

```diff

 1356.0.0.0.0
-  __TEXT.__text: 0x748
-  __TEXT.__auth_stubs: 0x480
+  __TEXT.__text: 0x6d0
+  __TEXT.__auth_stubs: 0x450
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x188
+  __TEXT.__cstring: 0x172
   __TEXT.__oslogstring: 0x35
   __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0x240
+  __DATA_CONST.__auth_got: 0x228
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0xe0
   __DATA.__data: 0x8

   - /usr/lib/system/libunwind.dylib
   - /usr/lib/system/libxpc.dylib
   - @rpath/libclang_rt.asan_ios_dynamic.dylib
-  UUID: C33A37CE-5B92-39CD-9F08-511A9591D892
+  UUID: 5F75D07A-8B99-380D-9F40-768FBAD1ABB1
   Functions: 23
-  Symbols:   117
-  CStrings:  12
+  Symbols:   114
+  CStrings:  11
 
Symbols:
- _dyld_program_sdk_at_least
- _getenv
- _strtol
Functions:
~ _libSystem_initializer : 988 -> 868
CStrings:
- "SYSTEM_VERSION_COMPAT"

```
