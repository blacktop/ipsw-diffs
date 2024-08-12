## ANECompiler

> `/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler`

```diff

-8.2.8.0.0
-  __TEXT.__text: 0x11b4e18
+8.2.16.0.0
+  __TEXT.__text: 0x11c39e8
   __TEXT.__auth_stubs: 0x20d0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x74434
-  __TEXT.__cstring: 0x8b90c
-  __TEXT.__gcc_except_tab: 0x6b470
-  __TEXT.__oslogstring: 0x15c1d
-  __TEXT.__unwind_info: 0x38008
+  __TEXT.__const: 0x750ec
+  __TEXT.__cstring: 0x8c5e7
+  __TEXT.__gcc_except_tab: 0x6c414
+  __TEXT.__oslogstring: 0x15e07
+  __TEXT.__unwind_info: 0x38360
   __TEXT.__eh_frame: 0x11b4
   __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__const: 0x35e8
+  __DATA_CONST.__const: 0x3610
   __AUTH_CONST.__auth_got: 0x1070
   __AUTH_CONST.__auth_ptr: 0x80
-  __AUTH_CONST.__const: 0x70ca0
-  __AUTH_CONST.__cfstring: 0x7e60
+  __AUTH_CONST.__const: 0x71350
+  __AUTH_CONST.__cfstring: 0x7f00
   __AUTH.__data: 0x3618
   __AUTH.__thread_vars: 0xf0
   __AUTH.__thread_bss: 0x16c
-  __DATA.__data: 0x6520
-  __DATA.__bss: 0x9cb8
-  __DATA.__common: 0x1560
+  __DATA.__data: 0x6540
+  __DATA.__bss: 0x9ca0
+  __DATA.__common: 0x1558
   __DATA_DIRTY.__data: 0x80
+  __DATA_DIRTY.__common: 0x38
   __DATA_DIRTY.__bss: 0xfa0
-  __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libncurses.5.4.dylib
-  Functions: 71080
-  Symbols:   83207
-  CStrings:  15380
+  Functions: 71285
+  Symbols:   83456
+  CStrings:  15467
 
CStrings:
+ " are not within supported range, "
+ " as "
+ "\" must have innermost axis ("
+ "%!s(MISSING): Invalid thread cmd flavor"
+ ") to be a valid interleave factor."
+ "1 <= tile_height"
+ "A locked tile has tile_height %!z(MISSING)d which violates HW constraints. It should have been updated by earlier optimization passes or JIT transfrom handling for %!s(MISSING)"
+ "ANE operation is too large"
+ "ANEBinaryPoint"
+ "ANECompiler internal error: Failed to create transpose for interleaved live-in"
+ "ANECompiler internal error: Failed to create transpose for interleaved live-out"
+ "ANECompiler internal error: operation %!s(MISSING) cannot be retrieved"
+ "Allocation error: compute_thread_command"
+ "BlobFileMutabilityInfo"
+ "C2S decomposition must be successful"
+ "C2S is required in a ZinChannelToSpaceLargeFactorCompositeLayer"
+ "CHANNEL_TO_SPACE_LARGE_FACTOR_COMPOSITE"
+ "C["
+ "Cache prefetch size is too high"
+ "Chained consumer is not an ANE layer"
+ "Concat tensor must be interleaved. Otherwise reshape is noop."
+ "Conv is required in a ZinChannelToSpaceLargeFactorCompositeLayer"
+ "Conv output channel must be divisible by split"
+ "D["
+ "Disable HW Layernorm Lowering to TernaryGOC: %!d(MISSING)\n"
+ "DisableLayernormOpt"
+ "Dram Fragmentation Factor: %!d(MISSING)\n"
+ "DramFragmentationFactor"
+ "Enable low effort CP allocation: %!d(MISSING)\n"
+ "EnableLowEffortCPAllocation"
+ "Error: Failed to serialize runtime section"
+ "Error: Input \"%!s(MISSING)\" must have innermost axis (%!l(MISSING)d) to be a valid interleave factor."
+ "Error: Output \""
+ "Error: Overran runtime section in %!s(MISSING)\n"
+ "Error: Runtime section data has already been allocated\n"
+ "Error: ZinIrSection::RUNTIME section not found"
+ "Error: graph manipulation failed when removing identity div-mul"
+ "Error: invalid dimension size for broadcast. Input size = %!z(MISSING)d, output size = %!z(MISSING)d"
+ "Error: thread argument buffer overrun."
+ "Error: thread argument is not supported."
+ "Factor of 4x4x1 is the only supported large factor"
+ "Failed in making ZinChannelToSpaceLargeFactorCompositeLayer."
+ "Failed to compute MIR info"
+ "Failed to compute tile height params of the chained producer"
+ "Failed to revalidate indices producer"
+ "Failed to split layer %!s(MISSING)"
+ "Failed to translate MIL binary point."
+ "H * W must be divisible by 8."
+ "H["
+ "Losing precision on ANE, cannot be consumed by "
+ "Mcache high priority intermediate relocation size is too high"
+ "Mcache low priority intermediate relocation size is too high"
+ "Mcache size is too high"
+ "Missing basic block in the schedule_map."
+ "Must not clone ZinChannelToSpaceLargeFactorCompositeLayer."
+ "N["
+ "NeuralEngineOptimizedIOBuffer"
+ "Number of split layers must be equal"
+ "OptimizeKernelCoalescingWithKernelStreaming"
+ "Output dimensions must match"
+ "Overlap should be zero on all layers but chained producer"
+ "Procedure header overran buffer"
+ "Procedure is too big"
+ "RCAS tile height %!z(MISSING)d is invalid. It should have been updated by earlier optimization passes or JIT transfrom handling for %!s(MISSING)"
+ "SetAllocationHint failed for tensors shared b/w ANEs."
+ "Setting interleave must succeed"
+ "Split cout offset vector size must be same as split"
+ "Split name vector size must be same as split"
+ "Split transforms vector size must be same as split"
+ "Tensor dimensions "
+ "Tensor dimensions N%!z(MISSING)dD%!z(MISSING)dC%!z(MISSING)dH%!z(MISSING)dW%!z(MISSING)d (incoming) and N%!z(MISSING)dD%!z(MISSING)dC%!z(MISSING)dH%!z(MISSING)dW%!z(MISSING)d (liveout) are not within supported range, N[%!z(MISSING)d-%!z(MISSING)d]D[%!z(MISSING)d-%!z(MISSING)d]C[%!z(MISSING)d-%!z(MISSING)d]H[%!z(MISSING)d-%!z(MISSING)d]W[%!z(MISSING)d-%!z(MISSING)d]."
+ "Too many operations in the procedure"
+ "Unsupported chained producer with overlap in ReductionAccumulationRetention"
+ "W["
+ "We only support 4x4x1"
+ "ZinChannelToSpaceLargeFactorCompositeLayer has at least 1 layer."
+ "ZinChannelToSpaceLargeFactorCompositeLayer input must be unique"
+ "ZinComputeProgramStatus ZinComputeProgramValidateLCThread(uint32_t, const void *, const void *, const void *)"
+ "_interleaved"
+ "_post_shuffle"
+ "_remove_identity_div_mul"
+ "aligned_td_end_addr is divisible by 64"
+ "ane_kick_1"
+ "disable-layernorm-opt"
+ "enable-low-effort-cp-allocation"
+ "fdram-fragmentation-factor"
+ "optimize-kernel-coalescing-with-kernel-streaming"
+ "supportOptimizedIOBuffer"
+ "tile_height <= hout"
+ "tile_height <= hout + hw.common_config.ane_common_config.tile_cfg.overlap_pad_top + hw.common_config.ane_common_config.tile_cfg.overlap_pad_bottom"
+ "uint32_t *GetPointerAtOffset(const std::span<uint32_t> &, const size_t, const size_t)"
- "Missing basic block."
- "Schedule is not populated yet"
- "Tensor dimensions N%!z(MISSING)dD%!z(MISSING)dC%!z(MISSING)dH%!z(MISSING)dW%!z(MISSING)d are not within supported range, N[%!z(MISSING)d-%!z(MISSING)d]D[%!z(MISSING)d-%!z(MISSING)d]C[%!z(MISSING)d-%!z(MISSING)d]H[%!z(MISSING)d-%!z(MISSING)d]W[%!z(MISSING)d-%!z(MISSING)d]."
- "This layer has multiple output tensors. Please specify corresponding output port"

```
