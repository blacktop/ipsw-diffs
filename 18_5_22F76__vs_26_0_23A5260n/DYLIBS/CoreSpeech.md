## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech`

```diff

-3405.29.3.11.1
-  __TEXT.__text: 0x1588ac
-  __TEXT.__auth_stubs: 0x1be0
-  __TEXT.__objc_methlist: 0x154a4
-  __TEXT.__const: 0x5e0
+3500.97.2.1.1
+  __TEXT.__text: 0x151480
+  __TEXT.__auth_stubs: 0x1b40
+  __TEXT.__objc_methlist: 0x142cc
+  __TEXT.__const: 0x58c
   __TEXT.__dlopen_cstrs: 0x197
-  __TEXT.__gcc_except_tab: 0x3fd4
-  __TEXT.__cstring: 0x272b8
-  __TEXT.__oslogstring: 0x1f930
-  __TEXT.__unwind_info: 0x5030
-  __TEXT.__objc_classname: 0x2e98
-  __TEXT.__objc_methname: 0x386be
-  __TEXT.__objc_methtype: 0x7c89
-  __TEXT.__objc_stubs: 0x1c5e0
-  __DATA_CONST.__got: 0x1aa8
-  __DATA_CONST.__const: 0x41b8
-  __DATA_CONST.__objc_classlist: 0x858
+  __TEXT.__gcc_except_tab: 0x3cac
+  __TEXT.__cstring: 0x273c0
+  __TEXT.__oslogstring: 0x1ed36
+  __TEXT.__unwind_info: 0x4d60
+  __TEXT.__objc_classname: 0x2e76
+  __TEXT.__objc_methname: 0x37957
+  __TEXT.__objc_methtype: 0x7a59
+  __TEXT.__objc_stubs: 0x1be40
+  __DATA_CONST.__got: 0x1a98
+  __DATA_CONST.__const: 0x40f8
+  __DATA_CONST.__objc_classlist: 0x840
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x490
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaa58
-  __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x698
-  __DATA_CONST.__objc_arraydata: 0x450
-  __AUTH_CONST.__auth_got: 0xe08
+  __DATA_CONST.__objc_selrefs: 0xa7b0
+  __DATA_CONST.__objc_protorefs: 0xa8
+  __DATA_CONST.__objc_superrefs: 0x688
+  __DATA_CONST.__objc_arraydata: 0x3e0
+  __AUTH_CONST.__auth_got: 0xdb8
   __AUTH_CONST.__const: 0x1e00
-  __AUTH_CONST.__cfstring: 0x8fe0
-  __AUTH_CONST.__objc_const: 0x21b98
-  __AUTH_CONST.__objc_intobj: 0xa20
+  __AUTH_CONST.__cfstring: 0x9360
+  __AUTH_CONST.__objc_const: 0x202f8
+  __AUTH_CONST.__objc_intobj: 0x990
   __AUTH_CONST.__objc_doubleobj: 0xb0
-  __AUTH_CONST.__objc_dictobj: 0x3e8
+  __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_floatobj: 0x4c0
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH.__objc_data: 0x320
-  __DATA.__objc_ivar: 0x1a80
+  __AUTH.__objc_data: 0x3e80
+  __DATA.__objc_ivar: 0x18f0
   __DATA.__data: 0x3650
-  __DATA.__bss: 0x660
+  __DATA.__bss: 0x670
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x5050
+  __DATA_DIRTY.__objc_data: 0x1400
   __DATA_DIRTY.__data: 0xc0
-  __DATA_DIRTY.__bss: 0x180
+  __DATA_DIRTY.__bss: 0x150
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C0DA3E06-0E32-308F-85BC-4CB039E2047C
-  Functions: 8276
-  Symbols:   26959
-  CStrings:  15669
+  UUID: EED7ECDD-4AA5-31E2-AADE-36172239C0BB
+  Functions: 7900
+  Symbols:   25976
+  CStrings:  15464
 
Symbols:
+ +[CSASRFeatures supportsSecureCoding]
+ +[CSAudioInjectionEngineFactory engineWithDevice:streamHandleId:]
+ +[CSAudioInjectionServices createAudioInjectionDeviceWithType:bundlePath:deviceName:deviceID:productID:completion:]
+ +[CSAudioInjectionServices createAudioInjectionDeviceWithType:bundlePath:deviceName:deviceID:productID:handlingDaemon:completion:]
+ +[CSAudioInjectionServices injectAudio:toDeviceWithUUID:withNumChannels:withUserIntentOptions:handlingDaemon:started:]
+ +[CSAudioInjectionServices injectAudio:toDeviceWithUUID:withNumChannels:withUserIntentOptions:started:]
+ +[CSAudioInjectionServices selectBuiltInInjectionDeviceWithUUID:completion:]
+ +[CSAudioInjectionServices selectBuiltInInjectionDeviceWithUUID:handlingDaemon:completion:]
+ +[CSEndpointDetectedSelfLogger _decodeFeaturesAtEndpoint:eventType:]
+ +[CSEndpointDetectedSelfLogger emitEndpointDetectedEventWithEndpointerMetrics:eventType:trpId:mhId:]
+ +[CSEndpointerFactory endpointAnalyzer:]
+ +[CSSelfTriggerController _isAVVCRefChannelAvailable]
+ +[CSSelfTriggerController shouldSetupSelfTrigger]
+ +[CSSiriAudioActivationInfo _alertBehaviorForRecordRoute:playbackRoute:speechEvent:speechRecordingMode:ringerState:startingAlertBeepOverideID:presentationMode:usePrelistening:isOnPhoneCall:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:suppressStartAlert:activationHostTime:isVoiceOverSiriSoundsEnabled:]
+ +[CSSiriAudioActivationInfo _alertDictionaryForRecordRoute:playbackRoute:speechEvent:ringerState:startingAlertBeepOverideID:presentationMode:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:activationHostTime:isVoiceOverSiriSoundsEnabled:]
+ +[CSSiriAudioActivationInfo _isJarvisVoiceTriggerSpeechEvent:]
+ -[CSASRFeatures copyWithZone:]
+ -[CSASRFeatures encodeWithCoder:]
+ -[CSASRFeatures initWithCoder:]
+ -[CSAssetController _findLatestInstalledAsset:assetType:]
+ -[CSAssetController _isNeededForOTA:]
+ -[CSAssetController _notInstalledAssetState:assetType:]
+ -[CSAudioInjectionDevice bundlePath]
+ -[CSAudioInjectionDevice initWithDeviceType:bundlePath:deviceName:deviceID:productID:]
+ -[CSAudioInjectionDevice isBundleDevice]
+ -[CSAudioInjectionDevice setBundlePath:]
+ -[CSAudioInjectionProvider _connectBuiltInDevice:withError:]
+ -[CSAudioInjectionProvider _connectPluginDevice:withError:]
+ -[CSAudioInjectionProvider connectDevice:withOutError:]
+ -[CSAudioInjectionProvider primaryBuiltInDevice]
+ -[CSAudioInjectionProvider primaryTvRemoteDevice]
+ -[CSAudioInjectionProvider selectBuiltInDevice:withCompletion:]
+ -[CSAudioInjectionProvider selectedBuiltInBundleDeviceUID]
+ -[CSAudioInjectionProvider setPrimaryBuiltInDevice:]
+ -[CSAudioInjectionProvider setPrimaryTvRemoteDevice:]
+ -[CSAudioInjectionProvider setSelectedBuiltInBundleDeviceUID:]
+ -[CSBuiltInVoiceTrigger isAudioServerAvailable]
+ -[CSBuiltInVoiceTrigger setIsAudioServerAvailable:]
+ -[CSBundleAudioInjectionEngine .cxx_destruct]
+ -[CSBundleAudioInjectionEngine _compensateChannelDataIfNeeded:receivedNumChannels:]
+ -[CSBundleAudioInjectionEngine _defaultOutASBD]
+ -[CSBundleAudioInjectionEngine attachDevice:withOutError:]
+ -[CSBundleAudioInjectionEngine audioBufferAvailable:]
+ -[CSBundleAudioInjectionEngine audioPlugin]
+ -[CSBundleAudioInjectionEngine audioStreamDidStartSuccessfully:error:]
+ -[CSBundleAudioInjectionEngine audioStreamDidStopSuccessfully:error:]
+ -[CSBundleAudioInjectionEngine audioStreamHandleId]
+ -[CSBundleAudioInjectionEngine delegate]
+ -[CSBundleAudioInjectionEngine initWithStreamHandleId:]
+ -[CSBundleAudioInjectionEngine isRecording]
+ -[CSBundleAudioInjectionEngine queue]
+ -[CSBundleAudioInjectionEngine setAudioPlugin:]
+ -[CSBundleAudioInjectionEngine setAudioStreamHandleId:]
+ -[CSBundleAudioInjectionEngine setDelegate:]
+ -[CSBundleAudioInjectionEngine setIsRecording:]
+ -[CSBundleAudioInjectionEngine setPluginBundleWithPath:withOutError:]
+ -[CSBundleAudioInjectionEngine setQueue:]
+ -[CSBundleAudioInjectionEngine setUuid:]
+ -[CSBundleAudioInjectionEngine startAudioStreamWithOption:withOutError:]
+ -[CSBundleAudioInjectionEngine start]
+ -[CSBundleAudioInjectionEngine stopAudioStreamWithOutError:]
+ -[CSBundleAudioInjectionEngine stop]
+ -[CSBundleAudioInjectionEngine uuid]
+ -[CSEndpointAnalyzerBase .cxx_destruct]
+ -[CSEndpointAnalyzerBase _shouldAcceptEagerResultForDuration:asrFeatures:lastReportedEndpointTimeMs:osdFeatures:resultsCompletionHandler:]
+ -[CSEndpointAnalyzerBase activeChannel]
+ -[CSEndpointAnalyzerBase anchorMachAbsTime]
+ -[CSEndpointAnalyzerBase asrFeatureLatencies]
+ -[CSEndpointAnalyzerBase asrFeaturesQueue]
+ -[CSEndpointAnalyzerBase asrFeaturesWarmupLatency]
+ -[CSEndpointAnalyzerBase cachedEndpointerMetrics]
+ -[CSEndpointAnalyzerBase canProcessCurrentRequest]
+ -[CSEndpointAnalyzerBase clampedASRFeatureLatencyMsForClientLag]
+ -[CSEndpointAnalyzerBase clientLagThresholdMs]
+ -[CSEndpointAnalyzerBase currentAsset]
+ -[CSEndpointAnalyzerBase currentRequestSampleRate]
+ -[CSEndpointAnalyzerBase delegate]
+ -[CSEndpointAnalyzerBase didCommunicateEndpoint]
+ -[CSEndpointAnalyzerBase didDetectSpeech]
+ -[CSEndpointAnalyzerBase didNotifyTwoShot]
+ -[CSEndpointAnalyzerBase didReceiveASRFeatures]
+ -[CSEndpointAnalyzerBase didTimestampFirstAudioPacket]
+ -[CSEndpointAnalyzerBase disableRCSelection]
+ -[CSEndpointAnalyzerBase endpointerModelVersion]
+ -[CSEndpointAnalyzerBase epResult]
+ -[CSEndpointAnalyzerBase firstAudioPacketTimestamp]
+ -[CSEndpointAnalyzerBase firstAudioSampleSensorTimestamp]
+ -[CSEndpointAnalyzerBase getHybridEndpointerConfigForAsset:]
+ -[CSEndpointAnalyzerBase getSerialQueueWithName:targetQueue:]
+ -[CSEndpointAnalyzerBase handleVoiceTriggerWithActivationInfo:]
+ -[CSEndpointAnalyzerBase hasAcceptedEagerResult]
+ -[CSEndpointAnalyzerBase hepAudioOriginInMs]
+ -[CSEndpointAnalyzerBase hybridClassifierQueue]
+ -[CSEndpointAnalyzerBase hybridClassifier]
+ -[CSEndpointAnalyzerBase init]
+ -[CSEndpointAnalyzerBase isASRFeatureFromServer]
+ -[CSEndpointAnalyzerBase isAnchorTimeBuffered]
+ -[CSEndpointAnalyzerBase isRequestTimeout]
+ -[CSEndpointAnalyzerBase lastASRFeatureTimestamp]
+ -[CSEndpointAnalyzerBase lastEndpointPosterior]
+ -[CSEndpointAnalyzerBase lastKnownASRFeatureLatency]
+ -[CSEndpointAnalyzerBase lastKnownASRFeatures]
+ -[CSEndpointAnalyzerBase lastKnownOSDFeatures]
+ -[CSEndpointAnalyzerBase lastReportedEndpointTimeMs]
+ -[CSEndpointAnalyzerBase logFeaturesWithEvent:locale:]
+ -[CSEndpointAnalyzerBase mhId]
+ -[CSEndpointAnalyzerBase multimodalEndpointerEnabled]
+ -[CSEndpointAnalyzerBase numSamplesProcessedBeforeAnchorTime]
+ -[CSEndpointAnalyzerBase osdFeaturesAtEndpoint]
+ -[CSEndpointAnalyzerBase postVoiceTriggerSilence]
+ -[CSEndpointAnalyzerBase processASRFeatures:fromServer:]
+ -[CSEndpointAnalyzerBase processAudioSamplesAsynchronously:]
+ -[CSEndpointAnalyzerBase processedAudioInSeconds]
+ -[CSEndpointAnalyzerBase recordContext]
+ -[CSEndpointAnalyzerBase recordingDidStop]
+ -[CSEndpointAnalyzerBase recordingStoppedForReason:]
+ -[CSEndpointAnalyzerBase resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]
+ -[CSEndpointAnalyzerBase setActiveChannel:]
+ -[CSEndpointAnalyzerBase setAnchorMachAbsTime:]
+ -[CSEndpointAnalyzerBase setAsrFeatureLatencies:]
+ -[CSEndpointAnalyzerBase setAsrFeaturesQueue:]
+ -[CSEndpointAnalyzerBase setAsrFeaturesWarmupLatency:]
+ -[CSEndpointAnalyzerBase setCanProcessCurrentRequest:]
+ -[CSEndpointAnalyzerBase setClampedASRFeatureLatencyMsForClientLag:]
+ -[CSEndpointAnalyzerBase setClientLagThresholdMs:]
+ -[CSEndpointAnalyzerBase setCurrentAsset:]
+ -[CSEndpointAnalyzerBase setCurrentRequestSampleRate:]
+ -[CSEndpointAnalyzerBase setDelegate:]
+ -[CSEndpointAnalyzerBase setDidCommunicateEndpoint:]
+ -[CSEndpointAnalyzerBase setDidDetectSpeech:]
+ -[CSEndpointAnalyzerBase setDidNotifyTwoShot:]
+ -[CSEndpointAnalyzerBase setDidReceiveASRFeatures:]
+ -[CSEndpointAnalyzerBase setDidTimestampFirstAudioPacket:]
+ -[CSEndpointAnalyzerBase setDisableRCSelection:]
+ -[CSEndpointAnalyzerBase setEndpointerModelVersion:]
+ -[CSEndpointAnalyzerBase setEndpointerOperationMode:]
+ -[CSEndpointAnalyzerBase setEpResult:]
+ -[CSEndpointAnalyzerBase setFirstAudioPacketTimestamp:]
+ -[CSEndpointAnalyzerBase setFirstAudioSampleSensorTimestamp:]
+ -[CSEndpointAnalyzerBase setHasAcceptedEagerResult:]
+ -[CSEndpointAnalyzerBase setHepAudioOriginInMs:]
+ -[CSEndpointAnalyzerBase setHybridClassifier:]
+ -[CSEndpointAnalyzerBase setHybridClassifierQueue:]
+ -[CSEndpointAnalyzerBase setIsASRFeatureFromServer:]
+ -[CSEndpointAnalyzerBase setIsAnchorTimeBuffered:]
+ -[CSEndpointAnalyzerBase setIsRequestTimeout:]
+ -[CSEndpointAnalyzerBase setLastASRFeatureTimestamp:]
+ -[CSEndpointAnalyzerBase setLastEndpointPosterior:]
+ -[CSEndpointAnalyzerBase setLastKnownASRFeatureLatency:]
+ -[CSEndpointAnalyzerBase setLastKnownASRFeatures:]
+ -[CSEndpointAnalyzerBase setLastKnownOSDFeatures:]
+ -[CSEndpointAnalyzerBase setLastReportedEndpointTimeMs:]
+ -[CSEndpointAnalyzerBase setMhId:]
+ -[CSEndpointAnalyzerBase setNumSamplesProcessedBeforeAnchorTime:]
+ -[CSEndpointAnalyzerBase setOsdFeaturesAtEndpoint:]
+ -[CSEndpointAnalyzerBase setPostVoiceTriggerSilence:]
+ -[CSEndpointAnalyzerBase setProcessedAudioInSeconds:]
+ -[CSEndpointAnalyzerBase setRecordContext:]
+ -[CSEndpointAnalyzerBase setRecordingDidStop:]
+ -[CSEndpointAnalyzerBase setSpeechEndpointDetected:]
+ -[CSEndpointAnalyzerBase setStateSerialQueue:]
+ -[CSEndpointAnalyzerBase setTargetQueue:]
+ -[CSEndpointAnalyzerBase setTwoShotSilenceThresholdInMs:]
+ -[CSEndpointAnalyzerBase setUseDefaultASRFeaturesOnClientLag:]
+ -[CSEndpointAnalyzerBase setVtEndInSampleCount:]
+ -[CSEndpointAnalyzerBase setVtExtraAudioAtStartInMs:]
+ -[CSEndpointAnalyzerBase shouldAcceptEagerResultForDuration:resultsCompletionHandler:]
+ -[CSEndpointAnalyzerBase shouldAcceptEagerResultForDuration:withEndpointerMetrics:resultsCompletionHandler:]
+ -[CSEndpointAnalyzerBase shouldAcceptEagerResultForDurationSync:withEndpointerMetrics:]
+ -[CSEndpointAnalyzerBase shouldProvideTwoShotFeedbackWithRecordContext]
+ -[CSEndpointAnalyzerBase speechEndpointDetected]
+ -[CSEndpointAnalyzerBase stateSerialQueue]
+ -[CSEndpointAnalyzerBase stopEndpointer]
+ -[CSEndpointAnalyzerBase targetQueue]
+ -[CSEndpointAnalyzerBase terminateProcessing]
+ -[CSEndpointAnalyzerBase twoShotSilenceThresholdInMs]
+ -[CSEndpointAnalyzerBase useDefaultASRFeaturesOnClientLag]
+ -[CSEndpointAnalyzerBase vtEndInSampleCount]
+ -[CSEndpointAnalyzerBase vtExtraAudioAtStartInMs]
+ -[CSEndpointDetectedSelfLogger attSiriNode:didDetectEndpointEventAtTime:eventType:withMetrics:usesAutomaticEndpointing:]
+ -[CSEndpointDetectedSelfLogger attSiriNode:didDetectHardEndpointAtTime:withMetrics:usesAutomaticEndpointing:]
+ -[CSEndpointerMetrics endpointerScore]
+ -[CSEndpointerMetrics endpointerThreshold]
+ -[CSEndpointerMetrics initWithTotalAudioRecorded:endpointBufferHostTime:featuresAtEndpoint:endpointerType:asrFeatureLatencyDistribution:additionalMetrics:trailingSilenceDurationAtEndpoint:requestId:osdFeatures:asrFeatures:isRequestTimeOut:assetConfigVersion:blkHepAudioOrigin:vtExtraAudioAtStartInMs:firstAudioSampleSensorTimestamp:isAnchorTimeBuffered:endpointHostTime:audioDeliveryHostTimeDelta:endpointerThreshold:endpointerScore:]
+ -[CSEndpointerMetrics setEndpointerScore:]
+ -[CSEndpointerMetrics setEndpointerThreshold:]
+ -[CSEndpointerXPCClient _deliverHardEndpointDetectedAtTime:withMetrics:eventType:]
+ -[CSEndpointerXPCClient activeChannel]
+ -[CSEndpointerXPCClient cachedEventType]
+ -[CSEndpointerXPCClient delegate]
+ -[CSEndpointerXPCClient didDetectHardEndpointAtTime:withMetrics:eventType:]
+ -[CSEndpointerXPCClient logFeaturesWithEvent:locale:]
+ -[CSEndpointerXPCClient mhId]
+ -[CSEndpointerXPCClient setCachedEventType:]
+ -[CSEndpointerXPCClient setDelegate:]
+ -[CSEndpointerXPCClient setEndpointerModelVersion:]
+ -[CSEndpointerXPCClient setMhId:]
+ -[CSEndpointerXPCClient shouldAcceptEagerResultForDuration:withEndpointerMetrics:resultsCompletionHandler:]
+ -[CSEndpointerXPCClient shouldAcceptEagerResultForDurationSync:withEndpointerMetrics:]
+ -[CSEndpointerXPCClient stopEndpointer]
+ -[CSFileAudioInjectionBuiltInEngine .cxx_destruct]
+ -[CSFileAudioInjectionBuiltInEngine alwaysOnVoiceTriggerEnabled]
+ -[CSFileAudioInjectionBuiltInEngine attachDevice:withOutError:]
+ -[CSFileAudioInjectionBuiltInEngine audioEngineAudioChunkForTvAvailable:audioChunk:]
+ -[CSFileAudioInjectionBuiltInEngine audioEngineBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:isFileLoadedBuffer:]
+ -[CSFileAudioInjectionBuiltInEngine audioEngineDidStartRecord:audioStreamHandleId:successfully:error:]
+ -[CSFileAudioInjectionBuiltInEngine audioEngineDidStopRecord:audioStreamHandleId:reason:]
+ -[CSFileAudioInjectionBuiltInEngine circularBuffer]
+ -[CSFileAudioInjectionBuiltInEngine connectedDevice]
+ -[CSFileAudioInjectionBuiltInEngine dealloc]
+ -[CSFileAudioInjectionBuiltInEngine delegate]
+ -[CSFileAudioInjectionBuiltInEngine getBestSampleCountWithOption:]
+ -[CSFileAudioInjectionBuiltInEngine hostTimeBuffer]
+ -[CSFileAudioInjectionBuiltInEngine initWithStreamHandleId:]
+ -[CSFileAudioInjectionBuiltInEngine injectAudio:]
+ -[CSFileAudioInjectionBuiltInEngine injectAudio:withScaleFactor:playbackStarted:completion:]
+ -[CSFileAudioInjectionBuiltInEngine isAlwaysOnVoiceTriggerAvailable]
+ -[CSFileAudioInjectionBuiltInEngine isForwarding]
+ -[CSFileAudioInjectionBuiltInEngine isRecording]
+ -[CSFileAudioInjectionBuiltInEngine keywordAnalyzer]
+ -[CSFileAudioInjectionBuiltInEngine lastForwardedSampleCount]
+ -[CSFileAudioInjectionBuiltInEngine queue]
+ -[CSFileAudioInjectionBuiltInEngine setAlwaysOnVoiceTriggerEnabled:]
+ -[CSFileAudioInjectionBuiltInEngine setCircularBuffer:]
+ -[CSFileAudioInjectionBuiltInEngine setConnectedDevice:]
+ -[CSFileAudioInjectionBuiltInEngine setDelegate:]
+ -[CSFileAudioInjectionBuiltInEngine setHostTimeBuffer:]
+ -[CSFileAudioInjectionBuiltInEngine setIsForwarding:]
+ -[CSFileAudioInjectionBuiltInEngine setKeywordAnalyzer:]
+ -[CSFileAudioInjectionBuiltInEngine setLastForwardedSampleCount:]
+ -[CSFileAudioInjectionBuiltInEngine setQueue:]
+ -[CSFileAudioInjectionBuiltInEngine setUserIntentOptions:]
+ -[CSFileAudioInjectionBuiltInEngine setUuid:]
+ -[CSFileAudioInjectionBuiltInEngine setVoiceTriggerEnabled:]
+ -[CSFileAudioInjectionBuiltInEngine setVoiceTriggerSampleCount:]
+ -[CSFileAudioInjectionBuiltInEngine startAudioStreamWithOption:withOutError:]
+ -[CSFileAudioInjectionBuiltInEngine start]
+ -[CSFileAudioInjectionBuiltInEngine stopAudioStreamWithOutError:]
+ -[CSFileAudioInjectionBuiltInEngine stop]
+ -[CSFileAudioInjectionBuiltInEngine userIntentOptions]
+ -[CSFileAudioInjectionBuiltInEngine uuid]
+ -[CSFileAudioInjectionBuiltInEngine voiceTriggerEnabled]
+ -[CSFileAudioInjectionBuiltInEngine voiceTriggerSampleCount]
+ -[CSFileAudioInjectionEngine .cxx_destruct]
+ -[CSFileAudioInjectionEngine _compensateChannelDataIfNeeded:receivedNumChannels:]
+ -[CSFileAudioInjectionEngine _createDeInterleaverIfNeeded]
+ -[CSFileAudioInjectionEngine _defaultOutASBD]
+ -[CSFileAudioInjectionEngine _deinterleaveBufferIfNeeded:]
+ -[CSFileAudioInjectionEngine _readAudioBufferAndFeed]
+ -[CSFileAudioInjectionEngine _startAudioFeedingTimer]
+ -[CSFileAudioInjectionEngine alwaysOnVoiceTriggerEnabled]
+ -[CSFileAudioInjectionEngine attachDevice:withOutError:]
+ -[CSFileAudioInjectionEngine audioFeedTimer]
+ -[CSFileAudioInjectionEngine audioStreamHandleId]
+ -[CSFileAudioInjectionEngine bufferDuration]
+ -[CSFileAudioInjectionEngine dealloc]
+ -[CSFileAudioInjectionEngine deinterleaver]
+ -[CSFileAudioInjectionEngine delegate]
+ -[CSFileAudioInjectionEngine didSetScaleFactor]
+ -[CSFileAudioInjectionEngine fileOption]
+ -[CSFileAudioInjectionEngine initWithStreamHandleId:]
+ -[CSFileAudioInjectionEngine initWithStreamHandleId:withInputRecordingNumberOfChannels:]
+ -[CSFileAudioInjectionEngine injectAudio:]
+ -[CSFileAudioInjectionEngine injectAudio:withScaleFactor:outASBD:playbackStarted:completion:]
+ -[CSFileAudioInjectionEngine injectAudio:withScaleFactor:playbackStarted:completion:]
+ -[CSFileAudioInjectionEngine injectionAudioFileList]
+ -[CSFileAudioInjectionEngine injectionCompletionNotifyBlocks]
+ -[CSFileAudioInjectionEngine injectionStartNotifyBlocks]
+ -[CSFileAudioInjectionEngine inputRecordingNumberOfChannels]
+ -[CSFileAudioInjectionEngine isAlwaysOnVoiceTriggerAvailable]
+ -[CSFileAudioInjectionEngine isRecording]
+ -[CSFileAudioInjectionEngine outASBD]
+ -[CSFileAudioInjectionEngine pNonInterleavedABL]
+ -[CSFileAudioInjectionEngine queue]
+ -[CSFileAudioInjectionEngine scaleFactor]
+ -[CSFileAudioInjectionEngine setAlwaysOnVoiceTriggerEnabled:]
+ -[CSFileAudioInjectionEngine setAudioFeedTimer:]
+ -[CSFileAudioInjectionEngine setAudioStreamHandleId:]
+ -[CSFileAudioInjectionEngine setBufferDuration:]
+ -[CSFileAudioInjectionEngine setDeinterleaver:]
+ -[CSFileAudioInjectionEngine setDelegate:]
+ -[CSFileAudioInjectionEngine setDidSetScaleFactor:]
+ -[CSFileAudioInjectionEngine setFileOption:]
+ -[CSFileAudioInjectionEngine setInjectionAudioFileList:]
+ -[CSFileAudioInjectionEngine setInjectionCompletionNotifyBlocks:]
+ -[CSFileAudioInjectionEngine setInjectionStartNotifyBlocks:]
+ -[CSFileAudioInjectionEngine setInputRecordingNumberOfChannels:]
+ -[CSFileAudioInjectionEngine setIsRecording:]
+ -[CSFileAudioInjectionEngine setOutASBD:]
+ -[CSFileAudioInjectionEngine setPNonInterleavedABL:]
+ -[CSFileAudioInjectionEngine setQueue:]
+ -[CSFileAudioInjectionEngine setScaleFactor:]
+ -[CSFileAudioInjectionEngine setStartInjectBlock:]
+ -[CSFileAudioInjectionEngine setUserIntentOptions:]
+ -[CSFileAudioInjectionEngine setUuid:]
+ -[CSFileAudioInjectionEngine startAudioStreamWithOption:withOutError:]
+ -[CSFileAudioInjectionEngine startInjectBlock]
+ -[CSFileAudioInjectionEngine start]
+ -[CSFileAudioInjectionEngine stopAudioStreamWithOutError:]
+ -[CSFileAudioInjectionEngine stop]
+ -[CSFileAudioInjectionEngine uuid]
+ -[CSFileAudioInjectionHearstEngine .cxx_destruct]
+ -[CSFileAudioInjectionHearstEngine alwaysOnVoiceTriggerEnabled]
+ -[CSFileAudioInjectionHearstEngine attachDevice:withOutError:]
+ -[CSFileAudioInjectionHearstEngine audioEngineAudioChunkForTvAvailable:audioChunk:]
+ -[CSFileAudioInjectionHearstEngine audioEngineBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:isFileLoadedBuffer:]
+ -[CSFileAudioInjectionHearstEngine audioEngineDidStartRecord:audioStreamHandleId:successfully:error:]
+ -[CSFileAudioInjectionHearstEngine audioEngineDidStopRecord:audioStreamHandleId:reason:]
+ -[CSFileAudioInjectionHearstEngine circularBuffer]
+ -[CSFileAudioInjectionHearstEngine connectedDevice]
+ -[CSFileAudioInjectionHearstEngine dealloc]
+ -[CSFileAudioInjectionHearstEngine delegate]
+ -[CSFileAudioInjectionHearstEngine initWithStreamHandleId:]
+ -[CSFileAudioInjectionHearstEngine injectAudio:]
+ -[CSFileAudioInjectionHearstEngine injectAudio:withScaleFactor:playbackStarted:completion:]
+ -[CSFileAudioInjectionHearstEngine isAlwaysOnVoiceTriggerAvailable]
+ -[CSFileAudioInjectionHearstEngine isForwarding]
+ -[CSFileAudioInjectionHearstEngine isRecording]
+ -[CSFileAudioInjectionHearstEngine keywordAnalyzer]
+ -[CSFileAudioInjectionHearstEngine lastDetectedVoiceTriggerBeginSampleCount]
+ -[CSFileAudioInjectionHearstEngine lastForwardedSampleCount]
+ -[CSFileAudioInjectionHearstEngine queue]
+ -[CSFileAudioInjectionHearstEngine setAlwaysOnVoiceTriggerEnabled:]
+ -[CSFileAudioInjectionHearstEngine setCircularBuffer:]
+ -[CSFileAudioInjectionHearstEngine setConnectedDevice:]
+ -[CSFileAudioInjectionHearstEngine setDelegate:]
+ -[CSFileAudioInjectionHearstEngine setIsForwarding:]
+ -[CSFileAudioInjectionHearstEngine setKeywordAnalyzer:]
+ -[CSFileAudioInjectionHearstEngine setLastDetectedVoiceTriggerBeginSampleCount:]
+ -[CSFileAudioInjectionHearstEngine setLastForwardedSampleCount:]
+ -[CSFileAudioInjectionHearstEngine setQueue:]
+ -[CSFileAudioInjectionHearstEngine setUuid:]
+ -[CSFileAudioInjectionHearstEngine setVoiceTriggerEnabled:]
+ -[CSFileAudioInjectionHearstEngine startAudioStreamWithOption:withOutError:]
+ -[CSFileAudioInjectionHearstEngine start]
+ -[CSFileAudioInjectionHearstEngine stopAudioStreamWithOutError:]
+ -[CSFileAudioInjectionHearstEngine stop]
+ -[CSFileAudioInjectionHearstEngine uuid]
+ -[CSFileAudioInjectionHearstEngine voiceTriggerEnabled]
+ -[CSFileAudioInjectionRemoraEngine .cxx_destruct]
+ -[CSFileAudioInjectionRemoraEngine alwaysOnVoiceTriggerEnabled]
+ -[CSFileAudioInjectionRemoraEngine attachDevice:withOutError:]
+ -[CSFileAudioInjectionRemoraEngine audioEngineAudioChunkForTvAvailable:audioChunk:]
+ -[CSFileAudioInjectionRemoraEngine audioEngineBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:isFileLoadedBuffer:]
+ -[CSFileAudioInjectionRemoraEngine audioEngineDidStartRecord:audioStreamHandleId:successfully:error:]
+ -[CSFileAudioInjectionRemoraEngine audioEngineDidStopRecord:audioStreamHandleId:reason:]
+ -[CSFileAudioInjectionRemoraEngine circularBuffer]
+ -[CSFileAudioInjectionRemoraEngine connectedDevice]
+ -[CSFileAudioInjectionRemoraEngine dealloc]
+ -[CSFileAudioInjectionRemoraEngine delegate]
+ -[CSFileAudioInjectionRemoraEngine initWithStreamHandleId:]
+ -[CSFileAudioInjectionRemoraEngine injectAudio:]
+ -[CSFileAudioInjectionRemoraEngine injectAudio:withScaleFactor:playbackStarted:completion:]
+ -[CSFileAudioInjectionRemoraEngine isAlwaysOnVoiceTriggerAvailable]
+ -[CSFileAudioInjectionRemoraEngine isForwarding]
+ -[CSFileAudioInjectionRemoraEngine isRecording]
+ -[CSFileAudioInjectionRemoraEngine keywordAnalyzer]
+ -[CSFileAudioInjectionRemoraEngine lastDetectedVoiceTriggerBeginSampleCount]
+ -[CSFileAudioInjectionRemoraEngine lastForwardedSampleCount]
+ -[CSFileAudioInjectionRemoraEngine queue]
+ -[CSFileAudioInjectionRemoraEngine setAlwaysOnVoiceTriggerEnabled:]
+ -[CSFileAudioInjectionRemoraEngine setCircularBuffer:]
+ -[CSFileAudioInjectionRemoraEngine setConnectedDevice:]
+ -[CSFileAudioInjectionRemoraEngine setDelegate:]
+ -[CSFileAudioInjectionRemoraEngine setIsForwarding:]
+ -[CSFileAudioInjectionRemoraEngine setKeywordAnalyzer:]
+ -[CSFileAudioInjectionRemoraEngine setLastDetectedVoiceTriggerBeginSampleCount:]
+ -[CSFileAudioInjectionRemoraEngine setLastForwardedSampleCount:]
+ -[CSFileAudioInjectionRemoraEngine setQueue:]
+ -[CSFileAudioInjectionRemoraEngine setUuid:]
+ -[CSFileAudioInjectionRemoraEngine setVoiceTriggerEnabled:]
+ -[CSFileAudioInjectionRemoraEngine startAudioStreamWithOption:withOutError:]
+ -[CSFileAudioInjectionRemoraEngine start]
+ -[CSFileAudioInjectionRemoraEngine stopAudioStreamWithOutError:]
+ -[CSFileAudioInjectionRemoraEngine stop]
+ -[CSFileAudioInjectionRemoraEngine uuid]
+ -[CSFileAudioInjectionRemoraEngine voiceTriggerEnabled]
+ -[CSFileAudioInjectionTvRemoteEngine .cxx_destruct]
+ -[CSFileAudioInjectionTvRemoteEngine alwaysOnVoiceTriggerEnabled]
+ -[CSFileAudioInjectionTvRemoteEngine attachDevice:withOutError:]
+ -[CSFileAudioInjectionTvRemoteEngine audioConverterDidConvertPackets:packets:durationInSec:timestamp:arrivalTimestampToAudioRecorder:]
+ -[CSFileAudioInjectionTvRemoteEngine audioEngineAudioChunkForTvAvailable:audioChunk:]
+ -[CSFileAudioInjectionTvRemoteEngine audioEngineBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:isFileLoadedBuffer:]
+ -[CSFileAudioInjectionTvRemoteEngine audioEngineDidStartRecord:audioStreamHandleId:successfully:error:]
+ -[CSFileAudioInjectionTvRemoteEngine audioEngineDidStopRecord:audioStreamHandleId:reason:]
+ -[CSFileAudioInjectionTvRemoteEngine connectedDevice]
+ -[CSFileAudioInjectionTvRemoteEngine delegate]
+ -[CSFileAudioInjectionTvRemoteEngine encoder]
+ -[CSFileAudioInjectionTvRemoteEngine initWithStreamHandleId:]
+ -[CSFileAudioInjectionTvRemoteEngine injectAudio:]
+ -[CSFileAudioInjectionTvRemoteEngine injectAudio:withScaleFactor:playbackStarted:completion:]
+ -[CSFileAudioInjectionTvRemoteEngine isAlwaysOnVoiceTriggerAvailable]
+ -[CSFileAudioInjectionTvRemoteEngine isRecording]
+ -[CSFileAudioInjectionTvRemoteEngine queue]
+ -[CSFileAudioInjectionTvRemoteEngine setAlwaysOnVoiceTriggerEnabled:]
+ -[CSFileAudioInjectionTvRemoteEngine setConnectedDevice:]
+ -[CSFileAudioInjectionTvRemoteEngine setDelegate:]
+ -[CSFileAudioInjectionTvRemoteEngine setEncoder:]
+ -[CSFileAudioInjectionTvRemoteEngine setQueue:]
+ -[CSFileAudioInjectionTvRemoteEngine setUuid:]
+ -[CSFileAudioInjectionTvRemoteEngine startAudioStreamWithOption:withOutError:]
+ -[CSFileAudioInjectionTvRemoteEngine start]
+ -[CSFileAudioInjectionTvRemoteEngine stopAudioStreamWithOutError:]
+ -[CSFileAudioInjectionTvRemoteEngine stop]
+ -[CSFileAudioInjectionTvRemoteEngine uuid]
+ -[CSHybridEndpointAnalyzer _generateEndpointerFeaturesWithEffectiveClientProcessedAudioMs:osdFeatures:completion:]
+ -[CSHybridEndpointAnalyzer _isTaskStringAccessible:]
+ -[CSHybridEndpointAnalyzer _processEnhancedEndpointerTaskString:]
+ -[CSHybridEndpointAnalyzer _swapEnhancedEndpointerModelForTaskString:]
+ -[CSHybridEndpointAnalyzer _updateAccessibleEndpointerThresholdIfNeeded]
+ -[CSHybridEndpointAnalyzer _updateCurrentAsset:]
+ -[CSHybridEndpointAnalyzer _updateEndpointerDelayedTrigger:]
+ -[CSHybridEndpointAnalyzer _updateEndpointerDelayedTriggerByMhId:]
+ -[CSHybridEndpointAnalyzer _updateEndpointerThreshold:]
+ -[CSHybridEndpointAnalyzer _updateEnhancedEndpointerDefaultThresholdPartial:defaultThresholdRC:relaxedThresholdPartial:relaxedThresholdRC:]
+ -[CSHybridEndpointAnalyzer _useEnhancedEndpointer]
+ -[CSHybridEndpointAnalyzer accessibleEndpointerEnabled]
+ -[CSHybridEndpointAnalyzer audioDeliveryHostTimeDelta]
+ -[CSHybridEndpointAnalyzer currentEndpointerThreshold]
+ -[CSHybridEndpointAnalyzer currentTaskString]
+ -[CSHybridEndpointAnalyzer didReceiveRCFeatures]
+ -[CSHybridEndpointAnalyzer endpointerAssetManagerDidUpdateAsset:]
+ -[CSHybridEndpointAnalyzer endpointerAssetManagerDidUpdateOSDAsset:]
+ -[CSHybridEndpointAnalyzer endpointerOperationMode]
+ -[CSHybridEndpointAnalyzer enhancedEndpointerDefaultResult]
+ -[CSHybridEndpointAnalyzer enhancedEndpointerTaskThresholdMap]
+ -[CSHybridEndpointAnalyzer enhancedEndpointer]
+ -[CSHybridEndpointAnalyzer extraDelayFrequency]
+ -[CSHybridEndpointAnalyzer lastKnownRCFeatureLatency]
+ -[CSHybridEndpointAnalyzer lastKnownRCFeatures]
+ -[CSHybridEndpointAnalyzer logAnchorMachAbsTime:numSamplesProcessedBeforeAnchorTime:isAnchorTimeBuffered:audioDeliveryHostTimeDelta:]
+ -[CSHybridEndpointAnalyzer processFirstAudioPacketTimestamp:firstAudioSampleSensorTimestamp:]
+ -[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]
+ -[CSHybridEndpointAnalyzer processRCFeatures:]
+ -[CSHybridEndpointAnalyzer processTaskString:]
+ -[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]
+ -[CSHybridEndpointAnalyzer setAccessibleEndpointerEnabled:]
+ -[CSHybridEndpointAnalyzer setAudioDeliveryHostTimeDelta:]
+ -[CSHybridEndpointAnalyzer setCurrentEndpointerThreshold:]
+ -[CSHybridEndpointAnalyzer setCurrentTaskString:]
+ -[CSHybridEndpointAnalyzer setDidReceiveRCFeatures:]
+ -[CSHybridEndpointAnalyzer setEnhancedEndpointer:]
+ -[CSHybridEndpointAnalyzer setEnhancedEndpointerDefaultResult:]
+ -[CSHybridEndpointAnalyzer setEnhancedEndpointerTaskThresholdMap:]
+ -[CSHybridEndpointAnalyzer setExtraDelayFrequency:]
+ -[CSHybridEndpointAnalyzer setLastKnownRCFeatureLatency:]
+ -[CSHybridEndpointAnalyzer setLastKnownRCFeatures:]
+ -[CSHybridEndpointAnalyzer setTaskEnhancedEndpointerMap:]
+ -[CSHybridEndpointAnalyzer setTaskThresholdMap:]
+ -[CSHybridEndpointAnalyzer taskEnhancedEndpointerMap]
+ -[CSHybridEndpointAnalyzer taskThresholdMap]
+ -[CSRemoraEndpointAnalyzer .cxx_destruct]
+ -[CSRemoraEndpointAnalyzer CSAssetManagerDidDownloadNewAsset:]
+ -[CSRemoraEndpointAnalyzer CSLanguageCodeUpdateMonitor:didReceiveLanguageCodeChanged:]
+ -[CSRemoraEndpointAnalyzer _emitEndpointDetectedEventWithEndpointTimeMs:endpointBufferHostTime:endpointerFeatures:endpointerDecisionLagInNs:extraDelayMs:endpointScore:asrFeaturesLatencies:]
+ -[CSRemoraEndpointAnalyzer _loadAndSetupEndpointerAssetIfNecessary]
+ -[CSRemoraEndpointAnalyzer _readParametersFromHEPAsset:]
+ -[CSRemoraEndpointAnalyzer _updateAssetWithCurrentLanguage]
+ -[CSRemoraEndpointAnalyzer _updateAssetWithLanguage:]
+ -[CSRemoraEndpointAnalyzer activeChannel]
+ -[CSRemoraEndpointAnalyzer apQueue]
+ -[CSRemoraEndpointAnalyzer delegate]
+ -[CSRemoraEndpointAnalyzer didAddAudio]
+ -[CSRemoraEndpointAnalyzer endpointerModelVersion]
+ -[CSRemoraEndpointAnalyzer init]
+ -[CSRemoraEndpointAnalyzer mhId]
+ -[CSRemoraEndpointAnalyzer numSamplesProcessed]
+ -[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]
+ -[CSRemoraEndpointAnalyzer osdAnalyzer]
+ -[CSRemoraEndpointAnalyzer osdQueue]
+ -[CSRemoraEndpointAnalyzer processAudioSamplesAsynchronously:]
+ -[CSRemoraEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]
+ -[CSRemoraEndpointAnalyzer setActiveChannel:]
+ -[CSRemoraEndpointAnalyzer setApQueue:]
+ -[CSRemoraEndpointAnalyzer setDelegate:]
+ -[CSRemoraEndpointAnalyzer setDidAddAudio:]
+ -[CSRemoraEndpointAnalyzer setEndpointerModelVersion:]
+ -[CSRemoraEndpointAnalyzer setEndpointerOperationMode:]
+ -[CSRemoraEndpointAnalyzer setMhId:]
+ -[CSRemoraEndpointAnalyzer setNumSamplesProcessed:]
+ -[CSRemoraEndpointAnalyzer setOsdAnalyzer:]
+ -[CSRemoraEndpointAnalyzer setOsdQueue:]
+ -[CSRemoraEndpointAnalyzer terminateProcessing]
+ -[CSSelfTriggerController initWithTargetQueue:audioProviderSelecting:]
+ -[CSSelfTriggerDetector audioProviderSelecting]
+ -[CSSelfTriggerDetector initWithTargetQueue:audioProviderSelecting:audioSourceType:]
+ -[CSSelfTriggerDetector setAudioProviderSelecting:]
+ -[CSSelfTriggerDetector setTapProviderType:]
+ -[CSSelfTriggerDetector tapProviderType]
+ -[CSSiriSpeechRecorder _playStopAlertIfNecessaryForReason:error:]
+ -[CSSiriSpeechRecorder endpointer:detectedTwoShotAtTime:]
+ -[CSSiriSpeechRecorder endpointer:didDetectHardEndpointAtTime:withMetrics:eventType:]
+ -[CSSmartSiriVolume audioProviderSelector]
+ -[CSSmartSiriVolume setAudioProviderSelector:]
+ -[CSSmartSiriVolume startSmartSiriVolumeWithAudioProviderSelector:]
+ -[CSSmartSiriVolumeManager startSmartSiriVolumeWithAudioProviderSelector:]
+ -[CSSpeechController _considerSmartRoutingForAudioRecordContext:]
+ -[CSSpeechController detectedTwoShotAtTime:]
+ -[CSSpeechController initWithEndpointId:xpcClientFactory:endpointAnalyzer:continuousVoiceTrigger:siriVolumeController:mediaPlayingMonitor:alarmMonitor:timerMonitor:audioSessionController:supportPhatic:supportHearstVoiceTrigger:supportTriagleModeSessionActivationRetry:supportSessionActivateDelay:supportsDuckingOnSpeakerEvaluator:]
+ -[CSSpeechController setEndpointAnalyzer:]
+ -[CSSpeechManager _tearDownBuiltInVoiceTrigger]
+ -[CSSpeechManager audioTapProviderWithType:]
+ -[CSSpeechManager audioTapProviders]
+ -[CSSpeechManager setAudioTapProviders:]
+ -[CSXPCClient attachTandemStream:withConfig:toPrimaryStream:completion:]
+ GCC_except_table1246
+ GCC_except_table1258
+ GCC_except_table1461
+ GCC_except_table1527
+ GCC_except_table1551
+ GCC_except_table1555
+ GCC_except_table1571
+ GCC_except_table1602
+ GCC_except_table1700
+ GCC_except_table1702
+ GCC_except_table1704
+ GCC_except_table1710
+ GCC_except_table1794
+ GCC_except_table1800
+ GCC_except_table1881
+ GCC_except_table1901
+ GCC_except_table2017
+ GCC_except_table2165
+ GCC_except_table2195
+ GCC_except_table2198
+ GCC_except_table2201
+ GCC_except_table2206
+ GCC_except_table2218
+ GCC_except_table2223
+ GCC_except_table2226
+ GCC_except_table2343
+ GCC_except_table2346
+ GCC_except_table2350
+ GCC_except_table2368
+ GCC_except_table2501
+ GCC_except_table2558
+ GCC_except_table2570
+ GCC_except_table2624
+ GCC_except_table2633
+ GCC_except_table2669
+ GCC_except_table2670
+ GCC_except_table2671
+ GCC_except_table2675
+ GCC_except_table2678
+ GCC_except_table2681
+ GCC_except_table2686
+ GCC_except_table2687
+ GCC_except_table2696
+ GCC_except_table2702
+ GCC_except_table2704
+ GCC_except_table2705
+ GCC_except_table2772
+ GCC_except_table3032
+ GCC_except_table3180
+ GCC_except_table3183
+ GCC_except_table3186
+ GCC_except_table3217
+ GCC_except_table3277
+ GCC_except_table3482
+ GCC_except_table3508
+ GCC_except_table3570
+ GCC_except_table3572
+ GCC_except_table3574
+ GCC_except_table3590
+ GCC_except_table3592
+ GCC_except_table3594
+ GCC_except_table3596
+ GCC_except_table3598
+ GCC_except_table3600
+ GCC_except_table3602
+ GCC_except_table3605
+ GCC_except_table3613
+ GCC_except_table3616
+ GCC_except_table3622
+ GCC_except_table3624
+ GCC_except_table3626
+ GCC_except_table3628
+ GCC_except_table3630
+ GCC_except_table3635
+ GCC_except_table3639
+ GCC_except_table3648
+ GCC_except_table3651
+ GCC_except_table3659
+ GCC_except_table3667
+ GCC_except_table3802
+ GCC_except_table3826
+ GCC_except_table3886
+ GCC_except_table3902
+ GCC_except_table3923
+ GCC_except_table4015
+ GCC_except_table4263
+ GCC_except_table4330
+ GCC_except_table4335
+ GCC_except_table4342
+ GCC_except_table4367
+ GCC_except_table4417
+ GCC_except_table4423
+ GCC_except_table4690
+ GCC_except_table4697
+ GCC_except_table4704
+ GCC_except_table4710
+ GCC_except_table4790
+ GCC_except_table4946
+ GCC_except_table4956
+ GCC_except_table4980
+ GCC_except_table5000
+ GCC_except_table5083
+ GCC_except_table5097
+ GCC_except_table5106
+ GCC_except_table5113
+ GCC_except_table5119
+ GCC_except_table5124
+ GCC_except_table5151
+ GCC_except_table5152
+ GCC_except_table5157
+ GCC_except_table5163
+ GCC_except_table5168
+ GCC_except_table5170
+ GCC_except_table5172
+ GCC_except_table5174
+ GCC_except_table5175
+ GCC_except_table5176
+ GCC_except_table5177
+ GCC_except_table5179
+ GCC_except_table5180
+ GCC_except_table5181
+ GCC_except_table5182
+ GCC_except_table5183
+ GCC_except_table5185
+ GCC_except_table5186
+ GCC_except_table5187
+ GCC_except_table5189
+ GCC_except_table5204
+ GCC_except_table5278
+ GCC_except_table5282
+ GCC_except_table5336
+ GCC_except_table5365
+ GCC_except_table5368
+ GCC_except_table5448
+ GCC_except_table5462
+ GCC_except_table5469
+ GCC_except_table5481
+ GCC_except_table5485
+ GCC_except_table5495
+ GCC_except_table5723
+ GCC_except_table5754
+ GCC_except_table5759
+ GCC_except_table5796
+ GCC_except_table5805
+ GCC_except_table5832
+ GCC_except_table5900
+ GCC_except_table6090
+ GCC_except_table6098
+ GCC_except_table6118
+ GCC_except_table6123
+ GCC_except_table6229
+ GCC_except_table6284
+ GCC_except_table6375
+ GCC_except_table6376
+ GCC_except_table6386
+ GCC_except_table6387
+ GCC_except_table6399
+ GCC_except_table6428
+ GCC_except_table6439
+ GCC_except_table6444
+ GCC_except_table6449
+ GCC_except_table6477
+ GCC_except_table6562
+ GCC_except_table6574
+ GCC_except_table6597
+ GCC_except_table6608
+ GCC_except_table6611
+ GCC_except_table6634
+ GCC_except_table6646
+ GCC_except_table6926
+ GCC_except_table6961
+ GCC_except_table7034
+ GCC_except_table7088
+ GCC_except_table7110
+ GCC_except_table7151
+ GCC_except_table7162
+ GCC_except_table7302
+ GCC_except_table7310
+ GCC_except_table7416
+ GCC_except_table7417
+ GCC_except_table7418
+ GCC_except_table7419
+ GCC_except_table7425
+ GCC_except_table7488
+ GCC_except_table7530
+ GCC_except_table7555
+ GCC_except_table7570
+ GCC_except_table7578
+ GCC_except_table7584
+ GCC_except_table7609
+ GCC_except_table7615
+ GCC_except_table7621
+ GCC_except_table7757
+ GCC_except_table916
+ GCC_except_table928
+ GCC_except_table931
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._anchorMachAbsTime
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._asrFeatureLatencies
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._asrFeaturesQueue
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._asrFeaturesWarmupLatency
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._canProcessCurrentRequest
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._clampedASRFeatureLatencyMsForClientLag
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._clientLagThresholdMs
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._currentAsset
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._currentRequestSampleRate
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._didCommunicateEndpoint
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._didDetectSpeech
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._didNotifyTwoShot
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._didReceiveASRFeatures
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._didTimestampFirstAudioPacket
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._disableRCSelection
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._epResult
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._firstAudioPacketTimestamp
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._firstAudioSampleSensorTimestamp
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._hasAcceptedEagerResult
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._hepAudioOriginInMs
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._hybridClassifier
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._hybridClassifierQueue
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._isASRFeatureFromServer
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._isAnchorTimeBuffered
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._isRequestTimeout
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._lastASRFeatureTimestamp
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._lastEndpointPosterior
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._lastKnownASRFeatureLatency
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._lastKnownASRFeatures
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._lastKnownOSDFeatures
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._lastReportedEndpointTimeMs
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._numSamplesProcessedBeforeAnchorTime
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._osdFeaturesAtEndpoint
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._postVoiceTriggerSilence
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._processedAudioInSeconds
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._recordContext
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._recordingDidStop
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._speechEndpointDetected
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._stateSerialQueue
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._targetQueue
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._twoShotSilenceThresholdInMs
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._useDefaultASRFeaturesOnClientLag
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._vtEndInSampleCount
+ OBJC_IVAR_$_CSEndpointAnalyzerBase._vtExtraAudioAtStartInMs
+ _AFHasRingerSwitch
+ _AFSpeechEventIsSmartRoutingEligible
+ _AudioConverterFillComplexBuffer_BlockInvoke.26224
+ _CSHearstRouteStatusGetName
+ _MobileTimerLibrary.800
+ _MobileTimerLibraryCore.frameworkLibrary.805
+ _OBJC_CLASS_$_CSBundleAudioInjectionEngine
+ _OBJC_CLASS_$_CSEndpointAnalyzerBase
+ _OBJC_CLASS_$_CSFileAudioInjectionBuiltInEngine
+ _OBJC_CLASS_$_CSFileAudioInjectionEngine
+ _OBJC_CLASS_$_CSFileAudioInjectionHearstEngine
+ _OBJC_CLASS_$_CSFileAudioInjectionRemoraEngine
+ _OBJC_CLASS_$_CSFileAudioInjectionTvRemoteEngine
+ _OBJC_CLASS_$_CSOtherAppRecordingStateMonitorFactory
+ _OBJC_CLASS_$_CSRemoraEndpointAnalyzer
+ _OBJC_CLASS_$_CSSecureSessionHandler
+ _OBJC_CLASS_$_CSVoiceOverSiriSoundsSettingsReader
+ _OBJC_CLASS_$_SFModelTaskSet
+ _OBJC_IVAR_$_CSAudioInjectionDevice._bundlePath
+ _OBJC_IVAR_$_CSAudioInjectionProvider._primaryBuiltInDevice
+ _OBJC_IVAR_$_CSAudioInjectionProvider._primaryTvRemoteDevice
+ _OBJC_IVAR_$_CSAudioInjectionProvider._selectedBuiltInBundleDeviceUID
+ _OBJC_IVAR_$_CSBuiltInVoiceTrigger._isAudioServerAvailable
+ _OBJC_IVAR_$_CSBundleAudioInjectionEngine._audioPlugin
+ _OBJC_IVAR_$_CSBundleAudioInjectionEngine._audioStreamHandleId
+ _OBJC_IVAR_$_CSBundleAudioInjectionEngine._delegate
+ _OBJC_IVAR_$_CSBundleAudioInjectionEngine._isRecording
+ _OBJC_IVAR_$_CSBundleAudioInjectionEngine._queue
+ _OBJC_IVAR_$_CSBundleAudioInjectionEngine._uuid
+ _OBJC_IVAR_$_CSEndpointAnalyzerBase._activeChannel
+ _OBJC_IVAR_$_CSEndpointAnalyzerBase._delegate
+ _OBJC_IVAR_$_CSEndpointAnalyzerBase._endpointerModelVersion
+ _OBJC_IVAR_$_CSEndpointAnalyzerBase._mhId
+ _OBJC_IVAR_$_CSEndpointerMetrics._endpointerScore
+ _OBJC_IVAR_$_CSEndpointerMetrics._endpointerThreshold
+ _OBJC_IVAR_$_CSEndpointerXPCClient._cachedEventType
+ _OBJC_IVAR_$_CSEndpointerXPCClient._delegate
+ _OBJC_IVAR_$_CSEndpointerXPCClient._mhId
+ _OBJC_IVAR_$_CSFileAudioInjectionBuiltInEngine._circularBuffer
+ _OBJC_IVAR_$_CSFileAudioInjectionBuiltInEngine._connectedDevice
+ _OBJC_IVAR_$_CSFileAudioInjectionBuiltInEngine._delegate
+ _OBJC_IVAR_$_CSFileAudioInjectionBuiltInEngine._hostTimeBuffer
+ _OBJC_IVAR_$_CSFileAudioInjectionBuiltInEngine._isForwarding
+ _OBJC_IVAR_$_CSFileAudioInjectionBuiltInEngine._keywordAnalyzer
+ _OBJC_IVAR_$_CSFileAudioInjectionBuiltInEngine._lastForwardedSampleCount
+ _OBJC_IVAR_$_CSFileAudioInjectionBuiltInEngine._queue
+ _OBJC_IVAR_$_CSFileAudioInjectionBuiltInEngine._userIntentOptions
+ _OBJC_IVAR_$_CSFileAudioInjectionBuiltInEngine._uuid
+ _OBJC_IVAR_$_CSFileAudioInjectionBuiltInEngine._voiceTriggerEnabled
+ _OBJC_IVAR_$_CSFileAudioInjectionBuiltInEngine._voiceTriggerSampleCount
+ _OBJC_IVAR_$_CSFileAudioInjectionEngine._audioFeedTimer
+ _OBJC_IVAR_$_CSFileAudioInjectionEngine._audioStreamHandleId
+ _OBJC_IVAR_$_CSFileAudioInjectionEngine._bufferDuration
+ _OBJC_IVAR_$_CSFileAudioInjectionEngine._deinterleaver
+ _OBJC_IVAR_$_CSFileAudioInjectionEngine._delegate
+ _OBJC_IVAR_$_CSFileAudioInjectionEngine._didSetScaleFactor
+ _OBJC_IVAR_$_CSFileAudioInjectionEngine._fileOption
+ _OBJC_IVAR_$_CSFileAudioInjectionEngine._injectionAudioFileList
+ _OBJC_IVAR_$_CSFileAudioInjectionEngine._injectionCompletionNotifyBlocks
+ _OBJC_IVAR_$_CSFileAudioInjectionEngine._injectionStartNotifyBlocks
+ _OBJC_IVAR_$_CSFileAudioInjectionEngine._inputRecordingNumberOfChannels
+ _OBJC_IVAR_$_CSFileAudioInjectionEngine._isRecording
+ _OBJC_IVAR_$_CSFileAudioInjectionEngine._outASBD
+ _OBJC_IVAR_$_CSFileAudioInjectionEngine._pNonInterleavedABL
+ _OBJC_IVAR_$_CSFileAudioInjectionEngine._queue
+ _OBJC_IVAR_$_CSFileAudioInjectionEngine._scaleFactor
+ _OBJC_IVAR_$_CSFileAudioInjectionEngine._startInjectBlock
+ _OBJC_IVAR_$_CSFileAudioInjectionEngine._uuid
+ _OBJC_IVAR_$_CSFileAudioInjectionHearstEngine._circularBuffer
+ _OBJC_IVAR_$_CSFileAudioInjectionHearstEngine._connectedDevice
+ _OBJC_IVAR_$_CSFileAudioInjectionHearstEngine._delegate
+ _OBJC_IVAR_$_CSFileAudioInjectionHearstEngine._isForwarding
+ _OBJC_IVAR_$_CSFileAudioInjectionHearstEngine._keywordAnalyzer
+ _OBJC_IVAR_$_CSFileAudioInjectionHearstEngine._lastDetectedVoiceTriggerBeginSampleCount
+ _OBJC_IVAR_$_CSFileAudioInjectionHearstEngine._lastForwardedSampleCount
+ _OBJC_IVAR_$_CSFileAudioInjectionHearstEngine._queue
+ _OBJC_IVAR_$_CSFileAudioInjectionHearstEngine._uuid
+ _OBJC_IVAR_$_CSFileAudioInjectionHearstEngine._voiceTriggerEnabled
+ _OBJC_IVAR_$_CSFileAudioInjectionRemoraEngine._circularBuffer
+ _OBJC_IVAR_$_CSFileAudioInjectionRemoraEngine._connectedDevice
+ _OBJC_IVAR_$_CSFileAudioInjectionRemoraEngine._delegate
+ _OBJC_IVAR_$_CSFileAudioInjectionRemoraEngine._isForwarding
+ _OBJC_IVAR_$_CSFileAudioInjectionRemoraEngine._keywordAnalyzer
+ _OBJC_IVAR_$_CSFileAudioInjectionRemoraEngine._lastDetectedVoiceTriggerBeginSampleCount
+ _OBJC_IVAR_$_CSFileAudioInjectionRemoraEngine._lastForwardedSampleCount
+ _OBJC_IVAR_$_CSFileAudioInjectionRemoraEngine._queue
+ _OBJC_IVAR_$_CSFileAudioInjectionRemoraEngine._uuid
+ _OBJC_IVAR_$_CSFileAudioInjectionRemoraEngine._voiceTriggerEnabled
+ _OBJC_IVAR_$_CSFileAudioInjectionTvRemoteEngine._connectedDevice
+ _OBJC_IVAR_$_CSFileAudioInjectionTvRemoteEngine._delegate
+ _OBJC_IVAR_$_CSFileAudioInjectionTvRemoteEngine._encoder
+ _OBJC_IVAR_$_CSFileAudioInjectionTvRemoteEngine._queue
+ _OBJC_IVAR_$_CSFileAudioInjectionTvRemoteEngine._uuid
+ _OBJC_IVAR_$_CSHybridEndpointAnalyzer._accessibleEndpointerEnabled
+ _OBJC_IVAR_$_CSHybridEndpointAnalyzer._audioDeliveryHostTimeDelta
+ _OBJC_IVAR_$_CSHybridEndpointAnalyzer._currentEndpointerThreshold
+ _OBJC_IVAR_$_CSHybridEndpointAnalyzer._currentTaskString
+ _OBJC_IVAR_$_CSHybridEndpointAnalyzer._didReceiveRCFeatures
+ _OBJC_IVAR_$_CSHybridEndpointAnalyzer._endpointerOperationMode
+ _OBJC_IVAR_$_CSHybridEndpointAnalyzer._enhancedEndpointer
+ _OBJC_IVAR_$_CSHybridEndpointAnalyzer._enhancedEndpointerDefaultResult
+ _OBJC_IVAR_$_CSHybridEndpointAnalyzer._enhancedEndpointerTaskThresholdMap
+ _OBJC_IVAR_$_CSHybridEndpointAnalyzer._extraDelayFrequency
+ _OBJC_IVAR_$_CSHybridEndpointAnalyzer._lastKnownRCFeatureLatency
+ _OBJC_IVAR_$_CSHybridEndpointAnalyzer._lastKnownRCFeatures
+ _OBJC_IVAR_$_CSHybridEndpointAnalyzer._taskEnhancedEndpointerMap
+ _OBJC_IVAR_$_CSHybridEndpointAnalyzer._taskThresholdMap
+ _OBJC_IVAR_$_CSRemoraEndpointAnalyzer._activeChannel
+ _OBJC_IVAR_$_CSRemoraEndpointAnalyzer._apQueue
+ _OBJC_IVAR_$_CSRemoraEndpointAnalyzer._delegate
+ _OBJC_IVAR_$_CSRemoraEndpointAnalyzer._didAddAudio
+ _OBJC_IVAR_$_CSRemoraEndpointAnalyzer._endpointerModelVersion
+ _OBJC_IVAR_$_CSRemoraEndpointAnalyzer._mhId
+ _OBJC_IVAR_$_CSRemoraEndpointAnalyzer._numSamplesProcessed
+ _OBJC_IVAR_$_CSRemoraEndpointAnalyzer._osdAnalyzer
+ _OBJC_IVAR_$_CSRemoraEndpointAnalyzer._osdQueue
+ _OBJC_IVAR_$_CSSelfTriggerDetector._audioProviderSelecting
+ _OBJC_IVAR_$_CSSelfTriggerDetector._tapProviderType
+ _OBJC_IVAR_$_CSSmartSiriVolume._audioProviderSelector
+ _OBJC_IVAR_$_CSSpeechController._endpointAnalyzer
+ _OBJC_IVAR_$_CSSpeechManager._audioTapProviders
+ _OBJC_METACLASS_$_CSBundleAudioInjectionEngine
+ _OBJC_METACLASS_$_CSEndpointAnalyzerBase
+ _OBJC_METACLASS_$_CSFileAudioInjectionBuiltInEngine
+ _OBJC_METACLASS_$_CSFileAudioInjectionEngine
+ _OBJC_METACLASS_$_CSFileAudioInjectionHearstEngine
+ _OBJC_METACLASS_$_CSFileAudioInjectionRemoraEngine
+ _OBJC_METACLASS_$_CSFileAudioInjectionTvRemoteEngine
+ _OBJC_METACLASS_$_CSRemoraEndpointAnalyzer
+ __OBJC_$_CLASS_METHODS_CSSelfTriggerController
+ __OBJC_$_CLASS_PROP_LIST_CSASRFeatures
+ __OBJC_$_INSTANCE_METHODS_CSBundleAudioInjectionEngine
+ __OBJC_$_INSTANCE_METHODS_CSEndpointAnalyzerBase
+ __OBJC_$_INSTANCE_METHODS_CSFileAudioInjectionBuiltInEngine
+ __OBJC_$_INSTANCE_METHODS_CSFileAudioInjectionEngine
+ __OBJC_$_INSTANCE_METHODS_CSFileAudioInjectionHearstEngine
+ __OBJC_$_INSTANCE_METHODS_CSFileAudioInjectionRemoraEngine
+ __OBJC_$_INSTANCE_METHODS_CSFileAudioInjectionTvRemoteEngine
+ __OBJC_$_INSTANCE_METHODS_CSRemoraEndpointAnalyzer
+ __OBJC_$_INSTANCE_VARIABLES_CSBundleAudioInjectionEngine
+ __OBJC_$_INSTANCE_VARIABLES_CSEndpointAnalyzerBase
+ __OBJC_$_INSTANCE_VARIABLES_CSFileAudioInjectionBuiltInEngine
+ __OBJC_$_INSTANCE_VARIABLES_CSFileAudioInjectionEngine
+ __OBJC_$_INSTANCE_VARIABLES_CSFileAudioInjectionHearstEngine
+ __OBJC_$_INSTANCE_VARIABLES_CSFileAudioInjectionRemoraEngine
+ __OBJC_$_INSTANCE_VARIABLES_CSFileAudioInjectionTvRemoteEngine
+ __OBJC_$_INSTANCE_VARIABLES_CSRemoraEndpointAnalyzer
+ __OBJC_$_PROP_LIST_CSAudioInjectionEngineProtocol
+ __OBJC_$_PROP_LIST_CSBundleAudioInjectionEngine
+ __OBJC_$_PROP_LIST_CSBundleAudioProviding
+ __OBJC_$_PROP_LIST_CSEndpointAnalyzerBase
+ __OBJC_$_PROP_LIST_CSFileAudioInjectionBuiltInEngine
+ __OBJC_$_PROP_LIST_CSFileAudioInjectionEngine
+ __OBJC_$_PROP_LIST_CSFileAudioInjectionHearstEngine
+ __OBJC_$_PROP_LIST_CSFileAudioInjectionRemoraEngine
+ __OBJC_$_PROP_LIST_CSFileAudioInjectionTvRemoteEngine
+ __OBJC_$_PROP_LIST_CSRemoraEndpointAnalyzer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioInjectionEngineProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSBundleAudioProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEagerResultAnalyzer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSBundleAudioDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioInjectionEngineProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSBundleAudioDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSBundleAudioProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSEagerResultAnalyzer
+ __OBJC_$_PROTOCOL_REFS_CSBundleAudioDelegate
+ __OBJC_$_PROTOCOL_REFS_CSBundleAudioProviding
+ __OBJC_$_PROTOCOL_REFS_CSEagerResultAnalyzer
+ __OBJC_$_PROTOCOL_REFS_CSEndpointerXPCService
+ __OBJC_CLASS_PROTOCOLS_$_CSASRFeatures
+ __OBJC_CLASS_PROTOCOLS_$_CSBundleAudioInjectionEngine
+ __OBJC_CLASS_PROTOCOLS_$_CSEndpointAnalyzerBase
+ __OBJC_CLASS_PROTOCOLS_$_CSFileAudioInjectionBuiltInEngine
+ __OBJC_CLASS_PROTOCOLS_$_CSFileAudioInjectionEngine
+ __OBJC_CLASS_PROTOCOLS_$_CSFileAudioInjectionHearstEngine
+ __OBJC_CLASS_PROTOCOLS_$_CSFileAudioInjectionRemoraEngine
+ __OBJC_CLASS_PROTOCOLS_$_CSFileAudioInjectionTvRemoteEngine
+ __OBJC_CLASS_PROTOCOLS_$_CSRemoraEndpointAnalyzer
+ __OBJC_CLASS_RO_$_CSBundleAudioInjectionEngine
+ __OBJC_CLASS_RO_$_CSEndpointAnalyzerBase
+ __OBJC_CLASS_RO_$_CSFileAudioInjectionBuiltInEngine
+ __OBJC_CLASS_RO_$_CSFileAudioInjectionEngine
+ __OBJC_CLASS_RO_$_CSFileAudioInjectionHearstEngine
+ __OBJC_CLASS_RO_$_CSFileAudioInjectionRemoraEngine
+ __OBJC_CLASS_RO_$_CSFileAudioInjectionTvRemoteEngine
+ __OBJC_CLASS_RO_$_CSRemoraEndpointAnalyzer
+ __OBJC_LABEL_PROTOCOL_$_CSAudioInjectionEngineProtocol
+ __OBJC_LABEL_PROTOCOL_$_CSBundleAudioDelegate
+ __OBJC_LABEL_PROTOCOL_$_CSBundleAudioProviding
+ __OBJC_LABEL_PROTOCOL_$_CSEagerResultAnalyzer
+ __OBJC_METACLASS_RO_$_CSBundleAudioInjectionEngine
+ __OBJC_METACLASS_RO_$_CSEndpointAnalyzerBase
+ __OBJC_METACLASS_RO_$_CSFileAudioInjectionBuiltInEngine
+ __OBJC_METACLASS_RO_$_CSFileAudioInjectionEngine
+ __OBJC_METACLASS_RO_$_CSFileAudioInjectionHearstEngine
+ __OBJC_METACLASS_RO_$_CSFileAudioInjectionRemoraEngine
+ __OBJC_METACLASS_RO_$_CSFileAudioInjectionTvRemoteEngine
+ __OBJC_METACLASS_RO_$_CSRemoraEndpointAnalyzer
+ __OBJC_PROTOCOL_$_CSAudioInjectionEngineProtocol
+ __OBJC_PROTOCOL_$_CSBundleAudioDelegate
+ __OBJC_PROTOCOL_$_CSBundleAudioProviding
+ __OBJC_PROTOCOL_$_CSEagerResultAnalyzer
+ __OBJC_PROTOCOL_REFERENCE_$_CSBundleAudioProviding
+ __ZNKSt3__111__copy_implclB8ne200100IPNS_6vectorINS2_IfNS_9allocatorIfEEEENS3_IS5_EEEES8_S8_EENS_4pairIT_T1_EESA_T0_SB_
+ __ZNKSt3__111__copy_implclB8ne200100IPNS_6vectorIfNS_9allocatorIfEEEES6_S6_EENS_4pairIT_T1_EES8_T0_S9_
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt12out_of_rangeC1B8ne200100EPKc
+ __ZNSt3__110unique_ptrI15SmartSiriVolumeNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
+ __ZNSt3__110unique_ptrIN10corespeech25CSAudioCircularBufferImplIhEENS_14default_deleteIS3_EEE5resetB8ne200100EPS3_
+ __ZNSt3__114__split_bufferIPjNS_9allocatorIS1_EEE12emplace_backIJRS1_EEEvDpOT_
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorINS_4pairIfjEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__120__throw_out_of_rangeB8ne200100EPKc
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorINS3_IfNS2_IfEEEENS2_IS5_EEEEEEPS7_EEED2B8ne200100Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIfNS2_IfEEEEEEPS5_EEED2B8ne200100Ev
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ne200100INS_9allocatorINS_6vectorINS2_IfNS1_IfEEEENS1_IS4_EEEEEEPS6_S8_S8_EET2_RT_T0_T1_S9_
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ne200100INS_9allocatorINS_6vectorIfNS1_IfEEEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
+ __ZNSt3__16vectorINS0_INS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEEENS1_IS7_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE16__init_with_sizeB8ne200100IPS5_S9_EEvT_T0_m
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__destroy_vectorclB8ne200100Ev
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__init_with_sizeB8ne200100IPS3_S7_EEvT_T0_m
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE18__assign_with_sizeB8ne200100IPS3_S7_EEvT_T0_l
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE5clearB8ne200100Ev
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEEC2B8ne200100EmRKS3_
+ __ZNSt3__16vectorINS_4pairIfjEENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne200100Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB8ne200100IPfS5_EEvT_T0_m
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB8ne200100IPfS5_EEvT_T0_l
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne200100EmRKf
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne200100Ev
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ ___102-[CSEndpointerXPCClient resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.22
+ ___105-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke
+ ___105-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.431
+ ___105-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.435
+ ___105-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.438
+ ___105-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke_2
+ ___105-[CSRemoraEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke
+ ___105-[CSRemoraEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.87
+ ___105-[CSRemoraEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.89
+ ___105-[CSRemoraEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.91
+ ___105-[CSRemoraEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke_2
+ ___107-[CSEndpointerXPCClient shouldAcceptEagerResultForDuration:withEndpointerMetrics:resultsCompletionHandler:]_block_invoke
+ ___108-[CSEndpointAnalyzerBase shouldAcceptEagerResultForDuration:withEndpointerMetrics:resultsCompletionHandler:]_block_invoke
+ ___109-[CSEndpointDetectedSelfLogger attSiriNode:didDetectHardEndpointAtTime:withMetrics:usesAutomaticEndpointing:]_block_invoke
+ ___110+[CSAudioInjectionServices injectAudio:toDeviceWithUUID:withfadingTimeWindowLength:handlingDaemon:completion:]_block_invoke.17
+ ___110-[CSSiriSpeechRecorder speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:]_block_invoke.182
+ ___114-[CSHybridEndpointAnalyzer _generateEndpointerFeaturesWithEffectiveClientProcessedAudioMs:osdFeatures:completion:]_block_invoke
+ ___118+[CSAudioInjectionServices injectAudio:toDeviceWithUUID:withNumChannels:withUserIntentOptions:handlingDaemon:started:]_block_invoke
+ ___118+[CSAudioInjectionServices injectAudio:toDeviceWithUUID:withNumChannels:withUserIntentOptions:handlingDaemon:started:]_block_invoke.20
+ ___118+[CSAudioInjectionServices injectAudio:toDeviceWithUUID:withNumChannels:withUserIntentOptions:handlingDaemon:started:]_block_invoke_2
+ ___119+[CSAudioInjectionServices createAudioInjectionDeviceWithType:deviceName:deviceID:productID:handlingDaemon:completion:]_block_invoke.14
+ ___119+[CSAudioInjectionServices createAudioInjectionDeviceWithType:deviceName:deviceID:productID:handlingDaemon:completion:]_block_invoke.15
+ ___120-[CSEndpointDetectedSelfLogger attSiriNode:didDetectEndpointEventAtTime:eventType:withMetrics:usesAutomaticEndpointing:]_block_invoke
+ ___121+[CSAudioInjectionServices injectAudio:toDeviceWithUUID:withNumChannels:withUserIntentOptions:handlingDaemon:completion:]_block_invoke.18
+ ___126-[CSFileAudioInjectionHearstEngine audioEngineBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:isFileLoadedBuffer:]_block_invoke
+ ___126-[CSFileAudioInjectionHearstEngine audioEngineBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:isFileLoadedBuffer:]_block_invoke_2
+ ___126-[CSFileAudioInjectionRemoraEngine audioEngineBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:isFileLoadedBuffer:]_block_invoke
+ ___126-[CSFileAudioInjectionRemoraEngine audioEngineBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:isFileLoadedBuffer:]_block_invoke_2
+ ___127-[CSFileAudioInjectionBuiltInEngine audioEngineBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:isFileLoadedBuffer:]_block_invoke
+ ___130+[CSAudioInjectionServices createAudioInjectionDeviceWithType:bundlePath:deviceName:deviceID:productID:handlingDaemon:completion:]_block_invoke
+ ___130+[CSAudioInjectionServices createAudioInjectionDeviceWithType:bundlePath:deviceName:deviceID:productID:handlingDaemon:completion:]_block_invoke.12
+ ___130+[CSAudioInjectionServices createAudioInjectionDeviceWithType:bundlePath:deviceName:deviceID:productID:handlingDaemon:completion:]_block_invoke.13
+ ___130+[CSAudioInjectionServices createAudioInjectionDeviceWithType:bundlePath:deviceName:deviceID:productID:handlingDaemon:completion:]_block_invoke_2
+ ___133-[CSHybridEndpointAnalyzer logAnchorMachAbsTime:numSamplesProcessedBeforeAnchorTime:isAnchorTimeBuffered:audioDeliveryHostTimeDelta:]_block_invoke
+ ___139-[CSHybridEndpointAnalyzer _updateEnhancedEndpointerDefaultThresholdPartial:defaultThresholdRC:relaxedThresholdPartial:relaxedThresholdRC:]_block_invoke
+ ___145-[CSSiriSpeechRecorder _speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:errorCodeOverride:underlyingError:]_block_invoke.186
+ ___145-[CSSiriSpeechRecorder _speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:errorCodeOverride:underlyingError:]_block_invoke_2.187
+ ___189-[CSRemoraEndpointAnalyzer _emitEndpointDetectedEventWithEndpointTimeMs:endpointBufferHostTime:endpointerFeatures:endpointerDecisionLagInNs:extraDelayMs:endpointScore:asrFeaturesLatencies:]_block_invoke
+ ___189-[CSRemoraEndpointAnalyzer _emitEndpointDetectedEventWithEndpointTimeMs:endpointBufferHostTime:endpointerFeatures:endpointerDecisionLagInNs:extraDelayMs:endpointScore:asrFeaturesLatencies:]_block_invoke_2
+ ___32+[CSSpeechManager sharedManager]_block_invoke
+ ___32-[CSRemoraEndpointAnalyzer init]_block_invoke
+ ___331-[CSSpeechController initWithEndpointId:xpcClientFactory:endpointAnalyzer:continuousVoiceTrigger:siriVolumeController:mediaPlayingMonitor:alarmMonitor:timerMonitor:audioSessionController:supportPhatic:supportHearstVoiceTrigger:supportTriagleModeSessionActivationRetry:supportSessionActivateDelay:supportsDuckingOnSpeakerEvaluator:]_block_invoke
+ ___331-[CSSpeechController initWithEndpointId:xpcClientFactory:endpointAnalyzer:continuousVoiceTrigger:siriVolumeController:mediaPlayingMonitor:alarmMonitor:timerMonitor:audioSessionController:supportPhatic:supportHearstVoiceTrigger:supportTriagleModeSessionActivationRetry:supportSessionActivateDelay:supportsDuckingOnSpeakerEvaluator:]_block_invoke_2
+ ___34-[CSFileAudioInjectionEngine stop]_block_invoke
+ ___35-[CSFileAudioInjectionEngine start]_block_invoke
+ ___36-[CSBundleAudioInjectionEngine stop]_block_invoke
+ ___36-[CSRemoraEndpointAnalyzer setMhId:]_block_invoke
+ ___37-[CSBundleAudioInjectionEngine start]_block_invoke
+ ___39-[CSEndpointerXPCClient stopEndpointer]_block_invoke
+ ___40-[CSFileAudioInjectionHearstEngine stop]_block_invoke
+ ___40-[CSFileAudioInjectionRemoraEngine stop]_block_invoke
+ ___41-[CSFileAudioInjectionBuiltInEngine stop]_block_invoke
+ ___41-[CSFileAudioInjectionEngine isRecording]_block_invoke
+ ___41-[CSFileAudioInjectionHearstEngine start]_block_invoke
+ ___41-[CSFileAudioInjectionRemoraEngine start]_block_invoke
+ ___42-[CSFileAudioInjectionBuiltInEngine start]_block_invoke
+ ___42-[CSFileAudioInjectionBuiltInEngine start]_block_invoke.20
+ ___43-[CSP2PService _sendVoiceProfile:toPeerId:]_block_invoke.362
+ ___43-[CSP2PService _sendVoiceProfile:toPeerId:]_block_invoke.363
+ ___43-[CSP2PService _sendVoiceProfile:toPeerId:]_block_invoke.364
+ ___43-[CSSpeechManager registerSiriClientProxy:]_block_invoke
+ ___44-[CSSpeechController detectedTwoShotAtTime:]_block_invoke
+ ___44-[CSSpeechManager audioTapProviderWithType:]_block_invoke
+ ___46-[CSHybridEndpointAnalyzer processRCFeatures:]_block_invoke
+ ___46-[CSHybridEndpointAnalyzer processTaskString:]_block_invoke
+ ___46-[CSHybridEndpointAnalyzer processTaskString:]_block_invoke.391
+ ___47-[CSFileAudioInjectionHearstEngine isRecording]_block_invoke
+ ___47-[CSFileAudioInjectionRemoraEngine isRecording]_block_invoke
+ ___47-[CSRemoraEndpointAnalyzer terminateProcessing]_block_invoke
+ ___47-[CSSiriSpeechRecorder playRecordingStartAlert]_block_invoke.156
+ ___48-[CSEndpointerXPCClient _createClientConnection]_block_invoke.136
+ ___48-[CSEndpointerXPCClient _createClientConnection]_block_invoke.137
+ ___48-[CSFileAudioInjectionBuiltInEngine isRecording]_block_invoke
+ ___48-[CSSpeechController CSXPCClient:didDisconnect:]_block_invoke.367
+ ___49-[CSAssetController _downloadAsset:withComplete:]_block_invoke.327
+ ___49-[CSP2PService _sendAcousticGradingDataToPeerId:]_block_invoke.369
+ ___50-[CSRemoraEndpointAnalyzer endpointerModelVersion]_block_invoke
+ ___50-[CSSiriSpeechRecorder _playPhaticWithCompletion:]_block_invoke.247
+ ___52-[CSSelfTriggerDetector _startListenWithCompletion:]_block_invoke.21
+ ___52-[CSSpeechController setCurrentRecordContext:error:]_block_invoke.246
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.39
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.44
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.48
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.55
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke_2.56
+ ___53-[CSBundleAudioInjectionEngine audioBufferAvailable:]_block_invoke
+ ___53-[CSEndpointerXPCClient logFeaturesWithEvent:locale:]_block_invoke
+ ___53-[CSFileAudioInjectionEngine _startAudioFeedingTimer]_block_invoke
+ ___53-[CSRemoraEndpointAnalyzer _updateAssetWithLanguage:]_block_invoke
+ ___54-[CSAssetController fetchRemoteMetaOfType:allowRetry:]_block_invoke.315
+ ___54-[CSEndpointAnalyzerBase logFeaturesWithEvent:locale:]_block_invoke
+ ___54-[CSEndpointAnalyzerBase logFeaturesWithEvent:locale:]_block_invoke_2
+ ___54-[CSEndpointAnalyzerBase logFeaturesWithEvent:locale:]_block_invoke_3
+ ___54-[CSEndpointAnalyzerBase logFeaturesWithEvent:locale:]_block_invoke_4
+ ___54-[CSSelfTriggerDetector _stopListeningWithCompletion:]_block_invoke.22
+ ___54-[CSSpeechController prepareRecordWithSettings:error:]_block_invoke.221
+ ___54-[CSSpeechController prepareRecordWithSettings:error:]_block_invoke.230
+ ___55-[CSAudioInjectionProvider connectDevice:withOutError:]_block_invoke
+ ___55-[CSHybridEndpointAnalyzer _updateEndpointerThreshold:]_block_invoke
+ ___55-[CSHybridEndpointAnalyzer setEndpointerOperationMode:]_block_invoke
+ ___55-[CSSpeechController startRecordingWithSettings:error:]_block_invoke.276
+ ___55-[CSSpeechController startRecordingWithSettings:error:]_block_invoke.284
+ ___55-[CSSpeechController startRecordingWithSettings:error:]_block_invoke_2.285
+ ___56-[CSEndpointAnalyzerBase processASRFeatures:fromServer:]_block_invoke
+ ___56-[CSEndpointAnalyzerBase processASRFeatures:fromServer:]_block_invoke_2
+ ___56-[CSRemoraEndpointAnalyzer _readParametersFromHEPAsset:]_block_invoke
+ ___56-[CSSiriSpeechRecorder performBlockAfterAlerts:timeout:]_block_invoke.257
+ ___58-[CSFileAudioInjectionEngine stopAudioStreamWithOutError:]_block_invoke
+ ___60-[CSBundleAudioInjectionEngine stopAudioStreamWithOutError:]_block_invoke
+ ___60-[CSHybridEndpointAnalyzer _updateEndpointerDelayedTrigger:]_block_invoke
+ ___60-[CSSpeechController handleStopRecordingRequestWithOptions:]_block_invoke.298
+ ___61-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke
+ ___61-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.59
+ ___61-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.60
+ ___61-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.62
+ ___61-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.63
+ ___61-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.68
+ ___61-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.71
+ ___61-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke_2
+ ___61-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke_2.69
+ ___61-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke_3
+ ___62-[CSRemoraEndpointAnalyzer processAudioSamplesAsynchronously:]_block_invoke
+ ___62-[CSRemoraEndpointAnalyzer processAudioSamplesAsynchronously:]_block_invoke.54
+ ___62-[CSRemoraEndpointAnalyzer processAudioSamplesAsynchronously:]_block_invoke_2
+ ___63-[CSAudioInjectionProvider selectBuiltInDevice:withCompletion:]_block_invoke
+ ___63-[CSEndpointAnalyzerBase handleVoiceTriggerWithActivationInfo:]_block_invoke
+ ___63-[CSFileAudioInjectionHearstEngine alwaysOnVoiceTriggerEnabled]_block_invoke
+ ___63-[CSFileAudioInjectionRemoraEngine alwaysOnVoiceTriggerEnabled]_block_invoke
+ ___63-[CSHybridEndpointAnalyzer fetchCurrentEndpointerOperationMode]_block_invoke
+ ___64-[CSEndpointerAssetManager _registerForAssetUpdateNotifications]_block_invoke.308
+ ___64-[CSFileAudioInjectionBuiltInEngine alwaysOnVoiceTriggerEnabled]_block_invoke
+ ___64-[CSFileAudioInjectionHearstEngine stopAudioStreamWithOutError:]_block_invoke
+ ___64-[CSFileAudioInjectionRemoraEngine stopAudioStreamWithOutError:]_block_invoke
+ ___64-[CSVoiceTriggerSecondPass _syncVoiceProfileEmbeddingsToExclave]_block_invoke.229
+ ___65-[CSFileAudioInjectionBuiltInEngine stopAudioStreamWithOutError:]_block_invoke
+ ___65-[CSHybridEndpointAnalyzer _processEnhancedEndpointerTaskString:]_block_invoke
+ ___65-[CSHybridEndpointAnalyzer endpointerAssetManagerDidUpdateAsset:]_block_invoke
+ ___66-[CSHybridEndpointAnalyzer _updateEndpointerDelayedTriggerByMhId:]_block_invoke
+ ___67-[CSFileAudioInjectionHearstEngine setAlwaysOnVoiceTriggerEnabled:]_block_invoke
+ ___67-[CSFileAudioInjectionRemoraEngine setAlwaysOnVoiceTriggerEnabled:]_block_invoke
+ ___67-[CSSmartSiriVolume startSmartSiriVolumeWithAudioProviderSelector:]_block_invoke
+ ___67-[CSSmartSiriVolume startSmartSiriVolumeWithAudioProviderSelector:]_block_invoke.53
+ ___67-[CSSmartSiriVolume startSmartSiriVolumeWithAudioProviderSelector:]_block_invoke_2
+ ___68-[CSFileAudioInjectionBuiltInEngine setAlwaysOnVoiceTriggerEnabled:]_block_invoke
+ ___68-[CSTrialAssetDownloadMonitor _validateDownloadedAssetForAssetType:]_block_invoke.49
+ ___68-[CSTrialAssetDownloadMonitor _validateDownloadedAssetForAssetType:]_block_invoke.50
+ ___68-[CSVoiceTriggerSecondPass _processSecondPassInExclave:rejectBlock:]_block_invoke.100
+ ___70-[CSFileAudioInjectionEngine startAudioStreamWithOption:withOutError:]_block_invoke
+ ___70-[CSSiriSpeechRecorder _startAudioPlaybackRequest:options:completion:]_block_invoke.258
+ ___72-[CSBundleAudioInjectionEngine startAudioStreamWithOption:withOutError:]_block_invoke
+ ___73-[CSSiriSpeechRecorder _performTwoShotPromptForType:withOverride:atTime:]_block_invoke.246
+ ___75-[CSEndpointerXPCClient didDetectHardEndpointAtTime:withMetrics:eventType:]_block_invoke
+ ___76+[CSAudioInjectionServices connectDeviceWithUUID:handlingDaemon:completion:]_block_invoke.21
+ ___76+[CSAudioInjectionServices connectDeviceWithUUID:handlingDaemon:completion:]_block_invoke.22
+ ___76-[CSFileAudioInjectionHearstEngine startAudioStreamWithOption:withOutError:]_block_invoke
+ ___76-[CSFileAudioInjectionRemoraEngine startAudioStreamWithOption:withOutError:]_block_invoke
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.396
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.397
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.398
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.400
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.401
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.404
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.409
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.413
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke_2
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke_2.402
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke_3
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke_4
+ ___77-[CSFileAudioInjectionBuiltInEngine startAudioStreamWithOption:withOutError:]_block_invoke
+ ___77-[CSSiriSpeechRecorder startSpeechCaptureWithContext:willStartHandler:error:]_block_invoke.111
+ ___79+[CSAudioInjectionServices disconnectDeviceWithUUID:handlingDaemon:completion:]_block_invoke.23
+ ___79+[CSAudioInjectionServices disconnectDeviceWithUUID:handlingDaemon:completion:]_block_invoke.24
+ ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.232
+ ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.242
+ ___84+[CSAudioInjectionServices primaryInputDeviceUUIDWithhandlingDaemon:WithCompletion:]_block_invoke.25
+ ___84+[CSAudioInjectionServices primaryInputDeviceUUIDWithhandlingDaemon:WithCompletion:]_block_invoke.26
+ ___84-[CSSiriSpeechRecorder speechControllerLPCMRecordBufferAvailable:buffer:recordedAt:]_block_invoke.202
+ ___85-[CSSiriSpeechRecorder endpointer:didDetectHardEndpointAtTime:withMetrics:eventType:]_block_invoke
+ ___85-[CSSiriSpeechRecorder endpointer:didDetectHardEndpointAtTime:withMetrics:eventType:]_block_invoke.227
+ ___86-[CSEndpointAnalyzerBase shouldAcceptEagerResultForDuration:resultsCompletionHandler:]_block_invoke
+ ___86-[CSEndpointAnalyzerBase shouldAcceptEagerResultForDuration:resultsCompletionHandler:]_block_invoke_2
+ ___86-[CSEndpointerXPCClient shouldAcceptEagerResultForDurationSync:withEndpointerMetrics:]_block_invoke
+ ___87-[CSEndpointAnalyzerBase shouldAcceptEagerResultForDurationSync:withEndpointerMetrics:]_block_invoke
+ ___87-[CSEndpointAnalyzerBase shouldAcceptEagerResultForDurationSync:withEndpointerMetrics:]_block_invoke_2
+ ___91+[CSAudioInjectionServices selectBuiltInInjectionDeviceWithUUID:handlingDaemon:completion:]_block_invoke
+ ___91+[CSAudioInjectionServices selectBuiltInInjectionDeviceWithUUID:handlingDaemon:completion:]_block_invoke.10
+ ___91+[CSAudioInjectionServices selectBuiltInInjectionDeviceWithUUID:handlingDaemon:completion:]_block_invoke.9
+ ___91+[CSAudioInjectionServices selectBuiltInInjectionDeviceWithUUID:handlingDaemon:completion:]_block_invoke_2
+ ___93-[CSFileAudioInjectionEngine injectAudio:withScaleFactor:outASBD:playbackStarted:completion:]_block_invoke
+ ___93-[CSFileAudioInjectionEngine injectAudio:withScaleFactor:outASBD:playbackStarted:completion:]_block_invoke.20
+ ___93-[CSFileAudioInjectionEngine injectAudio:withScaleFactor:outASBD:playbackStarted:completion:]_block_invoke_2
+ ___93-[CSHybridEndpointAnalyzer processFirstAudioPacketTimestamp:firstAudioSampleSensorTimestamp:]_block_invoke
+ ___93-[CSVoiceTriggerSecondPass _handleVoiceTriggerFirstPassFromAOP:audioProviderUUID:completion:]_block_invoke.113
+ ___97-[CSSiriSpeechRecorder speechControllerDidDetectVoiceTriggerTwoShot:atTime:wantsAudibleFeedback:]_block_invoke.213
+ ___97-[CSSiriSpeechRecorder speechControllerDidDetectVoiceTriggerTwoShot:atTime:wantsAudibleFeedback:]_block_invoke_2.214
+ ___97-[CSSiriSpeechRecordingContext _donateRecordedAudioForVoiceIdentificationTrainingWithCompletion:]_block_invoke.79
+ ___Block_byref_object_copy_.10146
+ ___Block_byref_object_copy_.10616
+ ___Block_byref_object_copy_.11822
+ ___Block_byref_object_copy_.13117
+ ___Block_byref_object_copy_.13536
+ ___Block_byref_object_copy_.1447
+ ___Block_byref_object_copy_.14596
+ ___Block_byref_object_copy_.14931
+ ___Block_byref_object_copy_.15801
+ ___Block_byref_object_copy_.15917
+ ___Block_byref_object_copy_.17542
+ ___Block_byref_object_copy_.1779
+ ___Block_byref_object_copy_.17833
+ ___Block_byref_object_copy_.18979
+ ___Block_byref_object_copy_.20116
+ ___Block_byref_object_copy_.20765
+ ___Block_byref_object_copy_.21377
+ ___Block_byref_object_copy_.21616
+ ___Block_byref_object_copy_.22248
+ ___Block_byref_object_copy_.2273
+ ___Block_byref_object_copy_.22901
+ ___Block_byref_object_copy_.23171
+ ___Block_byref_object_copy_.23906
+ ___Block_byref_object_copy_.24704
+ ___Block_byref_object_copy_.25133
+ ___Block_byref_object_copy_.25970
+ ___Block_byref_object_copy_.26405
+ ___Block_byref_object_copy_.2668
+ ___Block_byref_object_copy_.27219
+ ___Block_byref_object_copy_.3647
+ ___Block_byref_object_copy_.3781
+ ___Block_byref_object_copy_.3999
+ ___Block_byref_object_copy_.4581
+ ___Block_byref_object_copy_.6422
+ ___Block_byref_object_copy_.7370
+ ___Block_byref_object_copy_.8387
+ ___Block_byref_object_copy_.8985
+ ___Block_byref_object_dispose_.10147
+ ___Block_byref_object_dispose_.10617
+ ___Block_byref_object_dispose_.11823
+ ___Block_byref_object_dispose_.13118
+ ___Block_byref_object_dispose_.13537
+ ___Block_byref_object_dispose_.1448
+ ___Block_byref_object_dispose_.14597
+ ___Block_byref_object_dispose_.14932
+ ___Block_byref_object_dispose_.15802
+ ___Block_byref_object_dispose_.15918
+ ___Block_byref_object_dispose_.17543
+ ___Block_byref_object_dispose_.1780
+ ___Block_byref_object_dispose_.17834
+ ___Block_byref_object_dispose_.18980
+ ___Block_byref_object_dispose_.20117
+ ___Block_byref_object_dispose_.20766
+ ___Block_byref_object_dispose_.21378
+ ___Block_byref_object_dispose_.21617
+ ___Block_byref_object_dispose_.22249
+ ___Block_byref_object_dispose_.2274
+ ___Block_byref_object_dispose_.22902
+ ___Block_byref_object_dispose_.23172
+ ___Block_byref_object_dispose_.23907
+ ___Block_byref_object_dispose_.24705
+ ___Block_byref_object_dispose_.25134
+ ___Block_byref_object_dispose_.25971
+ ___Block_byref_object_dispose_.26406
+ ___Block_byref_object_dispose_.2669
+ ___Block_byref_object_dispose_.27220
+ ___Block_byref_object_dispose_.3648
+ ___Block_byref_object_dispose_.3782
+ ___Block_byref_object_dispose_.4000
+ ___Block_byref_object_dispose_.4582
+ ___Block_byref_object_dispose_.6423
+ ___Block_byref_object_dispose_.7371
+ ___Block_byref_object_dispose_.8388
+ ___Block_byref_object_dispose_.8986
+ ___MobileTimerLibraryCore_block_invoke.806
+ ___block_descriptor_112_e8_32r40r48r56r64r72r80r88r96r104r_e36_v16?0"CSEnhancedEndpointerResult"8lr32l8r40l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8
+ ___block_descriptor_40_e8_32bs_e23_v28?0B8"NSError"12Q20ls32l8
+ ___block_descriptor_56_e8_32s40s_e24_v32?0"MAAsset"8Q16^B24ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48r56r_e5_v8?0ls32l8s40l8r48l8r56l8
+ ___block_descriptor_81_e8_32s40r48r56r64r72r_e5_v8?0ls32l8r40l8r48l8r56l8r64l8r72l8
+ ___block_literal_global.10.10764
+ ___block_literal_global.10.19510
+ ___block_literal_global.10.21063
+ ___block_literal_global.10.22112
+ ___block_literal_global.10251
+ ___block_literal_global.1026
+ ___block_literal_global.10397
+ ___block_literal_global.10633
+ ___block_literal_global.10790
+ ___block_literal_global.109
+ ___block_literal_global.11.12104
+ ___block_literal_global.11006
+ ___block_literal_global.11217
+ ___block_literal_global.114
+ ___block_literal_global.11676
+ ___block_literal_global.1182
+ ___block_literal_global.11848
+ ___block_literal_global.12.14090
+ ___block_literal_global.12114
+ ___block_literal_global.12214
+ ___block_literal_global.12336
+ ___block_literal_global.12644
+ ___block_literal_global.12750
+ ___block_literal_global.12806
+ ___block_literal_global.1284
+ ___block_literal_global.12861
+ ___block_literal_global.13.21064
+ ___block_literal_global.13.21210
+ ___block_literal_global.13.22113
+ ___block_literal_global.13324
+ ___block_literal_global.13440
+ ___block_literal_global.13666
+ ___block_literal_global.14.21135
+ ___block_literal_global.14083
+ ___block_literal_global.14429
+ ___block_literal_global.14486
+ ___block_literal_global.14675
+ ___block_literal_global.14693
+ ___block_literal_global.14804
+ ___block_literal_global.15327
+ ___block_literal_global.15412
+ ___block_literal_global.155
+ ___block_literal_global.1577
+ ___block_literal_global.15904
+ ___block_literal_global.15946
+ ___block_literal_global.16.10379
+ ___block_literal_global.16.12094
+ ___block_literal_global.16.13325
+ ___block_literal_global.16.14487
+ ___block_literal_global.16.21065
+ ___block_literal_global.16589
+ ___block_literal_global.17.14430
+ ___block_literal_global.17.21136
+ ___block_literal_global.17063
+ ___block_literal_global.17072
+ ___block_literal_global.17118
+ ___block_literal_global.17152
+ ___block_literal_global.17416
+ ___block_literal_global.17492
+ ___block_literal_global.17600
+ ___block_literal_global.18.14774
+ ___block_literal_global.18.21211
+ ___block_literal_global.18066
+ ___block_literal_global.18135
+ ___block_literal_global.18165
+ ___block_literal_global.18718
+ ___block_literal_global.19001
+ ___block_literal_global.19308
+ ___block_literal_global.19389
+ ___block_literal_global.19527
+ ___block_literal_global.19642
+ ___block_literal_global.19687
+ ___block_literal_global.19703
+ ___block_literal_global.19981
+ ___block_literal_global.20.13301
+ ___block_literal_global.20.14431
+ ___block_literal_global.20.21137
+ ___block_literal_global.20.25116
+ ___block_literal_global.20033
+ ___block_literal_global.20138
+ ___block_literal_global.20214
+ ___block_literal_global.20415
+ ___block_literal_global.20749
+ ___block_literal_global.208
+ ___block_literal_global.21.12751
+ ___block_literal_global.21049
+ ___block_literal_global.21062
+ ___block_literal_global.21134
+ ___block_literal_global.21230
+ ___block_literal_global.2124
+ ___block_literal_global.21280
+ ___block_literal_global.21323
+ ___block_literal_global.21446
+ ___block_literal_global.22.17390
+ ___block_literal_global.22.21066
+ ___block_literal_global.22110
+ ___block_literal_global.22611
+ ___block_literal_global.22783
+ ___block_literal_global.2293
+ ___block_literal_global.22933
+ ___block_literal_global.23.21138
+ ___block_literal_global.23482
+ ___block_literal_global.236
+ ___block_literal_global.236.24721
+ ___block_literal_global.23698
+ ___block_literal_global.2372
+ ___block_literal_global.23783
+ ___block_literal_global.24.12752
+ ___block_literal_global.24160
+ ___block_literal_global.2474
+ ___block_literal_global.24834
+ ___block_literal_global.2488
+ ___block_literal_global.25.21067
+ ___block_literal_global.25157
+ ___block_literal_global.25488
+ ___block_literal_global.25778
+ ___block_literal_global.25827
+ ___block_literal_global.26.25105
+ ___block_literal_global.26006
+ ___block_literal_global.26111
+ ___block_literal_global.26341
+ ___block_literal_global.26474
+ ___block_literal_global.27.12753
+ ___block_literal_global.27014
+ ___block_literal_global.27230
+ ___block_literal_global.27504
+ ___block_literal_global.2758
+ ___block_literal_global.2818
+ ___block_literal_global.29.21068
+ ___block_literal_global.29.21139
+ ___block_literal_global.2909
+ ___block_literal_global.30.12754
+ ___block_literal_global.30.13286
+ ___block_literal_global.303
+ ___block_literal_global.3133
+ ___block_literal_global.326
+ ___block_literal_global.3347
+ ___block_literal_global.3512
+ ___block_literal_global.36.12755
+ ___block_literal_global.3697
+ ___block_literal_global.3772
+ ___block_literal_global.38.9135
+ ___block_literal_global.40.20727
+ ___block_literal_global.4037
+ ___block_literal_global.410
+ ___block_literal_global.42.12756
+ ___block_literal_global.46.6456
+ ___block_literal_global.46.9127
+ ___block_literal_global.5.27505
+ ___block_literal_global.5061
+ ___block_literal_global.518
+ ___block_literal_global.54.11207
+ ___block_literal_global.54.2368
+ ___block_literal_global.5685
+ ___block_literal_global.5796
+ ___block_literal_global.58
+ ___block_literal_global.5982
+ ___block_literal_global.6.26001
+ ___block_literal_global.6084
+ ___block_literal_global.6107
+ ___block_literal_global.6489
+ ___block_literal_global.658
+ ___block_literal_global.6626
+ ___block_literal_global.668
+ ___block_literal_global.6909
+ ___block_literal_global.7.22111
+ ___block_literal_global.7.815
+ ___block_literal_global.763
+ ___block_literal_global.8.1164
+ ___block_literal_global.8.26105
+ ___block_literal_global.8.26475
+ ___block_literal_global.8.27506
+ ___block_literal_global.827
+ ___block_literal_global.8562
+ ___block_literal_global.9167
+ ___block_literal_global.9219
+ ___block_literal_global.9336
+ ___block_literal_global.941
+ ___block_literal_global.9739
+ __block_invoke.enableHeartbeat.11002
+ __block_invoke.enableHeartbeat.26728
+ __compensateChannelDataIfNeeded:receivedNumChannels:.heartbeat.14584
+ __handleAudioChunk:.heartbeat_CORESPEECH_VOICETRIGGER_FIRSTPASS_LPCM_RECORD_BUFFER_AVAILABLE.18644
+ __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.10987
+ __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.18635
+ __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.26702
+ _audit_stringMobileTimer.809
+ _kBypassSecondPassVoiceTrigger_block_invoke.heartbeat
+ _kCSDiagnosticReporterEndpointerTypeUndefined
+ _kCSUtilsStatisticsWarmupKey_block_invoke.heartbeat_CORESPEECH_HYBRID_ENDPOINTER_PROCESS_AUDIO_ASYNC_BEGIN
+ _kCSUtilsStatisticsWarmupKey_block_invoke.heartbeat_CORESPEECH_HYBRID_ENDPOINTER_PROCESS_AUDIO_ASYNC_END
+ _kCSUtilsStatisticsWarmupKey_block_invoke_2.heartbeat_CORESPEECH_HYBRID_CLASSIFIER_PROCESS_END
+ _kCSUtilsStatisticsWarmupKey_block_invoke_2.heartbeat_CORESPEECH_PROCESS_SIL_SCORE_ESTIMATE_BEGIN
+ _kVTEIAudioTapProviderType
+ _objc_msgSend$SSRSpeakerProfilesBasePath
+ _objc_msgSend$_alertBehaviorForRecordRoute:playbackRoute:speechEvent:speechRecordingMode:ringerState:startingAlertBeepOverideID:presentationMode:usePrelistening:isOnPhoneCall:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:suppressStartAlert:activationHostTime:isVoiceOverSiriSoundsEnabled:
+ _objc_msgSend$_alertDictionaryForRecordRoute:playbackRoute:speechEvent:ringerState:startingAlertBeepOverideID:presentationMode:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:activationHostTime:isVoiceOverSiriSoundsEnabled:
+ _objc_msgSend$_connectBuiltInDevice:withError:
+ _objc_msgSend$_connectPluginDevice:withError:
+ _objc_msgSend$_considerSmartRoutingForAudioRecordContext:
+ _objc_msgSend$_decodeFeaturesAtEndpoint:eventType:
+ _objc_msgSend$_deliverHardEndpointDetectedAtTime:withMetrics:eventType:
+ _objc_msgSend$_findLatestInstalledAsset:assetType:
+ _objc_msgSend$_isJarvisVoiceTriggerSpeechEvent:
+ _objc_msgSend$_isNeededForOTA:
+ _objc_msgSend$_notInstalledAssetState:assetType:
+ _objc_msgSend$_playStopAlertIfNecessaryForReason:error:
+ _objc_msgSend$_updateAccessibleEndpointerThresholdIfNeeded
+ _objc_msgSend$_updateEndpointerDelayedTrigger:
+ _objc_msgSend$_updateEndpointerThreshold:
+ _objc_msgSend$_updateEnhancedEndpointerDefaultThresholdPartial:defaultThresholdRC:relaxedThresholdPartial:relaxedThresholdRC:
+ _objc_msgSend$assetForAssetType:resourcePath:configVersion:assetProvider:assetVariant:identity:assistantLanguageCode:uafAssetVersion:
+ _objc_msgSend$assetVersionForConfig:
+ _objc_msgSend$attachDevice:withOutError:
+ _objc_msgSend$audioTapProviderWithType:
+ _objc_msgSend$audioTapProviders
+ _objc_msgSend$bundlePath
+ _objc_msgSend$bundleWithPath:
+ _objc_msgSend$createAudioInjectionDeviceWithType:bundlePath:deviceName:deviceID:productID:completion:
+ _objc_msgSend$createAudioInjectionDeviceWithType:bundlePath:deviceName:deviceID:productID:handlingDaemon:completion:
+ _objc_msgSend$decodeArrayOfObjectsOfClass:forKey:
+ _objc_msgSend$decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:
+ _objc_msgSend$decodeDoubleForKey:
+ _objc_msgSend$detectedTwoShotAtTime:
+ _objc_msgSend$emitEndpointDetectedEventWithEndpointerMetrics:eventType:trpId:mhId:
+ _objc_msgSend$encodeDouble:forKey:
+ _objc_msgSend$endpointAnalyzer:
+ _objc_msgSend$endpointer:didDetectHardEndpointAtTime:withMetrics:eventType:
+ _objc_msgSend$endpointerScore
+ _objc_msgSend$endpointerThreshold
+ _objc_msgSend$engineWithDevice:streamHandleId:
+ _objc_msgSend$getHybridEndpointerConfigForAsset:
+ _objc_msgSend$getSerialQueueWithName:targetQueue:
+ _objc_msgSend$initWithEndpointId:xpcClientFactory:endpointAnalyzer:continuousVoiceTrigger:siriVolumeController:mediaPlayingMonitor:alarmMonitor:timerMonitor:audioSessionController:supportPhatic:supportHearstVoiceTrigger:supportTriagleModeSessionActivationRetry:supportSessionActivateDelay:supportsDuckingOnSpeakerEvaluator:
+ _objc_msgSend$initWithTappingType:
+ _objc_msgSend$initWithTargetQueue:audioProviderSelecting:
+ _objc_msgSend$initWithTargetQueue:audioProviderSelecting:audioSourceType:
+ _objc_msgSend$initWithTotalAudioRecorded:endpointBufferHostTime:featuresAtEndpoint:endpointerType:asrFeatureLatencyDistribution:additionalMetrics:trailingSilenceDurationAtEndpoint:requestId:osdFeatures:asrFeatures:isRequestTimeOut:assetConfigVersion:blkHepAudioOrigin:vtExtraAudioAtStartInMs:firstAudioSampleSensorTimestamp:isAnchorTimeBuffered:endpointHostTime:audioDeliveryHostTimeDelta:endpointerThreshold:endpointerScore:
+ _objc_msgSend$injectAudio:toDeviceWithUUID:withNumChannels:withUserIntentOptions:handlingDaemon:started:
+ _objc_msgSend$injectAudio:toDeviceWithUUID:withScaleFactor:withNumChannels:withUserIntentOptions:started:
+ _objc_msgSend$isBundleDevice
+ _objc_msgSend$isHearstDoubleTapTriggered
+ _objc_msgSend$isHearstHijackable
+ _objc_msgSend$isHypotheticalAudioRouteBluetoothAndNotBTSpeakerFromAudioSessinoId:
+ _objc_msgSend$load
+ _objc_msgSend$modelInfoVersionWithAssetPath:taskHint:
+ _objc_msgSend$multimodalEndpointerEnabled
+ _objc_msgSend$otherAppRecordingStateMonitor
+ _objc_msgSend$principalClass
+ _objc_msgSend$selectBuiltInInjectionDeivceWithUUID:completion:
+ _objc_msgSend$selectBuiltInInjectionDeviceWithUUID:handlingDaemon:completion:
+ _objc_msgSend$setAudioProviderSelector:
+ _objc_msgSend$setEndpointerThreshold:
+ _objc_msgSend$setPluginBundleWithPath:withOutError:
+ _objc_msgSend$setStartInjectBlock:
+ _objc_msgSend$setupAudioFormatWithBlockSize:audioFormat:outError:
+ _objc_msgSend$shouldPlaySiriSounds
+ _objc_msgSend$shouldProvideTwoShotFeedbackWithRecordContext
+ _objc_msgSend$shouldSetupSelfTrigger
+ _objc_msgSend$startAudioStreamWithOption:withOutError:
+ _objc_msgSend$startAudioStreamWithOutError:
+ _objc_msgSend$startInjectBlock
+ _objc_msgSend$startSmartSiriVolumeWithAudioProviderSelector:
+ _objc_msgSend$stopAudioStreamWithOutError:
+ _objc_msgSend$supportsHearstSmartRoutingImprovements
+ _objc_msgSend$supportsSystemDaemon
+ _sharedController.onceToken.11847
+ _sharedController.sharedController.11849
+ _sharedHandler.onceToken.1025
+ _sharedHandler.onceToken.19307
+ _sharedHandler.onceToken.26005
+ _sharedHandler.sharedHandler.1027
+ _sharedHandler.sharedHandler.19309
+ _sharedHandler.sharedHandler.26007
+ _sharedHandlerDisabledOnDeviceCompilation.onceToken.26000
+ _sharedHandlerDisabledOnDeviceCompilation.sharedHandler.26002
+ _sharedInstance._sharedInstance.11677
+ _sharedInstance._sharedInstance.12862
+ _sharedInstance._sharedInstance.14805
+ _sharedInstance._sharedInstance.17119
+ _sharedInstance._sharedInstance.17417
+ _sharedInstance._sharedInstance.17493
+ _sharedInstance._sharedInstance.18136
+ _sharedInstance._sharedInstance.19643
+ _sharedInstance._sharedInstance.19982
+ _sharedInstance._sharedInstance.20034
+ _sharedInstance._sharedInstance.20215
+ _sharedInstance._sharedInstance.23483
+ _sharedInstance._sharedInstance.24161
+ _sharedInstance._sharedInstance.25828
+ _sharedInstance._sharedInstance.27231
+ _sharedInstance._sharedInstance.2759
+ _sharedInstance._sharedInstance.2819
+ _sharedInstance._sharedInstance.3134
+ _sharedInstance._sharedInstance.5686
+ _sharedInstance._sharedInstance.5797
+ _sharedInstance._sharedInstance.6085
+ _sharedInstance._sharedInstance.659
+ _sharedInstance._sharedInstance.6627
+ _sharedInstance._sharedInstance.764
+ _sharedInstance._sharedInstance.828
+ _sharedInstance._sharedInstance.9220
+ _sharedInstance.onceToken.10396
+ _sharedInstance.onceToken.10632
+ _sharedInstance.onceToken.10789
+ _sharedInstance.onceToken.11675
+ _sharedInstance.onceToken.1181
+ _sharedInstance.onceToken.12805
+ _sharedInstance.onceToken.1283
+ _sharedInstance.onceToken.12860
+ _sharedInstance.onceToken.13439
+ _sharedInstance.onceToken.14803
+ _sharedInstance.onceToken.15326
+ _sharedInstance.onceToken.15411
+ _sharedInstance.onceToken.15903
+ _sharedInstance.onceToken.17117
+ _sharedInstance.onceToken.17415
+ _sharedInstance.onceToken.17491
+ _sharedInstance.onceToken.17599
+ _sharedInstance.onceToken.18065
+ _sharedInstance.onceToken.18134
+ _sharedInstance.onceToken.18164
+ _sharedInstance.onceToken.19526
+ _sharedInstance.onceToken.19641
+ _sharedInstance.onceToken.19980
+ _sharedInstance.onceToken.20032
+ _sharedInstance.onceToken.20213
+ _sharedInstance.onceToken.21048
+ _sharedInstance.onceToken.21229
+ _sharedInstance.onceToken.21322
+ _sharedInstance.onceToken.21445
+ _sharedInstance.onceToken.22610
+ _sharedInstance.onceToken.22782
+ _sharedInstance.onceToken.22932
+ _sharedInstance.onceToken.23481
+ _sharedInstance.onceToken.23782
+ _sharedInstance.onceToken.24159
+ _sharedInstance.onceToken.25487
+ _sharedInstance.onceToken.25826
+ _sharedInstance.onceToken.27013
+ _sharedInstance.onceToken.27229
+ _sharedInstance.onceToken.2757
+ _sharedInstance.onceToken.2817
+ _sharedInstance.onceToken.2908
+ _sharedInstance.onceToken.3132
+ _sharedInstance.onceToken.3511
+ _sharedInstance.onceToken.5060
+ _sharedInstance.onceToken.517
+ _sharedInstance.onceToken.5684
+ _sharedInstance.onceToken.5795
+ _sharedInstance.onceToken.6083
+ _sharedInstance.onceToken.657
+ _sharedInstance.onceToken.6625
+ _sharedInstance.onceToken.762
+ _sharedInstance.onceToken.826
+ _sharedInstance.onceToken.9218
+ _sharedInstance.sSharedInstance.18166
+ _sharedInstance.sharedInstance.12807
+ _sharedInstance.sharedInstance.13441
+ _sharedInstance.sharedInstance.15413
+ _sharedInstance.sharedInstance.18067
+ _sharedInstance.sharedInstance.19528
+ _sharedInstance.sharedInstance.21050
+ _sharedInstance.sharedInstance.21324
+ _sharedInstance.sharedInstance.22784
+ _sharedInstance.sharedInstance.22934
+ _sharedInstance.sharedInstance.27015
+ _sharedInstance.sharedInstance.3513
+ _sharedInstance.sharedInstance.5062
+ _sharedInstance.sharedManager.25489
+ _sharedInstance.sharedPolicy.1183
+ _sharedInstance.sharedPolicy.21231
+ _sharedInstance.sharedPolicy.23784
+ _sharedInstance.sharedProvider.22612
+ _sharedManager.onceToken.17062
+ _sharedManager.onceToken.19000
+ _sharedManager.onceToken.6488
+ _sharedManager.onceToken.6908
+ _sharedManager.sharedManager.17064
+ _sharedManager.sharedManager.6490
+ _sharedManager.sharedManager.6910
+ _sharedMonitor.onceToken.20137
+ _sharedMonitor.sharedMonitor.20139
+ _sharedService.onceToken.15945
+ _sharedService.onceToken.25156
+ _sharedService.sharedService.25158
- +[CSAudioInjectionEngineFactory engineWithDeviceType:streamHandleId:]
- +[CSEndpointDetectedSelfLogger _decodeFeaturesAtEndpoint:endpointerModelType:]
- +[CSEndpointDetectedSelfLogger emitEndpointDetectedEventWithEndpointerMetrics:withEndpointerModelType:withTrpId:withMhID:]
- +[CSEndpointerAssetManager _getOEPVersionFromPath:]
- +[CSEndpointerFactory endpointerProxy]
- +[CSNNVADEndpointAnalyzer timeStampString]
- +[CSOtherAppRecordingStateMonitorASMac sharedInstance]
- +[CSSiriAudioActivationInfo _alertBehaviorForRecordRoute:playbackRoute:speechEvent:speechRecordingMode:ringerState:startingAlertBeepOverideID:presentationMode:usePrelistening:isOnPhoneCall:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:suppressStartAlert:activationHostTime:]
- +[CSSiriAudioActivationInfo _alertDictionaryForRecordRoute:playbackRoute:speechEvent:ringerState:startingAlertBeepOverideID:presentationMode:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:activationHostTime:]
- +[CSSpeechManager sharedManagerForCoreSpeechDaemon]
- -[CSAssetController _findLatestInstalledAsset:]
- -[CSAudioInjectionBuiltInEngine .cxx_destruct]
- -[CSAudioInjectionBuiltInEngine alwaysOnVoiceTriggerEnabled]
- -[CSAudioInjectionBuiltInEngine attachDevice:]
- -[CSAudioInjectionBuiltInEngine audioEngineAudioChunkForTvAvailable:audioChunk:]
- -[CSAudioInjectionBuiltInEngine audioEngineBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:isFileLoadedBuffer:]
- -[CSAudioInjectionBuiltInEngine audioEngineDidStartRecord:audioStreamHandleId:successfully:error:]
- -[CSAudioInjectionBuiltInEngine audioEngineDidStopRecord:audioStreamHandleId:reason:]
- -[CSAudioInjectionBuiltInEngine circularBuffer]
- -[CSAudioInjectionBuiltInEngine connectedDevice]
- -[CSAudioInjectionBuiltInEngine dealloc]
- -[CSAudioInjectionBuiltInEngine delegate]
- -[CSAudioInjectionBuiltInEngine getBestSampleCountWithOption:]
- -[CSAudioInjectionBuiltInEngine hostTimeBuffer]
- -[CSAudioInjectionBuiltInEngine initWithStreamHandleId:]
- -[CSAudioInjectionBuiltInEngine injectAudio:]
- -[CSAudioInjectionBuiltInEngine injectAudio:withScaleFactor:playbackStarted:completion:]
- -[CSAudioInjectionBuiltInEngine isAlwaysOnVoiceTriggerAvailable]
- -[CSAudioInjectionBuiltInEngine isForwarding]
- -[CSAudioInjectionBuiltInEngine isRecording]
- -[CSAudioInjectionBuiltInEngine keywordAnalyzer]
- -[CSAudioInjectionBuiltInEngine lastForwardedSampleCount]
- -[CSAudioInjectionBuiltInEngine queue]
- -[CSAudioInjectionBuiltInEngine setAlwaysOnVoiceTriggerEnabled:]
- -[CSAudioInjectionBuiltInEngine setCircularBuffer:]
- -[CSAudioInjectionBuiltInEngine setConnectedDevice:]
- -[CSAudioInjectionBuiltInEngine setDelegate:]
- -[CSAudioInjectionBuiltInEngine setHostTimeBuffer:]
- -[CSAudioInjectionBuiltInEngine setIsForwarding:]
- -[CSAudioInjectionBuiltInEngine setKeywordAnalyzer:]
- -[CSAudioInjectionBuiltInEngine setLastForwardedSampleCount:]
- -[CSAudioInjectionBuiltInEngine setQueue:]
- -[CSAudioInjectionBuiltInEngine setUserIntentOptions:]
- -[CSAudioInjectionBuiltInEngine setUuid:]
- -[CSAudioInjectionBuiltInEngine setVoiceTriggerEnabled:]
- -[CSAudioInjectionBuiltInEngine setVoiceTriggerSampleCount:]
- -[CSAudioInjectionBuiltInEngine startAudioStreamWithOption:]
- -[CSAudioInjectionBuiltInEngine start]
- -[CSAudioInjectionBuiltInEngine stopAudioStream]
- -[CSAudioInjectionBuiltInEngine stop]
- -[CSAudioInjectionBuiltInEngine userIntentOptions]
- -[CSAudioInjectionBuiltInEngine uuid]
- -[CSAudioInjectionBuiltInEngine voiceTriggerEnabled]
- -[CSAudioInjectionBuiltInEngine voiceTriggerSampleCount]
- -[CSAudioInjectionEngine .cxx_destruct]
- -[CSAudioInjectionEngine _compensateChannelDataIfNeeded:receivedNumChannels:]
- -[CSAudioInjectionEngine _createDeInterleaverIfNeeded]
- -[CSAudioInjectionEngine _defaultOutASBD]
- -[CSAudioInjectionEngine _deinterleaveBufferIfNeeded:]
- -[CSAudioInjectionEngine _readAudioBufferAndFeed]
- -[CSAudioInjectionEngine _startAudioFeedingTimer]
- -[CSAudioInjectionEngine alwaysOnVoiceTriggerEnabled]
- -[CSAudioInjectionEngine attachDevice:]
- -[CSAudioInjectionEngine audioFeedTimer]
- -[CSAudioInjectionEngine audioStreamHandleId]
- -[CSAudioInjectionEngine bufferDuration]
- -[CSAudioInjectionEngine dealloc]
- -[CSAudioInjectionEngine deinterleaver]
- -[CSAudioInjectionEngine delegate]
- -[CSAudioInjectionEngine didSetScaleFactor]
- -[CSAudioInjectionEngine fileOption]
- -[CSAudioInjectionEngine initWithStreamHandleId:]
- -[CSAudioInjectionEngine initWithStreamHandleId:withInputRecordingNumberOfChannels:]
- -[CSAudioInjectionEngine injectAudio:]
- -[CSAudioInjectionEngine injectAudio:withScaleFactor:outASBD:playbackStarted:completion:]
- -[CSAudioInjectionEngine injectAudio:withScaleFactor:playbackStarted:completion:]
- -[CSAudioInjectionEngine injectionAudioFileList]
- -[CSAudioInjectionEngine injectionCompletionNotifyBlocks]
- -[CSAudioInjectionEngine injectionStartNotifyBlocks]
- -[CSAudioInjectionEngine inputRecordingNumberOfChannels]
- -[CSAudioInjectionEngine isAlwaysOnVoiceTriggerAvailable]
- -[CSAudioInjectionEngine isRecording]
- -[CSAudioInjectionEngine outASBD]
- -[CSAudioInjectionEngine pNonInterleavedABL]
- -[CSAudioInjectionEngine queue]
- -[CSAudioInjectionEngine scaleFactor]
- -[CSAudioInjectionEngine setAlwaysOnVoiceTriggerEnabled:]
- -[CSAudioInjectionEngine setAudioFeedTimer:]
- -[CSAudioInjectionEngine setAudioStreamHandleId:]
- -[CSAudioInjectionEngine setBufferDuration:]
- -[CSAudioInjectionEngine setDeinterleaver:]
- -[CSAudioInjectionEngine setDelegate:]
- -[CSAudioInjectionEngine setDidSetScaleFactor:]
- -[CSAudioInjectionEngine setFileOption:]
- -[CSAudioInjectionEngine setInjectionAudioFileList:]
- -[CSAudioInjectionEngine setInjectionCompletionNotifyBlocks:]
- -[CSAudioInjectionEngine setInjectionStartNotifyBlocks:]
- -[CSAudioInjectionEngine setInputRecordingNumberOfChannels:]
- -[CSAudioInjectionEngine setIsRecording:]
- -[CSAudioInjectionEngine setOutASBD:]
- -[CSAudioInjectionEngine setPNonInterleavedABL:]
- -[CSAudioInjectionEngine setQueue:]
- -[CSAudioInjectionEngine setScaleFactor:]
- -[CSAudioInjectionEngine setUserIntentOptions:]
- -[CSAudioInjectionEngine setUuid:]
- -[CSAudioInjectionEngine startAudioStreamWithOption:]
- -[CSAudioInjectionEngine start]
- -[CSAudioInjectionEngine stopAudioStream]
- -[CSAudioInjectionEngine stop]
- -[CSAudioInjectionEngine uuid]
- -[CSAudioInjectionHearstEngine .cxx_destruct]
- -[CSAudioInjectionHearstEngine alwaysOnVoiceTriggerEnabled]
- -[CSAudioInjectionHearstEngine attachDevice:]
- -[CSAudioInjectionHearstEngine audioEngineAudioChunkForTvAvailable:audioChunk:]
- -[CSAudioInjectionHearstEngine audioEngineBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:isFileLoadedBuffer:]
- -[CSAudioInjectionHearstEngine audioEngineDidStartRecord:audioStreamHandleId:successfully:error:]
- -[CSAudioInjectionHearstEngine audioEngineDidStopRecord:audioStreamHandleId:reason:]
- -[CSAudioInjectionHearstEngine circularBuffer]
- -[CSAudioInjectionHearstEngine connectedDevice]
- -[CSAudioInjectionHearstEngine dealloc]
- -[CSAudioInjectionHearstEngine delegate]
- -[CSAudioInjectionHearstEngine initWithStreamHandleId:]
- -[CSAudioInjectionHearstEngine injectAudio:]
- -[CSAudioInjectionHearstEngine injectAudio:withScaleFactor:playbackStarted:completion:]
- -[CSAudioInjectionHearstEngine isAlwaysOnVoiceTriggerAvailable]
- -[CSAudioInjectionHearstEngine isForwarding]
- -[CSAudioInjectionHearstEngine isRecording]
- -[CSAudioInjectionHearstEngine keywordAnalyzer]
- -[CSAudioInjectionHearstEngine lastDetectedVoiceTriggerBeginSampleCount]
- -[CSAudioInjectionHearstEngine lastForwardedSampleCount]
- -[CSAudioInjectionHearstEngine queue]
- -[CSAudioInjectionHearstEngine setAlwaysOnVoiceTriggerEnabled:]
- -[CSAudioInjectionHearstEngine setCircularBuffer:]
- -[CSAudioInjectionHearstEngine setConnectedDevice:]
- -[CSAudioInjectionHearstEngine setDelegate:]
- -[CSAudioInjectionHearstEngine setIsForwarding:]
- -[CSAudioInjectionHearstEngine setKeywordAnalyzer:]
- -[CSAudioInjectionHearstEngine setLastDetectedVoiceTriggerBeginSampleCount:]
- -[CSAudioInjectionHearstEngine setLastForwardedSampleCount:]
- -[CSAudioInjectionHearstEngine setQueue:]
- -[CSAudioInjectionHearstEngine setUuid:]
- -[CSAudioInjectionHearstEngine setVoiceTriggerEnabled:]
- -[CSAudioInjectionHearstEngine startAudioStreamWithOption:]
- -[CSAudioInjectionHearstEngine start]
- -[CSAudioInjectionHearstEngine stopAudioStream]
- -[CSAudioInjectionHearstEngine stop]
- -[CSAudioInjectionHearstEngine uuid]
- -[CSAudioInjectionHearstEngine voiceTriggerEnabled]
- -[CSAudioInjectionProvider _connectPluginDevice:]
- -[CSAudioInjectionProvider builtInAudioInjectionEngine]
- -[CSAudioInjectionProvider builtInDevice]
- -[CSAudioInjectionProvider bundleTvRemote]
- -[CSAudioInjectionProvider connectDevice:]
- -[CSAudioInjectionProvider setBuiltInAudioInjectionEngine:]
- -[CSAudioInjectionProvider setBuiltInDevice:]
- -[CSAudioInjectionProvider setBundleTvRemote:]
- -[CSAudioInjectionRemoraEngine .cxx_destruct]
- -[CSAudioInjectionRemoraEngine alwaysOnVoiceTriggerEnabled]
- -[CSAudioInjectionRemoraEngine attachDevice:]
- -[CSAudioInjectionRemoraEngine audioEngineAudioChunkForTvAvailable:audioChunk:]
- -[CSAudioInjectionRemoraEngine audioEngineBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:isFileLoadedBuffer:]
- -[CSAudioInjectionRemoraEngine audioEngineDidStartRecord:audioStreamHandleId:successfully:error:]
- -[CSAudioInjectionRemoraEngine audioEngineDidStopRecord:audioStreamHandleId:reason:]
- -[CSAudioInjectionRemoraEngine circularBuffer]
- -[CSAudioInjectionRemoraEngine connectedDevice]
- -[CSAudioInjectionRemoraEngine dealloc]
- -[CSAudioInjectionRemoraEngine delegate]
- -[CSAudioInjectionRemoraEngine initWithStreamHandleId:]
- -[CSAudioInjectionRemoraEngine injectAudio:]
- -[CSAudioInjectionRemoraEngine injectAudio:withScaleFactor:playbackStarted:completion:]
- -[CSAudioInjectionRemoraEngine isAlwaysOnVoiceTriggerAvailable]
- -[CSAudioInjectionRemoraEngine isForwarding]
- -[CSAudioInjectionRemoraEngine isRecording]
- -[CSAudioInjectionRemoraEngine keywordAnalyzer]
- -[CSAudioInjectionRemoraEngine lastDetectedVoiceTriggerBeginSampleCount]
- -[CSAudioInjectionRemoraEngine lastForwardedSampleCount]
- -[CSAudioInjectionRemoraEngine queue]
- -[CSAudioInjectionRemoraEngine setAlwaysOnVoiceTriggerEnabled:]
- -[CSAudioInjectionRemoraEngine setCircularBuffer:]
- -[CSAudioInjectionRemoraEngine setConnectedDevice:]
- -[CSAudioInjectionRemoraEngine setDelegate:]
- -[CSAudioInjectionRemoraEngine setIsForwarding:]
- -[CSAudioInjectionRemoraEngine setKeywordAnalyzer:]
- -[CSAudioInjectionRemoraEngine setLastDetectedVoiceTriggerBeginSampleCount:]
- -[CSAudioInjectionRemoraEngine setLastForwardedSampleCount:]
- -[CSAudioInjectionRemoraEngine setQueue:]
- -[CSAudioInjectionRemoraEngine setUuid:]
- -[CSAudioInjectionRemoraEngine setVoiceTriggerEnabled:]
- -[CSAudioInjectionRemoraEngine startAudioStreamWithOption:]
- -[CSAudioInjectionRemoraEngine start]
- -[CSAudioInjectionRemoraEngine stopAudioStream]
- -[CSAudioInjectionRemoraEngine stop]
- -[CSAudioInjectionRemoraEngine uuid]
- -[CSAudioInjectionRemoraEngine voiceTriggerEnabled]
- -[CSAudioInjectionTvRemoteEngine .cxx_destruct]
- -[CSAudioInjectionTvRemoteEngine alwaysOnVoiceTriggerEnabled]
- -[CSAudioInjectionTvRemoteEngine attachDevice:]
- -[CSAudioInjectionTvRemoteEngine audioConverterDidConvertPackets:packets:durationInSec:timestamp:arrivalTimestampToAudioRecorder:]
- -[CSAudioInjectionTvRemoteEngine audioEngineAudioChunkForTvAvailable:audioChunk:]
- -[CSAudioInjectionTvRemoteEngine audioEngineBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:isFileLoadedBuffer:]
- -[CSAudioInjectionTvRemoteEngine audioEngineDidStartRecord:audioStreamHandleId:successfully:error:]
- -[CSAudioInjectionTvRemoteEngine audioEngineDidStopRecord:audioStreamHandleId:reason:]
- -[CSAudioInjectionTvRemoteEngine connectedDevice]
- -[CSAudioInjectionTvRemoteEngine delegate]
- -[CSAudioInjectionTvRemoteEngine encoder]
- -[CSAudioInjectionTvRemoteEngine initWithStreamHandleId:]
- -[CSAudioInjectionTvRemoteEngine injectAudio:]
- -[CSAudioInjectionTvRemoteEngine injectAudio:withScaleFactor:playbackStarted:completion:]
- -[CSAudioInjectionTvRemoteEngine isAlwaysOnVoiceTriggerAvailable]
- -[CSAudioInjectionTvRemoteEngine isRecording]
- -[CSAudioInjectionTvRemoteEngine queue]
- -[CSAudioInjectionTvRemoteEngine setAlwaysOnVoiceTriggerEnabled:]
- -[CSAudioInjectionTvRemoteEngine setConnectedDevice:]
- -[CSAudioInjectionTvRemoteEngine setDelegate:]
- -[CSAudioInjectionTvRemoteEngine setEncoder:]
- -[CSAudioInjectionTvRemoteEngine setQueue:]
- -[CSAudioInjectionTvRemoteEngine setUuid:]
- -[CSAudioInjectionTvRemoteEngine startAudioStreamWithOption:]
- -[CSAudioInjectionTvRemoteEngine start]
- -[CSAudioInjectionTvRemoteEngine stopAudioStream]
- -[CSAudioInjectionTvRemoteEngine stop]
- -[CSAudioInjectionTvRemoteEngine uuid]
- -[CSAudioTapProvider .cxx_destruct]
- -[CSAudioTapProvider CSAudioServerCrashMonitorDidReceiveServerCrash:]
- -[CSAudioTapProvider CSAudioServerCrashMonitorDidReceiveServerRestart:]
- -[CSAudioTapProvider UUIDString]
- -[CSAudioTapProvider UUID]
- -[CSAudioTapProvider _calculateBufferSize:audioStreamBasicDescription:frameSizeInSec:]
- -[CSAudioTapProvider _destroyRecordingAudioQueue]
- -[CSAudioTapProvider _holdTransactionForStartListening]
- -[CSAudioTapProvider _releaseTransactionForStopListeningIfNeeded]
- -[CSAudioTapProvider _reset]
- -[CSAudioTapProvider _saveRecordingBufferFrom:to:toURL:]
- -[CSAudioTapProvider _setupRecordingAudioQueueIfNeededWithOption:]
- -[CSAudioTapProvider _stopRecordingAudioQueueIfNeededWithCompletion:]
- -[CSAudioTapProvider aqStartCompletion]
- -[CSAudioTapProvider aqStopCompletion]
- -[CSAudioTapProvider attachTandemStream:toPrimaryStream:completion:]
- -[CSAudioTapProvider audioChunkFrom:to:]
- -[CSAudioTapProvider audioChunkFrom:to:channelIdx:]
- -[CSAudioTapProvider audioChunkToEndFrom:]
- -[CSAudioTapProvider audioChunkToEndFrom:channelIdx:]
- -[CSAudioTapProvider audioDeviceInfo]
- -[CSAudioTapProvider audioStreamId]
- -[CSAudioTapProvider audioStreamWithRequest:streamName:completion:]
- -[CSAudioTapProvider audioStreamWithRequest:streamName:error:]
- -[CSAudioTapProvider audioStream]
- -[CSAudioTapProvider cancelAudioStreamHold:]
- -[CSAudioTapProvider circularBuffer]
- -[CSAudioTapProvider dealloc]
- -[CSAudioTapProvider destroyRecordingAudioQueue]
- -[CSAudioTapProvider holdAudioStreamWithDescription:option:]
- -[CSAudioTapProvider init]
- -[CSAudioTapProvider isNarrowBand]
- -[CSAudioTapProvider isRecording]
- -[CSAudioTapProvider loggingQueue]
- -[CSAudioTapProvider playbackRoute]
- -[CSAudioTapProvider prepareAudioStream:request:completion:]
- -[CSAudioTapProvider prepareAudioStreamSync:request:error:]
- -[CSAudioTapProvider processedSampleCount]
- -[CSAudioTapProvider queue]
- -[CSAudioTapProvider recordDeviceInfo]
- -[CSAudioTapProvider recordRoute]
- -[CSAudioTapProvider recordSettings]
- -[CSAudioTapProvider recordingAudioQueue]
- -[CSAudioTapProvider saveRecordingBufferFrom:to:toURL:]
- -[CSAudioTapProvider saveRecordingBufferToEndFrom:toURL:]
- -[CSAudioTapProvider setAnnounceCallsEnabled:withStreamHandleID:]
- -[CSAudioTapProvider setAqStartCompletion:]
- -[CSAudioTapProvider setAqStopCompletion:]
- -[CSAudioTapProvider setAudioStream:]
- -[CSAudioTapProvider setCircularBuffer:]
- -[CSAudioTapProvider setCurrentContext:error:]
- -[CSAudioTapProvider setLoggingQueue:]
- -[CSAudioTapProvider setProcessedSampleCount:]
- -[CSAudioTapProvider setQueue:]
- -[CSAudioTapProvider setRecordingAudioQueue:]
- -[CSAudioTapProvider setTransaction:]
- -[CSAudioTapProvider setUUIDString:]
- -[CSAudioTapProvider setup]
- -[CSAudioTapProvider startAudioStream:option:completion:]
- -[CSAudioTapProvider stopAudioStream:option:completion:]
- -[CSAudioTapProvider supportsDuckingOnCurrentRouteWithError:]
- -[CSAudioTapProvider transaction]
- -[CSEndpointDetectedSelfLogger attSiriNode:didDetectEndpointEventAtTime:eventType:withMetrics:useEndpointerSignal:]
- -[CSEndpointDetectedSelfLogger attSiriNode:didDetectHardEndpointAtTime:withMetrics:usesAutomaticEndPointing:]
- -[CSEndpointDetectedSelfLogger attSiriNode:didDetectStartpointAtTime:]
- -[CSEndpointerMetrics initWithTotalAudioRecorded:endpointBufferHostTime:featuresAtEndpoint:endpointerType:asrFeatureLatencyDistribution:additionalMetrics:trailingSilenceDurationAtEndpoint:requestId:]
- -[CSEndpointerMetrics initWithTotalAudioRecorded:endpointBufferHostTime:featuresAtEndpoint:endpointerType:asrFeatureLatencyDistribution:additionalMetrics:trailingSilenceDurationAtEndpoint:requestId:osdFeatures:asrFeatures:isRequestTimeOut:assetConfigVersion:blkHepAudioOrigin:vtExtraAudioAtStartInMs:firstAudioSampleSensorTimestamp:isAnchorTimeBuffered:endpointHostTime:audioDeliveryHostTimeDelta:]
- -[CSEndpointerProxy .cxx_destruct]
- -[CSEndpointerProxy _setupNNVADEndpointer]
- -[CSEndpointerProxy _updateAccessibleEndpointerThresholdIfNeed]
- -[CSEndpointerProxy accessibleEndpointerEnabled]
- -[CSEndpointerProxy activeEndpointer]
- -[CSEndpointerProxy automaticEndpointingSuspensionEndTime]
- -[CSEndpointerProxy cachedEndpointerMetrics]
- -[CSEndpointerProxy delay]
- -[CSEndpointerProxy endPointAnalyzerType]
- -[CSEndpointerProxy endWaitTime]
- -[CSEndpointerProxy endpointStyle]
- -[CSEndpointerProxy endpointer:detectedTwoShotAtTime:]
- -[CSEndpointerProxy endpointer:didDetectHardEndpointAtTime:withMetrics:]
- -[CSEndpointerProxy endpointer:didDetectHardEndpointAtTime:withMetrics:endpointerModelType:]
- -[CSEndpointerProxy endpointer:didDetectStartpointAtTime:]
- -[CSEndpointerProxy endpointer:reportEndpointBufferHostTime:firstBufferHostTime:]
- -[CSEndpointerProxy endpointerDelegate]
- -[CSEndpointerProxy endpointerImplDelegate]
- -[CSEndpointerProxy endpointerModelVersion]
- -[CSEndpointerProxy fetchCurrentEndpointerOperationMode]
- -[CSEndpointerProxy hybridEndpointer]
- -[CSEndpointerProxy initForSidekick]
- -[CSEndpointerProxy init]
- -[CSEndpointerProxy interspeechWaitTime]
- -[CSEndpointerProxy isWatchRTSTriggered]
- -[CSEndpointerProxy lastEndOfVoiceActivityTime]
- -[CSEndpointerProxy lastStartOfVoiceActivityTime]
- -[CSEndpointerProxy logAnchorMachAbsTime:numSamplesProcessedBeforeAnchorTime:isAnchorTimeBuffered:audioDeliveryHostTimeDelta:]
- -[CSEndpointerProxy logHybridEndpointFeaturesWithEvent:locale:]
- -[CSEndpointerProxy minimumDurationForEndpointer]
- -[CSEndpointerProxy nnvadEndpointer]
- -[CSEndpointerProxy postVoiceTriggerSilence]
- -[CSEndpointerProxy preheat]
- -[CSEndpointerProxy processASRFeatures:fromServer:]
- -[CSEndpointerProxy processAudioSamplesAsynchronously:]
- -[CSEndpointerProxy processFirstAudioPacketTimestamp:firstAudioSampleSensorTimestamp:]
- -[CSEndpointerProxy processOSDFeatures:withFrameDurationMs:withMHID:]
- -[CSEndpointerProxy processRCFeatures:]
- -[CSEndpointerProxy processTaskString:]
- -[CSEndpointerProxy recordContext]
- -[CSEndpointerProxy recordingDidStop]
- -[CSEndpointerProxy recordingStoppedForReason:]
- -[CSEndpointerProxy resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]
- -[CSEndpointerProxy resetForVoiceTriggerTwoShotWithSampleRate:]
- -[CSEndpointerProxy reset]
- -[CSEndpointerProxy saveSamplesSeenInReset]
- -[CSEndpointerProxy setAccessibleEndpointerEnabled:]
- -[CSEndpointerProxy setActiveChannel:]
- -[CSEndpointerProxy setActiveEndpointer:]
- -[CSEndpointerProxy setAutomaticEndpointingSuspensionEndTime:]
- -[CSEndpointerProxy setDelay:]
- -[CSEndpointerProxy setEndWaitTime:]
- -[CSEndpointerProxy setEndpointStyle:]
- -[CSEndpointerProxy setEndpointerDelegate:]
- -[CSEndpointerProxy setEndpointerImplDelegate:]
- -[CSEndpointerProxy setEndpointerOperationMode:]
- -[CSEndpointerProxy setHybridEndpointer:]
- -[CSEndpointerProxy setInterspeechWaitTime:]
- -[CSEndpointerProxy setMinimumDurationForEndpointer:]
- -[CSEndpointerProxy setNnvadEndpointer:]
- -[CSEndpointerProxy setRecordContext:]
- -[CSEndpointerProxy setRecordingDidStop:]
- -[CSEndpointerProxy setRequestMHUUID:]
- -[CSEndpointerProxy setSaveSamplesSeenInReset:]
- -[CSEndpointerProxy setStartWaitTime:]
- -[CSEndpointerProxy shouldAcceptEagerResultForDuration:resultsCompletionHandler:]
- -[CSEndpointerProxy shouldAcceptEagerResultForDuration:withEndpointerMetrics:resultsCompletionHandler:]
- -[CSEndpointerProxy shouldAcceptEagerResultForDurationSync:withEndpointerMetrics:]
- -[CSEndpointerProxy startWaitTime]
- -[CSEndpointerProxy stopEndpointer]
- -[CSEndpointerProxy updateEndpointerDelayedTrigger:]
- -[CSEndpointerProxy updateEndpointerThreshold:]
- -[CSEndpointerXPCClient _deliverHardEndpointDetectedAtTime:withMetrics:]
- -[CSEndpointerXPCClient activeEndpointer]
- -[CSEndpointerXPCClient didDetectHardEndpointAtTime:withMetrics:]
- -[CSEndpointerXPCClient didDetectStartpointAtTime:]
- -[CSEndpointerXPCClient endPointAnalyzerType]
- -[CSEndpointerXPCClient endpointerDelegate]
- -[CSEndpointerXPCClient endpointerImplDelegate]
- -[CSEndpointerXPCClient postVoiceTriggerSilence]
- -[CSEndpointerXPCClient resetForVoiceTriggerTwoShotWithSampleRate:]
- -[CSEndpointerXPCClient setActiveEndpointer:]
- -[CSEndpointerXPCClient setAutomaticEndpointingSuspensionEndTime:]
- -[CSEndpointerXPCClient setEndWaitTime:]
- -[CSEndpointerXPCClient setEndpointerDelegate:]
- -[CSEndpointerXPCClient setEndpointerImplDelegate:]
- -[CSEndpointerXPCClient setStartWaitTime:]
- -[CSEndpointerXPCClient updateEndpointerDelayedTrigger:]
- -[CSEndpointerXPCClient updateEndpointerThreshold:]
- -[CSHybridEndpointAnalyzer CSAssetManagerDidDownloadNewAsset:]
- -[CSHybridEndpointAnalyzer CSLanguageCodeUpdateMonitor:didReceiveLanguageCodeChanged:]
- -[CSHybridEndpointAnalyzer _emitEndpointDetectedEventWithEndpointTimeMs:endpointBufferHostTime:endpointerFeatures:endpointerDecisionLagInNs:extraDelayMs:endpointScore:asrFeaturesLatencies:]
- -[CSHybridEndpointAnalyzer _getCSHybridEndpointerConfigForAsset:]
- -[CSHybridEndpointAnalyzer _getSerialQueueWithName:targetQueue:]
- -[CSHybridEndpointAnalyzer _loadAndSetupEndpointerAssetIfNecessary]
- -[CSHybridEndpointAnalyzer _multimodalEndpointerEnabled]
- -[CSHybridEndpointAnalyzer _shouldProvideTwoShotFeedbackWithRecordContext]
- -[CSHybridEndpointAnalyzer _updateAssetWithCurrentLanguage]
- -[CSHybridEndpointAnalyzer _updateAssetWithLanguage:]
- -[CSHybridEndpointAnalyzer anchorMachAbsTime]
- -[CSHybridEndpointAnalyzer apQueue]
- -[CSHybridEndpointAnalyzer asrFeatureLatencies]
- -[CSHybridEndpointAnalyzer asrFeaturesQueue]
- -[CSHybridEndpointAnalyzer asrFeaturesWarmupLatency]
- -[CSHybridEndpointAnalyzer automaticEndpointingSuspensionEndTime]
- -[CSHybridEndpointAnalyzer canProcessCurrentRequest]
- -[CSHybridEndpointAnalyzer clampedASRFeatureLatencyMsForClientLag]
- -[CSHybridEndpointAnalyzer clientLagThresholdMs]
- -[CSHybridEndpointAnalyzer currentAsset]
- -[CSHybridEndpointAnalyzer currentRequestSampleRate]
- -[CSHybridEndpointAnalyzer delay]
- -[CSHybridEndpointAnalyzer didAddAudio]
- -[CSHybridEndpointAnalyzer didCommunicateEndpoint]
- -[CSHybridEndpointAnalyzer didDetectSpeech]
- -[CSHybridEndpointAnalyzer didNotifyTwoShot]
- -[CSHybridEndpointAnalyzer didReceiveASRFeatures]
- -[CSHybridEndpointAnalyzer didTimestampFirstAudioPacket]
- -[CSHybridEndpointAnalyzer endWaitTime]
- -[CSHybridEndpointAnalyzer endpointStyle]
- -[CSHybridEndpointAnalyzer epResult]
- -[CSHybridEndpointAnalyzer firstAudioPacketTimestamp]
- -[CSHybridEndpointAnalyzer firstAudioSampleSensorTimestamp]
- -[CSHybridEndpointAnalyzer handleVoiceTriggerWithActivationInfo:]
- -[CSHybridEndpointAnalyzer hepAudioOriginInMs]
- -[CSHybridEndpointAnalyzer hybridClassifierQueue]
- -[CSHybridEndpointAnalyzer hybridClassifier]
- -[CSHybridEndpointAnalyzer implDelegate]
- -[CSHybridEndpointAnalyzer interspeechWaitTime]
- -[CSHybridEndpointAnalyzer isAnchorTimeBuffered]
- -[CSHybridEndpointAnalyzer isRequestTimeout]
- -[CSHybridEndpointAnalyzer lastASRFeatureTimestamp]
- -[CSHybridEndpointAnalyzer lastEndOfVoiceActivityTime]
- -[CSHybridEndpointAnalyzer lastEndpointPosterior]
- -[CSHybridEndpointAnalyzer lastKnownASRFeatureLatency]
- -[CSHybridEndpointAnalyzer lastKnownASRFeatures]
- -[CSHybridEndpointAnalyzer lastKnownOSDFeatures]
- -[CSHybridEndpointAnalyzer lastReportedEndpointTimeMs]
- -[CSHybridEndpointAnalyzer lastStartOfVoiceActivityTime]
- -[CSHybridEndpointAnalyzer logFeaturesWithEvent:locale:]
- -[CSHybridEndpointAnalyzer minimumDurationForEndpointer]
- -[CSHybridEndpointAnalyzer numSamplesProcessedBeforeAnchorTime]
- -[CSHybridEndpointAnalyzer numSamplesProcessed]
- -[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]
- -[CSHybridEndpointAnalyzer osdAnalyzer]
- -[CSHybridEndpointAnalyzer osdFeaturesAtEndpoint]
- -[CSHybridEndpointAnalyzer osdQueue]
- -[CSHybridEndpointAnalyzer postVoiceTriggerSilence]
- -[CSHybridEndpointAnalyzer preheat]
- -[CSHybridEndpointAnalyzer processedAudioInSeconds]
- -[CSHybridEndpointAnalyzer recordContext]
- -[CSHybridEndpointAnalyzer recordingDidStop]
- -[CSHybridEndpointAnalyzer recordingStoppedForReason:]
- -[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]
- -[CSHybridEndpointAnalyzer reset]
- -[CSHybridEndpointAnalyzer saveSamplesSeenInReset]
- -[CSHybridEndpointAnalyzer setAnchorMachAbsTime:]
- -[CSHybridEndpointAnalyzer setApQueue:]
- -[CSHybridEndpointAnalyzer setAsrFeatureLatencies:]
- -[CSHybridEndpointAnalyzer setAsrFeaturesQueue:]
- -[CSHybridEndpointAnalyzer setAsrFeaturesWarmupLatency:]
- -[CSHybridEndpointAnalyzer setAutomaticEndpointingSuspensionEndTime:]
- -[CSHybridEndpointAnalyzer setCanProcessCurrentRequest:]
- -[CSHybridEndpointAnalyzer setClampedASRFeatureLatencyMsForClientLag:]
- -[CSHybridEndpointAnalyzer setClientLagThresholdMs:]
- -[CSHybridEndpointAnalyzer setCurrentAsset:]
- -[CSHybridEndpointAnalyzer setCurrentRequestSampleRate:]
- -[CSHybridEndpointAnalyzer setDelay:]
- -[CSHybridEndpointAnalyzer setDidAddAudio:]
- -[CSHybridEndpointAnalyzer setDidCommunicateEndpoint:]
- -[CSHybridEndpointAnalyzer setDidDetectSpeech:]
- -[CSHybridEndpointAnalyzer setDidNotifyTwoShot:]
- -[CSHybridEndpointAnalyzer setDidReceiveASRFeatures:]
- -[CSHybridEndpointAnalyzer setDidTimestampFirstAudioPacket:]
- -[CSHybridEndpointAnalyzer setEndWaitTime:]
- -[CSHybridEndpointAnalyzer setEndpointStyle:]
- -[CSHybridEndpointAnalyzer setEpResult:]
- -[CSHybridEndpointAnalyzer setFirstAudioPacketTimestamp:]
- -[CSHybridEndpointAnalyzer setFirstAudioSampleSensorTimestamp:]
- -[CSHybridEndpointAnalyzer setHepAudioOriginInMs:]
- -[CSHybridEndpointAnalyzer setHybridClassifier:]
- -[CSHybridEndpointAnalyzer setHybridClassifierQueue:]
- -[CSHybridEndpointAnalyzer setImplDelegate:]
- -[CSHybridEndpointAnalyzer setInterspeechWaitTime:]
- -[CSHybridEndpointAnalyzer setIsAnchorTimeBuffered:]
- -[CSHybridEndpointAnalyzer setIsRequestTimeout:]
- -[CSHybridEndpointAnalyzer setLastASRFeatureTimestamp:]
- -[CSHybridEndpointAnalyzer setLastEndpointPosterior:]
- -[CSHybridEndpointAnalyzer setLastKnownASRFeatureLatency:]
- -[CSHybridEndpointAnalyzer setLastKnownASRFeatures:]
- -[CSHybridEndpointAnalyzer setLastKnownOSDFeatures:]
- -[CSHybridEndpointAnalyzer setLastReportedEndpointTimeMs:]
- -[CSHybridEndpointAnalyzer setMinimumDurationForEndpointer:]
- -[CSHybridEndpointAnalyzer setNumSamplesProcessed:]
- -[CSHybridEndpointAnalyzer setNumSamplesProcessedBeforeAnchorTime:]
- -[CSHybridEndpointAnalyzer setOsdAnalyzer:]
- -[CSHybridEndpointAnalyzer setOsdFeaturesAtEndpoint:]
- -[CSHybridEndpointAnalyzer setOsdQueue:]
- -[CSHybridEndpointAnalyzer setPostVoiceTriggerSilence:]
- -[CSHybridEndpointAnalyzer setProcessedAudioInSeconds:]
- -[CSHybridEndpointAnalyzer setRecordContext:]
- -[CSHybridEndpointAnalyzer setRecordingDidStop:]
- -[CSHybridEndpointAnalyzer setSaveSamplesSeenInReset:]
- -[CSHybridEndpointAnalyzer setSpeechEndpointDetected:]
- -[CSHybridEndpointAnalyzer setStartWaitTime:]
- -[CSHybridEndpointAnalyzer setStateSerialQueue:]
- -[CSHybridEndpointAnalyzer setTwoShotSilenceThresholdInMs:]
- -[CSHybridEndpointAnalyzer setUseDefaultASRFeaturesOnClientLag:]
- -[CSHybridEndpointAnalyzer setVtEndInSampleCount:]
- -[CSHybridEndpointAnalyzer setVtExtraAudioAtStartInMs:]
- -[CSHybridEndpointAnalyzer shouldAcceptEagerResultForDuration:resultsCompletionHandler:]
- -[CSHybridEndpointAnalyzer speechEndpointDetected]
- -[CSHybridEndpointAnalyzer startWaitTime]
- -[CSHybridEndpointAnalyzer stateSerialQueue]
- -[CSHybridEndpointAnalyzer stopEndpointer]
- -[CSHybridEndpointAnalyzer twoShotSilenceThresholdInMs]
- -[CSHybridEndpointAnalyzer updateEndpointerDelayedTrigger:]
- -[CSHybridEndpointAnalyzer updateEndpointerThreshold:]
- -[CSHybridEndpointAnalyzer useDefaultASRFeaturesOnClientLag]
- -[CSHybridEndpointAnalyzer vtEndInSampleCount]
- -[CSHybridEndpointAnalyzer vtExtraAudioAtStartInMs]
- -[CSHybridEndpointer .cxx_destruct]
- -[CSHybridEndpointer _generateEndpointerFeaturesWithEffectiveClientProcessedAudioMs:osdFeatures:completion:]
- -[CSHybridEndpointer _getCSHybridEndpointerConfigForAsset:]
- -[CSHybridEndpointer _getSerialQueueWithName:targetQueue:]
- -[CSHybridEndpointer _isTaskStringAccessible:]
- -[CSHybridEndpointer _multimodalEndpointerEnabled]
- -[CSHybridEndpointer _processEnhancedEndpointerTaskString:]
- -[CSHybridEndpointer _readParametersFromHEPAsset:]
- -[CSHybridEndpointer _shouldAcceptEagerResultForDuration:asrFeatures:lastReportedEndpointTimeMs:osdFeatures:resultsCompletionHandler:]
- -[CSHybridEndpointer _shouldProvideTwoShotFeedbackWithRecordContext]
- -[CSHybridEndpointer _swapEnhancedEndpointerModelForTaskString:]
- -[CSHybridEndpointer _updateCurrentAsset:]
- -[CSHybridEndpointer _updateEndpointerDelayedTriggerByMhId:]
- -[CSHybridEndpointer _useEnhancedEndpointer]
- -[CSHybridEndpointer activeChannel]
- -[CSHybridEndpointer anchorMachAbsTime]
- -[CSHybridEndpointer asrFeaturesLatencies]
- -[CSHybridEndpointer asrFeaturesQueue]
- -[CSHybridEndpointer asrFeaturesWarmupLatency]
- -[CSHybridEndpointer audioDeliveryHostTimeDelta]
- -[CSHybridEndpointer automaticEndpointingSuspensionEndTime]
- -[CSHybridEndpointer canProcessCurrentRequest]
- -[CSHybridEndpointer clampedASRFeatureLatencyMsForClientLag]
- -[CSHybridEndpointer clientLagThresholdMs]
- -[CSHybridEndpointer currentAsset]
- -[CSHybridEndpointer currentRequestSampleRate]
- -[CSHybridEndpointer currentTaskString]
- -[CSHybridEndpointer delay]
- -[CSHybridEndpointer delegate]
- -[CSHybridEndpointer didCommunicateEndpoint]
- -[CSHybridEndpointer didDetectSpeech]
- -[CSHybridEndpointer didNotifyTwoShot]
- -[CSHybridEndpointer didReceiveASRFeatures]
- -[CSHybridEndpointer didReceiveRCFeatures]
- -[CSHybridEndpointer didTimestampFirstAudioPacket]
- -[CSHybridEndpointer disableRCSelection]
- -[CSHybridEndpointer endWaitTime]
- -[CSHybridEndpointer endpointStyle]
- -[CSHybridEndpointer endpointerAssetManagerDidUpdateAsset:]
- -[CSHybridEndpointer endpointerAssetManagerDidUpdateOSDAsset:]
- -[CSHybridEndpointer endpointerModelVersion]
- -[CSHybridEndpointer endpointerOperationMode]
- -[CSHybridEndpointer enhancedEndpointerDefaultResult]
- -[CSHybridEndpointer enhancedEndpointerTaskThresholdMap]
- -[CSHybridEndpointer enhancedEndpointer]
- -[CSHybridEndpointer epResult]
- -[CSHybridEndpointer extraDelayFrequency]
- -[CSHybridEndpointer fetchCurrentEndpointerOperationMode]
- -[CSHybridEndpointer firstAudioPacketTimestamp]
- -[CSHybridEndpointer firstAudioSampleSensorTimestamp]
- -[CSHybridEndpointer handleVoiceTriggerWithActivationInfo:]
- -[CSHybridEndpointer hasAcceptedEagerResult]
- -[CSHybridEndpointer hepAudioOriginInMs]
- -[CSHybridEndpointer hybridClassifierQueue]
- -[CSHybridEndpointer hybridClassifier]
- -[CSHybridEndpointer implDelegate]
- -[CSHybridEndpointer init]
- -[CSHybridEndpointer interspeechWaitTime]
- -[CSHybridEndpointer isASRFeatureFromServer]
- -[CSHybridEndpointer isAnchorTimeBuffered]
- -[CSHybridEndpointer isRequestTimeout]
- -[CSHybridEndpointer lastASRFeatureTimestamp]
- -[CSHybridEndpointer lastEndOfVoiceActivityTime]
- -[CSHybridEndpointer lastEndpointPosterior]
- -[CSHybridEndpointer lastKnownASRFeatureLatency]
- -[CSHybridEndpointer lastKnownASRFeatures]
- -[CSHybridEndpointer lastKnownOSDFeatures]
- -[CSHybridEndpointer lastKnownRCFeatureLatency]
- -[CSHybridEndpointer lastKnownRCFeatures]
- -[CSHybridEndpointer lastReportedEndpointTimeMs]
- -[CSHybridEndpointer lastStartOfVoiceActivityTime]
- -[CSHybridEndpointer logAnchorMachAbsTime:numSamplesProcessedBeforeAnchorTime:isAnchorTimeBuffered:audioDeliveryHostTimeDelta:]
- -[CSHybridEndpointer logFeaturesWithEvent:locale:]
- -[CSHybridEndpointer mhId]
- -[CSHybridEndpointer minimumDurationForEndpointer]
- -[CSHybridEndpointer numSamplesProcessedBeforeAnchorTime]
- -[CSHybridEndpointer osdFeaturesAtEndpoint]
- -[CSHybridEndpointer postVoiceTriggerSilence]
- -[CSHybridEndpointer preheat]
- -[CSHybridEndpointer processASRFeatures:fromServer:]
- -[CSHybridEndpointer processAudioSamplesAsynchronously:]
- -[CSHybridEndpointer processFirstAudioPacketTimestamp:firstAudioSampleSensorTimestamp:]
- -[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]
- -[CSHybridEndpointer processRCFeatures:]
- -[CSHybridEndpointer processTaskString:]
- -[CSHybridEndpointer processedAudioInSeconds]
- -[CSHybridEndpointer recordContext]
- -[CSHybridEndpointer recordingDidStop]
- -[CSHybridEndpointer recordingStoppedForReason:]
- -[CSHybridEndpointer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]
- -[CSHybridEndpointer reset]
- -[CSHybridEndpointer saveSamplesSeenInReset]
- -[CSHybridEndpointer setActiveChannel:]
- -[CSHybridEndpointer setAnchorMachAbsTime:]
- -[CSHybridEndpointer setAsrFeaturesLatencies:]
- -[CSHybridEndpointer setAsrFeaturesQueue:]
- -[CSHybridEndpointer setAsrFeaturesWarmupLatency:]
- -[CSHybridEndpointer setAudioDeliveryHostTimeDelta:]
- -[CSHybridEndpointer setAutomaticEndpointingSuspensionEndTime:]
- -[CSHybridEndpointer setCanProcessCurrentRequest:]
- -[CSHybridEndpointer setClampedASRFeatureLatencyMsForClientLag:]
- -[CSHybridEndpointer setClientLagThresholdMs:]
- -[CSHybridEndpointer setCurrentAsset:]
- -[CSHybridEndpointer setCurrentRequestSampleRate:]
- -[CSHybridEndpointer setCurrentTaskString:]
- -[CSHybridEndpointer setDelay:]
- -[CSHybridEndpointer setDelegate:]
- -[CSHybridEndpointer setDidCommunicateEndpoint:]
- -[CSHybridEndpointer setDidDetectSpeech:]
- -[CSHybridEndpointer setDidNotifyTwoShot:]
- -[CSHybridEndpointer setDidReceiveASRFeatures:]
- -[CSHybridEndpointer setDidReceiveRCFeatures:]
- -[CSHybridEndpointer setDidTimestampFirstAudioPacket:]
- -[CSHybridEndpointer setDisableRCSelection:]
- -[CSHybridEndpointer setEndWaitTime:]
- -[CSHybridEndpointer setEndpointStyle:]
- -[CSHybridEndpointer setEndpointerModelVersion:]
- -[CSHybridEndpointer setEndpointerOperationMode:]
- -[CSHybridEndpointer setEnhancedEndpointer:]
- -[CSHybridEndpointer setEnhancedEndpointerDefaultResult:]
- -[CSHybridEndpointer setEnhancedEndpointerTaskThresholdMap:]
- -[CSHybridEndpointer setEpResult:]
- -[CSHybridEndpointer setExtraDelayFrequency:]
- -[CSHybridEndpointer setFirstAudioPacketTimestamp:]
- -[CSHybridEndpointer setFirstAudioSampleSensorTimestamp:]
- -[CSHybridEndpointer setHasAcceptedEagerResult:]
- -[CSHybridEndpointer setHepAudioOriginInMs:]
- -[CSHybridEndpointer setHybridClassifier:]
- -[CSHybridEndpointer setHybridClassifierQueue:]
- -[CSHybridEndpointer setImplDelegate:]
- -[CSHybridEndpointer setInterspeechWaitTime:]
- -[CSHybridEndpointer setIsASRFeatureFromServer:]
- -[CSHybridEndpointer setIsAnchorTimeBuffered:]
- -[CSHybridEndpointer setIsRequestTimeout:]
- -[CSHybridEndpointer setLastASRFeatureTimestamp:]
- -[CSHybridEndpointer setLastEndpointPosterior:]
- -[CSHybridEndpointer setLastKnownASRFeatureLatency:]
- -[CSHybridEndpointer setLastKnownASRFeatures:]
- -[CSHybridEndpointer setLastKnownOSDFeatures:]
- -[CSHybridEndpointer setLastKnownRCFeatureLatency:]
- -[CSHybridEndpointer setLastKnownRCFeatures:]
- -[CSHybridEndpointer setLastReportedEndpointTimeMs:]
- -[CSHybridEndpointer setMhId:]
- -[CSHybridEndpointer setMinimumDurationForEndpointer:]
- -[CSHybridEndpointer setNumSamplesProcessedBeforeAnchorTime:]
- -[CSHybridEndpointer setOsdFeaturesAtEndpoint:]
- -[CSHybridEndpointer setPostVoiceTriggerSilence:]
- -[CSHybridEndpointer setProcessedAudioInSeconds:]
- -[CSHybridEndpointer setRecordContext:]
- -[CSHybridEndpointer setRecordingDidStop:]
- -[CSHybridEndpointer setSaveSamplesSeenInReset:]
- -[CSHybridEndpointer setSpeechEndpointDetected:]
- -[CSHybridEndpointer setStartWaitTime:]
- -[CSHybridEndpointer setStateSerialQueue:]
- -[CSHybridEndpointer setTaskEnhancedEndpointerMap:]
- -[CSHybridEndpointer setTaskThresholdMap:]
- -[CSHybridEndpointer setTwoShotSilenceThresholdInMs:]
- -[CSHybridEndpointer setUseDefaultASRFeaturesOnClientLag:]
- -[CSHybridEndpointer setVtEndInSampleCount:]
- -[CSHybridEndpointer setVtExtraAudioAtStartInMs:]
- -[CSHybridEndpointer shouldAcceptEagerResultForDuration:resultsCompletionHandler:]
- -[CSHybridEndpointer shouldAcceptEagerResultForDuration:withEndpointerMetrics:resultsCompletionHandler:]
- -[CSHybridEndpointer shouldAcceptEagerResultForDurationSync:withEndpointerMetrics:]
- -[CSHybridEndpointer speechEndpointDetected]
- -[CSHybridEndpointer startWaitTime]
- -[CSHybridEndpointer stateSerialQueue]
- -[CSHybridEndpointer stopEndpointer]
- -[CSHybridEndpointer taskEnhancedEndpointerMap]
- -[CSHybridEndpointer taskThresholdMap]
- -[CSHybridEndpointer terminateProcessing]
- -[CSHybridEndpointer twoShotSilenceThresholdInMs]
- -[CSHybridEndpointer updateEndpointerDelayedTrigger:]
- -[CSHybridEndpointer updateEndpointerThreshold:]
- -[CSHybridEndpointer updateEnhancedEndpointerDefaultThresholdPartial:defaultThresholdRC:relaxedThresholdPartial:relaxedThresholdRC:]
- -[CSHybridEndpointer useDefaultASRFeaturesOnClientLag]
- -[CSHybridEndpointer vtEndInSampleCount]
- -[CSHybridEndpointer vtExtraAudioAtStartInMs]
- -[CSNNVADEndpointAnalyzer .cxx_destruct]
- -[CSNNVADEndpointAnalyzer _checkSNObservationForEndpoint:]
- -[CSNNVADEndpointAnalyzer _checkSNObservationForStartpoint:]
- -[CSNNVADEndpointAnalyzer _effectiveAudioTimeInSecsForSNObservation:]
- -[CSNNVADEndpointAnalyzer _emitEndpointDetectedEventWithEndpointTime:endpointBufferHostTime:]
- -[CSNNVADEndpointAnalyzer _pcmBufferForAudioChunk:]
- -[CSNNVADEndpointAnalyzer _reportAudioFirstBufferInfoIfNecessary]
- -[CSNNVADEndpointAnalyzer _reportEndpointAtTsInSecs:]
- -[CSNNVADEndpointAnalyzer _reportStartpointAtTsInSecs:]
- -[CSNNVADEndpointAnalyzer _reportTwoShotAtTsInSecs:]
- -[CSNNVADEndpointAnalyzer _shouldEnterTwoShotAtAudioTimeInSecs:]
- -[CSNNVADEndpointAnalyzer _trailingSilenceDurationAtEndpoint]
- -[CSNNVADEndpointAnalyzer activeChannel]
- -[CSNNVADEndpointAnalyzer anchorMachAbsTime]
- -[CSNNVADEndpointAnalyzer audioFileWriter]
- -[CSNNVADEndpointAnalyzer automaticEndpointingSuspensionEndTime]
- -[CSNNVADEndpointAnalyzer canProcessCurrentRequest]
- -[CSNNVADEndpointAnalyzer currentRequestAudioFormat]
- -[CSNNVADEndpointAnalyzer currentRequestSampleRate]
- -[CSNNVADEndpointAnalyzer delay]
- -[CSNNVADEndpointAnalyzer delegate]
- -[CSNNVADEndpointAnalyzer didEnterTwoshot]
- -[CSNNVADEndpointAnalyzer endWaitTime]
- -[CSNNVADEndpointAnalyzer endpointStyle]
- -[CSNNVADEndpointAnalyzer finishedSkippingSamplesForVT]
- -[CSNNVADEndpointAnalyzer firstAudioSampleSensorTimestamp]
- -[CSNNVADEndpointAnalyzer firstSampleId]
- -[CSNNVADEndpointAnalyzer framePosition]
- -[CSNNVADEndpointAnalyzer handleVoiceTriggerWithActivationInfo:]
- -[CSNNVADEndpointAnalyzer hasReportedFirstAudioSampleSensorTimestamp]
- -[CSNNVADEndpointAnalyzer implDelegate]
- -[CSNNVADEndpointAnalyzer init]
- -[CSNNVADEndpointAnalyzer interspeechWaitTime]
- -[CSNNVADEndpointAnalyzer isAnchorTimeBuffered]
- -[CSNNVADEndpointAnalyzer isRequestTimeout]
- -[CSNNVADEndpointAnalyzer lastEndOfVoiceActivityTime]
- -[CSNNVADEndpointAnalyzer lastStartOfVoiceActivityTime]
- -[CSNNVADEndpointAnalyzer mhId]
- -[CSNNVADEndpointAnalyzer minimumDurationForEndpointer]
- -[CSNNVADEndpointAnalyzer nnvadAudioOriginInMs]
- -[CSNNVADEndpointAnalyzer nnvadState]
- -[CSNNVADEndpointAnalyzer numSamplesProcessedBeforeAnchorTime]
- -[CSNNVADEndpointAnalyzer numSamplesReceived]
- -[CSNNVADEndpointAnalyzer numSamplesSkippedForVT]
- -[CSNNVADEndpointAnalyzer preheat]
- -[CSNNVADEndpointAnalyzer processAudioSamplesAsynchronously:]
- -[CSNNVADEndpointAnalyzer queue]
- -[CSNNVADEndpointAnalyzer recordingStoppedForReason:]
- -[CSNNVADEndpointAnalyzer request:didFailWithError:]
- -[CSNNVADEndpointAnalyzer request:didProduceResult:]
- -[CSNNVADEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]
- -[CSNNVADEndpointAnalyzer reset]
- -[CSNNVADEndpointAnalyzer saveSamplesSeenInReset]
- -[CSNNVADEndpointAnalyzer setActiveChannel:]
- -[CSNNVADEndpointAnalyzer setAnchorMachAbsTime:]
- -[CSNNVADEndpointAnalyzer setAudioFileWriter:]
- -[CSNNVADEndpointAnalyzer setAutomaticEndpointingSuspensionEndTime:]
- -[CSNNVADEndpointAnalyzer setCurrentRequestAudioFormat:]
- -[CSNNVADEndpointAnalyzer setCurrentRequestSampleRate:]
- -[CSNNVADEndpointAnalyzer setDelay:]
- -[CSNNVADEndpointAnalyzer setDelegate:]
- -[CSNNVADEndpointAnalyzer setDidEnterTwoshot:]
- -[CSNNVADEndpointAnalyzer setEndWaitTime:]
- -[CSNNVADEndpointAnalyzer setEndpointStyle:]
- -[CSNNVADEndpointAnalyzer setFinishedSkippingSamplesForVT:]
- -[CSNNVADEndpointAnalyzer setFirstAudioSampleSensorTimestamp:]
- -[CSNNVADEndpointAnalyzer setFirstSampleId:]
- -[CSNNVADEndpointAnalyzer setFramePosition:]
- -[CSNNVADEndpointAnalyzer setHasReportedFirstAudioSampleSensorTimestamp:]
- -[CSNNVADEndpointAnalyzer setImplDelegate:]
- -[CSNNVADEndpointAnalyzer setInterspeechWaitTime:]
- -[CSNNVADEndpointAnalyzer setIsAnchorTimeBuffered:]
- -[CSNNVADEndpointAnalyzer setIsRequestTimeout:]
- -[CSNNVADEndpointAnalyzer setMhId:]
- -[CSNNVADEndpointAnalyzer setMinimumDurationForEndpointer:]
- -[CSNNVADEndpointAnalyzer setNnvadAudioOriginInMs:]
- -[CSNNVADEndpointAnalyzer setNnvadState:]
- -[CSNNVADEndpointAnalyzer setNumSamplesProcessedBeforeAnchorTime:]
- -[CSNNVADEndpointAnalyzer setNumSamplesReceived:]
- -[CSNNVADEndpointAnalyzer setNumSamplesSkippedForVT:]
- -[CSNNVADEndpointAnalyzer setQueue:]
- -[CSNNVADEndpointAnalyzer setSaveSamplesSeenInReset:]
- -[CSNNVADEndpointAnalyzer setShouldDetectTwoShot:]
- -[CSNNVADEndpointAnalyzer setSnAudioStreamAnalyzer:]
- -[CSNNVADEndpointAnalyzer setStartWaitTime:]
- -[CSNNVADEndpointAnalyzer setVtEndInSampleCount:]
- -[CSNNVADEndpointAnalyzer setVtEndInSecs:]
- -[CSNNVADEndpointAnalyzer setVtExtraAudioAtStartInMs:]
- -[CSNNVADEndpointAnalyzer shouldDetectTwoShot]
- -[CSNNVADEndpointAnalyzer snAudioStreamAnalyzer]
- -[CSNNVADEndpointAnalyzer startWaitTime]
- -[CSNNVADEndpointAnalyzer stopEndpointer]
- -[CSNNVADEndpointAnalyzer vtEndInSampleCount]
- -[CSNNVADEndpointAnalyzer vtEndInSecs]
- -[CSNNVADEndpointAnalyzer vtExtraAudioAtStartInMs]
- -[CSOtherAppRecordingStateMonitorASMac isOtherNonEligibleAppRecording]
- -[CSSelfTriggerController initWithTargetQueue:audioTapProvider:avvcRefChannelAvailable:]
- -[CSSelfTriggerDetector audioTapProvider]
- -[CSSelfTriggerDetector initWithTargetQueue:audioTapProvider:audioSourceType:]
- -[CSSelfTriggerDetector mode]
- -[CSSelfTriggerDetector setAudioTapProvider:]
- -[CSSelfTriggerDetector setMode:]
- -[CSSiriSpeechRecorder _cancelExtendedEndpointTimer]
- -[CSSiriSpeechRecorder _mapInstrumentationEndpointTypeFromStopRecordingReason:]
- -[CSSiriSpeechRecorder _playStopAlertIfNecessaryForReason:endpointMode:error:]
- -[CSSiriSpeechRecorder _scheduleExtendedEndpointTimer]
- -[CSSiriSpeechRecorder _setEndpointStyle:]
- -[CSSiriSpeechRecorder endpointer:didDetectHardEndpointAtTime:withMetrics:]
- -[CSSiriSpeechRecorder endpointer:didDetectStartpointAtTime:]
- -[CSSiriSpeechRecorder getLastStartpointTimestampAndCurrentTime:]
- -[CSSiriSpeechRecorder setEndpointerDelayedTrigger:]
- -[CSSiriSpeechRecorder setEndpointerThreshold:]
- -[CSSiriSpeechRecorder suspendAutomaticEndpointingInRange:]
- -[CSSmartSiriVolume startSmartSiriVolume]
- -[CSSmartSiriVolumeManager startSmartSiriVolume]
- -[CSSpeechController _scheduleAudibleFeedbackAtStartRecording]
- -[CSSpeechController _startPhaticDecision]
- -[CSSpeechController endpointer:detectedTwoShotAtTime:]
- -[CSSpeechController endpointerProxy]
- -[CSSpeechController initWithEndpointId:xpcClientFactory:endpointer:continuousVoiceTrigger:siriVolumeController:mediaPlayingMonitor:alarmMonitor:timerMonitor:audioSessionController:supportPhatic:supportHearstVoiceTrigger:supportTriagleModeSessionActivationRetry:supportSessionActivateDelay:supportsDuckingOnSpeakerEvaluator:]
- -[CSSpeechController lastEndOfVoiceActivityTime]
- -[CSSpeechController resetEndpointer]
- -[CSSpeechController setEndpointerProxy:]
- -[CSSpeechController stopEndpointer]
- -[CSSpeechController updateEndpointerDelayedTrigger:]
- -[CSSpeechController updateEndpointerThreshold:]
- -[CSSpeechManager _isAVVCRefChannelAvailable]
- -[CSSpeechManager _shouldSetupSelfTrigger]
- -[CSSpeechManager audioFingerprintProvider]
- -[CSSpeechManager audioTapProvider]
- -[CSSpeechManager setAudioTapProvider:]
- -[CSXPCClient attachTandemStream:toPrimaryStream:completion:]
- -[NviCSAudioDataSource .cxx_destruct]
- -[NviCSAudioDataSource _createAudioStreamWithCurrentNviContext]
- -[NviCSAudioDataSource addReceiver:]
- -[NviCSAudioDataSource audioStreamProvider:audioBufferAvailable:]
- -[NviCSAudioDataSource audioStreamProvider:audioChunkForTVAvailable:]
- -[NviCSAudioDataSource audioStreamProvider:avBufferAvailable:]
- -[NviCSAudioDataSource audioStreamProvider:didStopStreamUnexpectedly:]
- -[NviCSAudioDataSource audioStream]
- -[NviCSAudioDataSource init]
- -[NviCSAudioDataSource numBytesPerSample]
- -[NviCSAudioDataSource nviCtx]
- -[NviCSAudioDataSource queue]
- -[NviCSAudioDataSource receivers]
- -[NviCSAudioDataSource removeReceiver:]
- -[NviCSAudioDataSource sampleRate]
- -[NviCSAudioDataSource setAudioStream:]
- -[NviCSAudioDataSource setNviCtx:]
- -[NviCSAudioDataSource setQueue:]
- -[NviCSAudioDataSource setReceivers:]
- -[NviCSAudioDataSource startWithNviContext:didStartHandler:]
- -[NviCSAudioDataSource stopWithDidStopHandler:]
- -[NviCSAudioDataSource type]
- GCC_except_table1116
- GCC_except_table1128
- GCC_except_table1331
- GCC_except_table1397
- GCC_except_table1421
- GCC_except_table1425
- GCC_except_table1441
- GCC_except_table1444
- GCC_except_table1472
- GCC_except_table1570
- GCC_except_table1572
- GCC_except_table1580
- GCC_except_table1635
- GCC_except_table1661
- GCC_except_table1667
- GCC_except_table1748
- GCC_except_table1884
- GCC_except_table2138
- GCC_except_table2168
- GCC_except_table2171
- GCC_except_table2174
- GCC_except_table2179
- GCC_except_table2191
- GCC_except_table2196
- GCC_except_table2199
- GCC_except_table2314
- GCC_except_table2317
- GCC_except_table2321
- GCC_except_table2339
- GCC_except_table2474
- GCC_except_table2532
- GCC_except_table2544
- GCC_except_table2577
- GCC_except_table2598
- GCC_except_table2612
- GCC_except_table2653
- GCC_except_table2654
- GCC_except_table2655
- GCC_except_table2656
- GCC_except_table2657
- GCC_except_table2661
- GCC_except_table2664
- GCC_except_table2672
- GCC_except_table2673
- GCC_except_table2688
- GCC_except_table2690
- GCC_except_table2691
- GCC_except_table2757
- GCC_except_table3022
- GCC_except_table3179
- GCC_except_table3182
- GCC_except_table3185
- GCC_except_table3216
- GCC_except_table3276
- GCC_except_table3481
- GCC_except_table3507
- GCC_except_table3568
- GCC_except_table3571
- GCC_except_table3573
- GCC_except_table3589
- GCC_except_table3591
- GCC_except_table3593
- GCC_except_table3595
- GCC_except_table3597
- GCC_except_table3599
- GCC_except_table3601
- GCC_except_table3604
- GCC_except_table3612
- GCC_except_table3615
- GCC_except_table3621
- GCC_except_table3623
- GCC_except_table3625
- GCC_except_table3627
- GCC_except_table3629
- GCC_except_table3631
- GCC_except_table3636
- GCC_except_table3641
- GCC_except_table3649
- GCC_except_table3658
- GCC_except_table3663
- GCC_except_table3801
- GCC_except_table3825
- GCC_except_table3885
- GCC_except_table3899
- GCC_except_table3920
- GCC_except_table4010
- GCC_except_table4259
- GCC_except_table4326
- GCC_except_table4327
- GCC_except_table4334
- GCC_except_table4363
- GCC_except_table4413
- GCC_except_table4419
- GCC_except_table4685
- GCC_except_table4692
- GCC_except_table4699
- GCC_except_table4705
- GCC_except_table4753
- GCC_except_table4909
- GCC_except_table4919
- GCC_except_table4943
- GCC_except_table4963
- GCC_except_table5043
- GCC_except_table5055
- GCC_except_table5064
- GCC_except_table5071
- GCC_except_table5077
- GCC_except_table5079
- GCC_except_table5082
- GCC_except_table5090
- GCC_except_table5092
- GCC_except_table5096
- GCC_except_table5098
- GCC_except_table5109
- GCC_except_table5110
- GCC_except_table5115
- GCC_except_table5126
- GCC_except_table5128
- GCC_except_table5130
- GCC_except_table5133
- GCC_except_table5135
- GCC_except_table5137
- GCC_except_table5139
- GCC_except_table5141
- GCC_except_table5143
- GCC_except_table5144
- GCC_except_table5145
- GCC_except_table5147
- GCC_except_table5162
- GCC_except_table5236
- GCC_except_table5240
- GCC_except_table5294
- GCC_except_table5323
- GCC_except_table5326
- GCC_except_table5511
- GCC_except_table5527
- GCC_except_table5535
- GCC_except_table5542
- GCC_except_table5559
- GCC_except_table5563
- GCC_except_table5567
- GCC_except_table5569
- GCC_except_table5578
- GCC_except_table5834
- GCC_except_table5865
- GCC_except_table5870
- GCC_except_table5907
- GCC_except_table5916
- GCC_except_table5943
- GCC_except_table6012
- GCC_except_table6205
- GCC_except_table6213
- GCC_except_table6233
- GCC_except_table6238
- GCC_except_table6340
- GCC_except_table6395
- GCC_except_table6486
- GCC_except_table6487
- GCC_except_table6497
- GCC_except_table6498
- GCC_except_table6510
- GCC_except_table6643
- GCC_except_table6661
- GCC_except_table6665
- GCC_except_table6670
- GCC_except_table6675
- GCC_except_table6682
- GCC_except_table6684
- GCC_except_table6712
- GCC_except_table6793
- GCC_except_table6805
- GCC_except_table6828
- GCC_except_table6839
- GCC_except_table6842
- GCC_except_table6865
- GCC_except_table6877
- GCC_except_table7230
- GCC_except_table7265
- GCC_except_table7341
- GCC_except_table7351
- GCC_except_table7353
- GCC_except_table7354
- GCC_except_table7356
- GCC_except_table7363
- GCC_except_table7368
- GCC_except_table7369
- GCC_except_table7373
- GCC_except_table7374
- GCC_except_table7378
- GCC_except_table7379
- GCC_except_table7380
- GCC_except_table7381
- GCC_except_table7383
- GCC_except_table7384
- GCC_except_table7385
- GCC_except_table7386
- GCC_except_table7388
- GCC_except_table7390
- GCC_except_table7391
- GCC_except_table7474
- GCC_except_table7498
- GCC_except_table7540
- GCC_except_table7551
- GCC_except_table7697
- GCC_except_table7705
- GCC_except_table7811
- GCC_except_table7812
- GCC_except_table7813
- GCC_except_table7814
- GCC_except_table7815
- GCC_except_table7820
- GCC_except_table7883
- GCC_except_table7925
- GCC_except_table7950
- GCC_except_table7965
- GCC_except_table7973
- GCC_except_table7979
- GCC_except_table7999
- GCC_except_table8135
- _AFDeviceSupportsZLL
- _AudioConverterFillComplexBuffer_BlockInvoke.27006
- _AudioQueueAddPropertyListener
- _AudioQueueAllocateBuffer
- _AudioQueueDispose
- _AudioQueueEnqueueBuffer
- _AudioQueueFreeBuffer
- _AudioQueueGetProperty
- _AudioQueueNewInput
- _AudioQueueRemovePropertyListener
- _AudioQueueSetProperty
- _AudioQueueStart
- _AudioQueueStop
- _CSAttendingStopReasonGetFromName
- _CSAttendingStopReasonGetFromName.map
- _CSAttendingStopReasonGetFromName.onceToken
- _CSSiriSpeechRecordingGetUsesAutomaticEndpointingFromRequestOptions
- _MobileTimerLibrary.798
- _MobileTimerLibraryCore.frameworkLibrary.803
- _OBJC_CLASS_$_AFMyriadContext
- _OBJC_CLASS_$_AFMyriadMonitor
- _OBJC_CLASS_$_AFMyriadPerceptualAudioHash
- _OBJC_CLASS_$_ATAudioTap
- _OBJC_CLASS_$_ATAudioTapDescription
- _OBJC_CLASS_$_CSAudioInjectionBuiltInEngine
- _OBJC_CLASS_$_CSAudioInjectionEngine
- _OBJC_CLASS_$_CSAudioInjectionHearstEngine
- _OBJC_CLASS_$_CSAudioInjectionRemoraEngine
- _OBJC_CLASS_$_CSAudioInjectionTvRemoteEngine
- _OBJC_CLASS_$_CSAudioProviderSelectingProxy
- _OBJC_CLASS_$_CSEndpointerProxy
- _OBJC_CLASS_$_CSHybridEndpointer
- _OBJC_CLASS_$_CSNNVADEndpointAnalyzer
- _OBJC_CLASS_$_CSOtherAppRecordingStateMonitor
- _OBJC_CLASS_$_CSOtherAppRecordingStateMonitorASMac
- _OBJC_CLASS_$_NviCSAudioDataSource
- _OBJC_CLASS_$_SNDetectSpeechUtteranceRequest
- _OBJC_IVAR_$_CSAudioInjectionBuiltInEngine._circularBuffer
- _OBJC_IVAR_$_CSAudioInjectionBuiltInEngine._connectedDevice
- _OBJC_IVAR_$_CSAudioInjectionBuiltInEngine._delegate
- _OBJC_IVAR_$_CSAudioInjectionBuiltInEngine._hostTimeBuffer
- _OBJC_IVAR_$_CSAudioInjectionBuiltInEngine._isForwarding
- _OBJC_IVAR_$_CSAudioInjectionBuiltInEngine._keywordAnalyzer
- _OBJC_IVAR_$_CSAudioInjectionBuiltInEngine._lastForwardedSampleCount
- _OBJC_IVAR_$_CSAudioInjectionBuiltInEngine._queue
- _OBJC_IVAR_$_CSAudioInjectionBuiltInEngine._userIntentOptions
- _OBJC_IVAR_$_CSAudioInjectionBuiltInEngine._uuid
- _OBJC_IVAR_$_CSAudioInjectionBuiltInEngine._voiceTriggerEnabled
- _OBJC_IVAR_$_CSAudioInjectionBuiltInEngine._voiceTriggerSampleCount
- _OBJC_IVAR_$_CSAudioInjectionEngine._audioFeedTimer
- _OBJC_IVAR_$_CSAudioInjectionEngine._audioStreamHandleId
- _OBJC_IVAR_$_CSAudioInjectionEngine._bufferDuration
- _OBJC_IVAR_$_CSAudioInjectionEngine._deinterleaver
- _OBJC_IVAR_$_CSAudioInjectionEngine._delegate
- _OBJC_IVAR_$_CSAudioInjectionEngine._didSetScaleFactor
- _OBJC_IVAR_$_CSAudioInjectionEngine._fileOption
- _OBJC_IVAR_$_CSAudioInjectionEngine._injectionAudioFileList
- _OBJC_IVAR_$_CSAudioInjectionEngine._injectionCompletionNotifyBlocks
- _OBJC_IVAR_$_CSAudioInjectionEngine._injectionStartNotifyBlocks
- _OBJC_IVAR_$_CSAudioInjectionEngine._inputRecordingNumberOfChannels
- _OBJC_IVAR_$_CSAudioInjectionEngine._isRecording
- _OBJC_IVAR_$_CSAudioInjectionEngine._outASBD
- _OBJC_IVAR_$_CSAudioInjectionEngine._pNonInterleavedABL
- _OBJC_IVAR_$_CSAudioInjectionEngine._queue
- _OBJC_IVAR_$_CSAudioInjectionEngine._scaleFactor
- _OBJC_IVAR_$_CSAudioInjectionEngine._uuid
- _OBJC_IVAR_$_CSAudioInjectionHearstEngine._circularBuffer
- _OBJC_IVAR_$_CSAudioInjectionHearstEngine._connectedDevice
- _OBJC_IVAR_$_CSAudioInjectionHearstEngine._delegate
- _OBJC_IVAR_$_CSAudioInjectionHearstEngine._isForwarding
- _OBJC_IVAR_$_CSAudioInjectionHearstEngine._keywordAnalyzer
- _OBJC_IVAR_$_CSAudioInjectionHearstEngine._lastDetectedVoiceTriggerBeginSampleCount
- _OBJC_IVAR_$_CSAudioInjectionHearstEngine._lastForwardedSampleCount
- _OBJC_IVAR_$_CSAudioInjectionHearstEngine._queue
- _OBJC_IVAR_$_CSAudioInjectionHearstEngine._uuid
- _OBJC_IVAR_$_CSAudioInjectionHearstEngine._voiceTriggerEnabled
- _OBJC_IVAR_$_CSAudioInjectionProvider._builtInAudioInjectionEngine
- _OBJC_IVAR_$_CSAudioInjectionProvider._builtInDevice
- _OBJC_IVAR_$_CSAudioInjectionProvider._bundleTvRemote
- _OBJC_IVAR_$_CSAudioInjectionRemoraEngine._circularBuffer
- _OBJC_IVAR_$_CSAudioInjectionRemoraEngine._connectedDevice
- _OBJC_IVAR_$_CSAudioInjectionRemoraEngine._delegate
- _OBJC_IVAR_$_CSAudioInjectionRemoraEngine._isForwarding
- _OBJC_IVAR_$_CSAudioInjectionRemoraEngine._keywordAnalyzer
- _OBJC_IVAR_$_CSAudioInjectionRemoraEngine._lastDetectedVoiceTriggerBeginSampleCount
- _OBJC_IVAR_$_CSAudioInjectionRemoraEngine._lastForwardedSampleCount
- _OBJC_IVAR_$_CSAudioInjectionRemoraEngine._queue
- _OBJC_IVAR_$_CSAudioInjectionRemoraEngine._uuid
- _OBJC_IVAR_$_CSAudioInjectionRemoraEngine._voiceTriggerEnabled
- _OBJC_IVAR_$_CSAudioInjectionTvRemoteEngine._connectedDevice
- _OBJC_IVAR_$_CSAudioInjectionTvRemoteEngine._delegate
- _OBJC_IVAR_$_CSAudioInjectionTvRemoteEngine._encoder
- _OBJC_IVAR_$_CSAudioInjectionTvRemoteEngine._queue
- _OBJC_IVAR_$_CSAudioInjectionTvRemoteEngine._uuid
- _OBJC_IVAR_$_CSAudioTapProvider._UUIDString
- _OBJC_IVAR_$_CSAudioTapProvider._aqStartCompletion
- _OBJC_IVAR_$_CSAudioTapProvider._aqStopCompletion
- _OBJC_IVAR_$_CSAudioTapProvider._audioBuffers
- _OBJC_IVAR_$_CSAudioTapProvider._audioStream
- _OBJC_IVAR_$_CSAudioTapProvider._circularBuffer
- _OBJC_IVAR_$_CSAudioTapProvider._loggingQueue
- _OBJC_IVAR_$_CSAudioTapProvider._processedSampleCount
- _OBJC_IVAR_$_CSAudioTapProvider._queue
- _OBJC_IVAR_$_CSAudioTapProvider._recordingAudioQueue
- _OBJC_IVAR_$_CSAudioTapProvider._transaction
- _OBJC_IVAR_$_CSEndpointerProxy._accessibleEndpointerEnabled
- _OBJC_IVAR_$_CSEndpointerProxy._activeEndpointer
- _OBJC_IVAR_$_CSEndpointerProxy._endpointerDelegate
- _OBJC_IVAR_$_CSEndpointerProxy._endpointerImplDelegate
- _OBJC_IVAR_$_CSEndpointerProxy._hybridEndpointer
- _OBJC_IVAR_$_CSEndpointerProxy._nnvadEndpointer
- _OBJC_IVAR_$_CSEndpointerProxy._recordContext
- _OBJC_IVAR_$_CSEndpointerProxy._recordingDidStop
- _OBJC_IVAR_$_CSEndpointerXPCClient._activeEndpointer
- _OBJC_IVAR_$_CSEndpointerXPCClient._endpointerDelegate
- _OBJC_IVAR_$_CSEndpointerXPCClient._endpointerImplDelegate
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._anchorMachAbsTime
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._apQueue
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._asrFeatureLatencies
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._asrFeaturesQueue
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._asrFeaturesWarmupLatency
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._automaticEndpointingSuspensionEndTime
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._canProcessCurrentRequest
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._clampedASRFeatureLatencyMsForClientLag
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._clientLagThresholdMs
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._currentAsset
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._currentRequestSampleRate
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._delay
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._didAddAudio
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._didCommunicateEndpoint
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._didDetectSpeech
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._didNotifyTwoShot
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._didReceiveASRFeatures
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._didTimestampFirstAudioPacket
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._endWaitTime
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._endpointStyle
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._epResult
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._firstAudioPacketTimestamp
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._firstAudioSampleSensorTimestamp
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._hepAudioOriginInMs
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._hybridClassifier
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._hybridClassifierQueue
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._implDelegate
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._interspeechWaitTime
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._isAnchorTimeBuffered
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._isRequestTimeout
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._lastASRFeatureTimestamp
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._lastEndpointPosterior
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._lastKnownASRFeatureLatency
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._lastKnownASRFeatures
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._lastKnownOSDFeatures
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._lastReportedEndpointTimeMs
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._minimumDurationForEndpointer
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._numSamplesProcessed
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._numSamplesProcessedBeforeAnchorTime
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._osdAnalyzer
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._osdFeaturesAtEndpoint
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._osdQueue
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._postVoiceTriggerSilence
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._processedAudioInSeconds
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._recordContext
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._recordingDidStop
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._saveSamplesSeenInReset
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._speechEndpointDetected
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._startWaitTime
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._stateSerialQueue
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._twoShotSilenceThresholdInMs
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._useDefaultASRFeaturesOnClientLag
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._vtEndInSampleCount
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._vtExtraAudioAtStartInMs
- _OBJC_IVAR_$_CSHybridEndpointer._activeChannel
- _OBJC_IVAR_$_CSHybridEndpointer._anchorMachAbsTime
- _OBJC_IVAR_$_CSHybridEndpointer._asrFeaturesLatencies
- _OBJC_IVAR_$_CSHybridEndpointer._asrFeaturesQueue
- _OBJC_IVAR_$_CSHybridEndpointer._asrFeaturesWarmupLatency
- _OBJC_IVAR_$_CSHybridEndpointer._audioDeliveryHostTimeDelta
- _OBJC_IVAR_$_CSHybridEndpointer._automaticEndpointingSuspensionEndTime
- _OBJC_IVAR_$_CSHybridEndpointer._canProcessCurrentRequest
- _OBJC_IVAR_$_CSHybridEndpointer._clampedASRFeatureLatencyMsForClientLag
- _OBJC_IVAR_$_CSHybridEndpointer._clientLagThresholdMs
- _OBJC_IVAR_$_CSHybridEndpointer._currentAsset
- _OBJC_IVAR_$_CSHybridEndpointer._currentRequestSampleRate
- _OBJC_IVAR_$_CSHybridEndpointer._currentTaskString
- _OBJC_IVAR_$_CSHybridEndpointer._delay
- _OBJC_IVAR_$_CSHybridEndpointer._delegate
- _OBJC_IVAR_$_CSHybridEndpointer._didCommunicateEndpoint
- _OBJC_IVAR_$_CSHybridEndpointer._didDetectSpeech
- _OBJC_IVAR_$_CSHybridEndpointer._didNotifyTwoShot
- _OBJC_IVAR_$_CSHybridEndpointer._didReceiveASRFeatures
- _OBJC_IVAR_$_CSHybridEndpointer._didReceiveRCFeatures
- _OBJC_IVAR_$_CSHybridEndpointer._didTimestampFirstAudioPacket
- _OBJC_IVAR_$_CSHybridEndpointer._disableRCSelection
- _OBJC_IVAR_$_CSHybridEndpointer._endWaitTime
- _OBJC_IVAR_$_CSHybridEndpointer._endpointStyle
- _OBJC_IVAR_$_CSHybridEndpointer._endpointerModelVersion
- _OBJC_IVAR_$_CSHybridEndpointer._endpointerOperationMode
- _OBJC_IVAR_$_CSHybridEndpointer._enhancedEndpointer
- _OBJC_IVAR_$_CSHybridEndpointer._enhancedEndpointerDefaultResult
- _OBJC_IVAR_$_CSHybridEndpointer._enhancedEndpointerTaskThresholdMap
- _OBJC_IVAR_$_CSHybridEndpointer._epResult
- _OBJC_IVAR_$_CSHybridEndpointer._extraDelayFrequency
- _OBJC_IVAR_$_CSHybridEndpointer._firstAudioPacketTimestamp
- _OBJC_IVAR_$_CSHybridEndpointer._firstAudioSampleSensorTimestamp
- _OBJC_IVAR_$_CSHybridEndpointer._hasAcceptedEagerResult
- _OBJC_IVAR_$_CSHybridEndpointer._hepAudioOriginInMs
- _OBJC_IVAR_$_CSHybridEndpointer._hybridClassifier
- _OBJC_IVAR_$_CSHybridEndpointer._hybridClassifierQueue
- _OBJC_IVAR_$_CSHybridEndpointer._implDelegate
- _OBJC_IVAR_$_CSHybridEndpointer._interspeechWaitTime
- _OBJC_IVAR_$_CSHybridEndpointer._isASRFeatureFromServer
- _OBJC_IVAR_$_CSHybridEndpointer._isAnchorTimeBuffered
- _OBJC_IVAR_$_CSHybridEndpointer._isRequestTimeout
- _OBJC_IVAR_$_CSHybridEndpointer._lastASRFeatureTimestamp
- _OBJC_IVAR_$_CSHybridEndpointer._lastEndpointPosterior
- _OBJC_IVAR_$_CSHybridEndpointer._lastKnownASRFeatureLatency
- _OBJC_IVAR_$_CSHybridEndpointer._lastKnownASRFeatures
- _OBJC_IVAR_$_CSHybridEndpointer._lastKnownOSDFeatures
- _OBJC_IVAR_$_CSHybridEndpointer._lastKnownRCFeatureLatency
- _OBJC_IVAR_$_CSHybridEndpointer._lastKnownRCFeatures
- _OBJC_IVAR_$_CSHybridEndpointer._lastReportedEndpointTimeMs
- _OBJC_IVAR_$_CSHybridEndpointer._mhId
- _OBJC_IVAR_$_CSHybridEndpointer._minimumDurationForEndpointer
- _OBJC_IVAR_$_CSHybridEndpointer._numSamplesProcessedBeforeAnchorTime
- _OBJC_IVAR_$_CSHybridEndpointer._osdFeaturesAtEndpoint
- _OBJC_IVAR_$_CSHybridEndpointer._postVoiceTriggerSilence
- _OBJC_IVAR_$_CSHybridEndpointer._processedAudioInSeconds
- _OBJC_IVAR_$_CSHybridEndpointer._recordContext
- _OBJC_IVAR_$_CSHybridEndpointer._recordingDidStop
- _OBJC_IVAR_$_CSHybridEndpointer._saveSamplesSeenInReset
- _OBJC_IVAR_$_CSHybridEndpointer._speechEndpointDetected
- _OBJC_IVAR_$_CSHybridEndpointer._startWaitTime
- _OBJC_IVAR_$_CSHybridEndpointer._stateSerialQueue
- _OBJC_IVAR_$_CSHybridEndpointer._taskEnhancedEndpointerMap
- _OBJC_IVAR_$_CSHybridEndpointer._taskThresholdMap
- _OBJC_IVAR_$_CSHybridEndpointer._twoShotSilenceThresholdInMs
- _OBJC_IVAR_$_CSHybridEndpointer._useDefaultASRFeaturesOnClientLag
- _OBJC_IVAR_$_CSHybridEndpointer._vtEndInSampleCount
- _OBJC_IVAR_$_CSHybridEndpointer._vtExtraAudioAtStartInMs
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._activeChannel
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._anchorMachAbsTime
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._audioFileWriter
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._automaticEndpointingSuspensionEndTime
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._currentRequestAudioFormat
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._currentRequestSampleRate
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._delay
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._delegate
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._didEnterTwoshot
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._endWaitTime
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._endpointStyle
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._finishedSkippingSamplesForVT
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._firstAudioSampleSensorTimestamp
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._firstSampleId
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._framePosition
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._hasReportedFirstAudioSampleSensorTimestamp
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._implDelegate
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._interspeechWaitTime
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._isAnchorTimeBuffered
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._isRequestTimeout
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._lastEndOfVoiceActivityTime
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._lastStartOfVoiceActivityTime
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._mhId
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._minimumDurationForEndpointer
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._nnvadAudioOriginInMs
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._nnvadState
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._numSamplesProcessedBeforeAnchorTime
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._numSamplesReceived
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._numSamplesSkippedForVT
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._queue
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._saveSamplesSeenInReset
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._shouldDetectTwoShot
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._snAudioStreamAnalyzer
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._startWaitTime
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._vtEndInSampleCount
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._vtEndInSecs
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._vtExtraAudioAtStartInMs
- _OBJC_IVAR_$_CSSelfTriggerDetector._audioTapProvider
- _OBJC_IVAR_$_CSSelfTriggerDetector._mode
- _OBJC_IVAR_$_CSSiriSpeechRecorder._extendedEndpointTimer
- _OBJC_IVAR_$_CSSpeechController._endpointerProxy
- _OBJC_IVAR_$_CSSpeechManager._audioTapProvider
- _OBJC_IVAR_$_NviCSAudioDataSource._audioStream
- _OBJC_IVAR_$_NviCSAudioDataSource._nviCtx
- _OBJC_IVAR_$_NviCSAudioDataSource._queue
- _OBJC_IVAR_$_NviCSAudioDataSource._receivers
- _OBJC_METACLASS_$_CSAudioInjectionBuiltInEngine
- _OBJC_METACLASS_$_CSAudioInjectionEngine
- _OBJC_METACLASS_$_CSAudioInjectionHearstEngine
- _OBJC_METACLASS_$_CSAudioInjectionRemoraEngine
- _OBJC_METACLASS_$_CSAudioInjectionTvRemoteEngine
- _OBJC_METACLASS_$_CSAudioTapProvider
- _OBJC_METACLASS_$_CSEndpointerProxy
- _OBJC_METACLASS_$_CSHybridEndpointer
- _OBJC_METACLASS_$_CSNNVADEndpointAnalyzer
- _OBJC_METACLASS_$_CSOtherAppRecordingStateMonitorASMac
- _OBJC_METACLASS_$_NviCSAudioDataSource
- __OBJC_$_CLASS_METHODS_CSNNVADEndpointAnalyzer
- __OBJC_$_CLASS_METHODS_CSOtherAppRecordingStateMonitorASMac
- __OBJC_$_INSTANCE_METHODS_CSAudioInjectionBuiltInEngine
- __OBJC_$_INSTANCE_METHODS_CSAudioInjectionEngine
- __OBJC_$_INSTANCE_METHODS_CSAudioInjectionHearstEngine
- __OBJC_$_INSTANCE_METHODS_CSAudioInjectionRemoraEngine
- __OBJC_$_INSTANCE_METHODS_CSAudioInjectionTvRemoteEngine
- __OBJC_$_INSTANCE_METHODS_CSAudioTapProvider
- __OBJC_$_INSTANCE_METHODS_CSEndpointerProxy
- __OBJC_$_INSTANCE_METHODS_CSHybridEndpointer
- __OBJC_$_INSTANCE_METHODS_CSNNVADEndpointAnalyzer
- __OBJC_$_INSTANCE_METHODS_CSOtherAppRecordingStateMonitorASMac
- __OBJC_$_INSTANCE_METHODS_NviCSAudioDataSource
- __OBJC_$_INSTANCE_VARIABLES_CSAudioInjectionBuiltInEngine
- __OBJC_$_INSTANCE_VARIABLES_CSAudioInjectionEngine
- __OBJC_$_INSTANCE_VARIABLES_CSAudioInjectionHearstEngine
- __OBJC_$_INSTANCE_VARIABLES_CSAudioInjectionRemoraEngine
- __OBJC_$_INSTANCE_VARIABLES_CSAudioInjectionTvRemoteEngine
- __OBJC_$_INSTANCE_VARIABLES_CSAudioTapProvider
- __OBJC_$_INSTANCE_VARIABLES_CSEndpointerProxy
- __OBJC_$_INSTANCE_VARIABLES_CSHybridEndpointer
- __OBJC_$_INSTANCE_VARIABLES_CSNNVADEndpointAnalyzer
- __OBJC_$_INSTANCE_VARIABLES_NviCSAudioDataSource
- __OBJC_$_PROP_LIST_CSAudioInjectionBuiltInEngine
- __OBJC_$_PROP_LIST_CSAudioInjectionEngine
- __OBJC_$_PROP_LIST_CSAudioInjectionHearstEngine
- __OBJC_$_PROP_LIST_CSAudioInjectionRemoraEngine
- __OBJC_$_PROP_LIST_CSAudioInjectionTvRemoteEngine
- __OBJC_$_PROP_LIST_CSAudioTapProvider
- __OBJC_$_PROP_LIST_CSEndpointAnalyzerImpl
- __OBJC_$_PROP_LIST_CSEndpointerProxy
- __OBJC_$_PROP_LIST_CSHybridEndpointer
- __OBJC_$_PROP_LIST_CSNNVADEndpointAnalyzer
- __OBJC_$_PROP_LIST_NviAudioDataSource
- __OBJC_$_PROP_LIST_NviCSAudioDataSource
- __OBJC_$_PROP_LIST_NviDataSource
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzerImpl
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzerImplDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NviAudioDataSource
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NviDataSource
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzer
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzerDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzerImpl
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzerImplDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzerImpl
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzerImplDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_NviAudioDataSource
- __OBJC_$_PROTOCOL_METHOD_TYPES_NviDataSource
- __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzerImpl
- __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzerImplDelegate
- __OBJC_$_PROTOCOL_REFS_NviAudioDataSource
- __OBJC_$_PROTOCOL_REFS_NviDataSource
- __OBJC_CLASS_PROTOCOLS_$_CSAudioInjectionBuiltInEngine
- __OBJC_CLASS_PROTOCOLS_$_CSAudioInjectionHearstEngine
- __OBJC_CLASS_PROTOCOLS_$_CSAudioInjectionRemoraEngine
- __OBJC_CLASS_PROTOCOLS_$_CSAudioInjectionTvRemoteEngine
- __OBJC_CLASS_PROTOCOLS_$_CSAudioTapProvider
- __OBJC_CLASS_PROTOCOLS_$_CSEndpointerProxy
- __OBJC_CLASS_PROTOCOLS_$_CSHybridEndpointer
- __OBJC_CLASS_PROTOCOLS_$_CSNNVADEndpointAnalyzer
- __OBJC_CLASS_PROTOCOLS_$_NviCSAudioDataSource
- __OBJC_CLASS_RO_$_CSAudioInjectionBuiltInEngine
- __OBJC_CLASS_RO_$_CSAudioInjectionEngine
- __OBJC_CLASS_RO_$_CSAudioInjectionHearstEngine
- __OBJC_CLASS_RO_$_CSAudioInjectionRemoraEngine
- __OBJC_CLASS_RO_$_CSAudioInjectionTvRemoteEngine
- __OBJC_CLASS_RO_$_CSAudioTapProvider
- __OBJC_CLASS_RO_$_CSEndpointerProxy
- __OBJC_CLASS_RO_$_CSHybridEndpointer
- __OBJC_CLASS_RO_$_CSNNVADEndpointAnalyzer
- __OBJC_CLASS_RO_$_CSOtherAppRecordingStateMonitorASMac
- __OBJC_CLASS_RO_$_NviCSAudioDataSource
- __OBJC_LABEL_PROTOCOL_$_CSEndpointAnalyzerImpl
- __OBJC_LABEL_PROTOCOL_$_CSEndpointAnalyzerImplDelegate
- __OBJC_LABEL_PROTOCOL_$_NviAudioDataSource
- __OBJC_LABEL_PROTOCOL_$_NviDataSource
- __OBJC_METACLASS_RO_$_CSAudioInjectionBuiltInEngine
- __OBJC_METACLASS_RO_$_CSAudioInjectionEngine
- __OBJC_METACLASS_RO_$_CSAudioInjectionHearstEngine
- __OBJC_METACLASS_RO_$_CSAudioInjectionRemoraEngine
- __OBJC_METACLASS_RO_$_CSAudioInjectionTvRemoteEngine
- __OBJC_METACLASS_RO_$_CSAudioTapProvider
- __OBJC_METACLASS_RO_$_CSEndpointerProxy
- __OBJC_METACLASS_RO_$_CSHybridEndpointer
- __OBJC_METACLASS_RO_$_CSNNVADEndpointAnalyzer
- __OBJC_METACLASS_RO_$_CSOtherAppRecordingStateMonitorASMac
- __OBJC_METACLASS_RO_$_NviCSAudioDataSource
- __OBJC_PROTOCOL_$_CSEndpointAnalyzerImpl
- __OBJC_PROTOCOL_$_CSEndpointAnalyzerImplDelegate
- __OBJC_PROTOCOL_$_NviAudioDataSource
- __OBJC_PROTOCOL_$_NviDataSource
- __ZL17handleInputBufferPvP16OpaqueAudioQueueP16AudioQueueBufferPK14AudioTimeStampjPK28AudioStreamPacketDescription
- __ZL21isAudioQueueRecordingP16OpaqueAudioQueuePU15__autoreleasingP7NSError
- __ZL25isRunningListenerCallbackPvP16OpaqueAudioQueuej
- __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8ne190102IPNS_6vectorINS4_IfNS_9allocatorIfEEEENS5_IS7_EEEESA_SA_EENS_4pairIT_T1_EESC_T0_SD_
- __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8ne190102IPNS_6vectorIfNS_9allocatorIfEEEES8_S8_EENS_4pairIT_T1_EESA_T0_SB_
- __ZNKSt3__114default_deleteIN10corespeech25CSAudioCircularBufferImplIhEEEclB8ne190102EPS3_
- __ZNKSt3__16vectorINS0_INS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEEENS1_IS7_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorINS_4pairIfjEENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt12out_of_rangeC1B8ne190102EPKc
- __ZNSt3__110unique_ptrI15SmartSiriVolumeNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_4pairIfjEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__120__throw_out_of_rangeB8ne190102EPKc
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorINS3_IfNS2_IfEEEENS2_IS5_EEEEEEPS7_EEED2B8ne190102Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIfNS2_IfEEEEEEPS5_EEED2B8ne190102Ev
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne190102INS_9allocatorINS_6vectorINS2_IfNS1_IfEEEENS1_IS4_EEEEEEPS6_S8_S8_EET2_RT_T0_T1_S9_
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne190102INS_9allocatorINS_6vectorIfNS1_IfEEEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
- __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE16__init_with_sizeB8ne190102IPS5_S9_EEvT_T0_m
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__destroy_vectorclB8ne190102Ev
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__init_with_sizeB8ne190102IPS3_S7_EEvT_T0_m
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE18__assign_with_sizeB8ne190102IPS3_S7_EEvT_T0_l
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE7__clearB8ne190102Ev
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEEC2B8ne190102EmRKS3_
- __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne190102Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB8ne190102IPfS5_EEvT_T0_m
- __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB8ne190102IPfS5_EEvT_T0_l
- __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne190102EmRKf
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- ___102-[CSEndpointerXPCClient resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.14
- ___104-[CSHybridEndpointer shouldAcceptEagerResultForDuration:withEndpointerMetrics:resultsCompletionHandler:]_block_invoke
- ___108-[CSHybridEndpointer _generateEndpointerFeaturesWithEffectiveClientProcessedAudioMs:osdFeatures:completion:]_block_invoke
- ___109-[CSEndpointDetectedSelfLogger attSiriNode:didDetectHardEndpointAtTime:withMetrics:usesAutomaticEndPointing:]_block_invoke
- ___110+[CSAudioInjectionServices injectAudio:toDeviceWithUUID:withfadingTimeWindowLength:handlingDaemon:completion:]_block_invoke.12
- ___110-[CSSiriLauncher notifyDarwinVoiceTrigger:deviceId:myriadPHash:myriadLateActivationExpirationTime:completion:]_block_invoke_3
- ___110-[CSSiriSpeechRecorder speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:]_block_invoke.178
- ___115-[CSEndpointDetectedSelfLogger attSiriNode:didDetectEndpointEventAtTime:eventType:withMetrics:useEndpointerSignal:]_block_invoke
- ___119+[CSAudioInjectionServices createAudioInjectionDeviceWithType:deviceName:deviceID:productID:handlingDaemon:completion:]_block_invoke.10
- ___119+[CSAudioInjectionServices createAudioInjectionDeviceWithType:deviceName:deviceID:productID:handlingDaemon:completion:]_block_invoke.9
- ___121+[CSAudioInjectionServices injectAudio:toDeviceWithUUID:withNumChannels:withUserIntentOptions:handlingDaemon:completion:]_block_invoke.13
- ___122-[CSAudioInjectionHearstEngine audioEngineBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:isFileLoadedBuffer:]_block_invoke
- ___122-[CSAudioInjectionHearstEngine audioEngineBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:isFileLoadedBuffer:]_block_invoke_2
- ___122-[CSAudioInjectionRemoraEngine audioEngineBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:isFileLoadedBuffer:]_block_invoke
- ___122-[CSAudioInjectionRemoraEngine audioEngineBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:isFileLoadedBuffer:]_block_invoke_2
- ___123-[CSAudioInjectionBuiltInEngine audioEngineBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:isFileLoadedBuffer:]_block_invoke
- ___127-[CSHybridEndpointer logAnchorMachAbsTime:numSamplesProcessedBeforeAnchorTime:isAnchorTimeBuffered:audioDeliveryHostTimeDelta:]_block_invoke
- ___132-[CSHybridEndpointer updateEnhancedEndpointerDefaultThresholdPartial:defaultThresholdRC:relaxedThresholdPartial:relaxedThresholdRC:]_block_invoke
- ___145-[CSSiriSpeechRecorder _speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:errorCodeOverride:underlyingError:]_block_invoke.182
- ___145-[CSSiriSpeechRecorder _speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:errorCodeOverride:underlyingError:]_block_invoke_2.183
- ___189-[CSHybridEndpointAnalyzer _emitEndpointDetectedEventWithEndpointTimeMs:endpointBufferHostTime:endpointerFeatures:endpointerDecisionLagInNs:extraDelayMs:endpointScore:asrFeaturesLatencies:]_block_invoke
- ___189-[CSHybridEndpointAnalyzer _emitEndpointDetectedEventWithEndpointTimeMs:endpointBufferHostTime:endpointerFeatures:endpointerDecisionLagInNs:extraDelayMs:endpointScore:asrFeaturesLatencies:]_block_invoke_2
- ___26-[CSHybridEndpointer init]_block_invoke
- ___30-[CSAudioInjectionEngine stop]_block_invoke
- ___30-[CSHybridEndpointer setMhId:]_block_invoke
- ___31-[CSAudioInjectionEngine start]_block_invoke
- ___325-[CSSpeechController initWithEndpointId:xpcClientFactory:endpointer:continuousVoiceTrigger:siriVolumeController:mediaPlayingMonitor:alarmMonitor:timerMonitor:audioSessionController:supportPhatic:supportHearstVoiceTrigger:supportTriagleModeSessionActivationRetry:supportSessionActivateDelay:supportsDuckingOnSpeakerEvaluator:]_block_invoke
- ___325-[CSSpeechController initWithEndpointId:xpcClientFactory:endpointer:continuousVoiceTrigger:siriVolumeController:mediaPlayingMonitor:alarmMonitor:timerMonitor:audioSessionController:supportPhatic:supportHearstVoiceTrigger:supportTriagleModeSessionActivationRetry:supportSessionActivateDelay:supportsDuckingOnSpeakerEvaluator:]_block_invoke_2
- ___33-[CSAudioTapProvider isRecording]_block_invoke
- ___36-[CSAudioInjectionHearstEngine stop]_block_invoke
- ___36-[CSAudioInjectionRemoraEngine stop]_block_invoke
- ___36-[NviCSAudioDataSource addReceiver:]_block_invoke
- ___37-[CSAudioInjectionBuiltInEngine stop]_block_invoke
- ___37-[CSAudioInjectionEngine isRecording]_block_invoke
- ___37-[CSAudioInjectionHearstEngine start]_block_invoke
- ___37-[CSAudioInjectionRemoraEngine start]_block_invoke
- ___38-[CSAudioInjectionBuiltInEngine start]_block_invoke
- ___38-[CSAudioInjectionBuiltInEngine start]_block_invoke.20
- ___39-[NviCSAudioDataSource removeReceiver:]_block_invoke
- ___40-[CSEndpointerXPCClient setEndWaitTime:]_block_invoke
- ___40-[CSHybridEndpointer processRCFeatures:]_block_invoke
- ___40-[CSHybridEndpointer processTaskString:]_block_invoke
- ___40-[CSHybridEndpointer processTaskString:]_block_invoke.398
- ___41-[CSAudioInjectionEngine stopAudioStream]_block_invoke
- ___41-[CSHybridEndpointer terminateProcessing]_block_invoke
- ___41-[CSNNVADEndpointAnalyzer stopEndpointer]_block_invoke
- ___41-[CSSmartSiriVolume startSmartSiriVolume]_block_invoke
- ___41-[CSSmartSiriVolume startSmartSiriVolume]_block_invoke.53
- ___41-[CSSmartSiriVolume startSmartSiriVolume]_block_invoke_2
- ___42-[CSAudioInjectionProvider connectDevice:]_block_invoke
- ___42-[CSEndpointerXPCClient setStartWaitTime:]_block_invoke
- ___42-[CSNNVADEndpointAnalyzer setEndWaitTime:]_block_invoke
- ___42-[CSSpeechController _startPhaticDecision]_block_invoke
- ___42-[CSSpeechController _startPhaticDecision]_block_invoke.310
- ___42-[CSSpeechController _startPhaticDecision]_block_invoke.313
- ___42-[CSSpeechController _startPhaticDecision]_block_invoke.314
- ___43-[CSAudioInjectionHearstEngine isRecording]_block_invoke
- ___43-[CSAudioInjectionRemoraEngine isRecording]_block_invoke
- ___43-[CSP2PService _sendVoiceProfile:toPeerId:]_block_invoke.368
- ___43-[CSP2PService _sendVoiceProfile:toPeerId:]_block_invoke.369
- ___43-[CSP2PService _sendVoiceProfile:toPeerId:]_block_invoke.370
- ___44-[CSAudioInjectionBuiltInEngine isRecording]_block_invoke
- ___44-[CSHybridEndpointer endpointerModelVersion]_block_invoke
- ___44-[CSNNVADEndpointAnalyzer setStartWaitTime:]_block_invoke
- ___45-[CSEndpointerXPCClient endPointAnalyzerType]_block_invoke
- ___45-[CSEndpointerXPCClient endPointAnalyzerType]_block_invoke_2
- ___47-[CSAudioInjectionHearstEngine stopAudioStream]_block_invoke
- ___47-[CSAudioInjectionRemoraEngine stopAudioStream]_block_invoke
- ___47-[CSSiriSpeechRecorder playRecordingStartAlert]_block_invoke.152
- ___47-[NviCSAudioDataSource stopWithDidStopHandler:]_block_invoke
- ___47-[NviCSAudioDataSource stopWithDidStopHandler:]_block_invoke_2
- ___48-[CSAudioInjectionBuiltInEngine stopAudioStream]_block_invoke
- ___48-[CSAudioTapProvider destroyRecordingAudioQueue]_block_invoke
- ___48-[CSEndpointerXPCClient _createClientConnection]_block_invoke.58
- ___48-[CSEndpointerXPCClient _createClientConnection]_block_invoke.59
- ___48-[CSEndpointerXPCClient postVoiceTriggerSilence]_block_invoke
- ___48-[CSEndpointerXPCClient postVoiceTriggerSilence]_block_invoke_2
- ___48-[CSHybridEndpointer updateEndpointerThreshold:]_block_invoke
- ___48-[CSSpeechController CSXPCClient:didDisconnect:]_block_invoke.383
- ___49-[CSAssetController _downloadAsset:withComplete:]_block_invoke.324
- ___49-[CSAudioInjectionEngine _startAudioFeedingTimer]_block_invoke
- ___49-[CSHybridEndpointer setEndpointerOperationMode:]_block_invoke
- ___49-[CSP2PService _sendAcousticGradingDataToPeerId:]_block_invoke.375
- ___50-[CSHybridEndpointer _readParametersFromHEPAsset:]_block_invoke
- ___50-[CSHybridEndpointer logFeaturesWithEvent:locale:]_block_invoke
- ___50-[CSHybridEndpointer logFeaturesWithEvent:locale:]_block_invoke_2
- ___50-[CSHybridEndpointer logFeaturesWithEvent:locale:]_block_invoke_3
- ___50-[CSHybridEndpointer logFeaturesWithEvent:locale:]_block_invoke_4
- ___50-[CSSiriSpeechRecorder _playPhaticWithCompletion:]_block_invoke.242
- ___51+[CSSpeechManager sharedManagerForCoreSpeechDaemon]_block_invoke
- ___51-[CSEndpointerXPCClient didDetectStartpointAtTime:]_block_invoke
- ___51-[CSEndpointerXPCClient updateEndpointerThreshold:]_block_invoke
- ___52-[CSHybridEndpointer processASRFeatures:fromServer:]_block_invoke
- ___52-[CSHybridEndpointer processASRFeatures:fromServer:]_block_invoke_2
- ___52-[CSNNVADEndpointAnalyzer request:didProduceResult:]_block_invoke
- ___52-[CSSelfTriggerDetector _startListenWithCompletion:]_block_invoke.22
- ___52-[CSSpeechController setCurrentRecordContext:error:]_block_invoke.247
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.37
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.42
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.47
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.54
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke_2.55
- ___53-[CSAudioInjectionEngine startAudioStreamWithOption:]_block_invoke
- ___53-[CSHybridEndpointAnalyzer _updateAssetWithLanguage:]_block_invoke
- ___53-[CSHybridEndpointer updateEndpointerDelayedTrigger:]_block_invoke
- ___53-[CSNNVADEndpointAnalyzer recordingStoppedForReason:]_block_invoke
- ___54+[CSOtherAppRecordingStateMonitorASMac sharedInstance]_block_invoke
- ___54-[CSAssetController fetchRemoteMetaOfType:allowRetry:]_block_invoke.312
- ___54-[CSSelfTriggerDetector _stopListeningWithCompletion:]_block_invoke.23
- ___54-[CSSpeechController prepareRecordWithSettings:error:]_block_invoke.222
- ___54-[CSSpeechController prepareRecordWithSettings:error:]_block_invoke.231
- ___55-[CSAudioTapProvider saveRecordingBufferFrom:to:toURL:]_block_invoke
- ___55-[CSSpeechController endpointer:detectedTwoShotAtTime:]_block_invoke
- ___55-[CSSpeechController startRecordingWithSettings:error:]_block_invoke.277
- ___55-[CSSpeechController startRecordingWithSettings:error:]_block_invoke.285
- ___55-[CSSpeechController startRecordingWithSettings:error:]_block_invoke_2.286
- ___56-[CSAudioTapProvider _saveRecordingBufferFrom:to:toURL:]_block_invoke
- ___56-[CSAudioTapProvider stopAudioStream:option:completion:]_block_invoke
- ___56-[CSEndpointerXPCClient updateEndpointerDelayedTrigger:]_block_invoke
- ___56-[CSHybridEndpointAnalyzer logFeaturesWithEvent:locale:]_block_invoke
- ___56-[CSHybridEndpointAnalyzer logFeaturesWithEvent:locale:]_block_invoke_2
- ___56-[CSHybridEndpointAnalyzer logFeaturesWithEvent:locale:]_block_invoke_3
- ___56-[CSHybridEndpointAnalyzer logFeaturesWithEvent:locale:]_block_invoke_4
- ___56-[CSSiriSpeechRecorder performBlockAfterAlerts:timeout:]_block_invoke.252
- ___57-[CSAudioTapProvider saveRecordingBufferToEndFrom:toURL:]_block_invoke
- ___57-[CSAudioTapProvider startAudioStream:option:completion:]_block_invoke
- ___57-[CSAudioTapProvider startAudioStream:option:completion:]_block_invoke_2
- ___57-[CSHybridEndpointer fetchCurrentEndpointerOperationMode]_block_invoke
- ___58-[CSHybridEndpointAnalyzer processASRFeatures:fromServer:]_block_invoke_2
- ___59-[CSAudioInjectionHearstEngine alwaysOnVoiceTriggerEnabled]_block_invoke
- ___59-[CSAudioInjectionHearstEngine startAudioStreamWithOption:]_block_invoke
- ___59-[CSAudioInjectionRemoraEngine alwaysOnVoiceTriggerEnabled]_block_invoke
- ___59-[CSAudioInjectionRemoraEngine startAudioStreamWithOption:]_block_invoke
- ___59-[CSHybridEndpointer _processEnhancedEndpointerTaskString:]_block_invoke
- ___59-[CSHybridEndpointer endpointerAssetManagerDidUpdateAsset:]_block_invoke
- ___59-[CSHybridEndpointer handleVoiceTriggerWithActivationInfo:]_block_invoke
- ___60-[CSAudioInjectionBuiltInEngine alwaysOnVoiceTriggerEnabled]_block_invoke
- ___60-[CSAudioInjectionBuiltInEngine startAudioStreamWithOption:]_block_invoke
- ___60-[CSHybridEndpointer _updateEndpointerDelayedTriggerByMhId:]_block_invoke
- ___60-[CSSpeechController handleStopRecordingRequestWithOptions:]_block_invoke.316
- ___60-[NviCSAudioDataSource startWithNviContext:didStartHandler:]_block_invoke
- ___60-[NviCSAudioDataSource startWithNviContext:didStartHandler:]_block_invoke_2
- ___61-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke
- ___61-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.73
- ___61-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.74
- ___61-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.75
- ___61-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.76
- ___61-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.80
- ___61-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.85
- ___61-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke_2
- ___61-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke_2.81
- ___61-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke_3
- ___61-[CSNNVADEndpointAnalyzer processAudioSamplesAsynchronously:]_block_invoke
- ___61-[CSNNVADEndpointAnalyzer processAudioSamplesAsynchronously:]_block_invoke.7
- ___61-[CSSiriSpeechRecorder endpointer:didDetectStartpointAtTime:]_block_invoke
- ___62-[CSAudioTapProvider audioStreamWithRequest:streamName:error:]_block_invoke
- ___62-[CSAudioTapProvider audioStreamWithRequest:streamName:error:]_block_invoke.19
- ___62-[CSHybridEndpointAnalyzer processAudioSamplesAsynchronously:]_block_invoke
- ___62-[CSHybridEndpointAnalyzer processAudioSamplesAsynchronously:]_block_invoke.66
- ___62-[CSHybridEndpointAnalyzer processAudioSamplesAsynchronously:]_block_invoke_2
- ___62-[CSSpeechController _scheduleAudibleFeedbackAtStartRecording]_block_invoke
- ___62-[CSSpeechController _scheduleAudibleFeedbackAtStartRecording]_block_invoke.298
- ___62-[CSSpeechController _scheduleAudibleFeedbackAtStartRecording]_block_invoke.301
- ___63-[CSAudioInjectionHearstEngine setAlwaysOnVoiceTriggerEnabled:]_block_invoke
- ___63-[CSAudioInjectionRemoraEngine setAlwaysOnVoiceTriggerEnabled:]_block_invoke
- ___64-[CSAudioInjectionBuiltInEngine setAlwaysOnVoiceTriggerEnabled:]_block_invoke
- ___64-[CSEndpointerAssetManager _registerForAssetUpdateNotifications]_block_invoke.314
- ___64-[CSNNVADEndpointAnalyzer handleVoiceTriggerWithActivationInfo:]_block_invoke
- ___64-[CSVoiceTriggerSecondPass _syncVoiceProfileEmbeddingsToExclave]_block_invoke.227
- ___65-[CSEndpointerXPCClient didDetectHardEndpointAtTime:withMetrics:]_block_invoke
- ___65-[CSHybridEndpointAnalyzer handleVoiceTriggerWithActivationInfo:]_block_invoke
- ___65-[NviCSAudioDataSource audioStreamProvider:audioBufferAvailable:]_block_invoke
- ___66-[CSEndpointerXPCClient setAutomaticEndpointingSuspensionEndTime:]_block_invoke
- ___67-[CSAudioTapProvider audioStreamWithRequest:streamName:completion:]_block_invoke
- ___67-[CSEndpointerXPCClient resetForVoiceTriggerTwoShotWithSampleRate:]_block_invoke
- ___67-[CSSiriLauncher notifyBuiltInVoiceTrigger:myriadPHash:completion:]_block_invoke_3
- ___68-[CSNNVADEndpointAnalyzer setAutomaticEndpointingSuspensionEndTime:]_block_invoke
- ___68-[CSTrialAssetDownloadMonitor _validateDownloadedAssetForAssetType:]_block_invoke.52
- ___68-[CSTrialAssetDownloadMonitor _validateDownloadedAssetForAssetType:]_block_invoke.53
- ___68-[CSVoiceTriggerSecondPass _processSecondPassInExclave:rejectBlock:]_block_invoke_3
- ___69-[CSAudioTapProvider CSAudioServerCrashMonitorDidReceiveServerCrash:]_block_invoke
- ___69-[CSAudioTapProvider _stopRecordingAudioQueueIfNeededWithCompletion:]_block_invoke
- ___70-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke
- ___70-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.406
- ___70-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.407
- ___70-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.408
- ___70-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.410
- ___70-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.411
- ___70-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.414
- ___70-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.419
- ___70-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.423
- ___70-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke_2
- ___70-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke_2.412
- ___70-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke_3
- ___70-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke_4
- ___70-[CSSiriSpeechRecorder _startAudioPlaybackRequest:options:completion:]_block_invoke.253
- ___73-[CSSiriSpeechRecorder _performTwoShotPromptForType:withOverride:atTime:]_block_invoke.241
- ___75-[CSSiriSpeechRecorder endpointer:didDetectHardEndpointAtTime:withMetrics:]_block_invoke
- ___75-[CSSiriSpeechRecorder endpointer:didDetectHardEndpointAtTime:withMetrics:]_block_invoke.224
- ___76+[CSAudioInjectionServices connectDeviceWithUUID:handlingDaemon:completion:]_block_invoke.15
- ___76+[CSAudioInjectionServices connectDeviceWithUUID:handlingDaemon:completion:]_block_invoke.16
- ___76-[CSSiriLauncher notifyCarPlayVoiceTrigger:deviceId:myriadPHash:completion:]_block_invoke_3
- ___77-[CSSiriSpeechRecorder startSpeechCaptureWithContext:willStartHandler:error:]_block_invoke.109
- ___79+[CSAudioInjectionServices disconnectDeviceWithUUID:handlingDaemon:completion:]_block_invoke.17
- ___79+[CSAudioInjectionServices disconnectDeviceWithUUID:handlingDaemon:completion:]_block_invoke.18
- ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.235
- ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.243
- ___82-[CSHybridEndpointer shouldAcceptEagerResultForDuration:resultsCompletionHandler:]_block_invoke
- ___82-[CSHybridEndpointer shouldAcceptEagerResultForDuration:resultsCompletionHandler:]_block_invoke_2
- ___83-[CSHybridEndpointer shouldAcceptEagerResultForDurationSync:withEndpointerMetrics:]_block_invoke
- ___83-[CSHybridEndpointer shouldAcceptEagerResultForDurationSync:withEndpointerMetrics:]_block_invoke_2
- ___84+[CSAudioInjectionServices primaryInputDeviceUUIDWithhandlingDaemon:WithCompletion:]_block_invoke.19
- ___84+[CSAudioInjectionServices primaryInputDeviceUUIDWithhandlingDaemon:WithCompletion:]_block_invoke.20
- ___84-[CSSiriSpeechRecorder speechControllerLPCMRecordBufferAvailable:buffer:recordedAt:]_block_invoke.198
- ___87-[CSHybridEndpointer processFirstAudioPacketTimestamp:firstAudioSampleSensorTimestamp:]_block_invoke
- ___88-[CSHybridEndpointAnalyzer shouldAcceptEagerResultForDuration:resultsCompletionHandler:]_block_invoke
- ___88-[CSHybridEndpointAnalyzer shouldAcceptEagerResultForDuration:resultsCompletionHandler:]_block_invoke.69
- ___88-[CSHybridEndpointer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke
- ___88-[CSHybridEndpointer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke.467
- ___88-[CSHybridEndpointer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke.470
- ___88-[CSHybridEndpointer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke.473
- ___88-[CSHybridEndpointer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke_2
- ___89-[CSAudioInjectionEngine injectAudio:withScaleFactor:outASBD:playbackStarted:completion:]_block_invoke
- ___89-[CSAudioInjectionEngine injectAudio:withScaleFactor:outASBD:playbackStarted:completion:]_block_invoke.20
- ___89-[CSAudioInjectionEngine injectAudio:withScaleFactor:outASBD:playbackStarted:completion:]_block_invoke_2
- ___93-[CSNNVADEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke
- ___93-[CSVoiceTriggerSecondPass _handleVoiceTriggerFirstPassFromAOP:audioProviderUUID:completion:]_block_invoke.111
- ___94-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke
- ___94-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke.128
- ___94-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke.130
- ___94-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke.131
- ___94-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke_2
- ___97-[CSSiriSpeechRecorder speechControllerDidDetectVoiceTriggerTwoShot:atTime:wantsAudibleFeedback:]_block_invoke.210
- ___97-[CSSiriSpeechRecorder speechControllerDidDetectVoiceTriggerTwoShot:atTime:wantsAudibleFeedback:]_block_invoke_2.211
- ___97-[CSSiriSpeechRecordingContext _donateRecordedAudioForVoiceIdentificationTrainingWithCompletion:]_block_invoke.81
- ___Block_byref_object_copy_.10042
- ___Block_byref_object_copy_.10512
- ___Block_byref_object_copy_.11711
- ___Block_byref_object_copy_.12989
- ___Block_byref_object_copy_.13408
- ___Block_byref_object_copy_.1450
- ___Block_byref_object_copy_.14636
- ___Block_byref_object_copy_.15514
- ___Block_byref_object_copy_.15630
- ___Block_byref_object_copy_.17180
- ___Block_byref_object_copy_.17635
- ___Block_byref_object_copy_.18951
- ___Block_byref_object_copy_.20115
- ___Block_byref_object_copy_.20698
- ___Block_byref_object_copy_.2109
- ___Block_byref_object_copy_.21315
- ___Block_byref_object_copy_.21788
- ___Block_byref_object_copy_.22497
- ___Block_byref_object_copy_.23398
- ___Block_byref_object_copy_.23661
- ___Block_byref_object_copy_.24394
- ___Block_byref_object_copy_.2475
- ___Block_byref_object_copy_.25473
- ___Block_byref_object_copy_.25915
- ___Block_byref_object_copy_.26752
- ___Block_byref_object_copy_.27178
- ___Block_byref_object_copy_.27976
- ___Block_byref_object_copy_.3416
- ___Block_byref_object_copy_.3550
- ___Block_byref_object_copy_.3747
- ___Block_byref_object_copy_.4277
- ___Block_byref_object_copy_.6424
- ___Block_byref_object_copy_.7352
- ___Block_byref_object_copy_.8299
- ___Block_byref_object_copy_.8875
- ___Block_byref_object_dispose_.10043
- ___Block_byref_object_dispose_.10513
- ___Block_byref_object_dispose_.11712
- ___Block_byref_object_dispose_.12990
- ___Block_byref_object_dispose_.13409
- ___Block_byref_object_dispose_.1451
- ___Block_byref_object_dispose_.14637
- ___Block_byref_object_dispose_.15515
- ___Block_byref_object_dispose_.15631
- ___Block_byref_object_dispose_.17181
- ___Block_byref_object_dispose_.17636
- ___Block_byref_object_dispose_.18952
- ___Block_byref_object_dispose_.20116
- ___Block_byref_object_dispose_.20699
- ___Block_byref_object_dispose_.2110
- ___Block_byref_object_dispose_.21316
- ___Block_byref_object_dispose_.21789
- ___Block_byref_object_dispose_.22498
- ___Block_byref_object_dispose_.23399
- ___Block_byref_object_dispose_.23662
- ___Block_byref_object_dispose_.24395
- ___Block_byref_object_dispose_.2476
- ___Block_byref_object_dispose_.25474
- ___Block_byref_object_dispose_.25916
- ___Block_byref_object_dispose_.26753
- ___Block_byref_object_dispose_.27179
- ___Block_byref_object_dispose_.27977
- ___Block_byref_object_dispose_.3417
- ___Block_byref_object_dispose_.3551
- ___Block_byref_object_dispose_.3748
- ___Block_byref_object_dispose_.4278
- ___Block_byref_object_dispose_.6425
- ___Block_byref_object_dispose_.7353
- ___Block_byref_object_dispose_.8300
- ___Block_byref_object_dispose_.8876
- ___CSAttendingStopReasonGetFromName_block_invoke
- ___MobileTimerLibraryCore_block_invoke.804
- ____ZL17handleInputBufferPvP16OpaqueAudioQueueP16AudioQueueBufferPK14AudioTimeStampjPK28AudioStreamPacketDescription_block_invoke
- ____ZL25isRunningListenerCallbackPvP16OpaqueAudioQueuej_block_invoke
- ____ZL25isRunningListenerCallbackPvP16OpaqueAudioQueuej_block_invoke_2
- ____ZL25isRunningListenerCallbackPvP16OpaqueAudioQueuej_block_invoke_3
- ___block_descriptor_104_e8_32r40r48r56r64r72r80r88r96r_e36_v16?0"CSEnhancedEndpointerResult"8lr32l8r40l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8
- ___block_descriptor_40_e8_32s_e25_v24?0"CSAudioChunk"8Q16ls32l8
- ___block_descriptor_40_e8_32s_e35_v16?0"<AFMyriadContextMutating>"8ls32l8
- ___block_descriptor_48_e8_32r40r_e20_v24?0"NSError"8Q16lr32l8r40l8
- ___block_descriptor_48_e8_32r40r_e20_v24?0"NSError"8d16lr32l8r40l8
- ___block_descriptor_48_e8_32s40s_e35_v16?0"<AFMyriadContextMutating>"8ls32l8s40l8
- ___block_descriptor_48_e8_32s_e24_v32?0"MAAsset"8Q16^B24ls32l8
- ___block_descriptor_57_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
- ___block_descriptor_65_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
- ___block_descriptor_68_ea8_32s40bs48bs_e5_v8?0ls40l8s48l8s32l8
- ___block_descriptor_72_ea8_32s40s48s56bs64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.10.10660
- ___block_literal_global.10.19492
- ___block_literal_global.10.20997
- ___block_literal_global.10.22355
- ___block_literal_global.10147
- ___block_literal_global.1024
- ___block_literal_global.10293
- ___block_literal_global.10529
- ___block_literal_global.10686
- ___block_literal_global.10903
- ___block_literal_global.11114
- ___block_literal_global.11568
- ___block_literal_global.11737
- ___block_literal_global.1180
- ___block_literal_global.11998
- ___block_literal_global.12.13958
- ___block_literal_global.12098
- ___block_literal_global.12218
- ___block_literal_global.12512
- ___block_literal_global.12618
- ___block_literal_global.12678
- ___block_literal_global.12733
- ___block_literal_global.1282
- ___block_literal_global.13.20998
- ___block_literal_global.13.21146
- ___block_literal_global.13.22356
- ___block_literal_global.13196
- ___block_literal_global.13312
- ___block_literal_global.13536
- ___block_literal_global.13951
- ___block_literal_global.14.21071
- ___block_literal_global.14297
- ___block_literal_global.14354
- ___block_literal_global.14380
- ___block_literal_global.14398
- ___block_literal_global.14509
- ___block_literal_global.15032
- ___block_literal_global.151
- ___block_literal_global.15117
- ___block_literal_global.15617
- ___block_literal_global.15659
- ___block_literal_global.1578
- ___block_literal_global.16.10275
- ___block_literal_global.16.13197
- ___block_literal_global.16.14355
- ___block_literal_global.16.20999
- ___block_literal_global.16230
- ___block_literal_global.16705
- ___block_literal_global.16714
- ___block_literal_global.16760
- ___block_literal_global.16794
- ___block_literal_global.17.12619
- ___block_literal_global.17.14298
- ___block_literal_global.17.21072
- ___block_literal_global.17054
- ___block_literal_global.17130
- ___block_literal_global.17237
- ___block_literal_global.17904
- ___block_literal_global.18.14479
- ___block_literal_global.18.21147
- ___block_literal_global.18109
- ___block_literal_global.18139
- ___block_literal_global.18699
- ___block_literal_global.18982
- ___block_literal_global.19.21000
- ___block_literal_global.19289
- ___block_literal_global.19370
- ___block_literal_global.19509
- ___block_literal_global.19592
- ___block_literal_global.1960
- ___block_literal_global.19641
- ___block_literal_global.19686
- ___block_literal_global.19702
- ___block_literal_global.19980
- ___block_literal_global.20.13173
- ___block_literal_global.20.14299
- ___block_literal_global.20.21073
- ___block_literal_global.20.25898
- ___block_literal_global.20032
- ___block_literal_global.20137
- ___block_literal_global.20213
- ___block_literal_global.20366
- ___block_literal_global.20682
- ___block_literal_global.209
- ___block_literal_global.20983
- ___block_literal_global.20996
- ___block_literal_global.21.12620
- ___block_literal_global.21070
- ___block_literal_global.21166
- ___block_literal_global.21216
- ___block_literal_global.21259
- ___block_literal_global.2129
- ___block_literal_global.21389
- ___block_literal_global.22.17028
- ___block_literal_global.22.21001
- ___block_literal_global.2207
- ___block_literal_global.22353
- ___block_literal_global.22847
- ___block_literal_global.23.21074
- ___block_literal_global.23019
- ___block_literal_global.2309
- ___block_literal_global.2323
- ___block_literal_global.23430
- ___block_literal_global.237
- ___block_literal_global.23970
- ___block_literal_global.24.12621
- ___block_literal_global.24186
- ___block_literal_global.24271
- ___block_literal_global.24648
- ___block_literal_global.25.21002
- ___block_literal_global.2560
- ___block_literal_global.25605
- ___block_literal_global.25939
- ___block_literal_global.26.25887
- ___block_literal_global.2620
- ___block_literal_global.26270
- ___block_literal_global.26560
- ___block_literal_global.26609
- ___block_literal_global.26788
- ___block_literal_global.26893
- ___block_literal_global.27.12622
- ___block_literal_global.2711
- ___block_literal_global.27123
- ___block_literal_global.27232
- ___block_literal_global.27771
- ___block_literal_global.27987
- ___block_literal_global.28261
- ___block_literal_global.29.21003
- ___block_literal_global.29.21075
- ___block_literal_global.2934
- ___block_literal_global.30.12623
- ___block_literal_global.30.13158
- ___block_literal_global.304
- ___block_literal_global.306
- ___block_literal_global.3126
- ___block_literal_global.323
- ___block_literal_global.3283
- ___block_literal_global.3466
- ___block_literal_global.3541
- ___block_literal_global.36.12624
- ___block_literal_global.3784
- ___block_literal_global.38.9025
- ___block_literal_global.40.20660
- ___block_literal_global.412
- ___block_literal_global.42.12625
- ___block_literal_global.45.12626
- ___block_literal_global.46.9017
- ___block_literal_global.4736
- ___block_literal_global.5.28262
- ___block_literal_global.516
- ___block_literal_global.54.11104
- ___block_literal_global.54.2204
- ___block_literal_global.57
- ___block_literal_global.5753
- ___block_literal_global.5864
- ___block_literal_global.6.26783
- ___block_literal_global.6050
- ___block_literal_global.6152
- ___block_literal_global.6175
- ___block_literal_global.6484
- ___block_literal_global.656
- ___block_literal_global.6620
- ___block_literal_global.681
- ___block_literal_global.6903
- ___block_literal_global.7.22354
- ___block_literal_global.7.813
- ___block_literal_global.7406
- ___block_literal_global.761
- ___block_literal_global.8.1162
- ___block_literal_global.8.26887
- ___block_literal_global.8.27233
- ___block_literal_global.8.28263
- ___block_literal_global.825
- ___block_literal_global.8459
- ___block_literal_global.9059
- ___block_literal_global.9111
- ___block_literal_global.9228
- ___block_literal_global.939
- ___block_literal_global.9636
- __block_invoke.enableHeartbeat.10899
- __block_invoke.enableHeartbeat.27484
- __handleAudioChunk:.heartbeat_CORESPEECH_VOICETRIGGER_FIRSTPASS_LPCM_RECORD_BUFFER_AVAILABLE.18630
- __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.10884
- __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.18621
- __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.27459
- _audit_stringMobileTimer.807
- _kCSDiagnosticReporterEndpointerNNVADFallback
- _kUseDefaultServerFeaturesOnClientLag_block_invoke.heartbeat_CORESPEECH_HYBRID_ENDPOINTER_PROCESS_AUDIO_ASYNC_BEGIN
- _kUseDefaultServerFeaturesOnClientLag_block_invoke.heartbeat_CORESPEECH_HYBRID_ENDPOINTER_PROCESS_AUDIO_ASYNC_END
- _kUseDefaultServerFeaturesOnClientLag_block_invoke_2.heartbeat_CORESPEECH_HYBRID_CLASSIFIER_PROCESS_END
- _kUseDefaultServerFeaturesOnClientLag_block_invoke_2.heartbeat_CORESPEECH_PROCESS_SIL_SCORE_ESTIMATE_BEGIN
- _objc_msgSend$_alertBehaviorForRecordRoute:playbackRoute:speechEvent:speechRecordingMode:ringerState:startingAlertBeepOverideID:presentationMode:usePrelistening:isOnPhoneCall:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:suppressStartAlert:activationHostTime:
- _objc_msgSend$_alertDictionaryForRecordRoute:playbackRoute:speechEvent:ringerState:startingAlertBeepOverideID:presentationMode:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:activationHostTime:
- _objc_msgSend$_audibleFeedbackPlaybackReason
- _objc_msgSend$_calculateBufferSize:audioStreamBasicDescription:frameSizeInSec:
- _objc_msgSend$_cancelExtendedEndpointTimer
- _objc_msgSend$_checkSNObservationForEndpoint:
- _objc_msgSend$_checkSNObservationForStartpoint:
- _objc_msgSend$_connectPluginDevice:
- _objc_msgSend$_createAudioStreamWithCurrentNviContext
- _objc_msgSend$_decodeFeaturesAtEndpoint:endpointerModelType:
- _objc_msgSend$_deliverHardEndpointDetectedAtTime:withMetrics:
- _objc_msgSend$_destroyRecordingAudioQueue
- _objc_msgSend$_effectiveAudioTimeInSecsForSNObservation:
- _objc_msgSend$_emitEndpointDetectedEventWithEndpointTime:endpointBufferHostTime:
- _objc_msgSend$_findLatestInstalledAsset:
- _objc_msgSend$_getCSHybridEndpointerConfigForAsset:
- _objc_msgSend$_getOEPVersionFromPath:
- _objc_msgSend$_holdTransactionForStartListening
- _objc_msgSend$_multimodalEndpointerEnabled
- _objc_msgSend$_pcmBufferForAudioChunk:
- _objc_msgSend$_playStopAlertIfNecessaryForReason:endpointMode:error:
- _objc_msgSend$_releaseTransactionForStopListeningIfNeeded
- _objc_msgSend$_reportAudioFirstBufferInfoIfNecessary
- _objc_msgSend$_reportEndpointAtTsInSecs:
- _objc_msgSend$_reportStartpointAtTsInSecs:
- _objc_msgSend$_reportTwoShotAtTsInSecs:
- _objc_msgSend$_saveRecordingBufferFrom:to:toURL:
- _objc_msgSend$_scheduleExtendedEndpointTimer
- _objc_msgSend$_scheduledAudibleFeedbackDelay
- _objc_msgSend$_setEndpointStyle:
- _objc_msgSend$_setupNNVADEndpointer
- _objc_msgSend$_setupRecordingAudioQueueIfNeededWithOption:
- _objc_msgSend$_shouldEnterTwoShotAtAudioTimeInSecs:
- _objc_msgSend$_shouldProvideTwoShotFeedbackWithRecordContext
- _objc_msgSend$_shouldSetupSelfTrigger
- _objc_msgSend$_stopRecordingAudioQueueIfNeededWithCompletion:
- _objc_msgSend$_trailingSilenceDurationAtEndpoint
- _objc_msgSend$_updateAccessibleEndpointerThresholdIfNeed
- _objc_msgSend$activationSystemUptime
- _objc_msgSend$addSamples:numSamples:atHostTime:
- _objc_msgSend$aqStartCompletion
- _objc_msgSend$aqStopCompletion
- _objc_msgSend$attachDevice:
- _objc_msgSend$audioChunkAvailable:numChannels:numSamplesPerChannel:startSampleId:atAbsMachTimestamp:
- _objc_msgSend$audioTapProvider
- _objc_msgSend$canProcessCurrentRequest
- _objc_msgSend$circularBuffer
- _objc_msgSend$currentHEPAsset
- _objc_msgSend$currentOEPAsset
- _objc_msgSend$decisionDelay
- _objc_msgSend$decodeObjectOfClasses:forKey:
- _objc_msgSend$destroyRecordingAudioQueue
- _objc_msgSend$detected
- _objc_msgSend$disableEndpointer
- _objc_msgSend$emitEndpointDetectedEventWithEndpointerMetrics:withEndpointerModelType:withTrpId:withMhID:
- _objc_msgSend$endPointAnalyzerType
- _objc_msgSend$endpointer:didDetectHardEndpointAtTime:withMetrics:
- _objc_msgSend$endpointer:didDetectHardEndpointAtTime:withMetrics:endpointerModelType:
- _objc_msgSend$endpointer:didDetectStartpointAtTime:
- _objc_msgSend$endpointer:reportEndpointBufferHostTime:firstBufferHostTime:
- _objc_msgSend$endpointerProxy
- _objc_msgSend$engineWithDeviceType:streamHandleId:
- _objc_msgSend$fetchCurrentEndpointerOperationMode
- _objc_msgSend$frameLength
- _objc_msgSend$getEndPointAnalyzerTypeWithReply:
- _objc_msgSend$getPostVoiceTriggerSilenceWithReply:
- _objc_msgSend$initForSidekick
- _objc_msgSend$initProcessTapWithFormat:PID:
- _objc_msgSend$initSystemTapWithFormat:
- _objc_msgSend$initWithCommonFormat:sampleRate:channels:interleaved:
- _objc_msgSend$initWithEndpointId:xpcClientFactory:endpointer:continuousVoiceTrigger:siriVolumeController:mediaPlayingMonitor:alarmMonitor:timerMonitor:audioSessionController:supportPhatic:supportHearstVoiceTrigger:supportTriagleModeSessionActivationRetry:supportSessionActivateDelay:supportsDuckingOnSpeakerEvaluator:
- _objc_msgSend$initWithRequestType:
- _objc_msgSend$initWithStreamDescription:
- _objc_msgSend$initWithTapDescription:
- _objc_msgSend$initWithTargetQueue:audioTapProvider:audioSourceType:
- _objc_msgSend$initWithTargetQueue:audioTapProvider:avvcRefChannelAvailable:
- _objc_msgSend$initWithTotalAudioRecorded:endpointBufferHostTime:featuresAtEndpoint:endpointerType:asrFeatureLatencyDistribution:additionalMetrics:trailingSilenceDurationAtEndpoint:requestId:
- _objc_msgSend$initWithTotalAudioRecorded:endpointBufferHostTime:featuresAtEndpoint:endpointerType:asrFeatureLatencyDistribution:additionalMetrics:trailingSilenceDurationAtEndpoint:requestId:osdFeatures:asrFeatures:isRequestTimeOut:assetConfigVersion:blkHepAudioOrigin:vtExtraAudioAtStartInMs:firstAudioSampleSensorTimestamp:isAnchorTimeBuffered:endpointHostTime:audioDeliveryHostTimeDelta:
- _objc_msgSend$isHypotheticalAudioRouteBluetoothFromAudioSessinoId:
- _objc_msgSend$isNNVADFallbackUnexpectedForLanguageCode:
- _objc_msgSend$isWatchRTSTriggered
- _objc_msgSend$lastEndOfVoiceActivityTime
- _objc_msgSend$lastStartOfVoiceActivityTime
- _objc_msgSend$logAnchorMachAbsTime:numSamplesProcessedBeforeAnchorTime:isAnchorTimeBuffered:audioDeliveryHostTimeDelta:
- _objc_msgSend$logHybridEndpointFeaturesWithEvent:locale:
- _objc_msgSend$lpcmMonoNonInterleavedASBD
- _objc_msgSend$postVoiceTriggerSilence
- _objc_msgSend$preheat
- _objc_msgSend$processFirstAudioPacketTimestamp:firstAudioSampleSensorTimestamp:
- _objc_msgSend$processOSDFeatures:withFrameDurationMs:withMHID:
- _objc_msgSend$processRCFeatures:
- _objc_msgSend$processedSampleCount
- _objc_msgSend$receiveOnlyProcessedChannelData
- _objc_msgSend$recordingAudioQueue
- _objc_msgSend$reqStartAudioSampleId
- _objc_msgSend$requestHistoricalAudio
- _objc_msgSend$requestTelephonyDownlinkAudioTap
- _objc_msgSend$requiresHistoricalBuffer
- _objc_msgSend$resetForNewRequestWithSampleRate:recordContext:disableRCSelection:
- _objc_msgSend$resetForVoiceTriggerTwoShotWithSampleRate:
- _objc_msgSend$setAqStartCompletion:
- _objc_msgSend$setAqStopCompletion:
- _objc_msgSend$setAudioProviderImp:
- _objc_msgSend$setAutomaticEndpointingSuspensionEndTime:
- _objc_msgSend$setDelay:
- _objc_msgSend$setEndWaitTime:
- _objc_msgSend$setEndpointStyle:
- _objc_msgSend$setEndpointerDelegate:
- _objc_msgSend$setEndpointerImplDelegate:
- _objc_msgSend$setImplDelegate:
- _objc_msgSend$setInterspeechWaitTime:
- _objc_msgSend$setMinimumDurationForEndpointer:
- _objc_msgSend$setProcessedSampleCount:
- _objc_msgSend$setRecordingAudioQueue:
- _objc_msgSend$setRequestTelephonyDownlinkAudioTap:
- _objc_msgSend$setSaveSamplesSeenInReset:
- _objc_msgSend$setStartWaitTime:
- _objc_msgSend$setWithObjects:
- _objc_msgSend$sharedContollerProxy
- _objc_msgSend$sharedManagerForCoreSpeechDaemon
- _objc_msgSend$shouldUseVoiceTriggerAnalyzerStyle
- _objc_msgSend$skipSamplesAtStartSuchThatNumSamplesReceivedSoFar:reachesACountOf:completionHandler:
- _objc_msgSend$speechCapturing:didDetectStartpointAtTime:
- _objc_msgSend$speechControllerDidDetectVoiceTriggerTwoShot:atTime:
- _objc_msgSend$speechControllerRequestsOperation:forReason:completion:
- _objc_msgSend$startAudioStreamWithOption:
- _objc_msgSend$startRecordingSampleCount
- _objc_msgSend$startSmartSiriVolume
- _objc_msgSend$stopAudioStream
- _objc_msgSend$supportsSCDAFramework
- _objc_msgSend$updateEndpointerDelayedTrigger:
- _objc_msgSend$updateEndpointerThreshold:
- _objc_msgSend$updateEnhancedEndpointerDefaultThresholdPartial:defaultThresholdRC:relaxedThresholdPartial:relaxedThresholdRC:
- _processAudioSamplesAsynchronously:.heartbeat_CORESPEECH_ENDPOINTER_PROXY_PROCESS_AUDIO_ASYNC_BEGIN
- _processAudioSamplesAsynchronously:.heartbeat_CORESPEECH_ENDPOINTER_PROXY_PROCESS_AUDIO_ASYNC_END
- _sharedController.onceToken.11736
- _sharedController.sharedController.11738
- _sharedHandler.onceToken.1023
- _sharedHandler.onceToken.19288
- _sharedHandler.onceToken.26787
- _sharedHandler.sharedHandler.1025
- _sharedHandler.sharedHandler.19290
- _sharedHandler.sharedHandler.26789
- _sharedHandlerDisabledOnDeviceCompilation.onceToken.26782
- _sharedHandlerDisabledOnDeviceCompilation.sharedHandler.26784
- _sharedInstance._sharedInstance.11569
- _sharedInstance._sharedInstance.12734
- _sharedInstance._sharedInstance.14510
- _sharedInstance._sharedInstance.16761
- _sharedInstance._sharedInstance.17055
- _sharedInstance._sharedInstance.17131
- _sharedInstance._sharedInstance.18110
- _sharedInstance._sharedInstance.19642
- _sharedInstance._sharedInstance.19981
- _sharedInstance._sharedInstance.20033
- _sharedInstance._sharedInstance.20214
- _sharedInstance._sharedInstance.23971
- _sharedInstance._sharedInstance.24649
- _sharedInstance._sharedInstance.2561
- _sharedInstance._sharedInstance.2621
- _sharedInstance._sharedInstance.26610
- _sharedInstance._sharedInstance.27988
- _sharedInstance._sharedInstance.2935
- _sharedInstance._sharedInstance.5754
- _sharedInstance._sharedInstance.5865
- _sharedInstance._sharedInstance.6153
- _sharedInstance._sharedInstance.657
- _sharedInstance._sharedInstance.6621
- _sharedInstance._sharedInstance.762
- _sharedInstance._sharedInstance.826
- _sharedInstance._sharedInstance.9112
- _sharedInstance.onceToken.10292
- _sharedInstance.onceToken.10528
- _sharedInstance.onceToken.10685
- _sharedInstance.onceToken.11567
- _sharedInstance.onceToken.1179
- _sharedInstance.onceToken.12677
- _sharedInstance.onceToken.12732
- _sharedInstance.onceToken.1281
- _sharedInstance.onceToken.13311
- _sharedInstance.onceToken.14508
- _sharedInstance.onceToken.15031
- _sharedInstance.onceToken.15116
- _sharedInstance.onceToken.15616
- _sharedInstance.onceToken.16759
- _sharedInstance.onceToken.17053
- _sharedInstance.onceToken.17129
- _sharedInstance.onceToken.17236
- _sharedInstance.onceToken.17903
- _sharedInstance.onceToken.18108
- _sharedInstance.onceToken.18138
- _sharedInstance.onceToken.19508
- _sharedInstance.onceToken.19591
- _sharedInstance.onceToken.19640
- _sharedInstance.onceToken.19979
- _sharedInstance.onceToken.20031
- _sharedInstance.onceToken.20212
- _sharedInstance.onceToken.20982
- _sharedInstance.onceToken.21165
- _sharedInstance.onceToken.21258
- _sharedInstance.onceToken.21388
- _sharedInstance.onceToken.22846
- _sharedInstance.onceToken.23018
- _sharedInstance.onceToken.23429
- _sharedInstance.onceToken.23969
- _sharedInstance.onceToken.24270
- _sharedInstance.onceToken.24647
- _sharedInstance.onceToken.2559
- _sharedInstance.onceToken.2619
- _sharedInstance.onceToken.26269
- _sharedInstance.onceToken.26608
- _sharedInstance.onceToken.2710
- _sharedInstance.onceToken.27770
- _sharedInstance.onceToken.27986
- _sharedInstance.onceToken.2933
- _sharedInstance.onceToken.3282
- _sharedInstance.onceToken.4735
- _sharedInstance.onceToken.515
- _sharedInstance.onceToken.5752
- _sharedInstance.onceToken.5863
- _sharedInstance.onceToken.6151
- _sharedInstance.onceToken.655
- _sharedInstance.onceToken.6619
- _sharedInstance.onceToken.760
- _sharedInstance.onceToken.824
- _sharedInstance.onceToken.9110
- _sharedInstance.sSharedInstance.18140
- _sharedInstance.sharedInstance.12679
- _sharedInstance.sharedInstance.13313
- _sharedInstance.sharedInstance.15118
- _sharedInstance.sharedInstance.17905
- _sharedInstance.sharedInstance.19510
- _sharedInstance.sharedInstance.19593
- _sharedInstance.sharedInstance.20984
- _sharedInstance.sharedInstance.21260
- _sharedInstance.sharedInstance.23020
- _sharedInstance.sharedInstance.23431
- _sharedInstance.sharedInstance.27772
- _sharedInstance.sharedInstance.3284
- _sharedInstance.sharedInstance.4737
- _sharedInstance.sharedManager.26271
- _sharedInstance.sharedPolicy.1181
- _sharedInstance.sharedPolicy.21167
- _sharedInstance.sharedPolicy.24272
- _sharedInstance.sharedProvider.22848
- _sharedManager.onceToken.16704
- _sharedManager.onceToken.18981
- _sharedManager.onceToken.6902
- _sharedManager.sharedManager.16706
- _sharedManager.sharedManager.6904
- _sharedManagerForCoreSpeechDaemon.onceToken
- _sharedManagerForCoreSpeechDaemon.sharedManagerInstanceForCorespeechd
- _sharedMonitor.onceToken.20136
- _sharedMonitor.sharedMonitor.20138
- _sharedService.onceToken.15658
- _sharedService.onceToken.25938
- _sharedService.sharedService.25940
CStrings:
+ "%"
+ "%s AirPods are in hijackable state, ignore AOP trigger notification"
+ "%s Asset isn't set or the version is unknown, asset:%@ version:%@"
+ "%s Bundle Injection Device doesn't support setEnableAlwaysOnVoiceTrigger"
+ "%s Bundle Injection Device doesn't support speakAudio"
+ "%s Bundle Path is nil"
+ "%s Bypass audio here because ::                   1> VoiceTrigger enabled = %{public}d;                   2> phrase spotter bypassed = %{public}d;                   3> should ignore due to hearst routed and not in splitter = %{public}d;                   4> has HFP during call = %{public}d;                   5> AVVC recording client # = %{public}lu                   6> is hearst hijackable = %{public}d;                   heartbeat = %{public}lld"
+ "%s CSBundleAudioInjectionEngine is allocated with UUID: %@"
+ "%s CSVoiceTriggerSecondPass[%{public}@]:secondpass SAT reject but overriding decision with PHS threshold reduced setted"
+ "%s Creating Injection Device - Type: %lu, deviceName: %@, deviceId: %@, productId: %@, deviceUID: %@"
+ "%s Creating Injection Device - Type: %lu, deviceName: %@, deviceId: %@, productId: %@, deviceUID: %@, bundlePath: %@"
+ "%s Detected two shot at time: %f"
+ "%s Don't update threshold since an accessible threshold is set"
+ "%s Download for MA is deprecated"
+ "%s Elapsed time to get HEP mobile assets: %{public}f seconds"
+ "%s Elapsed time to get OEP assets: %{public}f seconds"
+ "%s Endpointer didDetectHardEndpointAtTime %f withMetrics %@ eventType %ld, current requestId %@"
+ "%s Endpointer running on assistantd"
+ "%s Endpointer running on corespeechd"
+ "%s Failed to create audioTapProvider!"
+ "%s Failed to instantiate plugin."
+ "%s Failed to load bundle: %@"
+ "%s Found OEP asset for %@ at path: %{public}@ with model version: %{public}@, UAF asset version: %{public}@"
+ "%s Hearst Route Status=%@, splitterState = %{public}lu"
+ "%s Ignoring the connection request given the device is the primaryBuiltInDevice and it has been attached with an injection engine"
+ "%s No asset for CSRemoraEndpointAnalyzer for currentLanguage: %{public}@."
+ "%s Opting into smart routing for hearst speech event"
+ "%s Opting into smart routing for hearst voice activation"
+ "%s Opting into smart routing for stem click activation"
+ "%s Principal class does not conform to CSBundleAudioProviding."
+ "%s Received Hearst event: %@"
+ "%s Receiving audio buffer from SRDS Plugin, numSamples: %lu, heartbeat = %lld"
+ "%s Request to create audio injection device bundlePath : %@, deviceName : %@, deviceId : %@, productId : %@"
+ "%s Request to select bundleDevice UUID : %@"
+ "%s Requested invalid AudioTapProvider type"
+ "%s VoiceOverSiriSounds is set to ON, always play Siri start sound"
+ "%s audio plugin is not getting set properly before calling start"
+ "%s audioEngineDidStartRecord with streamId: %ld"
+ "%s does not match with type : %lu, creating new audioTapProvider"
+ "%s has match with type : %lu"
+ "%s nil down the audio plugin due to audioFormat setting failure with error: %@"
+ "%s observer: %{public}@, endpointAsset: %{public}@, osdAsset: %{public}@"
+ "%s recordRoute = %@, playbackRoute = %@, speechEvent = %lu, speechRecordingMode = %lu, AFDeviceRingerSwitchState = %@, AFSoundID = %@, AFPresentationMode = %lu, usePrelistening = %d, isOnPhoneCall = %d, hasPlayedStartAlert = %d, supportsEchoCancellation = %d, isVoiceOverTouchEnabled = %d, isVibrationEnabled = %d, isVibrationSupported = %d, suppressStartAlert = %d, activationHostTime = %llu, isVoiceOverSiriSoundsEnabled = %d"
+ "%s recordingStoppedForReason: %{public}ld"
+ "%s selectBuiltInInjectionDeviceWithUUID timed-out!!"
+ "%s selecting bundleDevice with deviceUID: %@"
+ "+[CSAudioInjectionServices createAudioInjectionDeviceWithType:bundlePath:deviceName:deviceID:productID:handlingDaemon:completion:]"
+ "+[CSAudioInjectionServices createAudioInjectionDeviceWithType:bundlePath:deviceName:deviceID:productID:handlingDaemon:completion:]_block_invoke"
+ "+[CSAudioInjectionServices createAudioInjectionDeviceWithType:bundlePath:deviceName:deviceID:productID:handlingDaemon:completion:]_block_invoke_2"
+ "+[CSAudioInjectionServices injectAudio:toDeviceWithUUID:withNumChannels:withUserIntentOptions:handlingDaemon:started:]"
+ "+[CSAudioInjectionServices injectAudio:toDeviceWithUUID:withNumChannels:withUserIntentOptions:handlingDaemon:started:]_block_invoke"
+ "+[CSAudioInjectionServices injectAudio:toDeviceWithUUID:withNumChannels:withUserIntentOptions:handlingDaemon:started:]_block_invoke_2"
+ "+[CSAudioInjectionServices selectBuiltInInjectionDeviceWithUUID:handlingDaemon:completion:]"
+ "+[CSAudioInjectionServices selectBuiltInInjectionDeviceWithUUID:handlingDaemon:completion:]_block_invoke"
+ "+[CSAudioInjectionServices selectBuiltInInjectionDeviceWithUUID:handlingDaemon:completion:]_block_invoke_2"
+ "+[CSEndpointDetectedSelfLogger _decodeFeaturesAtEndpoint:eventType:]"
+ "+[CSEndpointDetectedSelfLogger emitEndpointDetectedEventWithEndpointerMetrics:eventType:trpId:mhId:]"
+ "+[CSEndpointerFactory endpointAnalyzer:]"
+ "+[CSSiriAudioActivationInfo _alertBehaviorForRecordRoute:playbackRoute:speechEvent:speechRecordingMode:ringerState:startingAlertBeepOverideID:presentationMode:usePrelistening:isOnPhoneCall:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:suppressStartAlert:activationHostTime:isVoiceOverSiriSoundsEnabled:]"
+ "+[CSSiriAudioActivationInfo _alertDictionaryForRecordRoute:playbackRoute:speechEvent:ringerState:startingAlertBeepOverideID:presentationMode:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:activationHostTime:isVoiceOverSiriSoundsEnabled:]"
+ "-[CSAssetController _findLatestInstalledAsset:assetType:]"
+ "-[CSAssetController fetchRemoteMetaOfType:]"
+ "-[CSAudioInjectionDevice initWithDeviceType:bundlePath:deviceName:deviceID:productID:]"
+ "-[CSAudioInjectionDevice initWithDeviceType:deviceName:deviceID:productID:]"
+ "-[CSAudioInjectionDevice setEnableAlwaysOnVoiceTrigger:]"
+ "-[CSAudioInjectionDevice speakAudio:]"
+ "-[CSAudioInjectionDevice speakAudio:withScaleFactor:outASBD:playbackStarted:completion:]"
+ "-[CSAudioInjectionDevice speakAudio:withScaleFactor:outASBD:playbackStarted:userIntentOptions:completion:]"
+ "-[CSAudioInjectionDevice speakAudio:withScaleFactor:playbackStarted:completion:]"
+ "-[CSAudioInjectionProvider _connectBuiltInDevice:withError:]"
+ "-[CSAudioInjectionProvider audioEngineDidStartRecord:audioStreamHandleId:successfully:error:]_block_invoke"
+ "-[CSAudioInjectionProvider selectBuiltInDevice:withCompletion:]_block_invoke"
+ "-[CSBundleAudioInjectionEngine _compensateChannelDataIfNeeded:receivedNumChannels:]"
+ "-[CSBundleAudioInjectionEngine audioBufferAvailable:]_block_invoke"
+ "-[CSBundleAudioInjectionEngine audioStreamDidStartSuccessfully:error:]"
+ "-[CSBundleAudioInjectionEngine audioStreamDidStopSuccessfully:error:]"
+ "-[CSBundleAudioInjectionEngine initWithStreamHandleId:]"
+ "-[CSBundleAudioInjectionEngine setPluginBundleWithPath:withOutError:]"
+ "-[CSBundleAudioInjectionEngine start]_block_invoke"
+ "-[CSBundleAudioInjectionEngine stopAudioStreamWithOutError:]_block_invoke"
+ "-[CSEndpointAnalyzerBase _shouldAcceptEagerResultForDuration:asrFeatures:lastReportedEndpointTimeMs:osdFeatures:resultsCompletionHandler:]"
+ "-[CSEndpointAnalyzerBase getHybridEndpointerConfigForAsset:]"
+ "-[CSEndpointAnalyzerBase handleVoiceTriggerWithActivationInfo:]_block_invoke"
+ "-[CSEndpointAnalyzerBase logFeaturesWithEvent:locale:]_block_invoke"
+ "-[CSEndpointAnalyzerBase processASRFeatures:fromServer:]"
+ "-[CSEndpointAnalyzerBase processASRFeatures:fromServer:]_block_invoke_2"
+ "-[CSEndpointAnalyzerBase recordingStoppedForReason:]"
+ "-[CSEndpointAnalyzerBase stopEndpointer]"
+ "-[CSEndpointAnalyzerBase terminateProcessing]"
+ "-[CSEndpointDetectedSelfLogger attSiriNode:didDetectEndpointEventAtTime:eventType:withMetrics:usesAutomaticEndpointing:]_block_invoke"
+ "-[CSEndpointDetectedSelfLogger attSiriNode:didDetectHardEndpointAtTime:withMetrics:usesAutomaticEndpointing:]_block_invoke"
+ "-[CSEndpointerXPCClient _deliverHardEndpointDetectedAtTime:withMetrics:eventType:]"
+ "-[CSEndpointerXPCClient didDetectHardEndpointAtTime:withMetrics:eventType:]_block_invoke"
+ "-[CSEndpointerXPCClient shouldAcceptEagerResultForDurationSync:withEndpointerMetrics:]"
+ "-[CSFileAudioInjectionBuiltInEngine audioEngineBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:isFileLoadedBuffer:]_block_invoke"
+ "-[CSFileAudioInjectionBuiltInEngine dealloc]"
+ "-[CSFileAudioInjectionBuiltInEngine getBestSampleCountWithOption:]"
+ "-[CSFileAudioInjectionBuiltInEngine start]_block_invoke"
+ "-[CSFileAudioInjectionBuiltInEngine start]_block_invoke_2"
+ "-[CSFileAudioInjectionEngine _compensateChannelDataIfNeeded:receivedNumChannels:]"
+ "-[CSFileAudioInjectionEngine _createDeInterleaverIfNeeded]"
+ "-[CSFileAudioInjectionEngine _deinterleaveBufferIfNeeded:]"
+ "-[CSFileAudioInjectionEngine _readAudioBufferAndFeed]"
+ "-[CSFileAudioInjectionEngine injectAudio:withScaleFactor:outASBD:playbackStarted:completion:]"
+ "-[CSFileAudioInjectionEngine stopAudioStreamWithOutError:]_block_invoke"
+ "-[CSFileAudioInjectionEngine stop]_block_invoke"
+ "-[CSFileAudioInjectionHearstEngine dealloc]"
+ "-[CSFileAudioInjectionHearstEngine start]_block_invoke"
+ "-[CSFileAudioInjectionRemoraEngine dealloc]"
+ "-[CSFileAudioInjectionRemoraEngine start]_block_invoke"
+ "-[CSHybridEndpointAnalyzer _generateEndpointerFeaturesWithEffectiveClientProcessedAudioMs:osdFeatures:completion:]"
+ "-[CSHybridEndpointAnalyzer _processEnhancedEndpointerTaskString:]"
+ "-[CSHybridEndpointAnalyzer _processEnhancedEndpointerTaskString:]_block_invoke"
+ "-[CSHybridEndpointAnalyzer _swapEnhancedEndpointerModelForTaskString:]"
+ "-[CSHybridEndpointAnalyzer _updateCurrentAsset:]"
+ "-[CSHybridEndpointAnalyzer _updateEndpointerDelayedTrigger:]"
+ "-[CSHybridEndpointAnalyzer _updateEndpointerDelayedTrigger:]_block_invoke"
+ "-[CSHybridEndpointAnalyzer _updateEndpointerThreshold:]"
+ "-[CSHybridEndpointAnalyzer _updateEndpointerThreshold:]_block_invoke"
+ "-[CSHybridEndpointAnalyzer _updateEnhancedEndpointerDefaultThresholdPartial:defaultThresholdRC:relaxedThresholdPartial:relaxedThresholdRC:]"
+ "-[CSHybridEndpointAnalyzer _updateEnhancedEndpointerDefaultThresholdPartial:defaultThresholdRC:relaxedThresholdPartial:relaxedThresholdRC:]_block_invoke"
+ "-[CSHybridEndpointAnalyzer endpointerModelVersion]_block_invoke"
+ "-[CSHybridEndpointAnalyzer fetchCurrentEndpointerOperationMode]_block_invoke"
+ "-[CSHybridEndpointAnalyzer processFirstAudioPacketTimestamp:firstAudioSampleSensorTimestamp:]_block_invoke"
+ "-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]"
+ "-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke"
+ "-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke_2"
+ "-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke_4"
+ "-[CSHybridEndpointAnalyzer processRCFeatures:]_block_invoke"
+ "-[CSHybridEndpointAnalyzer processTaskString:]_block_invoke"
+ "-[CSHybridEndpointAnalyzer processTaskString:]_block_invoke_2"
+ "-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]"
+ "-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke"
+ "-[CSHybridEndpointAnalyzer setEndpointerOperationMode:]"
+ "-[CSHybridEndpointAnalyzer setEndpointerOperationMode:]_block_invoke"
+ "-[CSRemoraEndpointAnalyzer CSAssetManagerDidDownloadNewAsset:]"
+ "-[CSRemoraEndpointAnalyzer CSLanguageCodeUpdateMonitor:didReceiveLanguageCodeChanged:]"
+ "-[CSRemoraEndpointAnalyzer _emitEndpointDetectedEventWithEndpointTimeMs:endpointBufferHostTime:endpointerFeatures:endpointerDecisionLagInNs:extraDelayMs:endpointScore:asrFeaturesLatencies:]"
+ "-[CSRemoraEndpointAnalyzer _loadAndSetupEndpointerAssetIfNecessary]"
+ "-[CSRemoraEndpointAnalyzer _readParametersFromHEPAsset:]_block_invoke"
+ "-[CSRemoraEndpointAnalyzer _updateAssetWithLanguage:]_block_invoke"
+ "-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]"
+ "-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke"
+ "-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke_2"
+ "-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke_3"
+ "-[CSRemoraEndpointAnalyzer processAudioSamplesAsynchronously:]"
+ "-[CSRemoraEndpointAnalyzer processAudioSamplesAsynchronously:]_block_invoke"
+ "-[CSRemoraEndpointAnalyzer processAudioSamplesAsynchronously:]_block_invoke_2"
+ "-[CSRemoraEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]"
+ "-[CSRemoraEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke"
+ "-[CSSelfTriggerDetector initWithTargetQueue:audioProviderSelecting:audioSourceType:]"
+ "-[CSSiriLauncher notifyBuiltInVoiceTrigger:myriadPHash:completion:]_block_invoke_2"
+ "-[CSSiriLauncher notifyCarPlayVoiceTrigger:deviceId:myriadPHash:completion:]_block_invoke_2"
+ "-[CSSiriLauncher notifyDarwinVoiceTrigger:deviceId:myriadPHash:myriadLateActivationExpirationTime:completion:]_block_invoke_2"
+ "-[CSSiriSpeechRecorder _playStopAlertIfNecessaryForReason:error:]"
+ "-[CSSiriSpeechRecorder endpointer:detectedTwoShotAtTime:]"
+ "-[CSSiriSpeechRecorder endpointer:didDetectHardEndpointAtTime:withMetrics:eventType:]"
+ "-[CSSiriSpeechRecorder endpointer:didDetectHardEndpointAtTime:withMetrics:eventType:]_block_invoke"
+ "-[CSSmartSiriVolume startSmartSiriVolumeWithAudioProviderSelector:]_block_invoke"
+ "-[CSSpeechController _considerSmartRoutingForAudioRecordContext:]"
+ "-[CSSpeechController detectedTwoShotAtTime:]_block_invoke"
+ "-[CSSpeechManager audioTapProviderWithType:]"
+ "-[CSSpeechManager audioTapProviderWithType:]_block_invoke"
+ "-[CSVoiceTriggerSecondPass _processSecondPassInExclave:rejectBlock:]_block_invoke_3"
+ "-[CSXPCClient attachTandemStream:withConfig:toPrimaryStream:completion:]"
+ "1"
+ "3!$"
+ "@\"<CSAudioInjectionEngineProtocol>\""
+ "@\"<CSAudioProviderSelecting>\""
+ "@\"<CSBundleAudioDelegate>\"16@0:8"
+ "@\"<CSBundleAudioProviding>\""
+ "@\"<CSOtherAppRecordingStateMonitorProviding>\""
+ "@\"CSAudioTapProvider\"24@0:8Q16"
+ "@\"CSEndpointerMetrics\"16@0:8"
+ "@\"CSFileAudioInjectionEngine\""
+ "@116@0:8@16@24q32q40q48q56q64B72B76B80B84B88B92B96B100Q104B112"
+ "@160@0:8d16Q24@32q40@48@56d64@72@80@88B96@100d108d116Q124B132Q136Q144f152f156"
+ "@56@0:8q16@24@32@40@48"
+ "@96@0:8@16@24q32q40q48q56B64B68B72B76B80Q84B92"
+ "B32@0:8@\"CSAudioInjectionDevice\"16^@24"
+ "B32@0:8@\"CSAudioStartStreamOption\"16^@24"
+ "B32@0:8q16Q24"
+ "B72@0:8Q16{AudioStreamBasicDescription=dIIIIIIII}24^@64"
+ "BuiltInMic_injectionDevice"
+ "CSASRFeatures:::acousticEndpointerScore"
+ "CSASRFeatures:::eosLikelihood"
+ "CSASRFeatures:::pauseCounts"
+ "CSASRFeatures:::processedAudioDurationInMilliseconds"
+ "CSASRFeatures:::silencePosterior"
+ "CSASRFeatures:::taskName"
+ "CSASRFeatures:::trailingSilenceDuration"
+ "CSASRFeatures:::wordCount"
+ "CSAudioInjectionEngineProtocol"
+ "CSBundleAudioDelegate"
+ "CSBundleAudioInjectionEngine"
+ "CSBundleAudioProviding"
+ "CSEagerResultAnalyzer"
+ "CSEndpointAnalyzerBase"
+ "CSEndpointMetrics:::asrFeaturesAtEndpoint"
+ "CSEndpointMetrics:::assetConfigVersion"
+ "CSEndpointMetrics:::audioDeliveryHostTimeDelta"
+ "CSEndpointMetrics:::blkHepAudioOrigin"
+ "CSEndpointMetrics:::endpointHostTime"
+ "CSEndpointMetrics:::endpointerScore"
+ "CSEndpointMetrics:::endpointerThreshold"
+ "CSEndpointMetrics:::firstAudioSampleSensorTimestamp"
+ "CSEndpointMetrics:::isAnchorTimeBuffered"
+ "CSEndpointMetrics:::isRequestTimeOut"
+ "CSEndpointMetrics:::osdFeaturesAtEndpoint"
+ "CSEndpointMetrics:::vtExtraAudioAtStartInMs"
+ "CSEndpointerXPCClient should not have the activeChannel getter called"
+ "CSEndpointerXPCClient should not have the endpointerModelVersion setter called"
+ "CSEndpointerXPCClient.m"
+ "CSFileAudioInjectionBuiltInEngine"
+ "CSFileAudioInjectionEngine"
+ "CSFileAudioInjectionHearstEngine"
+ "CSFileAudioInjectionRemoraEngine"
+ "CSFileAudioInjectionTvRemoteEngine"
+ "CSHybridEndpointAnalyzer should not receive audio samples"
+ "CSRemoraEndpointAnalyzer"
+ "Ignoring processAudioSamplesAsynchronously"
+ "Ignoring processAudioSamplesAsynchronously: Not queueing"
+ "Ignoring silenceScoreEstimateAvailable"
+ "Ignoring silenceScoreEstimateAvailable, Not queuing"
+ "KeyLog - %s EEP Features: [%{public}ld, %{public}.2f, %{public}f, %{public}ld, %{public}.2f, %{public}f, %{public}ld, %{public}f, %{public}ld, %{public}.2f, %{public}f, %{public}f, %{public}f] @ %{public}.0f, Scores: [%{public}f, %{public}f], Results: [%{public}d, %{public}d, %{public}d, %{public}f]"
+ "KeyLog - %s HEP.feats: [%{public}ld,%{public}f,%{public}f,%{public}ld,%{public}f,%{public}f] & [(%{public}@),%{public}f] @ %{public}lu [%{public}f, %{public}d]"
+ "KeyLog - %s No asset for CSHybridEndpointer for currentLanguage: %{public}@."
+ "RouteChangedToBeIneligible"
+ "SSRSpeakerProfilesBasePath"
+ "SiriDismissed"
+ "SiriPrompted"
+ "T@\"<CSAudioInjectionEngineProtocol>\",W,N,V_injectionEngine"
+ "T@\"<CSAudioProviderSelecting>\",&,N,V_audioProviderSelecting"
+ "T@\"<CSAudioProviderSelecting>\",&,N,V_audioProviderSelector"
+ "T@\"<CSBundleAudioDelegate>\",W,N"
+ "T@\"<CSBundleAudioProviding>\",&,N,V_audioPlugin"
+ "T@\"<CSEndpointAnalyzer>\",&,N,V_endpointAnalyzer"
+ "T@\"<CSOtherAppRecordingStateMonitorProviding>\",&,N,V_otherAppRecordingStateMonitor"
+ "T@\"CSAudioInjectionDevice\",&,N,V_primaryBuiltInDevice"
+ "T@\"CSAudioInjectionDevice\",&,N,V_primaryTvRemoteDevice"
+ "T@\"CSFileAudioInjectionEngine\",&,N,V_audioInjectionEngine"
+ "T@\"NSMutableDictionary\",&,N,V_audioTapProviders"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_targetQueue"
+ "T@\"NSString\",&,N"
+ "T@\"NSString\",&,N,V_bundlePath"
+ "T@\"NSUUID\",&,N,V_selectedBuiltInBundleDeviceUID"
+ "T@?,C,N,V_startInjectBlock"
+ "TB,N,V_isAudioServerAvailable"
+ "TQ,N,V_tapProviderType"
+ "Tf,N,V_currentEndpointerThreshold"
+ "Tf,N,V_endpointerScore"
+ "Tf,N,V_endpointerThreshold"
+ "Tq,N,V_cachedEventType"
+ "[asrFeatureLatencyDistribution = %@]"
+ "[asrFeatures = %@]"
+ "[assetConfigVersion = %@]"
+ "[audioDeliveryHostTimeDelta = %llu]"
+ "[blkHepAudioOrigin = %f]"
+ "[endpointHostTime = %llu]"
+ "[endpointerScore = %f]"
+ "[endpointerThreshold = %f]"
+ "[firstAudioSampleSensorTimestamp = %llu]"
+ "[isAnchorTimeBuffered = %d]"
+ "[isRequestTimeOut = %d]"
+ "[osdFeatures = %@]"
+ "[vtExtraAudioAtStartInMs = %f]"
+ "_alertBehaviorForRecordRoute:playbackRoute:speechEvent:speechRecordingMode:ringerState:startingAlertBeepOverideID:presentationMode:usePrelistening:isOnPhoneCall:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:suppressStartAlert:activationHostTime:isVoiceOverSiriSoundsEnabled:"
+ "_alertDictionaryForRecordRoute:playbackRoute:speechEvent:ringerState:startingAlertBeepOverideID:presentationMode:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:activationHostTime:isVoiceOverSiriSoundsEnabled:"
+ "_audioPlugin"
+ "_audioProviderSelecting"
+ "_audioProviderSelector"
+ "_audioTapProviders"
+ "_bundlePath"
+ "_cachedEventType"
+ "_connectBuiltInDevice:withError:"
+ "_connectPluginDevice:withError:"
+ "_considerSmartRoutingForAudioRecordContext:"
+ "_currentEndpointerThreshold"
+ "_decodeFeaturesAtEndpoint:eventType:"
+ "_deliverHardEndpointDetectedAtTime:withMetrics:eventType:"
+ "_endpointerScore"
+ "_endpointerThreshold"
+ "_findLatestInstalledAsset:assetType:"
+ "_isAudioServerAvailable"
+ "_isJarvisVoiceTriggerSpeechEvent:"
+ "_isNeededForOTA:"
+ "_notInstalledAssetState:assetType:"
+ "_playStopAlertIfNecessaryForReason:error:"
+ "_primaryBuiltInDevice"
+ "_primaryTvRemoteDevice"
+ "_selectedBuiltInBundleDeviceUID"
+ "_startInjectBlock"
+ "_tapProviderType"
+ "_tearDownBuiltInVoiceTrigger"
+ "_updateAccessibleEndpointerThresholdIfNeeded"
+ "_updateEndpointerDelayedTrigger:"
+ "_updateEndpointerThreshold:"
+ "_updateEnhancedEndpointerDefaultThresholdPartial:defaultThresholdRC:relaxedThresholdPartial:relaxedThresholdRC:"
+ "assetForAssetType:resourcePath:configVersion:assetProvider:assetVariant:identity:assistantLanguageCode:uafAssetVersion:"
+ "assetVersionForConfig:"
+ "attSiriNode:didDetectEndpointEventAtTime:eventType:withMetrics:usesAutomaticEndpointing:"
+ "attSiriNode:didDetectHardEndpointAtTime:withMetrics:usesAutomaticEndpointing:"
+ "attachDevice:withOutError:"
+ "attachTandemStream:withConfig:toPrimaryStream:completion:"
+ "audioBufferAvailable:"
+ "audioPlugin"
+ "audioProviderSelecting"
+ "audioProviderSelector"
+ "audioStreamDidStartSuccessfully:error:"
+ "audioStreamDidStopSuccessfully:error:"
+ "audioTapProviderWithType:"
+ "audioTapProviders"
+ "bundlePath"
+ "bundleWithPath:"
+ "cachedEventType"
+ "connectDevice:withOutError:"
+ "createAudioInjectionDeviceWithType:bundlePath:deviceName:deviceID:productID:completion:"
+ "createAudioInjectionDeviceWithType:bundlePath:deviceName:deviceID:productID:handlingDaemon:completion:"
+ "currentEndpointerThreshold"
+ "decodeArrayOfObjectsOfClass:forKey:"
+ "decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:"
+ "decodeDoubleForKey:"
+ "detectedTwoShotAtTime:"
+ "didDetectHardEndpointAtTime:withMetrics:eventType:"
+ "emitEndpointDetectedEventWithEndpointerMetrics:eventType:trpId:mhId:"
+ "encodeDouble:forKey:"
+ "endpointAnalyzer:"
+ "endpointer:didDetectHardEndpointAtTime:withMetrics:eventType:"
+ "endpointerScore"
+ "endpointerThreshold"
+ "engineWithDevice:streamHandleId:"
+ "getHybridEndpointerConfigForAsset:"
+ "getSerialQueueWithName:targetQueue:"
+ "initWithDeviceType:bundlePath:deviceName:deviceID:productID:"
+ "initWithEndpointId:xpcClientFactory:endpointAnalyzer:continuousVoiceTrigger:siriVolumeController:mediaPlayingMonitor:alarmMonitor:timerMonitor:audioSessionController:supportPhatic:supportHearstVoiceTrigger:supportTriagleModeSessionActivationRetry:supportSessionActivateDelay:supportsDuckingOnSpeakerEvaluator:"
+ "initWithTappingType:"
+ "initWithTargetQueue:audioProviderSelecting:"
+ "initWithTargetQueue:audioProviderSelecting:audioSourceType:"
+ "initWithTotalAudioRecorded:endpointBufferHostTime:featuresAtEndpoint:endpointerType:asrFeatureLatencyDistribution:additionalMetrics:trailingSilenceDurationAtEndpoint:requestId:osdFeatures:asrFeatures:isRequestTimeOut:assetConfigVersion:blkHepAudioOrigin:vtExtraAudioAtStartInMs:firstAudioSampleSensorTimestamp:isAnchorTimeBuffered:endpointHostTime:audioDeliveryHostTimeDelta:endpointerThreshold:endpointerScore:"
+ "injectAudio:toDeviceWithUUID:withNumChannels:withUserIntentOptions:handlingDaemon:started:"
+ "injectAudio:toDeviceWithUUID:withNumChannels:withUserIntentOptions:started:"
+ "injectAudio:toDeviceWithUUID:withScaleFactor:withNumChannels:withUserIntentOptions:started:"
+ "isAudioServerAvailable"
+ "isBundleDevice"
+ "isHearstDoubleTapTriggered"
+ "isHearstHijackable"
+ "isHypotheticalAudioRouteBluetoothAndNotBTSpeakerFromAudioSessinoId:"
+ "load"
+ "modelInfoVersionWithAssetPath:taskHint:"
+ "multimodalEndpointerEnabled"
+ "primaryBuiltInDevice"
+ "primaryTvRemoteDevice"
+ "principalClass"
+ "selectBuiltInDevice:withCompletion:"
+ "selectBuiltInInjectionDeivceWithUUID:completion:"
+ "selectBuiltInInjectionDeviceWithUUID:completion:"
+ "selectBuiltInInjectionDeviceWithUUID:handlingDaemon:completion:"
+ "selectedBuiltInBundleDeviceUID"
+ "setAudioPlugin:"
+ "setAudioProviderSelecting:"
+ "setAudioProviderSelector:"
+ "setAudioTapProviders:"
+ "setBundlePath:"
+ "setCachedEventType:"
+ "setCurrentEndpointerThreshold:"
+ "setIsAudioServerAvailable:"
+ "setPluginBundleWithPath:withOutError:"
+ "setPrimaryBuiltInDevice:"
+ "setPrimaryTvRemoteDevice:"
+ "setSelectedBuiltInBundleDeviceUID:"
+ "setStartInjectBlock:"
+ "setTapProviderType:"
+ "setupAudioFormatWithBlockSize:audioFormat:outError:"
+ "shouldPlaySiriSounds"
+ "shouldProvideTwoShotFeedbackWithRecordContext"
+ "shouldSetupSelfTrigger"
+ "startAudioStreamWithOption:withOutError:"
+ "startAudioStreamWithOutError:"
+ "startInjectBlock"
+ "startSmartSiriVolumeWithAudioProviderSelector:"
+ "stopAudioStreamWithOutError:"
+ "supportsHearstSmartRoutingImprovements"
+ "supportsSystemDaemon"
+ "tapProviderType"
+ "targetQueue"
+ "v24@0:8@\"<CSAudioInjectionEngineDelegate>\"16"
+ "v24@0:8@\"<CSAudioProviderSelecting>\"16"
+ "v24@0:8@\"<CSBundleAudioDelegate>\"16"
+ "v28@0:8B16@\"NSError\"20"
+ "v28@?0B8@\"NSError\"12Q20"
+ "v32@0:8@\"<CSAudioInjectionEngineProtocol>\"16@\"CSAudioChunkForTV\"24"
+ "v40@0:8@\"<CSAudioInjectionEngineProtocol>\"16Q24Q32"
+ "v40@0:8d16@\"CSEndpointerMetrics\"24q32"
+ "v40@0:8d16@24q32"
+ "v44@0:8@\"<CSAudioInjectionEngineProtocol>\"16Q24B32@\"NSError\"36"
+ "v48@0:8@\"CSAudioStream\"16@\"CSTandemAttachConfig\"24@\"CSAudioStream\"32@?<v@?B@\"NSError\">40"
+ "v48@0:8Q16@\"CSAudioRecordContext\"24@\"CSAudioStartStreamOption\"32@\"NSDictionary\"40"
+ "v60@0:8@\"<CSAudioInjectionEngineProtocol>\"16Q24@\"NSData\"32@\"NSData\"40Q48B56"
+ "v64@0:8q16@24@32@40@48@?56"
+ "v68@0:8q16@24@32@40@48i56@?60"
+ "{unique_ptr<SmartSiriVolume, std::default_delete<SmartSiriVolume>>=\"__ptr_\"^{SmartSiriVolume}}"
+ "{unique_ptr<corespeech::CSAudioCircularBufferImpl<unsigned char>, std::default_delete<corespeech::CSAudioCircularBufferImpl<unsigned char>>>=\"__ptr_\"^v}"
+ "{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"__cap_\"^f}"
+ "\xf0\xf0\x81"
- "$"
- "%s %{public}@: Endpointer didDetectDefaultEndpointAtTime:withMetrics: %{public}f, CallingDelegate: %{public}@"
- "%s Accepting RC: RCTime < 0: ASR's processedAudioDuration(%{public}f) > _lastReportedEndpointTimeMs(%{public}f): asrFeatureLatency: %{public}f, rcTimeMs: %{public}f"
- "%s Audible feedback decision postVoiceTriggerSilence: %{public}.3f"
- "%s Audible feedback not needed since we already stopped recording"
- "%s Audio Queue has been disposed"
- "%s AudioQueue listener property %d not match"
- "%s AudioQueueFreeBuffer error: %i"
- "%s Bypass audio here because ::                   1> VoiceTrigger enabled = %{public}d;                   2> phrase spotter bypassed = %{public}d;                   3> should ignore due to hearst routed and not in splitter = %{public}d;                   4> has HFP during call = %{public}d;                   5> AVVC recording client # = %{public}lu                   heartbeat = %{public}lld"
- "%s CSEndpointerProxy: ep-time: %{public}f, triggerEnd: %{public}f, nnvadEndWaitTime: %{public}f, delta: %{public}f, legacyTwoShotThreshold: %{public}f, enterTwoShot: %{public}d"
- "%s CSHybridEndpointAnalyzer recordingStoppedForReason: %{public}ld"
- "%s CSHybridEndpointer can NOT ProcessCurrentRequest, fallback to NNVAD"
- "%s CSHybridEndpointer canProcessCurrentRequest"
- "%s CSHybridEndpointer recordingStoppedForReason: %{public}ld"
- "%s Create circular buffer"
- "%s EP_PROXY::RecordingDidStop: Ignoring didDetectHardEndpointAtTime-reporting"
- "%s EP_PROXY::RecordingDidStop: Ignoring didDetectHardpoint-reporting"
- "%s EP_PROXY::RecordingDidStop: Ignoring startPoint-reporting"
- "%s Endpointer Failed to get endPointAnalyzerType"
- "%s Endpointer Failed to get postVoiceTriggerSilence"
- "%s Endpointer didDetectHardEndpointAtTime %f withMetrics %@, current requestId %@"
- "%s Endpointer is disabled in recordOption: %@"
- "%s Endpointer is not hybrid endpoint, we should rely on CVT for two shot beep"
- "%s Endpointer setStartWaitTime is set to %{public}f"
- "%s Err: %@"
- "%s Error reading AudioQueue property : %d"
- "%s Failed to add isRunning listener!"
- "%s Failed to create ATAudioTap!"
- "%s Failed to create AudioQueue input!"
- "%s Failed to dispose Audio Queue with error: %i"
- "%s Failed to get data format size!"
- "%s Failed to playback audible feedback, error: %{public}@"
- "%s Failed to set Audio Queue Process Tap!"
- "%s Failed to start Audio Queue! %d"
- "%s Failed to stop Audio Queue"
- "%s Found OEP asset for %@ at path: %{public}@"
- "%s HEP::RecordingDidStop: Ignoring processAudioSamplesAsynchronously"
- "%s HEP::RecordingDidStop: Ignoring processAudioSamplesAsynchronously: Not queueing"
- "%s HEP::RecordingDidStop: Ignoring silenceScoreEstimateAvailable"
- "%s HEP::RecordingDidStop: Ignoring silenceScoreEstimateAvailable, Not queuing"
- "%s Hearst Route Status=%ld, splitterState = %{public}lu"
- "%s Ignoring startpoint from stale CSEndpointAnalyzer"
- "%s NewReq: sampleRate: %lu, recordContext: %@"
- "%s No Preheat required"
- "%s No Startpt detected even after %{public}f secs. startWaitTime=%{public}f secs"
- "%s No asset for CSHybridEndpointer for currentLanguage: %{public}@. Fallback to VAD2"
- "%s Not supported in this call flow"
- "%s Notifying scheduled audible feedback playback..."
- "%s Postponing endpt as Endpoint(%{public}f) < _automaticEndpointingSuspensionEndTime(%{public}f)"
- "%s Processing Done. Returning"
- "%s Processing finished. Ignoring"
- "%s Processing finished. Not scheduling"
- "%s Received Hearst event: %{public}ld"
- "%s Received invalid Audio Queue buffer, ignore"
- "%s Received isRunningListenerCallback from Audio Queue"
- "%s Recording Stopped For Reason: %{public}ld"
- "%s Recording queue does not exist, return as stopped successfully"
- "%s Rejecting RC: ASRFeatureLatency < 0: ASR's processedAudioDuration(%{public}f): _lastReportedEndpointTimeMs(%{public}f): asrFeatureLatency: %{public}f, rcTimeMs: %{public}f"
- "%s Reported 2-shot at: %{public}f secs"
- "%s Rx first sample: %{public}ld, _numSamplesReceived=%{public}lu, _vtEndInSampleCount=%{public}lu"
- "%s Scheduled audible feedback decision after %{public}.3fseconds (vtEndMachTime: %{public}llu currentMachTime: %{public}llu)"
- "%s Setting delayed start delay %lf"
- "%s Skip update endpointer threshold from server for accessible endpointer request"
- "%s Start audio stream successfully ? %{public}@, error : %{public}@, startRecordingSampleCount=%lu"
- "%s Start recording invoked too late (%{public}.3f seconds), override scheduledCheckTime: %{public}llu to currentTime: %{public}llu"
- "%s Stopped Audio Queue successfully"
- "%s Stopped audioStream with result=%d, err=%@"
- "%s Stopping current audio queue before destroying"
- "%s Successfully created audio Queue for tapping"
- "%s Two shot audible feedback decision (%{public}.3fs later than the scheduled time), postVoiceTriggerSilence: %{public}.3f"
- "%s Two shot audible feedback decision not needed since we already stopped recording"
- "%s Two shot audible feedback is %{public}@needed. (isMediaPlaying = %{public}d, canPlayPhaticDuringMediaPlayback = %{public}d)"
- "%s Two shot audible feedback is prevented by Myriad decision."
- "%s Two shot audible feedback should notify? [%{public}@]"
- "%s Using Bluetooth audio analyzer style"
- "%s Using default audio analyzer style"
- "%s Using driving audio analyzer style"
- "%s Using voice trigger audio analyzer style"
- "%s WARN: endpointerModelVersion called when CSHybridEndpointer is not available"
- "%s WARN: logEndpointFeatures called when CSHybridEndpointer is not available"
- "%s _activeEndpointer=%{public}@"
- "%s _numSamplesSkippedForVT=%{public}lu, _finishedSkippingSamplesForVT=%{public}d"
- "%s audioProvider == nil, error : %{public}@"
- "%s audiomxd/bridgeaudiod restarted"
- "%s elapsed time to get HEP mobile assets: %{public}lf"
- "%s endpointAsset: %{public}@, osdAsset: %{public}@"
- "%s endpointedBuffer.hostTime=%{public}llu, isAnchorTimeBuffered=%{public}d"
- "%s endpointer running on assistantd"
- "%s endpointer running on corespeechd"
- "%s endpointer: %{public}@: didDetectStartpointAtTime: %{public}f"
- "%s isRecording: %{public}@"
- "%s preheat"
- "%s provider: %{public}@, unexpectedStop: %{public}ld"
- "%s recordRoute = %@, playbackRoute = %@, speechEvent = %lu, speechRecordingMode = %lu, AFDeviceRingerSwitchState = %@, AFSoundID = %@, AFPresentationMode = %lu, usePrelistening = %d, isOnPhoneCall = %d, hasPlayedStartAlert = %d, supportsEchoCancellation = %d, isVoiceOverTouchEnabled = %d, isVibrationEnabled = %d, isVibrationSupported = %d, suppressStartAlert = %d, activationHostTime = %llu"
- "%s recordingAudioQueue is nil!"
- "%s shouldUseCVT2ShotDecision: %{public}d, isWatchRTSTriggered=%{public}d"
- "%s stream: %{public}@, option: %{public}@"
- "%s triggerEndSeconds: %{public}f, _vtEndInSampleCount: %{public}lu, _vtExtraAudioAtStartInMs: %{public}lu,  _hepAudioOriginInMs: %{public}f, twoShotSilenceThresholdInMs: %{public}f, voiceTriggerInfo: %{public}@,"
- "%s triggerEndSeconds: %{public}f, _vtEndInSampleCount: %{public}lu, _vtExtraAudioAtStartInMs: %{public}lu,  _nnvadAudioOriginInMs: %{public}f, _numSamplesSkippedForVT: %{public}lu, _finishedSkippingSamplesForVT: %{public}d, voiceTriggerInfo: %{public}@,"
- "+[CSEndpointDetectedSelfLogger _decodeFeaturesAtEndpoint:endpointerModelType:]"
- "+[CSEndpointDetectedSelfLogger emitEndpointDetectedEventWithEndpointerMetrics:withEndpointerModelType:withTrpId:withMhID:]"
- "+[CSEndpointerAssetManager _getOEPVersionFromPath:]"
- "+[CSEndpointerFactory endpointerProxy]"
- "+[CSSiriAudioActivationInfo _alertBehaviorForRecordRoute:playbackRoute:speechEvent:speechRecordingMode:ringerState:startingAlertBeepOverideID:presentationMode:usePrelistening:isOnPhoneCall:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:suppressStartAlert:activationHostTime:]"
- "+[CSSiriAudioActivationInfo _alertDictionaryForRecordRoute:playbackRoute:speechEvent:ringerState:startingAlertBeepOverideID:presentationMode:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:activationHostTime:]"
- "-[CSAssetController _findLatestInstalledAsset:]"
- "-[CSAudioInjectionBuiltInEngine audioEngineBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:isFileLoadedBuffer:]_block_invoke"
- "-[CSAudioInjectionBuiltInEngine dealloc]"
- "-[CSAudioInjectionBuiltInEngine getBestSampleCountWithOption:]"
- "-[CSAudioInjectionBuiltInEngine start]_block_invoke"
- "-[CSAudioInjectionBuiltInEngine start]_block_invoke_2"
- "-[CSAudioInjectionEngine _compensateChannelDataIfNeeded:receivedNumChannels:]"
- "-[CSAudioInjectionEngine _createDeInterleaverIfNeeded]"
- "-[CSAudioInjectionEngine _deinterleaveBufferIfNeeded:]"
- "-[CSAudioInjectionEngine _readAudioBufferAndFeed]"
- "-[CSAudioInjectionEngine injectAudio:withScaleFactor:outASBD:playbackStarted:completion:]"
- "-[CSAudioInjectionEngine stopAudioStream]_block_invoke"
- "-[CSAudioInjectionEngine stop]_block_invoke"
- "-[CSAudioInjectionHearstEngine dealloc]"
- "-[CSAudioInjectionHearstEngine start]_block_invoke"
- "-[CSAudioInjectionRemoraEngine dealloc]"
- "-[CSAudioInjectionRemoraEngine start]_block_invoke"
- "-[CSAudioTapProvider CSAudioServerCrashMonitorDidReceiveServerCrash:]"
- "-[CSAudioTapProvider CSAudioServerCrashMonitorDidReceiveServerRestart:]"
- "-[CSAudioTapProvider _destroyRecordingAudioQueue]"
- "-[CSAudioTapProvider _saveRecordingBufferFrom:to:toURL:]_block_invoke"
- "-[CSAudioTapProvider _setupRecordingAudioQueueIfNeededWithOption:]"
- "-[CSAudioTapProvider _stopRecordingAudioQueueIfNeededWithCompletion:]"
- "-[CSAudioTapProvider audioStreamWithRequest:streamName:error:]_block_invoke"
- "-[CSAudioTapProvider destroyRecordingAudioQueue]_block_invoke"
- "-[CSAudioTapProvider startAudioStream:option:completion:]_block_invoke"
- "-[CSAudioTapProvider startAudioStream:option:completion:]_block_invoke_2"
- "-[CSAudioTapProvider stopAudioStream:option:completion:]_block_invoke"
- "-[CSEndpointDetectedSelfLogger attSiriNode:didDetectEndpointEventAtTime:eventType:withMetrics:useEndpointerSignal:]_block_invoke"
- "-[CSEndpointDetectedSelfLogger attSiriNode:didDetectHardEndpointAtTime:withMetrics:usesAutomaticEndPointing:]_block_invoke"
- "-[CSEndpointerAssetManager _notifyAssetsUpdate]"
- "-[CSEndpointerProxy cachedEndpointerMetrics]"
- "-[CSEndpointerProxy endpointer:detectedTwoShotAtTime:]"
- "-[CSEndpointerProxy endpointer:didDetectHardEndpointAtTime:withMetrics:]"
- "-[CSEndpointerProxy endpointer:didDetectHardEndpointAtTime:withMetrics:endpointerModelType:]"
- "-[CSEndpointerProxy endpointer:didDetectStartpointAtTime:]"
- "-[CSEndpointerProxy endpointerModelVersion]"
- "-[CSEndpointerProxy logHybridEndpointFeaturesWithEvent:locale:]"
- "-[CSEndpointerProxy preheat]"
- "-[CSEndpointerProxy resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]"
- "-[CSEndpointerProxy resetForVoiceTriggerTwoShotWithSampleRate:]"
- "-[CSEndpointerProxy updateEndpointerThreshold:]"
- "-[CSEndpointerXPCClient _deliverHardEndpointDetectedAtTime:withMetrics:]"
- "-[CSEndpointerXPCClient didDetectHardEndpointAtTime:withMetrics:]_block_invoke"
- "-[CSEndpointerXPCClient endPointAnalyzerType]"
- "-[CSEndpointerXPCClient endPointAnalyzerType]_block_invoke_2"
- "-[CSEndpointerXPCClient postVoiceTriggerSilence]"
- "-[CSEndpointerXPCClient postVoiceTriggerSilence]_block_invoke_2"
- "-[CSHybridEndpointAnalyzer CSAssetManagerDidDownloadNewAsset:]"
- "-[CSHybridEndpointAnalyzer CSLanguageCodeUpdateMonitor:didReceiveLanguageCodeChanged:]"
- "-[CSHybridEndpointAnalyzer _emitEndpointDetectedEventWithEndpointTimeMs:endpointBufferHostTime:endpointerFeatures:endpointerDecisionLagInNs:extraDelayMs:endpointScore:asrFeaturesLatencies:]"
- "-[CSHybridEndpointAnalyzer _getCSHybridEndpointerConfigForAsset:]"
- "-[CSHybridEndpointAnalyzer _loadAndSetupEndpointerAssetIfNecessary]"
- "-[CSHybridEndpointAnalyzer _updateAssetWithLanguage:]_block_invoke"
- "-[CSHybridEndpointAnalyzer handleVoiceTriggerWithActivationInfo:]_block_invoke"
- "-[CSHybridEndpointAnalyzer logFeaturesWithEvent:locale:]_block_invoke"
- "-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]"
- "-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke"
- "-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke_2"
- "-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke_3"
- "-[CSHybridEndpointAnalyzer processASRFeatures:fromServer:]"
- "-[CSHybridEndpointAnalyzer processAudioSamplesAsynchronously:]"
- "-[CSHybridEndpointAnalyzer processAudioSamplesAsynchronously:]_block_invoke"
- "-[CSHybridEndpointAnalyzer processAudioSamplesAsynchronously:]_block_invoke_2"
- "-[CSHybridEndpointAnalyzer recordingStoppedForReason:]"
- "-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]"
- "-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke"
- "-[CSHybridEndpointAnalyzer shouldAcceptEagerResultForDuration:resultsCompletionHandler:]_block_invoke"
- "-[CSHybridEndpointAnalyzer shouldAcceptEagerResultForDuration:resultsCompletionHandler:]_block_invoke_2"
- "-[CSHybridEndpointAnalyzer stopEndpointer]"
- "-[CSHybridEndpointAnalyzer updateEndpointerDelayedTrigger:]"
- "-[CSHybridEndpointAnalyzer updateEndpointerThreshold:]"
- "-[CSHybridEndpointer _generateEndpointerFeaturesWithEffectiveClientProcessedAudioMs:osdFeatures:completion:]"
- "-[CSHybridEndpointer _getCSHybridEndpointerConfigForAsset:]"
- "-[CSHybridEndpointer _processEnhancedEndpointerTaskString:]"
- "-[CSHybridEndpointer _processEnhancedEndpointerTaskString:]_block_invoke"
- "-[CSHybridEndpointer _readParametersFromHEPAsset:]_block_invoke"
- "-[CSHybridEndpointer _shouldAcceptEagerResultForDuration:asrFeatures:lastReportedEndpointTimeMs:osdFeatures:resultsCompletionHandler:]"
- "-[CSHybridEndpointer _swapEnhancedEndpointerModelForTaskString:]"
- "-[CSHybridEndpointer _updateCurrentAsset:]"
- "-[CSHybridEndpointer endpointerModelVersion]_block_invoke"
- "-[CSHybridEndpointer fetchCurrentEndpointerOperationMode]_block_invoke"
- "-[CSHybridEndpointer handleVoiceTriggerWithActivationInfo:]_block_invoke"
- "-[CSHybridEndpointer logFeaturesWithEvent:locale:]_block_invoke"
- "-[CSHybridEndpointer processASRFeatures:fromServer:]"
- "-[CSHybridEndpointer processASRFeatures:fromServer:]_block_invoke_2"
- "-[CSHybridEndpointer processFirstAudioPacketTimestamp:firstAudioSampleSensorTimestamp:]_block_invoke"
- "-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]"
- "-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke"
- "-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke_2"
- "-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke_4"
- "-[CSHybridEndpointer processRCFeatures:]_block_invoke"
- "-[CSHybridEndpointer processTaskString:]_block_invoke"
- "-[CSHybridEndpointer processTaskString:]_block_invoke_2"
- "-[CSHybridEndpointer recordingStoppedForReason:]"
- "-[CSHybridEndpointer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]"
- "-[CSHybridEndpointer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke"
- "-[CSHybridEndpointer setEndpointerOperationMode:]"
- "-[CSHybridEndpointer setEndpointerOperationMode:]_block_invoke"
- "-[CSHybridEndpointer stopEndpointer]"
- "-[CSHybridEndpointer terminateProcessing]"
- "-[CSHybridEndpointer updateEndpointerDelayedTrigger:]"
- "-[CSHybridEndpointer updateEndpointerDelayedTrigger:]_block_invoke"
- "-[CSHybridEndpointer updateEndpointerThreshold:]_block_invoke"
- "-[CSHybridEndpointer updateEnhancedEndpointerDefaultThresholdPartial:defaultThresholdRC:relaxedThresholdPartial:relaxedThresholdRC:]"
- "-[CSHybridEndpointer updateEnhancedEndpointerDefaultThresholdPartial:defaultThresholdRC:relaxedThresholdPartial:relaxedThresholdRC:]_block_invoke"
- "-[CSNNVADEndpointAnalyzer _checkSNObservationForEndpoint:]"
- "-[CSNNVADEndpointAnalyzer _checkSNObservationForStartpoint:]"
- "-[CSNNVADEndpointAnalyzer _emitEndpointDetectedEventWithEndpointTime:endpointBufferHostTime:]"
- "-[CSNNVADEndpointAnalyzer _reportEndpointAtTsInSecs:]"
- "-[CSNNVADEndpointAnalyzer _shouldEnterTwoShotAtAudioTimeInSecs:]"
- "-[CSNNVADEndpointAnalyzer handleVoiceTriggerWithActivationInfo:]_block_invoke"
- "-[CSNNVADEndpointAnalyzer preheat]"
- "-[CSNNVADEndpointAnalyzer processAudioSamplesAsynchronously:]_block_invoke"
- "-[CSNNVADEndpointAnalyzer recordingStoppedForReason:]_block_invoke"
- "-[CSNNVADEndpointAnalyzer request:didFailWithError:]"
- "-[CSNNVADEndpointAnalyzer request:didProduceResult:]"
- "-[CSNNVADEndpointAnalyzer request:didProduceResult:]_block_invoke"
- "-[CSNNVADEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke"
- "-[CSNNVADEndpointAnalyzer stopEndpointer]"
- "-[CSSelfTriggerDetector initWithTargetQueue:audioTapProvider:audioSourceType:]"
- "-[CSSiriLauncher notifyBuiltInVoiceTrigger:myriadPHash:completion:]_block_invoke_3"
- "-[CSSiriLauncher notifyCarPlayVoiceTrigger:deviceId:myriadPHash:completion:]_block_invoke_3"
- "-[CSSiriLauncher notifyDarwinVoiceTrigger:deviceId:myriadPHash:myriadLateActivationExpirationTime:completion:]_block_invoke_3"
- "-[CSSiriSpeechRecorder _playStopAlertIfNecessaryForReason:endpointMode:error:]"
- "-[CSSiriSpeechRecorder _setEndpointStyle:]"
- "-[CSSiriSpeechRecorder endpointer:didDetectHardEndpointAtTime:withMetrics:]"
- "-[CSSiriSpeechRecorder endpointer:didDetectHardEndpointAtTime:withMetrics:]_block_invoke"
- "-[CSSiriSpeechRecorder endpointer:didDetectStartpointAtTime:]"
- "-[CSSiriSpeechRecorder endpointer:didDetectStartpointAtTime:]_block_invoke"
- "-[CSSmartSiriVolume startSmartSiriVolume]_block_invoke"
- "-[CSSpeechController _scheduleAudibleFeedbackAtStartRecording]_block_invoke"
- "-[CSSpeechController _startPhaticDecision]"
- "-[CSSpeechController _startPhaticDecision]_block_invoke"
- "-[CSSpeechController endpointer:detectedTwoShotAtTime:]_block_invoke"
- "-[CSSpeechController stopEndpointer]"
- "-[CSXPCClient attachTandemStream:toPrimaryStream:completion:]"
- "-[NviCSAudioDataSource _createAudioStreamWithCurrentNviContext]"
- "-[NviCSAudioDataSource audioStreamProvider:audioChunkForTVAvailable:]"
- "-[NviCSAudioDataSource audioStreamProvider:avBufferAvailable:]"
- "-[NviCSAudioDataSource audioStreamProvider:didStopStreamUnexpectedly:]"
- "-[NviCSAudioDataSource startWithNviContext:didStartHandler:]_block_invoke_2"
- "-[NviCSAudioDataSource stopWithDidStopHandler:]_block_invoke_2"
- "1q"
- "2"
- "7"
- "@\"<CSAudioFileWriter>\""
- "@\"<CSEndpointAnalyzerImpl>\""
- "@\"<CSEndpointAnalyzerImplDelegate>\""
- "@\"<CSEndpointAnalyzerImplDelegate>\"16@0:8"
- "@\"AVAudioFormat\""
- "@\"CSAudioInjectionEngine\""
- "@\"CSAudioTapProvider\""
- "@\"CSEndpointerProxy\""
- "@\"CSOtherAppRecordingStateMonitor\""
- "@112@0:8@16@24q32q40q48q56q64B72B76B80B84B88B92B96B100Q104"
- "@152@0:8d16Q24@32q40@48@56d64@72@80@88B96@100d108d116Q124B132Q136Q144"
- "@32@0:8q16Q24"
- "@80@0:8d16Q24@32q40@48@56d64@72"
- "@92@0:8@16@24q32q40q48q56B64B68B72B76B80Q84"
- "A"
- "AudioTapProvider"
- "CSAudioInjectionBuiltInEngine"
- "CSAudioInjectionHearstEngine"
- "CSAudioInjectionRemoraEngine"
- "CSAudioInjectionTvRemoteEngine"
- "CSAudioTapProvider"
- "CSAudioTapProvider audioDispatchQueue"
- "CSAudioTapProvider logging"
- "CSEndpointAnalyzerImpl"
- "CSEndpointAnalyzerImplDelegate"
- "CSEndpointerProxy"
- "CSHybridEndpointAnalyzer reset called"
- "CSHybridEndpointer"
- "CSHybridEndpointer reset called"
- "CSHybridEndpointer.m"
- "CSNNVADEndpointAnalyzer"
- "CSNNVADEndpointAnalyzer.m"
- "CSOtherAppRecordingStateMonitorASMac"
- "Caches/VoiceTrigger/SATUpdate"
- "Don't process ASR features"
- "I68@0:8^{OpaqueAudioQueue=}16{AudioStreamBasicDescription=dIIIIIIII}24f64"
- "KeyLog - %s %{public}@: Endpointer didDetectHardEndpointAtTime:withMetrics:endpointerType: %{public}f, CallingDelegate: %{public}@, type %ld"
- "KeyLog - %s No asset for CSHybridEndpointer for currentLanguage: %{public}@. Fallback to NNVAD"
- "NviAudioDataSource"
- "NviCSAudioDataSource"
- "NviDataSource"
- "Reset called?"
- "T@\"<CSAudioFileWriter>\",&,N,V_audioFileWriter"
- "T@\"<CSAudioStreamProviding>\",W,N,V_audioTapProvider"
- "T@\"<CSEndpointAnalyzer>\",R,N"
- "T@\"<CSEndpointAnalyzerDelegate>\",W,N,V_endpointerDelegate"
- "T@\"<CSEndpointAnalyzerImpl>\",&,N,V_hybridEndpointer"
- "T@\"<CSEndpointAnalyzerImpl>\",&,N,V_nnvadEndpointer"
- "T@\"<CSEndpointAnalyzerImpl>\",W,N,V_activeEndpointer"
- "T@\"<CSEndpointAnalyzerImplDelegate>\",W,N"
- "T@\"<CSEndpointAnalyzerImplDelegate>\",W,N,V_endpointerImplDelegate"
- "T@\"<CSEndpointAnalyzerImplDelegate>\",W,N,V_implDelegate"
- "T@\"AVAudioFormat\",&,N,V_currentRequestAudioFormat"
- "T@\"CSAudioInjectionDevice\",&,N,V_builtInDevice"
- "T@\"CSAudioInjectionDevice\",&,N,V_bundleTvRemote"
- "T@\"CSAudioInjectionEngine\",&,N,V_audioInjectionEngine"
- "T@\"CSAudioInjectionEngine\",&,N,V_builtInAudioInjectionEngine"
- "T@\"CSAudioInjectionEngine\",W,N,V_injectionEngine"
- "T@\"CSAudioStream\",W,N,V_audioStream"
- "T@\"CSAudioTapProvider\",&,N,V_audioTapProvider"
- "T@\"CSEndpointerProxy\",&,N,V_endpointerProxy"
- "T@\"CSOSTransaction\",&,N,V_transaction"
- "T@\"CSOtherAppRecordingStateMonitor\",&,N,V_otherAppRecordingStateMonitor"
- "T@\"NSHashTable\",&,N,V_receivers"
- "T@\"NSMutableArray\",&,N,V_asrFeaturesLatencies"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_loggingQueue"
- "T@\"NSString\",&,N,V_UUIDString"
- "T@\"NSString\",?,&,N"
- "T@\"NSString\",?,&,N,V_mhId"
- "T@\"NSString\",?,R,N"
- "T@?,C,N,V_aqStartCompletion"
- "T@?,C,N,V_aqStopCompletion"
- "TB,?,N"
- "TB,?,N,V_saveSamplesSeenInReset"
- "TB,N,V_didEnterTwoshot"
- "TB,N,V_finishedSkippingSamplesForVT"
- "TB,N,V_hasReportedFirstAudioSampleSensorTimestamp"
- "TB,N,V_shouldDetectTwoShot"
- "TQ,N,V_framePosition"
- "TQ,N,V_mode"
- "TQ,N,V_nnvadState"
- "TQ,N,V_numSamplesReceived"
- "TQ,N,V_numSamplesSkippedForVT"
- "TQ,N,V_processedSampleCount"
- "T^{OpaqueAudioQueue=},N,V_recordingAudioQueue"
- "Td,?,N"
- "Td,?,N,V_endWaitTime"
- "Td,?,N,V_interspeechWaitTime"
- "Td,?,R,N"
- "Td,N"
- "Td,N,V_automaticEndpointingSuspensionEndTime"
- "Td,N,V_delay"
- "Td,N,V_minimumDurationForEndpointer"
- "Td,N,V_nnvadAudioOriginInMs"
- "Td,N,V_startWaitTime"
- "Td,N,V_vtEndInSecs"
- "Td,R,N,V_lastEndOfVoiceActivityTime"
- "Td,R,N,V_lastStartOfVoiceActivityTime"
- "Tq,N"
- "Tq,N,V_endpointStyle"
- "Tq,N,V_firstSampleId"
- "V!"
- "[4^{AudioQueueBuffer}]"
- "^{OpaqueAudioQueue=}"
- "^{OpaqueAudioQueue=}16@0:8"
- "_%d_%d_%@"
- "_UUIDString"
- "_activeEndpointer"
- "_alertBehaviorForRecordRoute:playbackRoute:speechEvent:speechRecordingMode:ringerState:startingAlertBeepOverideID:presentationMode:usePrelistening:isOnPhoneCall:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:suppressStartAlert:activationHostTime:"
- "_alertDictionaryForRecordRoute:playbackRoute:speechEvent:ringerState:startingAlertBeepOverideID:presentationMode:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:activationHostTime:"
- "_aqStartCompletion"
- "_aqStopCompletion"
- "_asrFeaturesLatencies"
- "_audioBuffers"
- "_audioTapProvider"
- "_automaticEndpointingSuspensionEndTime"
- "_builtInAudioInjectionEngine"
- "_builtInDevice"
- "_bundleTvRemote"
- "_calculateBufferSize:audioStreamBasicDescription:frameSizeInSec:"
- "_cancelExtendedEndpointTimer"
- "_checkSNObservationForEndpoint:"
- "_checkSNObservationForStartpoint:"
- "_connectPluginDevice:"
- "_createAudioStreamWithCurrentNviContext"
- "_currentRequestAudioFormat"
- "_decodeFeaturesAtEndpoint:endpointerModelType:"
- "_delay"
- "_deliverHardEndpointDetectedAtTime:withMetrics:"
- "_destroyRecordingAudioQueue"
- "_didEnterTwoshot"
- "_effectiveAudioTimeInSecsForSNObservation:"
- "_emitEndpointDetectedEventWithEndpointTime:endpointBufferHostTime:"
- "_endWaitTime"
- "_endpointStyle"
- "_endpointerDelegate"
- "_endpointerImplDelegate"
- "_endpointerProxy"
- "_extendedEndpointTimer"
- "_findLatestInstalledAsset:"
- "_finishedSkippingSamplesForVT"
- "_firstSampleId"
- "_framePosition"
- "_getCSHybridEndpointerConfigForAsset:"
- "_getOEPVersionFromPath:"
- "_hasReportedFirstAudioSampleSensorTimestamp"
- "_holdTransactionForStartListening"
- "_hybridEndpointer"
- "_implDelegate"
- "_interspeechWaitTime"
- "_lastEndOfVoiceActivityTime"
- "_lastStartOfVoiceActivityTime"
- "_loggingQueue"
- "_mapInstrumentationEndpointTypeFromStopRecordingReason:"
- "_minimumDurationForEndpointer"
- "_multimodalEndpointerEnabled"
- "_nnvadAudioOriginInMs"
- "_nnvadEndpointer"
- "_nnvadState"
- "_numSamplesReceived"
- "_numSamplesSkippedForVT"
- "_pcmBufferForAudioChunk:"
- "_playStopAlertIfNecessaryForReason:endpointMode:error:"
- "_receivers"
- "_recordingAudioQueue"
- "_releaseTransactionForStopListeningIfNeeded"
- "_reportAudioFirstBufferInfoIfNecessary"
- "_reportEndpointAtTsInSecs:"
- "_reportStartpointAtTsInSecs:"
- "_reportTwoShotAtTsInSecs:"
- "_saveRecordingBufferFrom:to:toURL:"
- "_saveSamplesSeenInReset"
- "_scheduleAudibleFeedbackAtStartRecording"
- "_scheduleExtendedEndpointTimer"
- "_setEndpointStyle:"
- "_setupNNVADEndpointer"
- "_setupRecordingAudioQueueIfNeededWithOption:"
- "_shouldDetectTwoShot"
- "_shouldEnterTwoShotAtAudioTimeInSecs:"
- "_shouldProvideTwoShotFeedbackWithRecordContext"
- "_shouldSetupSelfTrigger"
- "_startPhaticDecision"
- "_startWaitTime"
- "_stopRecordingAudioQueueIfNeededWithCompletion:"
- "_transaction"
- "_updateAccessibleEndpointerThresholdIfNeed"
- "_vtEndInSecs"
- "a"
- "activeEndpointer"
- "addSamples:numSamples:atHostTime:"
- "aqStartCompletion"
- "aqStopCompletion"
- "asrFeatureLatency"
- "asrFeaturesLatencies"
- "attSiriNode:didDetectEndpointEventAtTime:eventType:withMetrics:useEndpointerSignal:"
- "attSiriNode:didDetectHardEndpointAtTime:withMetrics:usesAutomaticEndPointing:"
- "attSiriNode:didDetectStartpointAtTime:"
- "attSiriNode:registerEndpointerProxy:"
- "attachDevice:"
- "attachTandemStream:toPrimaryStream:completion:"
- "audioFingerprintProvider"
- "audioStreamProvider:avBufferAvailable:"
- "audioTapProvider"
- "automaticEndpointingSuspensionEndTime"
- "ay12!Rd"
- "builtInAudioInjectionEngine"
- "builtInDevice"
- "bundleTvRemote"
- "bypassSamples"
- "com.apple.corespeech.nnvad"
- "com.apple.nvi.csaudiosrc"
- "connectDevice:"
- "currentRequestAudioFormat"
- "decisionDelay"
- "decodeObjectOfClasses:forKey:"
- "delay"
- "destroyRecordingAudioQueue"
- "detected"
- "didDetectHardEndpointAtTime:withMetrics:"
- "didDetectStartpointAtTime:"
- "didEnterTwoshot"
- "disableEndpointer"
- "emitEndpointDetectedEventWithEndpointerMetrics:withEndpointerModelType:withTrpId:withMhID:"
- "endPointAnalyzerType"
- "endWaitTime"
- "endpointStyle"
- "endpointer:didDetectHardEndpointAtTime:withMetrics:"
- "endpointer:didDetectHardEndpointAtTime:withMetrics:endpointerModelType:"
- "endpointer:didDetectStartpointAtTime:"
- "endpointer:reportEndpointBufferHostTime:firstBufferHostTime:"
- "endpointerDelegate"
- "endpointerImplDelegate"
- "endpointerProxy"
- "engineWithDeviceType:streamHandleId:"
- "finishedSkippingSamplesForVT"
- "firstSampleId"
- "frameLength"
- "framePosition"
- "getEndPointAnalyzerTypeWithReply:"
- "getPostVoiceTriggerSilenceWithReply:"
- "handleInputBuffer"
- "hasReportedFirstAudioSampleSensorTimestamp"
- "hybridEndpointer"
- "i20@0:8(?={?=SS}I)16"
- "implDelegate"
- "initForSidekick"
- "initProcessTapWithFormat:PID:"
- "initSystemTapWithFormat:"
- "initWithCommonFormat:sampleRate:channels:interleaved:"
- "initWithEndpointId:xpcClientFactory:endpointer:continuousVoiceTrigger:siriVolumeController:mediaPlayingMonitor:alarmMonitor:timerMonitor:audioSessionController:supportPhatic:supportHearstVoiceTrigger:supportTriagleModeSessionActivationRetry:supportSessionActivateDelay:supportsDuckingOnSpeakerEvaluator:"
- "initWithRequestType:"
- "initWithStreamDescription:"
- "initWithTapDescription:"
- "initWithTargetQueue:audioTapProvider:audioSourceType:"
- "initWithTargetQueue:audioTapProvider:avvcRefChannelAvailable:"
- "initWithTotalAudioRecorded:endpointBufferHostTime:featuresAtEndpoint:endpointerType:asrFeatureLatencyDistribution:additionalMetrics:trailingSilenceDurationAtEndpoint:requestId:"
- "initWithTotalAudioRecorded:endpointBufferHostTime:featuresAtEndpoint:endpointerType:asrFeatureLatencyDistribution:additionalMetrics:trailingSilenceDurationAtEndpoint:requestId:osdFeatures:asrFeatures:isRequestTimeOut:assetConfigVersion:blkHepAudioOrigin:vtExtraAudioAtStartInMs:firstAudioSampleSensorTimestamp:isAnchorTimeBuffered:endpointHostTime:audioDeliveryHostTimeDelta:"
- "interspeechWaitTime"
- "isAudioQueueRecording"
- "isHypotheticalAudioRouteBluetoothFromAudioSessinoId:"
- "isNNVADFallbackUnexpectedForLanguageCode:"
- "isRunningListenerCallback"
- "isRunningListenerCallback_block_invoke"
- "isRunningListenerCallback_block_invoke_3"
- "isWatchRTSTriggered"
- "lastEndOfVoiceActivityTime"
- "lastStartOfVoiceActivityTime"
- "logHybridEndpointFeaturesWithEvent:locale:"
- "loggingQueue"
- "lpcmMonoNonInterleavedASBD"
- "minimumDurationForEndpointer"
- "nnvadAudioOriginInMs"
- "nnvadEndpointer"
- "nnvadState"
- "not "
- "numBytesPerSample"
- "numSamplesReceived"
- "numSamplesSkippedForVT"
- "processedSampleCount"
- "qaaB"
- "receivers"
- "recordingAudioQueue"
- "requestTelephonyDownlinkAudioTap"
- "requiresHistoricalBuffer"
- "resetEndpointer"
- "resetForNewRequestWithSampleRate:recordContext:disableRCSelection:"
- "resetForVoiceTriggerTwoShotWithSampleRate:"
- "saveSamplesSeenInReset"
- "setActiveEndpointer:"
- "setAqStartCompletion:"
- "setAqStopCompletion:"
- "setAsrFeaturesLatencies:"
- "setAudioProviderImp:"
- "setAudioTapProvider:"
- "setAutomaticEndpointingSuspensionEndTime:"
- "setBuiltInAudioInjectionEngine:"
- "setBuiltInDevice:"
- "setBundleTvRemote:"
- "setBypassSamples:"
- "setCurrentRequestAudioFormat:"
- "setDelay:"
- "setDidEnterTwoshot:"
- "setEndWaitTime:"
- "setEndpointStyle:"
- "setEndpointerDelayedTrigger:"
- "setEndpointerDelegate:"
- "setEndpointerImplDelegate:"
- "setEndpointerProxy:"
- "setFinishedSkippingSamplesForVT:"
- "setFirstSampleId:"
- "setFramePosition:"
- "setHasReportedFirstAudioSampleSensorTimestamp:"
- "setHybridEndpointer:"
- "setImplDelegate:"
- "setInterspeechWaitTime:"
- "setLoggingQueue:"
- "setMinimumDurationForEndpointer:"
- "setNnvadAudioOriginInMs:"
- "setNnvadEndpointer:"
- "setNnvadState:"
- "setNumSamplesReceived:"
- "setNumSamplesSkippedForVT:"
- "setProcessedSampleCount:"
- "setReceivers:"
- "setRecordingAudioQueue:"
- "setRequestTelephonyDownlinkAudioTap:"
- "setSaveSamplesSeenInReset:"
- "setShouldDetectTwoShot:"
- "setStartWaitTime:"
- "setTransaction:"
- "setUUIDString:"
- "setVtEndInSecs:"
- "setWithObjects:"
- "sharedContollerProxy"
- "sharedManagerForCoreSpeechDaemon"
- "shouldDetectTwoShot"
- "skipSamplesAtStartSuchThatNumSamplesReceivedSoFar:reachesACountOf:completionHandler:"
- "speechCapturing:didDetectStartpointAtTime:"
- "speechControllerDidDetectEndpoint:ofType:atTime:"
- "speechControllerDidDetectStartpoint:"
- "startAudioStreamWithOption:"
- "startRecordingSampleCount"
- "startSmartSiriVolume"
- "startWaitTime"
- "stopAudioStream"
- "supportsSCDAFramework"
- "transaction"
- "triggerStartSampleCount"
- "updateEndpointerDelayedTrigger:"
- "updateEndpointerThreshold:"
- "updateEnhancedEndpointerDefaultThresholdPartial:defaultThresholdRC:relaxedThresholdPartial:relaxedThresholdRC:"
- "v16@?0@\"<AFMyriadContextMutating>\"8"
- "v24@0:8@\"<CSEndpointAnalyzerImplDelegate>\"16"
- "v24@0:8@\"<NviDataReceiver>\"16"
- "v24@0:8@?<v@?@\"NSError\"Q>16"
- "v24@0:8@?<v@?@\"NSError\"d>16"
- "v24@0:8^{OpaqueAudioQueue=}16"
- "v24@?0@\"CSAudioChunk\"8Q16"
- "v24@?0@\"NSError\"8Q16"
- "v24@?0@\"NSError\"8d16"
- "v32@0:8@\"<CSAttSiriNode>\"16@\"CSEndpointerProxy\"24"
- "v32@0:8@\"<CSAttSiriNode>\"16d24"
- "v32@0:8@\"<CSEndpointAnalyzerImpl>\"16d24"
- "v32@0:8@\"CSAudioInjectionEngine\"16@\"CSAudioChunkForTV\"24"
- "v32@0:8@\"NSDate\"16Q24"
- "v32@0:8d16@\"CSEndpointerMetrics\"24"
- "v32@0:8d16@24"
- "v32@0:8d16Q24"
- "v36@0:8Q16@\"CSAudioRecordContext\"24B32"
- "v36@0:8Q16@24B32"
- "v40@0:8@\"<CSEndpointAnalyzer>\"16d24@\"CSEndpointerMetrics\"32"
- "v40@0:8@\"<CSEndpointAnalyzerImpl>\"16Q24Q32"
- "v40@0:8@\"CSAudioInjectionEngine\"16Q24Q32"
- "v40@0:8@\"CSAudioStream\"16@\"CSAudioStream\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"CSSpeechController\"16q24d32"
- "v40@0:8@\"OSDFeatures\"16d24@\"NSString\"32"
- "v40@0:8@16q24d32"
- "v40@0:8q16q24@32"
- "v44@0:8@\"CSAudioInjectionEngine\"16Q24B32@\"NSError\"36"
- "v60@0:8@\"CSAudioInjectionEngine\"16Q24@\"NSData\"32@\"NSData\"40Q48B56"
- "vtEndInSecs"
- "{unique_ptr<SmartSiriVolume, std::default_delete<SmartSiriVolume>>=\"__ptr_\"{__compressed_pair<SmartSiriVolume *, std::default_delete<SmartSiriVolume>>=\"__value_\"^{SmartSiriVolume}}}"
- "{unique_ptr<corespeech::CSAudioCircularBufferImpl<unsigned char>, std::default_delete<corespeech::CSAudioCircularBufferImpl<unsigned char>>>=\"__ptr_\"{__compressed_pair<corespeech::CSAudioCircularBufferImpl<unsigned char> *, std::default_delete<corespeech::CSAudioCircularBufferImpl<unsigned char>>>=\"__value_\"^v}}"
- "{vector<float, std::allocator<float>>=\"__begin_\"^f\"__end_\"^f\"__end_cap_\"{__compressed_pair<float *, std::allocator<float>>=\"__value_\"^f}}"

```
