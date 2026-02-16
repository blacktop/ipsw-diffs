## GPUToolsCapture

> `/System/Library/PrivateFrameworks/GPUToolsCapture.framework/GPUToolsCapture`

```diff

-313.2.0.0.0
-  __TEXT.__text: 0x26ac2c
+314.9.0.0.0
+  __TEXT.__text: 0x2638ac
   __TEXT.__auth_stubs: 0x1780
-  __TEXT.__objc_stubs: 0x16aa0
+  __TEXT.__objc_stubs: 0x16dc0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x12644
-  __TEXT.__const: 0x79c0
-  __TEXT.__cstring: 0x26c87
-  __TEXT.__gcc_except_tab: 0x8dc
-  __TEXT.__objc_methname: 0x19c37
-  __TEXT.__objc_classname: 0x157b
-  __TEXT.__objc_methtype: 0x9c9c
-  __TEXT.__oslogstring: 0xedb
+  __TEXT.__objc_methlist: 0x128a4
+  __TEXT.__const: 0x46d0
+  __TEXT.__cstring: 0x27647
+  __TEXT.__gcc_except_tab: 0x8f4
+  __TEXT.__objc_methname: 0x1a372
+  __TEXT.__objc_classname: 0x1570
+  __TEXT.__objc_methtype: 0xa900
+  __TEXT.__oslogstring: 0x11c5
   __TEXT.__ustring: 0x20a
-  __TEXT.__unwind_info: 0x3f78
+  __TEXT.__unwind_info: 0x4300
   __DATA_CONST.__auth_got: 0xbd8
-  __DATA_CONST.__got: 0x800
+  __DATA_CONST.__got: 0x7f8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1c50
-  __DATA_CONST.__cfstring: 0x3ba0
-  __DATA_CONST.__objc_classlist: 0x310
+  __DATA_CONST.__const: 0x1d98
+  __DATA_CONST.__cfstring: 0x3fe0
+  __DATA_CONST.__objc_classlist: 0x318
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x430
+  __DATA_CONST.__objc_protolist: 0x428
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_superrefs: 0x300
+  __DATA_CONST.__objc_protorefs: 0x78
+  __DATA_CONST.__objc_superrefs: 0x308
   __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x19b80
-  __DATA.__objc_selrefs: 0x6a28
-  __DATA.__objc_ivar: 0xaa8
-  __DATA.__objc_data: 0x1ea0
-  __DATA.__data: 0x3458
+  __DATA.__objc_const: 0x1a030
+  __DATA.__objc_selrefs: 0x6be0
+  __DATA.__objc_ivar: 0xadc
+  __DATA.__objc_data: 0x1ef0
+  __DATA.__data: 0x3470
   __DATA.__thread_vars: 0x48
   __DATA.__thread_bss: 0x1018
-  __DATA.__bss: 0x530
-  __DATA.__common: 0x4d
+  __DATA.__bss: 0x558
+  __DATA.__common: 0x55
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: C7D1C1A4-0B8D-36DC-82D8-D384DA64D79E
-  Functions: 7788
-  Symbols:   46362
-  CStrings:  9028
+  UUID: E379BE03-1AE9-30FE-AA30-E41B15C92635
+  Functions: 7878
+  Symbols:   46790
+  CStrings:  9261
 
Symbols:
+ -[CaptureICBSnapshot .cxx_destruct]
+ -[CaptureICBSnapshot addRangeShapshot4:encodeRangeCopy:]
+ -[CaptureICBSnapshot addRangeShapshot:offset:encodeRangeCopy:]
+ -[CaptureICBSnapshot allocateRangeSnapshot]
+ -[CaptureICBSnapshot arg]
+ -[CaptureICBSnapshot funcIndex]
+ -[CaptureICBSnapshot initWithICB:map:traceEncoder:encodeCopy:]
+ -[CaptureICBSnapshot rangeArg]
+ -[CaptureICBSnapshot serialize]
+ -[CaptureICBSnapshotMap clearOnBarrier:]
+ -[CaptureICBSnapshotMap create:]
+ -[CaptureICBSnapshotMap dealloc]
+ -[CaptureICBSnapshotMap find:]
+ -[CaptureICBSnapshotMap init]
+ -[CaptureICBSnapshotMap remove:]
+ -[CaptureMTL4CommandBuffer addCompletionHandler:]
+ -[CaptureMTL4CommandBuffer isRecordingData]
+ -[CaptureMTL4CommandBuffer popCompletionHandlers]
+ -[CaptureMTL4CommandBuffer setAccelerationStructureDescriptorProcessEvent:]
+ -[CaptureMTL4CommandQueue _signalCompletionHandlers:count:]
+ -[CaptureMTL4ComputeCommandEncoder currentState:]
+ -[CaptureMTL4ComputeCommandEncoder dispatchWithDevicePipelineState:argumentTable:]
+ -[CaptureMTL4ComputeCommandEncoder encodeICBRangeSnapshot:encoder:src:dst:]
+ -[CaptureMTL4ComputeCommandEncoder encodeICBSnapshot:encoder:src:dst:]
+ -[CaptureMTL4ComputeCommandEncoder icbSnapshotResidencySet]
+ -[CaptureMTL4ComputeCommandEncoder takeICBSnapshot:rangeBuffer:traceEncoder:]
+ -[CaptureMTL4ComputeCommandEncoder takeICBSnapshot:traceEncoder:]
+ -[CaptureMTL4RenderCommandEncoder encodeICBRangeSnapshot:encoder:src:dst:]
+ -[CaptureMTL4RenderCommandEncoder encodeICBSnapshot:encoder:src:dst:]
+ -[CaptureMTL4RenderCommandEncoder icbSnapshotResidencySet]
+ -[CaptureMTL4RenderCommandEncoder restoreAfterIcbSnapshot]
+ -[CaptureMTL4RenderCommandEncoder takeICBSnapshot:rangeBuffer:traceEncoder:]
+ -[CaptureMTL4RenderCommandEncoder takeICBSnapshot:traceEncoder:]
+ -[GTDownloadContext finalizeRequest:withData:]
+ -[GTDownloadContext finalizeRequest:withData:subIndex:]
+ -[GTDownloadContext finalizeRequest:withICB:descriptor:]
+ -[GTDownloadContext finalizeRequest:withStore:]
+ -[GTDownloadContext finalizeRequest:withStore:subIndex:]
+ /Library/Caches/com.apple.xbs/EB5EB1E5-3E70-4CA5-90D9-62F5C0E2D199/TemporaryDirectory.Kab9YK/Binaries/GPUToolsDevice/install/TempContent/Objects/GPUToolsFoundation.build/GPUToolsCapture.build/DerivedSources/
+ /Library/Caches/com.apple.xbs/EB5EB1E5-3E70-4CA5-90D9-62F5C0E2D199/TemporaryDirectory.Kab9YK/Binaries/GPUToolsDevice/install/TempContent/Objects/GPUToolsFoundation.build/GPUToolsCapture.build/Objects-normal/arm64e/GPUToolsCapture_lto.o
+ GCC_except_table107
+ GCC_except_table1532
+ GCC_except_table1557
+ GCC_except_table16
+ GCC_except_table1662
+ GCC_except_table1663
+ GCC_except_table1667
+ GCC_except_table1668
+ GCC_except_table1669
+ GCC_except_table1670
+ GCC_except_table1671
+ GCC_except_table1879
+ GCC_except_table1880
+ GCC_except_table1884
+ GCC_except_table1892
+ GCC_except_table2036
+ GCC_except_table2072
+ GCC_except_table219
+ GCC_except_table242
+ GCC_except_table243
+ GCC_except_table2886
+ GCC_except_table2894
+ GCC_except_table298
+ GCC_except_table30
+ GCC_except_table3031
+ GCC_except_table3182
+ GCC_except_table3189
+ GCC_except_table3198
+ GCC_except_table323
+ GCC_except_table3296
+ GCC_except_table4014
+ GCC_except_table43
+ GCC_except_table633
+ GTAccelerationStructureDescriptorDownloader_processCopy.7906
+ GTAccelerationStructureDescriptorDownloader_processRefit.7907
+ GTCorePlatform_isCompositorProcess.isCompositorProcess
+ GTCorePlatform_isCompositorProcess.onceToken
+ GTFormatBytes.units
+ GTMTLCaptureEventBuffer_initializeOnce.onceToken
+ GetStream.20086
+ OBJC_IVAR_$_CaptureICBSnapshot._desc
+ OBJC_IVAR_$_CaptureICBSnapshot._device
+ OBJC_IVAR_$_CaptureICBSnapshot._icbCopy
+ OBJC_IVAR_$_CaptureICBSnapshot._icbOriginal
+ OBJC_IVAR_$_CaptureICBSnapshot._map
+ OBJC_IVAR_$_CaptureICBSnapshot._rangeCopy
+ OBJC_IVAR_$_CaptureICBSnapshot._rangeMem
+ OBJC_IVAR_$_CaptureICBSnapshot._snapshot
+ OBJC_IVAR_$_CaptureICBSnapshot._traceEncoder
+ OBJC_IVAR_$_CaptureICBSnapshotMap._pool
+ OBJC_IVAR_$_CaptureICBSnapshotMap._snapshotMap
+ OBJC_IVAR_$_CaptureMTL4CommandBuffer._accelerationStructureDescriptorProcessEventValue
+ OBJC_IVAR_$_CaptureMTL4CommandBuffer._completionHandlers
+ OBJC_IVAR_$_CaptureMTL4CommandBuffer._isRecordingData
+ OBJC_IVAR_$_CaptureMTL4CommandQueue._completionHandlerSync
+ OBJC_IVAR_$_CaptureMTL4CommandQueue._pool
+ OBJC_IVAR_$_CaptureMTL4ComputeCommandEncoder._deviceUserArgumentTable
+ OBJC_IVAR_$_CaptureMTL4ComputeCommandEncoder._deviceUserState
+ OBJC_IVAR_$_CaptureMTL4ComputeCommandEncoder._icbSnapshotMap
+ OBJC_IVAR_$_CaptureMTL4ComputeCommandEncoder._icbSnapshotResidencySet
+ OBJC_IVAR_$_CaptureMTL4RenderCommandEncoder._icbSnapshotMap
+ OBJC_IVAR_$_CaptureMTL4RenderCommandEncoder._icbSnapshotResidencySet
+ RetainObjectForDescriptorDownloader.9554
+ StoreMTLCompileOptionsUsingEncode.16515
+ _AdvanceMTL4CommandQueue
+ _DYTraceEncode_MTL4CommandQueue_copyBufferMappingsFromBuffer_toBuffer_operations_count
+ _DYTraceEncode_MTL4CommandQueue_copyTextureMappingsFromTexture_toTexture_operations_count
+ _DYTraceEncode_MTL4CommandQueue_updateBufferMappings_heap_operations_count
+ _DYTraceEncode_MTL4CommandQueue_updateTextureMappings_heap_operations_count
+ _DYTraceEncode_MTL4ComputeCommandEncoder_executeCommandsInBuffer_indirectBuffer
+ _DYTraceEncode_MTL4ComputeCommandEncoder_executeCommandsInBuffer_withRange
+ _DYTraceEncode_MTL4RenderCommandEncoder_executeCommandsInBuffer_indirectBuffer
+ _DYTraceEncode_MTL4RenderCommandEncoder_executeCommandsInBuffer_withRange
+ _DYTraceEncode_MTLDevice_convertSparsePixelRegions_toTileRegions_withTileSize_alignmentMode_numRegions
+ _DYTraceEncode_MTLDevice_convertSparseTileRegions_toPixelRegions_withTileSize_numRegions
+ _DYTraceEncode_MTLDevice_newBufferWithLength_options_placementSparsePageSize
+ _FillBufferBindingsFromICB
+ _GTAddActiveMetalLayers
+ _GTArchiveCheckFailed
+ _GTCorePlatform_isCompositorProcess
+ _GTEncodeInterfaceOrientation
+ _GTFenum_isCreateCommandEncoder
+ _GTFileSystem_stderr
+ _GTFileSystem_stdout
+ _GTFile_isTerminal
+ _GTFormatBytes
+ _GTMTL4SMArgumentTable_initializeBindings
+ _GTMTL4SMArgumentTable_isBufferBindingInitialized
+ _GTMTL4SMArgumentTable_isSamplerStateBindingInitialized
+ _GTMTL4SMArgumentTable_isTextureBindingInitialized
+ _GTMTL4SMArgumentTable_setBufferBindingAsInitialized
+ _GTMTL4SMArgumentTable_setSamplerStateBindingAsInitialized
+ _GTMTL4SMArgumentTable_setTextureBindingAsInitialized
+ _GTMTL4SMComputeCommandEncoder_loadIndirectCommand
+ _GTMTL4SMRenderCommandEncoder_loadIndirectCommand
+ _GTMTLCaptureEventBuffer_allocateEntry
+ _GTMTLCaptureEventBuffer_getGPUExecutionOrder
+ _GTMTLCaptureEventBuffer_hasOverflowed
+ _GTMTLCaptureEventBuffer_initializeOnce
+ _GTMTLCaptureEventBuffer_recordGPUEvent_MTL3
+ _GTMTLCaptureEventBuffer_recordGPUEvent_MTL4
+ _GTMTLCaptureEventBuffer_reset
+ _GTMTLCapture_shouldICBSnapshotInsertRenderMemoryBarrier
+ _GTMTLCoreSync_attachListener
+ _GTMTLCoreSync_createWithDevice
+ _GTMTLCoreSync_createWithEvent
+ _GTMTLCoreSync_logOperation
+ _GTMTLCoreSync_signalCPU
+ _GTMTLCoreSync_signalGPUWithHandler_MTL4
+ _GTMTLCoreSync_signalGPU_MTL3
+ _GTMTLCoreSync_signalGPU_MTL4
+ _GTMTLCoreSync_waitCPU
+ _GTMTLCoreSync_waitForValueCPU
+ _GTMTLCoreSync_waitForValueGPU_MTL3
+ _GTMTLCoreSync_waitForValueGPU_MTL4
+ _GTMTLCoreSync_waitGPU_MTL3
+ _GTMTLCoreSync_waitGPU_MTL4
+ _GTMTLDispatchUnrolledICB_MTL4Compute
+ _GTMTLDispatchUnrolledICB_MTL4Render
+ _GTMTLSMCommandEncoder_computePipelineState
+ _GTMTLSMCommandEncoder_renderPipelineState
+ _GTMTLSMContext_getLayers
+ _GTMTLTensorSliceToString
+ _GTResourceDownloaderRequest_markAsPresentDownload
+ _GTResourceTrackerIdentifier
+ _GTResourceTrackerLogOperation
+ _GTString_beginsWith
+ _GTTraceContext_getFlags
+ _GTTraceContext_replaceFlags
+ _GTTraceDispatch_reconstructArgumentTableState
+ _InsertDrawableTextureFenum
+ _LogDownloadRequest
+ _OBJC_CLASS_$_CaptureICBSnapshot
+ _OBJC_CLASS_$_CaptureICBSnapshotMap
+ _OBJC_METACLASS_$_CaptureICBSnapshot
+ _OBJC_METACLASS_$_CaptureICBSnapshotMap
+ _ProcessNonCommandBufferFuncs
+ _SaveMTL4UpdateSparseBufferMappingOperation
+ _SaveMTL4UpdateSparseTextureMappingOperation
+ __Block_byref_object_copy_.11679
+ __Block_byref_object_copy_.3994
+ __Block_byref_object_copy_.4493
+ __Block_byref_object_copy_.7158
+ __Block_byref_object_copy_.8370
+ __Block_byref_object_dispose_.11680
+ __Block_byref_object_dispose_.3995
+ __Block_byref_object_dispose_.4494
+ __Block_byref_object_dispose_.7159
+ __Block_byref_object_dispose_.8371
+ __OBJC_$_INSTANCE_METHODS_CaptureICBSnapshot
+ __OBJC_$_INSTANCE_METHODS_CaptureICBSnapshotMap
+ __OBJC_$_INSTANCE_VARIABLES_CaptureICBSnapshot
+ __OBJC_$_INSTANCE_VARIABLES_CaptureICBSnapshotMap
+ __OBJC_$_PROP_LIST_CaptureICBSnapshot
+ __OBJC_CLASS_RO_$_CaptureICBSnapshot
+ __OBJC_CLASS_RO_$_CaptureICBSnapshotMap
+ __OBJC_METACLASS_RO_$_CaptureICBSnapshot
+ __OBJC_METACLASS_RO_$_CaptureICBSnapshotMap
+ __OBJC_PROTOCOL_REFERENCE_$_MTLResourceSPI
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIxPU18objcproto8NSObject11objc_objectEENS_22__unordered_map_hasherIxNS_4pairIKxS3_EENS_4hashIxEENS_8equal_toIxEELb1EEENS_21__unordered_map_equalIxS8_SC_SA_Lb1EEENS_9allocatorIS8_EEE4findIxEENS_15__hash_iteratorIPNS_11__hash_nodeIS4_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIxPU18objcproto8NSObject11objc_objectEENS_22__unordered_map_hasherIxNS_4pairIKxS3_EENS_4hashIxEENS_8equal_toIxEELb1EEENS_21__unordered_map_equalIxS8_SC_SA_Lb1EEENS_9allocatorIS8_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIxPU18objcproto8NSObject11objc_objectEENS_22__unordered_map_hasherIxNS_4pairIKxS3_EENS_4hashIxEENS_8equal_toIxEELb1EEENS_21__unordered_map_equalIxS8_SC_SA_Lb1EEENS_9allocatorIS8_EEED2Ev
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__16vectorI16GTTelemetryLayerNS_9allocatorIS1_EEE20__throw_length_errorB9fon210106Ev
+ __ZNSt3__16vectorI16GTTelemetryQueueNS_9allocatorIS1_EEE20__throw_length_errorB9fon210106Ev
+ __ZNSt3__16vectorI16GTTelemetryQueueNS_9allocatorIS1_EEE9push_backB9fon210106ERKS1_
+ __ZNSt3__16vectorI17GTTelemetryDeviceNS_9allocatorIS1_EEE20__throw_length_errorB9fon210106Ev
+ __ZSt28__throw_bad_array_new_lengthB9fon210106v
+ ___59-[CaptureMTL4CommandQueue _signalCompletionHandlers:count:]_block_invoke
+ ___68-[CaptureMTLRenderCommandEncoder executeCommandsInBuffer:withRange:]_block_invoke_2
+ ___69-[CaptureMTLComputeCommandEncoder executeCommandsInBuffer:withRange:]_block_invoke_2
+ ___76-[CaptureMTL4RenderCommandEncoder takeICBSnapshot:rangeBuffer:traceEncoder:]_block_invoke
+ ___76-[CaptureMTL4RenderCommandEncoder takeICBSnapshot:rangeBuffer:traceEncoder:]_block_invoke_2
+ ___76-[CaptureMTL4RenderCommandEncoder takeICBSnapshot:rangeBuffer:traceEncoder:]_block_invoke_3
+ ___77-[CaptureMTL4ComputeCommandEncoder takeICBSnapshot:rangeBuffer:traceEncoder:]_block_invoke
+ ___77-[CaptureMTL4ComputeCommandEncoder takeICBSnapshot:rangeBuffer:traceEncoder:]_block_invoke_2
+ ___77-[CaptureMTL4ComputeCommandEncoder takeICBSnapshot:rangeBuffer:traceEncoder:]_block_invoke_3
+ ___94-[CaptureMTLRenderCommandEncoder executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:]_block_invoke_2
+ ___94-[CaptureMTLRenderCommandEncoder executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:]_block_invoke_3
+ ___95-[CaptureMTLComputeCommandEncoder executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:]_block_invoke_2
+ ___95-[CaptureMTLComputeCommandEncoder executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:]_block_invoke_3
+ ___DownloadPresentedDrawable_block_invoke
+ ___GTCorePlatform_isCompositorProcess_block_invoke
+ ___GTMTLCaptureEventBuffer_initializeOnce_block_invoke
+ ___GTMTLCoreSync_signalGPUWithHandler_MTL4_block_invoke
+ ___block_descriptor_33_e5_v8?0l
+ ___block_descriptor_40_e8_32s_e24_v24?0Q8"<MTLBuffer>"16ls32l8
+ ___block_descriptor_40_e8_32s_e40_v32?0"<MTLBuffer>"8Q16"<MTLBuffer>"24ls32l8
+ ___block_descriptor_40_e8_32s_e67_v24?0"<MTLIndirectCommandBuffer>"8"<MTLIndirectCommandBuffer>"16ls32l8
+ ___block_descriptor_48_e8_32s40r_e28_v16?0"<MTLCommandBuffer>"8lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e67_v24?0"<MTLIndirectCommandBuffer>"8"<MTLIndirectCommandBuffer>"16ls32l8r40l8
+ ___block_descriptor_56_8_32s40bs_e29_v24?0"<MTLSharedEvent>"8Q16ls32l8s40l8
+ ___copy_constructor_8_8_s0_s8_s16_t24w24_s48_s56
+ ___destructor_8_s0_s8_s16_s48_s56
+ ___strlcat_chk
+ ___strlcpy_chk
+ __block_descriptor_tmp.15205
+ __block_literal_global.10413
+ __block_literal_global.10911
+ __block_literal_global.11683
+ __block_literal_global.12124
+ __block_literal_global.138
+ __block_literal_global.15066
+ __block_literal_global.15304
+ __block_literal_global.15373
+ __block_literal_global.15387
+ __block_literal_global.1699
+ __block_literal_global.20471
+ __block_literal_global.274
+ __block_literal_global.3046
+ __block_literal_global.363
+ __block_literal_global.369
+ __block_literal_global.4323
+ __block_literal_global.4505
+ __block_literal_global.459
+ __block_literal_global.8092
+ __block_literal_global.8527
+ __block_literal_global.9531
+ _gContext
+ _isatty
+ _objc_msgSend$_signalCompletionHandlers:count:
+ _objc_msgSend$addCompletionHandler:
+ _objc_msgSend$addRangeShapshot4:encodeRangeCopy:
+ _objc_msgSend$addRangeShapshot:offset:encodeRangeCopy:
+ _objc_msgSend$allocateRangeSnapshot
+ _objc_msgSend$arg
+ _objc_msgSend$clearOnBarrier:
+ _objc_msgSend$create:
+ _objc_msgSend$currentState:
+ _objc_msgSend$dispatchWithDevicePipelineState:argumentTable:
+ _objc_msgSend$encodeICBRangeSnapshot:encoder:src:dst:
+ _objc_msgSend$encodeICBSnapshot:encoder:src:dst:
+ _objc_msgSend$finalizeRequest:withData:
+ _objc_msgSend$finalizeRequest:withData:subIndex:
+ _objc_msgSend$finalizeRequest:withICB:descriptor:
+ _objc_msgSend$finalizeRequest:withStore:
+ _objc_msgSend$finalizeRequest:withStore:subIndex:
+ _objc_msgSend$find:
+ _objc_msgSend$funcIndex
+ _objc_msgSend$icbSnapshotResidencySet
+ _objc_msgSend$initWithICB:map:traceEncoder:encodeCopy:
+ _objc_msgSend$isRecordingData
+ _objc_msgSend$placementSparsePageSize
+ _objc_msgSend$popCompletionHandlers
+ _objc_msgSend$rangeArg
+ _objc_msgSend$remove:
+ _objc_msgSend$restoreAfterIcbSnapshot
+ _objc_msgSend$serialize
+ _objc_msgSend$setAccelerationStructureDescriptorProcessEvent:
+ _objc_msgSend$setPlacementSparsePageSize:
+ _objc_msgSend$takeICBSnapshot:rangeBuffer:traceEncoder:
+ _objc_retainAutoreleasedReturnValue
+ initWithBaseObject:captureDevice:.completionHandlerListenerQueue
+ initWithBaseObject:captureDevice:.scheduledListenerQueue
+ name_array.16460
+ newHeapWithDescriptor:.onceToken.272
+ s_accelerationStructureDescriptorDownloaderPipelinesToken.7882
+ s_downloaderPipelines.0.7888
+ s_downloaderPipelines.1.7889
+ s_downloaderPipelines.2.7890
+ s_downloaderPipelines.3.7891
+ s_downloaderPipelines.4.7892
+ waitUntilSignaledValue:timeoutMS:.onceToken.13566
- -[CaptureMTL4PipelineDataSetSerializer .cxx_destruct]
- -[CaptureMTL4PipelineDataSetSerializer baseObject]
- -[CaptureMTL4PipelineDataSetSerializer conformsToProtocol:]
- -[CaptureMTL4PipelineDataSetSerializer dealloc]
- -[CaptureMTL4PipelineDataSetSerializer description]
- -[CaptureMTL4PipelineDataSetSerializer forwardingTargetForSelector:]
- -[CaptureMTL4PipelineDataSetSerializer initWithBaseObject:captureContext:]
- -[CaptureMTL4PipelineDataSetSerializer originalObject]
- -[CaptureMTL4PipelineDataSetSerializer respondsToSelector:]
- -[CaptureMTL4PipelineDataSetSerializer serializeAsArchiveAndFlushToURL:error:]
- -[CaptureMTL4PipelineDataSetSerializer serializeAsPipelinesScriptWithError:]
- -[CaptureMTL4PipelineDataSetSerializer streamReference]
- -[CaptureMTL4PipelineDataSetSerializer touch]
- -[CaptureMTL4PipelineDataSetSerializer traceContext]
- -[CaptureMTL4PipelineDataSetSerializer traceStream]
- -[CaptureMTLTexture updateDrawableStream:]
- -[GTDownloadContext objects]
- -[GTDownloadContext setObjects:]
- /Library/Caches/com.apple.xbs/Binaries/GPUToolsDevice/install/TempContent/Objects/GPUToolsFoundation.build/GPUToolsCapture.build/DerivedSources/
- /Library/Caches/com.apple.xbs/Binaries/GPUToolsDevice/install/TempContent/Objects/GPUToolsFoundation.build/GPUToolsCapture.build/Objects-normal/arm64e/GPUToolsCapture_lto.o
- GCC_except_table126
- GCC_except_table1522
- GCC_except_table1547
- GCC_except_table1652
- GCC_except_table1653
- GCC_except_table1657
- GCC_except_table1658
- GCC_except_table1659
- GCC_except_table1660
- GCC_except_table1661
- GCC_except_table1868
- GCC_except_table1869
- GCC_except_table1871
- GCC_except_table1873
- GCC_except_table2026
- GCC_except_table2062
- GCC_except_table238
- GCC_except_table261
- GCC_except_table262
- GCC_except_table3026
- GCC_except_table317
- GCC_except_table3188
- GCC_except_table3282
- GCC_except_table342
- GCC_except_table4003
- GCC_except_table4544
- GCC_except_table49
- GCC_except_table54
- GCC_except_table62
- GCC_except_table649
- GTAccelerationStructureDescriptorDownloader_processCopy.7892
- GTAccelerationStructureDescriptorDownloader_processRefit.7893
- GTMTLCaptureEventBuffer_add.computePipeline
- GTMTLCaptureEventBuffer_add.onceToken
- GetStream.19755
- IsCompositorProcess.isCompositorProcess
- IsCompositorProcess.onceToken
- OBJC_IVAR_$_CaptureMTL4CommandBuffer._accelerationStructureDescriptorCopyEventValue
- OBJC_IVAR_$_CaptureMTL4CommandQueue._submissionListener
- OBJC_IVAR_$_CaptureMTL4Compiler._capturePipelineDataSetSerializer
- OBJC_IVAR_$_CaptureMTL4PipelineDataSetSerializer._baseObject
- OBJC_IVAR_$_CaptureMTL4PipelineDataSetSerializer._traceContext
- OBJC_IVAR_$_CaptureMTL4PipelineDataSetSerializer._traceStream
- OBJC_IVAR_$_CaptureMTLComputeCommandEncoder._pool
- OBJC_IVAR_$_CaptureMTLRenderCommandEncoder._pool
- OBJC_IVAR_$_CaptureMTLTexture._drawableStream
- RetainObjectForDescriptorDownloader.9495
- StoreMTLCompileOptionsUsingEncode.16287
- _AllocateRangeSnapshotMemory
- _AllocateSnapshotMemory
- _CaptureClearFuncSnapshot
- _CaptureCreateFuncSnapshot
- _CaptureFindFuncSnapshot
- _CaptureRemoveFuncSnapshot
- _ColorSpaceData
- _CommandQueueForCommandBuffer
- _DNA1_BYTES
- _DecodeDYMTL4PipelineDataSetSerializerDescriptor
- _EncodeDYMTL4PipelineDataSetSerializerDescriptor
- _GTEncodeMetalLayers
- _GTMTL4SMArgumentTable_bufferBindingsMatch
- _GTMTL4SMCommandEncoder_init
- _GTMTL4SMCommandEncoder_processTraceFunc
- _GTMTLCaptureEventBuffer_add
- _GTMTLCaptureEventBuffer_getElements
- _GTMTLCoreSync_acquireSignalValue
- _GTMTLCoreSync_event
- _GTMTLCoreSync_init
- _GTMTLCoreSync_waitValue
- _GTResourceDownloaderRequest_markTextureAsDrawable
- _GTTraceContextDumpActiveDevice
- _GTTraceContextDumpUnusedCount
- _GTTraceContext_removeFlags
- _GetExecuteCommandsInBufferArgs
- _MakeMTL4PipelineDataSetSerializerDescriptor
- _OBJC_CLASS_$_CaptureMTL4PipelineDataSetSerializer
- _OBJC_CLASS_$_MTL4PipelineDataSetSerializerDescriptor
- _OBJC_METACLASS_$_CaptureMTL4PipelineDataSetSerializer
- _ProcessResourceAPIs
- _ResidencySetAllocationsContainDrawableTexture
- _ResidencySetHashContainsDrawableTexture
- _RetrieveGPUCaptureTexture
- _SaveMTL4PipelineDataSetSerializerDescriptor
- _TranslateGTMTL4PipelineDataSetSerializerDescriptor
- _UpdateAccess
- _WriteGTMTLSMLayer
- __Block_byref_object_copy_.11592
- __Block_byref_object_copy_.3903
- __Block_byref_object_copy_.4409
- __Block_byref_object_dispose_.11593
- __Block_byref_object_dispose_.3904
- __Block_byref_object_dispose_.4410
- __OBJC_$_INSTANCE_METHODS_CaptureMTL4PipelineDataSetSerializer
- __OBJC_$_INSTANCE_VARIABLES_CaptureMTL4PipelineDataSetSerializer
- __OBJC_$_PROP_LIST_CaptureMTL4PipelineDataSetSerializer
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4PipelineDataSetSerializer
- __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4PipelineDataSetSerializer
- __OBJC_$_PROTOCOL_REFS_MTL4PipelineDataSetSerializer
- __OBJC_CLASS_PROTOCOLS_$_CaptureMTL4PipelineDataSetSerializer
- __OBJC_CLASS_RO_$_CaptureMTL4PipelineDataSetSerializer
- __OBJC_LABEL_PROTOCOL_$_MTL4PipelineDataSetSerializer
- __OBJC_METACLASS_RO_$_CaptureMTL4PipelineDataSetSerializer
- __OBJC_PROTOCOL_$_MTL4PipelineDataSetSerializer
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIxPU18objcproto8NSObject11objc_objectEENS_22__unordered_map_hasherIxS4_NS_4hashIxEENS_8equal_toIxEELb1EEENS_21__unordered_map_equalIxS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE4findIxEENS_15__hash_iteratorIPNS_11__hash_nodeIS4_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIxPU18objcproto8NSObject11objc_objectEENS_22__unordered_map_hasherIxS4_NS_4hashIxEENS_8equal_toIxEELb1EEENS_21__unordered_map_equalIxS4_S9_S7_Lb1EEENS_9allocatorIS4_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIxPU18objcproto8NSObject11objc_objectEENS_22__unordered_map_hasherIxS4_NS_4hashIxEENS_8equal_toIxEELb1EEENS_21__unordered_map_equalIxS4_S9_S7_Lb1EEENS_9allocatorIS4_EEED2Ev
- __ZNSt3__16vectorI16GTTelemetryLayerNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
- __ZNSt3__16vectorI16GTTelemetryQueueNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
- __ZNSt3__16vectorI16GTTelemetryQueueNS_9allocatorIS1_EEE9push_backB8nn200100ERKS1_
- __ZNSt3__16vectorI17GTTelemetryDeviceNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
- __ZSt28__throw_bad_array_new_lengthB8nn200100v
- ___DownloadDrawable_block_invoke
- ___GTMTLCaptureEventBuffer_add_block_invoke
- ___IsCompositorProcess_block_invoke
- ___block_descriptor_56_e8_32s40bs_e29_v24?0"<MTLSharedEvent>"8Q16ls40l8s32l8
- ___block_descriptor_64_e8_32s40s48s_e28_v16?0"<MTLCommandBuffer>"8ls32l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48s56s_e28_v16?0"<MTLCommandBuffer>"8ls32l8s40l8s48l8s56l8
- __block_descriptor_tmp.15017
- __block_literal_global.10321
- __block_literal_global.10826
- __block_literal_global.11596
- __block_literal_global.12045
- __block_literal_global.14930
- __block_literal_global.15115
- __block_literal_global.15182
- __block_literal_global.15195
- __block_literal_global.156
- __block_literal_global.1670
- __block_literal_global.184
- __block_literal_global.20140
- __block_literal_global.2945
- __block_literal_global.359
- __block_literal_global.365
- __block_literal_global.4231
- __block_literal_global.4418
- __block_literal_global.482
- __block_literal_global.7302
- __block_literal_global.8075
- __block_literal_global.8505
- __block_literal_global.9472
- _dna1_length
- _eventBuffer
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$objects
- _objc_msgSend$serializeAsArchiveAndFlushToURL:error:
- _objc_msgSend$serializeAsPipelinesScriptWithError:
- _objc_msgSend$setConfiguration:
- _objc_msgSend$setPipelineDataSetSerializer:
- _objc_msgSend$updateDrawableStream:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x5
- _objc_retain_x7
- initWithBaseObject:captureDevice:.submissionListener
- name_array.16229
- newHeapWithDescriptor:.onceToken.182
- s_accelerationStructureDescriptorDownloaderPipelinesToken.7866
- s_downloaderPipelines.0.7873
- s_downloaderPipelines.1.7874
- s_downloaderPipelines.2.7875
- s_downloaderPipelines.3.7876
- s_downloaderPipelines.4.7877
- waitUntilSignaledValue:timeoutMS:.onceToken.13443
CStrings:
+ " %s %s"
+ " - %32s [%6llu]"
+ " cmdTypes:%x"
+ " cnt:%llu"
+ " dispIdx:%llu"
+ " fnCnt:%llu bufCnt:%llu"
+ " len:%6llu pl:%llu"
+ " len:%8llu off:%8llu"
+ " off:%8llu len:%8llu"
+ " s:%2u l:%2u %ux%ux%u"
+ " unknown"
+ " | %-22s"
+ " | %-9s: %p %s"
+ " | (no func)"
+ " | F%-8llu %s"
+ " | timeout  : %6llu ms%s"
+ "\""
+ "%-10@ | [%-11@] v: %8llu %s%s%s"
+ "%-32s %-11s%s%s"
+ "%-32s %-11s%s%s\n"
+ "%.0f %s"
+ "%.1f %s"
+ "%.2f %s"
+ "%40s [%6llu] | %9s | %s"
+ "%llu %s"
+ "%s%-8s"
+ "%s%llu"
+ "(TIMED OUT!)"
+ "(no label)"
+ ")"
+ ","
+ "/AppleInternal/Library/BuildRoots/4~CH9TugDK7NeNFXlDCJk5oGYOjZm0YEVbHWxHTo4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH9TugDK7NeNFXlDCJk5oGYOjZm0YEVbHWxHTo4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "0xffffc0e9"
+ "0xffffc0ea"
+ "@\"<MTL4ArgumentTable>\""
+ "@\"<MTLAccelerationStructureCommandEncoder>\"32@0:8^(?={?=b8b24IQQ}{?=b8b24IQQ})16Q24"
+ "@\"<MTLAccelerationStructureCommandEncoder>\"40@0:8@\"MTLAccelerationStructurePassDescriptor\"16^(?={?=b8b24IQQ}{?=b8b24IQQ})24Q32"
+ "@\"<MTLBlitCommandEncoder>\"32@0:8^(?={?=b8b24IQQ}{?=b8b24IQQ})16Q24"
+ "@\"<MTLBlitCommandEncoder>\"40@0:8@\"MTLBlitPassDescriptor\"16^(?={?=b8b24IQQ}{?=b8b24IQQ})24Q32"
+ "@\"<MTLIndirectCommandBuffer>\""
+ "@\"<MTLResidencySet>\""
+ "@\"CaptureICBSnapshotMap\""
+ "@\"MTLDeviceFeatureQueries\"16@0:8"
+ "@\"MTLIndirectCommandBufferDescriptor\""
+ "@32@0:8@16^{GTTraceEncoder=^{GTTraceContext}^{GTTraceStream}^{GTTraceFunc}QQCCC[5c]}24"
+ "@40@0:8@16Q24^{GTTraceEncoder=^{GTTraceContext}^{GTTraceStream}^{GTTraceFunc}QQCCC[5c]}32"
+ "@48@0:8@16@24^{GTTraceEncoder=^{GTTraceContext}^{GTTraceStream}^{GTTraceFunc}QQCCC[5c]}32@?40"
+ "C16@0:8"
+ "CU<b>U<b>@3ulul"
+ "CU<b>U<b>@3ululul"
+ "CaptureICBSnapshot"
+ "CaptureICBSnapshotMap"
+ "CmdBuffer"
+ "Completed"
+ "Completion handlers"
+ "Creation"
+ "CttU<b>ul"
+ "Dispatch"
+ "Download CB[%llu] FIdx[%llu]"
+ "Download MTL4Q[%llu] FIdx[%llu]"
+ "Downloader"
+ "Dwl@Wait CB[%llu] FIdx[%llu]"
+ "Event buffer (CPU) index %i: function index %llu"
+ "Event buffer (GPU) index %i: function index %llu"
+ "GiB"
+ "KiB"
+ "MTLCAPTURE_EVENT_BUFFER_ENTRIES_COUNT"
+ "MiB"
+ "Notify"
+ "PiB"
+ "Prep4Serialization"
+ "Queue"
+ "R<-"
+ "Resetting event buffer"
+ "ResourceTracker"
+ "Scheduled"
+ "Serialize"
+ "Signal CPU"
+ "Signal GPU3"
+ "Signal GPU4"
+ "Store"
+ "Sync"
+ "T@\"<MTLSharedEvent>\",&,V_accelerationStructureDescriptorProcessEvent"
+ "T@\"MTLDeviceFeatureQueries\",R"
+ "TC,R,N"
+ "TQ,R,V_accelerationStructureDescriptorProcessEventValue"
+ "TiB"
+ "USE #%-6d"
+ "W->"
+ "Wait   CPU"
+ "Wait   GPU3"
+ "Wait   GPU4"
+ "WaitE  CPU"
+ "[Unknown]"
+ "^{CaptureFuncSnapshot=Q^{GTTraceMemHeader}Q}"
+ "^{CaptureFuncSnapshot=Q^{GTTraceMemHeader}Q}24@0:8@16"
+ "^{GTMTLCoreSync=}"
+ "^{GTTraceEncoder=^{GTTraceContext}^{GTTraceStream}^{GTTraceFunc}QQCCC[5c]}"
+ "^{GTTraceMemHeader=QCCSI}"
+ "^{TextureViewSlot={MTLResourceID=Q}b63b1(?={?=QQ{GTMTLTextureDescriptor=QQIIISSSSSCCCCCCCCCCCCCC[4C]}}{?=B[7c]{GTMTLTextureViewDescriptor={GTRange=QQ}{GTRange=QQ}ISC[1C]}})}"
+ "_accelerationStructureDescriptorProcessEventValue"
+ "_completionHandlerSync"
+ "_completionHandlers"
+ "_desc"
+ "_deviceUserArgumentTable"
+ "_deviceUserState"
+ "_icbCopy"
+ "_icbOriginal"
+ "_icbSnapshotMap"
+ "_icbSnapshotResidencySet"
+ "_isRecordingData"
+ "_map"
+ "_rangeCopy"
+ "_rangeMem"
+ "_signalCompletionHandlers:count:"
+ "_snapshot"
+ "_traceEncoder"
+ "addCompletionHandler:"
+ "addRangeShapshot4:encodeRangeCopy:"
+ "addRangeShapshot:offset:encodeRangeCopy:"
+ "allocateRangeSnapshot"
+ "arg"
+ "byte"
+ "clearOnBarrier:"
+ "com.apple.gputools.CaptureMTL4CommandBufferCompletionHandlers"
+ "com.apple.gputools.EventBuffer"
+ "com.apple.gputools.EventBuffer.CPUOrder"
+ "com.apple.gputools.EventBuffer.GPUOrder"
+ "com.apple.gputools.EventBuffer.mtl3-i%u-f%llu"
+ "com.apple.gputools.EventBuffer.mtl4-i%u-f%llu"
+ "create:"
+ "currentState:"
+ "d:"
+ "dispatchWithDevicePipelineState:argumentTable:"
+ "drawable"
+ "drawables"
+ "encodeICBRangeSnapshot:encoder:src:dst:"
+ "encodeICBSnapshot:encoder:src:dst:"
+ "fail: Failed to create argument table for ICB snaphshot: %s"
+ "fail: Failed to create argument table for ICB snapshot: %s"
+ "fail: Failed to create residency set for ICB snapshot: %s"
+ "fail: GTMTLCaptureEventBuffer - Failed creating the CPU event buffer"
+ "fail: GTMTLCaptureEventBuffer - Failed creating the GPU event buffer"
+ "fail: GTMTLCaptureEventBuffer - Failed creating the argument table: %s"
+ "fail: GTMTLCaptureEventBuffer - Failed creating the residency set: %s"
+ "fail: GTMTLCaptureEventBuffer - event buffer overflow (capacity %llu). Stopping event recording."
+ "featureQueries"
+ "finalizeRequest:withData:"
+ "finalizeRequest:withData:subIndex:"
+ "finalizeRequest:withICB:descriptor:"
+ "finalizeRequest:withStore:"
+ "finalizeRequest:withStore:subIndex:"
+ "find:"
+ "fragmentGlobalConstantsBase"
+ "fragmentGlobalConstantsSize"
+ "funcIndex"
+ "globalConstantsBase"
+ "globalConstantsSize"
+ "icbSnapshotResidencySet"
+ "initWithICB:map:traceEncoder:encodeCopy:"
+ "isRecordingData"
+ "is_compositor"
+ "kDYFEMTLAccelerationStructure_rebuildMTLAccelerationStructure"
+ "meshGlobalConstantsBase"
+ "meshGlobalConstantsSize"
+ "o:("
+ "objectGlobalConstantsBase"
+ "objectGlobalConstantsSize"
+ "placementSparsePageSize"
+ "popCompletionHandlers"
+ "rangeArg"
+ "remove:"
+ "restoreAfterIcbSnapshot"
+ "sampledAccelerationStructureCommandEncoder:capacity:"
+ "sampledAccelerationStructureCommandEncoderWithDescriptor:programInfoBuffer:capacity:"
+ "sampledBlitCommandEncoder:capacity:"
+ "sampledBlitCommandEncoderWithDescriptor:programInfoBuffer:capacity:"
+ "serialize"
+ "setAccelerationStructureDescriptorProcessEvent:"
+ "setFragmentGlobalConstantsBase:"
+ "setFragmentGlobalConstantsSize:"
+ "setGlobalConstantsBase:"
+ "setGlobalConstantsSize:"
+ "setMeshGlobalConstantsBase:"
+ "setMeshGlobalConstantsSize:"
+ "setObjectGlobalConstantsBase:"
+ "setObjectGlobalConstantsSize:"
+ "setPlacementSparsePageSize:"
+ "setTileGlobalConstantsBase:"
+ "setTileGlobalConstantsSize:"
+ "setVertexGlobalConstantsBase:"
+ "setVertexGlobalConstantsSize:"
+ "supportsPlacementSparse"
+ "takeICBSnapshot:rangeBuffer:traceEncoder:"
+ "takeICBSnapshot:traceEncoder:"
+ "tileGlobalConstantsBase"
+ "tileGlobalConstantsSize"
+ "usedDrawableMap"
+ "v24@?0@\"<MTLIndirectCommandBuffer>\"8@\"<MTLIndirectCommandBuffer>\"16"
+ "v24@?0Q8@\"<MTLBuffer>\"16"
+ "v32@0:8r^{GTResourceDownloaderRequest=QQQQQISCb1b1b1b5(?={?=QQ}{?={GTMTLTensorSlice={GTMTLTensorExtents=Q[16Q]}{GTMTLTensorExtents=Q[16Q]}}{GTMTLTensorExtents=Q[16Q]}}{?=SS{?={?=ISS}{?=ISS}}IIISS[4c]}{?=QQ}{?={GTMTLIndirectCommandBufferDescriptor=QQSCCCCCCCCCCCCCCCCCCCCCCCCC[5C]}}{?=Q}{?=Q}{?=QQ})}16@24"
+ "v32@?0@\"<MTLBuffer>\"8Q16@\"<MTLBuffer>\"24"
+ "v36@0:8r^{GTResourceDownloaderRequest=QQQQQISCb1b1b1b5(?={?=QQ}{?={GTMTLTensorSlice={GTMTLTensorExtents=Q[16Q]}{GTMTLTensorExtents=Q[16Q]}}{GTMTLTensorExtents=Q[16Q]}}{?=SS{?={?=ISS}{?=ISS}}IIISS[4c]}{?=QQ}{?={GTMTLIndirectCommandBufferDescriptor=QQSCCCCCCCCCCCCCCCCCCCCCCCCC[5C]}}{?=Q}{?=Q}{?=QQ})}16@24I32"
+ "v40@0:8r^{GTResourceDownloaderRequest=QQQQQISCb1b1b1b5(?={?=QQ}{?={GTMTLTensorSlice={GTMTLTensorExtents=Q[16Q]}{GTMTLTensorExtents=Q[16Q]}}{GTMTLTensorExtents=Q[16Q]}}{?=SS{?={?=ISS}{?=ISS}}IIISS[4c]}{?=QQ}{?={GTMTLIndirectCommandBufferDescriptor=QQSCCCCCCCCCCCCCCCCCCCCCCCCC[5C]}}{?=Q}{?=Q}{?=QQ})}16@24@32"
+ "v48@0:8@16@24@32@40"
+ "vertexGlobalConstantsBase"
+ "vertexGlobalConstantsSize"
+ "x"
+ "{GTMTLSMCommandEncoder={GTMTLSMObject=IIQQQ^{GTMTLSMObject}}Q*(?=(?={GTMTLSMRenderCommandEncoder=^{GTMTLRenderPassDescriptor}[1Q][1Q](?={?=[31Q][31Q]}{?=[31Q][31Q]})[31Q][128Q][16Q][1Q](?={?=[31Q][31Q]}{?=[31Q][31Q]})[128Q][16Q][1Q](?={?=[31Q][31Q]}{?=[31Q][31Q]})[128Q][16Q][1Q](?={?=[31Q][31Q]}{?=[31Q][31Q]})[128Q][16Q][1Q](?={?=[31Q][31Q]}{?=[31Q][31Q]})[128Q][16Q]QQ[16{GTMTLViewport=dddddd}]Q[16{GTMTLScissorRect=QQQQ}]Q^{GTMTLVertexAmplificationViewMapping}Q[8Q][8Q]{GTMTLLogicalToPhysicalColorAttachmentMap=[8C]}fffff[4f]II[16f][16f][16f][16f][16f][16f][16f][16f][16f][16f]ffIII[31I][31I][31I]IIICCCCCCCCCCC[5c]}{?=^{GTMTLComputePassDescriptor}Q[1Q][1Q](?={?=[31Q][31Q]}{?=[31Q][31Q]})[31Q][128Q][16Q]{?={?=QQQ}{?=QQQ}}Q[31I]III[16f][16f]C[7c]}{?=Q}{?=^{GTMTLBlitPassDescriptor}}{GTMTLSMParallelCommandEncoder=^{GTMTLRenderPassDescriptor}[8Q][8Q]CCCC[4c]}{?=^{GTMTLResourceStatePassDescriptor}}{?=^{GTMTLAccelerationStructurePassDescriptor}})(?={GTMTL4SMRenderCommandEncoder=^{GTMTL4RenderPassDescriptor}[5Q]{?=[31Q][31Q][31Q][31Q][31Q][31Q][31Q][31Q][31Q][31Q]}QQQ[16{GTMTLViewport=dddddd}]Q[16{GTMTLScissorRect=QQQQ}]Q^{GTMTLVertexAmplificationViewMapping}[8Q]{GTMTLLogicalToPhysicalColorAttachmentMap=[8C]}fff[4f]IIf[31I][31I][31I]IICCCCCCC[5C]}{GTMTL4SMComputeCommandEncoder=QQ{?=[31Q][31Q]}[31I]II[4c]}{GTMTL4SMMachineLearningCommandEncoder=QQ}))}24@0:8^{apr_pool_t=}16"
- "\t1"
- "@\"<MTL4PipelineDataSetSerializer>\""
- "@\"CaptureMTL4PipelineDataSetSerializer\""
- "@\"NSData\"24@0:8^@16"
- "@24@0:8^@16"
- "CaptureMTL4PipelineDataSetSerializer"
- "Metal 4 Harvesting Data Set"
- "Metal 4 Render Command Encoder"
- "Metal4 Sparse Buffers"
- "Metal4 Sparse Textures"
- "T@\"NSMutableArray\",&,N,V_objects"
- "TQ,R,V_accelerationStructureDescriptorCopyEventValue"
- "^{TextureViewSlot={MTLResourceID=Q}b63b1(?={?=QQ{GTMTLTextureDescriptor=QQIIISSSSSCCCCCCCCCCCCC[5C]}}{?=B[7c]{GTMTLTextureViewDescriptor={GTRange=QQ}{GTRange=QQ}ISC[1C]}})}"
- "_capturePipelineDataSetSerializer"
- "_drawableStream"
- "_submissionListener"
- "kDYFEMTLCommandBuffer_computeCommandEncoderWithParallelExecution"
- "kDYFEMTLComputeCommandEncoder_dispatchBarrier"
- "objects"
- "serializeAsArchiveAndFlushToURL:error:"
- "serializeAsPipelinesScriptWithError:"
- "setConfiguration:"
- "setObjects:"
- "setPipelineDataSetSerializer:"
- "updateDrawableStream:"
- "v24@0:8^{GTTraceStream=}16"
- "{GTMTLCoreSync=\"event\"@\"<MTLSharedEvent>\"\"nextSignal\"AQ}"

```
