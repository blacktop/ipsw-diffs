## CoreRoutineDiagnostics

> `/System/Library/PrivateFrameworks/CoreRoutineDiagnostics.framework/CoreRoutineDiagnostics`

```diff

-1123.0.3.0.0
-  __TEXT.__text: 0xe6ac
-  __TEXT.__objc_methlist: 0xabc
+1123.0.6.0.0
+  __TEXT.__text: 0xe728
+  __TEXT.__objc_methlist: 0xac4
   __TEXT.__dlopen_cstrs: 0x6d
   __TEXT.__const: 0x170
   __TEXT.__gcc_except_tab: 0x3b4
   __TEXT.__oslogstring: 0x1b79
-  __TEXT.__cstring: 0x1768
+  __TEXT.__cstring: 0x1796
   __TEXT.__ustring: 0x7c
   __TEXT.__unwind_info: 0x478
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8d0
+  __DATA_CONST.__objc_selrefs: 0x8d8
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__got: 0x188
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x18c0
+  __AUTH_CONST.__cfstring: 0x18e0
   __AUTH_CONST.__objc_const: 0xed8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x120

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 268
-  Symbols:   653
-  CStrings:  360
+  Functions: 269
+  Symbols:   654
+  CStrings:  361
 
Symbols:
+ -[RTBugCaptureManager _generateRadarDescriptionForReason:diagnosticsMask:additionalDescription:]
+ -[RTBugCaptureManager captureBugForReason:module:category:diagnosticsMask:additionalDescription:handler:]
+ GCC_except_table23
+ GCC_except_table27
+ GCC_except_table40
+ GCC_except_table42
+ ___105-[RTBugCaptureManager captureBugForReason:module:category:diagnosticsMask:additionalDescription:handler:]_block_invoke
+ ___105-[RTBugCaptureManager captureBugForReason:module:category:diagnosticsMask:additionalDescription:handler:]_block_invoke_2
+ ___105-[RTBugCaptureManager captureBugForReason:module:category:diagnosticsMask:additionalDescription:handler:]_block_invoke_3
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80bs88r_e17_v16?0"NSArray"8ls32l8s40l8s48l8r88l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_88_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s64l8s48l8s56l8
- -[RTBugCaptureManager _generateRadarDescriptionForReason:diagnosticsMask:]
- GCC_except_table22
- GCC_except_table26
- GCC_except_table39
- GCC_except_table41
- ___83-[RTBugCaptureManager captureBugForReason:module:category:diagnosticsMask:handler:]_block_invoke
- ___83-[RTBugCaptureManager captureBugForReason:module:category:diagnosticsMask:handler:]_block_invoke_2
- ___83-[RTBugCaptureManager captureBugForReason:module:category:diagnosticsMask:handler:]_block_invoke_3
- ___block_descriptor_104_e8_32s40s48s56s64s72bs80r_e17_v16?0"NSArray"8ls32l8s40l8s48l8r80l8s56l8s64l8s72l8
- ___block_descriptor_80_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
CStrings:
+ "-[RTBugCaptureManager captureBugForReason:module:category:diagnosticsMask:additionalDescription:handler:]"
+ "Diagnostic Detail:\n%@\n\n"
- "-[RTBugCaptureManager captureBugForReason:module:category:diagnosticsMask:handler:]"
```
