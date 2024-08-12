## ANECompiler

> `/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler`

```diff

-8.2.12.0.0
-  __TEXT.__text: 0x11bb6a4
+8.2.17.0.0
+  __TEXT.__text: 0x11c3c38
   __TEXT.__auth_stubs: 0x20d0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x74854
-  __TEXT.__cstring: 0x8bff9
-  __TEXT.__gcc_except_tab: 0x6ba58
-  __TEXT.__oslogstring: 0x15db0
-  __TEXT.__unwind_info: 0x381f8
+  __TEXT.__const: 0x750ec
+  __TEXT.__cstring: 0x8c5e7
+  __TEXT.__gcc_except_tab: 0x6c424
+  __TEXT.__oslogstring: 0x15e07
+  __TEXT.__unwind_info: 0x38370
   __TEXT.__eh_frame: 0x11b4
   __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__const: 0x3600
+  __DATA_CONST.__const: 0x3610
   __AUTH_CONST.__auth_got: 0x1070
   __AUTH_CONST.__auth_ptr: 0x80
-  __AUTH_CONST.__const: 0x70f20
-  __AUTH_CONST.__cfstring: 0x7ec0
+  __AUTH_CONST.__const: 0x71350
+  __AUTH_CONST.__cfstring: 0x7f00
   __AUTH.__data: 0x3618
   __AUTH.__thread_vars: 0xf0
   __AUTH.__thread_bss: 0x16c
-  __DATA.__data: 0x6538
+  __DATA.__data: 0x6540
   __DATA.__bss: 0x9ca0
   __DATA.__common: 0x1558
   __DATA_DIRTY.__data: 0x80

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libncurses.5.4.dylib
-  Functions: 71198
-  Symbols:   83336
-  CStrings:  15429
+  Functions: 71287
+  Symbols:   83458
+  CStrings:  15467
 
CStrings:
+ " as "
+ "\" must have innermost axis ("
+ ") to be a valid interleave factor."
+ "ANEBinaryPoint"
+ "ANECompiler internal error: Failed to create transpose for interleaved live-in"
+ "ANECompiler internal error: Failed to create transpose for interleaved live-out"
+ "ANECompiler internal error: operation %!s(MISSING) cannot be retrieved"
+ "BlobFileMutabilityInfo"
+ "C2S decomposition must be successful"
+ "C2S is required in a ZinChannelToSpaceLargeFactorCompositeLayer"
+ "CHANNEL_TO_SPACE_LARGE_FACTOR_COMPOSITE"
+ "Concat tensor must be interleaved. Otherwise reshape is noop."
+ "Conv is required in a ZinChannelToSpaceLargeFactorCompositeLayer"
+ "Conv output channel must be divisible by split"
+ "Disable HW Layernorm Lowering to TernaryGOC: %!d(MISSING)\n"
+ "DisableLayernormOpt"
+ "Error: Input \"%!s(MISSING)\" must have innermost axis (%!l(MISSING)d) to be a valid interleave factor."
+ "Error: Output \""
+ "Factor of 4x4x1 is the only supported large factor"
+ "Failed in making ZinChannelToSpaceLargeFactorCompositeLayer."
+ "Failed to revalidate indices producer"
+ "Failed to translate MIL binary point."
+ "Losing precision on ANE, cannot be consumed by "
+ "Must not clone ZinChannelToSpaceLargeFactorCompositeLayer."
+ "NeuralEngineOptimizedIOBuffer"
+ "Number of split layers must be equal"
+ "Output dimensions must match"
+ "Setting interleave must succeed"
+ "Split cout offset vector size must be same as split"
+ "Split name vector size must be same as split"
+ "Split transforms vector size must be same as split"
+ "We only support 4x4x1"
+ "ZinChannelToSpaceLargeFactorCompositeLayer has at least 1 layer."
+ "ZinChannelToSpaceLargeFactorCompositeLayer input must be unique"
+ "_interleaved"
+ "_post_shuffle"
+ "disable-layernorm-opt"
+ "supportOptimizedIOBuffer"

```
