## libBKDM2.dylib

> `/usr/lib/libBKDM2.dylib`

```diff

 980.0.26.0.0
-  __TEXT.__text: 0x7c2d8
-  __TEXT.__objc_methlist: 0x5d84
-  __TEXT.__const: 0xd7b8
-  __TEXT.__cstring: 0x7066
-  __TEXT.__oslogstring: 0x46ec
-  __TEXT.__gcc_except_tab: 0x17b4
+  __TEXT.__text: 0x88640
+  __TEXT.__lazy_helpers: 0xa8
+  __TEXT.__objc_methlist: 0x61bc
+  __TEXT.__const: 0xd7f8
+  __TEXT.__cstring: 0x832a
+  __TEXT.__oslogstring: 0x52f7
+  __TEXT.__gcc_except_tab: 0x1a88
   __TEXT.__ustring: 0x11c
-  __TEXT.__unwind_info: 0xe30
+  __TEXT.__unwind_info: 0x1050
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x15e8
-  __DATA_CONST.__objc_classlist: 0xe0
+  __DATA_CONST.__const: 0x16d8
+  __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d60
-  __DATA_CONST.__objc_superrefs: 0xc0
-  __DATA_CONST.__objc_arraydata: 0x4a8
-  __DATA_CONST.__got: 0x448
-  __AUTH_CONST.__const: 0xc08
-  __AUTH_CONST.__cfstring: 0x65e0
-  __AUTH_CONST.__objc_const: 0x9a58
-  __AUTH_CONST.__objc_intobj: 0x3d8
+  __DATA_CONST.__objc_selrefs: 0x40b0
+  __DATA_CONST.__objc_superrefs: 0xd0
+  __DATA_CONST.__objc_arraydata: 0x4d8
+  __DATA_CONST.__got: 0x4a8
+  __AUTH_CONST.__const: 0xc28
+  __AUTH_CONST.__cfstring: 0x6c40
+  __AUTH_CONST.__objc_const: 0xa490
+  __AUTH_CONST.__lazy_load_got: 0x10
+  __AUTH_CONST.__objc_intobj: 0x420
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH_CONST.__objc_arrayobj: 0x168
-  __AUTH_CONST.__auth_got: 0x768
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0xacc
-  __DATA.__data: 0x880
-  __DATA_DIRTY.__objc_data: 0x6e0
-  __DATA_DIRTY.__data: 0x14
+  __AUTH_CONST.__objc_arrayobj: 0x1b0
+  __AUTH_CONST.__auth_got: 0x7d0
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0xbb4
+  __DATA.__data: 0x884
+  __DATA.__common: 0x10
+  __DATA_DIRTY.__objc_data: 0x730
+  __DATA_DIRTY.__data: 0x1c
   __DATA_DIRTY.__common: 0x40
-  __DATA_DIRTY.__bss: 0xa0
+  __DATA_DIRTY.__bss: 0xaa
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystemHealth.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2905
-  Symbols:   5371
-  CStrings:  1613
+  Functions: 3153
+  Symbols:   5708
+  CStrings:  1828
 
Symbols:
+ +[BLHelper stringFromAVFrameType:]
+ +[BLHelper stringFromAVInfraredLightSourceMode:]
+ +[BioLog setUsingExclaves:hasMirage:]
+ +[PearlFrame initialize]
+ -[BLFrameDebugExtraFID .cxx_destruct]
+ -[BLFrameDebugExtraFID dictionaryFromAlgoData:]
+ -[BLFrameDebugExtraFID dictionaryFromFrameMetadata:]
+ -[BLFrameDebugExtraFID lastAlgoDataFrameNumber]
+ -[BLFrameDebugExtraFID lastAlgoData]
+ -[BLFrameDebugExtraFID processFrameDebugData:withHeader:dict:]
+ -[BLFrameDebugExtraFID setLastAlgoData:]
+ -[BLFrameDebugExtraFID setLastAlgoDataFrameNumber:]
+ -[BioLog cacheQueuedFrame]
+ -[BioLog cacheQueuedFrames]
+ -[BioLog frameIRSharedMemoryMap]
+ -[BioLog frameIRSharedMemoryUnmap]
+ -[BioLog frameRGBSharedMemoryMap]
+ -[BioLog frameRGBSharedMemoryUnmap]
+ -[BioLog logBracketConfiguration:]
+ -[BioLog logFrame:]
+ -[BioLog logPasscodeShortcutRequested:]
+ -[BioLog releaseFramesFromQueue:toCount:]
+ -[BioLog updateFrameLoggingState]
+ -[BioLog writeQueuedFrame]
+ -[BiometricEnrollOperationPearl .cxx_destruct]
+ -[BiometricEnrollOperationPearl secureFaceDetectRequestDispatchBlock]
+ -[BiometricEnrollOperationPearl setSecureFaceDetectRequestDispatchBlock:]
+ -[BiometricKitXPCServerPearl avcRetryTypeFromSecureFaceDetectRetryType:]
+ -[BiometricKitXPCServerPearl captureSecureFaceDetectRequestDispatchBlock]
+ -[BiometricKitXPCServerPearl checkForPasscodeShortcut]
+ -[BiometricKitXPCServerPearl isFaceIDInExclavesEnabled]
+ -[BiometricKitXPCServerPearl loadReferenceFramesInfoRecord]
+ -[BiometricKitXPCServerPearl loadSummervilleFWCertificate]
+ -[BiometricKitXPCServerPearl platformHasMirage:]
+ -[BiometricKitXPCServerPearl platformHasPinnacles]
+ -[BiometricKitXPCServerPearl processCoachingStatus:frameType:projectorMode:]
+ -[BiometricKitXPCServerPearl processFrame:]
+ -[BiometricKitXPCServerPearl releaseFrameMessage:]
+ -[BiometricKitXPCServerPearl resetSecureFaceDetectDispatchHandlerBlock]
+ -[BiometricKitXPCServerPearl setSecureFaceDetectRequestDispatchBlock:]
+ -[BiometricMatchOperationPearl .cxx_destruct]
+ -[BiometricMatchOperationPearl secureFaceDetectRequestDispatchBlock]
+ -[BiometricMatchOperationPearl setSecureFaceDetectRequestDispatchBlock:]
+ -[BiometricPresenceDetectOperationPearl secureFaceDetectRequestDispatchBlock]
+ -[BiometricPresenceDetectOperationPearl setSecureFaceDetectRequestDispatchBlock:]
+ -[PearlCoreAnalytics analyzeSecureSequenceFrameMeta:requestType:fromCameraID:]
+ -[PearlFrame .cxx_destruct]
+ -[PearlFrame cacheMetadataWithPool:sharedBufferPort:]
+ -[PearlFrame cacheRawDataWithPool:sharedBufferPort:]
+ -[PearlFrame cachedMetadata]
+ -[PearlFrame cachedRawData]
+ -[PearlFrame cameraID]
+ -[PearlFrame dataLengthFromFormatDescription:]
+ -[PearlFrame dealloc]
+ -[PearlFrame description]
+ -[PearlFrame faceIDObject]
+ -[PearlFrame frameID]
+ -[PearlFrame frameType]
+ -[PearlFrame initWithAVMetadataFaceIDObject:sequenceNumber:cameraID:frameNumber:sessionID:]
+ -[PearlFrame isEqualToFrameID:]
+ -[PearlFrame lightSourceProjectorMode]
+ -[PearlFrame metadataLength]
+ -[PearlFrame rawDataLength]
+ -[PearlFrame redactedDescription]
+ -[PearlFrame referenceDataLength]
+ -[PearlFrame releaseCachedMetaData]
+ -[PearlFrame releaseCachedRawData]
+ -[PearlFrame releaseFaceIDObject]
+ -[PearlFrame retainFaceIDObject]
+ -[PearlFrame sessionID]
+ -[PearlFrame setTransaction:]
+ -[PearlFrame timestamp]
+ -[PearlFrame transaction]
+ -[PearlFrameQueue .cxx_destruct]
+ -[PearlFrameQueue _dequeue]
+ -[PearlFrameQueue _enqueue:]
+ -[PearlFrameQueue containsFrameID:]
+ -[PearlFrameQueue count]
+ -[PearlFrameQueue dequeueAllFramesToQueue:]
+ -[PearlFrameQueue dequeue]
+ -[PearlFrameQueue description]
+ -[PearlFrameQueue enqueue:]
+ -[PearlFrameQueue initWithName:capacity:releaseWhenFull:]
+ -[PearlFrameQueue isEmpty]
+ -[PearlFrameQueue releaseAllFrames]
+ -[PearlFrameQueue removeFrameID:]
+ GCC_except_table108
+ GCC_except_table113
+ GCC_except_table114
+ GCC_except_table115
+ GCC_except_table118
+ GCC_except_table120
+ GCC_except_table127
+ GCC_except_table18
+ GCC_except_table238
+ GCC_except_table248
+ GCC_except_table264
+ GCC_except_table268
+ GCC_except_table271
+ GCC_except_table274
+ GCC_except_table280
+ GCC_except_table281
+ GCC_except_table287
+ GCC_except_table289
+ GCC_except_table290
+ GCC_except_table30
+ GCC_except_table32
+ GCC_except_table34
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table38
+ GCC_except_table39
+ GCC_except_table50
+ GCC_except_table52
+ GCC_except_table53
+ GCC_except_table54
+ GCC_except_table67
+ GCC_except_table69
+ GCC_except_table84
+ _AMFDRSealingMapCopyLocalData
+ _AVCaptureDeviceTypeBuiltInColorAssistedInfraredMetadataCamera
+ _AVCaptureDeviceTypeBuiltInUltraWideAngleMetadataCamera
+ _AVMetadataObjectTypeFaceID
+ _CMFormatDescriptionGetExtension
+ _CMVideoFormatDescriptionGetDimensions
+ _FIDCDeserializeLogData
+ _FIDCDeserializeLogData$lazyAuthGOT_IA_0
+ _FIDCDeserializeLogData$lazyAuthGOT_IA_0$loadHelper_x8
+ _FIDCDeserializeLogData$lazyAuthGOT_IA_ad_0
+ _FIDCDeserializeLogData$lazyLoadStub
+ _OBJC_CLASS_$_AVCaptureConnection
+ _OBJC_CLASS_$_AVCaptureFaceIDBracketConfiguration
+ _OBJC_CLASS_$_AVCaptureFaceIDBracketEncryptionConfiguration
+ _OBJC_CLASS_$_AVCaptureFaceIDConfiguration
+ _OBJC_CLASS_$_BLFrameDebugExtraFID
+ _OBJC_CLASS_$_PearlFrame
+ _OBJC_CLASS_$_PearlFrameQueue
+ _OBJC_IVAR_$_BLFrameDebugExtraFID._lastAlgoData
+ _OBJC_IVAR_$_BLFrameDebugExtraFID._lastAlgoDataFrameNumber
+ _OBJC_IVAR_$_BioLog._exclavesIRBufferPort
+ _OBJC_IVAR_$_BioLog._exclavesRGBBufferPort
+ _OBJC_IVAR_$_BioLog._faceIDObjectCount
+ _OBJC_IVAR_$_BioLog._frameDispatchQueueCaching
+ _OBJC_IVAR_$_BioLog._frameMetaCachePool
+ _OBJC_IVAR_$_BioLog._frameQueueCaching
+ _OBJC_IVAR_$_BioLog._frameQueueWaiting
+ _OBJC_IVAR_$_BioLog._frameQueueWriting
+ _OBJC_IVAR_$_BioLog._frameRawIRCachePool
+ _OBJC_IVAR_$_BioLog._frameRawRGBCachePool
+ _OBJC_IVAR_$_BioLog._irFaceIDObjectRetainCount
+ _OBJC_IVAR_$_BioLog._lastFrameCachingSemaphore
+ _OBJC_IVAR_$_BioLog._lastPreCheckFrameID
+ _OBJC_IVAR_$_BioLog._lastPreCheckFrameMetadata
+ _OBJC_IVAR_$_BioLog._lastPreCheckFrameReady
+ _OBJC_IVAR_$_BioLog._prevPreCheckFrameID
+ _OBJC_IVAR_$_BioLog._prevPreCheckFrameMetadata
+ _OBJC_IVAR_$_BioLog._prevPreCheckFrameReady
+ _OBJC_IVAR_$_BioLog._rgbFaceIDObjectRetainCount
+ _OBJC_IVAR_$_BioLog._secureFaceDetectBracketFrameCount
+ _OBJC_IVAR_$_BioLog._secureFaceDetectFrameCount
+ _OBJC_IVAR_$_BioLog._secureFaceDetectIRFrameCount
+ _OBJC_IVAR_$_BioLog._secureFaceDetectRGBFrameCount
+ _OBJC_IVAR_$_BioLog._streamingBatchFrameCounter
+ _OBJC_IVAR_$_BiometricEnrollOperationPearl._secureFaceDetectRequestDispatchBlock
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._avcHPQueue
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._avcRGBOutput
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._frameProcessingQueue
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._irStreamRunning
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._passcodeShortcutRequested
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._remainingBracketIRFrames
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._remainingBracketRGBFrames
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._rgbStreamRunning
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._secureFaceDetectFrameCount
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._usingExclaveDriver
+ _OBJC_IVAR_$_BiometricMatchOperationPearl._secureFaceDetectRequestDispatchBlock
+ _OBJC_IVAR_$_BiometricPresenceDetectOperationPearl._secureFaceDetectRequestDispatchBlock
+ _OBJC_IVAR_$_PearlFrame._cachedMetadata
+ _OBJC_IVAR_$_PearlFrame._cachedRawData
+ _OBJC_IVAR_$_PearlFrame._cameraID
+ _OBJC_IVAR_$_PearlFrame._dataPool
+ _OBJC_IVAR_$_PearlFrame._faceIDObject
+ _OBJC_IVAR_$_PearlFrame._faceIDObjectRetainCount
+ _OBJC_IVAR_$_PearlFrame._frameID
+ _OBJC_IVAR_$_PearlFrame._frameType
+ _OBJC_IVAR_$_PearlFrame._lightSourceProjectorMode
+ _OBJC_IVAR_$_PearlFrame._metadataLength
+ _OBJC_IVAR_$_PearlFrame._rawDataLength
+ _OBJC_IVAR_$_PearlFrame._referenceDataLength
+ _OBJC_IVAR_$_PearlFrame._sessionID
+ _OBJC_IVAR_$_PearlFrame._timestamp
+ _OBJC_IVAR_$_PearlFrame._transaction
+ _OBJC_IVAR_$_PearlFrameQueue._array
+ _OBJC_IVAR_$_PearlFrameQueue._capacity
+ _OBJC_IVAR_$_PearlFrameQueue._name
+ _OBJC_IVAR_$_PearlFrameQueue._releasing
+ _OBJC_METACLASS_$_BLFrameDebugExtraFID
+ _OBJC_METACLASS_$_PearlFrame
+ _OBJC_METACLASS_$_PearlFrameQueue
+ __OBJC_$_CLASS_METHODS_PearlFrame
+ __OBJC_$_INSTANCE_METHODS_BLFrameDebugExtraFID
+ __OBJC_$_INSTANCE_METHODS_PearlFrame
+ __OBJC_$_INSTANCE_METHODS_PearlFrameQueue
+ __OBJC_$_INSTANCE_VARIABLES_BLFrameDebugExtraFID
+ __OBJC_$_INSTANCE_VARIABLES_PearlFrame
+ __OBJC_$_INSTANCE_VARIABLES_PearlFrameQueue
+ __OBJC_$_PROP_LIST_BLFrameDebugExtraFID
+ __OBJC_$_PROP_LIST_PearlFrame
+ __OBJC_CLASS_RO_$_BLFrameDebugExtraFID
+ __OBJC_CLASS_RO_$_PearlFrame
+ __OBJC_CLASS_RO_$_PearlFrameQueue
+ __OBJC_METACLASS_RO_$_BLFrameDebugExtraFID
+ __OBJC_METACLASS_RO_$_PearlFrame
+ __OBJC_METACLASS_RO_$_PearlFrameQueue
+ ___26-[BioLog cacheQueuedFrame]_block_invoke
+ ___26-[BioLog writeQueuedFrame]_block_invoke
+ ___32-[BioLog frameIRSharedMemoryMap]_block_invoke
+ ___33-[BioLog frameRGBSharedMemoryMap]_block_invoke
+ ___33-[BioLog updateFrameLoggingState]_block_invoke
+ ___33-[BioLog updateFrameLoggingState]_block_invoke_2
+ ___33-[BioLog updateFrameLoggingState]_block_invoke_3
+ ___33-[BioLog updateFrameLoggingState]_block_invoke_4
+ ___34-[BioLog frameIRSharedMemoryUnmap]_block_invoke
+ ___35-[BioLog frameRGBSharedMemoryUnmap]_block_invoke
+ ___50-[BiometricKitXPCServerPearl platformHasPinnacles]_block_invoke
+ ___50-[BiometricKitXPCServerPearl releaseFrameMessage:]_block_invoke
+ ___54-[BiometricKitXPCServerPearl checkForPasscodeShortcut]_block_invoke
+ ___55-[BiometricKitXPCServerPearl isFaceIDInExclavesEnabled]_block_invoke
+ ___62-[BLFrameDebugExtraFID processFrameDebugData:withHeader:dict:]_block_invoke
+ ___64-[BioLog logSecureFrameMeta:timestamp:frameNumber:fromCameraID:]_block_invoke_2
+ ___73-[BiometricKitXPCServerPearl captureSecureFaceDetectRequestDispatchBlock]_block_invoke
+ ___75-[BiometricKitXPCServerPearl processReceivedSecureFaceDetectRequestMessage]_block_invoke_2
+ ___block_descriptor_155_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_72_e8_32s40r48r56r_e5_v8?0ls32l8r40l8r48l8r56l8
+ ___block_descriptor_80_e8_32s40s48r56r64r_e5_v8?0ls32l8r48l8r56l8s40l8r64l8
+ ___block_descriptor_88_e8_32s40s48r56r64r72r_e5_v8?0ls32l8r48l8r56l8s40l8r64l8r72l8
+ ___osLogTrace_PearlFrameSupport
+ ___osLog_PearlFrameSupport
+ _coachingStatusToEngagementInfo
+ _dispatch_block_create
+ _dispatch_queue_create_with_target$V2
+ _dispatch_workloop_create_inactive
+ _dispatch_workloop_set_scheduler_priority
+ _exclaves_outbound_buffer_copyout
+ _exclaves_outbound_buffer_create
+ _isFaceIDInExclavesEnabled.onceToken
+ _kCMFormatDescriptionExtension_BytesPerRow
+ _kExclavesIRBufferSize
+ _kExclavesRGBBufferSize
+ _kPearlFrameQueueCapacity
+ _lazyLoadFlag$FaceIDCoreLib_demo
+ _mach_port_deallocate
+ _objc_copyStruct
+ _objc_msgSend$_dequeue
+ _objc_msgSend$_enqueue:
+ _objc_msgSend$addConnection:
+ _objc_msgSend$addOutputWithNoConnections:
+ _objc_msgSend$allocateData
+ _objc_msgSend$analyzeSecureSequenceFrameMeta:requestType:fromCameraID:
+ _objc_msgSend$arrayByAddingObject:
+ _objc_msgSend$avcRetryTypeFromSecureFaceDetectRetryType:
+ _objc_msgSend$cacheMetadataWithPool:sharedBufferPort:
+ _objc_msgSend$cacheQueuedFrame
+ _objc_msgSend$cacheQueuedFrames
+ _objc_msgSend$cacheRawDataWithPool:sharedBufferPort:
+ _objc_msgSend$cachedMetadata
+ _objc_msgSend$cachedRawData
+ _objc_msgSend$cameraID
+ _objc_msgSend$canAddConnection:
+ _objc_msgSend$captureFaceIDBracketWithConfiguration:
+ _objc_msgSend$captureSecureFaceDetectRequestDispatchBlock
+ _objc_msgSend$checkForPasscodeShortcut
+ _objc_msgSend$colorBracketEncryptionConfiguration
+ _objc_msgSend$connectionWithInputPorts:output:
+ _objc_msgSend$containsFrameID:
+ _objc_msgSend$contextIndex
+ _objc_msgSend$copyPathForPersistentData:error:
+ _objc_msgSend$dataLengthFromFormatDescription:
+ _objc_msgSend$dequeue
+ _objc_msgSend$dequeueAllFramesToQueue:
+ _objc_msgSend$dictionaryFromAlgoData:
+ _objc_msgSend$dictionaryFromFrameMetadata:
+ _objc_msgSend$doubleOrder
+ _objc_msgSend$enqueue:
+ _objc_msgSend$faceIDObject
+ _objc_msgSend$formatDescription
+ _objc_msgSend$frameID
+ _objc_msgSend$frameIRSharedMemoryMap
+ _objc_msgSend$frameIRSharedMemoryUnmap
+ _objc_msgSend$frameIdentifier
+ _objc_msgSend$frameRGBSharedMemoryMap
+ _objc_msgSend$frameRGBSharedMemoryUnmap
+ _objc_msgSend$frameType
+ _objc_msgSend$infraredBracketEncryptionConfiguration
+ _objc_msgSend$initWithAVMetadataFaceIDObject:sequenceNumber:cameraID:frameNumber:sessionID:
+ _objc_msgSend$initWithItemLength:capacity:
+ _objc_msgSend$initWithName:capacity:releaseWhenFull:
+ _objc_msgSend$isEmpty
+ _objc_msgSend$isEqualToFrameID:
+ _objc_msgSend$isFaceIDInExclavesEnabled
+ _objc_msgSend$lastAlgoData
+ _objc_msgSend$lastAlgoDataFrameNumber
+ _objc_msgSend$lightSourceProjectorMode
+ _objc_msgSend$loadReferenceFramesInfoRecord
+ _objc_msgSend$loadSummervilleFWCertificate
+ _objc_msgSend$logBracketConfiguration:
+ _objc_msgSend$logFrame:
+ _objc_msgSend$logPasscodeShortcutRequested:
+ _objc_msgSend$metadataFrameProxy
+ _objc_msgSend$metadataLength
+ _objc_msgSend$metadataObjectTypes
+ _objc_msgSend$numberOfDoubles
+ _objc_msgSend$platformHasMirage:
+ _objc_msgSend$platformHasPinnacles
+ _objc_msgSend$portsWithMediaType:sourceDeviceType:sourceDevicePosition:
+ _objc_msgSend$probePatternIndex
+ _objc_msgSend$probePatternType
+ _objc_msgSend$processCoachingStatus:frameType:projectorMode:
+ _objc_msgSend$processFrame:
+ _objc_msgSend$rawDataLength
+ _objc_msgSend$rawFrameProxy
+ _objc_msgSend$referenceDataLength
+ _objc_msgSend$referenceFrameProxy
+ _objc_msgSend$releaseAll
+ _objc_msgSend$releaseCachedMetaData
+ _objc_msgSend$releaseCachedRawData
+ _objc_msgSend$releaseFaceIDObject
+ _objc_msgSend$releaseFrameMessage:
+ _objc_msgSend$releaseFramesFromQueue:toCount:
+ _objc_msgSend$removeFrameID:
+ _objc_msgSend$resetSecureFaceDetectDispatchHandlerBlock
+ _objc_msgSend$retainFaceIDObject
+ _objc_msgSend$returnData:
+ _objc_msgSend$secureFaceDetectRequestDispatchBlock
+ _objc_msgSend$setAttentionRequired:
+ _objc_msgSend$setColorBracketEncryptionConfiguration:
+ _objc_msgSend$setDoubleOrder:
+ _objc_msgSend$setFaceIDConfiguration:
+ _objc_msgSend$setFrameMetadataEnabled:
+ _objc_msgSend$setHostMainKeyIndex:
+ _objc_msgSend$setInfraredBracketEncryptionConfiguration:
+ _objc_msgSend$setInitializationVector:
+ _objc_msgSend$setLastAlgoData:
+ _objc_msgSend$setLastAlgoDataFrameNumber:
+ _objc_msgSend$setLinearFeedbackShiftRegisterSeed:
+ _objc_msgSend$setMode:
+ _objc_msgSend$setNonce:
+ _objc_msgSend$setNumberOfDoubles:
+ _objc_msgSend$setPeriocularEnabled:
+ _objc_msgSend$setProbePatternIndex:
+ _objc_msgSend$setProbePatternType:
+ _objc_msgSend$setRetryType:
+ _objc_msgSend$setSecureFaceDetectRequestDispatchBlock:
+ _objc_msgSend$setTransaction:
+ _objc_msgSend$setUsingExclaves:hasMirage:
+ _objc_msgSend$sharedMemoryAreaOffset
+ _objc_msgSend$stringFromAVFrameType:
+ _objc_msgSend$stringFromAVInfraredLightSourceMode:
+ _objc_msgSend$timestamp
+ _objc_msgSend$transaction
+ _objc_msgSend$updateFrameLoggingState
+ _objc_msgSend$writeQueuedFrame
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _platformHasMirage:.hasMirage
+ _platformHasPinnacles.onceToken
+ _platformHasPinnacles.providesPinnacles
- GCC_except_table100
- GCC_except_table103
- GCC_except_table104
- GCC_except_table105
- GCC_except_table106
- GCC_except_table107
- GCC_except_table110
- GCC_except_table15
- GCC_except_table218
- GCC_except_table228
- GCC_except_table237
- GCC_except_table241
- GCC_except_table244
- GCC_except_table247
- GCC_except_table253
- GCC_except_table254
- GCC_except_table260
- GCC_except_table262
- GCC_except_table263
- GCC_except_table31
- GCC_except_table43
- GCC_except_table44
- GCC_except_table48
- GCC_except_table59
- GCC_except_table76
- _OUTLINED_FUNCTION_59
- _OUTLINED_FUNCTION_60
- ___block_descriptor_56_e8_32s40r_e5_v8?0ls32l8r40l8
- ___block_descriptor_64_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
CStrings:
+ "!(_secureFaceDetectRequestFlags & kSecureFDRequestFlagRGBAssist) || !(_secureFaceDetectRequestFlags & kSecureFDRequestFlagRGBOnly)"
+ "![_frameProcessingQueue containsFrameID:frame.frameID]"
+ "!__os_warn_unused(__builtin_mul_overflow((dimensions.height), (bytesPerRow), (&length)))"
+ "!_cachedMetadata"
+ "!_cachedRawData"
+ "!self->_exclavesIRBufferPort"
+ "!self->_exclavesRGBBufferPort"
+ "%05u-%u-%ld%@-%@-%@"
+ "%@ %@ -(%d)-> %@\n"
+ "%@ --> %@\n"
+ "%@ -> X\n"
+ "%@ ->-> %@\n"
+ "%@ -X-> %@\n"
+ "%@ -X-X (count:%lu)\n"
+ "%@ <-(%d)- %@\n"
+ "%@, cameraID:%u, type:%lu cached after %.1f ms\n"
+ "%@.cachedMetadata == nil\n"
+ "%@.cachedMetadata > %@\n"
+ "%@.cachedRawData == nil\n"
+ "%@.cachedRawData > %@\n"
+ "%@: Cached metadata released\n"
+ "%@: Cached raw data released\n"
+ "%@: FaceID object released\n"
+ "%@: Metadata cached\n"
+ "%@: Raw data cached\n"
+ "(uint8_t)frame.faceIDObject.contextIndex == frame.faceIDObject.contextIndex"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Pearl/BioLog/BLFrameDebugExtraFID.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Pearl/pearld/PearlFrameSupport.m"
+ "/System/Library/Pearl/DCNKernels/DCNKernels_H19_iPhone_Pro.bin"
+ "<%@: %p: %lu/%lu>"
+ "<%@: [%u:%u]>"
+ "A"
+ "AppleCamera"
+ "ApplePearlExclaveSEPDriver"
+ "BioLogFrameQueueCaching"
+ "BioLogFrameQueueWaiting"
+ "BioLogFrameQueueWriting"
+ "Couldn't create OS Log for 'com.apple.BiometricKit.PearlFrameSupport'!\n"
+ "ERROR: Dropping _prevPreCheckFrameID:[%u:%u]!\n"
+ "ERROR: Mismatching _lastPreCheckFrameID:[%u:%u] for sequenceInfo:[%u:*]!\n"
+ "ERROR: exclaves_outbound_buffer_create() -> KERN_DENIED => Check sandbox violation! (sbutil autobox quick-fix)\n"
+ "Empty CEISPLIB_DEBUG_INFO_GRIFFIN_ALGO_BLOB in frameDebug:[%u:%u]!\n"
+ "EnableFaceIDInExclaves"
+ "FIDCDeserializeLogData != ((void*)0)"
+ "Failed to cache frame data! %@\n"
+ "Failed to log frame data! %@\n"
+ "FrameProcessingQueue"
+ "IOClass"
+ "IR stream started\n"
+ "NO _cachedRawData for camera:%u\n"
+ "No CEISPLIB_DEBUG_INFO_GRIFFIN_ALGO_BLOB section in frameDebug:[%u:%u]!\n"
+ "No algo_data from frameDebug:[%u:%lu]!\n"
+ "PearlCoreAnalytics analyzeSecureSequenceFrameMeta\n"
+ "PearlCoreAnalytics analyzeSecureSequenceFrameMeta: Unexpected metaObj.type: %@\n"
+ "PearlFrame::initWithAVMetadataFaceIDObject *-> %@\n"
+ "PearlFrameSupport"
+ "Q"
+ "RCAM"
+ "RGB stream started\n"
+ "Reference frames info record already loaded.\n"
+ "Reference frames info record loaded successfully.\n"
+ "Reference frames info record loading failure (err:0x%x) allowed.\n"
+ "Reference frames info record not found at %@\n"
+ "Reference frames info record not loaded yet. Loading...\n"
+ "Releasing frameId:[%d:%d] (rawFrameProxyId:0x%lx, metaFrameProxyId:0x%lx) fid-griffin-bmk\n"
+ "Skipping projector SN check (not needed)\n"
+ "WARNING: _lastFrameCachingSemaphore timeout!\n"
+ "Yonkers/YonkersPatch.DER"
+ "Yonkers/YonkersPatchBinaryPlusHeader.FW"
+ "YonkersChipID"
+ "YonkersUID"
+ "[_avcSession canAddConnection:connection]"
+ "[_avcSession canAddOutput:_avcRGBOutput]"
+ "[_frameProcessingQueue enqueue:frame]"
+ "[msgData length] >= sizeof(message_release_frame_v1_t)"
+ "[self createFileAtPath:filepath contents:frame.cachedMetadata attributes:_fileAttributesProtected purgeable:__objc_yes]"
+ "[self createFileAtPath:filepath contents:frame.cachedRawData attributes:_fileAttributesProtected purgeable:__objc_yes]"
+ "[self isFaceIDInExclavesEnabled]"
+ "[self loadReferenceFramesInfoRecord] == 0 "
+ "[self platformHasMirage:&hasMirage] == 0 "
+ "[self sendSelfCheckResult:&selfCheckResultCmd] == 0 "
+ "[self sendSensorFWCertCheckResult:(err == 0 ? kBoolTrue : kBoolFalse) withCameraID:kPearlCameraID_RGB] == 0 "
+ "__os_warn_unused(__builtin_add_overflow((_faceIDObject.metadataFrameProxy.sharedMemoryAreaOffset), (_metadataLength), (&endOffset))) == 0 "
+ "__os_warn_unused(__builtin_add_overflow((_faceIDObject.rawFrameProxy.sharedMemoryAreaOffset), (_rawDataLength), (&endOffset))) == 0 "
+ "_array"
+ "_avcHPQueue"
+ "_avcRGBOutput"
+ "_cachedMetadata"
+ "_cachedMetadata.length >= _metadataLength"
+ "_cachedRawData"
+ "_cachedRawData.length >= _rawDataLength"
+ "_cameraID == kPearlCameraID_RGB"
+ "_exclavesIRBufferPort"
+ "_exclavesRGBBufferPort"
+ "_faceIDObject"
+ "_faceIDObjectRetainCount > 0"
+ "_frameDispatchQueueCaching"
+ "_frameMetaCachePool"
+ "_frameProcessingQueue"
+ "_frameQueueCaching"
+ "_frameQueueWaiting"
+ "_frameQueueWriting"
+ "_frameRawIRCachePool"
+ "_frameRawRGBCachePool"
+ "_lastAlgoData"
+ "_metadataLength > 0"
+ "_rawDataLength > 0"
+ "_referenceDataLength > 0"
+ "_remainingBracketIRFrames == 0"
+ "_remainingBracketRGBFrames == 0"
+ "_secureFaceDetectRequest == kSecureFDRequestEnroll || _secureFaceDetectRequest == kSecureFDRequestMatch"
+ "_secureFaceDetectRequest == kSecureFDRequestMatch"
+ "algo_data"
+ "algo_data_frame_number"
+ "avcWorkloop"
+ "baseFilename"
+ "bracket"
+ "bracket_config"
+ "bracket_frame_count"
+ "bytesPerRow > 0"
+ "cacheMetadataWithPool: exclaves_outbound_buffer_copyout(length:%u, offset:%lu)\n"
+ "cacheRawDataWithPool: exclaves_outbound_buffer_copyout(length:%u, offset:%lu)\n"
+ "cached"
+ "captureSecureFaceDetectRequestDispatchBlock -> %@\n"
+ "cfg.colorBracketEncryptionConfiguration"
+ "cfg.infraredBracketEncryptionConfiguration"
+ "clearing retained 'CameraObstructed' feedback\n"
+ "coachingStatus: 0x%lx\n"
+ "com.apple.BioLog.frameDataCaching"
+ "com.apple.biometrickitd.SharedMemIR"
+ "com.apple.biometrickitd.SharedMemRGB"
+ "com.apple.pearld.avcHP"
+ "com.apple.pearld.avcworkloop"
+ "configuration"
+ "connection"
+ "context_index"
+ "data.length"
+ "dataInstance"
+ "dbgInfoGriffinAlgoBlob->size <= sizeof(dbgInfoGriffinAlgoBlob->data)"
+ "dcnKernelsFilename"
+ "dimensions.height > 0"
+ "double_order"
+ "endOffset <= kExclavesIRBufferSize"
+ "endOffset <= kExclavesRGBBufferSize"
+ "eventEngagementInfoStruct"
+ "faceIDObject"
+ "face_id"
+ "face_id_count"
+ "fidLogPtr - data.bytes + fidLogSize <= data.length"
+ "fidLogPtr >= data.bytes"
+ "flood"
+ "formatDescription"
+ "frame.cameraID == kPearlCameraID_IR || (frame.cameraID == kPearlCameraID_RGB && (_secureFaceDetectRequestFlags & kSecureFDRequestFlagRGBAssist))"
+ "frame.cameraID == kPearlCameraID_RGB"
+ "frame.frameID.sequenceNumber == secureSequenceId.number"
+ "frameDataLength"
+ "frameDict[@\"face_id\"] == ((void *)0)"
+ "frame_count"
+ "frame_type"
+ "hasMirageOut"
+ "has_mirage"
+ "ir_frame_count"
+ "kBioLogFrameIRCachingCapacity:%lu reached! %@ dropped\n"
+ "kBioLogFrameRGBCachingCapacity:%lu reached! %@ dropped\n"
+ "light_source_projector_mode"
+ "loadReferenceFramesInfoRecord\n"
+ "loadReferenceFramesInfoRecord -> 0x%x\n"
+ "loadSummervilleFWCertificate\n"
+ "loadSummervilleFWCertificate -> 0x%x\n"
+ "mAmbient"
+ "mDot"
+ "mFlood"
+ "mach_port_deallocate(mach_task_self_, self->_exclavesIRBufferPort) == 0 "
+ "mach_port_deallocate(mach_task_self_, self->_exclavesRGBBufferPort) == 0 "
+ "message->data.captureBracket.eisplibAlgoType != kEisplibAlgoUninitialized"
+ "message->data.captureBracket.streamingSessionData.valid"
+ "message->sessionID == _secureFaceDetectSessionID"
+ "name"
+ "number_of_doubles"
+ "outDataSize == sizeof(outData)"
+ "passcode_shortcut_requested"
+ "pbsc"
+ "port"
+ "precheck_algo_data"
+ "precheck_algo_data_frame_number"
+ "probe_pattern_index"
+ "probe_pattern_type"
+ "processCoachingStatus: retaining faceDetectFeedback = %u\n"
+ "processFrame: bracket frame frameId:[%d:%d] skipped (isRGB:%u, remainingBracketIRFrames:%u, remainingBracketRGBFrames:%u, rawFrameProxyId:0x%lx, metaFrameProxyId:0x%lx) fid-griffin-bmk\n"
+ "processFrame: frameId:[%d:%d] processing (isBracket:%u, isRGB:%u, rawFrameProxyId:0x%lx, metaFrameProxyId:0x%lx) fid-griffin-bmk\n"
+ "processSecureFaceDetectRequestMessage: captureBracket: numOfDoubles:%u, doubleOrder:%u, probePatternType:%u, probePatternIndex:%u, eisplibAlgoType:%u, sessionData:%u\n"
+ "processSecureFaceDetectRequestMessage: pause\n"
+ "processSecureFaceDetectRequestMessage: session will restart after stopping\n"
+ "rawDataLength"
+ "refFramesInfoRecordData"
+ "refFramesInfoRecordData.length"
+ "refFramesInfoRecordFile"
+ "refFramesPath"
+ "reference-info-record.DAT"
+ "releaseFrameMessage: frameId:[%d:%d]\n"
+ "requestData"
+ "resetSecureFaceDetectRequestDispatchBlock: %@\n"
+ "rgb_assist"
+ "rgb_frame_count"
+ "sSparse"
+ "sSparseLP"
+ "secure_face_id"
+ "self->_exclavesIRBufferPort"
+ "sending MatchRequestedPasscodeShortcut: reason=%u\n\n"
+ "seqDict"
+ "serviceMatch: _usingExclaveDriver:%u\n"
+ "setSecureFaceDetectRequestDispatchBlock: %@\n"
+ "stream"
+ "unknown"
+ "updateFrameLoggingState: _frameLoggingEnabled:%d\n"
+ "ycrt"
- "!"
```
