## GPUToolsCapture

> `/System/Library/PrivateFrameworks/GPUToolsCapture.framework/GPUToolsCapture`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__interpose`
- `__DATA.__thread_vars`

```diff

-2027.1.3.0.0
-  __TEXT.__text: 0x291f04
-  __TEXT.__auth_stubs: 0x1920
-  __TEXT.__objc_stubs: 0x18660
+2027.2.4.0.0
+  __TEXT.__text: 0x290678
+  __TEXT.__auth_stubs: 0x18f0
+  __TEXT.__objc_stubs: 0x185a0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x1363c
-  __TEXT.__const: 0xa0a0
-  __TEXT.__cstring: 0x30a32
-  __TEXT.__oslogstring: 0x251a
-  __TEXT.__gcc_except_tab: 0x1634
-  __TEXT.__objc_methname: 0x1bb44
-  __TEXT.__objc_classname: 0x15da
-  __TEXT.__objc_methtype: 0xafc9
+  __TEXT.__objc_methlist: 0x137c4
+  __TEXT.__const: 0xa1a0
+  __TEXT.__cstring: 0x30692
+  __TEXT.__oslogstring: 0x243f
+  __TEXT.__gcc_except_tab: 0x16d0
+  __TEXT.__objc_methname: 0x1bb54
+  __TEXT.__objc_classname: 0x1601
+  __TEXT.__objc_methtype: 0xb07d
   __TEXT.__ustring: 0x20a
-  __TEXT.__unwind_info: 0x8240
-  __DATA_CONST.__const: 0x21d8
-  __DATA_CONST.__cfstring: 0x49c0
-  __DATA_CONST.__objc_classlist: 0x358
+  __TEXT.__unwind_info: 0x7f08
+  __DATA_CONST.__const: 0x21e0
+  __DATA_CONST.__cfstring: 0x43a0
+  __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x430
+  __DATA_CONST.__objc_protolist: 0x438
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__objc_superrefs: 0x330
-  __DATA_CONST.__objc_intobj: 0xd8
-  __DATA_CONST.__objc_arraydata: 0x90
-  __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0xca8
-  __DATA_CONST.__got: 0x868
-  __DATA_CONST.__auth_ptr: 0x50
+  __DATA_CONST.__objc_superrefs: 0x338
+  __DATA_CONST.__objc_intobj: 0x90
+  __DATA_CONST.__objc_arraydata: 0x60
+  __DATA_CONST.__objc_dictobj: 0x78
+  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__auth_got: 0xc90
+  __DATA_CONST.__got: 0x850
+  __DATA_CONST.__auth_ptr: 0x58
   __AUTH_CONST.__interpose: 0x50
-  __DATA.__objc_const: 0x1b658
-  __DATA.__objc_selrefs: 0x70d8
-  __DATA.__objc_ivar: 0xbb0
-  __DATA.__objc_data: 0x2170
-  __DATA.__data: 0x3530
+  __DATA.__objc_const: 0x1b908
+  __DATA.__objc_selrefs: 0x7098
+  __DATA.__objc_ivar: 0xbc8
+  __DATA.__objc_data: 0x21c0
+  __DATA.__data: 0x3598
   __DATA.__thread_vars: 0x48
   __DATA.__thread_bss: 0x201010
-  __DATA.__common: 0x7d
+  __DATA.__common: 0x5
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 9854
-  Symbols:   16278
-  CStrings:  9463
+  Functions: 9595
+  Symbols:   16026
+  CStrings:  9430
 
Symbols:
+ -[CaptureMTL4CommandBuffer resolveCounterHeap:withRange:intoBuffer:atOffset:waitFence:updateFence:]
+ -[CaptureMTL4CommandBuffer writeTimestampIntoHeap:atIndex:]
+ -[CaptureMTL4CommandQueue _postCommit:count:captured:]
+ -[CaptureMTL4CommandQueue _signalCompletionHandlers:count:captured:]
+ -[CaptureMTL4ComputeCommandEncoder writeTimestampWithGranularity:intoHeap:atIndex:]
+ -[CaptureMTL4CounterHeap .cxx_destruct]
+ -[CaptureMTL4CounterHeap baseObject]
+ -[CaptureMTL4CounterHeap conformsToProtocol:]
+ -[CaptureMTL4CounterHeap count]
+ -[CaptureMTL4CounterHeap dealloc]
+ -[CaptureMTL4CounterHeap description]
+ -[CaptureMTL4CounterHeap forwardingTargetForSelector:]
+ -[CaptureMTL4CounterHeap initWithBaseObject:captureContext:]
+ -[CaptureMTL4CounterHeap invalidateCounterRange:]
+ -[CaptureMTL4CounterHeap label]
+ -[CaptureMTL4CounterHeap originalObject]
+ -[CaptureMTL4CounterHeap resolveCounterRange:]
+ -[CaptureMTL4CounterHeap respondsToSelector:]
+ -[CaptureMTL4CounterHeap setLabel:]
+ -[CaptureMTL4CounterHeap streamReference]
+ -[CaptureMTL4CounterHeap touch]
+ -[CaptureMTL4CounterHeap traceContext]
+ -[CaptureMTL4CounterHeap traceStream]
+ -[CaptureMTL4CounterHeap type]
+ -[CaptureMTL4RenderCommandEncoder writeTimestampWithGranularity:afterStage:intoHeap:atIndex:]
+ -[CaptureMTLDevice newCounterHeapWithDescriptor:error:]
+ -[GTDownloadGPUBuffer getScalesPlaneTensorAlias:dataPlaneOffset:]
+ GCC_except_table1335
+ GCC_except_table1368
+ GCC_except_table1375
+ GCC_except_table141
+ GCC_except_table1571
+ GCC_except_table1594
+ GCC_except_table1678
+ GCC_except_table1679
+ GCC_except_table1683
+ GCC_except_table1684
+ GCC_except_table1685
+ GCC_except_table1686
+ GCC_except_table1687
+ GCC_except_table2089
+ GCC_except_table2211
+ GCC_except_table2212
+ GCC_except_table2213
+ GCC_except_table2214
+ GCC_except_table2215
+ GCC_except_table2216
+ GCC_except_table2242
+ GCC_except_table2398
+ GCC_except_table253
+ GCC_except_table275
+ GCC_except_table276
+ GCC_except_table2844
+ GCC_except_table2852
+ GCC_except_table3125
+ GCC_except_table3132
+ GCC_except_table3141
+ GCC_except_table3228
+ GCC_except_table331
+ GCC_except_table3356
+ GCC_except_table356
+ GCC_except_table3972
+ GCC_except_table4149
+ GCC_except_table4150
+ GCC_except_table4151
+ GCC_except_table4152
+ GCC_except_table4153
+ GCC_except_table4155
+ GCC_except_table4157
+ GCC_except_table4159
+ GCC_except_table4161
+ GCC_except_table4162
+ GCC_except_table4163
+ GCC_except_table4164
+ GCC_except_table4165
+ GCC_except_table4335
+ GCC_except_table4336
+ GCC_except_table4337
+ GCC_except_table4338
+ GCC_except_table4339
+ GCC_except_table4340
+ GCC_except_table49
+ GCC_except_table590
+ GCC_except_table64
+ GCC_except_table69
+ GCC_except_table77
+ _ApplyMTL4ColorAttachmentSpecialization
+ _BindingIsInitialized
+ _CompareArgumentTableUse
+ _DYTraceDecode_MTL4CommandBuffer_resolveCounterHeap_withRange_intoBuffer_atOffset_waitFence_updateFence
+ _DYTraceDecode_MTL4CommandBuffer_resolveCounterHeap_withRange_intoBuffer_waitFence_updateFence
+ _DYTraceDecode_MTL4CommandBuffer_writeTimestampIntoHeap_atIndex
+ _DYTraceDecode_MTL4Compiler_newRenderPipelineStateBySpecializationWithDescriptor_pipeline_completionHandler
+ _DYTraceDecode_MTL4Compiler_newRenderPipelineStateBySpecializationWithDescriptor_pipeline_error
+ _DYTraceDecode_MTL4ComputeCommandEncoder_writeTimestampWithGranularity_intoHeap_atIndex
+ _DYTraceDecode_MTL4CounterHeap_dealloc
+ _DYTraceDecode_MTL4CounterHeap_invalidateCounterRange
+ _DYTraceDecode_MTL4CounterHeap_resolveCounterRange
+ _DYTraceDecode_MTL4CounterHeap_setLabel
+ _DYTraceDecode_MTL4RenderCommandEncoder_writeTimestampWithGranularity_afterStage_intoHeap_atIndex
+ _DYTraceDecode_MTLDevice_newCounterHeapWithDescriptor_error
+ _DYTraceEncode_MTL4CommandBuffer_resolveCounterHeap_withRange_intoBuffer_atOffset_waitFence_updateFence
+ _DYTraceEncode_MTL4CommandBuffer_resolveCounterHeap_withRange_intoBuffer_waitFence_updateFence
+ _DYTraceEncode_MTL4CommandBuffer_writeTimestampIntoHeap_atIndex
+ _DYTraceEncode_MTL4Compiler_newRenderPipelineStateBySpecializationWithDescriptor_pipeline_completionHandler
+ _DYTraceEncode_MTL4Compiler_newRenderPipelineStateBySpecializationWithDescriptor_pipeline_error
+ _DYTraceEncode_MTL4ComputeCommandEncoder_writeTimestampWithGranularity_intoHeap_atIndex
+ _DYTraceEncode_MTL4CounterHeap_dealloc
+ _DYTraceEncode_MTL4CounterHeap_invalidateCounterRange
+ _DYTraceEncode_MTL4CounterHeap_resolveCounterRange
+ _DYTraceEncode_MTL4CounterHeap_setLabel
+ _DYTraceEncode_MTL4RenderCommandEncoder_writeTimestampWithGranularity_afterStage_intoHeap_atIndex
+ _DYTraceEncode_MTLDevice_newCounterHeapWithDescriptor_error
+ _DecodeDYMTL4CounterHeapDescriptor
+ _EncodeDYMTL4CounterHeapDescriptor
+ _GTCaptureArchive_openSeparateFile
+ _GTSMMTL4CounterHeap_init
+ _GTSMMTL4CounterHeap_processTraceFuncWithMap
+ _GTSMMTL4CounterHeap_processTraceFuncWithPool
+ _GTSMMTLBuilder_mtl4CounterHeap
+ _GTSMMTLContext_getMTL4CounterHeap
+ _GTSMMTLContext_getMTL4CounterHeaps
+ _GTTraceContext_cleanup
+ _MTLTensor_deviceSupportsMultiPlaneTensors
+ _MakeMTL4CounterHeapDescriptor
+ _MakeScratchTensorDescriptor
+ _NeedsBindingUpdate
+ _OBJC_CLASS_$_CaptureMTL4CounterHeap
+ _OBJC_CLASS_$_MTL4CounterHeapDescriptor
+ _OBJC_IVAR_$_CaptureMTL4CounterHeap._baseObject
+ _OBJC_IVAR_$_CaptureMTL4CounterHeap._traceContext
+ _OBJC_IVAR_$_CaptureMTL4CounterHeap._traceStream
+ _OBJC_IVAR_$_CaptureMTLTextureViewPool._nextLivePool
+ _OBJC_IVAR_$_CaptureMTLTextureViewPool._prevLivePool
+ _OBJC_IVAR_$_CaptureMTLTextureViewPool._resourceViewCount
+ _OBJC_IVAR_$_CaptureMTLTextureViewPool._snapshotGeneration
+ _OBJC_METACLASS_$_CaptureMTL4CounterHeap
+ _ProcessTensorRequest.onceToken
+ _ResolveMTL4ColorAttachmentDefaults
+ _StoreMTL4CounterHeapDescriptorUsingEncode
+ _TextureViewPoolEnsureSnapshot
+ _TranslateGTMTL4CounterHeapDescriptor
+ __OBJC_$_INSTANCE_METHODS_CaptureMTL4CounterHeap
+ __OBJC_$_INSTANCE_VARIABLES_CaptureMTL4CounterHeap
+ __OBJC_$_PROP_LIST_CaptureMTL4CounterHeap
+ __OBJC_$_PROP_LIST_MTL4CounterHeap
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTL4CounterHeap
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTL4CounterHeap
+ __OBJC_$_PROTOCOL_REFS_MTL4CounterHeap
+ __OBJC_CLASS_PROTOCOLS_$_CaptureMTL4CounterHeap
+ __OBJC_CLASS_RO_$_CaptureMTL4CounterHeap
+ __OBJC_LABEL_PROTOCOL_$_MTL4CounterHeap
+ __OBJC_METACLASS_RO_$_CaptureMTL4CounterHeap
+ __OBJC_PROTOCOL_$_MTL4CounterHeap
+ ___68-[CaptureMTL4CommandQueue _signalCompletionHandlers:count:captured:]_block_invoke
+ ___ProcessTensorRequest_block_invoke
+ ___block_descriptor_32_e349_v16?0r^{GTResourceDownloaderRequest=QQQQQISCb1b1b1b1b4(?={?=QQ}{?={GTMTLTensorSlice={GTMTLTensorExtents=Q[16Q]}{GTMTLTensorExtents=Q[16Q]}}{GTMTLTensorExtents=Q[16Q]}C[7c]}{?=SS{?={?=ISS}{?=ISS}}IIISS[4c]}{?=QQ}{?={GTMTLIndirectCommandBufferDescriptor=QQSCCCCCCCCCCCCCCCCCCCCCCCCC[5C]}}{?=QQ}{?=Q}{?=QQ}{?=QQ{GTRange=QQ}{GTRange=QQ}}{GTRange=QQ})}8l
+ ___block_descriptor_40_e349_v16?0r^{GTResourceDownloaderRequest=QQQQQISCb1b1b1b1b4(?={?=QQ}{?={GTMTLTensorSlice={GTMTLTensorExtents=Q[16Q]}{GTMTLTensorExtents=Q[16Q]}}{GTMTLTensorExtents=Q[16Q]}C[7c]}{?=SS{?={?=ISS}{?=ISS}}IIISS[4c]}{?=QQ}{?={GTMTLIndirectCommandBufferDescriptor=QQSCCCCCCCCCCCCCCCCCCCCCCCCC[5C]}}{?=QQ}{?=Q}{?=QQ}{?=QQ{GTRange=QQ}{GTRange=QQ}}{GTRange=QQ})}8l
+ ___block_descriptor_49_e8_32s40s_e29_v24?0"<MTLSharedEvent>"8Q16ls32l8s40l8
+ ___block_descriptor_56_8_32s40s48bs_e29_v24?0"<MTLSharedEvent>"8Q16ls32l8s40l8s48l8
+ _g_captureGeneration
+ _g_captureInProgress
+ _g_livePools
+ _g_livePoolsLock
+ _objc_msgSend$_postCommit:count:captured:
+ _objc_msgSend$_signalCompletionHandlers:count:captured:
+ _objc_msgSend$getScalesPlaneTensorAlias:dataPlaneOffset:
+ _objc_msgSend$invalidateCounterRange:
+ _objc_msgSend$newCounterHeapWithDescriptor:error:
+ _objc_msgSend$resolveCounterHeap:withRange:intoBuffer:atOffset:waitFence:updateFence:
+ _objc_msgSend$setCount:
+ _objc_msgSend$supportsMultiPlaneTensors
+ _objc_msgSend$writeTimestampIntoHeap:atIndex:
+ _objc_msgSend$writeTimestampWithGranularity:afterStage:intoHeap:atIndex:
+ _objc_msgSend$writeTimestampWithGranularity:intoHeap:atIndex:
+ _objc_retain_x10
+ _openat
- 
- -[CaptureMTL4CommandQueue _postCommit:count:]
- -[CaptureMTL4CommandQueue _signalCompletionHandlers:count:]
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/GPUToolsDevice/install/TempContent/Objects/GPUToolsFoundation.build/GPUToolsCapture.build/DerivedSources/
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/GPUToolsDevice/install/TempContent/Objects/GPUToolsFoundation.build/GPUToolsCapture.build/Objects-normal/arm64e/GPUToolsCapture_lto.o
- GCC_except_table1412
- GCC_except_table1445
- GCC_except_table153
- GCC_except_table1650
- GCC_except_table1675
- GCC_except_table1761
- GCC_except_table1762
- GCC_except_table1766
- GCC_except_table1767
- GCC_except_table1768
- GCC_except_table1769
- GCC_except_table1770
- GCC_except_table2012
- GCC_except_table2181
- GCC_except_table2226
- GCC_except_table2348
- GCC_except_table2349
- GCC_except_table2350
- GCC_except_table2351
- GCC_except_table2352
- GCC_except_table2353
- GCC_except_table2379
- GCC_except_table265
- GCC_except_table288
- GCC_except_table289
- GCC_except_table3063
- GCC_except_table3071
- GCC_except_table3209
- GCC_except_table3360
- GCC_except_table3367
- GCC_except_table3376
- GCC_except_table344
- GCC_except_table3479
- GCC_except_table3607
- GCC_except_table369
- GCC_except_table4233
- GCC_except_table4408
- GCC_except_table4409
- GCC_except_table4410
- GCC_except_table4411
- GCC_except_table4412
- GCC_except_table4414
- GCC_except_table4416
- GCC_except_table4418
- GCC_except_table4420
- GCC_except_table4421
- GCC_except_table4422
- GCC_except_table4423
- GCC_except_table4424
- GCC_except_table4595
- GCC_except_table4596
- GCC_except_table4597
- GCC_except_table4598
- GCC_except_table4599
- GCC_except_table4600
- GCC_except_table4871
- GCC_except_table61
- GCC_except_table632
- GCC_except_table681
- GCC_except_table76
- GCC_except_table81
- GCC_except_table89
- GPUToolsCapture_vers.c
- _BufferByStreamRef
- _CFArrayCreate
- _CaptureAGXInit
- _CaptureAGXProcessCompletedCommandBuffer
- _CaptureATF
- _CaptureAccelerationStructures
- _CaptureCA
- _CaptureCP
- _CaptureCP_SetLateFrameMonitoring
- _CaptureConformsToProtocol
- _CaptureGL
- _CaptureInterposerInit
- _CaptureMTLDeviceStoreMetadata
- _CaptureMTLFX
- _CaptureMTLHeap_registerBackbuffer
- _CaptureMTLIOCommandBuffer_recordBlockStart
- _CaptureMTLInit
- _CaptureNSHMDInit
- _CaptureServiceInit
- _CaptureXR
- _CopyGTMTLTextureDescriptor
- _CopyGTMTLTextureViewDescriptor
- _DYCreateTransportC
- _DYCreateTransportSocket
- _DYErrorDomain
- _DYMTLDispatchComputeCommandEncoder
- _DYMTLDrawRenderCommandEncoder
- _DYTraceDecode_MTL4FXTemporalScaler_executionMode
- _DYTraceEncode_MTL4FXTemporalScaler_executionMode
- _DY_TRANSPORT_ENCODED_MESSAGE_MAGIC
- _DaemonCreateGuestAppTransport
- _DaemonDeviceCapabilities
- _DownloadAccelerationStructure
- _DownloadHeap
- _DownloadTensor
- _FillCaptureDescriptor
- _FindDesktopReplayerPath
- _FindMetalLayerWithAddress
- _GPUToolsVersionQuery
- _GTAccelerationStructureDescriptorDownloader_MTL4_destroy
- _GTAccelerationStructureDescriptorDownloader_MTL4_make
- _GTAccelerationStructureDescriptorDownloader_MTL4_postProcess
- _GTAccelerationStructureDescriptorDownloader_MTL4_processBuild
- _GTAccelerationStructureDescriptorDownloader_MTL4_processEndEncoding
- _GTAccelerationStructureDescriptorDownloader_allocateStateBuffers
- _GTAccelerationStructureDescriptorDownloader_children
- _GTAccelerationStructureDescriptorDownloader_destroy
- _GTAccelerationStructureDescriptorDownloader_logDescriptor
- _GTAccelerationStructureDescriptorDownloader_make
- _GTAccelerationStructureDescriptorDownloader_needsDownloader
- _GTAccelerationStructureDescriptorDownloader_postProcess
- _GTAccelerationStructureDescriptorDownloader_preProcessFunc
- _GTAccelerationStructureDescriptorDownloader_processFunc
- _GTAccelerationStructureDescriptorDownloader_suballocate_common
- _GTAddActiveMetalLayers
- _GTCaptureArchive_confinedSeparateFilePath
- _GTCaptureBoundaryCondition_equals
- _GTCaptureBoundaryTracker_commandBufferHandlerBegin
- _GTCaptureBoundaryTracker_commandBufferHandlerEnd
- _GTCaptureBoundaryTracker_currentPhase
- _GTCaptureBoundaryTracker_currentPhaseID
- _GTCaptureBoundaryTracker_destroy
- _GTCaptureBoundaryTracker_init
- _GTCaptureBoundaryTracker_isCaptureActive
- _GTCaptureBoundaryTracker_isCaptureMetalFXHistory
- _GTCaptureBoundaryTracker_isCaptureRecordingData
- _GTCaptureBoundaryTracker_isInitialized
- _GTCaptureObjectTypeAsString
- _GTCapturePhase_addCondition
- _GTCapturePhase_checkTrigger
- _GTCapturePhase_copyConditionsWithTriggerType
- _GTCapturePhase_countConditionsWithHitCount
- _GTCapturePhase_create
- _GTCapturePhase_createGroup
- _GTCapturePhase_findCondition
- _GTCapturePhase_findConditionWithTriggerType
- _GTCapturePhase_forEachCondition
- _GTCapturePhase_getCondition
- _GTCapturePhase_getRootGroup
- _GTCapturePhase_isComplete
- _GTCapturePhase_numConditions
- _GTCapturePhase_removeAllConditions
- _GTCapturePhase_resetHitCount
- _GTCapturePhase_setRootGroup
- _GTCapturePhase_setRootGroupLogicalOperator
- _GTCaptureTriggerTypeAsString
- _GTCaptureWithKeyPressInit
- _GTConditionGroup_addCondition
- _GTConditionGroup_addSubgroup
- _GTConditionLogicOperatorAsString
- _GTEncodeInterfaceOrientation
- _GTEncodeNSHMDMetalSessions
- _GTEventTracker_isBlocked
- _GTEventTracker_isValueSignaled
- _GTEventTracker_logBlockedQueues
- _GTEventTracker_logEvents
- _GTEventTracker_makeFrom
- _GTEventTracker_signalEventValue
- _GTEventTracker_unblock
- _GTEventTracker_wasWaitSignaled
- _GTMTLCaptureEnvironment_init
- _GTMTLCaptureEventBuffer_getGPUExecutionOrder
- _GTMTLCaptureEventBuffer_hasOverflowed
- _GTMTLCaptureEventBuffer_recordGPUEvent_MTLIO
- _GTMTLCaptureEventBuffer_reset
- _GTMTLCaptureManager_abortActiveCapture
- _GTMTLCaptureManager_activateCaptureWithDescriptor
- _GTMTLCaptureManager_activeCaptureState
- _GTMTLCaptureManager_advanceToNextFrame
- _GTMTLCaptureManager_dumpDeviceFilesLocal
- _GTMTLCaptureManager_init
- _GTMTLCaptureManager_notifyUnsupportedFenum
- _GTMTLCaptureManager_preCaptureTakeSnapshots
- _GTMTLCaptureManager_signalCaptureTrigger
- _GTMTLCaptureManager_startCapture
- _GTMTLCaptureManager_stopActiveCapture
- _GTMTLCaptureManager_supportsRemoteCapture
- _GTMTLCaptureManager_updateCaptureDescriptorFromHost
- _GTMTLCaptureManager_waitForCaptureTrigger
- _GTMTLCaptureSparsePageTables_enumeratePlacementSparseHeaps
- _GTMTLCaptureStatistics_begin
- _GTMTLCaptureStatistics_end
- _GTMTLCaptureStatistics_stats
- _GTMTLCaptureStatistics_trackCommit
- _GTMTLCaptureStatistics_trackGPUData
- _GTMTLCaptureStatistics_trackGPUDataDownloaded
- _GTMTLCaptureStatistics_trackPresent
- _GTMTLCaptureStatistics_trackResources
- _GTMTLCaptureStatistics_trackResourcesDownloaded
- _GTMTLCapture_shouldICBSnapshotInsertRenderMemoryBarrier
- _GTMTLCapture_streamNSArrayScratch
- _GTMTLDecodeIndirectCommandBufferInternal
- _GTMTLDispatchUnrolledICB_MTL4Compute
- _GTMTLDispatchUnrolledICB_MTL4Render
- _GTMTLEncodeIndirectBufferBindings
- _GTMTLEncodeIndirectCommandBufferWithRange
- _GTMTLGuestAppClientAddMTL4CommandQueueInfo
- _GTMTLGuestAppClientAddMTLCommandQueueInfo
- _GTMTLGuestAppClientRemoveMTL4CommandQueueInfo
- _GTMTLGuestAppClientRemoveMTLCommandQueueInfo
- _GTMTLGuestAppClientSendMTLCaptureScopeInfo
- _GTMTLGuestAppClientUpdateMTLCommandQueueInfo
- _GTMTLGuestAppClientUpdateMTLDeviceInfo
- _GTMTLGuestAppClient_addCaptureDevice
- _GTMTLGuestAppClient_advanceToNextFrame
- _GTMTLGuestAppClient_allCaptureObjects
- _GTMTLGuestAppClient_copyCaptureDevices
- _GTMTLGuestAppClient_copyDeviceProfiles
- _GTMTLGuestAppClient_initPlatform
- _GTMTLGuestAppClient_interposeCommonInit
- _GTMTLGuestAppClient_notifyCaptureProgress
- _GTMTLGuestAppClient_notifyUnsupportedFenum
- _GTMTLGuestAppClient_release
- _GTMTLGuestAppClient_reportTelemetry
- _GTMTLGuestAppClient_unsupportedFenumDetected
- _GTMTLIndirectCommandEncoder_setBlendColor
- _GTMTLIndirectCommandEncoder_setCullMode
- _GTMTLIndirectCommandEncoder_setDepthBias
- _GTMTLIndirectCommandEncoder_setDepthClipMode
- _GTMTLIndirectCommandEncoder_setDepthStencilState
- _GTMTLIndirectCommandEncoder_setDepthTestBounds
- _GTMTLIndirectCommandEncoder_setFrontFacingWinding
- _GTMTLIndirectCommandEncoder_setScissorRects
- _GTMTLIndirectCommandEncoder_setScissorRectsCount
- _GTMTLIndirectCommandEncoder_setStencilReferenceValues
- _GTMTLIndirectCommandEncoder_setTriangleFillMode
- _GTMTLIndirectCommandEncoder_setViewports
- _GTMTLIndirectCommandEncoder_setViewportsCount
- _GTMTLQL_EncodeBuffer
- _GTMTLQL_EncodeSamplerState
- _GTMTLQL_EncodeTexture
- _GTMemWatchBufferMap_insert
- _GTMemWatchBufferMap_iterate
- _GTMemWatchBufferMap_lookupAddr
- _GTMemWatchBufferMap_remove
- _GTMemWatchLock_activateLockingMode
- _GTMemWatchLock_drainAndLock
- _GTMemWatchLock_lock
- _GTMemWatchLock_unlockForSyscall
- _GTMemWatchSyscallInterposer_isActive
- _GTMemWatch_installExceptionHandler
- _GTMemWatch_isEligibleForProtection
- _GTMemWatch_isEnabled
- _GTMemWatch_shouldBeEnabled
- _GTResourceDownloaderRequest_markAsPresentDownload
- _GTResourceHarvesterDestroy
- _GTResourceTrackerBuildArgumentBuffers
- _GTResourceTrackerIdentifier
- _GTResourceTrackerMake
- _GTResourceTrackerProcessCommandBuffer
- _GTResourceTrackerProcessCommandEncoder
- _GTResourceTrackerProcessIndirectCommandResourceUse
- _GTResourceTrackerResourceIsGPUOnly
- _GTResourceTrackerResourceReadArray
- _GTResourceTrackerResourceWriteArray
- _GTResourceTrackerResourceWriteMTLArray
- _GTResourceTrackerUsingResidencySetArray
- _GTResourceTrackerUsingResourceHeapArray
- _GTResourceTracker_resources
- _GTSMMTLRenderPipelineState_alphaToCoverageEnabled
- _GTSMMTLRenderPipelineState_colorAttachment
- _GTSMMTLRenderPipelineState_depthAttachmentPixelFormat
- _GTSMMTLRenderPipelineState_fragmentFunction
- _GTSMMTLRenderPipelineState_inputPrimitiveTopology
- _GTSMMTLRenderPipelineState_label
- _GTSMMTLRenderPipelineState_maxTessellationFactor
- _GTSMMTLRenderPipelineState_rasterSampleCount
- _GTSMMTLRenderPipelineState_rasterizationEnabled
- _GTSMMTLRenderPipelineState_stencilAttachmentPixelFormat
- _GTSMMTLRenderPipelineState_supportIndirectCommandBuffers
- _GTSMMTLRenderPipelineState_tessellationFactorFormat
- _GTSMMTLRenderPipelineState_tessellationFactorStepFunction
- _GTSMMTLRenderPipelineState_tessellationOutputWindingOrder
- _GTSMMTLRenderPipelineState_tessellationPartitionMode
- _GTSMMTLRenderPipelineState_vertexDescriptor
- _GTTraceDispatch_createArgumentTableStateMapFromParams
- _GTTraceDispatch_reconstructArgumentTableState
- _GTTraceDispatch_setArgumentTableStateForGPUCommandStage
- _GTTraceDispatch_sort_eventTracking
- _GTTraceStore_buildDebugContext
- _GetConditionByIndexInGroup
- _GetObjectForKey
- _GetSparseTextureMappingBuffer
- _GetSparseTextureMappingKernelFunction
- _IOObjectRelease
- _MGCopyMultipleAnswers
- _MTLDevice_newAccelerationStructureWithDescriptor
- _MTLDevice_newAccelerationStructureWithSize
- _MTLDevice_newAccelerationStructureWithSize_resourceIndex
- _MTLDevice_newAccelerationStructureWithSize_withDescriptor
- _MTLDevice_newTextureWithDescriptor
- _MTLIndirectCommandBuffer_descriptor
- _MTLTextureIsCube
- _MTLTextureMipmapSize
- _OBJC_IVAR_$_CaptureMTLTextureViewPool._textureViewsCopy
- _ResetHitCountInGroup
- _ResidencySetTakeSnapshot
- _ResidencySetTakeSnapshotForce
- _ResourceTracker_addTextureViewPools
- _ResourceTracker_processUsedDrawables
- _SaveMTL4ArgumentTableDescriptor
- _SaveMTL4BinaryFunctionDescriptor
- _SaveMTL4CommandAllocatorDescriptor
- _SaveMTL4CommandBufferOptions
- _SaveMTL4CommandQueueDescriptor
- _SaveMTL4CompilerDescriptor
- _SaveMTL4ComputePipelineDescriptor
- _SaveMTL4CopySparseBufferMappingOperation
- _SaveMTL4CopySparseTextureMappingOperation
- _SaveMTL4MachineLearningPipelineDescriptor
- _SaveMTL4UpdateSparseBufferMappingOperation
- _SaveMTL4UpdateSparseTextureMappingOperation
- _SaveMTLAccelerationStructureAllocationDescriptor
- _SaveMTLAccelerationStructurePassDescriptor
- _SaveMTLBinaryArchiveDescriptor
- _SaveMTLBlitPassDescriptor
- _SaveMTLBufferDescriptor
- _SaveMTLCommandBufferDescriptor
- _SaveMTLCommandQueueDescriptor
- _SaveMTLComputePassDescriptor
- _SaveMTLCounterSampleBufferDescriptor
- _SaveMTLDepthStencilDescriptor
- _SaveMTLDepthStencilStateInfo
- _SaveMTLHeapDescriptor
- _SaveMTLIOCommandQueueDescriptor
- _SaveMTLIndirectCommandBufferInfo
- _SaveMTLPipelineLibraryInfoWithPath
- _SaveMTLRenderPipelineFunctionsDescriptor
- _SaveMTLRenderPipelineReflection
- _SaveMTLResidencySetDescriptor
- _SaveMTLResourceStatePassDescriptor
- _SaveMTLResourceViewPoolDescriptor
- _SaveMTLSamplerDescriptor
- _SaveMTLSamplerStateInfo
- _SaveMTLScissorRect
- _SaveMTLShaderSamplingProgramInfo
- _SaveMTLTensorBufferAttachments
- _SaveMTLTextureMipmapInfo
- _SaveMTLTextureViewDescriptor
- _SaveMTLVertexAmplificationViewMappings
- _SaveMTLViewport
- _StreamArrayURL
- _TextureViewPoolTakeSnapshot
- _TranslateGTMTLAccelerationStructureInfo
- _TranslateGTMTLBinding
- _TranslateGTMTLBufferInfo
- _TranslateGTMTLDepthStencilStateInfo
- _TranslateGTMTLIndirectCommandBufferInfo
- _TranslateGTMTLIntersectionFunctionTableInfo
- _TranslateGTMTLLibraryInfo
- _TranslateGTMTLSamplerStateInfo
- _TranslateGTMTLTensorInfo
- _TranslateGTMTLTextureInfo
- _TranslateGTMTLTextureMipmapLevels
- _TranslateGTMTLVisibleFunctionTableInfo
- _UnwrapArray
- __NSGetExecutablePath
- __Z21DYDictionaryFromErrorP7NSError
- __Z21DYErrorFromDictionaryP12NSDictionary
- __ZN8GPUTools8VMBuffer10round_sizeEm
- __ZN8GPUTools8VMBuffer16protect_readonlyEv
- __ZN8GPUTools8VMBuffer5allocEmm
- __ZN8GPUTools8VMBuffer6resizeEm
- __ZN8GPUTools8VMBufferC1Emm
- __ZN8GPUTools8VMBufferC2Emm
- __ZN8GPUTools8VMBufferD1Ev
- __ZN8GPUTools8VMBufferD2Ev
- __ZN8GPUTools8VMBufferaSEOS0_
- __ZN8GPUTools9Interpose17DYCreateTransportEPKc
- ___59-[CaptureMTL4CommandQueue _signalCompletionHandlers:count:]_block_invoke
- ___block_descriptor_32_e344_v16?0r^{GTResourceDownloaderRequest=QQQQQISCb1b1b1b1b4(?={?=QQ}{?={GTMTLTensorSlice={GTMTLTensorExtents=Q[16Q]}{GTMTLTensorExtents=Q[16Q]}}{GTMTLTensorExtents=Q[16Q]}}{?=SS{?={?=ISS}{?=ISS}}IIISS[4c]}{?=QQ}{?={GTMTLIndirectCommandBufferDescriptor=QQSCCCCCCCCCCCCCCCCCCCCCCCCC[5C]}}{?=QQ}{?=Q}{?=QQ}{?=QQ{GTRange=QQ}{GTRange=QQ}}{GTRange=QQ})}8l
- ___block_descriptor_40_e344_v16?0r^{GTResourceDownloaderRequest=QQQQQISCb1b1b1b1b4(?={?=QQ}{?={GTMTLTensorSlice={GTMTLTensorExtents=Q[16Q]}{GTMTLTensorExtents=Q[16Q]}}{GTMTLTensorExtents=Q[16Q]}}{?=SS{?={?=ISS}{?=ISS}}IIISS[4c]}{?=QQ}{?={GTMTLIndirectCommandBufferDescriptor=QQSCCCCCCCCCCCCCCCCCCCCCCCCC[5C]}}{?=QQ}{?=Q}{?=QQ}{?=QQ{GTRange=QQ}{GTRange=QQ}}{GTRange=QQ})}8l
- ___block_descriptor_56_8_32s40bs_e29_v24?0"<MTLSharedEvent>"8Q16ls32l8s40l8
- _catch_mach_exception_raise_state
- _catch_mach_exception_raise_state_identity
- _catch_mach_exception_raise_state_identity_protected
- _copyDYMTLCommandQueueInfo
- _deviceMTLComputePipelineDescriptor
- _deviceMTLMeshRenderPipelineDescriptor
- _isDesktopReplayer
- _isMobileReplayer
- _kCFTypeArrayCallBacks
- _mach_exception_raise
- _mach_exception_raise_identity_protected
- _mach_exception_raise_state
- _mach_exception_raise_state_identity
- _mach_exception_raise_state_identity_protected
- _modifyReplayerEnvironment
- _newDYDeviceInfo
- _newDYMTL4CommandQueueInfo
- _newDYMTLCommandQueueInfo
- _objc_msgSend$_postCommit:count:
- _objc_msgSend$_signalCompletionHandlers:count:
- _objc_msgSend$addEntriesFromDictionary:
- _objc_msgSend$bundlePath
- _objc_msgSend$bundleWithPath:
- _objc_msgSend$commandQueueStreamRef
- _objc_msgSend$componentsSeparatedByString:
- _objc_msgSend$dictionaryForKey:
- _objc_msgSend$dictionaryWithObjectsAndKeys:
- _objc_msgSend$fileExistsAtPath:
- _objc_msgSend$getInfoWithAddress:
- _objc_msgSend$getInfoWithStreamRef:
- _objc_msgSend$initWithMode:
- _objc_msgSend$integerValue
- _objc_msgSend$pathWithComponents:
- _objc_msgSend$scopeStreamRef
- _objc_msgSend$subarrayWithRange:
- _objc_retain_x7
- _unwrapFrameInterpolatorDescriptor
- _unwrapMTL4AccelerationStructureDescriptor
- _unwrapMTL4CommandBufferOptions
- _unwrapMTL4CompilerDescriptor
- _unwrapMTL4CompilerTaskOptions
- _unwrapMTL4RenderPipelineBinaryFunctionsDescriptor
- _unwrapMTLCommandQueueDescriptor
- _unwrapMTLIntersectionFunctionDescriptor
- _unwrapMTLIntersectionFunctionTableDescriptor
- _unwrapMTLRenderPipelineFunctionsDescriptor
- _unwrapMTLResourceStatePassDescriptor_
- _unwrapMTLVisibleFunctionTableDescriptor
CStrings:
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/capture/mtl/CaptureMTLTextureViewPool.m:105"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/dump/GTTraceDispatch.c:683"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTCaptureArchive.c:283"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTCaptureArchive.c:354"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTCaptureArchive.c:413"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTCaptureArchive.c:712"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/sm/GTSMMTLBuilder.c:2657"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trace/GTTraceContext.c:170"
+ "0xffffc0e9"
+ "0xffffc0ea"
+ "@\"<MTL4CounterHeap>\""
+ "@\"CaptureMTLTextureViewPool\""
+ "@32@0:8@16^{GTTraceContext={?=B[7c]^{apr_pool_t}}{_opaque_pthread_mutex_t=q[56c]}^{GTTraceStore}AQAQ^{apr_hash_t}^(FreeNode)Ai[4c]^{GTTraceStream}AB[7c][16{GTTraceStoreList=^(GTTraceStoreNode)^(GTTraceStoreNode)AiAi}]}24"
+ "B40@0:8r^@16Q24Q32"
+ "CaptureMTL4CounterHeap"
+ "Ct@2ul@2ultt"
+ "Ct@2ultultt"
+ "Culultul"
+ "DownloadTensorPlane%u[name=%lu, ref=%llu]"
+ "MTL4CounterHeap"
+ "MTLTensor-%llu-%u-Plane%u"
+ "T@\"<MTL4CounterHeap>\",R"
+ "T^{GTTraceContext={?=B[7c]^{apr_pool_t}}{_opaque_pthread_mutex_t=q[56c]}^{GTTraceStore}AQAQ^{apr_hash_t}^(FreeNode)Ai[4c]^{GTTraceStream}AB[7c][16{GTTraceStoreList=^(GTTraceStoreNode)^(GTTraceStoreNode)AiAi}]},R"
+ "^{GTTraceContext={?=B[7c]^{apr_pool_t}}{_opaque_pthread_mutex_t=q[56c]}^{GTTraceStore}AQAQ^{apr_hash_t}^(FreeNode)Ai[4c]^{GTTraceStream}AB[7c][16{GTTraceStoreList=^(GTTraceStoreNode)^(GTTraceStoreNode)AiAi}]}"
+ "^{GTTraceContext={?=B[7c]^{apr_pool_t}}{_opaque_pthread_mutex_t=q[56c]}^{GTTraceStore}AQAQ^{apr_hash_t}^(FreeNode)Ai[4c]^{GTTraceStream}AB[7c][16{GTTraceStoreList=^(GTTraceStoreNode)^(GTTraceStoreNode)AiAi}]}16@0:8"
+ "_nextLivePool"
+ "_postCommit:count:captured:"
+ "_prevLivePool"
+ "_resourceViewCount"
+ "_signalCompletionHandlers:count:captured:"
+ "_snapshotGeneration"
+ "counterHeap"
+ "counterHeaps"
+ "fail: Failed to create MTLTensor scales plane target for downloading: %@"
+ "file.fd >= 0"
+ "getScalesPlaneTensorAlias:dataPlaneOffset:"
+ "invalidateCounterRange:"
+ "kDYFEMTL4CounterHeap_dealloc"
+ "kDYFEMTL4CounterHeap_invalidateCounterRange"
+ "kDYFEMTL4CounterHeap_resolveCounterRange"
+ "kDYFEMTL4CounterHeap_setLabel"
+ "memcmp((const char*)bytes + offset, (\"CUtt\"), sizeof(\"CUtt\")) == 0"
+ "memcmp((const char*)bytes + offset, (\"Ct@2ul@2ultt\"), sizeof(\"Ct@2ul@2ultt\")) == 0"
+ "memcmp((const char*)bytes + offset, (\"Ct@2ultultt\"), sizeof(\"Ct@2ultultt\")) == 0"
+ "memcmp((const char*)bytes + offset, (\"Culultul\"), sizeof(\"Culultul\")) == 0"
+ "resolveCounterHeap:withRange:intoBuffer:atOffset:waitFence:updateFence:"
+ "setCount:"
+ "v16@?0r^{GTResourceDownloaderRequest=QQQQQISCb1b1b1b1b4(?={?=QQ}{?={GTMTLTensorSlice={GTMTLTensorExtents=Q[16Q]}{GTMTLTensorExtents=Q[16Q]}}{GTMTLTensorExtents=Q[16Q]}C[7c]}{?=SS{?={?=ISS}{?=ISS}}IIISS[4c]}{?=QQ}{?={GTMTLIndirectCommandBufferDescriptor=QQSCCCCCCCCCCCCCCCCCCCCCCCCC[5C]}}{?=QQ}{?=Q}{?=QQ}{?=QQ{GTRange=QQ}{GTRange=QQ}}{GTRange=QQ})}8"
+ "v32@0:8r^{GTResourceDownloaderRequest=QQQQQISCb1b1b1b1b4(?={?=QQ}{?={GTMTLTensorSlice={GTMTLTensorExtents=Q[16Q]}{GTMTLTensorExtents=Q[16Q]}}{GTMTLTensorExtents=Q[16Q]}C[7c]}{?=SS{?={?=ISS}{?=ISS}}IIISS[4c]}{?=QQ}{?={GTMTLIndirectCommandBufferDescriptor=QQSCCCCCCCCCCCCCCCCCCCCCCCCC[5C]}}{?=QQ}{?=Q}{?=QQ}{?=QQ{GTRange=QQ}{GTRange=QQ}}{GTRange=QQ})}16@24"
+ "v36@0:8r^@16Q24B32"
+ "v36@0:8r^{GTResourceDownloaderRequest=QQQQQISCb1b1b1b1b4(?={?=QQ}{?={GTMTLTensorSlice={GTMTLTensorExtents=Q[16Q]}{GTMTLTensorExtents=Q[16Q]}}{GTMTLTensorExtents=Q[16Q]}C[7c]}{?=SS{?={?=ISS}{?=ISS}}IIISS[4c]}{?=QQ}{?={GTMTLIndirectCommandBufferDescriptor=QQSCCCCCCCCCCCCCCCCCCCCCCCCC[5C]}}{?=QQ}{?=Q}{?=QQ}{?=QQ{GTRange=QQ}{GTRange=QQ}}{GTRange=QQ})}16@24I32"
+ "v40@0:8r^{GTResourceDownloaderRequest=QQQQQISCb1b1b1b1b4(?={?=QQ}{?={GTMTLTensorSlice={GTMTLTensorExtents=Q[16Q]}{GTMTLTensorExtents=Q[16Q]}}{GTMTLTensorExtents=Q[16Q]}C[7c]}{?=SS{?={?=ISS}{?=ISS}}IIISS[4c]}{?=QQ}{?={GTMTLIndirectCommandBufferDescriptor=QQSCCCCCCCCCCCCCCCCCCCCCCCCC[5C]}}{?=QQ}{?=Q}{?=QQ}{?=QQ{GTRange=QQ}{GTRange=QQ}}{GTRange=QQ})}16@24@32"
+ "v72@0:8@16{_NSRange=QQ}24@40Q48@56@64"
+ "warning: MTLTensor plane %u is not supported for download"
- "/%@"
- "/Applications/Xcode.app/Contents/Developer/Applications/"
- "/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/Library/GPUToolsPlatform/"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/capture/mtl/CaptureMTLTextureViewPool.m:53"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/dump/GTTraceDispatch.c:673"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTCaptureArchive.c:278"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTCaptureArchive.c:349"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTCaptureArchive.c:408"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/net/GTCaptureArchive.c:719"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/sm/GTSMMTLBuilder.c:2613"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/GPUToolsDevice/GPUTools/GTMTLCapture/trace/GTTraceContext.c:162"
- "/System/Library/CoreServices/"
- "/System/Library/Frameworks/Metal.framework"
- "/System/Library/PrivateFrameworks/"
- "@32@0:8@16^{GTTraceContext={?=B[7c]}{_opaque_pthread_mutex_t=q[56c]}^{GTTraceStore}AQAQ^{apr_hash_t}^(FreeNode)Ai[4c]^{GTTraceStream}AB[7c][16{GTTraceStoreList=^(GTTraceStoreNode)^(GTTraceStoreNode)AiAi}]}24"
- "CaptureCommandQueueAddress"
- "CaptureDeviceName"
- "CaptureLayerAddress"
- "CaptureScopeAddress"
- "CaptureScopeID"
- "DYLD_INSERT_LIBRARIES"
- "DYMTL_TOOLS_DYLIB_PATH"
- "Developer/Applications"
- "FrameLimit"
- "GPUDebugger.ReplayerEnvironment"
- "GPUTOOLS_EXTRA_PLUGIN_PATHS"
- "GPUToolsCapture.framework/GPUToolsCapture"
- "GPUToolsDiagnostics.framework/GPUToolsDiagnostics"
- "GPUToolsTransportAgents.framework/Versions/A/XPCServices/GPUToolsAgentService.xpc/Contents/MacOS"
- "GTTransport *DYCreateTransportC(const char *)"
- "HostCaptureArchivePath"
- "IsBoundaryLess"
- "METAL_LOAD_INTERPOSER"
- "Metal 4 Counter Heap"
- "Render pipeline specialization"
- "Serial"
- "Skipping invalid buffer binding %lu (GPUVA 0x%llx)"
- "Skipping invalid kernel buffer binding %lu (GPUVA 0x%llx)"
- "Skipping invalid vertex buffer binding %lu (GPUVA 0x%llx)"
- "SuspendAfterCompletion"
- "T^{GTTraceContext={?=B[7c]}{_opaque_pthread_mutex_t=q[56c]}^{GTTraceStore}AQAQ^{apr_hash_t}^(FreeNode)Ai[4c]^{GTTraceStream}AB[7c][16{GTTraceStoreList=^(GTTraceStoreNode)^(GTTraceStoreNode)AiAi}]},R"
- "TriggerFrame"
- "^{GTTraceContext={?=B[7c]}{_opaque_pthread_mutex_t=q[56c]}^{GTTraceStore}AQAQ^{apr_hash_t}^(FreeNode)Ai[4c]^{GTTraceStream}AB[7c][16{GTTraceStoreList=^(GTTraceStoreNode)^(GTTraceStoreNode)AiAi}]}"
- "^{GTTraceContext={?=B[7c]}{_opaque_pthread_mutex_t=q[56c]}^{GTTraceStore}AQAQ^{apr_hash_t}^(FreeNode)Ai[4c]^{GTTraceStream}AB[7c][16{GTTraceStoreList=^(GTTraceStoreNode)^(GTTraceStoreNode)AiAi}]}16@0:8"
- "_postCommit:count:"
- "_signalCompletionHandlers:count:"
- "_textureViewsCopy"
- "addEntriesFromDictionary:"
- "bundlePath"
- "bundleWithPath:"
- "com.apple.DesktopReplayer"
- "com.apple.MTLReplayer"
- "com.apple.MobileReplayer"
- "commandQueueStreamRef"
- "componentsSeparatedByString:"
- "dictionaryForKey:"
- "dictionaryWithObjectsAndKeys:"
- "error code"
- "error description"
- "error domain"
- "fail: [create_transport] GT_HOST_URL environment not set"
- "fail: [create_transport] failed to create transport; GT_HOST_URL: %s"
- "fail: [create_transport] failed to parse GT_HOST_URL: %s"
- "fd > 0"
- "file"
- "fileExistsAtPath:"
- "gputools.contexts-info"
- "integerValue"
- "interpose_version"
- "interpose_version_metal"
- "kDYFEMTLCommandBuffer_computeCommandEncoderWithParallelExecution"
- "kDYFEMTLComputeCommandEncoder_dispatchBarrier"
- "metal_version"
- "nativePointerSize"
- "pathWithComponents:"
- "platformPrefix"
- "scopeStreamRef"
- "screen-dimensions"
- "shouldLoadCapture"
- "shouldLoadDiagnostics"
- "shouldLoadReplayer"
- "subarrayWithRange:"
- "url_str"
- "v16@?0r^{GTResourceDownloaderRequest=QQQQQISCb1b1b1b1b4(?={?=QQ}{?={GTMTLTensorSlice={GTMTLTensorExtents=Q[16Q]}{GTMTLTensorExtents=Q[16Q]}}{GTMTLTensorExtents=Q[16Q]}}{?=SS{?={?=ISS}{?=ISS}}IIISS[4c]}{?=QQ}{?={GTMTLIndirectCommandBufferDescriptor=QQSCCCCCCCCCCCCCCCCCCCCCCCCC[5C]}}{?=QQ}{?=Q}{?=QQ}{?=QQ{GTRange=QQ}{GTRange=QQ}}{GTRange=QQ})}8"
- "v32@0:8r^{GTResourceDownloaderRequest=QQQQQISCb1b1b1b1b4(?={?=QQ}{?={GTMTLTensorSlice={GTMTLTensorExtents=Q[16Q]}{GTMTLTensorExtents=Q[16Q]}}{GTMTLTensorExtents=Q[16Q]}}{?=SS{?={?=ISS}{?=ISS}}IIISS[4c]}{?=QQ}{?={GTMTLIndirectCommandBufferDescriptor=QQSCCCCCCCCCCCCCCCCCCCCCCCCC[5C]}}{?=QQ}{?=Q}{?=QQ}{?=QQ{GTRange=QQ}{GTRange=QQ}}{GTRange=QQ})}16@24"
- "v36@0:8r^{GTResourceDownloaderRequest=QQQQQISCb1b1b1b1b4(?={?=QQ}{?={GTMTLTensorSlice={GTMTLTensorExtents=Q[16Q]}{GTMTLTensorExtents=Q[16Q]}}{GTMTLTensorExtents=Q[16Q]}}{?=SS{?={?=ISS}{?=ISS}}IIISS[4c]}{?=QQ}{?={GTMTLIndirectCommandBufferDescriptor=QQSCCCCCCCCCCCCCCCCCCCCCCCCC[5C]}}{?=QQ}{?=Q}{?=QQ}{?=QQ{GTRange=QQ}{GTRange=QQ}}{GTRange=QQ})}16@24I32"
- "v40@0:8r^{GTResourceDownloaderRequest=QQQQQISCb1b1b1b1b4(?={?=QQ}{?={GTMTLTensorSlice={GTMTLTensorExtents=Q[16Q]}{GTMTLTensorExtents=Q[16Q]}}{GTMTLTensorExtents=Q[16Q]}}{?=SS{?={?=ISS}{?=ISS}}IIISS[4c]}{?=QQ}{?={GTMTLIndirectCommandBufferDescriptor=QQSCCCCCCCCCCCCCCCCCCCCCCCCC[5C]}}{?=QQ}{?=Q}{?=QQ}{?=QQ{GTRange=QQ}{GTRange=QQ}}{GTRange=QQ})}16@24@32"
```
