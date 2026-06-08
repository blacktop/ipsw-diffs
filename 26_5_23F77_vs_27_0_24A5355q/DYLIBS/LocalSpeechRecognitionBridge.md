## LocalSpeechRecognitionBridge

> `/System/Library/PrivateFrameworks/LocalSpeechRecognitionBridge.framework/LocalSpeechRecognitionBridge`

```diff

-3525.5.8.0.0
-  __TEXT.__text: 0x19140
-  __TEXT.__auth_stubs: 0x490
-  __TEXT.__objc_methlist: 0x1cc4
+3600.64.114.1.5
+  __TEXT.__text: 0x1b618
+  __TEXT.__objc_methlist: 0x23fc
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x27c
-  __TEXT.__oslogstring: 0x2005
-  __TEXT.__cstring: 0x3a2c
-  __TEXT.__unwind_info: 0x620
-  __TEXT.__objc_classname: 0x3dd
-  __TEXT.__objc_methname: 0x7167
-  __TEXT.__objc_methtype: 0x16e6
-  __TEXT.__objc_stubs: 0x2740
-  __DATA_CONST.__got: 0x1d0
-  __DATA_CONST.__const: 0x628
-  __DATA_CONST.__objc_classlist: 0xa8
-  __DATA_CONST.__objc_protolist: 0x88
+  __TEXT.__const: 0xa0
+  __TEXT.__gcc_except_tab: 0x1d0
+  __TEXT.__cstring: 0x4515
+  __TEXT.__oslogstring: 0x2617
+  __TEXT.__unwind_info: 0x6a0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x6d8
+  __DATA_CONST.__objc_classlist: 0xe0
+  __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfc0
-  __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA_CONST.__objc_selrefs: 0x1278
+  __DATA_CONST.__objc_protorefs: 0x58
+  __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x258
+  __DATA_CONST.__got: 0x1e8
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x1680
-  __AUTH_CONST.__objc_const: 0x2f38
+  __AUTH_CONST.__cfstring: 0x1940
+  __AUTH_CONST.__objc_const: 0x3c40
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x460
-  __DATA.__objc_ivar: 0x238
-  __DATA.__data: 0x670
-  __DATA.__bss: 0x18
-  __DATA_DIRTY.__objc_data: 0x230
-  __DATA_DIRTY.__bss: 0x40
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x5a0
+  __DATA.__objc_ivar: 0x2b8
+  __DATA.__data: 0x8b0
+  __DATA.__bss: 0x10
+  __DATA_DIRTY.__objc_data: 0x320
+  __DATA_DIRTY.__bss: 0x48
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2903E33E-B17E-3D3E-9F0D-3E1AF2BECFEA
-  Functions: 565
-  Symbols:   2035
-  CStrings:  1605
+  UUID: 6BE37CE9-9DE0-3BD2-B54E-0C4D7370E931
+  Functions: 708
+  Symbols:   2505
+  CStrings:  766
 
Symbols:
+ +[LBLocalSpeechRecognizerTurnFinalizedContext supportsSecureCoding]
+ +[LBLocalSpeechRecognizerTurnStartContext supportsSecureCoding]
+ +[LBOutputStreamConsumerConfiguration supportsSecureCoding]
+ +[LBSpeakerChangeEvent supportsSecureCoding]
+ -[LBAudioCapture startAudioCaptureWithRecordContext:startHostTime:siriSessionUUID:isLinwoodEnabled:completion:]
+ -[LBAudioStreamConsumer updateManualModeEnabled:]
+ -[LBAudioStreamConsumer updateStoppingWithHTTMode:]
+ -[LBAudioStreamInfo initWithAudioRecordType:audioRecordDeviceId:recordRoute:audioFormat:streamIdentifier:originatingDeviceType:]
+ -[LBAudioStreamInfo originatingDeviceType]
+ -[LBAudioStreamInfo setOriginatingDeviceType:]
+ -[LBAudioStreamProvider _didReceiveManualModeEnabled:]
+ -[LBAudioStreamProvider _didReceiveStoppingWithHTTMode:]
+ -[LBAudioStreamProvider _willStartStreaming]
+ -[LBAudioStreamProvider didReceiveManualModeEnabled:]
+ -[LBAudioStreamProvider didReceiveStoppingWithHTTMode:]
+ -[LBAudioStreamProvider willStartStreaming]
+ -[LBConversationalInteraction .cxx_destruct]
+ -[LBConversationalInteraction _invalidate]
+ -[LBConversationalInteraction _newOutputStreamPlayingConnection]
+ -[LBConversationalInteraction _newStreamProvidingConnection]
+ -[LBConversationalInteraction _newTurnConsumingConnection]
+ -[LBConversationalInteraction _outputStreamPlayerService]
+ -[LBConversationalInteraction _outputStreamPlayingConnection]
+ -[LBConversationalInteraction _startStreaming:]
+ -[LBConversationalInteraction _streamProvidingConnection]
+ -[LBConversationalInteraction _streamProvidingService]
+ -[LBConversationalInteraction _turnConsumingConnection]
+ -[LBConversationalInteraction _turnConsumingService]
+ -[LBConversationalInteraction addAudioChunk:to:]
+ -[LBConversationalInteraction currentStreamState]
+ -[LBConversationalInteraction dealloc]
+ -[LBConversationalInteraction didConfirmUserTurn:]
+ -[LBConversationalInteraction didReceiveAudioChunks:]
+ -[LBConversationalInteraction didStartStreamingWithInfo:]
+ -[LBConversationalInteraction didStopStreamingWithError:]
+ -[LBConversationalInteraction endAudioTo:]
+ -[LBConversationalInteraction informUserTurnBeginAt:]
+ -[LBConversationalInteraction informUserTurnEndAt:]
+ -[LBConversationalInteraction init]
+ -[LBConversationalInteraction invalidate]
+ -[LBConversationalInteraction isProvidingStream]
+ -[LBConversationalInteraction outputStreamPlayingConnection]
+ -[LBConversationalInteraction outputStreamPlayingQueue]
+ -[LBConversationalInteraction playbackStream:completion:]
+ -[LBConversationalInteraction requestOutputStream:completion:]
+ -[LBConversationalInteraction setCurrentStreamState:]
+ -[LBConversationalInteraction setOutputStreamPlayingConnection:]
+ -[LBConversationalInteraction setOutputStreamPlayingQueue:]
+ -[LBConversationalInteraction setStreamConsumingQueue:]
+ -[LBConversationalInteraction setStreamProviderDelegate:]
+ -[LBConversationalInteraction setStreamProvidingConnection:]
+ -[LBConversationalInteraction setStreamProvidingQueue:]
+ -[LBConversationalInteraction setStreamStateMachine:]
+ -[LBConversationalInteraction setTurnConfirmationDelegate:]
+ -[LBConversationalInteraction setTurnConsumingConnection:]
+ -[LBConversationalInteraction setTurnConsumingQueue:]
+ -[LBConversationalInteraction startStreaming:]
+ -[LBConversationalInteraction stopPlaying]
+ -[LBConversationalInteraction stopStreaming]
+ -[LBConversationalInteraction streamConsumingQueue]
+ -[LBConversationalInteraction streamProviderDelegate]
+ -[LBConversationalInteraction streamProvidingConnection]
+ -[LBConversationalInteraction streamProvidingQueue]
+ -[LBConversationalInteraction streamStateMachine]
+ -[LBConversationalInteraction turnConfirmationDelegate]
+ -[LBConversationalInteraction turnConsumingConnection]
+ -[LBConversationalInteraction turnConsumingQueue]
+ -[LBLocalSpeechDetectionUpdates initWithLastTRPCandidateId:speechDetected:isSameUser:isInvocationUser:didDetectPostVTSilence:didTRPArrivalTimeout:noSpeechTokensDetectedInRequest:minSpeechEventThresholdMet:longFormSpeechEventThresholdMet:maxSpeechEventThresholdMet:noTRPArrivalThresholdMet:mitigationTrailingSilenceThresholdMet:isManualMode:isRequestSampledForCollisionDetection:processedAudioDurationMs:]
+ -[LBLocalSpeechDetectionUpdates isRequestSampledForCollisionDetection]
+ -[LBLocalSpeechDetectionUpdatesBuilder setIsRequestSampledForCollisionDetection:]
+ -[LBLocalSpeechRecognitionSettings initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:asrLocale:activeUserInfo:messagesContext:sessionId:isLinwoodEnabled:]
+ -[LBLocalSpeechRecognitionSettings isLinwoodEnabled]
+ -[LBLocalSpeechRecognizerClient turnFinalizedwithContext:]
+ -[LBLocalSpeechRecognizerClient turnStartedwithContext:]
+ -[LBLocalSpeechRecognizerTurnEndContext initWithRequestId:selectedTrpId:turnEndReason:processedAudioDuration:trailingSilenceDurationMs:runtimeType:]
+ -[LBLocalSpeechRecognizerTurnEndContext runtimeType]
+ -[LBLocalSpeechRecognizerTurnFinalizedContext .cxx_destruct]
+ -[LBLocalSpeechRecognizerTurnFinalizedContext copyWithZone:]
+ -[LBLocalSpeechRecognizerTurnFinalizedContext description]
+ -[LBLocalSpeechRecognizerTurnFinalizedContext encodeWithCoder:]
+ -[LBLocalSpeechRecognizerTurnFinalizedContext initWithCoder:]
+ -[LBLocalSpeechRecognizerTurnFinalizedContext initWithRequestId:selectedTrpId:runtimeType:selectedRuntime:]
+ -[LBLocalSpeechRecognizerTurnFinalizedContext requestId]
+ -[LBLocalSpeechRecognizerTurnFinalizedContext runtimeType]
+ -[LBLocalSpeechRecognizerTurnFinalizedContext selectedRuntime]
+ -[LBLocalSpeechRecognizerTurnFinalizedContext selectedTrpId]
+ -[LBLocalSpeechRecognizerTurnStartContext .cxx_destruct]
+ -[LBLocalSpeechRecognizerTurnStartContext attendingModePreference]
+ -[LBLocalSpeechRecognizerTurnStartContext copyWithZone:]
+ -[LBLocalSpeechRecognizerTurnStartContext description]
+ -[LBLocalSpeechRecognizerTurnStartContext encodeWithCoder:]
+ -[LBLocalSpeechRecognizerTurnStartContext initWithCoder:]
+ -[LBLocalSpeechRecognizerTurnStartContext initWithRequestId:selectedTrpId:runtimeType:attendingModePreference:]
+ -[LBLocalSpeechRecognizerTurnStartContext requestId]
+ -[LBLocalSpeechRecognizerTurnStartContext runtimeType]
+ -[LBLocalSpeechRecognizerTurnStartContext selectedTrpId]
+ -[LBOutputStream .cxx_destruct]
+ -[LBOutputStream addAudioChunk:]
+ -[LBOutputStream endAudio]
+ -[LBOutputStream initWithStreamIdentifier:streamConsumer:]
+ -[LBOutputStream setStreamConsumer:]
+ -[LBOutputStream streamConsumer]
+ -[LBOutputStream streamIdentifier]
+ -[LBOutputStreamConsumerConfiguration encodeWithCoder:]
+ -[LBOutputStreamConsumerConfiguration initWithCoder:]
+ -[LBOutputStreamConsumerConfiguration initWithOutputStreamType:outputStreamFormat:outputStreamSampleRate:outputBufferDuration:]
+ -[LBOutputStreamConsumerConfiguration outputBufferDuration]
+ -[LBOutputStreamConsumerConfiguration outputStreamFormat]
+ -[LBOutputStreamConsumerConfiguration outputStreamSampleRate]
+ -[LBOutputStreamConsumerConfiguration outputStreamType]
+ -[LBSpeakerChangeEvent changeTime]
+ -[LBSpeakerChangeEvent encodeWithCoder:]
+ -[LBSpeakerChangeEvent initWithCoder:]
+ -[LBSpeakerChangeEvent initWithSpeakerChangeTime:]
+ GCC_except_table163
+ GCC_except_table308
+ GCC_except_table42
+ GCC_except_table427
+ GCC_except_table431
+ GCC_except_table438
+ GCC_except_table517
+ GCC_except_table631
+ GCC_except_table666
+ GCC_except_table671
+ GCC_except_table676
+ _LBOutputStreamPlayerServiceGetXPCInterface
+ _LBOutputStreamPlayerServiceName
+ _LBTurnInformationConsumerServiceDelegateGetXPCInterface
+ _LBTurnInformationConsumerServiceGetXPCInterface
+ _LBTurnInformationConsumerServiceName
+ _OBJC_CLASS_$_LBConversationalInteraction
+ _OBJC_CLASS_$_LBConversationalInteractionService
+ _OBJC_CLASS_$_LBLocalSpeechRecognizerTurnFinalizedContext
+ _OBJC_CLASS_$_LBLocalSpeechRecognizerTurnStartContext
+ _OBJC_CLASS_$_LBOutputStream
+ _OBJC_CLASS_$_LBOutputStreamConsumerConfiguration
+ _OBJC_CLASS_$_LBSpeakerChangeEvent
+ _OBJC_IVAR_$_LBAudioStreamInfo._originatingDeviceType
+ _OBJC_IVAR_$_LBConversationalInteraction._currentStreamState
+ _OBJC_IVAR_$_LBConversationalInteraction._outputStreamPlayingConnection
+ _OBJC_IVAR_$_LBConversationalInteraction._outputStreamPlayingQueue
+ _OBJC_IVAR_$_LBConversationalInteraction._streamConsumingQueue
+ _OBJC_IVAR_$_LBConversationalInteraction._streamProvidingConnection
+ _OBJC_IVAR_$_LBConversationalInteraction._streamProvidingQueue
+ _OBJC_IVAR_$_LBConversationalInteraction._streamStateMachine
+ _OBJC_IVAR_$_LBConversationalInteraction._turnConsumingConnection
+ _OBJC_IVAR_$_LBConversationalInteraction._turnConsumingQueue
+ _OBJC_IVAR_$_LBConversationalInteraction.isProvidingStream
+ _OBJC_IVAR_$_LBConversationalInteraction.streamProviderDelegate
+ _OBJC_IVAR_$_LBConversationalInteraction.turnConfirmationDelegate
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdates._isRequestSampledForCollisionDetection
+ _OBJC_IVAR_$_LBLocalSpeechDetectionUpdatesBuilder._isRequestSampledForCollisionDetection
+ _OBJC_IVAR_$_LBLocalSpeechRecognitionSettings._isLinwoodEnabled
+ _OBJC_IVAR_$_LBLocalSpeechRecognizerTurnEndContext._runtimeType
+ _OBJC_IVAR_$_LBLocalSpeechRecognizerTurnFinalizedContext._requestId
+ _OBJC_IVAR_$_LBLocalSpeechRecognizerTurnFinalizedContext._runtimeType
+ _OBJC_IVAR_$_LBLocalSpeechRecognizerTurnFinalizedContext._selectedRuntime
+ _OBJC_IVAR_$_LBLocalSpeechRecognizerTurnFinalizedContext._selectedTrpId
+ _OBJC_IVAR_$_LBLocalSpeechRecognizerTurnStartContext._attendingModePreference
+ _OBJC_IVAR_$_LBLocalSpeechRecognizerTurnStartContext._requestId
+ _OBJC_IVAR_$_LBLocalSpeechRecognizerTurnStartContext._runtimeType
+ _OBJC_IVAR_$_LBLocalSpeechRecognizerTurnStartContext._selectedTrpId
+ _OBJC_IVAR_$_LBOutputStream._streamConsumer
+ _OBJC_IVAR_$_LBOutputStream._streamIdentifier
+ _OBJC_IVAR_$_LBOutputStreamConsumerConfiguration._outputBufferDuration
+ _OBJC_IVAR_$_LBOutputStreamConsumerConfiguration._outputStreamFormat
+ _OBJC_IVAR_$_LBOutputStreamConsumerConfiguration._outputStreamSampleRate
+ _OBJC_IVAR_$_LBOutputStreamConsumerConfiguration._outputStreamType
+ _OBJC_IVAR_$_LBSpeakerChangeEvent._changeTime
+ _OBJC_METACLASS_$_LBConversationalInteraction
+ _OBJC_METACLASS_$_LBConversationalInteractionService
+ _OBJC_METACLASS_$_LBLocalSpeechRecognizerTurnFinalizedContext
+ _OBJC_METACLASS_$_LBLocalSpeechRecognizerTurnStartContext
+ _OBJC_METACLASS_$_LBOutputStream
+ _OBJC_METACLASS_$_LBOutputStreamConsumerConfiguration
+ _OBJC_METACLASS_$_LBSpeakerChangeEvent
+ __OBJC_$_CLASS_METHODS_LBLocalSpeechRecognizerTurnFinalizedContext
+ __OBJC_$_CLASS_METHODS_LBLocalSpeechRecognizerTurnStartContext
+ __OBJC_$_CLASS_METHODS_LBOutputStreamConsumerConfiguration
+ __OBJC_$_CLASS_METHODS_LBSpeakerChangeEvent
+ __OBJC_$_CLASS_PROP_LIST_LBLocalSpeechRecognizerTurnFinalizedContext
+ __OBJC_$_CLASS_PROP_LIST_LBLocalSpeechRecognizerTurnStartContext
+ __OBJC_$_CLASS_PROP_LIST_LBOutputStreamConsumerConfiguration
+ __OBJC_$_CLASS_PROP_LIST_LBSpeakerChangeEvent
+ __OBJC_$_INSTANCE_METHODS_LBConversationalInteraction
+ __OBJC_$_INSTANCE_METHODS_LBLocalSpeechRecognizerTurnFinalizedContext
+ __OBJC_$_INSTANCE_METHODS_LBLocalSpeechRecognizerTurnStartContext
+ __OBJC_$_INSTANCE_METHODS_LBOutputStream
+ __OBJC_$_INSTANCE_METHODS_LBOutputStreamConsumerConfiguration
+ __OBJC_$_INSTANCE_METHODS_LBSpeakerChangeEvent
+ __OBJC_$_INSTANCE_VARIABLES_LBConversationalInteraction
+ __OBJC_$_INSTANCE_VARIABLES_LBLocalSpeechRecognizerTurnFinalizedContext
+ __OBJC_$_INSTANCE_VARIABLES_LBLocalSpeechRecognizerTurnStartContext
+ __OBJC_$_INSTANCE_VARIABLES_LBOutputStream
+ __OBJC_$_INSTANCE_VARIABLES_LBOutputStreamConsumerConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_LBSpeakerChangeEvent
+ __OBJC_$_PROP_LIST_LBConversationalInteraction
+ __OBJC_$_PROP_LIST_LBLocalSpeechRecognizerTurnFinalizedContext
+ __OBJC_$_PROP_LIST_LBLocalSpeechRecognizerTurnStartContext
+ __OBJC_$_PROP_LIST_LBOutputStream
+ __OBJC_$_PROP_LIST_LBOutputStreamConsumerConfiguration
+ __OBJC_$_PROP_LIST_LBSpeakerChangeEvent
+ __OBJC_$_PROP_LIST_LBTurnInformationConsuming
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LBOutputStreamConsuming
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LBOutputStreamPlayerService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LBOutputStreamPlaying
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LBTurnInformationConsumerService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LBTurnInformationConsumerServiceDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LBTurnInformationConsuming
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LBOutputStreamConsuming
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LBOutputStreamPlayerService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LBOutputStreamPlaying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LBTurnInformationConsumerService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LBTurnInformationConsumerServiceDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LBTurnInformationConsuming
+ __OBJC_$_PROTOCOL_REFS_LBOutputStreamConsuming
+ __OBJC_$_PROTOCOL_REFS_LBOutputStreamPlayerService
+ __OBJC_$_PROTOCOL_REFS_LBOutputStreamPlaying
+ __OBJC_$_PROTOCOL_REFS_LBTurnInformationConsumerService
+ __OBJC_$_PROTOCOL_REFS_LBTurnInformationConsumerServiceDelegate
+ __OBJC_$_PROTOCOL_REFS_LBTurnInformationConsuming
+ __OBJC_CLASS_PROTOCOLS_$_LBConversationalInteraction
+ __OBJC_CLASS_PROTOCOLS_$_LBLocalSpeechRecognizerTurnFinalizedContext
+ __OBJC_CLASS_PROTOCOLS_$_LBLocalSpeechRecognizerTurnStartContext
+ __OBJC_CLASS_PROTOCOLS_$_LBOutputStreamConsumerConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_LBSpeakerChangeEvent
+ __OBJC_CLASS_RO_$_LBConversationalInteraction
+ __OBJC_CLASS_RO_$_LBConversationalInteractionService
+ __OBJC_CLASS_RO_$_LBLocalSpeechRecognizerTurnFinalizedContext
+ __OBJC_CLASS_RO_$_LBLocalSpeechRecognizerTurnStartContext
+ __OBJC_CLASS_RO_$_LBOutputStream
+ __OBJC_CLASS_RO_$_LBOutputStreamConsumerConfiguration
+ __OBJC_CLASS_RO_$_LBSpeakerChangeEvent
+ __OBJC_LABEL_PROTOCOL_$_LBOutputStreamConsuming
+ __OBJC_LABEL_PROTOCOL_$_LBOutputStreamPlayerService
+ __OBJC_LABEL_PROTOCOL_$_LBOutputStreamPlaying
+ __OBJC_LABEL_PROTOCOL_$_LBTurnInformationConsumerService
+ __OBJC_LABEL_PROTOCOL_$_LBTurnInformationConsumerServiceDelegate
+ __OBJC_LABEL_PROTOCOL_$_LBTurnInformationConsuming
+ __OBJC_METACLASS_RO_$_LBConversationalInteraction
+ __OBJC_METACLASS_RO_$_LBConversationalInteractionService
+ __OBJC_METACLASS_RO_$_LBLocalSpeechRecognizerTurnFinalizedContext
+ __OBJC_METACLASS_RO_$_LBLocalSpeechRecognizerTurnStartContext
+ __OBJC_METACLASS_RO_$_LBOutputStream
+ __OBJC_METACLASS_RO_$_LBOutputStreamConsumerConfiguration
+ __OBJC_METACLASS_RO_$_LBSpeakerChangeEvent
+ __OBJC_PROTOCOL_$_LBOutputStreamConsuming
+ __OBJC_PROTOCOL_$_LBOutputStreamPlayerService
+ __OBJC_PROTOCOL_$_LBOutputStreamPlaying
+ __OBJC_PROTOCOL_$_LBTurnInformationConsumerService
+ __OBJC_PROTOCOL_$_LBTurnInformationConsumerServiceDelegate
+ __OBJC_PROTOCOL_$_LBTurnInformationConsuming
+ __OBJC_PROTOCOL_REFERENCE_$_LBOutputStreamPlayerService
+ __OBJC_PROTOCOL_REFERENCE_$_LBTurnInformationConsumerService
+ __OBJC_PROTOCOL_REFERENCE_$_LBTurnInformationConsumerServiceDelegate
+ ___111-[LBAudioCapture startAudioCaptureWithRecordContext:startHostTime:siriSessionUUID:isLinwoodEnabled:completion:]_block_invoke
+ ___42-[LBConversationalInteraction endAudioTo:]_block_invoke
+ ___42-[LBConversationalInteraction stopPlaying]_block_invoke
+ ___43-[LBAudioStreamProvider willStartStreaming]_block_invoke
+ ___44-[LBConversationalInteraction stopStreaming]_block_invoke
+ ___44-[LBLocalSpeechRecognizerClient _connection]_block_invoke.411
+ ___46-[LBConversationalInteraction startStreaming:]_block_invoke
+ ___48-[LBConversationalInteraction addAudioChunk:to:]_block_invoke
+ ___49-[LBAudioStreamConsumer updateManualModeEnabled:]_block_invoke
+ ___51-[LBAudioStreamConsumer updateStoppingWithHTTMode:]_block_invoke
+ ___51-[LBConversationalInteraction informUserTurnEndAt:]_block_invoke
+ ___53-[LBAudioStreamProvider didReceiveManualModeEnabled:]_block_invoke
+ ___53-[LBConversationalInteraction informUserTurnBeginAt:]_block_invoke
+ ___55-[LBAudioStreamProvider didReceiveStoppingWithHTTMode:]_block_invoke
+ ___55-[LBConversationalInteraction _turnConsumingConnection]_block_invoke
+ ___55-[LBConversationalInteraction _turnConsumingConnection]_block_invoke.11
+ ___56-[LBLocalSpeechRecognizerClient turnStartedwithContext:]_block_invoke
+ ___57-[LBConversationalInteraction _streamProvidingConnection]_block_invoke
+ ___57-[LBConversationalInteraction _streamProvidingConnection]_block_invoke.14
+ ___57-[LBConversationalInteraction playbackStream:completion:]_block_invoke
+ ___58-[LBLocalSpeechRecognizerClient turnFinalizedwithContext:]_block_invoke
+ ___61-[LBConversationalInteraction _outputStreamPlayingConnection]_block_invoke
+ ___61-[LBConversationalInteraction _outputStreamPlayingConnection]_block_invoke.13
+ ___62-[LBConversationalInteraction requestOutputStream:completion:]_block_invoke
+ ___62-[LBConversationalInteraction requestOutputStream:completion:]_block_invoke_2
+ ___75-[LBLocalSpeechRecognizerClient startSpeechRecognitionResultsWithSettings:]_block_invoke.359
+ ___81-[LBLocalSpeechRecognizerClient _querySpeechDetectionUpdatesEventWithCompletion:]_block_invoke
+ ___block_descriptor_41_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32s40bs_e28_v24?0"NSUUID"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_literal_global.2021
+ _getCSXPCClientClass
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_didReceiveManualModeEnabled:
+ _objc_msgSend$_didReceiveStoppingWithHTTMode:
+ _objc_msgSend$_newOutputStreamPlayingConnection
+ _objc_msgSend$_newStreamProvidingConnection
+ _objc_msgSend$_newTurnConsumingConnection
+ _objc_msgSend$_outputStreamPlayerService
+ _objc_msgSend$_outputStreamPlayingConnection
+ _objc_msgSend$_streamProvidingConnection
+ _objc_msgSend$_streamProvidingService
+ _objc_msgSend$_turnConsumingConnection
+ _objc_msgSend$_turnConsumingService
+ _objc_msgSend$_willStartStreaming
+ _objc_msgSend$addAudioChunk:to:
+ _objc_msgSend$addChunk:to:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$audioStreamProvider:didReceiveManualModeEnabled:
+ _objc_msgSend$audioStreamProvider:didReceiveStoppingWithHTTMode:
+ _objc_msgSend$decodeDoubleForKey:
+ _objc_msgSend$encodeDouble:forKey:
+ _objc_msgSend$endAudioTo:
+ _objc_msgSend$endStreamTo:
+ _objc_msgSend$informTurnBeginAt:
+ _objc_msgSend$informTurnEndAt:
+ _objc_msgSend$initWithAudioRecordType:audioRecordDeviceId:recordRoute:audioFormat:streamIdentifier:originatingDeviceType:
+ _objc_msgSend$initWithLastTRPCandidateId:speechDetected:isSameUser:isInvocationUser:didDetectPostVTSilence:didTRPArrivalTimeout:noSpeechTokensDetectedInRequest:minSpeechEventThresholdMet:longFormSpeechEventThresholdMet:maxSpeechEventThresholdMet:noTRPArrivalThresholdMet:mitigationTrailingSilenceThresholdMet:isManualMode:isRequestSampledForCollisionDetection:processedAudioDurationMs:
+ _objc_msgSend$initWithOutputStreamType:outputStreamFormat:outputStreamSampleRate:outputBufferDuration:
+ _objc_msgSend$initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:asrLocale:activeUserInfo:messagesContext:sessionId:isLinwoodEnabled:
+ _objc_msgSend$initWithRequestId:selectedTrpId:runtimeType:attendingModePreference:
+ _objc_msgSend$initWithRequestId:selectedTrpId:runtimeType:selectedRuntime:
+ _objc_msgSend$initWithRequestId:selectedTrpId:turnEndReason:processedAudioDuration:trailingSilenceDurationMs:runtimeType:
+ _objc_msgSend$initWithSpeakerChangeTime:
+ _objc_msgSend$initWithStreamIdentifier:streamConsumer:
+ _objc_msgSend$isLinwoodEnabled
+ _objc_msgSend$isRequestSampledForCollisionDetection
+ _objc_msgSend$playOutputStream:
+ _objc_msgSend$querySpeechDetectionUpdatesEventWithCompletion:
+ _objc_msgSend$requestOutputStream:completion:
+ _objc_msgSend$setIsLinwoodEnabled:
+ _objc_msgSend$setOriginatingDeviceType:
+ _objc_msgSend$startAudioCaptureWithRecordContext:startHostTime:siriSessionUUID:isLinwoodEnabled:completion:
+ _objc_msgSend$stopPlaying
+ _objc_msgSend$streamIdentifier
+ _objc_msgSend$streamProviderDelegate
+ _objc_msgSend$turnConfirmationDelegate
+ _objc_msgSend$turnFinalizedwithContext:
+ _objc_msgSend$turnInformationConsumer:didConfirmTurn:
+ _objc_msgSend$turnStartedwithContext:
+ _objc_msgSend$updateManualModeEnabled:
+ _objc_msgSend$updateStoppingWithHTTMode:
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x9
- GCC_except_table150
- GCC_except_table275
- GCC_except_table37
- GCC_except_table376
- GCC_except_table380
- GCC_except_table387
- GCC_except_table453
- GCC_except_table555
- ___44-[LBLocalSpeechRecognizerClient _connection]_block_invoke.390
- ___75-[LBLocalSpeechRecognizerClient startSpeechRecognitionResultsWithSettings:]_block_invoke.338
- ___block_literal_global.1562
- _objc_autorelease
- _objc_msgSend$initWithLastTRPCandidateId:speechDetected:isSameUser:isInvocationUser:didDetectPostVTSilence:didTRPArrivalTimeout:noSpeechTokensDetectedInRequest:minSpeechEventThresholdMet:longFormSpeechEventThresholdMet:maxSpeechEventThresholdMet:noTRPArrivalThresholdMet:mitigationTrailingSilenceThresholdMet:isManualMode:processedAudioDurationMs:
- _objc_msgSend$initWithRequestId:selectedTrpId:turnEndReason:processedAudioDuration:trailingSilenceDurationMs:
- _objc_msgSend$startAudioCaptureWithRecordContext:startHostTime:siriSessionUUID:completion:
CStrings:
+ "%s #output_stream Creating new xpc connection... %@"
+ "%s #output_stream Creating new xpc connection... %p"
+ "%s #output_stream resumed connection... %@"
+ "%s #output_stream xpc connection %@ Interrupted"
+ "%s #output_stream xpc connection %@ Invalidated"
+ "%s #stream forwarding manual mode update: %d"
+ "%s #stream forwarding stoppingWithHTTMode update: %d"
+ "%s #stream ignoring didStartStreamingWithInfo. current state is %{public}@ but expected WaitingToStart"
+ "%s #stream ignoring manual mode update in state: %@"
+ "%s #stream ignoring manual mode update. currently in state %{public}@"
+ "%s #stream ignoring stoppingWithHTTMode update in state: %@"
+ "%s #stream ignoring stoppingWithHTTMode update. currently in state %{public}@"
+ "%s #stream received manual mode enabled: %d"
+ "%s #stream received stoppingWithHTTMode: %d"
+ "%s #stream will start streaming"
+ "%s #turn_consuming Creating new xpc connectigon... %@"
+ "%s #turn_consuming Creating new xpc connection... %@"
+ "%s #turn_consuming resumed connection... %@"
+ "%s #turn_consuming xpc connection %@ Interrupted"
+ "%s #turn_consuming xpc connection %@ Invalidated"
+ "%s #turn_information confirm : %p"
+ "%s #turn_information userTurnBegin at: %f"
+ "%s #turn_information userTurnEnd at: %f"
+ "%s Dealloc LBConversationalInteraction"
+ "%s Failed to decode `originatingDeviceType`"
+ "%s LBLocalSpeechRecognizerClient[%@], xpcConnection[%@]:Querying speech update"
+ "%s LBLocalSpeechRecognizerClient[%@], xpcConnection[%@]:TurnFinalizedContext : %@"
+ "%s LBLocalSpeechRecognizerClient[%@], xpcConnection[%@]:TurnStartContext : %@"
+ "%s _invalidate LBConversationalInteraction"
+ "-[LBAudioCapture startAudioCaptureWithRecordContext:startHostTime:siriSessionUUID:isLinwoodEnabled:completion:]"
+ "-[LBAudioCapture startAudioCaptureWithRecordContext:startHostTime:siriSessionUUID:isLinwoodEnabled:completion:]_block_invoke"
+ "-[LBAudioStreamConsumer updateManualModeEnabled:]_block_invoke"
+ "-[LBAudioStreamConsumer updateStoppingWithHTTMode:]_block_invoke"
+ "-[LBAudioStreamProvider _didReceiveManualModeEnabled:]"
+ "-[LBAudioStreamProvider _didReceiveStoppingWithHTTMode:]"
+ "-[LBAudioStreamProvider _willStartStreaming]"
+ "-[LBConversationalInteraction _invalidate]"
+ "-[LBConversationalInteraction _newOutputStreamPlayingConnection]"
+ "-[LBConversationalInteraction _newTurnConsumingConnection]"
+ "-[LBConversationalInteraction _outputStreamPlayingConnection]"
+ "-[LBConversationalInteraction _outputStreamPlayingConnection]_block_invoke"
+ "-[LBConversationalInteraction _streamProvidingConnection]"
+ "-[LBConversationalInteraction _streamProvidingConnection]_block_invoke"
+ "-[LBConversationalInteraction _turnConsumingConnection]"
+ "-[LBConversationalInteraction _turnConsumingConnection]_block_invoke"
+ "-[LBConversationalInteraction dealloc]"
+ "-[LBConversationalInteraction didConfirmUserTurn:]"
+ "-[LBConversationalInteraction informUserTurnBeginAt:]"
+ "-[LBConversationalInteraction informUserTurnEndAt:]"
+ "-[LBLocalSpeechRecognizerClient _querySpeechDetectionUpdatesEventWithCompletion:]_block_invoke"
+ "-[LBLocalSpeechRecognizerClient turnFinalizedwithContext:]_block_invoke"
+ "-[LBLocalSpeechRecognizerClient turnStartedwithContext:]_block_invoke"
+ "<%@: %p; messageHash=%lu, lastTRPCandidateId=%@, speechDetected=%d, isSameUser=%d, isInvocationUser=%d, didDetectPostVTSilence=%d, didTRPArrivalTimeout=%d, noSpeechTokensDetectedInRequest=%d, minSpeechEventThresholdMet=%d, longFormSpeechEventThresholdMet=%d, maxSpeechEventThresholdMet=%d, noTRPArrivalThresholdMet=%d, mitigationTrailingSilenceThresholdMet=%d, isManualMode=%d, isRequestSampledForCollisionDetection=%u, processedAudioDurationMs=%ld>"
+ "<%@: %p> requestId=%@, selectedTrpId=%@, runtimeType=%lu, attendingModePreference=%lu"
+ "<%@: %p> requestId=%@, selectedTrpId=%@, runtimeType=%lu, selectedRuntime=%i"
+ "<%@: %p> requestId=%@, trpId=%@, selectedTrpId=%@, turnEndReason=%@, processedAudioDuration=%f, trailingSilenceDurationMs=%f, runtimeType=%lu"
+ "LBAudioStreamInfo:::originatingDeviceType"
+ "LBConversationalInteraction_StreamConsuming"
+ "LBConversationalInteraction_StreamPlaying"
+ "LBConversationalInteraction_StreamProviding"
+ "LBConversationalInteraction_TurnConsuming"
+ "LBLocalSpeechRecognitionSettings:::isLinwoodEnabled"
+ "LBLocalSpeechRecognizerTurnEndSettings:::runtimeType"
+ "LBLocalSpeechRecognizerTurnFinalizedContext:::requestId"
+ "LBLocalSpeechRecognizerTurnFinalizedContext:::runtimeType"
+ "LBLocalSpeechRecognizerTurnFinalizedContext:::selectedRuntime"
+ "LBLocalSpeechRecognizerTurnFinalizedContext:::selectedTrpId"
+ "LBLocalSpeechRecognizerTurnStartContext:::attendingModePreference"
+ "LBLocalSpeechRecognizerTurnStartContext:::requestId"
+ "LBLocalSpeechRecognizerTurnStartContext:::runtimeType"
+ "LBLocalSpeechRecognizerTurnStartContext:::selectedTrpId"
+ "[isLinwoodEnabled = %@]"
+ "bufferDuration"
+ "changeTime"
+ "com.apple.siri.audio.stream.player.service.xpc"
+ "com.apple.siri.turn.service.xpc"
+ "isRequestSampledForCollisionDetection"
+ "streamFormat"
+ "streamSampleRate"
+ "streamType"
+ "v24@?0@\"NSUUID\"8@\"NSError\"16"
- "#16@0:8"
- ".cxx_destruct"
- "<%@: %p; messageHash=%lu, lastTRPCandidateId=%@, speechDetected=%d, isSameUser=%d, isInvocationUser=%d, didDetectPostVTSilence=%d, didTRPArrivalTimeout=%d, noSpeechTokensDetectedInRequest=%d, minSpeechEventThresholdMet=%d, longFormSpeechEventThresholdMet=%d, maxSpeechEventThresholdMet=%d, noTRPArrivalThresholdMet=%d, mitigationTrailingSilenceThresholdMet=%d, isManualMode=%d, processedAudioDurationMs=%ld>"
- "<%@: %p> requestId=%@, trpId=%@, selectedTrpId=%@, turnEndReason=%@, processedAudioDuration=%f, trailingSilenceDurationMs=%f"
- "@"
- "@\"<LBAttendingStatesServiceDelegate>\""
- "@\"<LBAudioStreamConsumingDelegate>\""
- "@\"<LBAudioStreamConsumingDelegate>\"16@0:8"
- "@\"<LBAudioStreamProvidingDelegate>\""
- "@\"<LBAudioStreamProvidingDelegate>\"16@0:8"
- "@\"<LBLocalSpeechRecognizerClientDelegate>\""
- "@\"AFASRSharedUserInfo\""
- "@\"AFPowerContextPolicy\""
- "@\"CLLocation\""
- "@\"CSAudioStream\""
- "@\"CSFAudioConverter\""
- "@\"CSSiriAudioMessageRequestClient\""
- "@\"CSStateMachine\""
- "@\"CSXPCClient\""
- "@\"LBAudioCapture\""
- "@\"LBAudioStreamConfiguration\""
- "@\"LBAudioStreamConsumerConfiguration\""
- "@\"LBAudioStreamInfo\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSMutableArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@\"NSXPCListenerEndpoint\""
- "@104@0:8@16@24Q32@40@48@56@64B72B76B80B84d88@96"
- "@108@0:8@16@24Q32@40@48@56@64B72B76B80B84d88@96B104"
- "@112@0:8@16@24Q32@40@48@56@64B72B76B80B84d88@96B104B108"
- "@120@0:8@16@24Q32@40@48@56@64B72B76B80B84d88@96B104B108@112"
- "@128@0:8@16@24Q32@40@48@56@64B72B76B80B84d88@96B104B108@112B120B124"
- "@136@0:8@16@24Q32@40@48@56@64B72B76B80B84d88@96B104B108@112B120B124@128"
- "@140@0:8@16@24Q32@40@48@56@64B72B76B80B84d88@96B104B108@112B120B124@128B136"
- "@148@0:8@16@24Q32@40@48@56@64B72B76B80B84d88@96B104B108@112B120B124@128B136@140"
- "@148@0:8@16@24Q32@40@48@56@64B72B76B80B84d88@96B104B108B112B116@120B128@132@140"
- "@16@0:8"
- "@172@0:8@16@24Q32@40@48@56@64B72B76B80B84d88@96B104B108B112B116@120B128@132@140@148@156@164"
- "@180@0:8@16@24Q32@40@48@56@64B72B76B80B84d88@96B104B108B112B116@120B128@132@140@148@156@164@172"
- "@20@0:8B16"
- "@216@0:8@16@24Q32Q40@48@56@64@72B80B84B88B92d96@104B112B116B120B124@128B136@140@148@156@164@172@180B188Q192q200@208"
- "@220@0:8@16@24Q32Q40@48@56@64@72B80B84B88B92d96@104B112B116B120B124@128B136@140@148@156@164@172@180B188Q192q200@208B216"
- "@220@0:8@16@24Q32Q40@48@56@64@72B80B84B88B92d96@104B112B116B120B124B128@132@140@148@156@164@172B180Q184q192@200B208@212"
- "@228@0:8@16@24Q32Q40@48@56@64@72B80B84B88B92d96@104B112B116B120B124@128B136@140@148@156@164@172@180B188Q192q200@208B216@220"
- "@236@0:8@16@24Q32Q40@48@56@64@72B80B84B88B92d96@104B112B116B120B124@128B136@140@148@156@164@172@180B188Q192q200@208B216@220@228"
- "@244@0:8@16@24Q32Q40@48@56@64@72B80B84B88B92d96@104B112B116B120B124@128B136@140@148@156@164@172@180B188Q192q200@208B216@220@228@236"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@252@0:8@16@24Q32Q40@48@56@64@72B80B84B88B92d96@104B112B116B120B124@128B136@140@148@156@164@172@180B188Q192q200@208B216@220@228@236@244"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@32@0:8@16d24"
- "@32@0:8Q16@24"
- "@32@0:8q16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16Q24Q32"
- "@40@0:8@16d24Q32"
- "@40@0:8Q16@24@32"
- "@48@0:8Q16q24q32@40"
- "@56@0:8@16@24Q32@40@48"
- "@56@0:8@16@24Q32d40d48"
- "@56@0:8q16@24@32q40@48"
- "@64@0:8@16@24Q32@40@48@56"
- "@68@0:8@16Q24Q32Q40Q48Q56B64"
- "@80@0:8@16B24B28B32B36B40B44B48B52B56B60B64B68q72"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8q16"
- "CSFAudioConverterDelegate"
- "CSStateMachineDelegate"
- "CSXPCClient:didDisconnect:"
- "CSXPCClientDelegate"
- "LBAttendingStatesService"
- "LBAttendingStatesServiceClient"
- "LBAttendingStatesServiceDelegate"
- "LBAudibleExperienceError"
- "LBAudioCapture"
- "LBAudioChunk"
- "LBAudioPacket"
- "LBAudioRecordingAccessor"
- "LBAudioSessionInformEvent"
- "LBAudioSessionMediaControlEvent"
- "LBAudioSessionPhoneCallEvent"
- "LBAudioSessionRecordingEvent"
- "LBAudioStreamConfiguration"
- "LBAudioStreamConsumer"
- "LBAudioStreamConsumerConfiguration"
- "LBAudioStreamConsumerService"
- "LBAudioStreamConsumerServiceDelegate"
- "LBAudioStreamConsuming"
- "LBAudioStreamInfo"
- "LBAudioStreamProviderService"
- "LBAudioStreamProviderServiceDelegate"
- "LBAudioStreamProviding"
- "LBLocalSpeechDetectionUpdates"
- "LBLocalSpeechDetectionUpdatesBuilder"
- "LBLocalSpeechRecognitionSettings"
- "LBLocalSpeechRecognizerClient"
- "LBLocalSpeechRecognizerTurnEndContext"
- "LBLocalSpeechService"
- "LBLocalSpeechServiceDelegate"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "T#,R"
- "T@\"<LBAttendingStatesServiceDelegate>\",W,N,V_delegate"
- "T@\"<LBAudioStreamConsumingDelegate>\",W,N"
- "T@\"<LBAudioStreamConsumingDelegate>\",W,N,V_streamConsumerDelegate"
- "T@\"<LBAudioStreamProvidingDelegate>\",W,N"
- "T@\"<LBAudioStreamProvidingDelegate>\",W,N,V_streamProviderDelegate"
- "T@\"<LBLocalSpeechRecognizerClientDelegate>\",W,N,V_delegate"
- "T@\"AFASRSharedUserInfo\",R,N,V_activeUserInfo"
- "T@\"AFPowerContextPolicy\",R,N,V_powerContext"
- "T@\"CLLocation\",R,N,V_location"
- "T@\"CSAudioStream\",&,N,V_audioStream"
- "T@\"CSFAudioConverter\",&,N,V_opusConverter"
- "T@\"CSSiriAudioMessageRequestClient\",&,N,V_audioMessageClient"
- "T@\"CSStateMachine\",&,N,V_stateMachine"
- "T@\"CSXPCClient\",&,N,V_xpcClient"
- "T@\"LBAudioStreamConfiguration\",C,N,V_streamConfiguration"
- "T@\"LBAudioStreamConsumerConfiguration\",&,N,V_configuration"
- "T@\"LBAudioStreamInfo\",C,N,V_incomingStreamInfo"
- "T@\"LBAudioStreamInfo\",C,N,V_outgoingStreamInfo"
- "T@\"LBAudioStreamInfo\",C,N,V_streamInfo"
- "T@\"NSArray\",C,N,V_chunks"
- "T@\"NSArray\",R,N,V_jitGrammar"
- "T@\"NSArray\",R,N,V_messagesContext"
- "T@\"NSArray\",R,N,V_sharedUserInfos"
- "T@\"NSData\",R,N,V_data"
- "T@\"NSDate\",R,N,V_timestamp"
- "T@\"NSDictionary\",R,N,V_recognitionOverrides"
- "T@\"NSError\",&,N,V_stopError"
- "T@\"NSMutableArray\",&,N,V_incomingAudioChunks"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSObject<OS_os_log>\",&,N,V_logger"
- "T@\"NSString\",&,N,V_requestId"
- "T@\"NSString\",&,N,V_uuidString"
- "T@\"NSString\",&,N,V_xpcConnectionUUIDString"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_audioRecordDeviceId"
- "T@\"NSString\",C,N,V_recordRoute"
- "T@\"NSString\",C,N,V_requestId"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_requestId"
- "T@\"NSString\",R,N,V_UILanguage"
- "T@\"NSString\",R,N,V_applicationName"
- "T@\"NSString\",R,N,V_asrLocale"
- "T@\"NSString\",R,N,V_audioRecordDeviceId"
- "T@\"NSString\",R,N,V_bundleId"
- "T@\"NSString\",R,N,V_dictationUIInteractionId"
- "T@\"NSString\",R,N,V_inputOrigin"
- "T@\"NSString\",R,N,V_lastTRPCandidateId"
- "T@\"NSString\",R,N,V_overrideModelPath"
- "T@\"NSString\",R,N,V_postfixText"
- "T@\"NSString\",R,N,V_prefixText"
- "T@\"NSString\",R,N,V_requestId"
- "T@\"NSString\",R,N,V_selectedText"
- "T@\"NSString\",R,N,V_selectedTrpId"
- "T@\"NSString\",R,N,V_sessionId"
- "T@\"NSString\",R,N,V_trpId"
- "T@\"NSUUID\",R,C,N,V_streamId"
- "T@\"NSXPCConnection\",&,N,V_xpcConnection"
- "T@\"NSXPCListenerEndpoint\",&,N,V_xpcListenerEndpoint"
- "T@,&,N,V_remoteObjectProxy"
- "TB,N,V_hasStartedEncodingPaackets"
- "TB,N,V_isAttending"
- "TB,N,V_isProvidingStream"
- "TB,R"
- "TB,R,N"
- "TB,R,N,V_continuousListening"
- "TB,R,N,V_deliverEagerPackage"
- "TB,R,N,V_detectUtterances"
- "TB,R,N,V_didDetectPostVTSilence"
- "TB,R,N,V_didTRPArrivalTimeout"
- "TB,R,N,V_enableAutoPunctuation"
- "TB,R,N,V_enableEmojiRecognition"
- "TB,R,N,V_enableVoiceCommands"
- "TB,R,N,V_isConsumingStream"
- "TB,R,N,V_isFloat"
- "TB,R,N,V_isInvocationUser"
- "TB,R,N,V_isManualMode"
- "TB,R,N,V_isSameUser"
- "TB,R,N,V_longFormSpeechEventThresholdMet"
- "TB,R,N,V_maxSpeechEventThresholdMet"
- "TB,R,N,V_minSpeechEventThresholdMet"
- "TB,R,N,V_mitigationTrailingSilenceThresholdMet"
- "TB,R,N,V_noSpeechTokensDetectedInRequest"
- "TB,R,N,V_noTRPArrivalThresholdMet"
- "TB,R,N,V_secureOfflineOnly"
- "TB,R,N,V_shouldGenerateVoiceCommandCandidates"
- "TB,R,N,V_shouldHandleCapitalization"
- "TB,R,N,V_shouldStartAudioCapture"
- "TB,R,N,V_shouldStoreAudioOnDevice"
- "TB,R,N,V_speechDetected"
- "TQ,N,V_audioCaptureStartHostTime"
- "TQ,N,V_currentOutgoingStreamIndex"
- "TQ,N,V_index"
- "TQ,R"
- "TQ,R,N,V_actionType"
- "TQ,R,N,V_arrivalHostTimeToAudioRecorder"
- "TQ,R,N,V_audioCaptureStartHostTime"
- "TQ,R,N,V_hostTime"
- "TQ,R,N,V_messageHash"
- "TQ,R,N,V_numSamples"
- "TQ,R,N,V_sampleByteDepth"
- "TQ,R,N,V_speechRecognitionMode"
- "TQ,R,N,V_speechRecognitionTask"
- "TQ,R,N,V_startSampleCount"
- "TQ,R,N,V_turnEndReason"
- "Td,N,V_duration"
- "Td,R,N,V_maximumRecognitionDuration"
- "Td,R,N,V_processedAudioDuration"
- "Td,R,N,V_trailingSilenceDurationMs"
- "Tq,N,V_audioFormat"
- "Tq,N,V_audioRecordType"
- "Tq,N,V_outputAudioFormat"
- "Tq,R,N,V_audioRecordType"
- "Tq,R,N,V_processedAudioDurationMs"
- "UILanguage"
- "URLByAppendingPathComponent:isDirectory:"
- "URLByDeletingLastPathComponent"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "Vv24@0:8@\"AFVoiceIdScoreCard\"16"
- "Vv24@0:8@\"LBAudioStreamInfo\"16"
- "Vv24@0:8@\"LBLocalSpeechDetectionUpdates\"16"
- "Vv24@0:8@\"LBLocalSpeechRecognitionSettings\"16"
- "Vv24@0:8@\"LBLocalSpeechRecognizerTurnEndContext\"16"
- "Vv24@0:8@\"NSArray\"16"
- "Vv24@0:8@\"NSDictionary\"16"
- "Vv24@0:8@\"NSError\"16"
- "Vv24@0:8@\"NSString\"16"
- "Vv24@0:8@\"SMTContinuityEnd\"16"
- "Vv24@0:8@\"SMTMultiUserTRPCandidate\"16"
- "Vv24@0:8@\"SMTSpeechDetectionUpdate\"16"
- "Vv24@0:8@\"SMTTRPCandidate\"16"
- "Vv24@0:8@\"SMTTRPDetected\"16"
- "Vv24@0:8@16"
- "Vv24@0:8@?16"
- "Vv24@0:8@?<v@?@\"LBLocalSpeechDetectionUpdates\"@\"NSError\">16"
- "Vv24@0:8d16"
- "Vv32@0:8@\"<LBAudioStreamProviderServiceDelegate>\"16Q24"
- "Vv32@0:8@\"AFSpeechCorrectionInfo\"16@\"NSString\"24"
- "Vv32@0:8@\"AFSpeechVisualContextAndCorrectionsInfo\"16@\"NSString\"24"
- "Vv32@0:8@\"LBAudioStreamConsumerConfiguration\"16@?<v@?B@\"NSError\">24"
- "Vv32@0:8@\"NSString\"16@\"AFSpeechPackage\"24"
- "Vv32@0:8@\"NSString\"16@\"NSError\"24"
- "Vv32@0:8@\"NSString\"16@\"NSString\"24"
- "Vv32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
- "Vv32@0:8@\"NSString\"16Q24"
- "Vv32@0:8@16@24"
- "Vv32@0:8@16@?24"
- "Vv32@0:8@16Q24"
- "Vv32@0:8Q16@\"NSString\"24"
- "Vv32@0:8Q16@24"
- "Vv40@0:8@\"NSArray\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
- "Vv40@0:8@\"NSString\"16@\"AFSpeechPackage\"24@\"AFSpeechInfoPackage\"32"
- "Vv40@0:8@\"NSString\"16@\"NSString\"24@\"NSArray\"32"
- "Vv40@0:8@16@24@32"
- "Vv40@0:8@16@24@?32"
- "Vv40@0:8d16@\"NSString\"24@\"NSString\"32"
- "Vv40@0:8d16@24@32"
- "Vv48@0:8@\"NSDictionary\"16@\"NSString\"24q32@\"NSError\"40"
- "Vv48@0:8@\"NSString\"16@\"NSString\"24@\"AFSpeechPackage\"32@\"AFSpeechInfoPackage\"40"
- "Vv48@0:8@\"NSString\"16@\"NSString\"24@\"NSArray\"32@\"AFSpeechInfoPackage\"40"
- "Vv48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40"
- "Vv48@0:8@\"NSString\"16Q24@\"AFSpeechPackage\"32d40"
- "Vv48@0:8@\"NSString\"16Q24B32B36@\"NSArray\"40"
- "Vv48@0:8@16@24@32@40"
- "Vv48@0:8@16@24q32@40"
- "Vv48@0:8@16Q24@32d40"
- "Vv48@0:8@16Q24B32B36@40"
- "Vv56@0:8@\"NSString\"16Q24@\"AFSpeechPackage\"32d40@\"AFSpeechInfoPackage\"48"
- "Vv56@0:8@16Q24@32d40@48"
- "Vv88@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSNumber\"48@\"NSNumber\"56@\"NSNumber\"64@\"NSNumber\"72@\"NSNumber\"80"
- "Vv88@0:8@16@24@32@40@48@56@64@72@80"
- "^{_NSZone=}16@0:8"
- "_UILanguage"
- "_actionType"
- "_activeUserInfo"
- "_applicationName"
- "_arrivalHostTimeToAudioRecorder"
- "_asrLocale"
- "_audioCapture"
- "_audioCaptureStartHostTime"
- "_audioFormat"
- "_audioMessageClient"
- "_audioRecordDeviceId"
- "_audioRecordType"
- "_audioStream"
- "_bundleId"
- "_chunks"
- "_cleanupAudioSessionForMediaControlWithEvent:completion:"
- "_cleanupAudioSessionForPhoneCallWithEvent:completion:"
- "_cleanupAudioSessionForRecordingWithEvent:completion:"
- "_cleanupStreamInfo"
- "_computeMessageHash"
- "_configuration"
- "_connection"
- "_consumePackets:completion:"
- "_continuousListening"
- "_convertChunksToOpus:"
- "_currentOutgoingStreamIndex"
- "_data"
- "_delegate"
- "_deliverEagerPackage"
- "_detectUtterances"
- "_dictationUIInteractionId"
- "_didDetectPostVTSilence"
- "_didReceiveAudioChunks:"
- "_didStartStreamingWithInfo:"
- "_didStopConsumingForRequestId:withError:"
- "_didStopStreamingWithError:"
- "_didTRPArrivalTimeout"
- "_duration"
- "_enableAutoPunctuation"
- "_enableEmojiRecognition"
- "_enableVoiceCommands"
- "_eventName:"
- "_flushConversionBufferIfNecessary"
- "_formatIsSupported:"
- "_forwardInitialSpeechUpdate"
- "_handleDidCompleteMediaControlEvent:completion:"
- "_handleDidCompletePhoneCallEvent:completion:"
- "_handleDidCompleteRecordingEvent:completion:"
- "_handleMediaControlEvent:completion:"
- "_handlePhoneCallEvent:completion:"
- "_handleRecordingEvent:completion:"
- "_handleWillStartMediaControlEvent:completion:"
- "_handleWillStartPhoneCallEvent:completion:"
- "_handleWillStartRecordingEvent:completion:"
- "_hasStartedEncodingPaackets"
- "_hostTime"
- "_incomingAudioChunks"
- "_incomingStreamInfo"
- "_index"
- "_inputOrigin"
- "_interruptionHandler:"
- "_invalidate"
- "_invalidationHandler:"
- "_isAttending"
- "_isConsumingStream"
- "_isFloat"
- "_isInvocationUser"
- "_isManualMode"
- "_isProvidingStream"
- "_isSameUser"
- "_jitGrammar"
- "_lastTRPCandidateId"
- "_location"
- "_logger"
- "_longFormSpeechEventThresholdMet"
- "_maxSpeechEventThresholdMet"
- "_maximumRecognitionDuration"
- "_messageHash"
- "_messagesContext"
- "_minSpeechEventThresholdMet"
- "_mitigationTrailingSilenceThresholdMet"
- "_newConnection"
- "_noSpeechTokensDetectedInRequest"
- "_noTRPArrivalThresholdMet"
- "_notifyDelegateDidStopWithError:"
- "_notifyDelegateOfChunks:fromFormat:toFormat:"
- "_notifyDelegateOfFloatConvertedChunks:"
- "_notifyDelegateOfNativeChunks:"
- "_notifyDelegateOfShortConvertedChunks:"
- "_notifyObserverOfSpeechDetectionEvent:"
- "_numSamples"
- "_opusConverter"
- "_outgoingStreamInfo"
- "_outputAudioFormat"
- "_overrideModelPath"
- "_postfixText"
- "_powerContext"
- "_prefixText"
- "_prepareAudioSessionForMediaControlWithEvent:completion:"
- "_prepareAudioSessionForPhoneCallWithEvent:completion:"
- "_prepareAudioSessionForRecordingWithEvent:completion:"
- "_processedAudioDuration"
- "_processedAudioDurationMs"
- "_querySpeechDetectionUpdatesEventWithCompletion:"
- "_queue"
- "_recognitionOverrides"
- "_recordRoute"
- "_remoteObjectProxy"
- "_requestId"
- "_resetStreamInfo"
- "_sampleByteDepth"
- "_sanitizeStreamConfiguration:"
- "_secureOfflineOnly"
- "_selectedText"
- "_selectedTrpId"
- "_service"
- "_sessionId"
- "_setQueue:"
- "_setupStateMachine"
- "_sharedUserInfos"
- "_shouldEnableAudioCapture"
- "_shouldGenerateVoiceCommandCandidates"
- "_shouldHandleCapitalization"
- "_shouldSetSpeechEventForRecordType:"
- "_shouldStartAudioCapture"
- "_shouldStoreAudioOnDevice"
- "_speechDetected"
- "_speechRecognitionMode"
- "_speechRecognitionTask"
- "_startConsumingWithConfiguration:completion:"
- "_startRequestWithAudioContext:streamOption:streamProvider:completion:"
- "_startSampleCount"
- "_startStreaming:"
- "_stateMachine"
- "_stateName:"
- "_stopAudioCaptureWithReason:requestId:"
- "_stopConsumingWithCompletion:"
- "_stopError"
- "_stopSpeechRecognitionTaskWithReason:requestId:shouldInvalidateAfterStop:completion:"
- "_stopStreamOptionWithReason:forRequestId:"
- "_stopStreaming"
- "_streamConfiguration"
- "_streamConsumerDelegate"
- "_streamId"
- "_streamInfo"
- "_streamProviderDelegate"
- "_timestamp"
- "_trailingSilenceDurationMs"
- "_trpId"
- "_turnEndReason"
- "_uuidString"
- "_xpcClient"
- "_xpcConnection"
- "_xpcConnectionUUIDString"
- "_xpcListenerEndpoint"
- "actionType"
- "activeUserInfo"
- "addEntriesFromDictionary:"
- "addObject:"
- "addSamples:timestamp:arrivalTimestampToAudioRecorder:"
- "addTransitionFrom:to:for:"
- "addTransitionFromAnyStateTo:for:"
- "allocWithZone:"
- "appendFormat:"
- "applicationName"
- "arrayWithObjects:count:"
- "asrLocale"
- "audioCaptureStartHostTime"
- "audioConverterDidConvertPackets:packets:durationInSec:timestamp:arrivalTimestampToAudioRecorder:"
- "audioFormat"
- "audioMessageClient"
- "audioRecordDeviceId"
- "audioRecordType"
- "audioStream"
- "audioStreamConsumer:didStopWithError:"
- "audioStreamProvider:didStartWithInfo:"
- "audioStreamProvider:didStopWithError:"
- "audioStreamProvider:receivedPackets:"
- "audioStreamWithRequest:streamName:error:"
- "autorelease"
- "boolValue"
- "build"
- "builder"
- "bundleId"
- "chunks"
- "class"
- "configuration"
- "conformsToProtocol:"
- "connect"
- "connectToServiceIfNeeded"
- "consumePackets:completion:"
- "consumePackets:forRequestId:completion:"
- "containerURLForSecurityApplicationGroupIdentifier:"
- "continuousListening"
- "convertAudioFromURL:toURL:format:completion:"
- "convertToFloatLPCMBufFromShortLPCMBuf:"
- "convertToShortLPCMBufFromFloatLPCMBuf:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "currentHandler"
- "currentOutgoingStreamIndex"
- "currentState"
- "d"
- "d16@0:8"
- "date"
- "dealloc"
- "debugDescription"
- "decodeArrayOfObjectsOfClass:forKey:"
- "decodeBoolForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultManager"
- "defaultRequestWithContext:"
- "delegate"
- "deliverEagerPackage"
- "description"
- "detectUtterances"
- "dictationUIInteractionId"
- "dictionaryWithObjects:forKeys:count:"
- "didIgnoreEvent:from:"
- "didReceiveAudioChunks:"
- "didStartStreamingWithInfo:"
- "didStopConsumingForRequestId:withError:"
- "didStopStreamingWithError:"
- "didTransitFrom:to:by:"
- "directActionJarvisAnnounceMessageTriggerWithDeviceId:"
- "disableAttendingForRootRequestId:"
- "disableLocalSpeechRecognitionForRequestId:"
- "disconnect"
- "dismissAttending"
- "dismissForRequestId:"
- "doubleValue"
- "duration"
- "enableAutoPunctuation"
- "enableEmojiRecognition"
- "enableVoiceCommands"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "errorWithCode:"
- "errorWithCode:localizedDescription:"
- "errorWithCode:userInfo:"
- "errorWithDomain:code:userInfo:"
- "fileExistsAtPath:"
- "flush"
- "getAudioFileURLWithCompletion:"
- "getAudioFileWithRequestId:completion:"
- "getSpeechEventForRecordType:"
- "getTaskStringFromSpeechRecognitionSettings:"
- "handleFailureInFunction:file:lineNumber:description:"
- "hasPrefix:"
- "hasStartedEncodingPaackets"
- "hash"
- "incomingAudioChunks"
- "incomingStreamInfo"
- "index"
- "informAudioSessionEvent:completion:"
- "init"
- "initWithActionType:"
- "initWithActionType:bundleId:"
- "initWithActionType:timestamp:"
- "initWithActionType:timestamp:bundleId:"
- "initWithAudioCaptureStartHostTime:outputAudioFormat:audioRecordType:audioRecordDeviceId:"
- "initWithAudioRecordType:audioRecordDeviceId:recordRoute:audioFormat:streamIdentifier:"
- "initWithBuilder:"
- "initWithCapacity:"
- "initWithChunks:duration:"
- "initWithChunks:duration:index:"
- "initWithChunks:index:"
- "initWithChunks:startSampleCount:numSamples:"
- "initWithCoder:"
- "initWithData:numSamples:sampleByteDepth:startSampleCount:hostTime:arrivalHostTimeToAudioRecorder:isFloat:"
- "initWithDelegate:"
- "initWithDelegate:xpcListenerEndpoint:"
- "initWithDelegate:xpcListenerEndpoint:audioCapture:"
- "initWithInitialState:"
- "initWithLastTRPCandidateId:speechDetected:isSameUser:isInvocationUser:didDetectPostVTSilence:didTRPArrivalTimeout:noSpeechTokensDetectedInRequest:minSpeechEventThresholdMet:longFormSpeechEventThresholdMet:maxSpeechEventThresholdMet:noTRPArrivalThresholdMet:mitigationTrailingSilenceThresholdMet:isManualMode:processedAudioDurationMs:"
- "initWithListenerEndpoint:"
- "initWithMachServiceName:options:"
- "initWithQueue:"
- "initWithRecordType:deviceId:"
- "initWithRequestId:"
- "initWithRequestId:inputOrigin:speechRecognitionTaskName:location:jitGrammar:"
- "initWithRequestId:inputOrigin:speechRecognitionTaskName:location:jitGrammar:overrideModelPath:"
- "initWithRequestId:inputOrigin:speechRecognitionTaskName:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:"
- "initWithRequestId:inputOrigin:speechRecognitionTaskName:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:"
- "initWithRequestId:inputOrigin:speechRecognitionTaskName:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:"
- "initWithRequestId:inputOrigin:speechRecognitionTaskName:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:"
- "initWithRequestId:inputOrigin:speechRecognitionTaskName:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:"
- "initWithRequestId:inputOrigin:speechRecognitionTaskName:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:"
- "initWithRequestId:inputOrigin:speechRecognitionTaskName:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:sharedUserIds:"
- "initWithRequestId:inputOrigin:speechRecognitionTaskName:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:sharedUserIds:enableEmojiRecognition:enableAutoPunctuation:"
- "initWithRequestId:inputOrigin:speechRecognitionTaskName:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:sharedUserIds:enableEmojiRecognition:enableAutoPunctuation:UILanguage:"
- "initWithRequestId:inputOrigin:speechRecognitionTaskName:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:sharedUserIds:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:"
- "initWithRequestId:inputOrigin:speechRecognitionTaskName:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:sharedUserIds:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:"
- "initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:"
- "initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:"
- "initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:asrLocale:"
- "initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:asrLocale:activeUserInfo:"
- "initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:asrLocale:activeUserInfo:messagesContext:"
- "initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:asrLocale:activeUserInfo:messagesContext:sessionId:"
- "initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:asrLocale:"
- "initWithRequestId:selectedTrpId:"
- "initWithRequestId:selectedTrpId:turnEndReason:processedAudioDuration:trailingSilenceDurationMs:"
- "initWithRequestId:streamInfo:"
- "initWithRequestId:trpId:turnEndReason:processedAudioDuration:trailingSilenceDurationMs:"
- "initWithStopRecordingReason:expectedStopHostTime:trailingSilenceDurationAtEndpoint:holdRequest:supportsMagus:requestId:"
- "initWithTimeout:clientIdentity:requireRecordModeLock:requireListeningMicIndicatorLock:"
- "initWithType:"
- "initWithUpdates:"
- "inputOrigin"
- "interfaceWithProtocol:"
- "invalidate"
- "isAttending"
- "isAudioStreamConsumingEnabled"
- "isAudioStreamProvidingEnabled"
- "isConsumingStream"
- "isEqual:"
- "isEqualToString:"
- "isInstalledFromStatusString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProvidingStream"
- "isProxy"
- "jitGrammar"
- "linkItemAtURL:toURL:error:"
- "localAttendingAlreadyStarted"
- "localAttendingStartedWithRootRequestId:"
- "localAttendingStopped"
- "localAttendingStoppedUnexpectedlyWithError:"
- "localAttendingWillStartWithRootRequestId:"
- "localSpeechRecognizerClient:didAcceptedEagerResultWithRequestId:rcId:mitigationSignal:featuresToLog:"
- "localSpeechRecognizerClient:didCompletionRecognitionWithStatistics:requestId:endpointMode:error:"
- "localSpeechRecognizerClient:didCompletionRecognitionWithStatistics:requestId:error:"
- "localSpeechRecognizerClient:receivedContinuityEndDetected:"
- "localSpeechRecognizerClient:receivedEagerRecognitionCandidateWithRequestId:rcId:speechPackage:duration:"
- "localSpeechRecognizerClient:receivedEagerRecognitionCandidateWithRequestId:rcId:speechPackage:duration:metadata:"
- "localSpeechRecognizerClient:receivedFinalEndpointDetectedAtTime:"
- "localSpeechRecognizerClient:receivedFinalResultCandidateWithRequestId:speechPackage:"
- "localSpeechRecognizerClient:receivedFinalResultWithRequestId:speechPackage:"
- "localSpeechRecognizerClient:receivedFinalResultWithRequestId:speechPackage:metadata:"
- "localSpeechRecognizerClient:receivedMultiUserTRPCandidatePackage:"
- "localSpeechRecognizerClient:receivedPartialResultWithRequestId:language:speechPackage:metadata:"
- "localSpeechRecognizerClient:receivedPartialResultWithRequestId:language:tokens:"
- "localSpeechRecognizerClient:receivedPartialResultWithRequestId:language:tokens:metadata:"
- "localSpeechRecognizerClient:receivedSpeechDetectionEvent:"
- "localSpeechRecognizerClient:receivedSpeechDetectionUpdate:"
- "localSpeechRecognizerClient:receivedTCUStateUpdate:"
- "localSpeechRecognizerClient:receivedTRPCandidatePackage:"
- "localSpeechRecognizerClient:receivedTRPDetected:"
- "localSpeechRecognizerClient:receivedVoiceCommandCandidateWithRequestId:speechPackage:metadata:"
- "localSpeechRecognizerClient:receivedVoiceIdScoreCard:"
- "localSpeechRecognizerClient:requestAttentionAssetDownload:"
- "localSpeechServiceDidCompletionRecognitionWithStatistics:requestId:endpointMode:error:"
- "localSpeechServiceDidDetectedFinalEndpointAtTime:"
- "localSpeechServiceDidReceiveContinuityEndDetected:"
- "localSpeechServiceDidReceiveMultiUserTRPCandidatePackage:"
- "localSpeechServiceDidReceiveSpeechDetectionEvent:"
- "localSpeechServiceDidReceiveSpeechDetectionUpdate:"
- "localSpeechServiceDidReceiveTCUStateUpdate:"
- "localSpeechServiceDidReceiveTRPCandidatePackage:"
- "localSpeechServiceDidReceiveTRPDetected:"
- "localSpeechServiceDidReceivedEagerRecognitionCandidateWithRequestId:rcId:speechPackage:duration:"
- "localSpeechServiceDidReceivedEagerRecognitionCandidateWithRequestId:rcId:speechPackage:duration:metadata:"
- "localSpeechServiceDidReceivedEagerResultWithRequestId:rcId:shouldAccept:mitigationSignal:featuresToLog:"
- "localSpeechServiceDidReceivedFinalResultCandidateWithRequestId:speechPackage:"
- "localSpeechServiceDidReceivedFinalResultWithRequestId:speechPackage:"
- "localSpeechServiceDidReceivedFinalResultWithRequestId:speechPackage:metadata:"
- "localSpeechServiceDidReceivedPartialResultWithRequestId:language:speechPackage:metadata:"
- "localSpeechServiceDidReceivedPartialResultWithRequestId:language:tokens:"
- "localSpeechServiceDidReceivedPartialResultWithRequestId:language:tokens:metadata:"
- "localSpeechServiceDidReceivedVoiceCommandCandidateWithRequestId:speechPackage:metadata:"
- "localSpeechServiceDidReceivedVoiceIdScoreCard:"
- "localSpeechServiceRequestAttentionAssetDownload"
- "localeWithLocaleIdentifier:"
- "localizedDescription"
- "localizedDescriptionForCode:"
- "location"
- "logger"
- "loggingHeartbeatRate"
- "longLongValue"
- "maximumRecognitionDuration"
- "messagesContext"
- "noAlertOption"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithLongLong:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "objectForKey:"
- "opusConverter"
- "outgoingStreamInfo"
- "outputAudioFormat"
- "overrideModelPath"
- "path"
- "pauseLocalSpeechRecognitionForRequestId:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performTransitionForEvent:"
- "postfixText"
- "powerContext"
- "prefixText"
- "preheatLocalSpeechRecognitionWithLanguage:source:"
- "prepareAudioProviderWithContext:clientType:error:"
- "processedAudioDuration"
- "q"
- "q16@0:8"
- "querySpeechDetectionUpdatesEventWithCompletion:"
- "queue"
- "recognitionOverrides"
- "recordRoute"
- "release"
- "releaseAudioMessageRetainLockFromRequestId:"
- "remoteObjectProxy"
- "requestDismissed"
- "requestId"
- "requestingSpeechDetectionNotificationAfter:forRequest:withTrpId:"
- "reset"
- "resetCacheAndCompileAllAssets"
- "respondsToSelector:"
- "resume"
- "resumeLocalRecognitionWithRequestId:prefixText:postfixText:selectedText:"
- "retain"
- "retainCount"
- "secureOfflineOnly"
- "selectedText"
- "selectedTrpId"
- "self"
- "sendSpeechCorrectionInfo:interactionIdentifier:"
- "sendVisualContextAndCorrectionsInfo:interactionIdentifier:"
- "sessionId"
- "setAudioCaptureStartHostTime:"
- "setAudioFormat:"
- "setAudioMessageClient:"
- "setAudioRecordDeviceId:"
- "setAudioRecordType:"
- "setAudioStream:"
- "setChunks:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setClientIdentity:"
- "setConfiguration:"
- "setConsumingDelegate:"
- "setCurrentOutgoingStreamIndex:"
- "setDateFormat:"
- "setDelegate:"
- "setDidDetectPostVTSilence:"
- "setDidTRPArrivalTimeout:"
- "setDisableRCSelection:"
- "setDuration:"
- "setEventTime:"
- "setEventType:"
- "setExportedInterface:"
- "setExportedObject:"
- "setHasStartedEncodingPaackets:"
- "setHostTime:"
- "setIncomingAudioChunks:"
- "setIncomingStreamInfo:"
- "setIndex:"
- "setInterface:forSelector:argumentIndex:ofReply:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsAttending:"
- "setIsInvocationUser:"
- "setIsManualMode:"
- "setIsProvidingStream:"
- "setIsSameUser:"
- "setLastTRPCandidateId:"
- "setLocalSpeechRecognizerClientDelegate:"
- "setLocale:"
- "setLogger:"
- "setLongFormSpeechEventThresholdMet:"
- "setMaxSpeechEventThresholdMet:"
- "setMinSpeechEventThresholdMet:"
- "setMitigationTrailingSilenceThresholdMet:"
- "setNoSpeechTokensDetectedInRequest:"
- "setNoTRPArrivalThresholdMet:"
- "setObject:forKey:"
- "setOpusConverter:"
- "setOutgoingStreamInfo:"
- "setOutputAudioFormat:"
- "setProcessedAudioDurationMs:"
- "setQueue:"
- "setRecordRoute:"
- "setRemoteObjectInterface:"
- "setRemoteObjectProxy:"
- "setRequestHistoricalAudioDataWithHostTime:"
- "setRequestId:"
- "setRequestListeningMicIndicatorLock:"
- "setRequestMHUUID:"
- "setSiriSessionUUID:"
- "setSpeechDetected:"
- "setSpeechEvent:"
- "setStartRecordingHostTime:"
- "setStateMachine:"
- "setStopError:"
- "setStreamConfiguration:"
- "setStreamConsumerDelegate:"
- "setStreamInfo:"
- "setStreamProviderDelegate:"
- "setStreamingDelegate:"
- "setUuidString:"
- "setWithArray:"
- "setWithObjects:"
- "setXpcClient:"
- "setXpcConnection:"
- "setXpcConnectionUUIDString:"
- "setXpcListenerEndpoint:"
- "sharedUserInfos"
- "shouldGenerateVoiceCommandCandidates"
- "shouldHandleCapitalization"
- "shouldStartAudioCapture"
- "shouldStoreAudioOnDevice"
- "siriDidPrompt"
- "siriDidPromptWithRootRequestId:"
- "siriPromptWillStart"
- "siriPromptWillStartWithRootRequestId:"
- "spIdKnownUserScores"
- "speechRecognitionMode"
- "speechRecognitionTask"
- "speechRecognizerReadyForNewTurnWithSpeechStartDetectedAtHostTime:audioRecordType:audioRecordDeviceId:"
- "speechStartDetectedWithHostTime:audioRecordType:audioRecordDeviceId:"
- "speechStartDetectedWithShouldDuckTTS:"
- "startAudioCaptureWithRecordContext:startHostTime:siriSessionUUID:completion:"
- "startAudioStreamWithOption:completion:"
- "startConsumingWithConfiguration:completion:"
- "startDeliverLocalSpeechRecognitionResultsWithSettings:"
- "startSpeechRecognitionResultsWithSettings:"
- "startStreaming:"
- "startStreamingWithDelegate:timestamp:"
- "startUpdateStates"
- "stateMachine"
- "stopAudioCaptureWithReason:requestId:completion:"
- "stopAudioStreamWithOption:completion:"
- "stopConsumingForRequestId:completion:"
- "stopConsumingWithCompletion:"
- "stopError"
- "stopLocalSpeechRecognitionTaskWithReason:"
- "stopLocalSpeechRecognitionTaskWithReason:requestId:"
- "stopSpeechRecognitionTaskAndInvalidateWithReason:requestId:completion:"
- "stopSpeechRecognitionTaskWithReason:requestId:"
- "stopSpeechRecognitionTaskWithReason:requestId:completion:"
- "stopSpeechRecognitionWithReason:requestId:"
- "stopStreaming"
- "streamConfiguration"
- "streamConsumerDelegate"
- "streamId"
- "streamInfo"
- "streamProviderDelegate"
- "string"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "supportsSecureCoding"
- "taskString:"
- "timestamp"
- "toBuilder"
- "trailingSilenceDurationMs"
- "trpCandidateReadyForExecutionForRequestId:withTrpId:"
- "trpId"
- "turnEndReason"
- "turnEndReasonString:"
- "turnEndedForRequestId:withTrpId:"
- "turnEndedwithContext:"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "updateTCUState:"
- "updateVoiceCommandContextWithRequestId:prefixText:postfixText:selectedText:disambiguationActive:cursorInVisibleText:favorCommandSuppression:abortCommandSuppression:undoEvent:"
- "uuidString"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"<LBAudioStreamConsumingDelegate>\"16"
- "v24@0:8@\"<LBAudioStreamProvidingDelegate>\"16"
- "v24@0:8@\"LBAudioStreamConfiguration\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@\"CSXPCClient\"16B24"
- "v28@0:8@16B24"
- "v32@0:8@\"LBAudioStreamConsumerConfiguration\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8Q16@24"
- "v32@0:8q16q24"
- "v40@0:8@16q24@?32"
- "v40@0:8@16q24q32"
- "v40@0:8Q16@24@?32"
- "v40@0:8Q16q24@\"NSString\"32"
- "v40@0:8Q16q24@32"
- "v40@0:8d16@24@32"
- "v40@0:8q16q24q32"
- "v44@0:8Q16@24B32@?36"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24q32@?40"
- "v48@0:8@16Q24@32@?40"
- "v52@0:8@\"CSFAudioConverter\"16@\"NSArray\"24f32Q36Q44"
- "v52@0:8@16@24f32Q36Q44"
- "v88@0:8@16@24@32@40@48@56@64@72@80"
- "writeAudioFileToURL:audioFormat:completion:"
- "xpcClient"
- "xpcConnection"
- "xpcConnectionUUIDString"
- "xpcListenerEndpoint"
- "zone"

```
