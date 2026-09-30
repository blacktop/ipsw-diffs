## libSparseBLAS.dylib

> `/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparseBLAS.dylib`

```diff

-1545.0.0.0.0
-  __TEXT.__text: 0x256b0
+1545.0.6.0.0
+  __TEXT.__text: 0x256a4
   __TEXT.__auth_stubs: 0x4a0
   __TEXT.__const: 0x70
   __TEXT.__oslogstring: 0x53
   __TEXT.__cstring: 0x201
-  __TEXT.__gcc_except_tab: 0x20
+  __TEXT.__gcc_except_tab: 0x2c
   __TEXT.__unwind_info: 0x3c0
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x8a0

   - /System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libBLAS.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 1392ADE1-DDE6-30BB-BFEC-ED93C028CEF2
-  Functions: 293
-  Symbols:   616
+  UUID: 92382C29-DE99-36FE-9943-7D536CCC1047
+  Functions: 292
+  Symbols:   614
   CStrings:  25
 
Symbols:
+ GCC_except_table14
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZnwmSt19__type_descriptor_t
- GCC_except_table15
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __Znwm
Functions:
~ __ZN6lapack8hardware5query17sysctlQueryStringEPKc : 180 -> 308
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
~ _sparse_permute_rows_double : 1176 -> 1168
~ _sparse_permute_cols_double : 1176 -> 1168
~ _sparse_permute_rows_float_complex : 1196 -> 1188
~ _sparse_permute_cols_float_complex : 1196 -> 1188
~ _sparse_storage_convert_float : 1968 -> 1984
~ _sparse_storage_convert_double : 1952 -> 1968
~ _sparse_storage_convert_float_complex : 1952 -> 1968
~ _sparse_storage_convert_double_complex : 1968 -> 1984

```
