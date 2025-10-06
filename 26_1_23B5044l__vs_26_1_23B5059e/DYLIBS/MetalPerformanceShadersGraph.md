## MetalPerformanceShadersGraph

> `/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`

```diff

-6.1.2.0.0
-  __TEXT.__text: 0xf9fd30
+6.1.5.0.0
+  __TEXT.__text: 0xfa2940
   __TEXT.__auth_stubs: 0x3070
   __TEXT.__mpsgraph_init_: 0x10
   __TEXT.__objc_methlist: 0x73ac
   __TEXT.__const: 0x3f0a9
-  __TEXT.__cstring: 0x89712
+  __TEXT.__cstring: 0x898ac
   __TEXT.__swift5_typeref: 0x2f3
   __TEXT.__swift5_capture: 0x10
   __TEXT.__constg_swiftt: 0x1d4

   __TEXT.__swift_as_ret: 0x8
   __TEXT.__gcc_except_tab: 0x55a44
   __TEXT.__oslogstring: 0x11c
-  __TEXT.__unwind_info: 0x290e8
+  __TEXT.__unwind_info: 0x29118
   __TEXT.__eh_frame: 0x2aa8
   __TEXT.__objc_classname: 0x1cad
   __TEXT.__objc_methname: 0x159f2

   __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0x1260
   __AUTH_CONST.__auth_got: 0x1848
-  __AUTH_CONST.__const: 0x66a78
+  __AUTH_CONST.__const: 0x66ad8
   __AUTH_CONST.__cfstring: 0x111a0
   __AUTH_CONST.__objc_const: 0x101c0
   __AUTH_CONST.__objc_intobj: 0x690

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 91993868-EC6A-3751-8DDC-33D44527F4A5
-  Functions: 61445
-  Symbols:   179307
-  CStrings:  16289
+  UUID: DC79E78C-ABC9-3970-B653-6261D3D10E2D
+  Functions: 61462
+  Symbols:   179344
+  CStrings:  16297
 
Symbols:
+ __ZN4llvm12function_refIFbRN4mlir9OpOperandEEE11callback_fnIZNKS1_3mps12_GLOBAL__N_120ViewOpRewritePatternINS7_8ConcatOpEE15bufferizeViewOpESA_RNS1_15PatternRewriterEEUlS3_E_EEblS3_
+ __ZN4llvm12function_refIFvRN4mlir10DiagnosticEEE11callback_fnIZNS1_12RewriterBase18notifyMatchFailureIRNS1_3mps8ConcatOpEEENS_13LogicalResultEOT_RKNS_5TwineEEUlS3_E_EEvlS3_
+ __ZN4llvm23SmallVectorTemplateBaseIN4mlir6memref7AllocOpELb1EE9push_backES3_
+ __ZN4mlir12RewriterBase18notifyMatchFailureIRNS_3mps8ConcatOpEEEN4llvm13LogicalResultEOT_PKc
+ __ZN4mlir3mps12_GLOBAL__N_126MPSToMemrefConcatConverterD0Ev
+ __ZN4mlir3mps12_GLOBAL__N_126MPSToMemrefConcatConverterD1Ev
+ __ZN4mlir9OpBuilder6createINS_4mpsx11UseMemrefOpEJRNS_5ValueEEEET_NS_8LocationEDpOT0_
+ __ZN4mlir9OpBuilder6createINS_4mpsx11UseMemrefOpEJRNS_5ValueEEEET_NS_8LocationEDpOT0_.cold.1
+ __ZNK4mlir3mps12_GLOBAL__N_120ViewOpRewritePatternINS0_11TransposeOpEE15bufferizeViewOpES3_RNS_15PatternRewriterE
+ __ZNK4mlir3mps12_GLOBAL__N_120ViewOpRewritePatternINS0_14StridedSliceOpEE15bufferizeViewOpES3_RNS_15PatternRewriterE
+ __ZNK4mlir3mps12_GLOBAL__N_120ViewOpRewritePatternINS0_17ReinterpretCastOpEE15bufferizeViewOpES3_RNS_15PatternRewriterE
+ __ZNK4mlir3mps12_GLOBAL__N_120ViewOpRewritePatternINS0_20StridedSliceUpdateOpEE15bufferizeViewOpES3_RNS_15PatternRewriterE
+ __ZNK4mlir3mps12_GLOBAL__N_120ViewOpRewritePatternINS0_7SliceOpEE15bufferizeViewOpES3_RNS_15PatternRewriterE
+ __ZNK4mlir3mps12_GLOBAL__N_120ViewOpRewritePatternINS0_8ConcatOpEE15bufferizeViewOpES3_RNS_15PatternRewriterE
+ __ZNK4mlir3mps12_GLOBAL__N_120ViewOpRewritePatternINS0_8ConcatOpEE15matchAndRewriteES3_RNS_15PatternRewriterE
+ __ZNK4mlir3mps12_GLOBAL__N_120ViewOpRewritePatternINS0_9PermuteOpEE15bufferizeViewOpES3_RNS_15PatternRewriterE
+ __ZNK4mlir3mps12_GLOBAL__N_126MPSToMemrefConcatConverter31matchAndRewriteWithStaticShapesENS_5ValueENS0_8ConcatOpERNS_15PatternRewriterE
+ __ZNSt3__113__stable_sortINS_17_ClassicAlgPolicyERZNK4mlir3mps12_GLOBAL__N_126MPSToMemrefConcatConverter31matchAndRewriteWithStaticShapesENS2_5ValueENS3_8ConcatOpERNS2_15PatternRewriterEEUlNS2_6memref7AllocOpESB_E_PSB_EEvT1_SF_T0_NS_15iterator_traitsISF_E15difference_typeEPNSI_10value_typeEl
+ __ZNSt3__115__inplace_mergeINS_17_ClassicAlgPolicyERZNK4mlir3mps12_GLOBAL__N_126MPSToMemrefConcatConverter31matchAndRewriteWithStaticShapesENS2_5ValueENS3_8ConcatOpERNS2_15PatternRewriterEEUlNS2_6memref7AllocOpESB_E_PSB_EEvT1_SF_SF_OT0_NS_15iterator_traitsISF_E15difference_typeESK_PNSJ_10value_typeEl
+ __ZNSt3__118__stable_sort_moveINS_17_ClassicAlgPolicyERZNK4mlir3mps12_GLOBAL__N_126MPSToMemrefConcatConverter31matchAndRewriteWithStaticShapesENS2_5ValueENS3_8ConcatOpERNS2_15PatternRewriterEEUlNS2_6memref7AllocOpESB_E_PSB_EEvT1_SF_T0_NS_15iterator_traitsISF_E15difference_typeEPNSI_10value_typeE
+ __ZTVN4mlir3mps12_GLOBAL__N_126MPSToMemrefConcatConverterE
- __ZN4mlir9OpBuilder6createINS_4mpsx11UseMemrefOpEJNS_5ValueEEEET_NS_8LocationEDpOT0_
- __ZN4mlir9OpBuilder6createINS_4mpsx11UseMemrefOpEJNS_5ValueEEEET_NS_8LocationEDpOT0_.cold.1
CStrings:
+ "6.1.5"
+ "Aliased inputs are not supported for bufferizing concat"
+ "Failed to find the source memref for concat operand"
+ "Failed to get `axis` vector from concat op"
+ "Only alloc ops are supported as the source of concat operand"
+ "StringRef llvm::getTypeName() [DesiredTypeName = mlir::mps::(anonymous namespace)::MPSToMemrefConcatConverter]"
+ "Unsupported concat op"
+ "concat_slice"
+ "could not bufferize concat with duplicate values"
+ "invalid shape in concat values"
- "6.1.2"
- "input must be a shaped type"

```
