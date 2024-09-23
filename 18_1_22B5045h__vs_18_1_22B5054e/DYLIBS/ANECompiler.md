## ANECompiler

> `/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler`

```diff

-8.3.5.0.0
-  __TEXT.__text: 0x11fdf8c
-  __TEXT.__auth_stubs: 0x20d0
+8.3.7.0.0
+  __TEXT.__text: 0x1200e54
+  __TEXT.__auth_stubs: 0x20f0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x778bc
-  __TEXT.__cstring: 0x90ca6
-  __TEXT.__gcc_except_tab: 0x6da28
-  __TEXT.__oslogstring: 0x15f27
-  __TEXT.__unwind_info: 0x38c48
+  __TEXT.__const: 0x778ec
+  __TEXT.__cstring: 0x90fb9
+  __TEXT.__gcc_except_tab: 0x6dcc4
+  __TEXT.__oslogstring: 0x15ffe
+  __TEXT.__unwind_info: 0x38c80
   __TEXT.__eh_frame: 0x11b4
   __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__const: 0x3620
-  __AUTH_CONST.__auth_got: 0x1070
+  __DATA_CONST.__const: 0x3630
+  __AUTH_CONST.__auth_got: 0x1080
   __AUTH_CONST.__auth_ptr: 0x80
   __AUTH_CONST.__const: 0x71f68
-  __AUTH_CONST.__cfstring: 0x7f20
+  __AUTH_CONST.__cfstring: 0x7f60
   __AUTH.__data: 0x3618
   __AUTH.__thread_vars: 0xf0
   __AUTH.__thread_bss: 0x16c
-  __DATA.__data: 0x6840
-  __DATA.__bss: 0xad50
+  __DATA.__data: 0x6850
+  __DATA.__bss: 0xad98
   __DATA.__common: 0x1558
   __DATA_DIRTY.__data: 0x80
   __DATA_DIRTY.__common: 0x38

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libncurses.5.4.dylib
-  Functions: 72494
-  Symbols:   84872
-  CStrings:  15651
+  Functions: 72514
+  Symbols:   84893
+  CStrings:  15674
 
Symbols:
+ __ZNSt3__14__fs10filesystem8__statusERKNS1_4pathEPNS_10error_codeE
+ __ZNSt3__14__fs10filesystem11__file_sizeERKNS1_4pathEPNS_10error_codeE
CStrings:
+ "fdisable-weight-file-size-check"
+ "Error in TryBatchDepthHeightSplitWithLegalFactor - illegal axis is given."
+ "SplitNEConvLayer: set interleave error."
+ "DisableInputAndConstantCaching"
+ "Disable input and Constant caching: %!d(MISSING)\n"
+ "Internal Error: softmax lowering"
+ "SplitNEConvLayer: MirInfo setup failure."
+ "Cannot find tensor info for %!s(MISSING)"
+ " bytes) exceeds the maximum ("
+ "Error: Cannot retrieve tensor format during decompose reflecting pad lowering."
+ "Error: GOC layer should contain a kernel"
+ "SuppressMathException"
+ "ZinPixelUnshuffleLayer: redundant view removal failure."
+ " bytes)"
+ "Internal error: softmax lowering"
+ "Disable weight file size check: %!d(MISSING)\n"
+ "Weight file size ("
+ ".CpAllocation.debug"
+ "Latency Splitting %!s(MISSING)(%!f(MISSING)) into %!z(MISSING)u parts. (%!s(MISSING) restriction)"
+ "_kernel_split"
+ "SplitNEConvLayer: conv should have only one input view."
+ "Enable supress math exception: %!d(MISSING)\n"
+ "DisableWeightFileSizeCheck"
+ "SplitNEConvLayer: NEConv with kernel coefficients should be handled by the kernel splitter."
+ "suppress-math-exception"
+ "Should not split a logical conv layer by input channel"
+ "SplitNEConvLayer: unable to split non-logical conv because of output cw transpose alignment."
+ "SplitNEConvLayer: unable to split goc."
+ "Error: fail to find the incoming layer for NEPool"
- ".CpSchedule.debug"
- "should never reach here"
- "InputAndConstantCaching"
- "Latency Splitting %!s(MISSING)(%!f(MISSING)) into %!z(MISSING)u parts. (height restriction)"
- "Should not split a conv layer by input channel"
- "Input and Constant caching: %!d(MISSING)\n"

```
