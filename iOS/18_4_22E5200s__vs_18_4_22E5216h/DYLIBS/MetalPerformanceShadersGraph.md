## MetalPerformanceShadersGraph

> `/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`

```diff

-5.4.6.0.0
-  __TEXT.__text: 0xf63f4c
+5.4.7.0.0
+  __TEXT.__text: 0xf67ba0
   __TEXT.__auth_stubs: 0x29c0
   __TEXT.__mpsgraph_init_: 0xc
-  __TEXT.__objc_methlist: 0x68a4
-  __TEXT.__const: 0x3d298
-  __TEXT.__cstring: 0x8822c
-  __TEXT.__gcc_except_tab: 0x588b8
+  __TEXT.__objc_methlist: 0x68bc
+  __TEXT.__const: 0x3d2d8
+  __TEXT.__cstring: 0x88562
+  __TEXT.__gcc_except_tab: 0x58e80
   __TEXT.__oslogstring: 0x32
-  __TEXT.__unwind_info: 0x27588
+  __TEXT.__unwind_info: 0x275e0
   __TEXT.__eh_frame: 0x24d4
   __TEXT.__objc_classname: 0x1c21
-  __TEXT.__objc_methname: 0x135cb
+  __TEXT.__objc_methname: 0x136eb
   __TEXT.__objc_methtype: 0x51a9
-  __TEXT.__objc_stubs: 0x9540
-  __DATA_CONST.__got: 0x7a0
-  __DATA_CONST.__const: 0x3368
+  __TEXT.__objc_stubs: 0x9580
+  __DATA_CONST.__got: 0x7a8
+  __DATA_CONST.__const: 0x3378
   __DATA_CONST.__objc_classlist: 0x738
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3430
+  __DATA_CONST.__objc_selrefs: 0x3448
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x1078
   __AUTH_CONST.__auth_got: 0x14f0
   __AUTH_CONST.__auth_ptr: 0x60
-  __AUTH_CONST.__const: 0x63038
-  __AUTH_CONST.__cfstring: 0xf8c0
-  __AUTH_CONST.__objc_const: 0xf2f8
+  __AUTH_CONST.__const: 0x630c0
+  __AUTH_CONST.__cfstring: 0xf960
+  __AUTH_CONST.__objc_const: 0xf388
   __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_arrayobj: 0x1ff8
   __AUTH_CONST.__objc_dictobj: 0x208
   __AUTH.__objc_data: 0x47e0
-  __AUTH.__data: 0x4108
+  __AUTH.__data: 0x4110
   __AUTH.__thread_vars: 0x120
   __AUTH.__thread_bss: 0x238
   __DATA.__objc_ivar: 0x1b4
   __DATA.__data: 0x5cc0
   __DATA.__bss: 0x390
   __DATA.__common: 0x1967
-  __DATA_DIRTY.__objc_ivar: 0x888
+  __DATA_DIRTY.__objc_ivar: 0x898
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0xa8
   __DATA_DIRTY.__bss: 0x1590

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libncurses.5.4.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 59492
-  Symbols:   76919
-  CStrings:  13763
+  Functions: 59446
+  Symbols:   76868
+  CStrings:  13796
 
Symbols:
+ _OBJC_CLASS_$_MPSNDArrayQuantizedConvolution
CStrings:
+ "\"\x11R"
+ "%@%@%@"
+ "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShadersGraph/mpsgraph/MetalPerformanceShadersGraph/Runtimes/MPSRuntime/Headers/Operations/GPUConvolutionOps.h"
+ "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShadersGraph/mpsgraph/MetalPerformanceShadersGraph/Runtimes/MPSRuntime/Headers/Operations/GPUFusionOps.h"
+ "/Library/Caches/com.apple.xbs/Sources/MetalPerformanceShadersGraph/mpsgraph/MetalPerformanceShadersGraph/Runtimes/MPSRuntime/Operations/GPUFusionOps.mm"
+ "5.4.7"
+ "Expected only one block in fusionOp.\n"
+ "Expected to only find one unique core op."
+ "GPUConvolutionOps.h"
+ "If enabled, dequantize and conv2D ops will be canonicalized as a single-dispatch Fusion op."
+ "MPSGRAPH_DISABLE_QUANTIZED_CONV_FUSION"
+ "MPSGRAPH_DISABLE_QUANTIZED_CONV_FUSION EV is set."
+ "MPSGRAPH_ENABLE_QUANTIZED_CONV_FUSION"
+ "MPSGRAPH_ENABLE_QUANTIZED_CONV_FUSION EV is set."
+ "MPSGRAPH_LOG_PASS_TIMINGS"
+ "MPSGRAPH_LOG_PASS_TIMINGS EV is set."
+ "No stitching expected in this fusionOp.\n"
+ "QuantizedConv2D"
+ "StringRef llvm::getTypeName() [DesiredTypeName = mlir::mps::(anonymous namespace)::CanonicalizeQuantizedConvPatternToFusionOp]"
+ "TQ,V_reducedPrecisionFastMath"
+ "Unexpected codepath for fusion op"
+ "_disableQuantizedConvFusion"
+ "_enableQuantizedConvFusion"
+ "_forceTimingPasses"
+ "_reducedPrecisionFastMath"
+ "casted_input"
+ "casted_min"
+ "casted_scale"
+ "casted_zeroPoint"
+ "centered"
+ "enable-quantized-conv-fusion"
+ "initWithDevice:ndArrayConvolution2DDescriptor:dataQuantizationDescriptor:weightsQuantizationDescriptor:"
+ "min_add"
+ "mps.reducedPrecisionFastMath"
+ "reducedPrecisionFastMath"
+ "scaled"
+ "setReducedPrecisionFastMath:"
- "\"\x11B"
- "Expected to only find one core op."
- "StringRef llvm::getTypeName() [DesiredTypeName = mlir::mps::(anonymous namespace)::CanonicalizeQuantizedLayerScale<mlir::mps::Conv2DOp>]"
- "StringRef llvm::getTypeName() [DesiredTypeName = mlir::mps::(anonymous namespace)::CanonicalizeQuantizedLayerScale<mlir::mps::DepthwiseConv3DDataGradientOp>]"
- "StringRef llvm::getTypeName() [DesiredTypeName = mlir::mps::(anonymous namespace)::CanonicalizeQuantizedLayerScale<mlir::mps::DepthwiseConv3DOp>]"

```
