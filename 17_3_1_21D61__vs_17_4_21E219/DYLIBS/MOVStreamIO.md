## MOVStreamIO

> `/System/Library/PrivateFrameworks/MOVStreamIO.framework/MOVStreamIO`

```diff

-3.24.0.0.0
-  __TEXT.__text: 0x5b7c4
-  __TEXT.__auth_stubs: 0xf10
-  __TEXT.__objc_methlist: 0x4b94
-  __TEXT.__const: 0x330
-  __TEXT.__cstring: 0x5e67
-  __TEXT.__oslogstring: 0x2ee3
-  __TEXT.__gcc_except_tab: 0x8e20
-  __TEXT.__ustring: 0x200
-  __TEXT.__unwind_info: 0x25e4
-  __TEXT.__eh_frame: 0x100
-  __TEXT.__objc_classname: 0xcd9
-  __TEXT.__objc_methname: 0xb88b
-  __TEXT.__objc_methtype: 0x4954
-  __TEXT.__objc_stubs: 0x7aa0
-  __DATA_CONST.__got: 0x438
-  __DATA_CONST.__const: 0x5c0
-  __DATA_CONST.__objc_classlist: 0x2e0
+3.25.2.0.0
+  __TEXT.__text: 0x5f210
+  __TEXT.__auth_stubs: 0xfd0
+  __TEXT.__objc_methlist: 0x4d0c
+  __TEXT.__const: 0x3a0
+  __TEXT.__cstring: 0x63a3
+  __TEXT.__oslogstring: 0x2eef
+  __TEXT.__gcc_except_tab: 0x9458
+  __TEXT.__ustring: 0x242
+  __TEXT.__unwind_info: 0x26cc
+  __TEXT.__eh_frame: 0x114
+  __TEXT.__objc_classname: 0xd04
+  __TEXT.__objc_methname: 0xbdef
+  __TEXT.__objc_methtype: 0x4b5e
+  __TEXT.__objc_stubs: 0x7dc0
+  __DATA_CONST.__got: 0x458
+  __DATA_CONST.__const: 0x660
+  __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xb4d8
-  __DATA_CONST.__objc_selrefs: 0x2758
-  __DATA_CONST.__objc_arraydata: 0x248
-  __AUTH_CONST.__const: 0x350
-  __AUTH_CONST.__cfstring: 0x4200
-  __AUTH_CONST.__objc_const: 0x1e00
-  __AUTH_CONST.__objc_intobj: 0x720
+  __DATA_CONST.__objc_const: 0xb6e8
+  __DATA_CONST.__objc_selrefs: 0x2840
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x3b8
+  __DATA_CONST.__objc_superrefs: 0x180
+  __DATA_CONST.__objc_arraydata: 0x278
+  __AUTH_CONST.__const: 0x330
+  __AUTH_CONST.__cfstring: 0x4600
+  __AUTH_CONST.__objc_const: 0x1e48
+  __AUTH_CONST.__objc_intobj: 0x810
   __AUTH_CONST.__objc_doubleobj: 0x90
-  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x7a0
-  __AUTH.__objc_data: 0x1cc0
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x3b0
-  __DATA.__objc_superrefs: 0x178
-  __DATA.__objc_ivar: 0x498
+  __AUTH_CONST.__auth_got: 0x800
+  __AUTH.__objc_data: 0x1d10
+  __DATA.__objc_ivar: 0x4bc
   __DATA.__data: 0x8a0
   __DATA.__bss: 0x148
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 017EE570-B24D-3530-B043-7EB15EA088A2
-  Functions: 1714
-  Symbols:   6628
-  CStrings:  3642
+  UUID: 55FA9A8C-A741-3172-9F17-FDAC0F6C1650
+  Functions: 1758
+  Symbols:   6792
+  CStrings:  3768
 
Symbols:
+ +[AVMetadataItem(MIOExtensions) trackMetadataItemWithStereoViewEncoding:]
+ +[MIOHEVCStreamOutputSettings hevcSettingsWithProfileLevel:encoderType:frameRate:mastery:enableAVEHighPerformanceProfile:]
+ +[MIOHEVCStreamOutputSettings outputBitDepthIfRequiredForEncoderType:]
+ +[MIOPixelBufferUtility transferAttachmentForKey:fromBuffer:toBuffer:]
+ +[MOVStreamIOUtility stereoConfigurationWidth:height:pixelFormat:frameRate:additionalEncoderSettings:]
+ -[MIOFifoBufferItem setTaggedBufferGroup:]
+ -[MIOFifoBufferItem setTaggedBufferPts:]
+ -[MIOFifoBufferItem taggedBufferGroup]
+ -[MIOFifoBufferItem taggedBufferPts]
+ -[MIOWriterBufferStreamInput doNotRecordAttachments]
+ -[MIOWriterBufferStreamInput setDoNotRecordAttachments:]
+ -[MIOWriterBufferStreamInput taggedPixelBufferAttributes]
+ -[MIOWriterPixelBufferStreamInput strictlyEnforceBufferCapacity]
+ -[MIOWriterStereoPixelBufferStreamInput .cxx_destruct]
+ -[MIOWriterStereoPixelBufferStreamInput appendLeftPixelBuffer:rightPixelBuffer:pts:error:]
+ -[MIOWriterStereoPixelBufferStreamInput dealloc]
+ -[MIOWriterStereoPixelBufferStreamInput initWithStreamId:format:recordingConfig:]
+ -[MIOWriterStereoPixelBufferStreamInput init]
+ -[MIOWriterStereoPixelBufferStreamInput sampleReorderingEnabled]
+ -[MIOWriterStereoPixelBufferStreamInput taggedPixelBufferAttributes]
+ -[MIOWriterStreamInput finalizeProcessing]
+ -[MIOWriterStreamInput setThreadingOption:]
+ -[MIOWriterStreamInput strictlyEnforceBufferCapacity]
+ -[MIOWriterStreamInput threadingOption]
+ -[MOVStreamReader copyNextStereoFramesForStream:leftBuffer:rightBuffer:timestamp:error:]
+ -[MOVStreamReader initWithAsset:delegate:error:]
+ -[MOVStreamReader isStereoStream:]
+ -[MOVStreamReaderStreamOutput copyNextStereoFrames:rightBuffer:timestamp:error:]
+ -[MOVStreamReaderStreamOutput determineStereoLayerIDs:]
+ -[MOVStreamReaderStreamOutput isStereoVideoStream]
+ -[MOVStreamReaderStreamOutput setStereoVideoStream:]
+ -[MOVStreamReaderStreamOutput stereoFramesFromSampleBuffer:outLeft:outRight:error:]
+ -[MOVStreamReaderStreamOutput stereoFramesFromSampleBuffer:outLeft:outRight:error:].cold.1
+ -[MOVStreamReaderStreamOutput useDefaultMIOLayerIds]
+ -[MOVStreamWriter startSessionWithFallbackSampleTime:streamId:mediaType:writerDelegate:delegateCallbackQueue:error:]
+ GCC_except_table101
+ GCC_except_table109
+ GCC_except_table110
+ GCC_except_table113
+ GCC_except_table114
+ GCC_except_table118
+ GCC_except_table122
+ GCC_except_table123
+ GCC_except_table127
+ GCC_except_table132
+ GCC_except_table133
+ GCC_except_table149
+ GCC_except_table150
+ GCC_except_table166
+ GCC_except_table167
+ GCC_except_table216
+ GCC_except_table221
+ GCC_except_table71
+ GCC_except_table83
+ GCC_except_table87
+ _AVVideoDecompressionPropertiesKey
+ _CFArrayAppendValue
+ _CFArrayCreateMutable
+ _CMVideoFormatDescriptionCopyTagCollectionArray
+ _CVBufferCopyAttachment
+ _CVBufferRemoveAttachment
+ _FigSampleBufferGetTaggedBufferGroup
+ _FigTagCollectionCreate
+ _FigTagCollectionGetTagsWithCategory
+ _FigTagGetSInt64Value
+ _FigTagMakeWithSInt64Value
+ _FigTaggedBufferGroupCreate
+ _FigTaggedBufferGroupGetCVPixelBufferAtIndex
+ _FigTaggedBufferGroupGetCount
+ _FigTaggedBufferGroupGetTagCollectionAtIndex
+ _OBJC_CLASS_$_AVAssetWriterInputTaggedPixelBufferGroupAdaptor
+ _OBJC_CLASS_$_MIOWriterStereoPixelBufferStreamInput
+ _OBJC_IVAR_$_MIOFifoBufferItem._taggedBufferGroup
+ _OBJC_IVAR_$_MIOFifoBufferItem._taggedBufferPts
+ _OBJC_IVAR_$_MIOWriterBufferStreamInput._doNotRecordAttachments
+ _OBJC_IVAR_$_MIOWriterBufferStreamInput._taggedPixelBufferGroupAdaptor
+ _OBJC_IVAR_$_MIOWriterStereoPixelBufferStreamInput._config
+ _OBJC_IVAR_$_MIOWriterStereoPixelBufferStreamInput._tagCollectionArray
+ _OBJC_IVAR_$_MIOWriterStreamInput._threadingOption
+ _OBJC_IVAR_$_MOVStreamReaderStreamOutput._stereoVideoStream
+ _OBJC_IVAR_$_MOVStreamReaderStreamOutput._videoLayerIds
+ _OBJC_METACLASS_$_MIOWriterStereoPixelBufferStreamInput
+ __OBJC_$_INSTANCE_METHODS_MIOWriterStereoPixelBufferStreamInput
+ __OBJC_$_INSTANCE_VARIABLES_MIOWriterStereoPixelBufferStreamInput
+ __OBJC_$_PROP_LIST_MIOFrameProcessor.69
+ __OBJC_CLASS_RO_$_MIOWriterStereoPixelBufferStreamInput
+ __OBJC_METACLASS_RO_$_MIOWriterStereoPixelBufferStreamInput
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEENS_16reverse_iteratorIPS6_EEEclB8ue170006Ev
+ __ZNKSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN12_GLOBAL__N_119StreamRecordingDataENS_4lessIS6_EENS4_INS_4pairIKS6_S8_EEEEE5countB8ue170006ERSC_
+ __ZNKSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN12_GLOBAL__N_121MetadataRecordingDataENS_4lessIS6_EENS4_INS_4pairIKS6_S8_EEEEE5countB8ue170006ERSC_
+ __ZNKSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS0_IS6_N12_GLOBAL__N_121MetadataRecordingDataENS_4lessIS6_EENS4_INS_4pairIKS6_S8_EEEEEESA_NS4_INSB_ISC_SF_EEEEE5countB8ue170006ERSC_
+ __ZNKSt3__14lessINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ue170006ERKS6_S9_
+ __ZNKSt3__16vectorI11CMTimeRangeNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorI6CMTimeNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE20__throw_length_errorB8ue170006Ev
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN12_GLOBAL__N_119StreamRecordingDataEEEPvEENS_22__tree_node_destructorINS6_ISD_EEEEED1B8ue170006Ev
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN12_GLOBAL__N_121MetadataRecordingDataEEEPvEENS_22__tree_node_destructorINS6_ISD_EEEEED1B8ue170006Ev
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3mapIS8_N12_GLOBAL__N_121MetadataRecordingDataENS_4lessIS8_EENS6_INS_4pairIKS8_SB_EEEEEEEEPvEENS_22__tree_node_destructorINS6_ISL_EEEEED1B8ue170006Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE25__init_copy_ctor_externalEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ue170006ILi0EEEPKc
+ __ZNSt3__114__split_bufferINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERNS4_IS6_EEE17__destruct_at_endB8ue170006EPS6_
+ __ZNSt3__116allocator_traitsINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEN12_GLOBAL__N_119StreamRecordingDataEEEPvEEEEE7destroyB8ue170006INS_4pairIKS8_SA_EEvvEEvRSE_PT_
+ __ZNSt3__116allocator_traitsINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEN12_GLOBAL__N_121MetadataRecordingDataEEEPvEEEEE7destroyB8ue170006INS_4pairIKS8_SA_EEvvEEvRSE_PT_
+ __ZNSt3__116allocator_traitsINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEENS_3mapIS8_N12_GLOBAL__N_121MetadataRecordingDataENS_4lessIS8_EENS1_INS_4pairIKS8_SB_EEEEEEEEPvEEEEE7destroyB8ue170006INSE_ISF_SI_EEvvEEvRSM_PT_
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorI11CMTimeRangeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorI6CMTimeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEE6CMTimeEEPvEEEEEclB8ue170006EPSC_
+ __ZNSt3__127__tree_balance_after_insertB8ue170006IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEEEENS_16reverse_iteratorIPS7_EEEEED2B8ue170006Ev
+ __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN12_GLOBAL__N_119StreamRecordingDataENS_4lessIS6_EENS4_INS_4pairIKS6_S8_EEEEE4findB8ue170006ERSC_
+ __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN12_GLOBAL__N_121MetadataRecordingDataENS_4lessIS6_EENS4_INS_4pairIKS6_S8_EEEEE4findB8ue170006ERSC_
+ __ZNSt3__13setIjNS_4lessIjEENS_9allocatorIjEEEC2B8ue170006ESt16initializer_listIjERKS2_
+ __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ue170006INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEENS_16reverse_iteratorIPS6_EESA_SA_EET2_RT_T0_T1_SB_
+ __ZNSt3__16vectorI11CMTimeRangeNS_9allocatorIS1_EEE11__vallocateB8ue170006Em
+ __ZNSt3__16vectorI11CMTimeRangeNS_9allocatorIS1_EEE18__assign_with_sizeB8ue170006IPS1_S6_EEvT_T0_l
+ __ZNSt3__16vectorI6CMTimeNS_9allocatorIS1_EEE11__vallocateB8ue170006Em
+ __ZNSt3__16vectorI6CMTimeNS_9allocatorIS1_EEE18__assign_with_sizeB8ue170006IPS1_S6_EEvT_T0_l
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__destroy_vectorclB8ue170006Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE21__push_back_slow_pathIRKS6_EEvOT_
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE7__clearB8ue170006Ev
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ ___33-[MIOWriterStreamInput canAppend]_block_invoke_2
+ ___41-[MOVStreamWriter processFinishRecording]_block_invoke.448
+ ___41-[MOVStreamWriter processFinishRecording]_block_invoke.449
+ ___58-[MIOWriterMetadataGroupStreamInput appendMetadata:error:]_block_invoke_2
+ ___63-[MIOWriterDataStreamInput appendMetadata:withTimeStamp:error:]_block_invoke.5
+ ___72-[MIOWriterPixelBufferStreamInput appendPixelBuffer:pts:timeCode:error:]_block_invoke.179
+ ___73-[MIOWriterSampleBufferStreamInput appendSampleBuffer:attachments:error:]_block_invoke_2
+ ___75-[MIOWriterSampleBufferStreamInput appendSampleBuffer:metadataGroup:error:]_block_invoke_2
+ ___90-[MIOWriterStereoPixelBufferStreamInput appendLeftPixelBuffer:rightPixelBuffer:pts:error:]_block_invoke
+ ___90-[MIOWriterStereoPixelBufferStreamInput appendLeftPixelBuffer:rightPixelBuffer:pts:error:]_block_invoke.163
+ ___block_descriptor_104_ea8_32s40w_e5_B8?0lw40l8s32l8
+ ___block_descriptor_112_ea8_32s40s48c66_ZTSNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE_e5_v8?0l
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_40_ea8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40s48w_e5_B8?0lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40w_e5_B8?0lw40l8s32l8
+ ___block_descriptor_80_e8_32s40s48w_e5_B8?0lw48l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40w_e5_B8?0lw40l8s32l8
+ ___block_descriptor_88_ea8_32s40w_e5_B8?0lw40l8s32l8
+ ___block_literal_global.135
+ ___block_literal_global.152
+ ___block_literal_global.476
+ ___copy_helper_block_ea8_48c66_ZTSNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ ___destroy_helper_block_ea8_48c66_ZTSNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
+ __unnamed_array_storage.252
+ __unnamed_array_storage.268
+ _kCFTypeArrayCallBacks
+ _kFigTagInvalid
+ _kMIODoNotRecordAttachments
+ _kMIOStereoVideoEncoding
+ _kMIOTaggedPixelBufferGroupAdaptorPixelBufferAttributes
+ _kVTCompressionPropertyKey_MVHEVCVideoLayerIDs
+ _objc_msgSend$appendTaggedPixelBufferGroup:withPresentationTime:
+ _objc_msgSend$combineLeftBuffer:rightBuffer:
+ _objc_msgSend$copyNextStereoFrames:rightBuffer:timestamp:error:
+ _objc_msgSend$determineStereoLayerIDs:
+ _objc_msgSend$doNotRecordAttachments
+ _objc_msgSend$finalizeProcessing
+ _objc_msgSend$hevcSettingsWithProfileLevel:encoderType:frameRate:mastery:enableAVEHighPerformanceProfile:
+ _objc_msgSend$initWithAsset:delegate:error:
+ _objc_msgSend$initWithAssetWriterInput:sourcePixelBufferAttributes:
+ _objc_msgSend$isStereoVideoStream
+ _objc_msgSend$numberValue
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$outputBitDepthIfRequiredForEncoderType:
+ _objc_msgSend$setDoNotRecordAttachments:
+ _objc_msgSend$setTaggedBufferGroup:
+ _objc_msgSend$setTaggedBufferPts:
+ _objc_msgSend$startSessionWithFallbackSampleTime:streamId:mediaType:writerDelegate:delegateCallbackQueue:error:
+ _objc_msgSend$stereoFramesFromSampleBuffer:outLeft:outRight:error:
+ _objc_msgSend$strictlyEnforceBufferCapacity
+ _objc_msgSend$taggedBufferGroup
+ _objc_msgSend$taggedBufferPts
+ _objc_msgSend$taggedPixelBufferAttributes
+ _objc_msgSend$threadingOption
+ _objc_msgSend$trackMetadataItemWithStereoViewEncoding:
+ _objc_msgSend$transferAttachmentForKey:fromBuffer:toBuffer:
+ _objc_msgSend$useDefaultMIOLayerIds
- +[MIOHEVCStreamOutputSettings hevcSettingsWithProfileLevel:frameRate:mastery:enableAVEHighPerformanceProfile:]
- +[MIOPixelBufferUtility extendedPixelsRightForPlanarBufferWidth:height:bytesPerRow:format:]
- GCC_except_table102
- GCC_except_table111
- GCC_except_table112
- GCC_except_table115
- GCC_except_table116
- GCC_except_table120
- GCC_except_table125
- GCC_except_table126
- GCC_except_table129
- GCC_except_table134
- GCC_except_table135
- GCC_except_table154
- GCC_except_table155
- GCC_except_table217
- GCC_except_table223
- GCC_except_table76
- GCC_except_table85
- GCC_except_table86
- GCC_except_table88
- _CVBufferGetAttachment
- __OBJC_$_PROP_LIST_MIOFrameProcessor.68
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEENS_16reverse_iteratorIPS6_EEEclB7v160006Ev
- __ZNKSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN12_GLOBAL__N_119StreamRecordingDataENS_4lessIS6_EENS4_INS_4pairIKS6_S8_EEEEE5countB7v160006ERSC_
- __ZNKSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN12_GLOBAL__N_121MetadataRecordingDataENS_4lessIS6_EENS4_INS_4pairIKS6_S8_EEEEE5countB7v160006ERSC_
- __ZNKSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS0_IS6_N12_GLOBAL__N_121MetadataRecordingDataENS_4lessIS6_EENS4_INS_4pairIKS6_S8_EEEEEESA_NS4_INSB_ISC_SF_EEEEE5countB7v160006ERSC_
- __ZNKSt3__14lessINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB7v160006ERKS6_S9_
- __ZNKSt3__16vectorI11CMTimeRangeNS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorI6CMTimeNS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE20__throw_length_errorB7v160006Ev
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN12_GLOBAL__N_119StreamRecordingDataEEEPvEENS_22__tree_node_destructorINS6_ISD_EEEEED1B7v160006Ev
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN12_GLOBAL__N_121MetadataRecordingDataEEEPvEENS_22__tree_node_destructorINS6_ISD_EEEEED1B7v160006Ev
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_3mapIS8_N12_GLOBAL__N_121MetadataRecordingDataENS_4lessIS8_EENS6_INS_4pairIKS8_SB_EEEEEEEEPvEENS_22__tree_node_destructorINS6_ISL_EEEEED1B7v160006Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B7v160006IDnEEPKc
- __ZNSt3__114__split_bufferINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERNS4_IS6_EEE17__destruct_at_endB7v160006EPS6_
- __ZNSt3__116allocator_traitsINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEN12_GLOBAL__N_119StreamRecordingDataEEEPvEEEEE7destroyB7v160006INS_4pairIKS8_SA_EEvvEEvRSE_PT_
- __ZNSt3__116allocator_traitsINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEN12_GLOBAL__N_121MetadataRecordingDataEEEPvEEEEE7destroyB7v160006INS_4pairIKS8_SA_EEvvEEvRSE_PT_
- __ZNSt3__116allocator_traitsINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEENS_3mapIS8_N12_GLOBAL__N_121MetadataRecordingDataENS_4lessIS8_EENS1_INS_4pairIKS8_SB_EEEEEEEEPvEEEEE7destroyB7v160006INSE_ISF_SI_EEvvEEvRSM_PT_
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorI11CMTimeRangeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorI6CMTimeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEE6CMTimeEEPvEEEEEclB7v160006EPSC_
- __ZNSt3__127__tree_balance_after_insertB7v160006IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS2_IcEEEEEENS_16reverse_iteratorIPS7_EEEEED2B7v160006Ev
- __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN12_GLOBAL__N_119StreamRecordingDataENS_4lessIS6_EENS4_INS_4pairIKS6_S8_EEEEE4findB7v160006ERSC_
- __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN12_GLOBAL__N_121MetadataRecordingDataENS_4lessIS6_EENS4_INS_4pairIKS6_S8_EEEEE4findB7v160006ERSC_
- __ZNSt3__13setIjNS_4lessIjEENS_9allocatorIjEEEC2B7v160006ESt16initializer_listIjERKS2_
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB7v160006INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEENS_16reverse_iteratorIPS6_EESA_SA_EET2_RT_T0_T1_SB_
- __ZNSt3__16vectorI11CMTimeRangeNS_9allocatorIS1_EEE11__vallocateB7v160006Em
- __ZNSt3__16vectorI11CMTimeRangeNS_9allocatorIS1_EEE6assignIPS1_Li0EEEvT_S7_
- __ZNSt3__16vectorI6CMTimeNS_9allocatorIS1_EEE11__vallocateB7v160006Em
- __ZNSt3__16vectorI6CMTimeNS_9allocatorIS1_EEE6assignIPS1_Li0EEEvT_S7_
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__destroy_vectorclB7v160006Ev
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE7__clearB7v160006Ev
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE9push_backB7v160006ERKS6_
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEED2B7v160006Ev
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- ___41-[MOVStreamWriter processFinishRecording]_block_invoke.441
- ___41-[MOVStreamWriter processFinishRecording]_block_invoke.442
- ___block_descriptor_104_ea8_32s40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_112_ea8_32s40s56c66_ZTSNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE_e5_v8?0l
- ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_80_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
- ___block_descriptor_80_e8_32s40w_e5_v8?0lw40l8s32l8
- ___block_literal_global.132
- ___block_literal_global.147
- ___block_literal_global.463
- __unnamed_array_storage.259
- _objc_msgSend$hevcSettingsWithProfileLevel:frameRate:mastery:enableAVEHighPerformanceProfile:
CStrings:
+ "\x021#\x12!"
+ "\a\x11"
+ "-[MOVStreamReaderStreamOutput stereoFramesFromSampleBuffer:outLeft:outRight:error:]"
+ "16a\x12"
+ "3.25.2"
+ "875704934_0"
+ "875704934_1"
+ "@\"AVAssetWriterInputTaggedPixelBufferGroupAdaptor\""
+ "@24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@B@{?=qiIq}Q@qi@iC}16"
+ "@32@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@B@{?=qiIq}Q@qi@iC}16d24"
+ "@36@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@B@{?=qiIq}Q@qi@iC}16d24B32"
+ "@48@0:8@16i24d28@36B44"
+ "@52@0:8Q16Q24I32d36@44"
+ "Attempted to enqueue metadata in full Fifo for stream %@.  Indicates leak in overall pending sample metadata tracking."
+ "B24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@B@{?=qiIq}Q@qi@iC}16"
+ "B48@0:8^{opaqueCMSampleBuffer=}16^^{__CVBuffer}24^^{__CVBuffer}32^@40"
+ "B48@0:8o^^{__CVBuffer}16o^^{__CVBuffer}24o^{?=qiIq}32o^@40"
+ "B56@0:8@16o^^{__CVBuffer}24o^^{__CVBuffer}32o^{?=qiIq}40o^@48"
+ "B64@0:8^{__CVBuffer=}16^{__CVBuffer=}24{?=qiIq}32^@56"
+ "B80@0:8{?=qiIq}16@40q48@56@64^@72"
+ "B8@?0"
+ "Can't add stream input to the asset writer to stream: %@"
+ "Cannot add metadata input for stream '%@'."
+ "Cannot add sample input for stream '%@'."
+ "DoNotRecordAttachments"
+ "Failed getting FigTagCollectionArray (%d)"
+ "Failed getting multiple FigTagCollections (numCollections=%d)"
+ "Failed getting tag (%d)"
+ "Failed getting video layer tag. Error %d"
+ "FigTagCollectionCreate left failed."
+ "FigTagCollectionCreate right failed."
+ "FigTaggedBufferGroupCreate failed for stream %@."
+ "Frame was dropped because writer or AV input state does not allow writing."
+ "HasLeftStereoEyeView"
+ "I24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@B@{?=qiIq}Q@qi@iC}16"
+ "MIOWriterStereoPixelBufferStreamInput"
+ "No format description found for stereo stream."
+ "No pixel buffer for video layer."
+ "No tagged buffer group in sample buffer."
+ "Q32@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@B@{?=qiIq}Q@qi@iC}16d24"
+ "RequestedMVHEVCVideoLayerIDs"
+ "SampleDescriptionExtensionAtoms"
+ "StereoVideoEncoding"
+ "Stream: %@ inputs are not ready, dropping sample"
+ "T@\"NSString\",?,R,C"
+ "TB,GisStereoVideoStream,V_stereoVideoStream"
+ "TB,R,GisStereoVideoStream"
+ "TB,V_doNotRecordAttachments"
+ "T^{OpaqueCMTaggedBufferGroup=},V_taggedBufferGroup"
+ "TaggedPixelBufferGroupAdaptorPixelBufferAttributes"
+ "Tq,V_threadingOption"
+ "T{?=qiIq},V_taggedBufferPts"
+ "Unknown videoLayerID: %d"
+ "Writer invalid sessionStartTime, startSession failed."
+ "Writer startSession failed: %@"
+ "^{OpaqueCMTaggedBufferGroup=}"
+ "^{OpaqueCMTaggedBufferGroup=}16@0:8"
+ "^{__CFArray=}"
+ "^{__CVBuffer=}40@0:8^{__CVBuffer=}16^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@B@{?=qiIq}Q@qi@iC}24^@32"
+ "^{opaqueCMFormatDescription=}24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@B@{?=qiIq}Q@qi@iC}16"
+ "^{opaqueCMFormatDescription=}32@0:8^{__CVBuffer=}16^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@B@{?=qiIq}Q@qi@iC}24"
+ "_doNotRecordAttachments"
+ "_stereoVideoStream"
+ "_tagCollectionArray"
+ "_taggedBufferGroup"
+ "_taggedBufferPts"
+ "_taggedPixelBufferGroupAdaptor"
+ "_threadingOption"
+ "_videoLayerIds"
+ "_videoLayerIds.count > 1"
+ "appendLeftPixelBuffer:rightPixelBuffer:pts:error:"
+ "appendTaggedPixelBufferGroup:withPresentationTime:"
+ "copyNextStereoFrames:rightBuffer:timestamp:error:"
+ "copyNextStereoFramesForStream:leftBuffer:rightBuffer:timestamp:error:"
+ "d24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@B@{?=qiIq}Q@qi@iC}16"
+ "determineStereoLayerIDs:"
+ "doNotRecordAttachments"
+ "finalizeProcessing"
+ "hevcSettingsWithProfileLevel:encoderType:frameRate:mastery:enableAVEHighPerformanceProfile:"
+ "hvcC"
+ "i24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@B@{?=qiIq}Q@qi@iC}16"
+ "initWithAsset:delegate:error:"
+ "initWithAssetWriterInput:sourcePixelBufferAttributes:"
+ "isStereoStream:"
+ "isStereoVideoStream"
+ "lhvC"
+ "mdta/com.apple.stream_stereo_video"
+ "mio.append.stereo.sample.buffer"
+ "numberValue"
+ "numberWithLongLong:"
+ "outputBitDepthIfRequiredForEncoderType:"
+ "setDoNotRecordAttachments:"
+ "setStereoVideoStream:"
+ "setTaggedBufferGroup:"
+ "setTaggedBufferPts:"
+ "setThreadingOption:"
+ "startSessionWithFallbackSampleTime:streamId:mediaType:writerDelegate:delegateCallbackQueue:error:"
+ "startWritingThread-metadata"
+ "startWritingThread-sample"
+ "startWritingThreadForNonMetadataOnlyThreadId"
+ "stereoConfigurationWidth:height:pixelFormat:frameRate:additionalEncoderSettings:"
+ "stereoFramesFromSampleBuffer:outLeft:outRight:error:"
+ "stereoVideoStream"
+ "strictlyEnforceBufferCapacity"
+ "taggedBufferGroup"
+ "taggedBufferPts"
+ "taggedPixelBufferAttributes"
+ "threadingOption"
+ "trackMetadataItemWithStereoViewEncoding:"
+ "transferAttachmentForKey:fromBuffer:toBuffer:"
+ "useDefaultMIOLayerIds"
+ "v24@0:8^{OpaqueCMTaggedBufferGroup=}16"
+ "v40@0:8^{__CFString=}16^{__CVBuffer=}24^{__CVBuffer=}32"
+ "writeNextItemFromFifo dropped sample because writer does not allow writing anymore."
+ "\xe2"
+ "\xe5\x11"
- "\x021%!"
- "3.24.0"
- "@24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@iC}16"
- "@32@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@iC}16d24"
- "@36@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@iC}16d24B32"
- "@44@0:8@16d24@32B40"
- "B24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@iC}16"
- "HEVC_Main422_AutoLevel"
- "I24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@iC}16"
- "Info: The metadata append triggered the start for the asset writer. Are you sure this is what you want?"
- "Not supported setting: 8bit 422"
- "Q32@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@iC}16d24"
- "^{__CVBuffer=}40@0:8^{__CVBuffer=}16^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@iC}24^@32"
- "^{opaqueCMFormatDescription=}24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@iC}16"
- "^{opaqueCMFormatDescription=}32@0:8^{__CVBuffer=}16^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@iC}24"
- "d24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@iC}16"
- "extendedPixelsRightForPlanarBufferWidth:height:bytesPerRow:format:"
- "fa\x12"
- "hevcSettingsWithProfileLevel:frameRate:mastery:enableAVEHighPerformanceProfile:"
- "i24@0:8^{StreamRecordingData=^{opaqueCMFormatDescription}B@@@@@@Q@@@@@@@@{?=qiIq}Q@qi@iC}16"
- "q44@0:8Q16Q24Q32I40"
- "\xd2"
- "\xd5\x11"

```
