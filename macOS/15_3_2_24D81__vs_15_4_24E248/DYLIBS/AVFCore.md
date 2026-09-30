## AVFCore

> `/System/Library/PrivateFrameworks/AVFCore.framework/Versions/A/AVFCore`

```diff

-2315.5.1.0.0
-  __TEXT.__text: 0x1c0214
+2320.19.1.0.0
+  __TEXT.__text: 0x1b7298
   __TEXT.__auth_stubs: 0x36b0
-  __TEXT.__objc_methlist: 0x1c100
+  __TEXT.__objc_methlist: 0x1d6a4
   __TEXT.__const: 0x268
-  __TEXT.__gcc_except_tab: 0x4530
-  __TEXT.__cstring: 0x27576
-  __TEXT.__oslogstring: 0x7923
+  __TEXT.__gcc_except_tab: 0x456c
+  __TEXT.__cstring: 0x27703
+  __TEXT.__oslogstring: 0x77dc
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x8e88
-  __TEXT.__objc_classname: 0x6743
-  __TEXT.__objc_methname: 0x36e1a
-  __TEXT.__objc_methtype: 0xaf22
-  __TEXT.__objc_stubs: 0x20ba0
-  __DATA_CONST.__got: 0x4be0
-  __DATA_CONST.__const: 0x34d0
+  __TEXT.__unwind_info: 0x8fe0
+  __TEXT.__objc_classname: 0x6770
+  __TEXT.__objc_methname: 0x37081
+  __TEXT.__objc_methtype: 0xaf6e
+  __TEXT.__objc_stubs: 0x20ca0
+  __DATA_CONST.__got: 0x4c40
+  __DATA_CONST.__const: 0x3530
   __DATA_CONST.__objc_classlist: 0x1310
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xac80
+  __DATA_CONST.__objc_selrefs: 0xada8
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0xdd8
   __DATA_CONST.__objc_arraydata: 0x270
   __AUTH_CONST.__auth_got: 0x1b68
-  __AUTH_CONST.__const: 0x3a40
-  __AUTH_CONST.__cfstring: 0x19b60
-  __AUTH_CONST.__objc_const: 0x377a0
+  __AUTH_CONST.__const: 0x3a60
+  __AUTH_CONST.__cfstring: 0x19d60
+  __AUTH_CONST.__objc_const: 0x35340
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x2d0
   __AUTH.__objc_data: 0x27b0
   __AUTH.__data: 0x88
-  __DATA.__objc_ivar: 0x25ec
-  __DATA.__data: 0x1bb0
+  __DATA.__objc_ivar: 0x2604
+  __DATA.__data: 0x1bc0
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x420
+  __DATA.__bss: 0x430
   __DATA.__common: 0x300
   __DATA_DIRTY.__objc_data: 0x96f0
   __DATA_DIRTY.__data: 0xb8

   - /System/Library/PrivateFrameworks/MediaExperience.framework/Versions/A/MediaExperience
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 58DD74B3-23A8-3FE2-82DF-C393C75F4926
-  Functions: 11411
-  Symbols:   28454
-  CStrings:  17458
+  UUID: 16054380-857B-34AD-87A3-148D0EDAAEF4
+  Functions: 11688
+  Symbols:   28880
+  CStrings:  17501
 
Symbols:
+ +[AVApplicationStateMonitor sharedApplicationStateMonitor].cold.1
+ +[AVAssetTrack mediaCharacteristicsForMediaTypes].cold.1
+ +[AVCaptionRegion appleiTTBottom].cold.1
+ +[AVCaptionRegion appleiTTLeft].cold.1
+ +[AVCaptionRegion appleiTTRight].cold.1
+ +[AVCaptionRegion appleiTTTop].cold.1
+ +[AVCaptionRegion subRipTextBottom].cold.1
+ +[AVContentKeySession(AVContentKeySessionPendingExpiredSessionReports) pendingExpiredSessionReportsWithAppIdentifier:storageDirectoryAtURL:].cold.1
+ +[AVContentKeySession(AVContentKeySessionPendingExpiredSessionReports) removePendingExpiredSessionReports:withAppIdentifier:storageDirectoryAtURL:].cold.1
+ +[AVExecutionEnvironment sharedExecutionEnvironment].cold.1
+ +[AVFigAssetInspectorLoader _figAssetMediaSelectionPropertiesArray].cold.1
+ +[AVFigAssetInspectorLoader _figAssetPropertiesForKeys].cold.1
+ +[AVFigAssetInspectorLoader _figAssetTrackMediaSelectionPropertiesArray].cold.1
+ +[AVFigAssetInspectorLoader _figAssetTrackPropertiesForKeys].cold.1
+ +[AVFigEndpointUIAgentOutputContextManagerImpl copySharedEndpointUIAgent].cold.1
+ +[AVGlobalOperationQueue defaultQueue].cold.1
+ +[AVKVODispatcher sharedKVODispatcher].cold.1
+ +[AVMetadataItem _isoUserDataKeysRequiringKeySpaceConversion].cold.1
+ +[AVMetadataItemFilter metadataItemFilterForSharing].cold.1
+ +[AVMovie movieTypes].cold.1
+ +[AVOutputContextManager outputContextManagerForAllOutputContexts].cold.1
+ +[AVOutputDeviceAuthorizationSession sharedAuthorizationSession].cold.1
+ +[AVOutputDeviceFrecencyManager _frecentsReaderAfterMigrationIfNecessary].cold.1
+ +[AVOutputDeviceFrecencyManager _frecentsReaderAfterMigrationIfNecessary].cold.2
+ +[AVOutputDeviceFrecencyManager _frecentsWriter].cold.1
+ +[AVPlayer _createFigPlayerWithType:options:player:].cold.1
+ +[AVSampleBufferGenerator notifyOfDataReadyForSampleBuffer:completionHandler:].cold.1
+ +[AVStreamDataParser audiovisualMIMETypes].cold.1
+ +[AVStreamSession(AVStreamSession_PendingExpiredSessionReports) pendingExpiredSessionReportsWithAppIdentifier:].cold.1
+ +[AVStreamSession(AVStreamSession_PendingExpiredSessionReports) pendingExpiredSessionReportsWithAppIdentifier:storageDirectoryAtURL:].cold.1
+ +[AVURLAsset _UTTypes].cold.1
+ +[AVURLAsset _UTTypes].cold.2
+ +[AVURLAsset _UTTypes].cold.3
+ +[AVURLAsset _avfValidationPlist].cold.1
+ +[AVURLAsset _figMIMETypes].cold.1
+ +[AVURLAsset _figMIMETypes].cold.2
+ +[AVURLAsset _figMIMETypes].cold.3
+ +[AVURLAsset _fileUTTypes].cold.1
+ +[AVURLAsset _fileUTTypes].cold.2
+ +[AVURLAsset _fileUTTypes].cold.3
+ +[AVURLAsset _getFigAssetiTunesStoreContentInfoFromURLAssetiTunesStoreContentInfo:]
+ +[AVURLAsset _initializationOptionsClasses].cold.1
+ +[AVURLAsset _streamingUTTypes].cold.1
+ +[AVURLAsset _streamingUTTypes].cold.2
+ +[AVURLAsset _streamingUTTypes].cold.3
+ +[AVURLAsset(AVURLAssetInstanceIdentiferMapping) instanceIdentifierMapTable].cold.1
+ +[AVVideoCompositionRenderContext(Internal) renderContextPropertiesFromFigCompositor:].cold.1
+ -[AVAnnotation initWithJSONData:representationBinaryDataBindings:error:].cold.1
+ -[AVAnnotation initWithJSONData:representationBinaryDataBindings:error:].cold.10
+ -[AVAnnotation initWithJSONData:representationBinaryDataBindings:error:].cold.11
+ -[AVAnnotation initWithJSONData:representationBinaryDataBindings:error:].cold.12
+ -[AVAnnotation initWithJSONData:representationBinaryDataBindings:error:].cold.13
+ -[AVAnnotation initWithJSONData:representationBinaryDataBindings:error:].cold.2
+ -[AVAnnotation initWithJSONData:representationBinaryDataBindings:error:].cold.3
+ -[AVAnnotation initWithJSONData:representationBinaryDataBindings:error:].cold.4
+ -[AVAnnotation initWithJSONData:representationBinaryDataBindings:error:].cold.5
+ -[AVAnnotation initWithJSONData:representationBinaryDataBindings:error:].cold.6
+ -[AVAnnotation initWithJSONData:representationBinaryDataBindings:error:].cold.7
+ -[AVAnnotation initWithJSONData:representationBinaryDataBindings:error:].cold.8
+ -[AVAnnotation initWithJSONData:representationBinaryDataBindings:error:].cold.9
+ -[AVAssetAnalysisTextParsingMessage description].cold.1
+ -[AVAssetCustomURLAuthentication _handleAuthChallenge:requestID:canHandleRequestOut:].cold.1
+ -[AVAssetDownloadConfiguration setInterstitialMediaSelectionCriteria:forMediaCharacteristic:]
+ -[AVAssetDownloadSession(AVAssetDownloadSession_Local) _startOnQueue].cold.1
+ -[AVAssetImageGenerator _invalidated]
+ -[AVAssetImageGenerator status]
+ -[AVAssetMakeReadyForInspectionLoader _dictionaryOfSpecialLoadingMethodsForKeys].cold.1
+ -[AVAssetReaderOutput _attachToWeakReferenceToAssetReader:].cold.1
+ -[AVAssetResourceLoader initWithURLRequestHelper:asset:remoteCustomURLHandlerContext:].cold.1
+ -[AVAssetResourceLoader(AVAssetResourceLoaderURLAuthenticationChallengeSender) performDefaultHandlingForAuthenticationChallenge:].cold.1
+ -[AVAssetResourceLoadingRequest _sendDataToCustomURLHandler:].cold.1
+ -[AVAssetResourceLoadingRequest _sendResponseInfoToCustomURLHandler].cold.1
+ -[AVAssetResourceLoadingRequest keyRequestDataUsingCryptorForApp:contentIdentifier:options:performAsync:error:].cold.1
+ -[AVAssetResourceLoadingRequest persistentContentKeyFromKeyVendorResponse:options:error:].cold.1
+ -[AVAssetWriterInput setPreferredMediaChunkAlignment:].cold.1
+ -[AVAssetWriterInputCaptionAdaptor initWithAssetWriterInput:].cold.1
+ -[AVAssetWriterInputFigAssetWriterEndPassOperation initWithFigAssetWriter:trackID:].cold.1
+ -[AVAssetWriterInputFigAssetWriterEndPassOperation initWithFigAssetWriter:trackID:].cold.2
+ -[AVAssetWriterInputInterPassAnalysisHelper initWithWritingHelper:].cold.1
+ -[AVAssetWriterInputNoMorePassesHelper initWithWritingHelper:].cold.1
+ -[AVAssetWriterInputPassDescriptionResponder initWithCallbackQueue:block:].cold.1
+ -[AVAssetWriterInputPassDescriptionResponder initWithCallbackQueue:block:].cold.2
+ -[AVAssetWriterInputWritingHelper appendCaption:error:].cold.1
+ -[AVAssetWriterInputWritingHelper appendCaptionGroup:error:].cold.1
+ -[AVAsynchronousCIImageFilteringRequest finishWithImage:context:].cold.1
+ -[AVAsynchronousCIImageFilteringRequest finishWithImage:context:].cold.2
+ -[AVAudioMixProcessingEffect _fourCCToFigPropertyDict].cold.1
+ -[AVAudioMixProcessingEffect isValueSupported:exceptionReasonOut:].cold.1
+ -[AVBlockOperation initWithBlock:].cold.1
+ -[AVCMNotificationDispatcher initWithCMNotificationCenter:].cold.1
+ -[AVCaption _setFontStyle:inRange:].cold.1
+ -[AVCaption _setFontStyle:inRange:].cold.2
+ -[AVCaption _setFontWeight:inRange:].cold.1
+ -[AVCaption _setFontWeight:inRange:].cold.2
+ -[AVCaption _setTextAlignment:].cold.1
+ -[AVCaption _setTextCombine:inRange:].cold.1
+ -[AVCaption _setTextCombine:inRange:].cold.2
+ -[AVCaptionConversionWarning description].cold.1
+ -[AVCaptionRegion _endPosition].cold.1
+ -[AVCaptionRegion _endPosition].cold.2
+ -[AVCaptionRegion _predefinedRegionPositionShouldBeNil].cold.1
+ -[AVCaptionRegion _setDisplayAlignment:].cold.1
+ -[AVCaptionRegion _setWritingMode:].cold.1
+ -[AVCaptionRegion _updateExtentPropertiesOfFigCaptionRegionWithPosition:endPosition:].cold.1
+ -[AVCaptionRegion _updateExtentPropertiesOfFigCaptionRegionWithPosition:endPosition:].cold.2
+ -[AVCaptionRegion mutableCopyWithZone:].cold.1
+ -[AVContentKeyReportGroup _associateRequestWithGroupWithRequestID:error:].cold.1
+ -[AVContentKeyReportGroup _destroyContentKeyGroupWithError:].cold.1
+ -[AVContentKeyReportGroup(AVContentKeyReportGroupPrivateUtilities) configureAppIdentifier:].cold.1
+ -[AVContentKeyReportGroup(AVContentKeyReportGroupPrivateUtilities) copyCryptorForCryptKeyAttributes:].cold.1
+ -[AVContentKeyReportGroup(AVContentKeyReportGroupPrivateUtilities) externalProtectionStatusForCryptor:withDisplays:].cold.1
+ -[AVContentKeyReportGroup(AVContentKeyReportGroupPrivateUtilities) hasProtector].cold.1
+ -[AVContentKeyRequest _processContentKeyResponse:renewalDate:initializationVector:error:].cold.1
+ -[AVContentKeyRequest _processContentKeyResponseError:].cold.1
+ -[AVContentKeyRequest contentKeyRequestDataForApp:contentIdentifier:options:error:].cold.1
+ -[AVContentKeyRequest initWithContentKeySession:reportGroup:identifier:contentIdentifier:keyIDFromInitializationData:initializationData:preloadingRequestOptions:providesPersistableKey:].cold.1
+ -[AVContentKeyRequest processContentKeyResponse:].cold.1
+ -[AVContentKeyRequest processContentKeyResponseData:renewalDate:error:].cold.1
+ -[AVContentKeyRequest(AVContentKeyRequest_ExternalProtectionStateSupport) externalContentProtectionStatus].cold.1
+ -[AVContentKeyRequest(AVContentKeyRequest_ExternalProtectionStateSupport) externalContentProtectionStatus].cold.2
+ -[AVContentKeyRequest(AVContentKeyRequest_ExternalProtectionStateSupport) externalContentProtectionStatus].cold.3
+ -[AVContentKeyRequest(AVContentKeyRequest_ExternalProtectionStateSupport) externalContentProtectionStatus].cold.4
+ -[AVContentKeyRequest(AVContentKeyRequest_ExternalProtectionStateSupport) willOutputBeObscuredDueToInsufficientExternalProtectionForDisplays:].cold.1
+ -[AVContentKeyRequest(AVContentKeyRequest_ExternalProtectionStateSupport) willOutputBeObscuredDueToInsufficientExternalProtectionForDisplays:].cold.2
+ -[AVContentKeyRequest(AVContentKeyRequest_ExternalProtectionStateSupport) willOutputBeObscuredDueToInsufficientExternalProtectionForDisplays:].cold.3
+ -[AVContentKeySession(FigContentKeyBoss) _processContentKeyRequestWithIdentifier:encryptionMethod:supportedProtocolVersions:options:groupID:error:].cold.1
+ -[AVCustomVideoCompositorSession(AVCustomVideoCompositorSession_FigCallbackHandling) _compositionFrame:atTime:requiresRenderUsingSources:requiresSampleBuffersUsingSources:withInstruction:].cold.1
+ -[AVCustomVideoCompositorSession(AVCustomVideoCompositorSession_FigCallbackHandling) _compositionFrame:atTime:requiresRenderUsingSources:requiresSampleBuffersUsingSources:withInstruction:].cold.2
+ -[AVFigAssetTrackInspector loadValuesAsynchronouslyForKeys:completionHandler:].cold.1
+ -[AVFigAssetTrackInspector statusOfValueForKey:error:].cold.1
+ -[AVFigAssetWriterFinishWritingAsyncOperation initWithFigAssetWriter:].cold.1
+ -[AVFigEndpointFigRoutingContextOutputDeviceTranslator removeOutputDevice:withOptions:fromRoutingContext:completionHandler:].cold.1
+ -[AVFigEndpointFigRoutingContextOutputDeviceTranslator setOutputDevice:withOptions:onRoutingContext:completionHandler:].cold.1
+ -[AVFigEndpointFigRoutingContextOutputDeviceTranslator setOutputDevices:withOptions:onRoutingContext:completionHandler:].cold.1
+ -[AVFigEndpointOutputDeviceImpl alternateTransportType]
+ -[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator removeOutputDevice:withOptions:fromRoutingContext:completionHandler:].cold.1
+ -[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator setOutputDevice:withOptions:onRoutingContext:completionHandler:].cold.1
+ -[AVFigRouteDescriptorFigRoutingContextOutputDeviceTranslator setOutputDevices:withOptions:onRoutingContext:completionHandler:].cold.1
+ -[AVFigRouteDescriptorOutputDeviceImpl alternateTransportType]
+ -[AVFigRouteDiscovererOutputDeviceDiscoverySessionImpl _serverDied].cold.1
+ -[AVKeyPathDependencyManager initWithDependencyHost:].cold.1
+ -[AVLegibleMediaSearchCursor _numberOfMatchesInCueAtIndex:].cold.1
+ -[AVLegibleMediaSearchCursor matchDescription].cold.1
+ -[AVLegibleMediaSearchCursor presentationTimeStamp].cold.1
+ -[AVMetadataItem(AVMetadataItem_Local) _updateCommonKey].cold.1
+ -[AVMetadataItem(AVMetadataItem_Local) _valueFromCFType:].cold.1
+ -[AVMetadataItemFilterForSharing whitelist].cold.1
+ -[AVMutableCompositionTrack insertTimeRanges:ofTracks:atTime:error:].cold.1
+ -[AVMutableCompositionTrack insertTimeRanges:ofTracks:atTime:error:].cold.2
+ -[AVOutputContext outputContextImplDidChangeGlobalOutputDeviceConfiguration:].cold.1
+ -[AVOutputDevice alternateTransportType]
+ -[AVPlaybackItemInspectorLoader _dictionaryOfSpecialGettersForKeyValueStatus].cold.1
+ -[AVPlayer _addItemToLinkedList_invokeOnIvarAccessQueue:afterItem:].cold.1
+ -[AVPlayer _removeItemFromLinkedList_invokeOnIvarAccessQueue:].cold.1
+ -[AVPlayer _setNeroVideoGravityOnFigPlayer].cold.1
+ -[AVPlayer _setStartupSyncIgnoresAudioDeviceLatency:]
+ -[AVPlayer _startupSyncIgnoresAudioDeviceLatency]
+ -[AVPlayer init].cold.1
+ -[AVPlayerConnection removeItemFromPlayQueue].cold.1
+ -[AVPlayerItem _attachToFigPlayer].cold.1
+ -[AVPlayerItem _insertAfterItem:].cold.1
+ -[AVPlayerItem _isNonForcedSubtitleDisplayEnabled].cold.1
+ -[AVPlayerItem _updatePlaybackPropertiesOnFigPlaybackItem].cold.1
+ -[AVPlayerItem(AVPlayerInterstitialSupport) _integratedSessionIdentifier]
+ -[AVPlayerItem(AVPlayerInterstitialSupport) _setIntegratedSessionIdentifier:]
+ -[AVPlayerItemIntegratedTimeline .cxx_destruct]
+ -[AVPlayerItemIntegratedTimeline _informDelegateOfSeekForTimeIfNecessary:]
+ -[AVPlayerItemIntegratedTimeline(AVPlayerItemIntegratedTimeline_Private) seekDelegate]
+ -[AVPlayerItemIntegratedTimeline(AVPlayerItemIntegratedTimeline_Private) setSeekDelegate:]
+ -[AVPlayerItemIntegratedTimelinePeriodicObserver .cxx_destruct]
+ -[AVPlayerItemIntegratedTimelinePeriodicObserver initWithInterval:queue:block:integratedTimeline:]
+ -[AVPlayerLayer init].cold.1
+ -[AVRoutingSessionManager startRoutingSessionForHighConfidenceExternalDestinationIfPresentWithCompletionHandler:].cold.1
+ -[AVRoutingSessionManager startRoutingSessionWithOutputDeviceDescriptions:error:].cold.1
+ -[AVRoutingSessionManager startSuppressingLikelyDestinationsUntilNextPlayEventAndReturnError:].cold.1
+ -[AVRoutingSessionManager stopSuppressingLikelyDestinationsAndReturnError:].cold.1
+ -[AVRoutingSessionManager updateCurrentRoutingSessionFromLikelyDestinationsWithCompletionHandler:].cold.1
+ -[AVSampleBufferAudioRenderer setAudioOutputDeviceUniqueID:].cold.1
+ -[AVSampleBufferAudioRenderer setAudioTimePitchAlgorithm:].cold.1
+ -[AVSampleBufferAudioRenderer setOutputContext:].cold.1
+ -[AVSampleBufferGeneratorBatch makeDataReadyWithCompletionHandler:].cold.1
+ -[AVSampleCursor currentChunkStorageURL].cold.1
+ -[AVSampleCursor currentSampleAudioDependencyInfo].cold.1
+ -[AVScheduledAudioParameters _volumeCurveKeysForScheduledRampClassNames].cold.1
+ -[AVStreamDataParser(AVStreamDataParser_FigManifold) _figManifold:formatDescription:orDecryptorDidChange:forTrackID:].cold.1
+ -[AVStreamDataParser(AVStreamDataParser_FigManifold) _figManifold:formatDescription:orDecryptorDidChange:forTrackID:].cold.2
+ -[AVStreamDataParser(AVStreamDataParser_FigManifold) _figManifold:formatDescription:orDecryptorDidChange:forTrackID:].cold.3
+ -[AVStreamDataParser(AVStreamDataParser_FigManifold) _figManifold:formatDescription:orDecryptorDidChange:forTrackID:].cold.4
+ -[AVVideoComposition init].cold.1
+ AVCanWriteFilesToDirectoryAtURL.cold.1
+ AVIsSpecialSpokenExtendedLanguageTag.cold.1
+ AVOutputDeviceCopySharedRouteDiscovererForRouteDescriptor.cold.1
+ AVOutputDeviceNotificationFromFigNotification.cold.1
+ AVSampleBufferAttachContentKey.cold.1
+ AVTranslateAVMediaCharacteristicToFigMediaCharacteristic.cold.1
+ AVTranslateFigMediaCharacteristicToAVMediaCharacteristic.cold.1
+ AVUnsupportedOutputURLPathExtensions.cold.1
+ GCC_except_table1003
+ GCC_except_table1005
+ GCC_except_table1009
+ GCC_except_table1013
+ GCC_except_table1017
+ GCC_except_table1021
+ GCC_except_table1027
+ GCC_except_table1029
+ GCC_except_table1036
+ GCC_except_table1040
+ GCC_except_table109
+ GCC_except_table129
+ GCC_except_table174
+ GCC_except_table178
+ GCC_except_table183
+ GCC_except_table185
+ GCC_except_table188
+ GCC_except_table190
+ GCC_except_table197
+ GCC_except_table203
+ GCC_except_table208
+ GCC_except_table210
+ GCC_except_table217
+ GCC_except_table231
+ GCC_except_table237
+ GCC_except_table247
+ GCC_except_table253
+ GCC_except_table259
+ GCC_except_table266
+ GCC_except_table269
+ GCC_except_table273
+ GCC_except_table282
+ GCC_except_table288
+ GCC_except_table296
+ GCC_except_table298
+ GCC_except_table304
+ GCC_except_table306
+ GCC_except_table312
+ GCC_except_table314
+ GCC_except_table320
+ GCC_except_table329
+ GCC_except_table334
+ GCC_except_table349
+ GCC_except_table355
+ GCC_except_table357
+ GCC_except_table374
+ GCC_except_table380
+ GCC_except_table386
+ GCC_except_table392
+ GCC_except_table398
+ GCC_except_table404
+ GCC_except_table407
+ GCC_except_table412
+ GCC_except_table416
+ GCC_except_table419
+ GCC_except_table422
+ GCC_except_table428
+ GCC_except_table432
+ GCC_except_table434
+ GCC_except_table436
+ GCC_except_table437
+ GCC_except_table442
+ GCC_except_table444
+ GCC_except_table446
+ GCC_except_table456
+ GCC_except_table458
+ GCC_except_table464
+ GCC_except_table466
+ GCC_except_table468
+ GCC_except_table476
+ GCC_except_table481
+ GCC_except_table486
+ GCC_except_table491
+ GCC_except_table496
+ GCC_except_table501
+ GCC_except_table508
+ GCC_except_table509
+ GCC_except_table512
+ GCC_except_table514
+ GCC_except_table520
+ GCC_except_table523
+ GCC_except_table533
+ GCC_except_table537
+ GCC_except_table541
+ GCC_except_table543
+ GCC_except_table546
+ GCC_except_table548
+ GCC_except_table551
+ GCC_except_table555
+ GCC_except_table558
+ GCC_except_table56
+ GCC_except_table560
+ GCC_except_table563
+ GCC_except_table565
+ GCC_except_table568
+ GCC_except_table570
+ GCC_except_table574
+ GCC_except_table579
+ GCC_except_table582
+ GCC_except_table586
+ GCC_except_table592
+ GCC_except_table594
+ GCC_except_table596
+ GCC_except_table598
+ GCC_except_table600
+ GCC_except_table601
+ GCC_except_table608
+ GCC_except_table612
+ GCC_except_table616
+ GCC_except_table618
+ GCC_except_table621
+ GCC_except_table629
+ GCC_except_table634
+ GCC_except_table639
+ GCC_except_table641
+ GCC_except_table645
+ GCC_except_table652
+ GCC_except_table657
+ GCC_except_table662
+ GCC_except_table667
+ GCC_except_table671
+ GCC_except_table673
+ GCC_except_table675
+ GCC_except_table679
+ GCC_except_table683
+ GCC_except_table685
+ GCC_except_table689
+ GCC_except_table691
+ GCC_except_table696
+ GCC_except_table701
+ GCC_except_table706
+ GCC_except_table715
+ GCC_except_table721
+ GCC_except_table731
+ GCC_except_table737
+ GCC_except_table743
+ GCC_except_table751
+ GCC_except_table759
+ GCC_except_table764
+ GCC_except_table766
+ GCC_except_table772
+ GCC_except_table778
+ GCC_except_table788
+ GCC_except_table792
+ GCC_except_table794
+ GCC_except_table796
+ GCC_except_table802
+ GCC_except_table811
+ GCC_except_table817
+ GCC_except_table831
+ GCC_except_table833
+ GCC_except_table839
+ GCC_except_table841
+ GCC_except_table849
+ GCC_except_table851
+ GCC_except_table857
+ GCC_except_table864
+ GCC_except_table870
+ GCC_except_table873
+ GCC_except_table888
+ GCC_except_table890
+ GCC_except_table896
+ GCC_except_table903
+ GCC_except_table91
+ GCC_except_table922
+ GCC_except_table924
+ GCC_except_table926
+ GCC_except_table928
+ GCC_except_table946
+ GCC_except_table956
+ GCC_except_table960
+ GCC_except_table967
+ GCC_except_table971
+ GCC_except_table977
+ GCC_except_table979
+ GCC_except_table98
+ GCC_except_table991
+ GCC_except_table995
+ GCC_except_table999
+ OBJC_IVAR_$_AVAssetDownloadConfiguration._interstitialMediaSelectionCriteria
+ OBJC_IVAR_$_AVAssetImageGeneratorInternal.status
+ OBJC_IVAR_$_AVPlayerInternal.startupSyncIgnoresAudioDeviceLatency
+ OBJC_IVAR_$_AVPlayerItemIntegratedTimeline._seekDelegate
+ OBJC_IVAR_$_AVPlayerItemIntegratedTimelinePeriodicObserver._integratedTimeline
+ OBJC_IVAR_$_AVPlayerItemInternal.integratedSessionIdentifier
+ _AVAssetPlaybackConfigurationOptionNonRectilinearProjection
+ _AVMediaCharacteristicIndicatesNonRectilinearProjection
+ _AVOutputDeviceAVFBluetoothAlternateTransportForFigAlternateTransport
+ _AVOutputDeviceBluetoothAlternateTransportTypeDefault
+ _AVOutputDeviceBluetoothAlternateTransportTypeUSBC
+ _AVPlayerItemAVFTimeJumpReasonForFigReason
+ _AVURLAssetiTunesStoreContentAlternateContentInfoAssetURLStringKey
+ _AVURLAssetiTunesStoreContentAlternateContentInfoKey
+ _AVURLAssetiTunesStoreContentDSIDKey
+ _AVURLAssetiTunesStoreContentDownloadParametersKey
+ _AVURLAssetiTunesStoreContentHLSAssetURLStringKey
+ _AVURLAssetiTunesStoreContentIDKey
+ _AVURLAssetiTunesStoreContentInfoKey
+ _AVURLAssetiTunesStoreContentPurchasedMediaKindKey
+ _AVURLAssetiTunesStoreContentRentalIDKey
+ _AVURLAssetiTunesStoreContentTypeKey
+ _AVURLAssetiTunesStoreContentUserAgentKey
+ _FigStreamingAssetDownloadConfigSetMediaSelectionCriteriaForInterstitials
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __108-[AVContentKeyRequest makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:]_block_invoke.156.cold.1
+ __108-[AVContentKeyRequest makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:]_block_invoke.156.cold.2
+ __109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke.400
+ __109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke.408
+ __109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke.412
+ __109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke_2.413
+ __111-[AVContentKeyReportGroup(AVContentKeyReportGroupPrivateUtilities) _setAuthorizationToken:forIdentifier:error:]_block_invoke.cold.1
+ __111-[AVContentKeyReportGroup(AVContentKeyReportGroupPrivateUtilities) createProtectorSessionIdentifierIfNecessary]_block_invoke.cold.1
+ __125-[AVPlayerItem(AVPlayerItemProtectedContent) requestContentAuthorizationAsynchronouslyWithTimeoutInterval:completionHandler:]_block_invoke.1153
+ __125-[AVPlayerItem(AVPlayerItemProtectedContent) requestContentAuthorizationAsynchronouslyWithTimeoutInterval:completionHandler:]_block_invoke_2.1154
+ __23-[AVRouteDetector init]_block_invoke_3.cold.1
+ __26-[AVPlayerItem _setAsset:]_block_invoke.513
+ __30-[AVPlayer _advanceToNextItem]_block_invoke.425
+ __34-[AVPlayer _insertItem:afterItem:]_block_invoke.436
+ __34-[AVPlayerItem _attachToFigPlayer]_block_invoke.472
+ __35-[AVPlayer _addPlayerCaptionLayer:]_block_invoke.578
+ __36-[AVPlayerItem setVideoComposition:]_block_invoke.623
+ __42-[AVPlayer _synchronizeWithNewCurrentItem]_block_invoke.398
+ __45-[AVPlayer replaceCurrentItemWithPlayerItem:]_block_invoke.511
+ __46-[AVPlayer prepareItem:withCompletionHandler:]_block_invoke.429
+ __46-[AVPlayer prepareItem:withCompletionHandler:]_block_invoke_2.430
+ __51-[AVPlayer _setUsesLegacyAutomaticWaitingBehavior:]_block_invoke.533
+ __51-[AVPlayer _startObservingPropertiesOfCurrentItem:]_block_invoke.422
+ __53-[AVPlayerItem _addInterstitialEventCollectorLocked:]_block_invoke.667
+ __60-[AVPlayerItem _ensureAssetWithFigPlaybackItemWithTrackIDs:]_block_invoke.514
+ __62-[AVPlayer _setRate:rateChangeReason:figPlayerSetRateHandler:]_block_invoke.517
+ __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.459
+ __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.480
+ __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.485
+ __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.460
+ __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.481
+ __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_3.464
+ __69-[AVPlayerItem _setAudioEffectParameters:previousEffects:forTrackID:]_block_invoke.612
+ __82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke.71
+ __82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke.87
+ __82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke_2.72
+ __82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke_2.88
+ __87-[AVPlayer _removeLayer:videoLayer:closedCaptionLayer:subtitleLayer:interstitialLayer:]_block_invoke.579
+ __91-[AVPlayer(AVPlayerTaggedBufferOutputSupport) setVideoOutput:withOwningTaggedBufferOutput:]_block_invoke.1014
+ __92-[AVPlayerItem(AVMetricEventStreamPublisherInternal) getEventTimelineWithCompletionHandler:]_block_invoke.1433
+ __MergedGlobals
+ __OBJC_$_INSTANCE_METHODS_AVPlayerItemIntegratedTimeline(AVPlayerItemIntegratedTimelineObserver|AVPlayerItemIntegratedTimeline_Private)
+ ___34-[AVPlayerItem _attachToFigPlayer]_block_invoke_3
+ ___49-[AVPlayer _startupSyncIgnoresAudioDeviceLatency]_block_invoke
+ ___53-[AVPlayer _setStartupSyncIgnoresAudioDeviceLatency:]_block_invoke
+ ___53-[AVPlayer _setStartupSyncIgnoresAudioDeviceLatency:]_block_invoke_2
+ ___53-[AVPlayer _setStartupSyncIgnoresAudioDeviceLatency:]_block_invoke_3
+ ___73-[AVPlayerItem(AVPlayerInterstitialSupport) _integratedSessionIdentifier]_block_invoke
+ ___77-[AVPlayerItem(AVPlayerInterstitialSupport) _setIntegratedSessionIdentifier:]_block_invoke
+ ___block_descriptor_96_e8_32o40r48r56r64r72r80r88r_e5_v8?0l
+ ___copy_helper_block_e8_32o40r48r56r64r72r80r88r
+ ___destroy_helper_block_e8_32o40r48r56r64r72r80r88r
+ __avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke.1136
+ __avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke.1137
+ __avplayer_fpNotificationCallback_block_invoke.1155
+ __avplayer_fpNotificationCallback_block_invoke.1160
+ __avplayer_fpNotificationCallback_block_invoke_2.1157
+ __avplayer_fpNotificationCallback_block_invoke_2.1161
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1455
+ __avplayeritem_fpItemNotificationCallback_block_invoke.1478
+ __avplayeritem_fpItemNotificationCallback_block_invoke_10.1490
+ __avplayeritem_fpItemNotificationCallback_block_invoke_11.1491
+ __avplayeritem_fpItemNotificationCallback_block_invoke_2.1456
+ __avplayeritem_fpItemNotificationCallback_block_invoke_2.1479
+ __avplayeritem_fpItemNotificationCallback_block_invoke_3.1460
+ __avplayeritem_fpItemNotificationCallback_block_invoke_3.1480
+ __avplayeritem_fpItemNotificationCallback_block_invoke_4.1464
+ __avplayeritem_fpItemNotificationCallback_block_invoke_4.1484
+ __avplayeritem_fpItemNotificationCallback_block_invoke_5.1471
+ __avplayeritem_fpItemNotificationCallback_block_invoke_5.1485
+ __avplayeritem_fpItemNotificationCallback_block_invoke_6.1472
+ __avplayeritem_fpItemNotificationCallback_block_invoke_6.1486
+ __avplayeritem_fpItemNotificationCallback_block_invoke_7.1473
+ __avplayeritem_fpItemNotificationCallback_block_invoke_7.1487
+ __avplayeritem_fpItemNotificationCallback_block_invoke_8.1477
+ __avplayeritem_fpItemNotificationCallback_block_invoke_8.1488
+ __avplayeritem_fpItemNotificationCallback_block_invoke_9.1489
+ __block_literal_global.1029
+ __block_literal_global.1031
+ __block_literal_global.444
+ __block_literal_global.537
+ __block_literal_global.541
+ __block_literal_global.566
+ __block_literal_global.569
+ __block_literal_global.583
+ __block_literal_global.653
+ __block_literal_global.659
+ __block_literal_global.688
+ __block_literal_global.860
+ _attachToFigPlayer.sMetricRetrievalOnceToken
+ _attachToFigPlayer.sMetricRetrievalQueue
+ _kFigAssetOptionKey_iTunesStoreContentInfo
+ _kFigAssetiTunesStoreContentOptionsKey_AlternateContentInfo
+ _kFigAssetiTunesStoreContentOptionsKey_AlternateContentInfoAssetURLString
+ _kFigAssetiTunesStoreContentOptionsKey_DSID
+ _kFigAssetiTunesStoreContentOptionsKey_DownloadParameters
+ _kFigAssetiTunesStoreContentOptionsKey_HLSAssetURLString
+ _kFigAssetiTunesStoreContentOptionsKey_ID
+ _kFigAssetiTunesStoreContentOptionsKey_PurchasedMediaKind
+ _kFigAssetiTunesStoreContentOptionsKey_RentalID
+ _kFigAssetiTunesStoreContentOptionsKey_Type
+ _kFigAssetiTunesStoreContentOptionsKey_UserAgent
+ _kFigMetadataFormat_VorbisComment
+ _kFigPlaybackItemOptionKey_IntegratedSessionID
+ _kFigPlayerProperty_IgnoreAudioDeviceLatencyInStartupSync
+ _kFigVorbisCommentMetadataKeyspace
+ _objc_msgSend$_getFigAssetiTunesStoreContentInfoFromURLAssetiTunesStoreContentInfo:
+ _objc_msgSend$_informDelegateOfSeekForTimeIfNecessary:
+ _objc_msgSend$_integratedSessionIdentifier
+ _objc_msgSend$_setIntegratedSessionIdentifier:
+ _objc_msgSend$_startupSyncIgnoresAudioDeviceLatency
+ _objc_msgSend$alternateTransportType
+ _objc_msgSend$initWithInterval:queue:block:integratedTimeline:
+ _objc_msgSend$integratedTimeline:willSeekToTime:currentTime:
+ _objc_msgSend$setRestrictsAutomaticMediaSelectionToAvailableOfflineOptions:
+ appendCaptionGroupToQueue.cold.1
+ avasset_formatsChangedNotificationCallback.cold.1
+ avasset_formatsChangedNotificationCallback.cold.2
+ avckrg_externalProtectionStateChangedCallback.cold.1
+ avckrg_keyResponseErrorCallback.cold.1
+ avckrg_keyResponseSuccessfullyProcessedCallback.cold.1
+ avckrg_persistentKeyUpdatedCallback.cold.1
+ avckrg_secureStopDidFinalizeRecordCallback.cold.1
+ customURLAuthHandlerHandleRequestCallback.cold.1
+ customURLAuthHandlerHandleRequestCallback.cold.2
+ customURLAuthHandlerRequestCancelled.cold.1
+ customURLAuthHandlerRequestCancelled.cold.2
+ customURLHandlerHandleRequestCallback.cold.1
+ customURLHandlerHandleRequestCallback.cold.2
+ customURLHandlerRequestCancelled.cold.1
+ customURLHandlerRequestCancelled.cold.2
+ dictionaryOfFigAssetTrackPropertiesForTrackKeys.cold.1
+ initAVMetadataMakeDependentSpecificationsForValue.cold.1
+ initAVMetadataMakeMetadataObjectFromBoxedMetadata.cold.1
+ initAVMetadataObjectCreateBoxedMetadataFromObjectAndFormatDescription.cold.1
- -[AVPlayerItemIntegratedTimelinePeriodicObserver initWithInterval:queue:block:]
- -[AVTimeFormatter stringFromTimeInterval:].cold.1
- GCC_except_table1002
- GCC_except_table1004
- GCC_except_table1008
- GCC_except_table1012
- GCC_except_table1016
- GCC_except_table1022
- GCC_except_table1024
- GCC_except_table1026
- GCC_except_table1035
- GCC_except_table135
- GCC_except_table140
- GCC_except_table157
- GCC_except_table170
- GCC_except_table179
- GCC_except_table181
- GCC_except_table196
- GCC_except_table202
- GCC_except_table207
- GCC_except_table214
- GCC_except_table230
- GCC_except_table236
- GCC_except_table241
- GCC_except_table258
- GCC_except_table268
- GCC_except_table272
- GCC_except_table279
- GCC_except_table281
- GCC_except_table287
- GCC_except_table295
- GCC_except_table297
- GCC_except_table303
- GCC_except_table311
- GCC_except_table313
- GCC_except_table319
- GCC_except_table321
- GCC_except_table333
- GCC_except_table348
- GCC_except_table354
- GCC_except_table373
- GCC_except_table379
- GCC_except_table385
- GCC_except_table397
- GCC_except_table411
- GCC_except_table415
- GCC_except_table418
- GCC_except_table420
- GCC_except_table427
- GCC_except_table429
- GCC_except_table431
- GCC_except_table433
- GCC_except_table440
- GCC_except_table441
- GCC_except_table443
- GCC_except_table445
- GCC_except_table449
- GCC_except_table457
- GCC_except_table462
- GCC_except_table465
- GCC_except_table470
- GCC_except_table475
- GCC_except_table479
- GCC_except_table480
- GCC_except_table484
- GCC_except_table495
- GCC_except_table503
- GCC_except_table507
- GCC_except_table511
- GCC_except_table519
- GCC_except_table522
- GCC_except_table524
- GCC_except_table530
- GCC_except_table532
- GCC_except_table534
- GCC_except_table540
- GCC_except_table542
- GCC_except_table544
- GCC_except_table547
- GCC_except_table549
- GCC_except_table552
- GCC_except_table553
- GCC_except_table559
- GCC_except_table562
- GCC_except_table564
- GCC_except_table567
- GCC_except_table569
- GCC_except_table573
- GCC_except_table575
- GCC_except_table580
- GCC_except_table581
- GCC_except_table588
- GCC_except_table589
- GCC_except_table591
- GCC_except_table595
- GCC_except_table597
- GCC_except_table599
- GCC_except_table603
- GCC_except_table605
- GCC_except_table607
- GCC_except_table615
- GCC_except_table617
- GCC_except_table628
- GCC_except_table638
- GCC_except_table640
- GCC_except_table644
- GCC_except_table651
- GCC_except_table655
- GCC_except_table659
- GCC_except_table666
- GCC_except_table670
- GCC_except_table672
- GCC_except_table674
- GCC_except_table678
- GCC_except_table682
- GCC_except_table684
- GCC_except_table688
- GCC_except_table690
- GCC_except_table695
- GCC_except_table700
- GCC_except_table705
- GCC_except_table714
- GCC_except_table720
- GCC_except_table730
- GCC_except_table736
- GCC_except_table742
- GCC_except_table750
- GCC_except_table758
- GCC_except_table763
- GCC_except_table765
- GCC_except_table771
- GCC_except_table777
- GCC_except_table787
- GCC_except_table791
- GCC_except_table793
- GCC_except_table795
- GCC_except_table801
- GCC_except_table810
- GCC_except_table816
- GCC_except_table830
- GCC_except_table832
- GCC_except_table838
- GCC_except_table840
- GCC_except_table848
- GCC_except_table850
- GCC_except_table856
- GCC_except_table863
- GCC_except_table869
- GCC_except_table871
- GCC_except_table887
- GCC_except_table889
- GCC_except_table895
- GCC_except_table90
- GCC_except_table902
- GCC_except_table921
- GCC_except_table923
- GCC_except_table925
- GCC_except_table927
- GCC_except_table945
- GCC_except_table955
- GCC_except_table959
- GCC_except_table966
- GCC_except_table97
- GCC_except_table970
- GCC_except_table976
- GCC_except_table978
- GCC_except_table990
- GCC_except_table994
- GCC_except_table998
- _AVFileTypeQuickTimeAudio
- __109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke.399
- __109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke.406
- __109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke.411
- __109-[AVPlayer _runOnIvarAccessQueueOperationThatMayChangeCurrentItemWithPreflightBlock:modificationBlock:error:]_block_invoke_2.412
- __125-[AVPlayerItem(AVPlayerItemProtectedContent) requestContentAuthorizationAsynchronouslyWithTimeoutInterval:completionHandler:]_block_invoke.1149
- __125-[AVPlayerItem(AVPlayerItemProtectedContent) requestContentAuthorizationAsynchronouslyWithTimeoutInterval:completionHandler:]_block_invoke_2.1150
- __26-[AVPlayerItem _setAsset:]_block_invoke.511
- __30-[AVPlayer _advanceToNextItem]_block_invoke.424
- __34-[AVPlayer _insertItem:afterItem:]_block_invoke.435
- __34-[AVPlayerItem _attachToFigPlayer]_block_invoke.471
- __35-[AVPlayer _addPlayerCaptionLayer:]_block_invoke.577
- __36-[AVPlayerItem setVideoComposition:]_block_invoke.619
- __42-[AVPlayer _synchronizeWithNewCurrentItem]_block_invoke.397
- __45-[AVPlayer replaceCurrentItemWithPlayerItem:]_block_invoke.510
- __46-[AVPlayer prepareItem:withCompletionHandler:]_block_invoke.428
- __46-[AVPlayer prepareItem:withCompletionHandler:]_block_invoke_2.429
- __51-[AVPlayer _setUsesLegacyAutomaticWaitingBehavior:]_block_invoke.532
- __51-[AVPlayer _startObservingPropertiesOfCurrentItem:]_block_invoke.421
- __53-[AVPlayerItem _addInterstitialEventCollectorLocked:]_block_invoke.663
- __60-[AVPlayerItem _ensureAssetWithFigPlaybackItemWithTrackIDs:]_block_invoke.512
- __62-[AVPlayer _setRate:rateChangeReason:figPlayerSetRateHandler:]_block_invoke.516
- __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.458
- __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.479
- __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke.484
- __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.459
- __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_2.480
- __67-[AVPlayer _createAndConfigureFigPlayerWithType:completionHandler:]_block_invoke_3.463
- __69-[AVPlayerItem _setAudioEffectParameters:previousEffects:forTrackID:]_block_invoke.608
- __82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke.69
- __82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke.85
- __82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke_2.70
- __82-[AVAssetImageGenerator generateCGImagesAsynchronouslyForTimes:completionHandler:]_block_invoke_2.86
- __87-[AVPlayer _removeLayer:videoLayer:closedCaptionLayer:subtitleLayer:interstitialLayer:]_block_invoke.578
- __91-[AVPlayer(AVPlayerTaggedBufferOutputSupport) setVideoOutput:withOwningTaggedBufferOutput:]_block_invoke.1011
- __92-[AVPlayerItem(AVMetricEventStreamPublisherInternal) getEventTimelineWithCompletionHandler:]_block_invoke.1427
- __OBJC_$_INSTANCE_METHODS_AVPlayerItemIntegratedTimeline(AVPlayerItemIntegratedTimelineObserver)
- __OBJC_$_PROP_LIST_AVPlayerItemIntegratedTimeline
- ___assert_rtn
- ___block_descriptor_88_e8_32o40r48r56r64r72r80r_e5_v8?0l
- ___copy_helper_block_e8_32o40r48r56r64r72r80r
- ___destroy_helper_block_e8_32o40r48r56r64r72r80r
- __avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke.1133
- __avplayer_fpInterstitialCoordinatorNotificationCallback_block_invoke.1134
- __avplayer_fpNotificationCallback_block_invoke.1152
- __avplayer_fpNotificationCallback_block_invoke.1157
- __avplayer_fpNotificationCallback_block_invoke_2.1154
- __avplayer_fpNotificationCallback_block_invoke_2.1158
- __avplayeritem_fpItemNotificationCallback_block_invoke.1449
- __avplayeritem_fpItemNotificationCallback_block_invoke.1472
- __avplayeritem_fpItemNotificationCallback_block_invoke_10.1484
- __avplayeritem_fpItemNotificationCallback_block_invoke_11.1485
- __avplayeritem_fpItemNotificationCallback_block_invoke_2.1450
- __avplayeritem_fpItemNotificationCallback_block_invoke_2.1473
- __avplayeritem_fpItemNotificationCallback_block_invoke_3.1454
- __avplayeritem_fpItemNotificationCallback_block_invoke_3.1474
- __avplayeritem_fpItemNotificationCallback_block_invoke_4.1458
- __avplayeritem_fpItemNotificationCallback_block_invoke_4.1478
- __avplayeritem_fpItemNotificationCallback_block_invoke_5.1465
- __avplayeritem_fpItemNotificationCallback_block_invoke_5.1479
- __avplayeritem_fpItemNotificationCallback_block_invoke_6.1466
- __avplayeritem_fpItemNotificationCallback_block_invoke_6.1480
- __avplayeritem_fpItemNotificationCallback_block_invoke_7.1467
- __avplayeritem_fpItemNotificationCallback_block_invoke_7.1481
- __avplayeritem_fpItemNotificationCallback_block_invoke_8.1471
- __avplayeritem_fpItemNotificationCallback_block_invoke_8.1482
- __avplayeritem_fpItemNotificationCallback_block_invoke_9.1483
- __block_literal_global.443
- __block_literal_global.536
- __block_literal_global.565
- __block_literal_global.568
- __block_literal_global.582
- __block_literal_global.649
- __block_literal_global.655
- __block_literal_global.826
- __block_literal_global.995
- __block_literal_global.997
- _avsbrs_rendererIsAudioRenderer
- _copyDefaultChannelLayoutForChannelCount
- _objc_msgSend$initWithInterval:queue:block:
- makePropertyListForProxyWithOptions:.commonKeysWeWantToKeep
- makePropertyListForProxyWithOptions:.commonKeysWeWantToKeepOnce
CStrings:
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator returned error (%d) handling new control state."
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator returned error (%d) handling new participant state."
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator returned error (%d) handling replacement participant state."
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator trying to broadcast participant state but coordination medium delegate is nil"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator trying to broadcast timeline state but coordination medium delegate is nil"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator trying to reload timeline state but coordination medium delegate is nil.  Clearing delegate and calling completion handler."
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: Ignoring stale state for %{public}@"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: States aren't distinguishable. Assuming existing state is better for %{public}@."
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/Utilities/AVDelegateUtilities.m"
+ "<<<< AVPlayerItemIntegratedTimeline >>>> %s: rescheduling observer %p with offset %f, interval %f"
+ "@\"<AVPlayerItemIntegratedTimelineSeekDelegate>\""
+ "@64@0:8{?=qiIq}16@40@?48@56"
+ "AVAssetPlaybackConfigurationOptionNonRectilinearProjection"
+ "AVOutputDeviceBluetoothAlternateTransportTypeDefault"
+ "AVOutputDeviceBluetoothAlternateTransportTypeUSBC"
+ "AVPlayerItemIntegratedTimeline_Private"
+ "AVURLAssetiTunesStoreContentAlternateContentInfoAssetURLStringKey"
+ "AVURLAssetiTunesStoreContentAlternateContentInfoKey"
+ "AVURLAssetiTunesStoreContentDSIDKey"
+ "AVURLAssetiTunesStoreContentDownloadParametersKey"
+ "AVURLAssetiTunesStoreContentHLSAssetURLStringKey"
+ "AVURLAssetiTunesStoreContentIDKey"
+ "AVURLAssetiTunesStoreContentInfoKey"
+ "AVURLAssetiTunesStoreContentPurchasedMediaKindKey"
+ "AVURLAssetiTunesStoreContentRentalIDKey"
+ "AVURLAssetiTunesStoreContentTypeKey"
+ "AVURLAssetiTunesStoreContentUserAgentKey"
+ "BTDetails_AlternateTransport"
+ "T@\"<AVPlayerItemIntegratedTimelineSeekDelegate>\",W,N"
+ "_getFigAssetiTunesStoreContentInfoFromURLAssetiTunesStoreContentInfo:"
+ "_informDelegateOfSeekForTimeIfNecessary:"
+ "_integratedSessionIdentifier"
+ "_interstitialMediaSelectionCriteria"
+ "_invalidated"
+ "_seekDelegate"
+ "_setIntegratedSessionIdentifier:"
+ "_setStartupSyncIgnoresAudioDeviceLatency:"
+ "_startupSyncIgnoresAudioDeviceLatency"
+ "alternateTransportType"
+ "com.apple.avfoundation.metric-retrieval"
+ "initWithInterval:queue:block:integratedTimeline:"
+ "integratedSessionIdentifier"
+ "integratedTimeline:willSeekToTime:currentTime:"
+ "interstitalMediaSelectionCriteria"
+ "public.indicates-non-rectilinear-projection"
+ "seekDelegate"
+ "setInterstitialMediaSelectionCriteria:forMediaCharacteristic:"
+ "setSeekDelegate:"
+ "startupSyncIgnoresAudioDeviceLatency"
+ "\xf0Q"
+ "\xf0\x91"
- "-[AVPlayerPlaybackCoordinator _updateParticipantStateOnFigPlaybackCoordinatorForItemWithIdentifier:]"
- "-[AVPlayerPlaybackCoordinator _updateTransportControlStateDictionaryOnFigPlaybackCoordinatorForItemIdentifier:]"
- "-[AVPlayerPlaybackCoordinator handleReplacementParticipantStateDictionaries:]"
- "-[AVSampleBufferVideoRenderer dealloc]"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator returned error (%d) handling new control state."
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator returned error (%d) handling new participant state."
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator returned error (%d) handling replacement participant state."
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator trying to broadcast participant state but coordination medium delegate is nil"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator trying to broadcast timeline state but coordination medium delegate is nil"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: FigTimelineCoordinator trying to reload timeline state but coordination medium delegate is nil.  Clearing delegate and calling completion handler."
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: Ignoring stale state for %{public}@"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/AVDelegatingPlaybackCoordinator.m %s: States aren't distinguishable. Assuming existing state is better for %{public}@."
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AVFoundation_AVFCore/Fig/Utilities/AVDelegateUtilities.m"
- "<<<< AVPlaybackCoordinator >>>> %s: FigPlaybackCoordinator is NULL when trying to handle new control state."
- "<<<< AVPlaybackCoordinator >>>> %s: FigPlaybackCoordinator is NULL when trying to handle new participant state."
- "<<<< AVPlaybackCoordinator >>>> %s: FigPlaybackCoordinator is NULL when trying to handle replacement participant state."
- "<<<< AVPlayerItemIntegratedTimeline >>>> %s: rescheduling observer %p with offset %f"
- "AVCrackTime"
- "AVTimeFormatter.m"
- "com.apple.quicktime-audio"
- "initWithInterval:queue:block:"
- "time >= 0.0"

```
