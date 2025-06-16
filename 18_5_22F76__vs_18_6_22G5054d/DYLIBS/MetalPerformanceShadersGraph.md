## MetalPerformanceShadersGraph

> `/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`

```diff

-5.4.11.0.0
+5.6.2.0.0
   __TEXT.__text: 0xf67f48
   __TEXT.__auth_stubs: 0x29c0
   __TEXT.__mpsgraph_init_: 0xc
   __TEXT.__objc_methlist: 0x68cc
   __TEXT.__const: 0x3d37c
-  __TEXT.__cstring: 0x88534
-  __TEXT.__gcc_except_tab: 0x59134
+  __TEXT.__cstring: 0x88533
+  __TEXT.__gcc_except_tab: 0x59130
   __TEXT.__oslogstring: 0x32
   __TEXT.__unwind_info: 0x275e0
   __TEXT.__eh_frame: 0x24d4

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libncurses.5.4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 12BA163B-BB4E-37D0-888E-156185B22723
-  Functions: 59440
-  Symbols:   173136
+  UUID: 8FCE75E7-80EA-37ED-8B13-DA4282E4EEA4
+  Functions: 59439
+  Symbols:   173134
   CStrings:  15775
 
Functions:
~ -[MPSGraphExecutable initWithMPSGraphPackageAtURLCommon:compilationDescriptor:error:] : 10372 -> 10384
~ __ZNK4mlir3mps12_GLOBAL__N_137CanonicalizeMatMulExpandSqueezeBinaryINS0_5AddOpEE15matchAndRewriteENS0_9ReshapeOpERNS_15PatternRewriterE : 788 -> 768
+ _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_12
~ _OUTLINED_FUNCTION_14 : 12 -> 20
~ _OUTLINED_FUNCTION_15 : 20 -> 32
- _OUTLINED_FUNCTION_17
~ __ZN4mlir21createRawElementsAttrENS_16RankedTensorTypeEN4llvm8ArrayRefIcEE : 328 -> 400
~ __ZNK4mlir3mps12_GLOBAL__N_112AddSubConsts15matchAndRewriteENS0_5AddOpERNS_15PatternRewriterE : 372 -> 376
~ __ZNK4mlir3mps12_GLOBAL__N_136CanonicalizeMatMulExpandSqueezeUnaryINS0_6ReluOpEE15matchAndRewriteENS0_9ReshapeOpERNS_15PatternRewriterE : 744 -> 680
~ __ZNK4mlir3mps12_GLOBAL__N_123FuseBinaryWithConstantsINS0_5AddOpELb1EE15matchAndRewriteES3_RNS_15PatternRewriterE : 400 -> 404
~ __ZNK4mlir3mps12_GLOBAL__N_123FuseBinaryWithConstantsINS0_10MultiplyOpELb1EE15matchAndRewriteES3_RNS_15PatternRewriterE : 400 -> 404
CStrings:
+ "180600"
+ "5.6.2"
- "180500"
- "5.4.11"

```
