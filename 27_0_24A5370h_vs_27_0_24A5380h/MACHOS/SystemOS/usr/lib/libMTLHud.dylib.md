## libMTLHud.dylib

> `/usr/lib/libMTLHud.dylib`

```diff

-  __TEXT.__text: 0x2fb00
+  __TEXT.__text: 0x31348
   __TEXT.__auth_stubs: 0xc80
-  __TEXT.__objc_stubs: 0x3b00
+  __TEXT.__objc_stubs: 0x3b40
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x1cf4
+  __TEXT.__objc_methlist: 0x1d0c
   __TEXT.__const: 0x448
-  __TEXT.__gcc_except_tab: 0x2008
-  __TEXT.__cstring: 0x6bf2
+  __TEXT.__gcc_except_tab: 0x208c
+  __TEXT.__cstring: 0x6c99
   __TEXT.__objc_classname: 0x3be
-  __TEXT.__objc_methname: 0x4952
-  __TEXT.__objc_methtype: 0x3f78
+  __TEXT.__objc_methname: 0x49e4
+  __TEXT.__objc_methtype: 0x4462
   __TEXT.__ustring: 0xb8
   __TEXT.__oslogstring: 0x9a
-  __TEXT.__unwind_info: 0xe20
+  __TEXT.__unwind_info: 0xe90
   __DATA_CONST.__const: 0xff8
-  __DATA_CONST.__cfstring: 0x3380
+  __DATA_CONST.__cfstring: 0x3400
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xc0
-  __DATA_CONST.__objc_intobj: 0x6a8
-  __DATA_CONST.__objc_arraydata: 0x488
+  __DATA_CONST.__objc_intobj: 0x6c0
+  __DATA_CONST.__objc_arraydata: 0x498
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__auth_got: 0x658
-  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__got: 0x208
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA.__objc_const: 0x3450
-  __DATA.__objc_selrefs: 0x1518
-  __DATA.__objc_ivar: 0x1ec
+  __DATA.__objc_const: 0x34b0
+  __DATA.__objc_selrefs: 0x1528
+  __DATA.__objc_ivar: 0x1f8
   __DATA.__objc_data: 0x910
   __DATA.__data: 0x698
   __DATA.__thread_vars: 0x18
   __DATA.__thread_bss: 0x1
-  __DATA.__bss: 0x1c50
+  __DATA.__bss: 0x1c68
   __DATA.__common: 0x41
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 868
-  Symbols:   2421
-  CStrings:  2422
+  Functions: 895
+  Symbols:   2463
+  CStrings:  2438
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ -[HUDGPUTimeline alignedTimeRangeWithEncoderEnabled:cmdBufferEnabled:]
+ -[HUDGPUTimeline withCurrentCommandBufferTimeline:]
+ OBJC_IVAR_$_HUDGPUTimeline._cmdBufLock
+ OBJC_IVAR_$_HUDGPUTimeline._currentCmdBufTimeline
+ OBJC_IVAR_$_HUDGPUTimeline._updatingCmdBufTimeline
+ __Z43_HUDGPUCommandBufferTimelineBuildUITimelineP32HUDGPUCommandBufferTimelineStore
+ __Z51_HUDGPUCommandBufferTimelineSnapshotFrameTimingDataP41FPMTLMetricsGPUTimeTrackerFrameTimingDataP32HUDGPUCommandBufferTimelineStore
+ __ZNKSt3__111__copy_implclB9fqe220106IP19HUDGPUTimelineTrackS3_S3_Li0EEENS_4pairIT_T1_EES5_T0_S6_
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorI19HUDGPUTimelineTrackEEPS2_EclB9fqe220106Ev
+ __ZNSt3__114__split_bufferI19HUDGPUTimelineTrackRNS_9allocatorIS1_EEE17__destruct_at_endB9fqe220106EPS1_
+ __ZNSt3__114__split_bufferI19HUDGPUTimelineTrackRNS_9allocatorIS1_EEED2Ev
+ __ZNSt3__119__allocate_at_leastB9fqe220106INS_9allocatorI19HUDGPUTimelineTrackEENS_16allocator_traitsIS3_EEEENS_19__allocation_resultINT0_7pointerENS7_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9fqe220106INS_9allocatorI24HUDUISimpleTimelineTrackEENS_16allocator_traitsIS3_EEEENS_19__allocation_resultINT0_7pointerENS7_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9fqe220106INS_9allocatorI29HUDUISimpleTimelineTrackChunkEENS_16allocator_traitsIS3_EEEENS_19__allocation_resultINT0_7pointerENS7_9size_typeEEERT_m
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorI19HUDGPUTimelineTrackEEPS3_EEED2B9fqe220106Ev
+ __ZNSt3__134__uninitialized_allocator_relocateB9fqe220106INS_9allocatorI19HUDGPUTimelineTrackEEPS2_EEvRT_T0_S7_S7_
+ __ZNSt3__135__uninitialized_allocator_copy_implB9fqe220106INS_9allocatorI19HUDGPUTimelineTrackEEPS2_S4_S4_EET2_RT_T0_T1_S5_
+ __ZNSt3__16vectorI19HUDGPUTimelineTrackNS_9allocatorIS1_EEE11__vallocateB9fqe220106Em
+ __ZNSt3__16vectorI19HUDGPUTimelineTrackNS_9allocatorIS1_EEE13__vdeallocateEv
+ __ZNSt3__16vectorI19HUDGPUTimelineTrackNS_9allocatorIS1_EEE16__destroy_vectorclB9fqe220106Ev
+ __ZNSt3__16vectorI19HUDGPUTimelineTrackNS_9allocatorIS1_EEE18__assign_with_sizeB9fqe220106INS_17_ClassicAlgPolicyEPS1_S7_EEvT0_T1_l
+ __ZNSt3__16vectorI19HUDGPUTimelineTrackNS_9allocatorIS1_EEE20__throw_length_errorB9fqe220106Ev
+ __ZNSt3__16vectorI19HUDGPUTimelineTrackNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJEEEPS1_DpOT_
+ __ZNSt3__16vectorI19HUDGPUTimelineTrackNS_9allocatorIS1_EEE5clearB9fqe220106Ev
+ __ZNSt3__16vectorI21FPMTLMetricsTimeRangeNS_9allocatorIS1_EEE16__init_with_sizeB9fqe220106IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorI24HUDUISimpleTimelineTrackNS_9allocatorIS1_EEE11__vallocateB9fqe220106Em
+ __ZNSt3__16vectorI24HUDUISimpleTimelineTrackNS_9allocatorIS1_EEE18__assign_with_sizeB9fqe220106INS_17_ClassicAlgPolicyEPS1_S7_EEvT0_T1_l
+ __ZNSt3__16vectorI24HUDUISimpleTimelineTrackNS_9allocatorIS1_EEE20__throw_length_errorB9fqe220106Ev
+ __ZNSt3__16vectorI24HUDUISimpleTimelineTrackNS_9allocatorIS1_EEE6resizeEm
+ __ZNSt3__16vectorI29HUDUISimpleTimelineTrackChunkNS_9allocatorIS1_EEE11__vallocateB9fqe220106Em
+ __ZNSt3__16vectorI29HUDUISimpleTimelineTrackChunkNS_9allocatorIS1_EEE18__assign_with_sizeB9fqe220106INS_17_ClassicAlgPolicyEPS1_S7_EEvT0_T1_l
+ __ZNSt3__16vectorI29HUDUISimpleTimelineTrackChunkNS_9allocatorIS1_EEE20__throw_length_errorB9fqe220106Ev
+ __ZNSt3__16vectorI29HUDUISimpleTimelineTrackChunkNS_9allocatorIS1_EEE6resizeEm
+ ___82-[HUDUserClientMainWindow draw:drawableState:fontSize:frame:layout:height:qrCode:]_block_invoke_5
+ ___block_descriptor_64_e80_v32?0^{HUDUISimpleTimeline=^{HUDUISimpleTimelineTrack}QQ^Q}8{HUDTimeRange=QQ}16l
+ _objc_msgSend$alignedTimeRangeWithEncoderEnabled:cmdBufferEnabled:
+ _objc_msgSend$withCurrentCommandBufferTimeline:
- ___block_descriptor_56_e80_v32?0^{HUDUISimpleTimeline=^{HUDUISimpleTimelineTrack}QQ^Q}8{HUDTimeRange=QQ}16l
CStrings:
+ "Cmd Buffer"
+ "MTL_HUD_COMMAND_BUFFER_GPU_TIMELINE_FRAME_COUNT"
+ "MTL_HUD_COMMAND_BUFFER_GPU_TIMELINE_HEIGHT"
+ "MTL_HUD_COMMAND_BUFFER_GPU_TIMELINE_SWAP_DELTA"
+ "^{_MTLHUDConfig=BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB[2c]ffffffQQQQdfQddfffffIfIfIIQi@}16@0:8"
+ "_cmdBufLock"
+ "_currentCmdBufTimeline"
+ "_updatingCmdBufTimeline"
+ "alignedTimeRangeWithEncoderEnabled:cmdBufferEnabled:"
+ "cmdbufgputimeline"
+ "withCurrentCommandBufferTimeline:"
+ "{HUDGPUCommandBufferTimelineStore=\"allRanges\"{vector<FPMTLMetricsTimeRange, std::allocator<FPMTLMetricsTimeRange>>=\"__begin_\"^{FPMTLMetricsTimeRange}\"__end_\"^{FPMTLMetricsTimeRange}\"\"{?=\"__cap_\"^{FPMTLMetricsTimeRange}}}\"frameNumbers\"{vector<unsigned long long, std::allocator<unsigned long long>>=\"__begin_\"^Q\"__end_\"^Q\"\"{?=\"__cap_\"^Q}}\"markers\"{vector<unsigned long long, std::allocator<unsigned long long>>=\"__begin_\"^Q\"__end_\"^Q\"\"{?=\"__cap_\"^Q}}\"laneTracks\"{vector<HUDGPUTimelineTrack, std::allocator<HUDGPUTimelineTrack>>=\"__begin_\"^{HUDGPUTimelineTrack}\"__end_\"^{HUDGPUTimelineTrack}\"\"{?=\"__cap_\"^{HUDGPUTimelineTrack}}}\"uiTrackChunks\"{vector<HUDUISimpleTimelineTrackChunk, std::allocator<HUDUISimpleTimelineTrackChunk>>=\"__begin_\"^{HUDUISimpleTimelineTrackChunk}\"__end_\"^{HUDUISimpleTimelineTrackChunk}\"\"{?=\"__cap_\"^{HUDUISimpleTimelineTrackChunk}}}\"uiTracks\"{vector<HUDUISimpleTimelineTrack, std::allocator<HUDUISimpleTimelineTrack>>=\"__begin_\"^{HUDUISimpleTimelineTrack}\"__end_\"^{HUDUISimpleTimelineTrack}\"\"{?=\"__cap_\"^{HUDUISimpleTimelineTrack}}}\"uiTimeline\"{HUDUISimpleTimeline=\"tracks\"^{HUDUISimpleTimelineTrack}\"numTracks\"Q\"numMarkers\"Q\"markers\"^Q}\"lastPresentedTime\"Q\"earliestTime\"Q\"latestTime\"Q\"sampleCount\"Q}"
+ "{HUDTimeRange=QQ}24@0:8B16B20"
- "^{_MTLHUDConfig=BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB[2c]ffffffQQQQddfffffIfIfIIQi@}16@0:8"

```
