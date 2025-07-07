## MetalPerformanceShadersGraph

> `/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`

```diff

-6.0.13.0.0
-  __TEXT.__text: 0xf80fa0
-  __TEXT.__auth_stubs: 0x3030
+6.0.15.0.0
+  __TEXT.__text: 0xf838b8
+  __TEXT.__auth_stubs: 0x3040
   __TEXT.__mpsgraph_init_: 0x10
-  __TEXT.__objc_methlist: 0x7384
-  __TEXT.__const: 0x3ef39
-  __TEXT.__cstring: 0x884da
+  __TEXT.__objc_methlist: 0x739c
+  __TEXT.__const: 0x3ef59
+  __TEXT.__cstring: 0x885f7
   __TEXT.__swift5_typeref: 0x2c7
   __TEXT.__swift5_capture: 0x10
   __TEXT.__constg_swiftt: 0x1d4

   __TEXT.__swift5_types: 0x34
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__gcc_except_tab: 0x55084
-  __TEXT.__oslogstring: 0x32
-  __TEXT.__unwind_info: 0x28c18
+  __TEXT.__gcc_except_tab: 0x5522c
+  __TEXT.__oslogstring: 0x64
+  __TEXT.__unwind_info: 0x28c90
   __TEXT.__eh_frame: 0x2aa8
   __TEXT.__objc_classname: 0x1cad
-  __TEXT.__objc_methname: 0x1589c
+  __TEXT.__objc_methname: 0x158b2
   __TEXT.__objc_methtype: 0x4bd4
-  __TEXT.__objc_stubs: 0x9d20
+  __TEXT.__objc_stubs: 0x9d40
   __DATA_CONST.__got: 0x898
   __DATA_CONST.__const: 0x3478
   __DATA_CONST.__objc_classlist: 0x758
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ab0
+  __DATA_CONST.__objc_selrefs: 0x3ac0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0x1220
-  __AUTH_CONST.__auth_got: 0x1828
-  __AUTH_CONST.__const: 0x66168
-  __AUTH_CONST.__cfstring: 0x10c80
-  __AUTH_CONST.__objc_const: 0x101c0
-  __AUTH_CONST.__objc_intobj: 0x540
+  __AUTH_CONST.__auth_got: 0x1830
+  __AUTH_CONST.__const: 0x66260
+  __AUTH_CONST.__cfstring: 0x10d20
+  __AUTH_CONST.__objc_const: 0x101a0
+  __AUTH_CONST.__objc_intobj: 0x6a8
   __AUTH_CONST.__objc_arrayobj: 0x2028
   __AUTH_CONST.__objc_dictobj: 0x2f8
   __AUTH.__objc_data: 0x4920

   __DATA.__data: 0x5f08
   __DATA.__bss: 0x1720
   __DATA.__common: 0x1a87
-  __DATA_DIRTY.__objc_ivar: 0x8d4
+  __DATA_DIRTY.__objc_ivar: 0x8d0
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0xa8
   __DATA_DIRTY.__bss: 0x15b0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C4D7E7BD-4C8A-3EEF-8855-F79F057DDA44
-  Functions: 61114
-  Symbols:   178389
-  CStrings:  16148
+  UUID: E882A773-AF6B-383C-99AF-0EEFD5BAB881
+  Functions: 61144
+  Symbols:   178472
+  CStrings:  16162
 
Symbols:
+ -[MPSGraphDelegatePrecompilationDescriptor initWithArchitecture:]
+ -[MPSGraphDelegatePrecompilationDescriptor initWithArchitecture:aneOptionsURL:]
+ GCC_except_table406
+ GCC_except_table409
+ GCC_except_table525
+ GCC_except_table529
+ GCC_except_table548
+ GCC_except_table552
+ GCC_except_table570
+ GCC_except_table579
+ GCC_except_table592
+ GCC_except_table598
+ __ZN12_GLOBAL__N_119GeneratedRewriter78D0Ev
+ __ZN12_GLOBAL__N_119GeneratedRewriter78D1Ev
+ __ZN4llvm12function_refIFvPN4mlir9OperationEEE11callback_fnIZNS1_6detail4walkILNS1_9WalkOrderE1ENS1_15ForwardIteratorEZN12_GLOBAL__N_123SegmentAllOpsToDelegate14runOnOperationEvE3$_2NS1_4ODIE8Compiler6CoreML15IsolatedGroupOpEvEENSt3__19enable_ifIXaantsr4llvm9is_one_ofIT2_S3_PNS1_6RegionEPNS1_5BlockEEE5valuesr3std7is_sameIT3_vEE5valueESP_E4typeES3_OT1_EUlS3_E_EEvlS3_
+ __ZN4llvm12function_refIFvPN4mlir9OperationEEE11callback_fnIZNS1_6detail4walkILNS1_9WalkOrderE1ENS1_15ForwardIteratorEZNS1_28moduleHasIndependentAdaptersENS1_8ModuleOpEE3$_0NS1_4ODIE8Compiler6CoreML7GraphOpEvEENSt3__19enable_ifIXaantsr4llvm9is_one_ofIT2_S3_PNS1_6RegionEPNS1_5BlockEEE5valuesr3std7is_sameIT3_vEE5valueESO_E4typeES3_OT1_EUlS3_E_EEvlS3_
+ __ZN4llvm14raw_fd_ostreamC1ENS_9StringRefERNSt3__110error_codeE
+ __ZN4mlir14RewritePattern6createINS_4anec16ConvertPow2ToMulEJRPNS_11MLIRContextEEEENSt3__110unique_ptrIT_NS7_14default_deleteIS9_EEEEDpOT0_
+ __ZN4mlir28moduleHasIndependentAdaptersENS_8ModuleOpE
+ __ZN4mlir3mps12_GLOBAL__N_149CanonicalizeHigherRankTensorToMPSKernelSizeTensorD0Ev
+ __ZN4mlir3mps12_GLOBAL__N_149CanonicalizeHigherRankTensorToMPSKernelSizeTensorD1Ev
+ __ZN4mlir3mps15RandomUniformOp5buildERNS_9OpBuilderERNS_14OperationStateENS_9TypeRangeENS_10ValueRangeEN4llvm8ArrayRefINS_14NamedAttributeEEE
+ __ZN4mlir3mps15RandomUniformOp5buildERNS_9OpBuilderERNS_14OperationStateENS_9TypeRangeENS_10ValueRangeEN4llvm8ArrayRefINS_14NamedAttributeEEE.cold.1
+ __ZN4mlir4anec12_GLOBAL__N_15utils25isSplatConstAndGetFPValueENS_3mps10ConstantOpE
+ __ZN4mlir4anec16ConvertPow2ToMulD0Ev
+ __ZN4mlir4anec16ConvertPow2ToMulD1Ev
+ __ZN4mlir6detail18constant_op_binderINS_3mps19MPSBufferTensorAttrEE5matchEPNS_9OperationE
+ __ZN4mlir6detail18constant_op_binderINS_3mps19MPSBufferTensorAttrEE5matchEPNS_9OperationE.cold.1
+ __ZN4mlir9OpBuilder6createINS_3mps14StridedSliceOpEJRNS2_9PermuteOpENS2_10ConstantOpES6_S6_jjjbEEET_NS_8LocationEDpOT0_
+ __ZN4mlir9OpBuilder6createINS_3mps14StridedSliceOpEJRNS2_9PermuteOpENS2_10ConstantOpES6_S6_jjjbEEET_NS_8LocationEDpOT0_.cold.1
+ __ZN4mlir9OpBuilder6createINS_3mps15RandomUniformOpEJRNS_16RankedTensorTypeENS_12OperandRangeEN4llvm8ArrayRefINS_14NamedAttributeEEEEEET_NS_8LocationEDpOT0_
+ __ZN4mlir9OpBuilder6createINS_3mps15RandomUniformOpEJRNS_16RankedTensorTypeENS_12OperandRangeEN4llvm8ArrayRefINS_14NamedAttributeEEEEEET_NS_8LocationEDpOT0_.cold.1
+ __ZN4mlir9OpBuilder6createINS_3mps9NonZeroOpEJRNS_5ValueEEEET_NS_8LocationEDpOT0_
+ __ZN4mlir9OpBuilder6createINS_3mps9ReshapeOpEJRNS2_15RandomUniformOpERNS2_10ConstantOpEEEET_NS_8LocationEDpOT0_
+ __ZN4mlir9OpBuilder6createINS_3mps9ReshapeOpEJRNS2_15RandomUniformOpERNS2_10ConstantOpEEEET_NS_8LocationEDpOT0_.cold.1
+ __ZN4mlir9OpBuilder6createINS_4anec17ScaledElementWiseEJNS_10MemRefTypeERNS_5ValueES6_NS_10StringAttrENS_9FloatAttrES8_S8_NS_8BoolAttrES9_EEET_NS_8LocationEDpOT0_
+ __ZN4mlir9OpBuilder6createINS_4anec17ScaledElementWiseEJNS_10MemRefTypeERNS_5ValueES6_NS_10StringAttrENS_9FloatAttrES8_S8_NS_8BoolAttrES9_EEET_NS_8LocationEDpOT0_.cold.1
+ __ZNK12_GLOBAL__N_119GeneratedRewriter7815matchAndRewriteERKN3MIL11IROperationER17MILToMLIRRewriter
+ __ZNK4mlir3mps12_GLOBAL__N_149CanonicalizeHigherRankTensorToMPSKernelSizeTensor19matchAndRewriteImplENS0_15RandomUniformOpERNS_15PatternRewriterE
+ __ZNK4mlir3mps27BaseCanonicalizationPatternINS0_15RandomUniformOpEE15matchAndRewriteES2_RNS_15PatternRewriterE
+ __ZNK4mlir4anec16ConvertPow2ToMul15matchAndRewriteENS0_16ElementwisePowerERNS_15PatternRewriterE
+ __ZNK4mlir6detail31OpOrInterfaceRewritePatternBaseINS_4anec16ElementwisePowerEE15matchAndRewriteEPNS_9OperationERNS_15PatternRewriterE
+ __ZNK4mlir6detail31OpOrInterfaceRewritePatternBaseINS_4anec16ElementwisePowerEE5matchEPNS_9OperationE
+ __ZNK4mlir6detail31OpOrInterfaceRewritePatternBaseINS_4anec16ElementwisePowerEE5matchES3_
+ __ZNK4mlir6detail31OpOrInterfaceRewritePatternBaseINS_4anec16ElementwisePowerEE7rewriteEPNS_9OperationERNS_15PatternRewriterE
+ __ZNK4mlir6detail31OpOrInterfaceRewritePatternBaseINS_4anec16ElementwisePowerEE7rewriteES3_RNS_15PatternRewriterE
+ __ZTIN12_GLOBAL__N_119GeneratedRewriter78E
+ __ZTSN12_GLOBAL__N_119GeneratedRewriter78E
+ __ZTVN12_GLOBAL__N_119GeneratedRewriter78E
+ __ZTVN4mlir3mps12_GLOBAL__N_149CanonicalizeHigherRankTensorToMPSKernelSizeTensorE
+ __ZTVN4mlir4anec16ConvertPow2ToMulE
+ __ZZN4mlir3mps12_GLOBAL__N_123PermuteOpReorderDetails22moveThroughOperandImplINS0_14StridedSliceOpEEEN4llvm11SmallVectorINS_5ValueELj4EEEPPNS_9OperationERNS_10IRRewriterENS_8LocationESA_SA_ENKUlT_E_clIS7_EEDaSF_
+ __ZZN4mlir3mps12_GLOBAL__N_123PermuteOpReorderDetails22moveThroughOperandImplINS0_14StridedSliceOpEEEN4llvm11SmallVectorINS_5ValueELj4EEEPPNS_9OperationERNS_10IRRewriterENS_8LocationESA_SA_ENKUljE_clEj
+ ___Block_byref_object_copy_.585
+ ___Block_byref_object_copy_.703
+ ___Block_byref_object_copy_.708
+ ___Block_byref_object_dispose_.586
+ ___Block_byref_object_dispose_.704
+ ___Block_byref_object_dispose_.709
+ ___block_literal_global.1213
+ ___block_literal_global.1216
+ ___block_literal_global.1219
+ ___block_literal_global.858
+ ___block_literal_global.862
+ __os_log_impl
+ _objc_msgSend$initWithArchitecture:aneOptionsURL:
- GCC_except_table393
- GCC_except_table399
- GCC_except_table402
- GCC_except_table405
- GCC_except_table521
- GCC_except_table528
- GCC_except_table550
- GCC_except_table553
- GCC_except_table558
- GCC_except_table568
- GCC_except_table571
- GCC_except_table580
- GCC_except_table589
- GCC_except_table593
- __ZN4llvm23SmallVectorTemplateBaseIfLb1EE9push_backEf
- __ZN4mlir9getValuesIfEEvNS_19DenseFPElementsAttrERN4llvm15SmallVectorImplIT_EE
- ___Block_byref_object_copy_.587
- ___Block_byref_object_copy_.706
- ___Block_byref_object_copy_.711
- ___Block_byref_object_dispose_.588
- ___Block_byref_object_dispose_.707
- ___Block_byref_object_dispose_.712
- ___block_literal_global.1217
- ___block_literal_global.1220
- ___block_literal_global.1223
- ___block_literal_global.861
- ___block_literal_global.865
CStrings:
+ "%@%i%s"
+ "6.0.15"
+ "Dimension 1 stride (bytes per row) must be aligned to 64 bytes"
+ "StringRef llvm::getTypeName() [DesiredTypeName = mlir::anec::ConvertPow2ToMul]"
+ "StringRef llvm::getTypeName() [DesiredTypeName = mlir::mps::(anonymous namespace)::CanonicalizeHigherRankTensorToMPSKernelSizeTensor]"
+ "Tensor offset is not zero"
+ "Warning: GPU core count option is deprecated, passed value ignored"
+ "c"
+ "g"
+ "initWithArchitecture:"
+ "initWithArchitecture:aneOptionsURL:"
- "6.0.13"
- "MPSGRAPH_TREAT_AS_INDEPENDENT_ADAPTER_SET"
- "MPSGRAPH_TREAT_AS_INDEPENDENT_ADAPTER_SET EV is set."
- "_enableTreatAsIndependentAdapterSet"

```
