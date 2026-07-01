## libSparse.dylib

> `/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparse.dylib`

```diff

-  __TEXT.__text: 0x160374
-  __TEXT.__auth_stubs: 0xc30
-  __TEXT.__const: 0x6f0
-  __TEXT.__cstring: 0x4d5c
-  __TEXT.__oslogstring: 0x1c5d
-  __TEXT.__gcc_except_tab: 0xa28
-  __TEXT.__unwind_info: 0x17b8
-  __TEXT.__eh_frame: 0x890
+  __TEXT.__text: 0x1622dc
+  __TEXT.__auth_stubs: 0xc70
+  __TEXT.__const: 0x700
+  __TEXT.__cstring: 0x4d93
+  __TEXT.__oslogstring: 0x1c97
+  __TEXT.__gcc_except_tab: 0xa58
+  __TEXT.__unwind_info: 0x17a0
+  __TEXT.__eh_frame: 0x7f0
   __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0xad0
-  __AUTH_CONST.__auth_got: 0x620
-  __AUTH_CONST.__const: 0x1d0
+  __DATA_CONST.__const: 0xab0
+  __AUTH_CONST.__auth_got: 0x640
+  __AUTH_CONST.__const: 0x1b0
   __AUTH.__thread_vars: 0xd8
   __AUTH.__thread_data: 0xc
   __AUTH.__thread_bss: 0x8818
   __DATA.__data: 0x14
   __DATA.__common: 0x98
-  __DATA.__bss: 0x12018
+  __DATA.__bss: 0x12008
   - /System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBLAS.dylib
   - /System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libLAPACK.dylib
   - /System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparseBLAS.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 1959
-  Symbols:   675
-  CStrings:  694
+  Functions: 1956
+  Symbols:   679
+  CStrings:  695
 
Sections:
~ __DATA_CONST.__got : content changed
Symbols:
+ _getHardwareInfo
+ _sparse_csc_spmv_complex_double
+ _sparse_csc_spmv_complex_float
+ _sparse_csc_spmv_double
+ _sparse_csc_spmv_float
- _dispatch_once
CStrings:
+ "Unexpected matrix storage scheme.\n"
+ "Workspace size calculation overflowed in partialLURefactor.\n"
- "Unexpected matrix storage scheme %d.\n"
- "v8@?0"

```
