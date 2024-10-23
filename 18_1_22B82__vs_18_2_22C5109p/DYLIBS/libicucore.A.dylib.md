## libicucore.A.dylib

> `/usr/lib/libicucore.A.dylib`

```diff

-74221.0.0.0.0
-  __TEXT.__text: 0x24f894
-  __TEXT.__auth_stubs: 0x6b0
+74222.203.0.0.0
+  __TEXT.__text: 0x24f824
+  __TEXT.__auth_stubs: 0x6c0
   __TEXT.__const: 0x600a0
   __TEXT.__cstring: 0x8b9c
+  __TEXT.__oslogstring: 0xf0
   __TEXT.__ustring: 0x4986
-  __TEXT.__oslogstring: 0x86
   __TEXT.__unwind_info: 0x58
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x108d0
-  __AUTH_CONST.__auth_got: 0x358
+  __AUTH_CONST.__auth_got: 0x360
   __AUTH_CONST.__auth_ptr: 0x28
   __AUTH_CONST.__const: 0x11da8
   __DATA.__data: 0x928
-  __DATA.__bss: 0x12b0
+  __DATA.__bss: 0x1290
   __DATA_DIRTY.__data: 0x9c
   __DATA_DIRTY.__bss: 0x1760
   __DATA_DIRTY.__common: 0x30
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 11914
-  Symbols:   8601
-  CStrings:  3802
+  Functions: 11915
+  Symbols:   8602
+  CStrings:  3803
 
Symbols:
+ __os_log_error_impl
CStrings:
+ "ICU's u_setMemoryFunctions() is not safe and has been disabled. Please remove calls to it from your code."

```
