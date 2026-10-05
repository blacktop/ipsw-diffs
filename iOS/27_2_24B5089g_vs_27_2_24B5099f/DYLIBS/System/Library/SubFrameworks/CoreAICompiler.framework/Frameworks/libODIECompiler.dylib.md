## libODIECompiler.dylib

> `/System/Library/SubFrameworks/CoreAICompiler.framework/Frameworks/libODIECompiler.dylib`

```diff

-3605.5.4.0.0
-  __TEXT.__text: 0xc46f50
+3605.6.4.0.0
+  __TEXT.__text: 0xc4759c
   __TEXT.__init_offsets: 0x30
   __TEXT.__const: 0x2a1c
   __TEXT.__oslogstring: 0x3b
-  __TEXT.__cstring: 0xab996
-  __TEXT.__unwind_info: 0x371c0
+  __TEXT.__cstring: 0xaba47
+  __TEXT.__unwind_info: 0x371c8
   __TEXT.__eh_frame: 0x128
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x27b8

   __DATA.__common: 0x2660
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 74696
-  Symbols:   83177
-  CStrings:  11455
+  Functions: 74699
+  Symbols:   83180
+  CStrings:  11459
 
Symbols:
+ __ZN4llvm15SmallVectorImplIPN4mlir9OperationEE6appendINS1_17ValueUserIteratorINS1_16ValueUseIteratorINS1_9OpOperandEEES8_EEvEEvT_SB_
+ __ZN4mlir10DiagnosticlsINS_16RankedTensorTypeEEENSt3__19enable_ifIXaantsr3std14is_convertibleIT_N4llvm9StringRefEEE5valuesr3std16is_constructibleINS_18DiagnosticArgumentES5_EE5valueERS0_E4typeEOS5_
+ __ZN4mlir12matchPatternINS_6detail18constant_op_binderINS_19DenseFPElementsAttrEEEEEbNS_5ValueERKT_
CStrings:
+ "3605.6.4"
+ "offset1 must be statically shaped, but got "
+ "offset2 must be statically shaped, but got "
+ "per-axis quantization requires a constant axis"
+ "scale must be statically shaped, but got "
- "3605.5.4"
```
