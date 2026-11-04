## libODIECompiler.dylib

> `/System/Library/SubFrameworks/CoreAICompiler.framework/Frameworks/libODIECompiler.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-3605.6.4.0.0
-  __TEXT.__text: 0xc4759c
+3610.5.1.0.0
+  __TEXT.__text: 0xc478c8
   __TEXT.__init_offsets: 0x30
   __TEXT.__const: 0x2a1c
   __TEXT.__oslogstring: 0x3b
   __TEXT.__cstring: 0xaba47
-  __TEXT.__unwind_info: 0x371c8
+  __TEXT.__unwind_info: 0x371d8
   __TEXT.__eh_frame: 0x128
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x27b8

   __AUTH_CONST.__const: 0x5db48
   __AUTH_CONST.__weak_auth_got: 0x48
   __AUTH_CONST.__auth_got: 0x6f8
-  __AUTH.__data: 0x6098
+  __AUTH.__data: 0x60a0
   __AUTH.__thread_vars: 0x108
   __AUTH.__thread_bss: 0x230
   __DATA.__data: 0x42e0
   __DATA.__common: 0x2660
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 74699
-  Symbols:   83180
+  Functions: 74703
+  Symbols:   83184
   CStrings:  11459
 
Symbols:
+ __ZN4llvm12DenseMapBaseINS_8DenseMapINS_9StringRefENS_6detail13DenseSetEmptyENS_12DenseMapInfoIS2_vEENS3_12DenseSetPairIS2_EEEES2_S4_S6_S8_E24lookupOrInsertIntoBucketIRKS2_JEEENSt3__14pairIPS8_bEEOT_DpOT0_
+ __ZN4llvm12function_refIFvPN4mlir9OperationEEE11callback_fnIZNS1_6detail4walkILNS1_9WalkOrderE1ENS1_15ForwardIteratorEZNS1_4ODIE8Compiler13SerializationL14invokeRewriterENS1_8ModuleOpERKNSC_14ModuleRewriterERKNSt3__18optionalINSI_4__fs10filesystem4pathEEERKSM_E3$_0NS1_6coreai10ConstantOpEvEENSI_9enable_ifIXaantsr4llvm9is_one_ofIT2_S3_PNS1_6RegionEPNS1_5BlockEEE5valuesr3std7is_sameIT3_vEE5valueES11_E4typeES3_OT1_EUlS3_E_EEvlS3_
+ __ZN4llvm12function_refIFvRKNS_5TwineEEE11callback_fnIZN4mlir4ODIE8Compiler13SerializationL14invokeRewriterENS7_8ModuleOpERKNS9_14ModuleRewriterERKNSt3__18optionalINSF_4__fs10filesystem4pathEEERKSJ_E3$_1EEvlS3_
+ __ZN4mlir4ODIE8Compiler4capi6detailL17get_resource_keysE33odiec_external_rewriter_payload_tPFvPKcxPvES7_
+ __ZNSt3__111__find_loopB9fqn220106IPN4llvm9StringRefES3_S2_NS_10__identityEEET_S5_T0_RKT1_RT2_
- __ZN4llvm12function_refIFvRKNS_5TwineEEE11callback_fnIZN4mlir4ODIE8Compiler13SerializationL14invokeRewriterENS7_8ModuleOpERKNS9_14ModuleRewriterERKNSt3__18optionalINSF_4__fs10filesystem4pathEEERKSJ_E3$_0EEvlS3_
Functions:
+ __ZN4mlir4ODIE8Compiler4capi6detailL17get_resource_keysE33odiec_external_rewriter_payload_tPFvPKcxPvES7_
~ _odiec_initialize : 308 -> 300
+ __ZN4llvm12DenseMapBaseINS_8DenseMapINS_9StringRefENS_6detail13DenseSetEmptyENS_12DenseMapInfoIS2_vEENS3_12DenseSetPairIS2_EEEES2_S4_S6_S8_E24lookupOrInsertIntoBucketIRKS2_JEEENSt3__14pairIPS8_bEEOT_DpOT0_
+ __ZNSt3__111__find_loopB9fqn220106IPN4llvm9StringRefES3_S2_NS_10__identityEEET_S5_T0_RKT1_RT2_
~ __ZN4mlir4ODIE8Compiler13Serialization13rewriteModuleENS_8ModuleOpERKNS1_14ModuleRewriterERKNSt3__18optionalINS7_4__fs10filesystem4pathEEERKSB_b : 1228 -> 1452
+ __ZN4llvm12function_refIFvPN4mlir9OperationEEE11callback_fnIZNS1_6detail4walkILNS1_9WalkOrderE1ENS1_15ForwardIteratorEZNS1_4ODIE8Compiler13SerializationL14invokeRewriterENS1_8ModuleOpERKNSC_14ModuleRewriterERKNSt3__18optionalINSI_4__fs10filesystem4pathEEERKSM_E3$_0NS1_6coreai10ConstantOpEvEENSI_9enable_ifIXaantsr4llvm9is_one_ofIT2_S3_PNS1_6RegionEPNS1_5BlockEEE5valuesr3std7is_sameIT3_vEE5valueES11_E4typeES3_OT1_EUlS3_E_EEvlS3_
CStrings:
+ "3610.5.1"
- "3605.6.4"
```
