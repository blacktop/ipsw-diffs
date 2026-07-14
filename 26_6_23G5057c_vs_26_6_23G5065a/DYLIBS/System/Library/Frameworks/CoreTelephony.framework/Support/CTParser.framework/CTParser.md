## CTParser

> `/System/Library/Frameworks/CoreTelephony.framework/Support/CTParser.framework/CTParser`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__DATA.__data`

```diff

-  __TEXT.__text: 0x59fc
-  __TEXT.__auth_stubs: 0x4b0
+  __TEXT.__text: 0x58ec
+  __TEXT.__auth_stubs: 0x4a0
   __TEXT.__const: 0x515
-  __TEXT.__gcc_except_tab: 0x664
+  __TEXT.__gcc_except_tab: 0x66c
   __TEXT.__cstring: 0xe5
-  __TEXT.__oslogstring: 0x16f
-  __TEXT.__unwind_info: 0x4d0
+  __TEXT.__oslogstring: 0x154
+  __TEXT.__unwind_info: 0x4b8
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x18
-  __AUTH_CONST.__auth_got: 0x260
+  __AUTH_CONST.__auth_got: 0x258
   __AUTH_CONST.__const: 0x738
   __DATA.__data: 0x30
   - /System/Library/Frameworks/CoreTelephony.framework/Support/libCellularDecoders.dylib

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 226
-  Symbols:   452
-  CStrings:  33
+  Functions: 224
+  Symbols:   450
+  CStrings:  32
 
Symbols:
+ GCC_except_table24
+ GCC_except_table34
+ GCC_except_table46
+ GCC_except_table54
+ GCC_except_table62
+ GCC_except_table65
- GCC_except_table25
- GCC_except_table50
- GCC_except_table57
- GCC_except_table61
- GCC_except_table66
- GCC_except_table67
- __ZNK3xpc4dict15to_debug_stringEv
- __os_log_debug_impl
CStrings:
- "#D Received XPC object: %s"
```
