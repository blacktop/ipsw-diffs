## LocalSpeechRecognitionBridge

> `/System/Library/PrivateFrameworks/LocalSpeechRecognitionBridge.framework/LocalSpeechRecognitionBridge`

```diff

-3515.11.1.0.0
-  __TEXT.__text: 0xaefc
-  __TEXT.__auth_stubs: 0x400
-  __TEXT.__objc_methlist: 0xc14
+3520.87.3.1.5
+  __TEXT.__text: 0x19140
+  __TEXT.__auth_stubs: 0x490
+  __TEXT.__objc_methlist: 0x1cc4
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__const: 0x1a8
-  __TEXT.__gcc_except_tab: 0x150
-  __TEXT.__cstring: 0x1f50
-  __TEXT.__oslogstring: 0xacf
-  __TEXT.__unwind_info: 0x288
-  __TEXT.__objc_classname: 0x14b
-  __TEXT.__objc_methname: 0x46f3
-  __TEXT.__objc_methtype: 0xf6d
-  __TEXT.__objc_stubs: 0x13a0
-  __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x360
-  __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x48
+  __TEXT.__const: 0x80
+  __TEXT.__gcc_except_tab: 0x27c
+  __TEXT.__oslogstring: 0x2005
+  __TEXT.__cstring: 0x3a2c
+  __TEXT.__unwind_info: 0x620
+  __TEXT.__objc_classname: 0x3dd
+  __TEXT.__objc_methname: 0x7167
+  __TEXT.__objc_methtype: 0x16e6
+  __TEXT.__objc_stubs: 0x2740
+  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__const: 0x628
+  __DATA_CONST.__objc_classlist: 0xa8
+  __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x808
-  __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x210
-  __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0xb40
-  __AUTH_CONST.__objc_const: 0x10f8
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0xd0
-  __DATA.__data: 0x370
-  __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x140
-  __DATA_DIRTY.__bss: 0x38
+  __DATA_CONST.__objc_selrefs: 0xfc0
+  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA_CONST.__objc_arraydata: 0x20
+  __AUTH_CONST.__auth_got: 0x258
+  __AUTH_CONST.__const: 0x80
+  __AUTH_CONST.__cfstring: 0x1680
+  __AUTH_CONST.__objc_const: 0x2f38
+  __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH.__objc_data: 0x460
+  __DATA.__objc_ivar: 0x238
+  __DATA.__data: 0x670
+  __DATA.__bss: 0x18
+  __DATA_DIRTY.__objc_data: 0x230
+  __DATA_DIRTY.__bss: 0x40
   __DATA_DIRTY.__common: 0x8
+  - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2916A78A-58A1-3AA0-BDAD-F7B546D670EB
-  Functions: 222
-  Symbols:   881
-  CStrings:  786
+  UUID: E0CF58F6-171F-3DF4-BF74-A5AF1F6966F6
+  Functions: 565
+  Symbols:   2035
+  CStrings:  1605
 
Symbols:
+ +[LBAudibleExperienceError errorWithCode:]
+ +[LBAudibleExperienceError errorWithCode:localizedDescription:]
+ +[LBAudibleExperienceError errorWithCode:userInfo:]
+ +[LBAudibleExperienceError localizedDescriptionForCode:]
+ +[LBAudioChunk supportsSecureCoding]
+ +[LBAudioPacket supportsSecureCoding]
+ +[LBAudioStreamConfiguration supportsSecureCoding]
+ +[LBAudioStreamConsumerConfiguration supportsSecureCoding]
+ +[LBAudioStreamInfo supportsSecureCoding]
+ +[LBLocalSpeechDetectionUpdates builder]
+ +[LBLocalSpeechDetectionUpdates supportsSecureCoding]
+ +[LBLocalSpeechRecognizerTurnEndContext supportsSecureCoding]
+ +[LBLocalSpeechRecognizerTurnEndContext turnEndReasonString:]
+ -[LBAttendingStatesServiceClient disableAttendingForRootRequestId:]
+ -[LBAudibleExperienceClient .cxx_destruct]
+ -[LBAudibleExperienceClient _cleanupAudioSessionForMediaControlWithEvent:completion:]
+ -[LBAudibleExperienceClient _cleanupAudioSessionForPhoneCallWithEvent:completion:]
+ -[LBAudibleExperienceClient _cleanupAudioSessionForRecordingWithEvent:completion:]
+ -[LBAudibleExperienceClient _handleDidCompleteMediaControlEvent:completion:]
+ -[LBAudibleExperienceClient _handleDidCompletePhoneCallEvent:completion:]
+ -[LBAudibleExperienceClient _handleDidCompleteRecordingEvent:completion:]
+ -[LBAudibleExperienceClient _handleMediaControlEvent:completion:]
+ -[LBAudibleExperienceClient _handlePhoneCallEvent:completion:]
+ -[LBAudibleExperienceClient _handleRecordingEvent:completion:]
+ -[LBAudibleExperienceClient _handleWillStartMediaControlEvent:completion:]
+ -[LBAudibleExperienceClient _handleWillStartPhoneCallEvent:completion:]
+ -[LBAudibleExperienceClient _handleWillStartRecordingEvent:completion:]
+ -[LBAudibleExperienceClient _prepareAudioSessionForMediaControlWithEvent:completion:]
+ -[LBAudibleExperienceClient _prepareAudioSessionForPhoneCallWithEvent:completion:]
+ -[LBAudibleExperienceClient _prepareAudioSessionForRecordingWithEvent:completion:]
+ -[LBAudibleExperienceClient informAudioSessionEvent:completion:]
+ -[LBAudibleExperienceClient init]
+ -[LBAudibleExperienceClient logger]
+ -[LBAudibleExperienceClient queue]
+ -[LBAudibleExperienceClient setLogger:]
+ -[LBAudibleExperienceClient setQueue:]
+ -[LBAudioChunk .cxx_destruct]
+ -[LBAudioChunk arrivalHostTimeToAudioRecorder]
+ -[LBAudioChunk copyWithZone:]
+ -[LBAudioChunk data]
+ -[LBAudioChunk encodeWithCoder:]
+ -[LBAudioChunk hostTime]
+ -[LBAudioChunk initWithCoder:]
+ -[LBAudioChunk initWithData:numSamples:sampleByteDepth:startSampleCount:hostTime:arrivalHostTimeToAudioRecorder:isFloat:]
+ -[LBAudioChunk isFloat]
+ -[LBAudioChunk numSamples]
+ -[LBAudioChunk sampleByteDepth]
+ -[LBAudioChunk startSampleCount]
+ -[LBAudioPacket .cxx_destruct]
+ -[LBAudioPacket chunks]
+ -[LBAudioPacket copyWithZone:]
+ -[LBAudioPacket duration]
+ -[LBAudioPacket encodeWithCoder:]
+ -[LBAudioPacket index]
+ -[LBAudioPacket initWithChunks:duration:]
+ -[LBAudioPacket initWithChunks:duration:index:]
+ -[LBAudioPacket initWithChunks:index:]
+ -[LBAudioPacket initWithChunks:startSampleCount:numSamples:]
+ -[LBAudioPacket initWithCoder:]
+ -[LBAudioPacket setChunks:]
+ -[LBAudioPacket setDuration:]
+ -[LBAudioPacket setIndex:]
+ -[LBAudioRecordingAccessor .cxx_destruct]
+ -[LBAudioRecordingAccessor audioMessageClient]
+ -[LBAudioRecordingAccessor convertAudioFromURL:toURL:format:completion:]
+ -[LBAudioRecordingAccessor dealloc]
+ -[LBAudioRecordingAccessor getAudioFileURLWithCompletion:]
+ -[LBAudioRecordingAccessor initWithRequestId:]
+ -[LBAudioRecordingAccessor requestId]
+ -[LBAudioRecordingAccessor setAudioMessageClient:]
+ -[LBAudioRecordingAccessor writeAudioFileToURL:audioFormat:completion:]
+ -[LBAudioSessionInformEvent .cxx_destruct]
+ -[LBAudioSessionInformEvent actionType]
+ -[LBAudioSessionInformEvent description]
+ -[LBAudioSessionInformEvent initWithActionType:]
+ -[LBAudioSessionInformEvent initWithActionType:timestamp:]
+ -[LBAudioSessionInformEvent timestamp]
+ -[LBAudioSessionMediaControlEvent initWithActionType:]
+ -[LBAudioSessionMediaControlEvent initWithActionType:timestamp:]
+ -[LBAudioSessionPhoneCallEvent initWithActionType:]
+ -[LBAudioSessionPhoneCallEvent initWithActionType:timestamp:]
+ -[LBAudioSessionRecordingEvent .cxx_destruct]
+ -[LBAudioSessionRecordingEvent bundleId]
+ -[LBAudioSessionRecordingEvent initWithActionType:bundleId:]
+ -[LBAudioSessionRecordingEvent initWithActionType:timestamp:]
+ -[LBAudioSessionRecordingEvent initWithActionType:timestamp:bundleId:]
+ -[LBAudioStreamConfiguration .cxx_destruct]
+ -[LBAudioStreamConfiguration audioCaptureStartHostTime]
+ -[LBAudioStreamConfiguration audioRecordDeviceId]
+ -[LBAudioStreamConfiguration audioRecordType]
+ -[LBAudioStreamConfiguration copyWithZone:]
+ -[LBAudioStreamConfiguration encodeWithCoder:]
+ -[LBAudioStreamConfiguration initWithAudioCaptureStartHostTime:outputAudioFormat:audioRecordType:audioRecordDeviceId:]
+ -[LBAudioStreamConfiguration initWithCoder:]
+ -[LBAudioStreamConfiguration outputAudioFormat]
+ -[LBAudioStreamConfiguration setAudioCaptureStartHostTime:]
+ -[LBAudioStreamConfiguration setAudioRecordDeviceId:]
+ -[LBAudioStreamConfiguration setAudioRecordType:]
+ -[LBAudioStreamConfiguration setOutputAudioFormat:]
+ -[LBAudioStreamConsumer .cxx_destruct]
+ -[LBAudioStreamConsumer _cleanupStreamInfo]
+ -[LBAudioStreamConsumer _connection]
+ -[LBAudioStreamConsumer _consumePackets:completion:]
+ -[LBAudioStreamConsumer _didStopConsumingForRequestId:withError:]
+ -[LBAudioStreamConsumer _eventName:]
+ -[LBAudioStreamConsumer _interruptionHandler:]
+ -[LBAudioStreamConsumer _invalidate]
+ -[LBAudioStreamConsumer _invalidationHandler:]
+ -[LBAudioStreamConsumer _newConnection]
+ -[LBAudioStreamConsumer _notifyDelegateDidStopWithError:]
+ -[LBAudioStreamConsumer _service]
+ -[LBAudioStreamConsumer _setupStateMachine]
+ -[LBAudioStreamConsumer _startConsumingWithConfiguration:completion:]
+ -[LBAudioStreamConsumer _stateName:]
+ -[LBAudioStreamConsumer _stopConsumingWithCompletion:]
+ -[LBAudioStreamConsumer configuration]
+ -[LBAudioStreamConsumer consumePackets:completion:]
+ -[LBAudioStreamConsumer didIgnoreEvent:from:]
+ -[LBAudioStreamConsumer didStopConsumingForRequestId:withError:]
+ -[LBAudioStreamConsumer didTransitFrom:to:by:]
+ -[LBAudioStreamConsumer initWithDelegate:]
+ -[LBAudioStreamConsumer initWithDelegate:xpcListenerEndpoint:]
+ -[LBAudioStreamConsumer isConsumingStream]
+ -[LBAudioStreamConsumer queue]
+ -[LBAudioStreamConsumer setConfiguration:]
+ -[LBAudioStreamConsumer setConsumingDelegate:]
+ -[LBAudioStreamConsumer setQueue:]
+ -[LBAudioStreamConsumer setStateMachine:]
+ -[LBAudioStreamConsumer setStopError:]
+ -[LBAudioStreamConsumer setStreamConsumerDelegate:]
+ -[LBAudioStreamConsumer setUuidString:]
+ -[LBAudioStreamConsumer setXpcConnection:]
+ -[LBAudioStreamConsumer setXpcConnectionUUIDString:]
+ -[LBAudioStreamConsumer setXpcListenerEndpoint:]
+ -[LBAudioStreamConsumer startConsumingWithConfiguration:completion:]
+ -[LBAudioStreamConsumer stateMachine]
+ -[LBAudioStreamConsumer stopConsumingWithCompletion:]
+ -[LBAudioStreamConsumer stopError]
+ -[LBAudioStreamConsumer streamConsumerDelegate]
+ -[LBAudioStreamConsumer uuidString]
+ -[LBAudioStreamConsumer xpcConnectionUUIDString]
+ -[LBAudioStreamConsumer xpcConnection]
+ -[LBAudioStreamConsumer xpcListenerEndpoint]
+ -[LBAudioStreamConsumerConfiguration .cxx_destruct]
+ -[LBAudioStreamConsumerConfiguration copyWithZone:]
+ -[LBAudioStreamConsumerConfiguration encodeWithCoder:]
+ -[LBAudioStreamConsumerConfiguration initWithCoder:]
+ -[LBAudioStreamConsumerConfiguration initWithRequestId:streamInfo:]
+ -[LBAudioStreamConsumerConfiguration requestId]
+ -[LBAudioStreamConsumerConfiguration setRequestId:]
+ -[LBAudioStreamConsumerConfiguration setStreamInfo:]
+ -[LBAudioStreamConsumerConfiguration streamInfo]
+ -[LBAudioStreamInfo .cxx_destruct]
+ -[LBAudioStreamInfo audioFormat]
+ -[LBAudioStreamInfo audioRecordDeviceId]
+ -[LBAudioStreamInfo audioRecordType]
+ -[LBAudioStreamInfo copyWithZone:]
+ -[LBAudioStreamInfo encodeWithCoder:]
+ -[LBAudioStreamInfo initWithAudioRecordType:audioRecordDeviceId:recordRoute:audioFormat:streamIdentifier:]
+ -[LBAudioStreamInfo initWithCoder:]
+ -[LBAudioStreamInfo recordRoute]
+ -[LBAudioStreamInfo setAudioFormat:]
+ -[LBAudioStreamInfo setAudioRecordDeviceId:]
+ -[LBAudioStreamInfo setAudioRecordType:]
+ -[LBAudioStreamInfo setRecordRoute:]
+ -[LBAudioStreamInfo streamId]
+ -[LBAudioStreamProvider .cxx_destruct]
+ -[LBAudioStreamProvider _cleanupStreamInfo]
+ -[LBAudioStreamProvider _connection]
+ -[LBAudioStreamProvider _convertChunksToOpus:]
+ -[LBAudioStreamProvider _didReceiveAudioChunks:]
+ -[LBAudioStreamProvider _didStartStreamingWithInfo:]
+ -[LBAudioStreamProvider _didStopStreamingWithError:]
+ -[LBAudioStreamProvider _eventName:]
+ -[LBAudioStreamProvider _flushConversionBufferIfNecessary]
+ -[LBAudioStreamProvider _formatIsSupported:]
+ -[LBAudioStreamProvider _interruptionHandler:]
+ -[LBAudioStreamProvider _invalidate]
+ -[LBAudioStreamProvider _invalidationHandler:]
+ -[LBAudioStreamProvider _newConnection]
+ -[LBAudioStreamProvider _notifyDelegateOfChunks:fromFormat:toFormat:]
+ -[LBAudioStreamProvider _notifyDelegateOfFloatConvertedChunks:]
+ -[LBAudioStreamProvider _notifyDelegateOfNativeChunks:]
+ -[LBAudioStreamProvider _notifyDelegateOfShortConvertedChunks:]
+ -[LBAudioStreamProvider _resetStreamInfo]
+ -[LBAudioStreamProvider _sanitizeStreamConfiguration:]
+ -[LBAudioStreamProvider _service]
+ -[LBAudioStreamProvider _setupStateMachine]
+ -[LBAudioStreamProvider _startStreaming:]
+ -[LBAudioStreamProvider _stateName:]
+ -[LBAudioStreamProvider _stopStreaming]
+ -[LBAudioStreamProvider audioConverterDidConvertPackets:packets:durationInSec:timestamp:arrivalTimestampToAudioRecorder:]
+ -[LBAudioStreamProvider currentOutgoingStreamIndex]
+ -[LBAudioStreamProvider didIgnoreEvent:from:]
+ -[LBAudioStreamProvider didReceiveAudioChunks:]
+ -[LBAudioStreamProvider didStartStreamingWithInfo:]
+ -[LBAudioStreamProvider didStopStreamingWithError:]
+ -[LBAudioStreamProvider didTransitFrom:to:by:]
+ -[LBAudioStreamProvider hasStartedEncodingPaackets]
+ -[LBAudioStreamProvider incomingAudioChunks]
+ -[LBAudioStreamProvider incomingStreamInfo]
+ -[LBAudioStreamProvider initWithDelegate:]
+ -[LBAudioStreamProvider initWithDelegate:xpcListenerEndpoint:]
+ -[LBAudioStreamProvider isProvidingStream]
+ -[LBAudioStreamProvider opusConverter]
+ -[LBAudioStreamProvider outgoingStreamInfo]
+ -[LBAudioStreamProvider queue]
+ -[LBAudioStreamProvider requestId]
+ -[LBAudioStreamProvider setCurrentOutgoingStreamIndex:]
+ -[LBAudioStreamProvider setHasStartedEncodingPaackets:]
+ -[LBAudioStreamProvider setIncomingAudioChunks:]
+ -[LBAudioStreamProvider setIncomingStreamInfo:]
+ -[LBAudioStreamProvider setIsProvidingStream:]
+ -[LBAudioStreamProvider setOpusConverter:]
+ -[LBAudioStreamProvider setOutgoingStreamInfo:]
+ -[LBAudioStreamProvider setQueue:]
+ -[LBAudioStreamProvider setRequestId:]
+ -[LBAudioStreamProvider setStateMachine:]
+ -[LBAudioStreamProvider setStreamConfiguration:]
+ -[LBAudioStreamProvider setStreamProviderDelegate:]
+ -[LBAudioStreamProvider setStreamingDelegate:]
+ -[LBAudioStreamProvider setUuidString:]
+ -[LBAudioStreamProvider setXpcConnection:]
+ -[LBAudioStreamProvider setXpcConnectionUUIDString:]
+ -[LBAudioStreamProvider setXpcListenerEndpoint:]
+ -[LBAudioStreamProvider startStreaming:]
+ -[LBAudioStreamProvider stateMachine]
+ -[LBAudioStreamProvider stopStreaming]
+ -[LBAudioStreamProvider streamConfiguration]
+ -[LBAudioStreamProvider streamProviderDelegate]
+ -[LBAudioStreamProvider uuidString]
+ -[LBAudioStreamProvider xpcConnectionUUIDString]
+ -[LBAudioStreamProvider xpcConnection]
+ -[LBAudioStreamProvider xpcListenerEndpoint]
+ -[LBLocalSpeechDetectionUpdates .cxx_destruct]
+ -[LBLocalSpeechDetectionUpdates _computeMessageHash]
+ -[LBLocalSpeechDetectionUpdates copyWithZone:]
+ -[LBLocalSpeechDetectionUpdates description]
+ -[LBLocalSpeechDetectionUpdates didDetectPostVTSilence]
+ -[LBLocalSpeechDetectionUpdates didTRPArrivalTimeout]
+ -[LBLocalSpeechDetectionUpdates encodeWithCoder:]
+ -[LBLocalSpeechDetectionUpdates initWithCoder:]
+ -[LBLocalSpeechDetectionUpdates initWithLastTRPCandidateId:speechDetected:isSameUser:isInvocationUser:didDetectPostVTSilence:didTRPArrivalTimeout:noSpeechTokensDetectedInRequest:minSpeechEventThresholdMet:longFormSpeechEventThresholdMet:maxSpeechEventThresholdMet:noTRPArrivalThresholdMet:mitigationTrailingSilenceThresholdMet:isManualMode:processedAudioDurationMs:]
+ -[LBLocalSpeechDetectionUpdates isInvocationUser]
+ -[LBLocalSpeechDetectionUpdates isManualMode]
+ -[LBLocalSpeechDetectionUpdates isSameUser]
+ -[LBLocalSpeechDetectionUpdates lastTRPCandidateId]
+ -[LBLocalSpeechDetectionUpdates longFormSpeechEventThresholdMet]
+ -[LBLocalSpeechDetectionUpdates maxSpeechEventThresholdMet]
+ -[LBLocalSpeechDetectionUpdates messageHash]
+ -[LBLocalSpeechDetectionUpdates minSpeechEventThresholdMet]
+ -[LBLocalSpeechDetectionUpdates mitigationTrailingSilenceThresholdMet]
+ -[LBLocalSpeechDetectionUpdates noSpeechTokensDetectedInRequest]
+ -[LBLocalSpeechDetectionUpdates noTRPArrivalThresholdMet]
+ -[LBLocalSpeechDetectionUpdates processedAudioDurationMs]
+ -[LBLocalSpeechDetectionUpdates speechDetected]
+ -[LBLocalSpeechDetectionUpdates toBuilder]
+ -[LBLocalSpeechDetectionUpdatesBuilder .cxx_destruct]
+ -[LBLocalSpeechDetectionUpdatesBuilder build]
+ -[LBLocalSpeechDetectionUpdatesBuilder initWithUpdates:]
+ -[LBLocalSpeechDetectionUpdatesBuilder init]
+ -[LBLocalSpeechDetectionUpdatesBuilder setDidDetectPostVTSilence:]
+ -[LBLocalSpeechDetectionUpdatesBuilder setDidTRPArrivalTimeout:]
+ -[LBLocalSpeechDetectionUpdatesBuilder setIsInvocationUser:]
+ -[LBLocalSpeechDetectionUpdatesBuilder setIsManualMode:]
+ -[LBLocalSpeechDetectionUpdatesBuilder setIsSameUser:]
+ -[LBLocalSpeechDetectionUpdatesBuilder setLastTRPCandidateId:]
+ -[LBLocalSpeechDetectionUpdatesBuilder setLongFormSpeechEventThresholdMet:]
+ -[LBLocalSpeechDetectionUpdatesBuilder setMaxSpeechEventThresholdMet:]
+ -[LBLocalSpeechDetectionUpdatesBuilder setMinSpeechEventThresholdMet:]
+ -[LBLocalSpeechDetectionUpdatesBuilder setMitigationTrailingSilenceThresholdMet:]
+ -[LBLocalSpeechDetectionUpdatesBuilder setNoSpeechTokensDetectedInRequest:]
+ -[LBLocalSpeechDetectionUpdatesBuilder setNoTRPArrivalThresholdMet:]
+ -[LBLocalSpeechDetectionUpdatesBuilder setProcessedAudioDurationMs:]
+ -[LBLocalSpeechDetectionUpdatesBuilder setSpeechDetected:]
+ -[LBLocalSpeechRecognitionSettings initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:asrLocale:activeUserInfo:messagesContext:sessionId:]
+ -[LBLocalSpeechRecognitionSettings sessionId]
+ -[LBLocalSpeechRecognizerClient _forwardInitialSpeechUpdate]
+ -[LBLocalSpeechRecognizerClient _notifyObserverOfSpeechDetectionEvent:]
+ -[LBLocalSpeechRecognizerClient _querySpeechDetectionUpdatesEventWithCompletion:]
+ -[LBLocalSpeechRecognizerClient _stopAudioCaptureWithReason:requestId:]
+ -[LBLocalSpeechRecognizerClient dismissForRequestId:]
+ -[LBLocalSpeechRecognizerClient localSpeechServiceDidReceiveSpeechDetectionEvent:]
+ -[LBLocalSpeechRecognizerClient localSpeechServiceDidReceiveSpeechDetectionUpdate:]
+ -[LBLocalSpeechRecognizerClient requestingSpeechDetectionNotificationAfter:forRequest:withTrpId:]
+ -[LBLocalSpeechRecognizerClient turnEndedForRequestId:withTrpId:]
+ -[LBLocalSpeechRecognizerClient turnEndedwithContext:]
+ -[LBLocalSpeechRecognizerTurnEndContext .cxx_destruct]
+ -[LBLocalSpeechRecognizerTurnEndContext copyWithZone:]
+ -[LBLocalSpeechRecognizerTurnEndContext description]
+ -[LBLocalSpeechRecognizerTurnEndContext encodeWithCoder:]
+ -[LBLocalSpeechRecognizerTurnEndContext initWithCoder:]
+ -[LBLocalSpeechRecognizerTurnEndContext initWithRequestId:selectedTrpId:]
+ -[LBLocalSpeechRecognizerTurnEndContext initWithRequestId:selectedTrpId:turnEndReason:processedAudioDuration:trailingSilenceDurationMs:]
+ -[LBLocalSpeechRecognizerTurnEndContext initWithRequestId:trpId:turnEndReason:processedAudioDuration:trailingSilenceDurationMs:]
+ -[LBLocalSpeechRecognizerTurnEndContext processedAudioDuration]
+ -[LBLocalSpeechRecognizerTurnEndContext requestId]
+ -[LBLocalSpeechRecognizerTurnEndContext selectedTrpId]
+ -[LBLocalSpeechRecognizerTurnEndContext trailingSilenceDurationMs]
+ -[LBLocalSpeechRecognizerTurnEndContext trpId]
+ -[LBLocalSpeechRecognizerTurnEndContext turnEndReason]
+ GCC_except_table150
+ GCC_except_table275
+ GCC_except_table37
+ GCC_except_table376
+ GCC_except_table380
+ GCC_except_table387
+ GCC_except_table453
+ GCC_except_table555
+ _ExtAudioFileCreateWithURL
+ _ExtAudioFileDispose
+ _ExtAudioFileGetProperty
+ _ExtAudioFileOpenURL
+ _ExtAudioFileRead
+ _ExtAudioFileSetProperty
+ _ExtAudioFileWrite
+ _LBAudibleExperienceErrorDomain
+ _LBAudioStreamConsumerServiceDelegateGetXPCInterface
+ _LBAudioStreamConsumerServiceGetXPCInterface
+ _LBAudioStreamConsumerServiceName
+ _LBAudioStreamProviderServiceDelegateGetXPCInterface
+ _LBAudioStreamProviderServiceGetXPCInterface
+ _LBAudioStreamProviderServiceName
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_AFAudioSessionEvent
+ _OBJC_CLASS_$_AFAudioSessionEventInformService
+ _OBJC_CLASS_$_CSFAudioConverter
+ _OBJC_CLASS_$_CSFLPCMTypeConverter
+ _OBJC_CLASS_$_CSSiriAudioMessageRequestClient
+ _OBJC_CLASS_$_CSStateMachine
+ _OBJC_CLASS_$_CSUtils
+ _OBJC_CLASS_$_LBAudibleExperienceClient
+ _OBJC_CLASS_$_LBAudibleExperienceError
+ _OBJC_CLASS_$_LBAudioChunk
+ _OBJC_CLASS_$_LBAudioPacket
+ _OBJC_CLASS_$_LBAudioRecordingAccessor
+ _OBJC_CLASS_$_LBAudioSessionInformEvent
+ _OBJC_CLASS_$_LBAudioSessionMediaControlEvent
+ _OBJC_CLASS_$_LBAudioSessionPhoneCallEvent
+ _OBJC_CLASS_$_LBAudioSessionRecordingEvent
+ _OBJC_CLASS_$_LBAudioStreamConfiguration
+ _OBJC_CLASS_$_LBAudioStreamConsumer
+ _OBJC_CLASS_$_LBAudioStreamConsumerConfiguration
+ _OBJC_CLASS_$_LBAudioStreamInfo
+ _OBJC_CLASS_$_LBAudioStreamProvider
+ _OBJC_CLASS_$_LBLocalSpeechDetectionUpdates
+ _OBJC_CLASS_$_LBLocalSpeechDetectionUpdatesBuilder
+ _OBJC_CLASS_$_LBLocalSpeechRecognizerTurnEndContext
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_IVAR_$_LBAudibleExperienceClient._logger
+ _OBJC_IVAR_$_LBAudibleExperienceClient._queue
+ _OBJC_IVAR_$_LBAudioChunk._arrivalHostTimeToAudioRecorder
+ _OBJC_IVAR_$_LBAudioChunk._data
+ _OBJC_IVAR_$_LBAudioChunk._hostTime
+ _OBJC_IVAR_$_LBAudioChunk._isFloat
+ _OBJC_IVAR_$_LBAudioChunk._numSamples
+ _OBJC_IVAR_$_LBAudioChunk._sampleByteDepth
+ _OBJC_IVAR_$_LBAudioChunk._startSampleCount
+ _OBJC_IVAR_$_LBAudioPacket._chunks
+ _OBJC_IVAR_$_LBAudioPacket._duration
+ _OBJC_IVAR_$_LBAudioPacket._index
+ _OBJC_IVAR_$_LBAudioRecordingAccessor._audioMessageClient
+ _OBJC_IVAR_$_LBAudioRecordingAccessor._requestId
+ _OBJC_IVAR_$_LBAudioSessionInformEvent._actionType
+ _OBJC_IVAR_$_LBAudioSessionInformEvent._timestamp
+ _OBJC_IVAR_$_LBAudioSessionRecordingEvent._bundleId
+ _OBJC_IVAR_$_LBAudioStreamConfiguration._audioCaptureStartHostTime
+ _OBJC_IVAR_$_LBAudioStreamConfiguration._audioRecordDeviceId
+ _OBJC_IVAR_$_LBAudioStreamConfiguration._audioRecordType
+ _OBJC_IVAR_$_LBAudioStreamConfiguration._outputAudioFormat
+ _OBJC_IVAR_$_LBAudioStreamConsumer._configuration
+ _OBJC_IVAR_$_LBAudioStreamConsumer._isConsumingStream
+ _OBJC_IVAR_$_LBAudioStreamConsumer._queue
+ _OBJC_IVAR_$_LBAudioStreamConsumer._stateMachine
+ _OBJC_IVAR_$_LBAudioStreamConsumer._stopError
+ _OBJC_IVAR_$_LBAudioStreamConsumer._streamConsumerDelegate
+ _OBJC_IVAR_$_LBAudioStreamConsumer._uuidString
+ _OBJC_IVAR_$_LBAudioStreamConsumer._xpcConnection
+ _OBJC_IVAR_$_LBAudioStreamConsumer._xpcConnectionUUIDString
+ _OBJC_IVAR_$_LBAudioStreamConsumer._xpcListenerEndpoint
+ _OBJC_IVAR_$_LBAudioStreamConsumerConfiguration._requestId
+ _OBJC_IVAR_$_LBAudioStreamConsumerConfiguration._streamInfo
+ _OBJC_IVAR_$_LBAudioStreamInfo._audioFormat
+ _OBJC_IVAR_$_LBAudioStreamInfo._audioRecordDeviceId
+ _OBJC_IVAR_$_LBAudioStreamInfo._audioRecordType
+ _OBJC_IVAR_$_LBAudioStreamInfo._recordRoute
+ _OBJC_IVAR_$_LBAudioStreamInfo._streamId
+ _OBJC_IVAR_$_LBAudioStreamProvider._currentOutgoingStreamIndex
+ _OBJC_IVAR_$_LBAudioStreamProvider._hasStartedEncodingPaackets
+ _OBJC_IVAR_$_LBAudioStreamProvider._incomingAudioChunks
+ _OBJC_IVAR_$_LBAudioStreamProvider._incomingStreamInfo
+ _OBJC_IVAR_$_LBAudioStreamProvider._isProvidingStream
+ _OBJC_IVAR_$_LBAudioStreamProvider._opusConverter
+ _OBJC_IVAR_$_LBAudioStreamProvider._outgoingStreamInfo
+ _OBJC_IVAR_$_LBAudioStreamProvider._queue
+ _OBJC_IVAR_$_LBAudioStreamProvider._requestId
+ _OBJC_IVAR_$_LBAudioStreamProvider._stateMachine
+ _OBJC_IVAR_$_LBAudioStreamProvider._streamConfiguration
+ _OBJC_IVAR_$_LBAudioStreamProvider._streamProviderDelegate
+ _OBJC_IVAR_$_LBAudioStreamProvider._uuidString
+ _OBJC_IVAR_$_LBAudioStreamProvider._xpcConnection
+ _OBJC_IVAR_$_LBAudioStreamProvider._xpcConnectionUUIDString
+ _OBJC_IVAR_$_LBAudioStreamProvider._xpcListenerEndpoint
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdates._didDetectPostVTSilence
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdates._didTRPArrivalTimeout
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdates._isInvocationUser
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdates._isManualMode
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdates._isSameUser
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdates._lastTRPCandidateId
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdates._longFormSpeechEventThresholdMet
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdates._maxSpeechEventThresholdMet
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdates._messageHash
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdates._minSpeechEventThresholdMet
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdates._mitigationTrailingSilenceThresholdMet
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdates._noSpeechTokensDetectedInRequest
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdates._noTRPArrivalThresholdMet
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdates._processedAudioDurationMs
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdates._speechDetected
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdatesBuilder._didDetectPostVTSilence
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdatesBuilder._didTRPArrivalTimeout
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdatesBuilder._isInvocationUser
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdatesBuilder._isManualMode
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdatesBuilder._isSameUser
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdatesBuilder._lastTRPCandidateId
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdatesBuilder._longFormSpeechEventThresholdMet
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdatesBuilder._maxSpeechEventThresholdMet
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdatesBuilder._minSpeechEventThresholdMet
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdatesBuilder._mitigationTrailingSilenceThresholdMet
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdatesBuilder._noSpeechTokensDetectedInRequest
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdatesBuilder._noTRPArrivalThresholdMet
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdatesBuilder._processedAudioDurationMs
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdatesBuilder._speechDetected
+ _OBJC_IVAR_$_LBLocalSpeechRecognitionSettings._sessionId
+ _OBJC_IVAR_$_LBLocalSpeechRecognizerTurnEndContext._processedAudioDuration
+ _OBJC_IVAR_$_LBLocalSpeechRecognizerTurnEndContext._requestId
+ _OBJC_IVAR_$_LBLocalSpeechRecognizerTurnEndContext._selectedTrpId
+ _OBJC_IVAR_$_LBLocalSpeechRecognizerTurnEndContext._trailingSilenceDurationMs
+ _OBJC_IVAR_$_LBLocalSpeechRecognizerTurnEndContext._trpId
+ _OBJC_IVAR_$_LBLocalSpeechRecognizerTurnEndContext._turnEndReason
+ _OBJC_METACLASS_$_LBAudibleExperienceClient
+ _OBJC_METACLASS_$_LBAudibleExperienceError
+ _OBJC_METACLASS_$_LBAudioChunk
+ _OBJC_METACLASS_$_LBAudioPacket
+ _OBJC_METACLASS_$_LBAudioRecordingAccessor
+ _OBJC_METACLASS_$_LBAudioSessionInformEvent
+ _OBJC_METACLASS_$_LBAudioSessionMediaControlEvent
+ _OBJC_METACLASS_$_LBAudioSessionPhoneCallEvent
+ _OBJC_METACLASS_$_LBAudioSessionRecordingEvent
+ _OBJC_METACLASS_$_LBAudioStreamConfiguration
+ _OBJC_METACLASS_$_LBAudioStreamConsumer
+ _OBJC_METACLASS_$_LBAudioStreamConsumerConfiguration
+ _OBJC_METACLASS_$_LBAudioStreamInfo
+ _OBJC_METACLASS_$_LBAudioStreamProvider
+ _OBJC_METACLASS_$_LBLocalSpeechDetectionUpdates
+ _OBJC_METACLASS_$_LBLocalSpeechDetectionUpdatesBuilder
+ _OBJC_METACLASS_$_LBLocalSpeechRecognizerTurnEndContext
+ __OBJC_$_CLASS_METHODS_LBAudibleExperienceError
+ __OBJC_$_CLASS_METHODS_LBAudioChunk
+ __OBJC_$_CLASS_METHODS_LBAudioPacket
+ __OBJC_$_CLASS_METHODS_LBAudioStreamConfiguration
+ __OBJC_$_CLASS_METHODS_LBAudioStreamConsumerConfiguration
+ __OBJC_$_CLASS_METHODS_LBAudioStreamInfo
+ __OBJC_$_CLASS_METHODS_LBLocalSpeechDetectionUpdates
+ __OBJC_$_CLASS_METHODS_LBLocalSpeechRecognizerTurnEndContext
+ __OBJC_$_CLASS_PROP_LIST_LBAudioChunk
+ __OBJC_$_CLASS_PROP_LIST_LBAudioPacket
+ __OBJC_$_CLASS_PROP_LIST_LBAudioStreamConfiguration
+ __OBJC_$_CLASS_PROP_LIST_LBAudioStreamConsumerConfiguration
+ __OBJC_$_CLASS_PROP_LIST_LBAudioStreamInfo
+ __OBJC_$_CLASS_PROP_LIST_LBLocalSpeechDetectionUpdates
+ __OBJC_$_CLASS_PROP_LIST_LBLocalSpeechRecognizerTurnEndContext
+ __OBJC_$_INSTANCE_METHODS_LBAudibleExperienceClient
+ __OBJC_$_INSTANCE_METHODS_LBAudioChunk
+ __OBJC_$_INSTANCE_METHODS_LBAudioPacket
+ __OBJC_$_INSTANCE_METHODS_LBAudioRecordingAccessor
+ __OBJC_$_INSTANCE_METHODS_LBAudioSessionInformEvent
+ __OBJC_$_INSTANCE_METHODS_LBAudioSessionMediaControlEvent
+ __OBJC_$_INSTANCE_METHODS_LBAudioSessionPhoneCallEvent
+ __OBJC_$_INSTANCE_METHODS_LBAudioSessionRecordingEvent
+ __OBJC_$_INSTANCE_METHODS_LBAudioStreamConfiguration
+ __OBJC_$_INSTANCE_METHODS_LBAudioStreamConsumer
+ __OBJC_$_INSTANCE_METHODS_LBAudioStreamConsumerConfiguration
+ __OBJC_$_INSTANCE_METHODS_LBAudioStreamInfo
+ __OBJC_$_INSTANCE_METHODS_LBAudioStreamProvider
+ __OBJC_$_INSTANCE_METHODS_LBLocalSpeechDetectionUpdates
+ __OBJC_$_INSTANCE_METHODS_LBLocalSpeechDetectionUpdatesBuilder
+ __OBJC_$_INSTANCE_METHODS_LBLocalSpeechRecognizerTurnEndContext
+ __OBJC_$_INSTANCE_VARIABLES_LBAudibleExperienceClient
+ __OBJC_$_INSTANCE_VARIABLES_LBAudioChunk
+ __OBJC_$_INSTANCE_VARIABLES_LBAudioPacket
+ __OBJC_$_INSTANCE_VARIABLES_LBAudioRecordingAccessor
+ __OBJC_$_INSTANCE_VARIABLES_LBAudioSessionInformEvent
+ __OBJC_$_INSTANCE_VARIABLES_LBAudioSessionRecordingEvent
+ __OBJC_$_INSTANCE_VARIABLES_LBAudioStreamConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_LBAudioStreamConsumer
+ __OBJC_$_INSTANCE_VARIABLES_LBAudioStreamConsumerConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_LBAudioStreamInfo
+ __OBJC_$_INSTANCE_VARIABLES_LBAudioStreamProvider
+ __OBJC_$_INSTANCE_VARIABLES_LBLocalSpeechDetectionUpdates
+ __OBJC_$_INSTANCE_VARIABLES_LBLocalSpeechDetectionUpdatesBuilder
+ __OBJC_$_INSTANCE_VARIABLES_LBLocalSpeechRecognizerTurnEndContext
+ __OBJC_$_PROP_LIST_LBAudibleExperienceClient
+ __OBJC_$_PROP_LIST_LBAudioChunk
+ __OBJC_$_PROP_LIST_LBAudioPacket
+ __OBJC_$_PROP_LIST_LBAudioRecordingAccessor
+ __OBJC_$_PROP_LIST_LBAudioSessionInformEvent
+ __OBJC_$_PROP_LIST_LBAudioSessionRecordingEvent
+ __OBJC_$_PROP_LIST_LBAudioStreamConfiguration
+ __OBJC_$_PROP_LIST_LBAudioStreamConsumer
+ __OBJC_$_PROP_LIST_LBAudioStreamConsumerConfiguration
+ __OBJC_$_PROP_LIST_LBAudioStreamConsuming
+ __OBJC_$_PROP_LIST_LBAudioStreamInfo
+ __OBJC_$_PROP_LIST_LBAudioStreamProvider
+ __OBJC_$_PROP_LIST_LBAudioStreamProviding
+ __OBJC_$_PROP_LIST_LBLocalSpeechDetectionUpdates
+ __OBJC_$_PROP_LIST_LBLocalSpeechRecognizerTurnEndContext
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSFAudioConverterDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSStateMachineDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LBAudioStreamConsumerService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LBAudioStreamConsumerServiceDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LBAudioStreamConsuming
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LBAudioStreamProviderService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LBAudioStreamProviderServiceDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LBAudioStreamProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSFAudioConverterDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSStateMachineDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LBAudioStreamConsumerService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LBAudioStreamConsumerServiceDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LBAudioStreamConsuming
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LBAudioStreamProviderService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LBAudioStreamProviderServiceDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LBAudioStreamProviding
+ __OBJC_$_PROTOCOL_REFS_CSFAudioConverterDelegate
+ __OBJC_$_PROTOCOL_REFS_CSStateMachineDelegate
+ __OBJC_$_PROTOCOL_REFS_LBAudioStreamConsumerService
+ __OBJC_$_PROTOCOL_REFS_LBAudioStreamConsumerServiceDelegate
+ __OBJC_$_PROTOCOL_REFS_LBAudioStreamConsuming
+ __OBJC_$_PROTOCOL_REFS_LBAudioStreamProviderService
+ __OBJC_$_PROTOCOL_REFS_LBAudioStreamProviderServiceDelegate
+ __OBJC_$_PROTOCOL_REFS_LBAudioStreamProviding
+ __OBJC_CLASS_PROTOCOLS_$_LBAudioChunk
+ __OBJC_CLASS_PROTOCOLS_$_LBAudioPacket
+ __OBJC_CLASS_PROTOCOLS_$_LBAudioStreamConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_LBAudioStreamConsumer
+ __OBJC_CLASS_PROTOCOLS_$_LBAudioStreamConsumerConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_LBAudioStreamInfo
+ __OBJC_CLASS_PROTOCOLS_$_LBAudioStreamProvider
+ __OBJC_CLASS_PROTOCOLS_$_LBLocalSpeechDetectionUpdates
+ __OBJC_CLASS_PROTOCOLS_$_LBLocalSpeechRecognizerTurnEndContext
+ __OBJC_CLASS_RO_$_LBAudibleExperienceClient
+ __OBJC_CLASS_RO_$_LBAudibleExperienceError
+ __OBJC_CLASS_RO_$_LBAudioChunk
+ __OBJC_CLASS_RO_$_LBAudioPacket
+ __OBJC_CLASS_RO_$_LBAudioRecordingAccessor
+ __OBJC_CLASS_RO_$_LBAudioSessionInformEvent
+ __OBJC_CLASS_RO_$_LBAudioSessionMediaControlEvent
+ __OBJC_CLASS_RO_$_LBAudioSessionPhoneCallEvent
+ __OBJC_CLASS_RO_$_LBAudioSessionRecordingEvent
+ __OBJC_CLASS_RO_$_LBAudioStreamConfiguration
+ __OBJC_CLASS_RO_$_LBAudioStreamConsumer
+ __OBJC_CLASS_RO_$_LBAudioStreamConsumerConfiguration
+ __OBJC_CLASS_RO_$_LBAudioStreamInfo
+ __OBJC_CLASS_RO_$_LBAudioStreamProvider
+ __OBJC_CLASS_RO_$_LBLocalSpeechDetectionUpdates
+ __OBJC_CLASS_RO_$_LBLocalSpeechDetectionUpdatesBuilder
+ __OBJC_CLASS_RO_$_LBLocalSpeechRecognizerTurnEndContext
+ __OBJC_LABEL_PROTOCOL_$_CSFAudioConverterDelegate
+ __OBJC_LABEL_PROTOCOL_$_CSStateMachineDelegate
+ __OBJC_LABEL_PROTOCOL_$_LBAudioStreamConsumerService
+ __OBJC_LABEL_PROTOCOL_$_LBAudioStreamConsumerServiceDelegate
+ __OBJC_LABEL_PROTOCOL_$_LBAudioStreamConsuming
+ __OBJC_LABEL_PROTOCOL_$_LBAudioStreamProviderService
+ __OBJC_LABEL_PROTOCOL_$_LBAudioStreamProviderServiceDelegate
+ __OBJC_LABEL_PROTOCOL_$_LBAudioStreamProviding
+ __OBJC_METACLASS_RO_$_LBAudibleExperienceClient
+ __OBJC_METACLASS_RO_$_LBAudibleExperienceError
+ __OBJC_METACLASS_RO_$_LBAudioChunk
+ __OBJC_METACLASS_RO_$_LBAudioPacket
+ __OBJC_METACLASS_RO_$_LBAudioRecordingAccessor
+ __OBJC_METACLASS_RO_$_LBAudioSessionInformEvent
+ __OBJC_METACLASS_RO_$_LBAudioSessionMediaControlEvent
+ __OBJC_METACLASS_RO_$_LBAudioSessionPhoneCallEvent
+ __OBJC_METACLASS_RO_$_LBAudioSessionRecordingEvent
+ __OBJC_METACLASS_RO_$_LBAudioStreamConfiguration
+ __OBJC_METACLASS_RO_$_LBAudioStreamConsumer
+ __OBJC_METACLASS_RO_$_LBAudioStreamConsumerConfiguration
+ __OBJC_METACLASS_RO_$_LBAudioStreamInfo
+ __OBJC_METACLASS_RO_$_LBAudioStreamProvider
+ __OBJC_METACLASS_RO_$_LBLocalSpeechDetectionUpdates
+ __OBJC_METACLASS_RO_$_LBLocalSpeechDetectionUpdatesBuilder
+ __OBJC_METACLASS_RO_$_LBLocalSpeechRecognizerTurnEndContext
+ __OBJC_PROTOCOL_$_CSFAudioConverterDelegate
+ __OBJC_PROTOCOL_$_CSStateMachineDelegate
+ __OBJC_PROTOCOL_$_LBAudioStreamConsumerService
+ __OBJC_PROTOCOL_$_LBAudioStreamConsumerServiceDelegate
+ __OBJC_PROTOCOL_$_LBAudioStreamConsuming
+ __OBJC_PROTOCOL_$_LBAudioStreamProviderService
+ __OBJC_PROTOCOL_$_LBAudioStreamProviderServiceDelegate
+ __OBJC_PROTOCOL_$_LBAudioStreamProviding
+ __OBJC_PROTOCOL_REFERENCE_$_LBAudioStreamConsumerService
+ __OBJC_PROTOCOL_REFERENCE_$_LBAudioStreamConsumerServiceDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_LBAudioStreamProviderService
+ __OBJC_PROTOCOL_REFERENCE_$_LBAudioStreamProviderServiceDelegate
+ ___36-[LBAudioStreamConsumer _connection]_block_invoke
+ ___36-[LBAudioStreamConsumer _connection]_block_invoke.7
+ ___36-[LBAudioStreamProvider _connection]_block_invoke
+ ___36-[LBAudioStreamProvider _connection]_block_invoke.4
+ ___38-[LBAudioStreamProvider stopStreaming]_block_invoke
+ ___40-[LBAudioStreamProvider startStreaming:]_block_invoke
+ ___44-[LBLocalSpeechRecognizerClient _connection]_block_invoke.390
+ ___46-[LBAudioStreamConsumer setConsumingDelegate:]_block_invoke
+ ___46-[LBAudioStreamProvider setStreamingDelegate:]_block_invoke
+ ___47-[LBAudioStreamProvider didReceiveAudioChunks:]_block_invoke
+ ___51-[LBAudioStreamConsumer consumePackets:completion:]_block_invoke
+ ___51-[LBAudioStreamProvider didStartStreamingWithInfo:]_block_invoke
+ ___51-[LBAudioStreamProvider didStopStreamingWithError:]_block_invoke
+ ___52-[LBAudioStreamConsumer _consumePackets:completion:]_block_invoke
+ ___53-[LBAudioStreamConsumer stopConsumingWithCompletion:]_block_invoke
+ ___53-[LBLocalSpeechRecognizerClient dismissForRequestId:]_block_invoke
+ ___54-[LBLocalSpeechRecognizerClient turnEndedwithContext:]_block_invoke
+ ___58-[LBAudioRecordingAccessor getAudioFileURLWithCompletion:]_block_invoke
+ ___60-[LBLocalSpeechRecognizerClient _forwardInitialSpeechUpdate]_block_invoke
+ ___64-[LBAudibleExperienceClient informAudioSessionEvent:completion:]_block_invoke
+ ___64-[LBAudioStreamConsumer didStopConsumingForRequestId:withError:]_block_invoke
+ ___67-[LBAttendingStatesServiceClient disableAttendingForRootRequestId:]_block_invoke
+ ___68-[LBAudioStreamConsumer startConsumingWithConfiguration:completion:]_block_invoke
+ ___69-[LBAudioStreamConsumer _startConsumingWithConfiguration:completion:]_block_invoke
+ ___69-[LBAudioStreamConsumer _startConsumingWithConfiguration:completion:]_block_invoke_2
+ ___71-[LBAudibleExperienceClient _handleWillStartPhoneCallEvent:completion:]_block_invoke
+ ___71-[LBAudibleExperienceClient _handleWillStartRecordingEvent:completion:]_block_invoke
+ ___71-[LBAudioRecordingAccessor writeAudioFileToURL:audioFormat:completion:]_block_invoke
+ ___71-[LBLocalSpeechRecognizerClient _stopAudioCaptureWithReason:requestId:]_block_invoke
+ ___73-[LBAudibleExperienceClient _handleDidCompletePhoneCallEvent:completion:]_block_invoke
+ ___73-[LBAudibleExperienceClient _handleDidCompleteRecordingEvent:completion:]_block_invoke
+ ___74-[LBAudibleExperienceClient _handleWillStartMediaControlEvent:completion:]_block_invoke
+ ___75-[LBLocalSpeechRecognizerClient startSpeechRecognitionResultsWithSettings:]_block_invoke.338
+ ___76-[LBAudibleExperienceClient _handleDidCompleteMediaControlEvent:completion:]_block_invoke
+ ___82-[LBAudibleExperienceClient _prepareAudioSessionForPhoneCallWithEvent:completion:]_block_invoke
+ ___82-[LBAudibleExperienceClient _prepareAudioSessionForPhoneCallWithEvent:completion:]_block_invoke_2
+ ___82-[LBAudibleExperienceClient _prepareAudioSessionForRecordingWithEvent:completion:]_block_invoke
+ ___82-[LBAudibleExperienceClient _prepareAudioSessionForRecordingWithEvent:completion:]_block_invoke_2
+ ___85-[LBAudibleExperienceClient _prepareAudioSessionForMediaControlWithEvent:completion:]_block_invoke
+ ___85-[LBAudibleExperienceClient _prepareAudioSessionForMediaControlWithEvent:completion:]_block_invoke_2
+ ___97-[LBLocalSpeechRecognizerClient requestingSpeechDetectionNotificationAfter:forRequest:withTrpId:]_block_invoke
+ ___NSArray0__struct
+ ___block_descriptor_32_e39_v16?0"<AFAudioSessionEventMutating>"8l
+ ___block_descriptor_40_e8_32bs_e28_v24?0"NSString"8"NSURL"16ls32l8
+ ___block_descriptor_40_e8_32s_e51_v24?0"LBLocalSpeechDetectionUpdates"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e20_v20?0B8"NSError"12lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48bs56w_e5_v8?0lw56l8s48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e15_v16?0"NSURL"8ls56l8s32l8s40l8s48l8
+ ___block_literal_global.1562
+ ___block_literal_global.16
+ ___block_literal_global.18
+ ___getSMTSpeechDetectionUpdateClass_block_invoke
+ _getSMTSpeechDetectionUpdateClass.softClass
+ _localSpeechServiceDidReceiveSpeechDetectionUpdate:.heartbeat
+ _mach_absolute_time
+ _malloc_type_malloc
+ _objc_allocWithZone
+ _objc_autorelease
+ _objc_enumerationMutation
+ _objc_msgSend$URLByAppendingPathComponent:isDirectory:
+ _objc_msgSend$URLByDeletingLastPathComponent
+ _objc_msgSend$_cleanupAudioSessionForMediaControlWithEvent:completion:
+ _objc_msgSend$_cleanupAudioSessionForPhoneCallWithEvent:completion:
+ _objc_msgSend$_cleanupAudioSessionForRecordingWithEvent:completion:
+ _objc_msgSend$_cleanupStreamInfo
+ _objc_msgSend$_computeMessageHash
+ _objc_msgSend$_consumePackets:completion:
+ _objc_msgSend$_convertChunksToOpus:
+ _objc_msgSend$_didReceiveAudioChunks:
+ _objc_msgSend$_didStartStreamingWithInfo:
+ _objc_msgSend$_didStopConsumingForRequestId:withError:
+ _objc_msgSend$_didStopStreamingWithError:
+ _objc_msgSend$_eventName:
+ _objc_msgSend$_flushConversionBufferIfNecessary
+ _objc_msgSend$_formatIsSupported:
+ _objc_msgSend$_forwardInitialSpeechUpdate
+ _objc_msgSend$_handleDidCompleteMediaControlEvent:completion:
+ _objc_msgSend$_handleDidCompletePhoneCallEvent:completion:
+ _objc_msgSend$_handleDidCompleteRecordingEvent:completion:
+ _objc_msgSend$_handleMediaControlEvent:completion:
+ _objc_msgSend$_handlePhoneCallEvent:completion:
+ _objc_msgSend$_handleRecordingEvent:completion:
+ _objc_msgSend$_handleWillStartMediaControlEvent:completion:
+ _objc_msgSend$_handleWillStartPhoneCallEvent:completion:
+ _objc_msgSend$_handleWillStartRecordingEvent:completion:
+ _objc_msgSend$_interruptionHandler:
+ _objc_msgSend$_invalidationHandler:
+ _objc_msgSend$_notifyDelegateDidStopWithError:
+ _objc_msgSend$_notifyDelegateOfChunks:fromFormat:toFormat:
+ _objc_msgSend$_notifyDelegateOfFloatConvertedChunks:
+ _objc_msgSend$_notifyDelegateOfNativeChunks:
+ _objc_msgSend$_notifyDelegateOfShortConvertedChunks:
+ _objc_msgSend$_notifyObserverOfSpeechDetectionEvent:
+ _objc_msgSend$_prepareAudioSessionForMediaControlWithEvent:completion:
+ _objc_msgSend$_prepareAudioSessionForPhoneCallWithEvent:completion:
+ _objc_msgSend$_prepareAudioSessionForRecordingWithEvent:completion:
+ _objc_msgSend$_querySpeechDetectionUpdatesEventWithCompletion:
+ _objc_msgSend$_resetStreamInfo
+ _objc_msgSend$_sanitizeStreamConfiguration:
+ _objc_msgSend$_setupStateMachine
+ _objc_msgSend$_startConsumingWithConfiguration:completion:
+ _objc_msgSend$_startStreaming:
+ _objc_msgSend$_stateName:
+ _objc_msgSend$_stopAudioCaptureWithReason:requestId:
+ _objc_msgSend$_stopConsumingWithCompletion:
+ _objc_msgSend$_stopStreaming
+ _objc_msgSend$actionType
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$addObject:
+ _objc_msgSend$addSamples:timestamp:arrivalTimestampToAudioRecorder:
+ _objc_msgSend$addTransitionFrom:to:for:
+ _objc_msgSend$addTransitionFromAnyStateTo:for:
+ _objc_msgSend$allocWithZone:
+ _objc_msgSend$arrivalHostTimeToAudioRecorder
+ _objc_msgSend$audioFormat
+ _objc_msgSend$audioMessageClient
+ _objc_msgSend$audioStreamConsumer:didStopWithError:
+ _objc_msgSend$audioStreamProvider:didStartWithInfo:
+ _objc_msgSend$audioStreamProvider:didStopWithError:
+ _objc_msgSend$audioStreamProvider:receivedPackets:
+ _objc_msgSend$bundleId
+ _objc_msgSend$consumePackets:forRequestId:completion:
+ _objc_msgSend$containerURLForSecurityApplicationGroupIdentifier:
+ _objc_msgSend$convertAudioFromURL:toURL:format:completion:
+ _objc_msgSend$convertToFloatLPCMBufFromShortLPCMBuf:
+ _objc_msgSend$convertToShortLPCMBufFromFloatLPCMBuf:
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$currentState
+ _objc_msgSend$data
+ _objc_msgSend$date
+ _objc_msgSend$decodeArrayOfObjectsOfClass:forKey:
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeIntegerForKey:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$didDetectPostVTSilence
+ _objc_msgSend$didTRPArrivalTimeout
+ _objc_msgSend$disableAttendingForRootRequestId:
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeInteger:forKey:
+ _objc_msgSend$errorWithCode:
+ _objc_msgSend$errorWithCode:localizedDescription:
+ _objc_msgSend$errorWithCode:userInfo:
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$flush
+ _objc_msgSend$getAudioFileURLWithCompletion:
+ _objc_msgSend$getAudioFileWithRequestId:completion:
+ _objc_msgSend$hash
+ _objc_msgSend$hostTime
+ _objc_msgSend$informAudioSessionEvent:completion:
+ _objc_msgSend$init
+ _objc_msgSend$initWithActionType:timestamp:
+ _objc_msgSend$initWithActionType:timestamp:bundleId:
+ _objc_msgSend$initWithAudioCaptureStartHostTime:outputAudioFormat:audioRecordType:audioRecordDeviceId:
+ _objc_msgSend$initWithAudioRecordType:audioRecordDeviceId:recordRoute:audioFormat:streamIdentifier:
+ _objc_msgSend$initWithBuilder:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithChunks:index:
+ _objc_msgSend$initWithData:numSamples:sampleByteDepth:startSampleCount:hostTime:arrivalHostTimeToAudioRecorder:isFloat:
+ _objc_msgSend$initWithDelegate:xpcListenerEndpoint:
+ _objc_msgSend$initWithInitialState:
+ _objc_msgSend$initWithLastTRPCandidateId:speechDetected:isSameUser:isInvocationUser:didDetectPostVTSilence:didTRPArrivalTimeout:noSpeechTokensDetectedInRequest:minSpeechEventThresholdMet:longFormSpeechEventThresholdMet:maxSpeechEventThresholdMet:noTRPArrivalThresholdMet:mitigationTrailingSilenceThresholdMet:isManualMode:processedAudioDurationMs:
+ _objc_msgSend$initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:asrLocale:activeUserInfo:messagesContext:sessionId:
+ _objc_msgSend$initWithRequestId:selectedTrpId:
+ _objc_msgSend$initWithRequestId:selectedTrpId:turnEndReason:processedAudioDuration:trailingSilenceDurationMs:
+ _objc_msgSend$initWithUpdates:
+ _objc_msgSend$isAudioStreamConsumingEnabled
+ _objc_msgSend$isAudioStreamProvidingEnabled
+ _objc_msgSend$isInvocationUser
+ _objc_msgSend$isManualMode
+ _objc_msgSend$isSameUser
+ _objc_msgSend$lastTRPCandidateId
+ _objc_msgSend$linkItemAtURL:toURL:error:
+ _objc_msgSend$localSpeechRecognizerClient:receivedSpeechDetectionEvent:
+ _objc_msgSend$localSpeechRecognizerClient:receivedSpeechDetectionUpdate:
+ _objc_msgSend$localizedDescriptionForCode:
+ _objc_msgSend$logger
+ _objc_msgSend$loggingHeartbeatRate
+ _objc_msgSend$longFormSpeechEventThresholdMet
+ _objc_msgSend$maxSpeechEventThresholdMet
+ _objc_msgSend$minSpeechEventThresholdMet
+ _objc_msgSend$mitigationTrailingSilenceThresholdMet
+ _objc_msgSend$noSpeechTokensDetectedInRequest
+ _objc_msgSend$noTRPArrivalThresholdMet
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$opusConverter
+ _objc_msgSend$outputAudioFormat
+ _objc_msgSend$path
+ _objc_msgSend$performTransitionForEvent:
+ _objc_msgSend$processedAudioDurationMs
+ _objc_msgSend$recordRoute
+ _objc_msgSend$releaseAudioMessageRetainLockFromRequestId:
+ _objc_msgSend$reset
+ _objc_msgSend$setAudioCaptureStartHostTime:
+ _objc_msgSend$setAudioFormat:
+ _objc_msgSend$setAudioRecordDeviceId:
+ _objc_msgSend$setAudioRecordType:
+ _objc_msgSend$setEventTime:
+ _objc_msgSend$setEventType:
+ _objc_msgSend$setHostTime:
+ _objc_msgSend$setInterface:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setOutputAudioFormat:
+ _objc_msgSend$setRecordRoute:
+ _objc_msgSend$setRequestId:
+ _objc_msgSend$setStreamInfo:
+ _objc_msgSend$speechDetected
+ _objc_msgSend$startConsumingWithConfiguration:completion:
+ _objc_msgSend$startStreamingWithDelegate:timestamp:
+ _objc_msgSend$stopStreaming
+ _objc_msgSend$streamId
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$turnEndReasonString:
+ _objc_msgSend$turnEndedwithContext:
+ _objc_opt_isKindOfClass
+ _objc_release_x1
+ _objc_retainAutoreleasedReturnValue
+ _objc_setProperty_nonatomic_copy
- +[CSRecordTypeSpeechEventConverter getRecordTypeForSpeechEvent:]
- +[CSRecordTypeSpeechEventConverter getSpeechEventForRecordType:]
- GCC_except_table13
- GCC_except_table146
- GCC_except_table213
- GCC_except_table95
- _NSLog
- _OBJC_METACLASS_$_CSRecordTypeSpeechEventConverter
- __OBJC_$_CLASS_METHODS_CSRecordTypeSpeechEventConverter
- __OBJC_CLASS_RO_$_CSRecordTypeSpeechEventConverter
- __OBJC_METACLASS_RO_$_CSRecordTypeSpeechEventConverter
- ___44-[LBLocalSpeechRecognizerClient _connection]_block_invoke.328
- ___75-[LBLocalSpeechRecognizerClient startSpeechRecognitionResultsWithSettings:]_block_invoke.287
- ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutorelease
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x9
CStrings:
+ ""
+ "%s #stream Creating new xpc connection..."
+ "%s #stream Ignore event(%{public}@) from(%{public}@) since we don't have transition"
+ "%s #stream Ignore since the UUID of xpc connection not match : %@ vs. %@"
+ "%s #stream attempt to start stream while already streaming"
+ "%s #stream consuming packets encountered an error: %@"
+ "%s #stream converting %lu packets to opus"
+ "%s #stream converting packet from %lld to %lld"
+ "%s #stream created LBAudioStreamConsumer with uuid [%@]"
+ "%s #stream created LBAudioStreamProvider with uuid [%@]"
+ "%s #stream did receive audio: %lu"
+ "%s #stream did start streaming: %@"
+ "%s #stream did stop streaming with error: %@"
+ "%s #stream failed to create opus converter"
+ "%s #stream flushing current encoding buffer"
+ "%s #stream format not supported: %lld"
+ "%s #stream from:%{public}@ to:%{public}@ by:%{public}@"
+ "%s #stream ignoring request stop for request: %@ when current request: %@"
+ "%s #stream ignoring request. already in state %{public}@"
+ "%s #stream ignoring request. currently in state %{public}@"
+ "%s #stream incorrect state to be streaming: %@"
+ "%s #stream incorrect state to stop streaming: %@"
+ "%s #stream invalidating connection"
+ "%s #stream not streaming. Ignoring request."
+ "%s #stream nothing to flush as current stream does not require it"
+ "%s #stream nothing to flush as encoder does not exist"
+ "%s #stream nothing to flush as no packets have been encoded"
+ "%s #stream notifying delegate of stop state with error: %@"
+ "%s #stream opus converter created"
+ "%s #stream packets consumed successfully"
+ "%s #stream posting packets: %lu"
+ "%s #stream receievd request stop when no request is active: %@"
+ "%s #stream received empty chunks"
+ "%s #stream received empty packet conversion"
+ "%s #stream start called with hosttime: %llu"
+ "%s #stream start encountered an error: %@"
+ "%s #stream started consuming successfully"
+ "%s #stream stop stream with requestId: %@"
+ "%s #stream streaming consuming is not supported."
+ "%s #stream streaming providing is not supported."
+ "%s #stream unable to connect"
+ "%s #stream xpc connection %@ Interrupted"
+ "%s #stream xpc connection %@ Invalidated"
+ "%s #stream xpc connection did interrupt"
+ "%s #stream xpc connection did invalidate"
+ "%s Failed to create destination audio file: %d"
+ "%s Failed to decode `arrivalHostTimeToAudioRecorder`"
+ "%s Failed to decode `audioCaptureStartHostTime`"
+ "%s Failed to decode `audioFormat`"
+ "%s Failed to decode `audioRecordDeviceId`"
+ "%s Failed to decode `audioRecordType`"
+ "%s Failed to decode `chunks`"
+ "%s Failed to decode `data`"
+ "%s Failed to decode `duration`"
+ "%s Failed to decode `hostTime`"
+ "%s Failed to decode `index`"
+ "%s Failed to decode `isFloat`"
+ "%s Failed to decode `numSamples`"
+ "%s Failed to decode `outputAudioFormat`"
+ "%s Failed to decode `recordRoute`"
+ "%s Failed to decode `requestId`"
+ "%s Failed to decode `sampleByteDepth`"
+ "%s Failed to decode `startSampleCount`"
+ "%s Failed to decode `streamId`"
+ "%s Failed to decode `streamInfo`"
+ "%s Failed to get source audio format: %d"
+ "%s Failed to link audio file: %@"
+ "%s Failed to open source audio file: %d"
+ "%s Failed to read audio data: %d"
+ "%s Failed to set destination client format: %d"
+ "%s Failed to set source client format: %d"
+ "%s Failed to write audio data: %d"
+ "%s LBLocalSpeechRecognizerClient[%@], xpcConnection[%@]:Delegate does not respond to receivedSpeechDetectionEvent"
+ "%s LBLocalSpeechRecognizerClient[%@], xpcConnection[%@]:Delivering LBSpeechDetectionUpdate: %@"
+ "%s LBLocalSpeechRecognizerClient[%@], xpcConnection[%@]:Error querying speechUpdate"
+ "%s LBLocalSpeechRecognizerClient[%@], xpcConnection[%@]:No delegate set, skipping initial speech update check"
+ "%s LBLocalSpeechRecognizerClient[%@], xpcConnection[%@]:TurnEndContext : %@"
+ "%s LBLocalSpeechRecognizerClient[%@], xpcConnection[%@]:notify speechUpdate: %@"
+ "%s LBLocalSpeechRecognizerClient[%@], xpcConnection[%@]:received speech detection event at processedAudioDuration: %ld"
+ "%s LBLocalSpeechRecognizerClient[%@], xpcConnection[%@]:received speech update at %{public}ld, heartbeat = %{public}lld"
+ "%s LBLocalSpeechRecognizerClient[%@], xpcConnection[%@]:remainingTrailingSilence: %f, requestId : %@, trpId : %@"
+ "%s Successfully converted audio file from %@ to %@"
+ "%s Unable to access audio recording since Missing request ID"
+ "%s Unable to create output directory at %@: %@"
+ "%s Unable to write audio file since Missing output URL"
+ "%s Unable to write audio file since Missing request ID"
+ "%s Unable to write audio file: Output file already exists at %@"
+ "%s Unable to write audio file: Source audio file not found"
+ "("
+ "(null)"
+ "-[LBAttendingStatesServiceClient disableAttendingForRootRequestId:]_block_invoke"
+ "-[LBAudioChunk initWithCoder:]"
+ "-[LBAudioPacket initWithCoder:]"
+ "-[LBAudioRecordingAccessor convertAudioFromURL:toURL:format:completion:]"
+ "-[LBAudioRecordingAccessor getAudioFileURLWithCompletion:]"
+ "-[LBAudioRecordingAccessor writeAudioFileToURL:audioFormat:completion:]"
+ "-[LBAudioRecordingAccessor writeAudioFileToURL:audioFormat:completion:]_block_invoke"
+ "-[LBAudioStreamConfiguration initWithCoder:]"
+ "-[LBAudioStreamConsumer _connection]"
+ "-[LBAudioStreamConsumer _connection]_block_invoke"
+ "-[LBAudioStreamConsumer _consumePackets:completion:]"
+ "-[LBAudioStreamConsumer _consumePackets:completion:]_block_invoke"
+ "-[LBAudioStreamConsumer _didStopConsumingForRequestId:withError:]"
+ "-[LBAudioStreamConsumer _interruptionHandler:]"
+ "-[LBAudioStreamConsumer _invalidate]"
+ "-[LBAudioStreamConsumer _invalidationHandler:]"
+ "-[LBAudioStreamConsumer _notifyDelegateDidStopWithError:]"
+ "-[LBAudioStreamConsumer _startConsumingWithConfiguration:completion:]"
+ "-[LBAudioStreamConsumer _startConsumingWithConfiguration:completion:]_block_invoke"
+ "-[LBAudioStreamConsumer _startConsumingWithConfiguration:completion:]_block_invoke_2"
+ "-[LBAudioStreamConsumer _stopConsumingWithCompletion:]"
+ "-[LBAudioStreamConsumer didIgnoreEvent:from:]"
+ "-[LBAudioStreamConsumer didStopConsumingForRequestId:withError:]"
+ "-[LBAudioStreamConsumer didTransitFrom:to:by:]"
+ "-[LBAudioStreamConsumer initWithDelegate:xpcListenerEndpoint:]"
+ "-[LBAudioStreamConsumer setConsumingDelegate:]_block_invoke"
+ "-[LBAudioStreamConsumerConfiguration initWithCoder:]"
+ "-[LBAudioStreamInfo initWithCoder:]"
+ "-[LBAudioStreamProvider _connection]"
+ "-[LBAudioStreamProvider _connection]_block_invoke"
+ "-[LBAudioStreamProvider _convertChunksToOpus:]"
+ "-[LBAudioStreamProvider _didReceiveAudioChunks:]"
+ "-[LBAudioStreamProvider _didStartStreamingWithInfo:]"
+ "-[LBAudioStreamProvider _didStopStreamingWithError:]"
+ "-[LBAudioStreamProvider _flushConversionBufferIfNecessary]"
+ "-[LBAudioStreamProvider _interruptionHandler:]"
+ "-[LBAudioStreamProvider _invalidate]"
+ "-[LBAudioStreamProvider _invalidationHandler:]"
+ "-[LBAudioStreamProvider _notifyDelegateOfChunks:fromFormat:toFormat:]"
+ "-[LBAudioStreamProvider _notifyDelegateOfFloatConvertedChunks:]"
+ "-[LBAudioStreamProvider _notifyDelegateOfNativeChunks:]"
+ "-[LBAudioStreamProvider _notifyDelegateOfShortConvertedChunks:]"
+ "-[LBAudioStreamProvider _startStreaming:]"
+ "-[LBAudioStreamProvider _stopStreaming]"
+ "-[LBAudioStreamProvider audioConverterDidConvertPackets:packets:durationInSec:timestamp:arrivalTimestampToAudioRecorder:]"
+ "-[LBAudioStreamProvider didIgnoreEvent:from:]"
+ "-[LBAudioStreamProvider didTransitFrom:to:by:]"
+ "-[LBAudioStreamProvider initWithDelegate:xpcListenerEndpoint:]"
+ "-[LBAudioStreamProvider setStreamingDelegate:]_block_invoke"
+ "-[LBLocalSpeechRecognizerClient _forwardInitialSpeechUpdate]"
+ "-[LBLocalSpeechRecognizerClient _forwardInitialSpeechUpdate]_block_invoke"
+ "-[LBLocalSpeechRecognizerClient _notifyObserverOfSpeechDetectionEvent:]"
+ "-[LBLocalSpeechRecognizerClient _stopAudioCaptureWithReason:requestId:]_block_invoke"
+ "-[LBLocalSpeechRecognizerClient localSpeechServiceDidReceiveSpeechDetectionEvent:]"
+ "-[LBLocalSpeechRecognizerClient localSpeechServiceDidReceiveSpeechDetectionUpdate:]"
+ "-[LBLocalSpeechRecognizerClient requestingSpeechDetectionNotificationAfter:forRequest:withTrpId:]_block_invoke"
+ "-[LBLocalSpeechRecognizerClient turnEndedwithContext:]_block_invoke"
+ "1"
+ "<%@: %p, actionType: %lu, timestamp: %@>"
+ "<%@: %p; messageHash=%lu, lastTRPCandidateId=%@, speechDetected=%d, isSameUser=%d, isInvocationUser=%d, didDetectPostVTSilence=%d, didTRPArrivalTimeout=%d, noSpeechTokensDetectedInRequest=%d, minSpeechEventThresholdMet=%d, longFormSpeechEventThresholdMet=%d, maxSpeechEventThresholdMet=%d, noTRPArrivalThresholdMet=%d, mitigationTrailingSilenceThresholdMet=%d, isManualMode=%d, processedAudioDurationMs=%ld>"
+ "<%@: %p> requestId=%@, trpId=%@, selectedTrpId=%@, turnEndReason=%@, processedAudioDuration=%f, trailingSilenceDurationMs=%f"
+ "@\"<LBAudioStreamConsumingDelegate>\""
+ "@\"<LBAudioStreamConsumingDelegate>\"16@0:8"
+ "@\"<LBAudioStreamProvidingDelegate>\""
+ "@\"<LBAudioStreamProvidingDelegate>\"16@0:8"
+ "@\"CSFAudioConverter\""
+ "@\"CSSiriAudioMessageRequestClient\""
+ "@\"CSStateMachine\""
+ "@\"LBAudioStreamConfiguration\""
+ "@\"LBAudioStreamConsumerConfiguration\""
+ "@\"LBAudioStreamInfo\""
+ "@\"NSData\""
+ "@\"NSDate\""
+ "@\"NSError\""
+ "@\"NSMutableArray\""
+ "@\"NSObject<OS_os_log>\""
+ "@\"NSUUID\""
+ "@20@0:8B16"
+ "@24@0:8q16"
+ "@252@0:8@16@24Q32Q40@48@56@64@72B80B84B88B92d96@104B112B116B120B124@128B136@140@148@156@164@172@180B188Q192q200@208B216@220@228@236@244"
+ "@32@0:8@16@24"
+ "@32@0:8@16Q24"
+ "@32@0:8@16d24"
+ "@32@0:8q16@24"
+ "@40@0:8@16Q24Q32"
+ "@40@0:8@16d24Q32"
+ "@40@0:8Q16@24@32"
+ "@48@0:8Q16q24q32@40"
+ "@56@0:8@16@24Q32d40d48"
+ "@56@0:8q16@24@32q40@48"
+ "@68@0:8@16Q24Q32Q40Q48Q56B64"
+ "@80@0:8@16B24B28B32B36B40B44B48B52B56B60B64B68q72"
+ "Audio session event cannot be nil"
+ "Audio session event: %@ with action: %lu"
+ "Audio session event: media control did complete"
+ "Audio session event: media control will start"
+ "Audio session event: phone call did complete"
+ "Audio session event: phone call will start"
+ "Audio session event: recording did complete - bundle: %@"
+ "Audio session event: recording will start - bundle: %@"
+ "CSFAudioConverterDelegate"
+ "CSStateMachineDelegate"
+ "Class getSMTSpeechDetectionUpdateClass(void)_block_invoke"
+ "Connect"
+ "Connected"
+ "Consuming"
+ "Disconnect"
+ "Event cannot be nil"
+ "Failed to cleanup after media control event: %{public}@"
+ "Failed to cleanup after phone call event: %{public}@"
+ "Failed to cleanup after recording event: %{public}@"
+ "Failed to cleanup audio session"
+ "Failed to create destination audio file: %d"
+ "Failed to get source audio format: %d"
+ "Failed to open source audio file: %d"
+ "Failed to prepare audio session"
+ "Failed to prepare for media control event: %{public}@"
+ "Failed to prepare for phone call event: %{public}@"
+ "Failed to prepare for recording event: %{public}@"
+ "Failed to read audio data: %d"
+ "Failed to set destination client format: %d"
+ "Failed to set source client format: %d"
+ "Failed to write audio data: %d"
+ "FirstTurnMitigation"
+ "FollowUpAcousticMitigation"
+ "Invalid"
+ "LBAudibleExperienceClient"
+ "LBAudibleExperienceError"
+ "LBAudibleExperienceErrorDomain"
+ "LBAudioChunk"
+ "LBAudioPacket"
+ "LBAudioPacket:::chunks"
+ "LBAudioPacket:::duration"
+ "LBAudioPacket:::index"
+ "LBAudioRecordingAccessor"
+ "LBAudioSessionInformEvent"
+ "LBAudioSessionMediaControlEvent"
+ "LBAudioSessionPhoneCallEvent"
+ "LBAudioSessionRecordingEvent"
+ "LBAudioStreamConfiguration"
+ "LBAudioStreamConfiguration:::audioCaptureStartHostTime"
+ "LBAudioStreamConfiguration:::audioFormat"
+ "LBAudioStreamConfiguration:::audioRecordDeviceId"
+ "LBAudioStreamConfiguration:::audioRecordType"
+ "LBAudioStreamConsumer"
+ "LBAudioStreamConsumer Queue"
+ "LBAudioStreamConsumerConfiguration"
+ "LBAudioStreamConsumerConfiguration:::requestId"
+ "LBAudioStreamConsumerConfiguration:::streamInfo"
+ "LBAudioStreamConsumerService"
+ "LBAudioStreamConsumerServiceDelegate"
+ "LBAudioStreamConsuming"
+ "LBAudioStreamInfo"
+ "LBAudioStreamInfo:::audioFormat"
+ "LBAudioStreamInfo:::audioRecordDeviceId"
+ "LBAudioStreamInfo:::audioRecordType"
+ "LBAudioStreamInfo:::recordRoute"
+ "LBAudioStreamInfo:::streamId"
+ "LBAudioStreamProvider"
+ "LBAudioStreamProviderService"
+ "LBAudioStreamProviderServiceDelegate"
+ "LBAudioStreamProviding"
+ "LBLocalSpeechDetectionUpdates"
+ "LBLocalSpeechDetectionUpdatesBuilder"
+ "LBLocalSpeechRecognitionSettings:::sessionId"
+ "LBLocalSpeechRecognizerTurnEndContext"
+ "LBLocalSpeechRecognizerTurnEndSettings:::processedAudioDuration"
+ "LBLocalSpeechRecognizerTurnEndSettings:::requestId"
+ "LBLocalSpeechRecognizerTurnEndSettings:::selectedTrpId"
+ "LBLocalSpeechRecognizerTurnEndSettings:::trailingSilenceDurationMs"
+ "LBLocalSpeechRecognizerTurnEndSettings:::trpId"
+ "LBLocalSpeechRecognizerTurnEndSettings:::turnEndReason"
+ "SMTSpeechDetectionUpdate"
+ "SpeakerChange"
+ "SpeechNoMatch"
+ "StartConsuming"
+ "StartStreaming"
+ "StartedStreaming"
+ "StopConsuming"
+ "StopStreaming"
+ "Stopped"
+ "StoppedStreaming"
+ "Successfully cleaned up after media control event"
+ "Successfully cleaned up after phone call event"
+ "Successfully cleaned up after recording event"
+ "Successfully prepared for media control event"
+ "Successfully prepared for phone call event"
+ "Successfully prepared for recording event"
+ "T@\"<LBAudioStreamConsumingDelegate>\",W,N"
+ "T@\"<LBAudioStreamConsumingDelegate>\",W,N,V_streamConsumerDelegate"
+ "T@\"<LBAudioStreamProvidingDelegate>\",W,N"
+ "T@\"<LBAudioStreamProvidingDelegate>\",W,N,V_streamProviderDelegate"
+ "T@\"CSFAudioConverter\",&,N,V_opusConverter"
+ "T@\"CSSiriAudioMessageRequestClient\",&,N,V_audioMessageClient"
+ "T@\"CSStateMachine\",&,N,V_stateMachine"
+ "T@\"LBAudioStreamConfiguration\",C,N,V_streamConfiguration"
+ "T@\"LBAudioStreamConsumerConfiguration\",&,N,V_configuration"
+ "T@\"LBAudioStreamInfo\",C,N,V_incomingStreamInfo"
+ "T@\"LBAudioStreamInfo\",C,N,V_outgoingStreamInfo"
+ "T@\"LBAudioStreamInfo\",C,N,V_streamInfo"
+ "T@\"NSArray\",C,N,V_chunks"
+ "T@\"NSData\",R,N,V_data"
+ "T@\"NSDate\",R,N,V_timestamp"
+ "T@\"NSError\",&,N,V_stopError"
+ "T@\"NSMutableArray\",&,N,V_incomingAudioChunks"
+ "T@\"NSObject<OS_os_log>\",&,N,V_logger"
+ "T@\"NSString\",C,N,V_audioRecordDeviceId"
+ "T@\"NSString\",C,N,V_recordRoute"
+ "T@\"NSString\",C,N,V_requestId"
+ "T@\"NSString\",R,C,N,V_requestId"
+ "T@\"NSString\",R,N,V_bundleId"
+ "T@\"NSString\",R,N,V_lastTRPCandidateId"
+ "T@\"NSString\",R,N,V_selectedTrpId"
+ "T@\"NSString\",R,N,V_sessionId"
+ "T@\"NSString\",R,N,V_trpId"
+ "T@\"NSUUID\",R,C,N,V_streamId"
+ "T@\"NSXPCListenerEndpoint\",&,N,V_xpcListenerEndpoint"
+ "TB,N,V_hasStartedEncodingPaackets"
+ "TB,N,V_isProvidingStream"
+ "TB,R,N"
+ "TB,R,N,V_didDetectPostVTSilence"
+ "TB,R,N,V_didTRPArrivalTimeout"
+ "TB,R,N,V_isConsumingStream"
+ "TB,R,N,V_isFloat"
+ "TB,R,N,V_isInvocationUser"
+ "TB,R,N,V_isManualMode"
+ "TB,R,N,V_isSameUser"
+ "TB,R,N,V_longFormSpeechEventThresholdMet"
+ "TB,R,N,V_maxSpeechEventThresholdMet"
+ "TB,R,N,V_minSpeechEventThresholdMet"
+ "TB,R,N,V_mitigationTrailingSilenceThresholdMet"
+ "TB,R,N,V_noSpeechTokensDetectedInRequest"
+ "TB,R,N,V_noTRPArrivalThresholdMet"
+ "TB,R,N,V_speechDetected"
+ "TQ,N,V_audioCaptureStartHostTime"
+ "TQ,N,V_currentOutgoingStreamIndex"
+ "TQ,N,V_index"
+ "TQ,R,N,V_actionType"
+ "TQ,R,N,V_arrivalHostTimeToAudioRecorder"
+ "TQ,R,N,V_hostTime"
+ "TQ,R,N,V_messageHash"
+ "TQ,R,N,V_numSamples"
+ "TQ,R,N,V_sampleByteDepth"
+ "TQ,R,N,V_startSampleCount"
+ "TQ,R,N,V_turnEndReason"
+ "TRPTimeOut"
+ "Td,N,V_duration"
+ "Td,R,N,V_processedAudioDuration"
+ "Td,R,N,V_trailingSilenceDurationMs"
+ "Tq,N,V_audioFormat"
+ "Tq,N,V_audioRecordType"
+ "Tq,N,V_outputAudioFormat"
+ "Tq,R,N,V_processedAudioDurationMs"
+ "TrailingSilence"
+ "URLByAppendingPathComponent:isDirectory:"
+ "URLByDeletingLastPathComponent"
+ "Unable to create output directory: %@"
+ "Unable to write audio file: Missing output URL"
+ "Unable to write audio file: Missing request ID"
+ "Unable to write audio file: Output file already exists"
+ "Unable to write audio file: Source audio file not found"
+ "Unknown action type"
+ "Unknown action type: %lu"
+ "Unknown audio session event type: %@"
+ "Unknown error"
+ "Unknown event type"
+ "Unknown event type: %@"
+ "Vv24@0:8@\"LBAudioStreamInfo\"16"
+ "Vv24@0:8@\"LBLocalSpeechDetectionUpdates\"16"
+ "Vv24@0:8@\"LBLocalSpeechRecognizerTurnEndContext\"16"
+ "Vv24@0:8@\"NSArray\"16"
+ "Vv24@0:8@\"NSError\"16"
+ "Vv24@0:8@\"SMTSpeechDetectionUpdate\"16"
+ "Vv24@0:8@?16"
+ "Vv24@0:8@?<v@?@\"LBLocalSpeechDetectionUpdates\"@\"NSError\">16"
+ "Vv32@0:8@\"<LBAudioStreamProviderServiceDelegate>\"16Q24"
+ "Vv32@0:8@\"LBAudioStreamConsumerConfiguration\"16@?<v@?B@\"NSError\">24"
+ "Vv32@0:8@\"NSString\"16@\"NSError\"24"
+ "Vv32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
+ "Vv32@0:8@16@?24"
+ "Vv40@0:8@\"NSArray\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
+ "Vv40@0:8@16@24@?32"
+ "Vv40@0:8d16@\"NSString\"24@\"NSString\"32"
+ "Vv40@0:8d16@24@32"
+ "WaitingToStart"
+ "WillStartConsuming"
+ "WillStartStreaming"
+ "XPC connection error"
+ "[sessionId = %@]"
+ "_actionType"
+ "_arrivalHostTimeToAudioRecorder"
+ "_audioFormat"
+ "_audioMessageClient"
+ "_bundleId"
+ "_chunks"
+ "_cleanupAudioSessionForMediaControlWithEvent:completion:"
+ "_cleanupAudioSessionForPhoneCallWithEvent:completion:"
+ "_cleanupAudioSessionForRecordingWithEvent:completion:"
+ "_cleanupStreamInfo"
+ "_computeMessageHash"
+ "_configuration"
+ "_consumePackets:completion:"
+ "_convertChunksToOpus:"
+ "_currentOutgoingStreamIndex"
+ "_data"
+ "_didDetectPostVTSilence"
+ "_didReceiveAudioChunks:"
+ "_didStartStreamingWithInfo:"
+ "_didStopConsumingForRequestId:withError:"
+ "_didStopStreamingWithError:"
+ "_didTRPArrivalTimeout"
+ "_duration"
+ "_eventName:"
+ "_flushConversionBufferIfNecessary"
+ "_formatIsSupported:"
+ "_forwardInitialSpeechUpdate"
+ "_handleDidCompleteMediaControlEvent:completion:"
+ "_handleDidCompletePhoneCallEvent:completion:"
+ "_handleDidCompleteRecordingEvent:completion:"
+ "_handleMediaControlEvent:completion:"
+ "_handlePhoneCallEvent:completion:"
+ "_handleRecordingEvent:completion:"
+ "_handleWillStartMediaControlEvent:completion:"
+ "_handleWillStartPhoneCallEvent:completion:"
+ "_handleWillStartRecordingEvent:completion:"
+ "_hasStartedEncodingPaackets"
+ "_hostTime"
+ "_incomingAudioChunks"
+ "_incomingStreamInfo"
+ "_index"
+ "_interruptionHandler:"
+ "_invalidationHandler:"
+ "_isConsumingStream"
+ "_isFloat"
+ "_isInvocationUser"
+ "_isManualMode"
+ "_isProvidingStream"
+ "_isSameUser"
+ "_lastTRPCandidateId"
+ "_logger"
+ "_longFormSpeechEventThresholdMet"
+ "_maxSpeechEventThresholdMet"
+ "_messageHash"
+ "_minSpeechEventThresholdMet"
+ "_mitigationTrailingSilenceThresholdMet"
+ "_noSpeechTokensDetectedInRequest"
+ "_noTRPArrivalThresholdMet"
+ "_notifyDelegateDidStopWithError:"
+ "_notifyDelegateOfChunks:fromFormat:toFormat:"
+ "_notifyDelegateOfFloatConvertedChunks:"
+ "_notifyDelegateOfNativeChunks:"
+ "_notifyDelegateOfShortConvertedChunks:"
+ "_notifyObserverOfSpeechDetectionEvent:"
+ "_numSamples"
+ "_opusConverter"
+ "_outgoingStreamInfo"
+ "_outputAudioFormat"
+ "_prepareAudioSessionForMediaControlWithEvent:completion:"
+ "_prepareAudioSessionForPhoneCallWithEvent:completion:"
+ "_prepareAudioSessionForRecordingWithEvent:completion:"
+ "_processedAudioDuration"
+ "_processedAudioDurationMs"
+ "_querySpeechDetectionUpdatesEventWithCompletion:"
+ "_recordRoute"
+ "_resetStreamInfo"
+ "_sampleByteDepth"
+ "_sanitizeStreamConfiguration:"
+ "_selectedTrpId"
+ "_sessionId"
+ "_setupStateMachine"
+ "_speechDetected"
+ "_startConsumingWithConfiguration:completion:"
+ "_startSampleCount"
+ "_startStreaming:"
+ "_stateMachine"
+ "_stateName:"
+ "_stopAudioCaptureWithReason:requestId:"
+ "_stopConsumingWithCompletion:"
+ "_stopError"
+ "_stopStreaming"
+ "_streamConfiguration"
+ "_streamConsumerDelegate"
+ "_streamId"
+ "_streamInfo"
+ "_streamProviderDelegate"
+ "_timestamp"
+ "_trailingSilenceDurationMs"
+ "_trpId"
+ "_turnEndReason"
+ "actionType"
+ "addEntriesFromDictionary:"
+ "addObject:"
+ "addSamples:timestamp:arrivalTimestampToAudioRecorder:"
+ "addTransitionFrom:to:for:"
+ "addTransitionFromAnyStateTo:for:"
+ "allocWithZone:"
+ "arrivalHostTimeToAudioRecorder"
+ "audioConverterDidConvertPackets:packets:durationInSec:timestamp:arrivalTimestampToAudioRecorder:"
+ "audioFormat"
+ "audioMessageClient"
+ "audioStreamConsumer:didStopWithError:"
+ "audioStreamProvider:didStartWithInfo:"
+ "audioStreamProvider:didStopWithError:"
+ "audioStreamProvider:receivedPackets:"
+ "build"
+ "builder"
+ "bundleId"
+ "chunks"
+ "com.apple.corespeech.localspeechrecognitionbridge"
+ "com.apple.siri.audio.stream.consumer.service.xpc"
+ "com.apple.siri.audio.stream.provider.service.xpc"
+ "configuration"
+ "consumePackets:completion:"
+ "consumePackets:forRequestId:completion:"
+ "containerURLForSecurityApplicationGroupIdentifier:"
+ "convertAudioFromURL:toURL:format:completion:"
+ "convertToFloatLPCMBufFromShortLPCMBuf:"
+ "convertToShortLPCMBufFromFloatLPCMBuf:"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "currentOutgoingStreamIndex"
+ "currentState"
+ "data"
+ "date"
+ "decodeArrayOfObjectsOfClass:forKey:"
+ "decodeBoolForKey:"
+ "decodeIntegerForKey:"
+ "defaultManager"
+ "dictionaryWithObjects:forKeys:count:"
+ "didDetectPostVTSilence"
+ "didIgnoreEvent:from:"
+ "didReceiveAudioChunks:"
+ "didStartStreamingWithInfo:"
+ "didStopConsumingForRequestId:withError:"
+ "didStopStreamingWithError:"
+ "didTRPArrivalTimeout"
+ "didTransitFrom:to:by:"
+ "disableAttendingForRootRequestId:"
+ "dismissForRequestId:"
+ "duration"
+ "encodeBool:forKey:"
+ "encodeInteger:forKey:"
+ "errorWithCode:"
+ "errorWithCode:localizedDescription:"
+ "errorWithCode:userInfo:"
+ "fileExistsAtPath:"
+ "flush"
+ "getAudioFileURLWithCompletion:"
+ "getAudioFileWithRequestId:completion:"
+ "hasStartedEncodingPaackets"
+ "hostTime"
+ "incomingAudioChunks"
+ "incomingStreamInfo"
+ "index"
+ "informAudioSessionEvent:completion:"
+ "initWithActionType:"
+ "initWithActionType:bundleId:"
+ "initWithActionType:timestamp:"
+ "initWithActionType:timestamp:bundleId:"
+ "initWithAudioCaptureStartHostTime:outputAudioFormat:audioRecordType:audioRecordDeviceId:"
+ "initWithAudioRecordType:audioRecordDeviceId:recordRoute:audioFormat:streamIdentifier:"
+ "initWithBuilder:"
+ "initWithCapacity:"
+ "initWithChunks:duration:"
+ "initWithChunks:duration:index:"
+ "initWithChunks:index:"
+ "initWithChunks:startSampleCount:numSamples:"
+ "initWithData:numSamples:sampleByteDepth:startSampleCount:hostTime:arrivalHostTimeToAudioRecorder:isFloat:"
+ "initWithDelegate:xpcListenerEndpoint:"
+ "initWithInitialState:"
+ "initWithLastTRPCandidateId:speechDetected:isSameUser:isInvocationUser:didDetectPostVTSilence:didTRPArrivalTimeout:noSpeechTokensDetectedInRequest:minSpeechEventThresholdMet:longFormSpeechEventThresholdMet:maxSpeechEventThresholdMet:noTRPArrivalThresholdMet:mitigationTrailingSilenceThresholdMet:isManualMode:processedAudioDurationMs:"
+ "initWithRequestId:"
+ "initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:asrLocale:activeUserInfo:messagesContext:sessionId:"
+ "initWithRequestId:selectedTrpId:"
+ "initWithRequestId:selectedTrpId:turnEndReason:processedAudioDuration:trailingSilenceDurationMs:"
+ "initWithRequestId:streamInfo:"
+ "initWithRequestId:trpId:turnEndReason:processedAudioDuration:trailingSilenceDurationMs:"
+ "initWithUpdates:"
+ "isAudioStreamConsumingEnabled"
+ "isAudioStreamProvidingEnabled"
+ "isConsumingStream"
+ "isFloat"
+ "isInvocationUser"
+ "isManualMode"
+ "isProvidingStream"
+ "isSameUser"
+ "lastTRPCandidateId"
+ "linkItemAtURL:toURL:error:"
+ "localSpeechRecognition connection interrupted"
+ "localSpeechRecognition connection invalidated"
+ "localSpeechRecognizerClient:receivedSpeechDetectionEvent:"
+ "localSpeechRecognizerClient:receivedSpeechDetectionUpdate:"
+ "localSpeechServiceDidReceiveSpeechDetectionEvent:"
+ "localSpeechServiceDidReceiveSpeechDetectionUpdate:"
+ "localizedDescriptionForCode:"
+ "logger"
+ "loggingHeartbeatRate"
+ "longFormSpeechEventThresholdMet"
+ "maxSpeechEventThresholdMet"
+ "messageHash"
+ "minSpeechEventThresholdMet"
+ "mitigationTrailingSilenceThresholdMet"
+ "noSpeechTokensDetectedInRequest"
+ "noTRPArrivalThresholdMet"
+ "numSamples"
+ "objectForKey:"
+ "opusConverter"
+ "outgoingStreamInfo"
+ "outputAudioFormat"
+ "path"
+ "performTransitionForEvent:"
+ "processedAudioDuration"
+ "processedAudioDurationMs"
+ "querySpeechDetectionUpdatesEventWithCompletion:"
+ "reason"
+ "recordRoute"
+ "releaseAudioMessageRetainLockFromRequestId:"
+ "requestingSpeechDetectionNotificationAfter:forRequest:withTrpId:"
+ "reset"
+ "sampleByteDepth"
+ "selectedTrpId"
+ "sessionId"
+ "setAudioCaptureStartHostTime:"
+ "setAudioFormat:"
+ "setAudioMessageClient:"
+ "setAudioRecordDeviceId:"
+ "setAudioRecordType:"
+ "setChunks:"
+ "setConfiguration:"
+ "setConsumingDelegate:"
+ "setCurrentOutgoingStreamIndex:"
+ "setDidDetectPostVTSilence:"
+ "setDidTRPArrivalTimeout:"
+ "setDuration:"
+ "setEventTime:"
+ "setEventType:"
+ "setHasStartedEncodingPaackets:"
+ "setHostTime:"
+ "setIncomingAudioChunks:"
+ "setIncomingStreamInfo:"
+ "setIndex:"
+ "setInterface:forSelector:argumentIndex:ofReply:"
+ "setIsInvocationUser:"
+ "setIsManualMode:"
+ "setIsProvidingStream:"
+ "setIsSameUser:"
+ "setLastTRPCandidateId:"
+ "setLogger:"
+ "setLongFormSpeechEventThresholdMet:"
+ "setMaxSpeechEventThresholdMet:"
+ "setMinSpeechEventThresholdMet:"
+ "setMitigationTrailingSilenceThresholdMet:"
+ "setNoSpeechTokensDetectedInRequest:"
+ "setNoTRPArrivalThresholdMet:"
+ "setObject:forKey:"
+ "setOpusConverter:"
+ "setOutgoingStreamInfo:"
+ "setOutputAudioFormat:"
+ "setProcessedAudioDurationMs:"
+ "setRecordRoute:"
+ "setSpeechDetected:"
+ "setStateMachine:"
+ "setStopError:"
+ "setStreamConfiguration:"
+ "setStreamConsumerDelegate:"
+ "setStreamInfo:"
+ "setStreamProviderDelegate:"
+ "setStreamingDelegate:"
+ "setXpcListenerEndpoint:"
+ "speechDetected"
+ "startConsumingWithConfiguration:completion:"
+ "startSampleCount"
+ "startStreaming:"
+ "startStreamingWithDelegate:timestamp:"
+ "stateMachine"
+ "stopConsumingForRequestId:completion:"
+ "stopConsumingWithCompletion:"
+ "stopError"
+ "stopStreaming"
+ "streamConfiguration"
+ "streamConsumerDelegate"
+ "streamId"
+ "streamInfo"
+ "streamProviderDelegate"
+ "stringWithFormat:"
+ "timestamp"
+ "toBuilder"
+ "trailingSilenceDurationMs"
+ "trpId"
+ "turnEndReason"
+ "turnEndReasonString:"
+ "turnEndedForRequestId:withTrpId:"
+ "turnEndedwithContext:"
+ "unknown"
+ "unknown(%tu)"
+ "v16@?0@\"<AFAudioSessionEventMutating>\"8"
+ "v16@?0@\"NSURL\"8"
+ "v24@0:8@\"<LBAudioStreamConsumingDelegate>\"16"
+ "v24@0:8@\"<LBAudioStreamProvidingDelegate>\"16"
+ "v24@0:8@\"LBAudioStreamConfiguration\"16"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v24@0:8d16"
+ "v24@0:8q16"
+ "v24@?0@\"LBLocalSpeechDetectionUpdates\"8@\"NSError\"16"
+ "v24@?0@\"NSString\"8@\"NSURL\"16"
+ "v32@0:8@\"LBAudioStreamConsumerConfiguration\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"NSArray\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@16@?24"
+ "v32@0:8q16q24"
+ "v40@0:8@16q24@?32"
+ "v40@0:8@16q24q32"
+ "v40@0:8d16@24@32"
+ "v40@0:8q16q24q32"
+ "v48@0:8@16@24q32@?40"
+ "v52@0:8@\"CSFAudioConverter\"16@\"NSArray\"24f32Q36Q44"
+ "v52@0:8@16@24f32Q36Q44"
+ "writeAudioFileToURL:audioFormat:completion:"
+ "xpcListenerEndpoint"
- "::: Initializing LocalSRBridge logging..."
- "CSRecordTypeSpeechEventConverter"
- "getRecordTypeForSpeechEvent:"
- "q24@0:8q16"

```
