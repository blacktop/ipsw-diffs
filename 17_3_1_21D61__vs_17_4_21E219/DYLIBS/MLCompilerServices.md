## MLCompilerServices

> `/System/Library/PrivateFrameworks/MLCompilerServices.framework/MLCompilerServices`

```diff

-95.0.0.0.0
-  __TEXT.__text: 0x12954
-  __TEXT.__auth_stubs: 0xac0
-  __TEXT.__gcc_except_tab: 0xd88
-  __TEXT.__cstring: 0x1ad7
-  __TEXT.__oslogstring: 0x283
-  __TEXT.__const: 0x1a8
+3304.5.1.0.0
+  __TEXT.__text: 0x12fdc
+  __TEXT.__auth_stubs: 0xaa0
+  __TEXT.__gcc_except_tab: 0xda4
+  __TEXT.__cstring: 0x1b9d
+  __TEXT.__oslogstring: 0x2bb
+  __TEXT.__const: 0x1a7
   __TEXT.__dlopen_cstrs: 0x6b
-  __TEXT.__unwind_info: 0x604
+  __TEXT.__unwind_info: 0x60c
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__const: 0x80
   __AUTH_CONST.__const: 0x7a0
   __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x568
+  __AUTH_CONST.__auth_got: 0x558
   __DATA.__bss: 0x30
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 272
-  Symbols:   233
-  CStrings:  263
+  Functions: 278
+  Symbols:   231
+  CStrings:  270
 
Symbols:
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strERKNS_12basic_stringIcS2_S4_EE
CStrings:
+ "--llvm-ir"
+ "--use-fixed-point"
+ ".dylib"
+ "Can't open BNNSGraph model at %s"
+ "Can't open model at %s"
+ "Outputs LLVM IR files to /tmp or the directory specified with --save-temps"
+ "Quantize float-point model to use fixed-point arithmetics. (Supported values: 'i32_16')"

```
