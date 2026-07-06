## libSparse.dylib

> `/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparse.dylib`

```diff

-  __TEXT.__text: 0x1671d8
+  __TEXT.__text: 0x168a38
   __TEXT.__const: 0x700
-  __TEXT.__cstring: 0x4e08
+  __TEXT.__cstring: 0x4e02
   __TEXT.__oslogstring: 0x1d06
   __TEXT.__gcc_except_tab: 0xa4c
-  __TEXT.__unwind_info: 0x16a0
-  __TEXT.__eh_frame: 0x2a8
+  __TEXT.__unwind_info: 0x1690
+  __TEXT.__eh_frame: 0x208
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0xad0
+  __DATA_CONST.__const: 0xab0
   __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x1d0
+  __AUTH_CONST.__const: 0x1b0
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__auth_got: 0x618
+  __AUTH_CONST.__auth_got: 0x638
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
-  Functions: 1967
-  Symbols:   676
-  CStrings:  698
+  Functions: 1963
+  Symbols:   680
+  CStrings:  697
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__weak_got : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH.__thread_vars : content changed
Symbols:
+ _getHardwareInfo
+ _sparse_csc_spmv_complex_double
+ _sparse_csc_spmv_complex_float
+ _sparse_csc_spmv_double
+ _sparse_csc_spmv_float
- _dispatch_once
CStrings:
- "v8@?0"

```
