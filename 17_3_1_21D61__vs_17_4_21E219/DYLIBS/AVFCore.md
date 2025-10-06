## AVFCore

> `/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`

```diff

-2225.4.2.0.0
-  __TEXT.__text: 0x18d3c8
-  __TEXT.__auth_stubs: 0x3200
-  __TEXT.__objc_methlist: 0x18300
-  __TEXT.__cstring: 0x223d8
+2230.19.1.0.0
+  __TEXT.__text: 0x18e86c
+  __TEXT.__auth_stubs: 0x3220
+  __TEXT.__objc_methlist: 0x183f0
+  __TEXT.__cstring: 0x225a9
   __TEXT.__const: 0x1e8
-  __TEXT.__gcc_except_tab: 0x40b0
-  __TEXT.__oslogstring: 0x75e2
+  __TEXT.__gcc_except_tab: 0x40f0
+  __TEXT.__oslogstring: 0x771f
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x7fb0
-  __TEXT.__objc_classname: 0x5a2f
-  __TEXT.__objc_methname: 0x303bc
-  __TEXT.__objc_methtype: 0x98e8
-  __TEXT.__objc_stubs: 0x1dba0
-  __DATA_CONST.__got: 0x3a98
-  __DATA_CONST.__const: 0x5260
+  __TEXT.__unwind_info: 0x8020
+  __TEXT.__objc_classname: 0x5a81
+  __TEXT.__objc_methname: 0x306f4
+  __TEXT.__objc_methtype: 0x9977
+  __TEXT.__objc_stubs: 0x1dd40
+  __DATA_CONST.__got: 0x3ab8
+  __DATA_CONST.__const: 0x52c0
   __DATA_CONST.__objc_classlist: 0x1008
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x25570
-  __DATA_CONST.__objc_selrefs: 0x98b8
+  __DATA_CONST.__objc_const: 0x25730
+  __DATA_CONST.__objc_selrefs: 0x9938
+  __DATA_CONST.__objc_protorefs: 0x48
+  __DATA_CONST.__objc_classrefs: 0x1140
+  __DATA_CONST.__objc_superrefs: 0xb30
   __DATA_CONST.__objc_arraydata: 0x1d0
   __AUTH_CONST.__objc_const: 0xa670
-  __AUTH_CONST.__cfstring: 0x16340
-  __AUTH_CONST.__const: 0xc38
+  __AUTH_CONST.__cfstring: 0x163e0
+  __AUTH_CONST.__const: 0xc68
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_arrayobj: 0x258
-  __AUTH_CONST.__auth_got: 0x1910
+  __AUTH_CONST.__auth_got: 0x1920
   __AUTH.__objc_data: 0x62c0
   __AUTH.__data: 0x138
-  __DATA.__objc_protorefs: 0x48
-  __DATA.__objc_classrefs: 0x1140
-  __DATA.__objc_superrefs: 0xb30
-  __DATA.__objc_ivar: 0x213c
-  __DATA.__data: 0x1db8
+  __DATA.__objc_ivar: 0x215c
+  __DATA.__data: 0x1dc8
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x1a8
-  __DATA.__common: 0x60
+  __DATA.__bss: 0x198
+  __DATA.__common: 0x80
   __DATA_DIRTY.__objc_data: 0x3d90
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x1a1

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A8918968-F4BB-37EE-A142-5C27A8BB8B31
-  Functions: 10010
-  Symbols:   35101
-  CStrings:  15269
+  UUID: 2BC4F294-28AE-3EA2-91D0-7FF1119023CC
+  Functions: 10038
+  Symbols:   35193
+  CStrings:  15320
 
Symbols:
+ +[AVContentKey contentKeyWithSpecifier:cryptor:contentKeyBoss:contentKeySpecifier:]
+ -[AVAssetDownloadSession(AVAssetDownloadSession_Local) _createDuplicateFigAssetFromAVAsset:options:]
+ -[AVAssetDownloadSession(AVAssetDownloadSession_Local) _setFileFigAsset:options:]
+ -[AVAssetReader initWithAsset:options:error:]
+ -[AVAssetWriterWritingHelper checkAVAssetWriterInputConfigurationToOutputSegmentDataForFragmentedMPEG4FileTypeProfile:preferredOutputSegmentInterval:returningDebugDescription:]
+ -[AVContentKey _internalContentKeySpecifier]
+ -[AVContentKey externalContentProtectionStatus]
+ -[AVContentKey initWithSpecifier:cryptor:contentKeyBoss:contentKeySpecifier:]
+ -[AVContentKey revoke]
+ -[AVContentKeySession(FigContentKeyBoss) _processContentKeyRequestWithIdentifier:encryptionMode:supportedProtocolVersions:options:groupID:error:]
+ -[AVFigEndpointOutputDeviceImpl setMediaRemoteData:completionHandler:]
+ -[AVFigRouteDescriptorOutputDeviceImpl setMediaRemoteData:completionHandler:]
+ -[AVLocalOutputDeviceImpl setMediaRemoteData:completionHandler:]
+ -[AVOutputDevice setMediaRemoteData:completionHandler:]
+ -[AVSampleBufferDisplayLayer isReadyForDisplay]
+ -[AVSampleBufferVideoRenderer isReadyForDisplay]
+ -[AVSampleBufferVideoRenderer removeDisplayLayer]
+ -[AVSampleBufferVideoRenderer setReadyForDisplayWithoutKVO:]
+ -[AVSampleBufferVideoRenderer(AVSampleBufferVideoRendererVideoPerformanceMetrics) loadVideoPerformanceMetricsWithCompletionHandler:]
+ -[AVSampleBufferVideoRenderer(VideoPerformanceMetricsPrivate) videoPerformanceMetrics]
+ -[AVURLAsset allowsConstrainedNetworkAccess]
+ -[AVURLAsset allowsExpensiveNetworkAccess]
+ -[AVURLAsset recommendedDestinationURLPathExtension]
+ -[AVVideoPerformanceMetrics numberOfCorruptedFrames]
+ -[AVVideoPerformanceMetrics numberOfDroppedFrames]
+ -[AVVideoPerformanceMetrics numberOfFramesDisplayedUsingOptimizedCompositing]
+ -[AVVideoPerformanceMetrics totalAccumulatedFrameDelay]
+ -[AVVideoPerformanceMetrics totalNumberOfFrames]
+ GCC_except_table100
+ GCC_except_table127
+ GCC_except_table145
+ GCC_except_table150
+ GCC_except_table173
+ GCC_except_table183
+ GCC_except_table244
+ GCC_except_table70
+ GCC_except_table87
+ _AVAssetReaderCreationOptionPermitNonLocalURLKey
+ _AVOutputDeviceSetMediaRemoteDataOnEndpoint
+ _AVSampleBufferDisplayLayerReadyForDisplayDidChangeNotification
+ _FigIsSecTaskGPUExtensionOfBrowserEngine
+ _FigPlayerInterstitialEventGetPrimaryItem
+ _OBJC_IVAR_$_AVContentKey._contentKeySpecifier
+ _OBJC_IVAR_$_AVContentKey._keyBoss
+ _OBJC_IVAR_$_AVContentKeySessionInternal.contentKeyByKeySpecifierMap
+ _OBJC_IVAR_$_AVHUDStringGenerator._startupTime
+ _OBJC_IVAR_$_AVSampleBufferVideoRenderer._readyForDisplay
+ _OBJC_IVAR_$_AVSampleBufferVideoRenderer._videoPerformanceMetricsQueue
+ _OBJC_IVAR_$_AVURLAssetInternal.allowsConstrainedNetworkAccess
+ _OBJC_IVAR_$_AVURLAssetInternal.allowsExpensiveNetworkAccess
+ __OBJC_$_CLASS_METHODS_AVSampleBufferVideoRenderer(VideoPerformanceMetricsPrivate|AVSampleBufferVideoRendererVideoPerformanceMetrics|AVSampleBufferVideoRendererProtectedContent|AVSampleBufferVideoRendererImageProtection|AVSampleBufferVideoRendererVideoDisplaySleepPrevention|AVSampleBufferVideoRendererAutomaticBackgroundPrevention|AVSampleBufferVideoRendererDisplayCompositing|PowerOptimization|AVSampleBufferVideoRendererOutputs)
+ __OBJC_$_INSTANCE_METHODS_AVSampleBufferVideoRenderer(VideoPerformanceMetricsPrivate|AVSampleBufferVideoRendererVideoPerformanceMetrics|AVSampleBufferVideoRendererProtectedContent|AVSampleBufferVideoRendererImageProtection|AVSampleBufferVideoRendererVideoDisplaySleepPrevention|AVSampleBufferVideoRendererAutomaticBackgroundPrevention|AVSampleBufferVideoRendererDisplayCompositing|PowerOptimization|AVSampleBufferVideoRendererOutputs)
+ __OBJC_$_PROP_LIST_AVVideoCompositionInstruction.193
+ ___132-[AVSampleBufferVideoRenderer(AVSampleBufferVideoRendererVideoPerformanceMetrics) loadVideoPerformanceMetricsWithCompletionHandler:]_block_invoke
+ ___48-[AVSampleBufferVideoRenderer isReadyForDisplay]_block_invoke
+ ___49-[AVSampleBufferVideoRenderer removeDisplayLayer]_block_invoke
+ ___60-[AVSampleBufferVideoRenderer setReadyForDisplayWithoutKVO:]_block_invoke
+ ___77-[AVFigRouteDescriptorOutputDeviceImpl setMediaRemoteData:completionHandler:]_block_invoke
+ ___86-[AVSampleBufferVideoRenderer(VideoPerformanceMetricsPrivate) videoPerformanceMetrics]_block_invoke
+ ___AVOutputDeviceSetMediaRemoteDataOnEndpoint_block_invoke
+ ___Block_byref_object_copy_.91
+ ___Block_byref_object_dispose_.92
+ ___block_descriptor_40_e8_32b_e8_v12?0i8ls32l8
+ ___block_descriptor_49_e8_32o40r_e5_v8?0lr40l8s32l8
+ ___block_literal_global.1039
+ ___block_literal_global.1041
+ ___block_literal_global.1240
+ ___block_literal_global.133
+ ___block_literal_global.194
+ ___block_literal_global.197
+ ___block_literal_global.282
+ ___block_literal_global.333
+ ___block_literal_global.338
+ ___block_literal_global.341
+ ___block_literal_global.369
+ ___block_literal_global.379
+ ___block_literal_global.393
+ ___block_literal_global.406
+ ___block_literal_global.410
+ ___block_literal_global.474
+ ___block_literal_global.626
+ ___block_literal_global.728
+ ___block_literal_global.863
+ ___clientCanDecryptContentKey_block_invoke
+ ___handleFigAssetLoadingNotification_block_invoke.529
+ __figVideoQueueFirstVideoFrameEnqueued
+ __unnamed_array_storage.183
+ __unnamed_array_storage.358
+ __unnamed_array_storage.446
+ __unnamed_array_storage.509
+ __unnamed_array_storage.515
+ __unnamed_array_storage.536
+ __unnamed_array_storage.548
+ __unnamed_array_storage.594
+ _clientCanDecryptContentKey.browserEngineAllowedToDecrypt
+ _clientCanDecryptContentKey.getBrowserEngineOnce
+ _gAVUXMDisplayManager
+ _initWithFigAsset:.sAVAssetCustomURLCallbacksForNSURLSession.220
+ _kFigEndpointRemoteControlSessionCreationOption_ClientTypeUUID
+ _kFigEndpointRemoteControlSessionCreationOption_SessionType
+ _kFigEndpointSendCommand_CommandType_SetMRInfo
+ _kFigEndpointSendCommand_Param_MRInfo
+ _kFigPlaybackItemProperty_AssetDownloadedImageData
+ _kFigPlaybackItemProperty_AssetDownloadedName
+ _kFigPlayerOptionKey_AllowVideoRenderingIfSendingVisualsToNero
+ _kFigVideoQueueNotification_FirstVideoFrameEnqueued
+ _objc_msgSend$_createDuplicateFigAssetFromAVAsset:options:
+ _objc_msgSend$_internalContentKeySpecifier
+ _objc_msgSend$_processContentKeyRequestWithIdentifier:encryptionMode:supportedProtocolVersions:options:groupID:error:
+ _objc_msgSend$_setFileFigAsset:options:
+ _objc_msgSend$checkAVAssetWriterInputConfigurationToOutputSegmentDataForFragmentedMPEG4FileTypeProfile:preferredOutputSegmentInterval:returningDebugDescription:
+ _objc_msgSend$contentKeySession:externalProtectionStatusDidChangeForContentKey:
+ _objc_msgSend$initWithAsset:options:error:
+ _objc_msgSend$initWithSpecifier:cryptor:contentKeyBoss:contentKeySpecifier:
+ _objc_msgSend$numberOfCorruptedFrames
+ _objc_msgSend$numberOfDisplayCompositedVideoFrames
+ _objc_msgSend$numberOfDroppedFrames
+ _objc_msgSend$removeDisplayLayer
+ _objc_msgSend$setMediaRemoteData:completionHandler:
+ _objc_msgSend$setReadyForDisplayWithoutKVO:
+ _objc_msgSend$startupTime
+ _objc_msgSend$totalFrameDelay
+ _objc_msgSend$totalNumberOfFrames
+ _objc_msgSend$typeWithTag:tagClass:conformingToType:
- +[AVContentKey contentKeyWithSpecifier:andCryptor:]
- -[AVAssetDownloadSession(AVAssetDownloadSession_Local) _createDuplicateFigAssetFromAVAsset:]
- -[AVAssetDownloadSession(AVAssetDownloadSession_Local) _setFileFigAsset:]
- -[AVAssetWriterWritingHelper checkAVAssetWriterInputConfigurationToOutputSegmentDataForOutputFileTypeProfile:preferredOutputSegmentInterval:returningDebugDescription:]
- -[AVContentKey initWithSpecifier:andCryptor:]
- -[AVContentKeySession(FigContentKeyBoss) _processContentKeyRequestWithIdentifier:encryptionMode:supportedProtocolVersions:groupID:error:]
- -[AVPlayerItemErrorLogEvent allHTTPResponseHeaderFields]
- -[AVSampleBufferVideoRenderer(VideoPerformanceMetrics) videoPerformanceMetrics]
- GCC_except_table116
- GCC_except_table119
- GCC_except_table121
- GCC_except_table147
- GCC_except_table156
- GCC_except_table163
- GCC_except_table169
- GCC_except_table241
- _AVSampleBufferAttachContentKey.authorizedToDecrypt
- _AVSampleBufferAttachContentKey.getAuthorizedToDecryptBooleanOnce
- __OBJC_$_CLASS_METHODS_AVSampleBufferVideoRenderer(VideoPerformanceMetrics|AVSampleBufferVideoRendererProtectedContent|AVSampleBufferVideoRendererImageProtection|AVSampleBufferVideoRendererVideoDisplaySleepPrevention|AVSampleBufferVideoRendererAutomaticBackgroundPrevention|AVSampleBufferVideoRendererDisplayCompositing|PowerOptimization|AVSampleBufferVideoRendererOutputs)
- __OBJC_$_INSTANCE_METHODS_AVSampleBufferVideoRenderer(VideoPerformanceMetrics|AVSampleBufferVideoRendererProtectedContent|AVSampleBufferVideoRendererImageProtection|AVSampleBufferVideoRendererVideoDisplaySleepPrevention|AVSampleBufferVideoRendererAutomaticBackgroundPrevention|AVSampleBufferVideoRendererDisplayCompositing|PowerOptimization|AVSampleBufferVideoRendererOutputs)
- __OBJC_$_PROP_LIST_AVVideoCompositionInstruction.191
- ___79-[AVSampleBufferVideoRenderer(VideoPerformanceMetrics) videoPerformanceMetrics]_block_invoke
- ___AVSampleBufferAttachContentKey_block_invoke
- ___Block_byref_object_copy_.89
- ___Block_byref_object_dispose_.90
- ___block_literal_global.1032
- ___block_literal_global.1034
- ___block_literal_global.1239
- ___block_literal_global.132
- ___block_literal_global.193
- ___block_literal_global.196
- ___block_literal_global.281
- ___block_literal_global.330
- ___block_literal_global.337
- ___block_literal_global.340
- ___block_literal_global.368
- ___block_literal_global.378
- ___block_literal_global.392
- ___block_literal_global.405
- ___block_literal_global.473
- ___block_literal_global.529
- ___block_literal_global.623
- ___block_literal_global.725
- ___block_literal_global.856
- ___handleFigAssetLoadingNotification_block_invoke.526
- __unnamed_array_storage.181
- __unnamed_array_storage.353
- __unnamed_array_storage.443
- __unnamed_array_storage.503
- __unnamed_array_storage.512
- __unnamed_array_storage.533
- __unnamed_array_storage.545
- __unnamed_array_storage.591
- _initWithFigAsset:.sAVAssetCustomURLCallbacksForNSURLSession.219
- _kFigEndpointRemoteControlSessionClientTypeUUIDKey
- _kFigEndpointRemoteControlSessionKey_SessionType
- _kFigErrorLogKey_AllHTTPResponseHeaderFields
- _objc_msgSend$_createDuplicateFigAssetFromAVAsset:
- _objc_msgSend$_processContentKeyRequestWithIdentifier:encryptionMode:supportedProtocolVersions:groupID:error:
- _objc_msgSend$_setFileFigAsset:
- _objc_msgSend$checkAVAssetWriterInputConfigurationToOutputSegmentDataForOutputFileTypeProfile:preferredOutputSegmentInterval:returningDebugDescription:
- _objc_msgSend$initWithSpecifier:andCryptor:
CStrings:
+ "-[AVSampleBufferVideoRenderer setReadyForDisplayWithoutKVO:]"
+ "-[AVUXMDisplayManager setPreferredDisplayCriteria:]_block_invoke"
+ "<<<< AVOutputDevice (FigEndpoint) >>>> %s: Sending %{public}@ command"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] Received first video frame enqueued notification"
+ "<<<< AVSampleBufferVideoRenderer >>>> %s: [%p] setting readyForDisplay to %@"
+ "<<<< AVUXMDisplayManager >>>> %s: <%p> preferredDisplayCriteria set to %p"
+ "@48@0:8@16^{OpaqueFigCPECryptor=}24^{CMBaseObject=}32^{FigContentKeySpecifier=}40"
+ "AVAssetWriter does not supports file type %@ if the delegate method to output segment data is implemented."
+ "AVOutputDeviceSetMediaRemoteDataOnEndpoint"
+ "AVSampleBufferDisplayLayerReadyForDisplayDidChangeNotification"
+ "AVSampleBufferVideoRenderer videoPerformanceMetricsQueue"
+ "AVSampleBufferVideoRendererVideoPerformanceMetrics"
+ "AssetReaderOption_PermitNonLocalURL"
+ "A\xe1\xf0\x11"
+ "Q60@0:8@16i24@28@36Q44^@52"
+ "T@\"NSArray\",?,R,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,N"
+ "T@\"NSString\",?,R,N,V_modelID"
+ "TB,?,R,N"
+ "TB,?,R,N,V_isClusterLeader"
+ "Tq,?,R,N"
+ "Tq,?,R,N,V_deviceSubType"
+ "Tq,?,R,N,V_deviceType"
+ "VideoPerformanceMetricsPrivate"
+ "^{FigContentKeySpecifier=}16@0:8"
+ "^{OpaqueFigAsset=}32@0:8@16@24"
+ "_contentKeySpecifier"
+ "_createDuplicateFigAssetFromAVAsset:options:"
+ "_figVideoQueueFirstVideoFrameEnqueued"
+ "_internalContentKeySpecifier"
+ "_keyBoss"
+ "_processContentKeyRequestWithIdentifier:encryptionMode:supportedProtocolVersions:options:groupID:error:"
+ "_readyForDisplay"
+ "_setFileFigAsset:options:"
+ "_startupTime"
+ "_videoPerformanceMetricsQueue"
+ "allowsConstrainedNetworkAccess"
+ "allowsExpensiveNetworkAccess"
+ "avuxm_trace"
+ "checkAVAssetWriterInputConfigurationToOutputSegmentDataForFragmentedMPEG4FileTypeProfile:preferredOutputSegmentInterval:returningDebugDescription:"
+ "com.apple.private.coremedia.allow-fps-attachment"
+ "contentKeyByKeySpecifierMap"
+ "contentKeySession:externalProtectionStatusDidChangeForContentKey:"
+ "contentKeyWithSpecifier:cryptor:contentKeyBoss:contentKeySpecifier:"
+ "description=AVFoundation_AVFCore-2230.19.1"
+ "i32@0:8^{OpaqueFigAsset=}16@24"
+ "initWithAsset:options:error:"
+ "initWithSpecifier:cryptor:contentKeyBoss:contentKeySpecifier:"
+ "loadVideoPerformanceMetricsWithCompletionHandler:"
+ "movpkg"
+ "numberOfCorruptedFrames"
+ "numberOfDroppedFrames"
+ "numberOfFramesDisplayedUsingOptimizedCompositing"
+ "recommendedDestinationURLPathExtension"
+ "removeDisplayLayer"
+ "revoke"
+ "setMediaRemoteData:completionHandler:"
+ "setReadyForDisplayWithoutKVO:"
+ "startupTime:%fs"
+ "totalAccumulatedFrameDelay"
+ "totalNumberOfFrames"
+ "typeWithTag:tagClass:conformingToType:"
+ "v40@0:8@\"AVContentKeySession\"16@\"NSArray\"24@\"NSData\"32"
- "@32@0:8@16^{OpaqueFigCPECryptor=}24"
- "A\xd1\xf0\x11"
- "Q52@0:8@16i24@28Q36^@44"
- "T@\"NSString\",R,N,V_modelID"
- "TB,R,N,V_isClusterLeader"
- "The value of the outputFileType must be AVFileTypeMPEG4 for file type profile %@."
- "Tq,R,N,V_deviceSubType"
- "Tq,R,N,V_deviceType"
- "^{OpaqueFigAsset=}24@0:8@16"
- "_createDuplicateFigAssetFromAVAsset:"
- "_processContentKeyRequestWithIdentifier:encryptionMode:supportedProtocolVersions:groupID:error:"
- "_setFileFigAsset:"
- "allHTTPResponseHeaderFields"
- "checkAVAssetWriterInputConfigurationToOutputSegmentDataForOutputFileTypeProfile:preferredOutputSegmentInterval:returningDebugDescription:"
- "contentKeyWithSpecifier:andCryptor:"
- "description=AVFoundation_AVFCore-2225.4.2"
- "i24@0:8^{OpaqueFigAsset=}16"
- "initWithSpecifier:andCryptor:"
- "sample buffer does not have format description"

```
