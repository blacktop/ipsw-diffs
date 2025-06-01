## SpeakerRecognition

> `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`

```diff

-3303.7.1.0.0
-  __TEXT.__text: 0x6d2cc
-  __TEXT.__auth_stubs: 0xfb0
-  __TEXT.__objc_methlist: 0x42ac
-  __TEXT.__const: 0x4f0
-  __TEXT.__cstring: 0xba01
-  __TEXT.__swift5_typeref: 0x291
-  __TEXT.__constg_swiftt: 0x6cc
-  __TEXT.__swift5_reflstr: 0x34a
-  __TEXT.__swift5_fieldmd: 0x31c
-  __TEXT.__swift5_types: 0x2c
-  __TEXT.__swift5_capture: 0x20
-  __TEXT.__swift5_assocty: 0x18
-  __TEXT.__swift5_proto: 0x10
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_protos: 0x4
-  __TEXT.__gcc_except_tab: 0x1b60
-  __TEXT.__oslogstring: 0xa2dd
+3304.82.8.1.2
+  __TEXT.__text: 0x670b8
+  __TEXT.__auth_stubs: 0xb90
+  __TEXT.__objc_methlist: 0x4498
+  __TEXT.__const: 0x170
+  __TEXT.__gcc_except_tab: 0x1c58
+  __TEXT.__cstring: 0xb940
+  __TEXT.__oslogstring: 0xae1e
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x154c
+  __TEXT.__unwind_info: 0x1258
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0xa46
-  __TEXT.__objc_methname: 0xdd39
-  __TEXT.__objc_methtype: 0x1d44
-  __TEXT.__objc_stubs: 0x8040
-  __DATA_CONST.__got: 0x248
-  __DATA_CONST.__const: 0x1698
-  __DATA_CONST.__objc_classlist: 0x228
-  __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x118
+  __TEXT.__objc_classname: 0xb15
+  __TEXT.__objc_methname: 0xe7f3
+  __TEXT.__objc_methtype: 0x1fa4
+  __TEXT.__objc_stubs: 0x8860
+  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__const: 0x1998
+  __DATA_CONST.__objc_classlist: 0x220
+  __DATA_CONST.__objc_catlist: 0x28
+  __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xc218
-  __DATA_CONST.__objc_selrefs: 0x2dd8
+  __DATA_CONST.__objc_const: 0xce08
+  __DATA_CONST.__objc_selrefs: 0x2ff0
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x4d8
+  __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__const: 0x588
-  __AUTH_CONST.__cfstring: 0x4560
-  __AUTH_CONST.__objc_const: 0x1720
+  __AUTH_CONST.__cfstring: 0x4760
+  __AUTH_CONST.__const: 0x360
+  __AUTH_CONST.__objc_const: 0x1970
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x7f0
-  __AUTH.__objc_data: 0x1cc0
-  __AUTH.__data: 0x148
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x480
-  __DATA.__objc_superrefs: 0x150
-  __DATA.__objc_ivar: 0x5e0
-  __DATA.__objc_data: 0x68
-  __DATA.__data: 0xe38
-  __DATA.__bss: 0x2a0
-  __DATA.__common: 0x88
+  __AUTH_CONST.__auth_got: 0x5e0
+  __AUTH.__objc_data: 0x13b0
+  __DATA.__objc_ivar: 0x664
+  __DATA.__data: 0xce8
+  __DATA.__bss: 0xb8
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__common: 0x18
   __DATA_DIRTY.__bss: 0x60

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
-  - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E17728DB-B130-34B3-B182-57AA86C930E9
-  Functions: 2006
-  Symbols:   6175
-  CStrings:  4882
+  UUID: 451270F9-AFF0-35C1-8769-792F04CCF40F
+  Functions: 1721
+  Symbols:   6564
+  CStrings:  5075
 
Symbols:
+ +[BloomFilter supportsSecureCoding]
+ +[CSVTUITrainingResult supportsSecureCoding]
+ +[MurmurHasher hash128WithKey:length:seed:]
+ +[SSRSpeakerProfileEmbeddingExtractor _extractWithModelContext:completion:]
+ +[SSRSpeakerProfileEmbeddingExtractor extractPSRVoiceProfileWithContext:completion:]
+ +[SSRSpeakerProfileEmbeddingExtractor extractSATVoiceProfileWithContext:completion:]
+ +[SSRVoiceProfileManager clearVTEnableAfterProfileSyncFlag]
+ +[SSRVoiceProfileMetadataManager readVoiceTriggerRePromptMetadata:]
+ +[SSRVoiceProfileMetadataManager saveVoiceTriggeRePromptMetadata:]
+ +[VoiceTriggerRePromptUtil sharedInstance]
+ -[BitVector .cxx_destruct]
+ -[BitVector bvData]
+ -[BitVector description]
+ -[BitVector initWithNumberOfBits:]
+ -[BitVector loadData:]
+ -[BitVector numberOfBits]
+ -[BitVector numberOfBytes]
+ -[BitVector setAtIndex:]
+ -[BitVector testAtIndex:]
+ -[BloomFilter .cxx_destruct]
+ -[BloomFilter _loadBitVectorData:]
+ -[BloomFilter add:]
+ -[BloomFilter contains:]
+ -[BloomFilter encodeWithCoder:]
+ -[BloomFilter expectedNumberOfItems]
+ -[BloomFilter falsePositiveRate]
+ -[BloomFilter initWithCoder:]
+ -[BloomFilter initWithExpectedNumberOfItems:falsePositiveRate:seed:]
+ -[BloomFilter seed]
+ -[CSAsset(VTReprompt) blobName]
+ -[CSAsset(VTReprompt) blobVersion]
+ -[CSVTUIAudioSessionRecorder _forceFetchAudioProvider:recordContext:]
+ -[CSVTUIAudioSessionRecorder _hasCorrectInputAudioRouteFromHardwareConfiguration:]
+ -[CSVTUIAudioSessionRecorder audioStreamProvider:audioBufferAvailable:]
+ -[CSVTUIAudioSessionRecorder audioStreamProvider:audioChunkForTVAvailable:]
+ -[CSVTUIAudioSessionRecorder audioStreamProvider:didHardwareConfigurationChange:]
+ -[CSVTUIAudioSessionRecorder audioStreamProvider:didStopStreamUnexpectedly:]
+ -[CSVTUIAudioSessionRecorder audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:]
+ -[CSVTUIAudioSessionRecorder initWithAudioProvider:forceSupportsRemoteDarwinDisplay:]
+ -[CSVTUITrainingResult encodeWithCoder:]
+ -[CSVTUITrainingResult initWithCoder:]
+ -[SSRMobileAssetProvider _getVTRepromptListAssetTypeString]
+ -[SSRMobileAssetProvider _getVTRepromptListCurrentCompatibilityVersion]
+ -[SSRVTUITrainingListener .cxx_destruct]
+ -[SSRVTUITrainingListener activeConnection]
+ -[SSRVTUITrainingListener initWithMessageHandler:]
+ -[SSRVTUITrainingListener listen]
+ -[SSRVTUITrainingListener listener:shouldAcceptNewConnection:]
+ -[SSRVTUITrainingListener listener]
+ -[SSRVTUITrainingListener messageHandler]
+ -[SSRVTUITrainingListener queue]
+ -[SSRVTUITrainingListener setActiveConnection:]
+ -[SSRVTUITrainingListener setListener:]
+ -[SSRVTUITrainingListener setMessageHandler:]
+ -[SSRVTUITrainingListener setQueue:]
+ -[SSRVTUITrainingManager CSVTUIRemoteTrainingSessionRMSAvailable:]
+ -[SSRVTUITrainingManager initWithLocaleIdentifier:withAudioSession:withAppDomain:shouldTrainViaXPC:]
+ -[SSRVTUITrainingMessageHandler .cxx_destruct]
+ -[SSRVTUITrainingMessageHandler VTUITrainingManagerFeedLevel:]
+ -[SSRVTUITrainingMessageHandler audioSourceWithCompletion:]
+ -[SSRVTUITrainingMessageHandler cancelTrainingViaXPCForID:]
+ -[SSRVTUITrainingMessageHandler cleanupViaXPCWithCompletion:]
+ -[SSRVTUITrainingMessageHandler didDetectForceEndPoint]
+ -[SSRVTUITrainingMessageHandler init]
+ -[SSRVTUITrainingMessageHandler prepareWithCompletion:]
+ -[SSRVTUITrainingMessageHandler remoteObjectProxy]
+ -[SSRVTUITrainingMessageHandler reset]
+ -[SSRVTUITrainingMessageHandler setLocaleIdentifier:]
+ -[SSRVTUITrainingMessageHandler setRemoteObjectProxy:]
+ -[SSRVTUITrainingMessageHandler setTrainingManager:]
+ -[SSRVTUITrainingMessageHandler setupWithLocaleID:appDomain:]
+ -[SSRVTUITrainingMessageHandler startRMS]
+ -[SSRVTUITrainingMessageHandler stopRMS]
+ -[SSRVTUITrainingMessageHandler trainUtteranceViaXPC:shouldUseASR:completion:]
+ -[SSRVTUITrainingMessageHandler trainUtteranceViaXPC:shouldUseASR:mhUUID:completionWithResult:]
+ -[SSRVTUITrainingMessageHandler trainingManager]
+ -[SSRVTUITrainingMessageHandler voiceProfileWithCompletion:]
+ -[SSRVTUITrainingMessageHandler vtuiTrainingXPCDisconnected]
+ -[SSRVTUITrainingServiceClient .cxx_destruct]
+ -[SSRVTUITrainingServiceClient CSVTUIRemoteTrainingSessionRMSAvailable:]
+ -[SSRVTUITrainingServiceClient _connection]
+ -[SSRVTUITrainingServiceClient _handleXPCDisconnectedUnexpectedlyWithError:]
+ -[SSRVTUITrainingServiceClient _newConnection]
+ -[SSRVTUITrainingServiceClient _resetupIfNeeded]
+ -[SSRVTUITrainingServiceClient _service]
+ -[SSRVTUITrainingServiceClient audioSourceWithCompletion:]
+ -[SSRVTUITrainingServiceClient cancelTrainingViaXPCForID:]
+ -[SSRVTUITrainingServiceClient cleanupCompletion]
+ -[SSRVTUITrainingServiceClient cleanupViaXPCWithCompletion:]
+ -[SSRVTUITrainingServiceClient delegate]
+ -[SSRVTUITrainingServiceClient didDetectForceEndPoint]
+ -[SSRVTUITrainingServiceClient initWithDelegate:]
+ -[SSRVTUITrainingServiceClient invalidate]
+ -[SSRVTUITrainingServiceClient prepareCompletion]
+ -[SSRVTUITrainingServiceClient prepareWithCompletion:]
+ -[SSRVTUITrainingServiceClient queue]
+ -[SSRVTUITrainingServiceClient remoteObjectProxy]
+ -[SSRVTUITrainingServiceClient requireResetup]
+ -[SSRVTUITrainingServiceClient reset]
+ -[SSRVTUITrainingServiceClient setCleanupCompletion:]
+ -[SSRVTUITrainingServiceClient setDelegate:]
+ -[SSRVTUITrainingServiceClient setLocaleIdentifier:]
+ -[SSRVTUITrainingServiceClient setPrepareCompletion:]
+ -[SSRVTUITrainingServiceClient setQueue:]
+ -[SSRVTUITrainingServiceClient setRemoteObjectProxy:]
+ -[SSRVTUITrainingServiceClient setRequireResetup:]
+ -[SSRVTUITrainingServiceClient setTrainCompletion:]
+ -[SSRVTUITrainingServiceClient setTrainCompletionWithResult:]
+ -[SSRVTUITrainingServiceClient setXpcConnection:]
+ -[SSRVTUITrainingServiceClient setupWithLocaleID:appDomain:]
+ -[SSRVTUITrainingServiceClient startRMS]
+ -[SSRVTUITrainingServiceClient stopRMS]
+ -[SSRVTUITrainingServiceClient trainCompletionWithResult]
+ -[SSRVTUITrainingServiceClient trainCompletion]
+ -[SSRVTUITrainingServiceClient trainUtteranceViaXPC:shouldUseASR:completion:]
+ -[SSRVTUITrainingServiceClient trainUtteranceViaXPC:shouldUseASR:mhUUID:completionWithResult:]
+ -[SSRVTUITrainingServiceClient voiceProfileWithCompletion:]
+ -[SSRVTUITrainingServiceClient xpcConnection]
+ -[SSRVoiceProfileManager isVoiceTriggerRepromptRequiredWithCompletion:]
+ -[SSRVoiceProfileManager isVoiceTriggerRepromptRequired]
+ -[SSRVoiceProfileManager voiceTriggerRepromptFinishedWithCompletion:]
+ -[SSRVoiceProfileManager voiceTriggerRepromptFinished]
+ -[VoiceTriggerRePromptUtil .cxx_destruct]
+ -[VoiceTriggerRePromptUtil bloomFilter]
+ -[VoiceTriggerRePromptUtil initAndLoadImpactedAssistantIdsForRePromptWithAsset:]
+ -[VoiceTriggerRePromptUtil initAndLoadImpactedAssistantIdsForRePrompt]
+ -[VoiceTriggerRePromptUtil isRePromptableWithAssistantId:]
+ -[VoiceTriggerRePromptUtil setBloomFilter:]
+ GCC_except_table1005
+ GCC_except_table1009
+ GCC_except_table1018
+ GCC_except_table1023
+ GCC_except_table1027
+ GCC_except_table1079
+ GCC_except_table1083
+ GCC_except_table1087
+ GCC_except_table1090
+ GCC_except_table1112
+ GCC_except_table1265
+ GCC_except_table1291
+ GCC_except_table1298
+ GCC_except_table1303
+ GCC_except_table1319
+ GCC_except_table1323
+ GCC_except_table1327
+ GCC_except_table1402
+ GCC_except_table1406
+ GCC_except_table1428
+ GCC_except_table1433
+ GCC_except_table1482
+ GCC_except_table1490
+ GCC_except_table1504
+ GCC_except_table1513
+ GCC_except_table1529
+ GCC_except_table1546
+ GCC_except_table160
+ GCC_except_table163
+ GCC_except_table169
+ GCC_except_table171
+ GCC_except_table281
+ GCC_except_table324
+ GCC_except_table330
+ GCC_except_table333
+ GCC_except_table391
+ GCC_except_table407
+ GCC_except_table477
+ GCC_except_table485
+ GCC_except_table487
+ GCC_except_table632
+ GCC_except_table670
+ GCC_except_table675
+ GCC_except_table701
+ GCC_except_table704
+ GCC_except_table748
+ GCC_except_table749
+ GCC_except_table752
+ GCC_except_table753
+ GCC_except_table754
+ GCC_except_table755
+ GCC_except_table756
+ GCC_except_table757
+ GCC_except_table758
+ GCC_except_table759
+ GCC_except_table760
+ GCC_except_table762
+ GCC_except_table763
+ GCC_except_table765
+ GCC_except_table768
+ GCC_except_table845
+ GCC_except_table899
+ GCC_except_table903
+ GCC_except_table921
+ GCC_except_table992
+ GCC_except_table993
+ GCC_except_table995
+ _OBJC_CLASS_$_BitVector
+ _OBJC_CLASS_$_BloomFilter
+ _OBJC_CLASS_$_CSAudioProvider
+ _OBJC_CLASS_$_CSAudioRecorder
+ _OBJC_CLASS_$_CSAudioStartStreamOption
+ _OBJC_CLASS_$_CSAudioStreamRequest
+ _OBJC_CLASS_$_CSRemoteDarwinDeviceInfo
+ _OBJC_CLASS_$_MurmurHasher
+ _OBJC_CLASS_$_NSInputStream
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_CLASS_$_NSXPCListener
+ _OBJC_CLASS_$_SSRSpeakerProfileEmbeddingExtractor
+ _OBJC_CLASS_$_SSRVTUITrainingListener
+ _OBJC_CLASS_$_SSRVTUITrainingMessageHandler
+ _OBJC_CLASS_$_SSRVTUITrainingServiceClient
+ _OBJC_CLASS_$_VoiceTriggerRePromptUtil
+ _OBJC_IVAR_$_BitVector._bitShift
+ _OBJC_IVAR_$_BitVector._bitsPerBlock
+ _OBJC_IVAR_$_BitVector._bvData
+ _OBJC_IVAR_$_BitVector._data
+ _OBJC_IVAR_$_BitVector._numberOfBits
+ _OBJC_IVAR_$_BitVector._numberOfBytes
+ _OBJC_IVAR_$_BloomFilter._bitVector
+ _OBJC_IVAR_$_BloomFilter._expectedNumberOfItems
+ _OBJC_IVAR_$_BloomFilter._falsePositiveRate
+ _OBJC_IVAR_$_BloomFilter._numberHashes
+ _OBJC_IVAR_$_BloomFilter._numberOfBits
+ _OBJC_IVAR_$_BloomFilter._seed
+ _OBJC_IVAR_$_CSVTUIAudioSessionRecorder._audioProvider
+ _OBJC_IVAR_$_CSVTUIAudioSessionRecorder._audioStream
+ _OBJC_IVAR_$_SSRVTUITrainingListener._activeConnection
+ _OBJC_IVAR_$_SSRVTUITrainingListener._listener
+ _OBJC_IVAR_$_SSRVTUITrainingListener._messageHandler
+ _OBJC_IVAR_$_SSRVTUITrainingListener._queue
+ _OBJC_IVAR_$_SSRVTUITrainingManager._shouldTrainViaXPC
+ _OBJC_IVAR_$_SSRVTUITrainingManager._trainingServiceClient
+ _OBJC_IVAR_$_SSRVTUITrainingMessageHandler._remoteObjectProxy
+ _OBJC_IVAR_$_SSRVTUITrainingMessageHandler._trainingManager
+ _OBJC_IVAR_$_SSRVTUITrainingServiceClient._appDomain
+ _OBJC_IVAR_$_SSRVTUITrainingServiceClient._cleanupCompletion
+ _OBJC_IVAR_$_SSRVTUITrainingServiceClient._delegate
+ _OBJC_IVAR_$_SSRVTUITrainingServiceClient._localeIdentifier
+ _OBJC_IVAR_$_SSRVTUITrainingServiceClient._prepareCompletion
+ _OBJC_IVAR_$_SSRVTUITrainingServiceClient._queue
+ _OBJC_IVAR_$_SSRVTUITrainingServiceClient._remoteObjectProxy
+ _OBJC_IVAR_$_SSRVTUITrainingServiceClient._requireResetup
+ _OBJC_IVAR_$_SSRVTUITrainingServiceClient._trainCompletion
+ _OBJC_IVAR_$_SSRVTUITrainingServiceClient._trainCompletionWithResult
+ _OBJC_IVAR_$_SSRVTUITrainingServiceClient._xpcConnection
+ _OBJC_IVAR_$_VoiceTriggerRePromptUtil._bloomFilter
+ _OBJC_METACLASS_$_BitVector
+ _OBJC_METACLASS_$_BloomFilter
+ _OBJC_METACLASS_$_MurmurHasher
+ _OBJC_METACLASS_$_SSRSpeakerProfileEmbeddingExtractor
+ _OBJC_METACLASS_$_SSRVTUITrainingListener
+ _OBJC_METACLASS_$_SSRVTUITrainingMessageHandler
+ _OBJC_METACLASS_$_SSRVTUITrainingServiceClient
+ _OBJC_METACLASS_$_VoiceTriggerRePromptUtil
+ _SSRVTUITrainingServiceDelegateGetXPCInterface
+ _SSRVTUITrainingServiceGetXPCInterface
+ _SSRVTUITrainingServiceName
+ __OBJC_$_CATEGORY_CSAsset_$_VTReprompt
+ __OBJC_$_CLASS_METHODS_BloomFilter
+ __OBJC_$_CLASS_METHODS_CSVTUITrainingResult
+ __OBJC_$_CLASS_METHODS_MurmurHasher
+ __OBJC_$_CLASS_METHODS_SSRSpeakerProfileEmbeddingExtractor
+ __OBJC_$_CLASS_METHODS_VoiceTriggerRePromptUtil
+ __OBJC_$_CLASS_PROP_LIST_BloomFilter
+ __OBJC_$_CLASS_PROP_LIST_CSVTUITrainingResult
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.3255
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.6347
+ __OBJC_$_INSTANCE_METHODS_BitVector
+ __OBJC_$_INSTANCE_METHODS_BloomFilter
+ __OBJC_$_INSTANCE_METHODS_CSAsset(VTReprompt|SpeakerRecognition)
+ __OBJC_$_INSTANCE_METHODS_SSRVTUITrainingListener
+ __OBJC_$_INSTANCE_METHODS_SSRVTUITrainingMessageHandler
+ __OBJC_$_INSTANCE_METHODS_SSRVTUITrainingServiceClient
+ __OBJC_$_INSTANCE_METHODS_VoiceTriggerRePromptUtil
+ __OBJC_$_INSTANCE_VARIABLES_BitVector
+ __OBJC_$_INSTANCE_VARIABLES_BloomFilter
+ __OBJC_$_INSTANCE_VARIABLES_SSRVTUITrainingListener
+ __OBJC_$_INSTANCE_VARIABLES_SSRVTUITrainingMessageHandler
+ __OBJC_$_INSTANCE_VARIABLES_SSRVTUITrainingServiceClient
+ __OBJC_$_INSTANCE_VARIABLES_VoiceTriggerRePromptUtil
+ __OBJC_$_PROP_LIST_BitVector
+ __OBJC_$_PROP_LIST_BloomFilter
+ __OBJC_$_PROP_LIST_NSObject.1113
+ __OBJC_$_PROP_LIST_NSObject.1473
+ __OBJC_$_PROP_LIST_NSObject.1681
+ __OBJC_$_PROP_LIST_NSObject.1957
+ __OBJC_$_PROP_LIST_NSObject.2205
+ __OBJC_$_PROP_LIST_NSObject.2530
+ __OBJC_$_PROP_LIST_NSObject.276
+ __OBJC_$_PROP_LIST_NSObject.2922
+ __OBJC_$_PROP_LIST_NSObject.3022
+ __OBJC_$_PROP_LIST_NSObject.3581
+ __OBJC_$_PROP_LIST_NSObject.3770
+ __OBJC_$_PROP_LIST_NSObject.4023
+ __OBJC_$_PROP_LIST_NSObject.407
+ __OBJC_$_PROP_LIST_NSObject.4272
+ __OBJC_$_PROP_LIST_NSObject.4465
+ __OBJC_$_PROP_LIST_NSObject.4817
+ __OBJC_$_PROP_LIST_NSObject.5042
+ __OBJC_$_PROP_LIST_NSObject.5081
+ __OBJC_$_PROP_LIST_NSObject.5415
+ __OBJC_$_PROP_LIST_NSObject.585
+ __OBJC_$_PROP_LIST_NSObject.6013
+ __OBJC_$_PROP_LIST_NSObject.6115
+ __OBJC_$_PROP_LIST_NSObject.780
+ __OBJC_$_PROP_LIST_NSObject.941
+ __OBJC_$_PROP_LIST_SSRSpeakerRecognizer.2531
+ __OBJC_$_PROP_LIST_SSRVTUITrainingListener
+ __OBJC_$_PROP_LIST_SSRVTUITrainingMessageHandler
+ __OBJC_$_PROP_LIST_SSRVTUITrainingServiceClient
+ __OBJC_$_PROP_LIST_SSRVoiceProfileRetrainer.2206
+ __OBJC_$_PROP_LIST_VoiceTriggerRePromptUtil
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.3256
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.6348
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVTUIAudioSessionDelegate.4273
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVTUIAudioSessionDelegate.4466
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVTUIEndPointDelegate.4467
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.3257
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.6349
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1114
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1474
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1682
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1958
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2207
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2532
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.277
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2923
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3023
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3582
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3771
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4024
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.408
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4274
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4468
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4818
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5043
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5082
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5416
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.586
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6014
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6116
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.781
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.942
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioProviderDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_EARSyncPSRAudioProcessorDelegate.2208
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1115
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1475
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1683
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1959
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2209
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2533
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.278
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2924
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3024
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3583
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3772
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4025
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.409
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4275
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4469
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4819
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5044
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5083
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5417
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.587
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6015
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6117
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.782
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.943
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSXPCListenerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SFSpeechRecognitionTaskDelegate.4470
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRAssetProviding.5084
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRVTUITrainingService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRVTUITrainingService.1116
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRVTUITrainingService.1476
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRVTUITrainingService.3584
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRVTUITrainingServiceDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRVTUITrainingServiceDelegate.1477
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRVTUITrainingServiceDelegate.3585
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSRAssetProviding.5085
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSRSpeakerRecognizer.2534
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSRVTUITrainingService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSRVTUITrainingService.1117
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSRVTUITrainingService.1478
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSRVTUITrainingService.3586
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSRVoiceProfileRetrainer.2210
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioProviderDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVTUIAudioSessionDelegate.4276
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVTUIAudioSessionDelegate.4471
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVTUIEndPointDelegate.4472
+ __OBJC_$_PROTOCOL_METHOD_TYPES_EARSyncPSRAudioProcessorDelegate.2211
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.3258
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.6350
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1118
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1479
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1684
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1960
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2212
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2535
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.279
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2925
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3025
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3587
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3773
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4026
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.410
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4277
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4473
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4820
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5045
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5086
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5418
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.588
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6016
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6118
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.783
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.944
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.3259
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.6351
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSXPCListenerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFSpeechRecognitionTaskDelegate.4474
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSRAssetProviding.5087
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSRSpeakerRecognizer.2536
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSRVTUITrainingService
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSRVTUITrainingService.1119
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSRVTUITrainingService.1480
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSRVTUITrainingService.3588
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSRVTUITrainingServiceDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSRVTUITrainingServiceDelegate.1481
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSRVTUITrainingServiceDelegate.3589
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSRVoiceProfileRetrainer.2213
+ __OBJC_$_PROTOCOL_REFS_CSAudioProviderDelegate
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate
+ __OBJC_$_PROTOCOL_REFS_CSVTUIAudioSessionDelegate.4278
+ __OBJC_$_PROTOCOL_REFS_CSVTUIAudioSessionDelegate.4475
+ __OBJC_$_PROTOCOL_REFS_CSVTUIEndPointDelegate.4476
+ __OBJC_$_PROTOCOL_REFS_EARSyncPSRAudioProcessorDelegate.2214
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.3260
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.6352
+ __OBJC_$_PROTOCOL_REFS_NSXPCListenerDelegate
+ __OBJC_$_PROTOCOL_REFS_SFSpeechRecognitionTaskDelegate.4477
+ __OBJC_$_PROTOCOL_REFS_SSRAssetProviding.5088
+ __OBJC_$_PROTOCOL_REFS_SSRSpeakerRecognizer.2537
+ __OBJC_$_PROTOCOL_REFS_SSRVTUITrainingService
+ __OBJC_$_PROTOCOL_REFS_SSRVTUITrainingService.1120
+ __OBJC_$_PROTOCOL_REFS_SSRVTUITrainingService.1482
+ __OBJC_$_PROTOCOL_REFS_SSRVTUITrainingService.3590
+ __OBJC_$_PROTOCOL_REFS_SSRVTUITrainingServiceDelegate
+ __OBJC_$_PROTOCOL_REFS_SSRVTUITrainingServiceDelegate.1483
+ __OBJC_$_PROTOCOL_REFS_SSRVTUITrainingServiceDelegate.3591
+ __OBJC_$_PROTOCOL_REFS_SSRVoiceProfileRetrainer.2215
+ __OBJC_CLASS_PROTOCOLS_$_BloomFilter
+ __OBJC_CLASS_PROTOCOLS_$_CSVTUITrainingResult
+ __OBJC_CLASS_PROTOCOLS_$_SSRVTUITrainingListener
+ __OBJC_CLASS_PROTOCOLS_$_SSRVTUITrainingMessageHandler
+ __OBJC_CLASS_PROTOCOLS_$_SSRVTUITrainingServiceClient
+ __OBJC_CLASS_RO_$_BitVector
+ __OBJC_CLASS_RO_$_BloomFilter
+ __OBJC_CLASS_RO_$_MurmurHasher
+ __OBJC_CLASS_RO_$_SSRSpeakerProfileEmbeddingExtractor
+ __OBJC_CLASS_RO_$_SSRVTUITrainingListener
+ __OBJC_CLASS_RO_$_SSRVTUITrainingMessageHandler
+ __OBJC_CLASS_RO_$_SSRVTUITrainingServiceClient
+ __OBJC_CLASS_RO_$_VoiceTriggerRePromptUtil
+ __OBJC_LABEL_PROTOCOL_$_CSAudioProviderDelegate
+ __OBJC_LABEL_PROTOCOL_$_CSAudioStreamProvidingDelegate
+ __OBJC_LABEL_PROTOCOL_$_NSXPCListenerDelegate
+ __OBJC_LABEL_PROTOCOL_$_SSRVTUITrainingService
+ __OBJC_LABEL_PROTOCOL_$_SSRVTUITrainingServiceDelegate
+ __OBJC_METACLASS_RO_$_BitVector
+ __OBJC_METACLASS_RO_$_BloomFilter
+ __OBJC_METACLASS_RO_$_MurmurHasher
+ __OBJC_METACLASS_RO_$_SSRSpeakerProfileEmbeddingExtractor
+ __OBJC_METACLASS_RO_$_SSRVTUITrainingListener
+ __OBJC_METACLASS_RO_$_SSRVTUITrainingMessageHandler
+ __OBJC_METACLASS_RO_$_SSRVTUITrainingServiceClient
+ __OBJC_METACLASS_RO_$_VoiceTriggerRePromptUtil
+ __OBJC_PROTOCOL_$_CSAudioProviderDelegate
+ __OBJC_PROTOCOL_$_CSAudioStreamProvidingDelegate
+ __OBJC_PROTOCOL_$_NSXPCListenerDelegate
+ __OBJC_PROTOCOL_$_SSRVTUITrainingService
+ __OBJC_PROTOCOL_$_SSRVTUITrainingServiceDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_SSRVTUITrainingService
+ __OBJC_PROTOCOL_REFERENCE_$_SSRVTUITrainingServiceDelegate
+ ___108-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withLocale:withAsset:withCompletion:]_block_invoke.690
+ ___108-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withLocale:withAsset:withCompletion:]_block_invoke.704
+ ___37-[SSRVTUITrainingManager audioSource]_block_invoke_2
+ ___37-[SSRVTUITrainingManager audioSource]_block_invoke_3
+ ___37-[SSRVTUITrainingServiceClient reset]_block_invoke
+ ___38-[SSRVTUITrainingManager voiceProfile]_block_invoke
+ ___38-[SSRVTUITrainingManager voiceProfile]_block_invoke_2
+ ___39-[SSRVTUITrainingServiceClient stopRMS]_block_invoke
+ ___40-[SSRVTUITrainingServiceClient startRMS]_block_invoke
+ ___42+[VoiceTriggerRePromptUtil sharedInstance]_block_invoke
+ ___42-[SSRVTUITrainingServiceClient invalidate]_block_invoke
+ ___43-[CSVTUIAudioSessionRecorder stopRecording]_block_invoke
+ ___43-[SSRVTUITrainingServiceClient _connection]_block_invoke
+ ___43-[SSRVTUITrainingServiceClient _connection]_block_invoke.10
+ ___44-[CSVTUIAudioSessionRecorder startRecording]_block_invoke
+ ___46-[SSRVTUITrainingManager cancelTrainingForID:]_block_invoke_2
+ ___46-[SSRVTUITrainingManager setLocaleIdentifier:]_block_invoke
+ ___48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.23
+ ___48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.24
+ ___48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke_2
+ ___48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke_2.22
+ ___48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke_3
+ ___48-[SSRVTUITrainingManager prepareWithCompletion:]_block_invoke_2
+ ___48-[SSRVTUITrainingManager prepareWithCompletion:]_block_invoke_3
+ ___48-[SSRVTUITrainingManager prepareWithCompletion:]_block_invoke_4
+ ___52-[SSRVTUITrainingServiceClient setLocaleIdentifier:]_block_invoke
+ ___54-[SSRVTUITrainingServiceClient didDetectForceEndPoint]_block_invoke
+ ___54-[SSRVTUITrainingServiceClient prepareWithCompletion:]_block_invoke
+ ___54-[SSRVTUITrainingServiceClient prepareWithCompletion:]_block_invoke_2
+ ___56-[SSRVoiceProfileManager isVoiceTriggerRepromptRequired]_block_invoke
+ ___58-[SSRVTUITrainingServiceClient audioSourceWithCompletion:]_block_invoke
+ ___58-[SSRVTUITrainingServiceClient audioSourceWithCompletion:]_block_invoke_2
+ ___58-[SSRVTUITrainingServiceClient cancelTrainingViaXPCForID:]_block_invoke
+ ___59-[SSRVTUITrainingServiceClient voiceProfileWithCompletion:]_block_invoke
+ ___59-[SSRVTUITrainingServiceClient voiceProfileWithCompletion:]_block_invoke_2
+ ___60-[SSRVTUITrainingServiceClient cleanupViaXPCWithCompletion:]_block_invoke
+ ___60-[SSRVTUITrainingServiceClient cleanupViaXPCWithCompletion:]_block_invoke_2
+ ___60-[SSRVTUITrainingServiceClient setupWithLocaleID:appDomain:]_block_invoke
+ ___62-[SSRVTUITrainingListener listener:shouldAcceptNewConnection:]_block_invoke
+ ___62-[SSRVTUITrainingListener listener:shouldAcceptNewConnection:]_block_invoke.3
+ ___62-[SSRVTUITrainingListener listener:shouldAcceptNewConnection:]_block_invoke.5
+ ___62-[SSRVTUITrainingListener listener:shouldAcceptNewConnection:]_block_invoke_2
+ ___62-[SSRVTUITrainingListener listener:shouldAcceptNewConnection:]_block_invoke_2.4
+ ___65-[SSRVTUITrainingManager trainUtterance:shouldUseASR:completion:]_block_invoke_3
+ ___65-[SSRVTUITrainingManager trainUtterance:shouldUseASR:completion:]_block_invoke_4
+ ___65-[SSRVTUITrainingManager trainUtterance:shouldUseASR:completion:]_block_invoke_5
+ ___69-[CSVTUIAudioSessionRecorder _forceFetchAudioProvider:recordContext:]_block_invoke
+ ___77-[SSRVTUITrainingServiceClient trainUtteranceViaXPC:shouldUseASR:completion:]_block_invoke
+ ___77-[SSRVTUITrainingServiceClient trainUtteranceViaXPC:shouldUseASR:completion:]_block_invoke_2
+ ___81-[CSVTUIAudioSessionRecorder audioStreamProvider:didHardwareConfigurationChange:]_block_invoke
+ ___82-[SSRVTUITrainingManager trainUtterance:shouldUseASR:mhUUID:completionWithResult:]_block_invoke_3
+ ___82-[SSRVTUITrainingManager trainUtterance:shouldUseASR:mhUUID:completionWithResult:]_block_invoke_4
+ ___82-[SSRVTUITrainingManager trainUtterance:shouldUseASR:mhUUID:completionWithResult:]_block_invoke_5
+ ___84+[SSRSpeakerProfileEmbeddingExtractor extractPSRVoiceProfileWithContext:completion:]_block_invoke
+ ___84+[SSRSpeakerProfileEmbeddingExtractor extractSATVoiceProfileWithContext:completion:]_block_invoke
+ ___94-[SSRVTUITrainingServiceClient trainUtteranceViaXPC:shouldUseASR:mhUUID:completionWithResult:]_block_invoke
+ ___94-[SSRVTUITrainingServiceClient trainUtteranceViaXPC:shouldUseASR:mhUUID:completionWithResult:]_block_invoke_2
+ ___Block_byref_object_copy_.1416
+ ___Block_byref_object_copy_.1634
+ ___Block_byref_object_copy_.1789
+ ___Block_byref_object_copy_.2107
+ ___Block_byref_object_copy_.2612
+ ___Block_byref_object_copy_.2769
+ ___Block_byref_object_copy_.3428
+ ___Block_byref_object_copy_.3673
+ ___Block_byref_object_copy_.3903
+ ___Block_byref_object_copy_.4769
+ ___Block_byref_object_copy_.4896
+ ___Block_byref_object_copy_.5169
+ ___Block_byref_object_copy_.5532
+ ___Block_byref_object_copy_.733
+ ___Block_byref_object_copy_.858
+ ___Block_byref_object_copy_.967
+ ___Block_byref_object_dispose_.1417
+ ___Block_byref_object_dispose_.1635
+ ___Block_byref_object_dispose_.1790
+ ___Block_byref_object_dispose_.2108
+ ___Block_byref_object_dispose_.2613
+ ___Block_byref_object_dispose_.2770
+ ___Block_byref_object_dispose_.3429
+ ___Block_byref_object_dispose_.3674
+ ___Block_byref_object_dispose_.3904
+ ___Block_byref_object_dispose_.4770
+ ___Block_byref_object_dispose_.4897
+ ___Block_byref_object_dispose_.5170
+ ___Block_byref_object_dispose_.5533
+ ___Block_byref_object_dispose_.734
+ ___Block_byref_object_dispose_.859
+ ___Block_byref_object_dispose_.968
+ ___block_descriptor_40_e8_32bs_e18_v32?0q8i16B20^24ls32l8
+ ___block_descriptor_40_e8_32bs_e34_v32?0"NSData"8I16I20"NSError"24ls32l8
+ ___block_descriptor_40_e8_32bs_e37_v28?0"CSVTUITrainingResult"8B16^20ls32l8
+ ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
+ ___block_descriptor_40_e8_32r_e25_v16?0"SSRVoiceProfile"8lr32l8
+ ___block_descriptor_40_e8_32r_e8_v16?0Q8lr32l8
+ ___block_descriptor_40_e8_32s_e18_v32?0q8i16B20^24ls32l8
+ ___block_descriptor_40_e8_32s_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_40_e8_32s_e37_v28?0"CSVTUITrainingResult"8B16^20ls32l8
+ ___block_descriptor_40_e8_32s_e8_v12?0B8ls32l8
+ ___block_descriptor_48_e8_32s40r_e25_v16?0"SSRVoiceProfile"8lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e31_v24?0"AFAccount"8"NSError"16lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e8_v16?0Q8lr40l8s32l8
+ ___block_descriptor_48_e8_32w40w_e5_v8?0lw32l8w40l8
+ ___block_descriptor_56_e8_32r40r48r_e23_v32?0Q8q16"NSError"24lr32l8r40l8r48l8
+ ___block_descriptor_57_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_57_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_61_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_65_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.1128
+ ___block_literal_global.1423
+ ___block_literal_global.2044
+ ___block_literal_global.2633
+ ___block_literal_global.2694
+ ___block_literal_global.3461
+ ___block_literal_global.3984
+ ___block_literal_global.4535
+ ___block_literal_global.4933
+ ___block_literal_global.5070
+ ___block_literal_global.5301
+ ___block_literal_global.5376
+ ___block_literal_global.5640
+ ___block_literal_global.5974
+ ___block_literal_global.976
+ __unnamed_array_storage.4626
+ __unnamed_array_storage.687
+ __unnamed_array_storage.688
+ _log
+ _objc_msgSend$CSVTUIRemoteTrainingSessionRMSAvailable:
+ _objc_msgSend$_connection
+ _objc_msgSend$_extractWithModelContext:completion:
+ _objc_msgSend$_forceFetchAudioProvider:recordContext:
+ _objc_msgSend$_getVTRepromptListAssetTypeString
+ _objc_msgSend$_handleXPCDisconnectedUnexpectedlyWithError:
+ _objc_msgSend$_hasCorrectInputAudioRouteFromHardwareConfiguration:
+ _objc_msgSend$_loadBitVectorData:
+ _objc_msgSend$_newConnection
+ _objc_msgSend$_resetupIfNeeded
+ _objc_msgSend$_service
+ _objc_msgSend$_setQueue:
+ _objc_msgSend$activateAudioSessionWithReason:dynamicAttribute:bundleID:error:
+ _objc_msgSend$activeConnection
+ _objc_msgSend$audioSourceWithCompletion:
+ _objc_msgSend$audioStreamWithRequest:streamName:error:
+ _objc_msgSend$blobName
+ _objc_msgSend$blobVersion
+ _objc_msgSend$bvData
+ _objc_msgSend$cancelTrainingForID:
+ _objc_msgSend$cancelTrainingViaXPCForID:
+ _objc_msgSend$cleanupViaXPCWithCompletion:
+ _objc_msgSend$cleanupWithCompletion:
+ _objc_msgSend$close
+ _objc_msgSend$contains:
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$dateWhenVoiceTriggerRePrompted
+ _objc_msgSend$decodeDoubleForKey:
+ _objc_msgSend$decodeInt32ForKey:
+ _objc_msgSend$defaultRequestWithContext:
+ _objc_msgSend$deviceConnectedWithUUID:
+ _objc_msgSend$didDetectForceEndPoint
+ _objc_msgSend$encodeDouble:forKey:
+ _objc_msgSend$encodeInt32:forKey:
+ _objc_msgSend$fakeVoiceTriggerRepromptAssetPath
+ _objc_msgSend$fetchActiveAccount:
+ _objc_msgSend$fetchRichDeviceUIDStringFromUUID:
+ _objc_msgSend$forceRePromptVoiceTrigger
+ _objc_msgSend$hash128WithKey:length:seed:
+ _objc_msgSend$initAndLoadImpactedAssistantIdsForRePrompt
+ _objc_msgSend$initAndLoadImpactedAssistantIdsForRePromptWithAsset:
+ _objc_msgSend$initWithAudioStreamHandleId:audioStreamType:audioRecordContext:audioRecorder:
+ _objc_msgSend$initWithDelegate:
+ _objc_msgSend$initWithExpectedNumberOfItems:falsePositiveRate:seed:
+ _objc_msgSend$initWithLocaleIdentifier:withAudioSession:withAppDomain:shouldTrainViaXPC:
+ _objc_msgSend$initWithMachServiceName:
+ _objc_msgSend$initWithMachServiceName:options:
+ _objc_msgSend$initWithNumberOfBits:
+ _objc_msgSend$initWithRecordType:deviceId:
+ _objc_msgSend$inputStreamWithFileAtPath:
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$isExclaveHardware
+ _objc_msgSend$isRePromptableWithAssistantId:
+ _objc_msgSend$isStreaming
+ _objc_msgSend$isVoiceTriggerRepromptAssetOverridingEnabled
+ _objc_msgSend$loadData:
+ _objc_msgSend$longLongValue
+ _objc_msgSend$messageHandler
+ _objc_msgSend$noAlertOption
+ _objc_msgSend$now
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$open
+ _objc_msgSend$playbackRoute
+ _objc_msgSend$prepareWithCompletion:
+ _objc_msgSend$processIdentifier
+ _objc_msgSend$processInfo
+ _objc_msgSend$queue
+ _objc_msgSend$read:maxLength:
+ _objc_msgSend$remoteObjectProxy
+ _objc_msgSend$resume
+ _objc_msgSend$setActiveConnection:
+ _objc_msgSend$setAtIndex:
+ _objc_msgSend$setAudioProviderDelegate:
+ _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$setClientIdentity:
+ _objc_msgSend$setContext:completion:
+ _objc_msgSend$setExportedInterface:
+ _objc_msgSend$setExportedObject:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setLatestRecordContext:streamType:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$setRemoteObjectProxy:
+ _objc_msgSend$setRequireSingleChannelLookup:
+ _objc_msgSend$setSelectedChannel:
+ _objc_msgSend$setupWithLocaleID:appDomain:
+ _objc_msgSend$speechIdentifier
+ _objc_msgSend$start
+ _objc_msgSend$startAudioStreamWithOption:completion:
+ _objc_msgSend$startRMS
+ _objc_msgSend$stopAudioStreamWithOption:completion:
+ _objc_msgSend$stopRMS
+ _objc_msgSend$systemUptime
+ _objc_msgSend$testAtIndex:
+ _objc_msgSend$trainUtterance:shouldUseASR:completion:
+ _objc_msgSend$trainUtterance:shouldUseASR:mhUUID:completionWithResult:
+ _objc_msgSend$trainUtteranceViaXPC:shouldUseASR:completion:
+ _objc_msgSend$trainUtteranceViaXPC:shouldUseASR:mhUUID:completionWithResult:
+ _objc_msgSend$unarchivedObjectOfClass:fromData:error:
+ _objc_msgSend$voiceProfileWithCompletion:
+ _objc_msgSend$voiceTriggerRePromptFinishedWithDate:
+ _objc_msgSend$vtuiTrainingXPCDisconnected
+ _objc_setProperty_nonatomic_copy
+ _sharedInstance.onceToken.2693
+ _sharedInstance.onceToken.5300
+ _sharedInstance.onceToken.5375
+ _sharedInstance.vtRepromptUtil
- +[CSOnDeviceCompilationUtils _getBaseNamingWithHashToUse:milName:configVersion:]
- +[CSOnDeviceCompilationUtils getBackendTypeFromModelFile:]
- +[CSOnDeviceCompilationUtils getCachedIrForPurgingWithMilName:configVersion:hashToUse:compileDir:]
- +[CSOnDeviceCompilationUtils getCachedIrsFromCSAsset:cachedIrDir:]
- +[CSOnDeviceCompilationUtils getIrNameFromModelNameForCompile:locale:assetVersion:hashToUse:]
- +[CSOnDeviceCompilationUtils getMilConfigFromMilFilePath:]
- +[CSOnDeviceCompilationUtils getModelNameFromMilFilePath:]
- +[CSOnDeviceCompilationUtils isBnnsIrNameForCurrentBuild:]
- +[CSOnDeviceCompilationUtils readMilFilePathFromConfig:]
- +[CSOnDeviceCompilationUtils sortCachedIrsByLastAccessTimeStamp:]
- +[CSUtils(AudioHardware) hasRemoteBuiltInMic]
- +[CSUtils(AudioHardware) isRemoteDarwinWithDeviceId:]
- +[CSUtils(LanguageCode) getSiriLanguageWithEndpointId:fallbackLanguage:]
- +[CSUtils(LanguageCode) getSiriLanguageWithFallback:]
- +[CSUtils(RecordContext) isRecordContextAutoPrompt:]
- +[CSUtils(RecordContext) isRecordContextBuiltInVoiceTrigger:]
- +[CSUtils(RecordContext) isRecordContextDarwinVoiceTrigger:]
- +[CSUtils(RecordContext) isRecordContextHearstDoubleTap:]
- +[CSUtils(RecordContext) isRecordContextHearstVoiceTrigger:]
- +[CSUtils(RecordContext) isRecordContextHomeButtonPress:]
- +[CSUtils(RecordContext) isRecordContextJarvisButtonPress:]
- +[CSUtils(RecordContext) isRecordContextJarvisVoiceTrigger:]
- +[CSUtils(RecordContext) isRecordContextRaiseToSpeak:]
- +[CSUtils(RecordContext) isRecordContextRemoraVoiceTrigger:]
- +[CSUtils(RecordContext) isRecordContextSpeakerIdTrainingTrigger:]
- +[CSUtils(RecordContext) isRecordContextVoiceTrigger:]
- +[CSUtils(RecordContext) isValidRecordContext:]
- +[CSUtils(RecordContext) recordContextString:]
- -[CSAudioRecordContext(AVVC) avvcContextSettings]
- -[CSVTUIAudioSessionRecorder _audioRecorder]
- -[CSVTUIAudioSessionRecorder audioRecorderBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:]
- -[CSVTUIAudioSessionRecorder audioRecorderDidStartRecord:audioStreamHandleId:successfully:error:]
- -[CSVTUIAudioSessionRecorder audioRecorderDidStopRecord:audioStreamHandleId:reason:]
- -[CSVTUIAudioSessionRecorder audioRecorderDisconnected:]
- -[CSVTUIAudioSessionRecorder audioRecorderRecordHardwareConfigurationDidChange:toConfiguration:]
- -[CSVTUIAudioSessionRecorder initWithAudioRecorder:forceSupportsRemoteDarwinDisplay:]
- GCC_except_table1124
- GCC_except_table1145
- GCC_except_table1152
- GCC_except_table1157
- GCC_except_table1173
- GCC_except_table1177
- GCC_except_table1181
- GCC_except_table1187
- GCC_except_table1195
- GCC_except_table1255
- GCC_except_table1259
- GCC_except_table1286
- GCC_except_table1355
- GCC_except_table1364
- GCC_except_table1380
- GCC_except_table1397
- GCC_except_table162
- GCC_except_table167
- GCC_except_table170
- GCC_except_table172
- GCC_except_table271
- GCC_except_table312
- GCC_except_table328
- GCC_except_table377
- GCC_except_table385
- GCC_except_table387
- GCC_except_table544
- GCC_except_table549
- GCC_except_table575
- GCC_except_table578
- GCC_except_table634
- GCC_except_table635
- GCC_except_table638
- GCC_except_table639
- GCC_except_table640
- GCC_except_table641
- GCC_except_table642
- GCC_except_table643
- GCC_except_table644
- GCC_except_table645
- GCC_except_table646
- GCC_except_table648
- GCC_except_table649
- GCC_except_table651
- GCC_except_table654
- GCC_except_table745
- GCC_except_table789
- GCC_except_table793
- GCC_except_table855
- GCC_except_table856
- GCC_except_table858
- GCC_except_table868
- GCC_except_table872
- GCC_except_table881
- GCC_except_table886
- GCC_except_table890
- GCC_except_table940
- GCC_except_table944
- GCC_except_table948
- GCC_except_table951
- GCC_except_table973
- _AFPreferencesMobileUserSessionLanguage
- _AVVoiceActivationDeviceIDKey
- _AVVoiceActivationModeKey
- _ExtAudioFileCreateWithURL
- _ExtAudioFileWrite
- _MGGetStringAnswer
- _NSFileModificationDate
- _OBJC_CLASS_$_CSKeywordAnalyzerNDAPIResult
- _OBJC_CLASS_$_CSOnDeviceCompilationUtils
- _OBJC_CLASS_$_NSSortDescriptor
- _OBJC_CLASS_$__TtC18SpeakerRecognition27CSVTUIKeywordDetectorHelper
- _OBJC_CLASS_$__TtC18SpeakerRecognition27CSVTUITrainingSessionHelper
- _OBJC_CLASS_$__TtC18SpeakerRecognition28CSPlainAudioFileWriterHelper
- _OBJC_CLASS_$__TtC18SpeakerRecognition28SSRVTUITrainingManagerHelper
- _OBJC_CLASS_$__TtC18SpeakerRecognition29SSRVoiceProfileComposerHelper
- _OBJC_CLASS_$__TtC18SpeakerRecognition30SSREnrollmentDataManagerHelper
- _OBJC_CLASS_$__TtC18SpeakerRecognition33CSVTUITrainingSessionHelperResult
- _OBJC_CLASS_$__TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper
- _OBJC_IVAR_$_CSVTUIAudioSessionRecorder._audioRecorder
- _OBJC_METACLASS_$_CSOnDeviceCompilationUtils
- _OBJC_METACLASS_$__TtC18SpeakerRecognition27CSVTUIKeywordDetectorHelper
- _OBJC_METACLASS_$__TtC18SpeakerRecognition27CSVTUITrainingSessionHelper
- _OBJC_METACLASS_$__TtC18SpeakerRecognition28CSPlainAudioFileWriterHelper
- _OBJC_METACLASS_$__TtC18SpeakerRecognition28SSRVTUITrainingManagerHelper
- _OBJC_METACLASS_$__TtC18SpeakerRecognition29SSRVoiceProfileComposerHelper
- _OBJC_METACLASS_$__TtC18SpeakerRecognition30SSREnrollmentDataManagerHelper
- _OBJC_METACLASS_$__TtC18SpeakerRecognition33CSVTUITrainingSessionHelperResult
- _OBJC_METACLASS_$__TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper
- __DATA__TtC18SpeakerRecognition27CSVTUIKeywordDetectorHelper
- __DATA__TtC18SpeakerRecognition27CSVTUITrainingSessionHelper
- __DATA__TtC18SpeakerRecognition28CSPlainAudioFileWriterHelper
- __DATA__TtC18SpeakerRecognition28SSRVTUITrainingManagerHelper
- __DATA__TtC18SpeakerRecognition29SSRVoiceProfileComposerHelper
- __DATA__TtC18SpeakerRecognition30SSREnrollmentDataManagerHelper
- __DATA__TtC18SpeakerRecognition33CSVTUITrainingSessionHelperResult
- __DATA__TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper
- __IVARS__TtC18SpeakerRecognition27CSVTUIKeywordDetectorHelper
- __IVARS__TtC18SpeakerRecognition27CSVTUITrainingSessionHelper
- __IVARS__TtC18SpeakerRecognition28CSPlainAudioFileWriterHelper
- __IVARS__TtC18SpeakerRecognition28SSRVTUITrainingManagerHelper
- __IVARS__TtC18SpeakerRecognition33CSVTUITrainingSessionHelperResult
- __IVARS__TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper
- __METACLASS_DATA__TtC18SpeakerRecognition27CSVTUIKeywordDetectorHelper
- __METACLASS_DATA__TtC18SpeakerRecognition27CSVTUITrainingSessionHelper
- __METACLASS_DATA__TtC18SpeakerRecognition28CSPlainAudioFileWriterHelper
- __METACLASS_DATA__TtC18SpeakerRecognition28SSRVTUITrainingManagerHelper
- __METACLASS_DATA__TtC18SpeakerRecognition29SSRVoiceProfileComposerHelper
- __METACLASS_DATA__TtC18SpeakerRecognition30SSREnrollmentDataManagerHelper
- __METACLASS_DATA__TtC18SpeakerRecognition33CSVTUITrainingSessionHelperResult
- __METACLASS_DATA__TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper
- __OBJC_$_CATEGORY_CSAsset_$_SpeakerRecognition
- __OBJC_$_CATEGORY_CSAudioRecordContext_$_AVVC
- __OBJC_$_CATEGORY_CSUtils_$_LanguageCode
- __OBJC_$_CLASS_METHODS_CSOnDeviceCompilationUtils
- __OBJC_$_CLASS_METHODS_CSUtils(LanguageCode|RecordContext|AudioHardware)
- __OBJC_$_INSTANCE_METHODS_CSAsset(SpeakerRecognition)
- __OBJC_$_INSTANCE_METHODS_CSAudioRecordContext(AVVC)
- __OBJC_$_INSTANCE_METHODS__TtC18SpeakerRecognition27CSVTUIKeywordDetectorHelper
- __OBJC_$_INSTANCE_METHODS__TtC18SpeakerRecognition27CSVTUITrainingSessionHelper
- __OBJC_$_INSTANCE_METHODS__TtC18SpeakerRecognition28CSPlainAudioFileWriterHelper
- __OBJC_$_INSTANCE_METHODS__TtC18SpeakerRecognition28SSRVTUITrainingManagerHelper
- __OBJC_$_INSTANCE_METHODS__TtC18SpeakerRecognition29SSRVoiceProfileComposerHelper
- __OBJC_$_INSTANCE_METHODS__TtC18SpeakerRecognition30SSREnrollmentDataManagerHelper
- __OBJC_$_INSTANCE_METHODS__TtC18SpeakerRecognition33CSVTUITrainingSessionHelperResult
- __OBJC_$_INSTANCE_METHODS__TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper
- __OBJC_$_PROP_LIST_NSObject.1101
- __OBJC_$_PROP_LIST_NSObject.1281
- __OBJC_$_PROP_LIST_NSObject.1622
- __OBJC_$_PROP_LIST_NSObject.1854
- __OBJC_$_PROP_LIST_NSObject.2219
- __OBJC_$_PROP_LIST_NSObject.2555
- __OBJC_$_PROP_LIST_NSObject.277
- __OBJC_$_PROP_LIST_NSObject.3143
- __OBJC_$_PROP_LIST_NSObject.3392
- __OBJC_$_PROP_LIST_NSObject.3621
- __OBJC_$_PROP_LIST_NSObject.3814
- __OBJC_$_PROP_LIST_NSObject.409
- __OBJC_$_PROP_LIST_NSObject.4153
- __OBJC_$_PROP_LIST_NSObject.4376
- __OBJC_$_PROP_LIST_NSObject.4431
- __OBJC_$_PROP_LIST_NSObject.4757
- __OBJC_$_PROP_LIST_NSObject.510
- __OBJC_$_PROP_LIST_NSObject.5354
- __OBJC_$_PROP_LIST_NSObject.5455
- __OBJC_$_PROP_LIST_NSObject.666
- __OBJC_$_PROP_LIST_SSRSpeakerRecognizer.2220
- __OBJC_$_PROP_LIST_SSRVoiceProfileRetrainer.1855
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioFileWriter
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVTUIAudioRecorderDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVTUIAudioSessionDelegate.3622
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVTUIAudioSessionDelegate.3815
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVTUIEndPointDelegate.3816
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1102
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1282
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1623
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1856
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2221
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2556
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.278
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3144
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3393
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3623
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3817
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.410
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4154
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4377
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4432
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4758
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.511
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5355
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5456
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.667
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVTUIAudioRecorderDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_EARSyncPSRAudioProcessorDelegate.1857
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1103
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1283
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1624
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1858
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2222
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2557
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.279
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3145
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3394
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3624
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3818
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.411
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4155
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4378
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4433
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4759
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.512
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5356
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5457
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.668
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SFSpeechRecognitionTaskDelegate.3819
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRAssetProviding.4434
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSRAssetProviding.4435
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSRSpeakerRecognizer.2223
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSRVoiceProfileRetrainer.1859
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioFileWriter
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVTUIAudioRecorderDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVTUIAudioSessionDelegate.3625
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVTUIAudioSessionDelegate.3820
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVTUIEndPointDelegate.3821
- __OBJC_$_PROTOCOL_METHOD_TYPES_EARSyncPSRAudioProcessorDelegate.1860
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1104
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1284
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1625
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1861
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2224
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2558
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.280
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3146
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3395
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3626
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3822
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.412
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4156
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4379
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4436
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4760
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.513
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5357
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5458
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.669
- __OBJC_$_PROTOCOL_METHOD_TYPES_SFSpeechRecognitionTaskDelegate.3823
- __OBJC_$_PROTOCOL_METHOD_TYPES_SSRAssetProviding.4437
- __OBJC_$_PROTOCOL_METHOD_TYPES_SSRSpeakerRecognizer.2225
- __OBJC_$_PROTOCOL_METHOD_TYPES_SSRVoiceProfileRetrainer.1862
- __OBJC_$_PROTOCOL_REFS_CSAudioFileWriter
- __OBJC_$_PROTOCOL_REFS_CSVTUIAudioRecorderDelegate
- __OBJC_$_PROTOCOL_REFS_CSVTUIAudioSessionDelegate.3627
- __OBJC_$_PROTOCOL_REFS_CSVTUIAudioSessionDelegate.3824
- __OBJC_$_PROTOCOL_REFS_CSVTUIEndPointDelegate.3825
- __OBJC_$_PROTOCOL_REFS_EARSyncPSRAudioProcessorDelegate.1863
- __OBJC_$_PROTOCOL_REFS_SFSpeechRecognitionTaskDelegate.3826
- __OBJC_$_PROTOCOL_REFS_SSRAssetProviding.4438
- __OBJC_$_PROTOCOL_REFS_SSRSpeakerRecognizer.2226
- __OBJC_$_PROTOCOL_REFS_SSRVoiceProfileRetrainer.1864
- __OBJC_CLASS_RO_$_CSOnDeviceCompilationUtils
- __OBJC_LABEL_PROTOCOL_$_CSAudioFileWriter
- __OBJC_LABEL_PROTOCOL_$_CSVTUIAudioRecorderDelegate
- __OBJC_METACLASS_RO_$_CSOnDeviceCompilationUtils
- __OBJC_PROTOCOL_$_CSAudioFileWriter
- __OBJC_PROTOCOL_$_CSVTUIAudioRecorderDelegate
- __PROPERTIES__TtC18SpeakerRecognition33CSVTUITrainingSessionHelperResult
- __PROTOCOLS__TtC18SpeakerRecognition27CSVTUIKeywordDetectorHelper
- __PROTOCOLS__TtC18SpeakerRecognition27CSVTUIKeywordDetectorHelper.3
- __PROTOCOLS__TtC18SpeakerRecognition28CSPlainAudioFileWriterHelper
- __PROTOCOLS__TtC18SpeakerRecognition28CSPlainAudioFileWriterHelper.3
- __PROTOCOLS__TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper
- __PROTOCOLS__TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper.3
- __PROTOCOL_INSTANCE_METHODS__TtP18SpeakerRecognition26CSVTUIKeywordDetectorSwift_
- __PROTOCOL_METHOD_TYPES__TtP18SpeakerRecognition26CSVTUIKeywordDetectorSwift_
- __PROTOCOL__TtP18SpeakerRecognition26CSVTUIKeywordDetectorSwift_
- ___108-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withLocale:withAsset:withCompletion:]_block_invoke.679
- ___108-[SSRVoiceProfileManager importVoiceProfile:appDomain:withSharedUserId:withLocale:withAsset:withCompletion:]_block_invoke.693
- ___48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.19
- ___48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.20
- ___48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.22
- ___48-[SSRVTUITrainingManager prepareWithCompletion:]_block_invoke.18
- ___96-[CSVTUIAudioSessionRecorder audioRecorderRecordHardwareConfigurationDidChange:toConfiguration:]_block_invoke
- ___Block_byref_object_copy_.1385
- ___Block_byref_object_copy_.1752
- ___Block_byref_object_copy_.2305
- ___Block_byref_object_copy_.2408
- ___Block_byref_object_copy_.2899
- ___Block_byref_object_copy_.3046
- ___Block_byref_object_copy_.3275
- ___Block_byref_object_copy_.3867
- ___Block_byref_object_copy_.4109
- ___Block_byref_object_copy_.4231
- ___Block_byref_object_copy_.4874
- ___Block_byref_object_copy_.586
- ___Block_byref_object_copy_.692
- ___Block_byref_object_dispose_.1386
- ___Block_byref_object_dispose_.1753
- ___Block_byref_object_dispose_.2306
- ___Block_byref_object_dispose_.2409
- ___Block_byref_object_dispose_.2900
- ___Block_byref_object_dispose_.3047
- ___Block_byref_object_dispose_.3276
- ___Block_byref_object_dispose_.3868
- ___Block_byref_object_dispose_.4110
- ___Block_byref_object_dispose_.4232
- ___Block_byref_object_dispose_.4875
- ___Block_byref_object_dispose_.587
- ___Block_byref_object_dispose_.693
- ___block_literal_global.1065
- ___block_literal_global.1708
- ___block_literal_global.2326
- ___block_literal_global.2936
- ___block_literal_global.3353
- ___block_literal_global.3877
- ___block_literal_global.4267
- ___block_literal_global.4403
- ___block_literal_global.4645
- ___block_literal_global.4718
- ___block_literal_global.4983
- ___block_literal_global.5315
- ___block_literal_global.701
- ___block_literal_global.749
- ___chkstk_darwin
- ___swift_instantiateConcreteTypeFromMangledName
- ___swift_memcpy1_1
- ___swift_memcpy40_8
- ___swift_noop_void_return
- __swiftEmptyArrayStorage
- __swift_stdlib_reportUnimplementedInitializer
- __unnamed_array_storage.3965
- __unnamed_array_storage.676
- __unnamed_array_storage.677
- _associated conformance 18SpeakerRecognition33CSVTUITrainingSessionHelperStatusOSHAASQ
- _malloc
- _objc_allocWithZone
- _objc_msgSend$_audioRecorder
- _objc_msgSend$_getBaseNamingWithHashToUse:milName:configVersion:
- _objc_msgSend$activateAudioSessionWithReason:streamHandleId:error:
- _objc_msgSend$audioStreamHandleId
- _objc_msgSend$fetchAllVoiceTriggerSecondPassRecognizer:
- _objc_msgSend$getCachedIrForPurgingWithMilName:configVersion:hashToUse:compileDir:
- _objc_msgSend$getModelNameFromMilFilePath:
- _objc_msgSend$getPlaybackRouteForStreamID:
- _objc_msgSend$initWithKey:ascending:
- _objc_msgSend$initWithLocaleIdentifier:withAudioSession:withAppDomain:
- _objc_msgSend$initWithMode:deviceUID:
- _objc_msgSend$isRecordContextAutoPrompt:
- _objc_msgSend$isRecordContextBuiltInVoiceTrigger:
- _objc_msgSend$isRecordContextDarwinVoiceTrigger:
- _objc_msgSend$isRecordContextHearstDoubleTap:
- _objc_msgSend$isRecordContextHearstVoiceTrigger:
- _objc_msgSend$isRecordContextJarvisVoiceTrigger:
- _objc_msgSend$isRecordContextRaiseToSpeak:
- _objc_msgSend$isRecordContextRemoraVoiceTrigger:
- _objc_msgSend$isRecordingWithStreamHandleId:
- _objc_msgSend$isRequestDuringActiveCall
- _objc_msgSend$languageCodeDarwin
- _objc_msgSend$pathComponents
- _objc_msgSend$prepareAudioStreamRecordWithStreamHandleId:error:
- _objc_msgSend$readMilFilePathFromConfig:
- _objc_msgSend$readValuesFromJsonFile:keyword:
- _objc_msgSend$recordRouteWithStreamHandleId:
- _objc_msgSend$registerObserver:
- _objc_msgSend$setActivationMode:
- _objc_msgSend$setAnnounceCallsEnabled:
- _objc_msgSend$sortedArrayUsingDescriptors:
- _objc_msgSend$startAudioStreamWithStreamHandleId:error:
- _objc_msgSend$stopAudioStreamWithStreamHandleId:error:
- _objc_msgSend$stringByStandardizingPath
- _objc_msgSend$supportHandsFree
- _objc_msgSend$supportRingtoneA2DP
- _objc_msgSend$unregisterObserver:
- _objc_msgSend$updateAudioRecorderForTrainingDevice:deviceUUIDs:
- _objc_opt_self
- _sharedInstance.onceToken.4644
- _sharedInstance.onceToken.4717
- _swift_allocObject
- _swift_beginAccess
- _swift_bridgeObjectRelease
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain
- _swift_deallocObject
- _swift_deallocPartialClassInstance
- _swift_dynamicCast
- _swift_endAccess
- _swift_errorRelease
- _swift_getErrorValue
- _swift_getForeignTypeMetadata
- _swift_getObjCClassMetadata
- _swift_getObjectType
- _swift_getTypeByMangledNameInContext2
- _swift_getWitnessTable
- _swift_isaMask
- _swift_once
- _swift_release
- _swift_release_n
- _swift_retain
- _swift_unknownObjectRelease
- _swift_unknownObjectRetain
- _swift_unknownObjectWeakAssign
- _swift_unknownObjectWeakDestroy
- _swift_unknownObjectWeakInit
- _swift_unknownObjectWeakLoadStrong
- _swift_willThrow
- _symbolic $s18SpeakerRecognition26CSVTUIKeywordDetectorSwiftP
- _symbolic $s18SpeakerRecognition35CSVTUITrainingSessionHelperDelegateP
- _symbolic $sSY
- _symbolic 18SpeakerRecognition26CSVTUIKeywordDetectorSwift_p
- _symbolic SS
- _symbolic Sb
- _symbolic Sd
- _symbolic Sf
- _symbolic Si
- _symbolic So12NSDictionaryC
- _symbolic So15SSRVoiceProfileCSg
- _symbolic So16CSPhraseDetectorC
- _symbolic So17CSAudioFileWriter_p
- _symbolic So21CSAudioCircularBufferC
- _symbolic So21CSVTUITrainingSessionCSgXw
- _symbolic So22CSKeywordAnalyzerNDAPICSg
- _symbolic So29SSRTriggerPhraseDetectorNDAPICSg
- _symbolic So30SSRVTUITrainingManagerDelegate_pSg
- _symbolic So5NSURLCSg
- _symbolic So7CSAssetCSg
- _symbolic So8NSObjectC
- _symbolic Su
- _symbolic _____ 18SpeakerRecognition27CSVTUIKeywordDetectorHelperC
- _symbolic _____ 18SpeakerRecognition27CSVTUITrainingSessionHelperC
- _symbolic _____ 18SpeakerRecognition28CSPlainAudioFileWriterHelperC
- _symbolic _____ 18SpeakerRecognition28SSRVTUITrainingManagerHelperC
- _symbolic _____ 18SpeakerRecognition29SSRVoiceProfileComposerHelperC
- _symbolic _____ 18SpeakerRecognition30SSREnrollmentDataManagerHelperC
- _symbolic _____ 18SpeakerRecognition33CSVTUITrainingSessionHelperResultC
- _symbolic _____ 18SpeakerRecognition33CSVTUITrainingSessionHelperStatusO
- _symbolic _____ 18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelperC
- _symbolic _____ 18SpeakerRecognition7VTEIKeyV
- _symbolic _____ So27AudioStreamBasicDescriptionV
- _symbolic _____ s6UInt32V
- _symbolic _____Sg s13OpaquePointerV
- _symbolic _____SgXw 18SpeakerRecognition27CSVTUITrainingSessionHelperC
- _symbolic ______p s7CVarArgP
- _symbolic ______pSg s7CVarArgP
- _symbolic ______pSgXw 18SpeakerRecognition35CSVTUITrainingSessionHelperDelegateP
- _symbolic _____y______pG s23_ContiguousArrayStorageC s7CVarArgP
- _symbolic _____yyp_yptG s23_ContiguousArrayStorageC
- _symbolic x
- _symbolic ypSg
CStrings:
+ "\x02\x13\x14"
+ "\x03!"
+ "\x17(\x11!"
+ "#SPKERAT v001\n\n\n"
+ "%s ::: Error creating json RePrompt Metadata: %{public}@"
+ "%s Active Assistant Account is %@"
+ "%s Already RePrompted on %@"
+ "%s AssistantId required RePrompt"
+ "%s AudioStream is already recording, do not prepare anymore"
+ "%s Blob file not found at path : %{public}@"
+ "%s Bloom filter inference to check if ID exists took %{public}.3fms"
+ "%s Cannot prepare since audio provider does not exist"
+ "%s Checking if already reprompted..."
+ "%s Checking if isVoiceTriggerRepromptRequired..."
+ "%s Clearing the VT enable flag upon profile sync"
+ "%s Creating new xpc connection..."
+ "%s Done VoiceTriggerRePromptFinised!"
+ "%s ERR: path is nil - Bailing out"
+ "%s Extracting profile from : %@"
+ "%s Failed to create audio recorder : %{public}@"
+ "%s Failed to get audio stream handle ID : %{publid}@"
+ "%s Failed to startAudioStream since audioStream not existing"
+ "%s Failed to unarchive blob with err: %{public}@"
+ "%s Fetched assetStr: %{public}@ for deviceType: %{public}@"
+ "%s Fetching active account using AFSettingConnection..."
+ "%s For Context : %{public}@, audioStreamId(%llu) has allocated"
+ "%s Force re-prompt enabled. Continuing with RePrompt.."
+ "%s Force re-prompt preference config value %@"
+ "%s Got new connection on attending service: %@"
+ "%s Invalid listener - %{public}@"
+ "%s Json-Err reading metaVersionDict: %{public}@: err: %{public}@"
+ "%s No asset found, nothing to do"
+ "%s Not RePrompted before"
+ "%s Not-implemented"
+ "%s Re-setup training service due to xpc rebuilt"
+ "%s RePrompt is not required. Return false."
+ "%s RePrompted on %@"
+ "%s Result of isVoiceTriggerRepromptRequired is %@..."
+ "%s Running VoiceTriggerRePromptFinised..."
+ "%s SSRVTUITrainingListener start listening"
+ "%s Setting up AFSettingsConnection..."
+ "%s Storing VoiceTriggerRePromptFinished on date %@"
+ "%s Successfully prepared record"
+ "%s Timedout waiting for AFSettingsConnection:fetchActiveAccount: %{public}ld, waitedFor: %{public}d, Returning false"
+ "%s Unsupported blob version %@"
+ "%s Update to latest record context with device type: %zu, Remote device UUID list: %{private}@"
+ "%s [Service:%{public}@] Listener Interruption Handler: %{public}@, client PID: %{public}d)"
+ "%s [Service:%{public}@] Listener Invalidation Handler: %{public}@, client PID: %{public}d exited"
+ "%s _expectedNumberOfItems: %lu\n _falsePositiveRate: %f\n _numberOfBits: %lu\n _numberHashes: %lu\n seed: %lu\n BitVector: %@\n"
+ "%s audioProvider already exists and force == %d, return the current one."
+ "%s audioSource : %lu"
+ "%s cannot extract profile embedding : context is nil"
+ "%s cannot extract profile embedding : cookie match failed %d %d"
+ "%s cannot extract profile embedding : inputStream = nil, %@"
+ "%s cannot extract profile embedding : model context is nil"
+ "%s cannot extract profile embedding : modelContext = nil"
+ "%s cannot extract profile embedding : profileURL = nil"
+ "%s cannot read enough data from file:"
+ "%s cannot read incompatible version"
+ "%s end training and clean up"
+ "%s failed to stopRecording since audioStream not existing"
+ "%s hardwareConfig: %ld"
+ "%s header specifies implausible filesize"
+ "%s isVoiceTriggerRePrompt required check if re prompt is required took %{public}.3fms"
+ "%s localeIdentifier : %{public}@, appDomain : %{public}@"
+ "%s not-implemented. return false."
+ "%s only float32 dataformat supported"
+ "%s speechIdentifier is %@"
+ "%s stride is less than width"
+ "%s timeToRet(AFSettingsConnection:fetchActiveAccount:): %{public}fms"
+ "%s unexpected file size"
+ "%s utterance: %ld, shouldUseASR : %d"
+ "%s utterance: %ld, shouldUseASR : %d, mhuuid : %@"
+ "%s xpc connection %@ Interrupted"
+ "%s xpc connection %@ Invalidated"
+ "*"
+ "+[SSRSpeakerProfileEmbeddingExtractor _extractWithModelContext:completion:]"
+ "+[SSRSpeakerProfileEmbeddingExtractor extractPSRVoiceProfileWithContext:completion:]"
+ "+[SSRSpeakerProfileEmbeddingExtractor extractSATVoiceProfileWithContext:completion:]"
+ "+[SSRVoiceProfileManager clearVTEnableAfterProfileSyncFlag]"
+ "+[SSRVoiceProfileMetadataManager readVoiceTriggerRePromptMetadata:]"
+ "+[SSRVoiceProfileMetadataManager saveVoiceTriggeRePromptMetadata:]"
+ "-[BloomFilter initWithExpectedNumberOfItems:falsePositiveRate:seed:]"
+ "-[CSVTUIAudioSessionRecorder _forceFetchAudioProvider:recordContext:]"
+ "-[CSVTUIAudioSessionRecorder _hasCorrectInputAudioRouteFromHardwareConfiguration:]"
+ "-[CSVTUIAudioSessionRecorder stopRecording]_block_invoke"
+ "-[CSVTUIAudioSessionRecorder updateAudioRecorderForTrainingDevice:deviceUUIDs:]"
+ "-[SSRMobileAssetProvider _getVTRepromptListAssetTypeString]"
+ "-[SSRVTUITrainingListener listen]"
+ "-[SSRVTUITrainingListener listener:shouldAcceptNewConnection:]"
+ "-[SSRVTUITrainingListener listener:shouldAcceptNewConnection:]_block_invoke_2"
+ "-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke_2"
+ "-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke_3"
+ "-[SSRVTUITrainingManager prepareWithCompletion:]_block_invoke_3"
+ "-[SSRVTUITrainingManager trainUtterance:shouldUseASR:completion:]_block_invoke_5"
+ "-[SSRVTUITrainingManager trainUtterance:shouldUseASR:mhUUID:completionWithResult:]_block_invoke_5"
+ "-[SSRVTUITrainingMessageHandler audioSourceWithCompletion:]"
+ "-[SSRVTUITrainingMessageHandler cancelTrainingViaXPCForID:]"
+ "-[SSRVTUITrainingMessageHandler cleanupViaXPCWithCompletion:]"
+ "-[SSRVTUITrainingMessageHandler setupWithLocaleID:appDomain:]"
+ "-[SSRVTUITrainingMessageHandler trainUtteranceViaXPC:shouldUseASR:completion:]"
+ "-[SSRVTUITrainingMessageHandler trainUtteranceViaXPC:shouldUseASR:mhUUID:completionWithResult:]"
+ "-[SSRVTUITrainingMessageHandler voiceProfileWithCompletion:]"
+ "-[SSRVTUITrainingMessageHandler vtuiTrainingXPCDisconnected]"
+ "-[SSRVTUITrainingServiceClient _connection]"
+ "-[SSRVTUITrainingServiceClient _connection]_block_invoke"
+ "-[SSRVTUITrainingServiceClient _handleXPCDisconnectedUnexpectedlyWithError:]"
+ "-[SSRVTUITrainingServiceClient _resetupIfNeeded]"
+ "-[SSRVTUITrainingServiceClient initWithDelegate:]"
+ "-[SSRVTUITrainingServiceClient invalidate]_block_invoke"
+ "-[SSRVTUITrainingServiceClient setupWithLocaleID:appDomain:]_block_invoke"
+ "-[SSRVoiceProfileManager isVoiceTriggerRepromptRequiredWithCompletion:]"
+ "-[SSRVoiceProfileManager isVoiceTriggerRepromptRequired]"
+ "-[SSRVoiceProfileManager isVoiceTriggerRepromptRequired]_block_invoke"
+ "-[SSRVoiceProfileManager voiceTriggerRepromptFinishedWithCompletion:]"
+ "-[SSRVoiceProfileManager voiceTriggerRepromptFinished]"
+ "-[VoiceTriggerRePromptUtil initAndLoadImpactedAssistantIdsForRePromptWithAsset:]"
+ "-[VoiceTriggerRePromptUtil initAndLoadImpactedAssistantIdsForRePrompt]"
+ "-[VoiceTriggerRePromptUtil isRePromptableWithAssistantId:]"
+ "@"
+ "@\"<SSRVTUITrainingServiceDelegate>\""
+ "@\"BitVector\""
+ "@\"BloomFilter\""
+ "@\"CSAudioProvider\""
+ "@\"CSAudioStream\""
+ "@\"NSXPCConnection\""
+ "@\"NSXPCListener\""
+ "@\"SSRVTUITrainingManager\""
+ "@\"SSRVTUITrainingMessageHandler\""
+ "@\"SSRVTUITrainingServiceClient\""
+ "@28@0:8B16@20"
+ "@36@0:8Q16d24I32"
+ "@44@0:8@16@24@32B40"
+ "@?16@0:8"
+ "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
+ "BitVector"
+ "BloomFilter"
+ "CSAudioProviderDelegate"
+ "CSAudioStreamProvidingDelegate"
+ "CSVTUIRemoteTrainingSessionRMSAvailable:"
+ "HACBuiltIn"
+ "I16@0:8"
+ "MurmurHasher"
+ "NSXPCListenerDelegate"
+ "RePrompt_Date"
+ "RePrompt_Finished"
+ "SSRBitVector-Data"
+ "SSRBloomFilter-FalsePositiveRate"
+ "SSRBloomFilter-NumItems"
+ "SSRBloomFilter-Seed"
+ "SSRSpeakerProfileEmbeddingExtractor"
+ "SSRVTUITrainingListener"
+ "SSRVTUITrainingListener Queue"
+ "SSRVTUITrainingMessageHandler"
+ "SSRVTUITrainingService"
+ "SSRVTUITrainingServiceClient"
+ "SSRVTUITrainingServiceDelegate"
+ "T@\"<SSRVTUITrainingServiceDelegate>\",&,N,V_remoteObjectProxy"
+ "T@\"<SSRVTUITrainingServiceDelegate>\",W,N,V_delegate"
+ "T@\"BloomFilter\",&,V_bloomFilter"
+ "T@\"NSData\",R,C,V_bvData"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSXPCConnection\",&,N,V_activeConnection"
+ "T@\"NSXPCConnection\",&,N,V_xpcConnection"
+ "T@\"NSXPCListener\",&,N,V_listener"
+ "T@\"SSRVTUITrainingManager\",&,N,V_trainingManager"
+ "T@\"SSRVTUITrainingMessageHandler\",&,N,V_messageHandler"
+ "T@,&,N,V_remoteObjectProxy"
+ "T@?,C,N,V_cleanupCompletion"
+ "T@?,C,N,V_prepareCompletion"
+ "T@?,C,N,V_trainCompletion"
+ "T@?,C,N,V_trainCompletionWithResult"
+ "TB,N,V_requireResetup"
+ "TI,R,V_seed"
+ "TQ,R,V_expectedNumberOfItems"
+ "TQ,R,V_numberOfBytes"
+ "TRUE"
+ "Td,R,V_falsePositiveRate"
+ "Tq,R,V_numberOfBits"
+ "VTReprompt"
+ "VTUITrainingAudioStatus"
+ "VTUITrainingResultSessionId"
+ "VTUITrainingResultStatus"
+ "VoiceTriggerRePromptUtil"
+ "_activeConnection"
+ "_audioProvider"
+ "_audioStream"
+ "_bitShift"
+ "_bitVector"
+ "_bitsPerBlock"
+ "_bloomFilter"
+ "_bvData"
+ "_data"
+ "_expectedNumberOfItems"
+ "_extractWithModelContext:completion:"
+ "_falsePositiveRate"
+ "_forceFetchAudioProvider:recordContext:"
+ "_getVTRepromptListAssetTypeString"
+ "_getVTRepromptListCurrentCompatibilityVersion"
+ "_handleXPCDisconnectedUnexpectedlyWithError:"
+ "_hasCorrectInputAudioRouteFromHardwareConfiguration:"
+ "_listener"
+ "_loadBitVectorData:"
+ "_localeIdentifier"
+ "_messageHandler"
+ "_newConnection"
+ "_numberHashes"
+ "_numberOfBits"
+ "_numberOfBytes"
+ "_prepareCompletion"
+ "_remoteObjectProxy"
+ "_requireResetup"
+ "_resetupIfNeeded"
+ "_seed"
+ "_service"
+ "_setQueue:"
+ "_shouldTrainViaXPC"
+ "_trainCompletion"
+ "_trainCompletionWithResult"
+ "_trainingManager"
+ "_trainingServiceClient"
+ "activateAudioSessionWithReason:dynamicAttribute:bundleID:error:"
+ "activeConnection"
+ "add:"
+ "audioProviderInvalidated:streamHandleId:"
+ "audioSourceWithCompletion:"
+ "audioStreamProvider:audioBufferAvailable:"
+ "audioStreamProvider:audioChunkForTVAvailable:"
+ "audioStreamProvider:didHardwareConfigurationChange:"
+ "audioStreamProvider:didStopStreamUnexpectedly:"
+ "audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:"
+ "audioStreamWithRequest:streamName:error:"
+ "blobName"
+ "blobVersion"
+ "bloomFilter"
+ "bvData"
+ "cancelTrainingViaXPCForID:"
+ "cleanupCompletion"
+ "cleanupViaXPCWithCompletion:"
+ "clearVTEnableAfterProfileSyncFlag"
+ "close"
+ "com.apple.MobileAsset.VoiceTriggerRePromptListiPad"
+ "com.apple.MobileAsset.VoiceTriggerRePromptListiPhone12AndOlder"
+ "com.apple.MobileAsset.VoiceTriggerRePromptListiPhone13x"
+ "com.apple.MobileAsset.VoiceTriggerRePromptListiPhone14x"
+ "com.apple.MobileAsset.VoiceTriggerRePromptListiPhone15x"
+ "com.apple.VoiceTriggerUI.TrainingService"
+ "com.apple.siri.ssrvtuitrainingservice.xpc"
+ "contains:"
+ "dataUsingEncoding:"
+ "dataWithLength:"
+ "dateWhenVoiceTriggerRePrompted"
+ "decodeDoubleForKey:"
+ "decodeInt32ForKey:"
+ "defaultRequestWithContext:"
+ "deviceConnectedWithUUID:"
+ "encodeDouble:forKey:"
+ "encodeInt32:forKey:"
+ "expectedNumberOfItems"
+ "extractPSRVoiceProfileWithContext:completion:"
+ "extractSATVoiceProfileWithContext:completion:"
+ "fakeVoiceTriggerRepromptAssetPath"
+ "falsePositiveRate"
+ "fetchActiveAccount:"
+ "fetchRichDeviceUIDStringFromUUID:"
+ "forceRePromptVoiceTrigger"
+ "hash128WithKey:length:seed:"
+ "iPhone14,2"
+ "iPhone14,3"
+ "iPhone14,4"
+ "iPhone14,5"
+ "iPhone14,6"
+ "iPhone14,7"
+ "iPhone14,8"
+ "iPhone15,2"
+ "iPhone15,3"
+ "iPhone15,4"
+ "iPhone15,5"
+ "iPhone16,1"
+ "iPhone16,2"
+ "initAndLoadImpactedAssistantIdsForRePrompt"
+ "initAndLoadImpactedAssistantIdsForRePromptWithAsset:"
+ "initWithAudioProvider:forceSupportsRemoteDarwinDisplay:"
+ "initWithAudioStreamHandleId:audioStreamType:audioRecordContext:audioRecorder:"
+ "initWithDelegate:"
+ "initWithExpectedNumberOfItems:falsePositiveRate:seed:"
+ "initWithLocaleIdentifier:withAudioSession:withAppDomain:shouldTrainViaXPC:"
+ "initWithMachServiceName:"
+ "initWithMachServiceName:options:"
+ "initWithMessageHandler:"
+ "initWithNumberOfBits:"
+ "initWithRecordType:deviceId:"
+ "inputStreamWithFileAtPath:"
+ "interfaceWithProtocol:"
+ "isExclaveHardware"
+ "isRePromptableWithAssistantId:"
+ "isStreaming"
+ "isVoiceTriggerRepromptAssetOverridingEnabled"
+ "isVoiceTriggerRepromptRequired"
+ "isVoiceTriggerRepromptRequiredWithCompletion:"
+ "listen"
+ "listener"
+ "listener:shouldAcceptNewConnection:"
+ "loadData:"
+ "longLongValue"
+ "messageHandler"
+ "noAlertOption"
+ "now"
+ "numBits %lu, dataLen %lu"
+ "numberOfBits"
+ "numberOfBytes"
+ "numberWithLongLong:"
+ "open"
+ "playbackRoute"
+ "prepareCompletion"
+ "processIdentifier"
+ "processInfo"
+ "read:maxLength:"
+ "readVoiceTriggerRePromptMetadata:"
+ "remoteObjectProxy"
+ "requireResetup"
+ "resume"
+ "saveVoiceTriggeRePromptMetadata:"
+ "seed"
+ "setActiveConnection:"
+ "setAtIndex:"
+ "setAudioProviderDelegate:"
+ "setBloomFilter:"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "setCleanupCompletion:"
+ "setClientIdentity:"
+ "setContext:completion:"
+ "setExportedInterface:"
+ "setExportedObject:"
+ "setInterruptionHandler:"
+ "setInvalidationHandler:"
+ "setLatestRecordContext:streamType:"
+ "setListener:"
+ "setMessageHandler:"
+ "setPrepareCompletion:"
+ "setRemoteObjectInterface:"
+ "setRemoteObjectProxy:"
+ "setRequireResetup:"
+ "setRequireSingleChannelLookup:"
+ "setSelectedChannel:"
+ "setTrainCompletion:"
+ "setTrainCompletionWithResult:"
+ "setTrainingManager:"
+ "setupWithLocaleID:appDomain:"
+ "speechIdentifier"
+ "start"
+ "startAudioStreamWithOption:completion:"
+ "stopAudioStreamWithOption:completion:"
+ "systemUptime"
+ "testAtIndex:"
+ "trainCompletion"
+ "trainCompletionWithResult"
+ "trainUtteranceViaXPC:shouldUseASR:completion:"
+ "trainUtteranceViaXPC:shouldUseASR:mhUUID:completionWithResult:"
+ "trainingManager"
+ "unarchivedObjectOfClass:fromData:error:"
+ "v12@?0B8"
+ "v16@?0@\"SSRVoiceProfile\"8"
+ "v16@?0Q8"
+ "v24@0:8@\"NSString\"16"
+ "v24@0:8@?<v@?>16"
+ "v24@0:8@?<v@?@\"SSRVoiceProfile\">16"
+ "v24@0:8@?<v@?B>16"
+ "v24@0:8@?<v@?Q>16"
+ "v24@?0@\"AFAccount\"8@\"NSError\"16"
+ "v28@?0@\"CSVTUITrainingResult\"8B16^@20"
+ "v32@0:8@\"<CSAudioStreamProviding>\"16@\"CSAudioChunk\"24"
+ "v32@0:8@\"<CSAudioStreamProviding>\"16@\"CSAudioChunkForTV\"24"
+ "v32@0:8@\"<CSAudioStreamProviding>\"16q24"
+ "v32@0:8@\"CSAudioProvider\"16Q24"
+ "v32@0:8@\"NSString\"16@\"NSString\"24"
+ "v32@?0@\"NSData\"8I16I20@\"NSError\"24"
+ "v32@?0Q8q16@\"NSError\"24"
+ "v32@?0q8i16B20^@24"
+ "v36@0:8q16B24@?28"
+ "v36@0:8q16B24@?<v@?qiB^@>28"
+ "v44@0:8q16B24@\"NSUUID\"28@?<v@?@\"CSVTUITrainingResult\"B^@>36"
+ "v44@0:8q16B24@28@?36"
+ "v56@0:8@\"<CSAudioStreamProviding>\"16Q24Q32Q40Q48"
+ "v56@0:8@16Q24Q32Q40Q48"
+ "voiceProfileWithCompletion:"
+ "voiceTriggerRePromptFinishedWithDate:"
+ "voiceTriggerRepromptFinished"
+ "voiceTriggerRepromptFinishedWithCompletion:"
+ "vtuiTrainingXPCDisconnected"
+ "yyyy-MM-dd HH:mm:ss"
+ "{?=QQ}36@0:8r^v16Q24I32"
+ "\xf0a"
- "\x02!"
- "\x17(!"
- "%@-%@-%@-%@"
- "%s %{public}lu %s %{public}lu (%{public}lu, %{public}lu, %{public}lu)"
- "%s AudioRecorder creation failed : %@"
- "%s AudioRecorder is already recording, do not prepare anymore"
- "%s AudioStream Handle ID is invalid : %{public}@"
- "%s Cannot prepare since audio recorder does not exist"
- "%s Failed to query language code with endpointId %@, trying legacy query"
- "%s Failed to startAudioStream : %{public}@"
- "%s Invalid device with deviceId %{public}@"
- "%s Setting mixable to yes as we are in an active call"
- "%s Siri language is nil, falling back to %@"
- "%s audioRecorder %p created"
- "%s cachedIrs info sorted by timestamps: %@"
- "%s endpointUUID not provided, fallback to legacy query"
- "%{public}s called"
- "+[CSOnDeviceCompilationUtils sortCachedIrsByLastAccessTimeStamp:]"
- "+[CSUtils(AudioHardware) isRemoteDarwinWithDeviceId:]"
- "+[CSUtils(LanguageCode) getSiriLanguageWithEndpointId:fallbackLanguage:]"
- "+[CSUtils(LanguageCode) getSiriLanguageWithFallback:]"
- "-%@"
- "-.*.%@$"
- "-[CSAudioRecordContext(AVVC) avvcContextSettings]"
- "-[CSVTUIAudioSessionRecorder _audioRecorder]"
- "-[SSRVTUITrainingManager prepareWithCompletion:]_block_invoke"
- "-[SSRVTUITrainingManager trainUtterance:shouldUseASR:completion:]_block_invoke_2"
- "-[SSRVTUITrainingManager trainUtterance:shouldUseASR:mhUUID:completionWithResult:]_block_invoke_2"
- "."
- ".bnns.mil"
- ".mil"
- "::: Error creating output file %{public}@, err: %{public}d"
- "::: Error writing to output wave file. : %{public}ld"
- "@\"CSVTUIAudioRecorder\""
- "@\"NSData\"24@0:8@\"NSDictionary\"16"
- "@\"NSDictionary\"24@0:8@\"NSData\"16"
- "@24@0:8@\"CSAsset\"16"
- "AVVC"
- "AudioHardware"
- "B32@0:8^v16Q24"
- "B32@0:8r^v16Q24"
- "BuildVersion"
- "CSAudioFileWriter"
- "CSOnDeviceCompilationUtils"
- "CSVTUIAudioRecorderDelegate"
- "CSVoiceTriggerAsset found: %{public}@"
- "Cannot create CSVTUIKeywordDetector since there is no asset available"
- "Cannot create CSVTUIKeywordDetector since we cannot initialize NDAPI"
- "Cannot create json file : %{public}@"
- "Cannot find voicetrigger asset from asset manager, let's fallback to asset in the framework"
- "Discarding surplus audio of"
- "ERR: Failed to save explicit utterance"
- "ERR: called with nil metaPath"
- "ERR: called with nil uttMeta"
- "ERR: called with nil uttPath"
- "Failed to addSamples to CSAudioFileWriter: %{public}@"
- "Failed to endAudio on CSAudioFileWriter: %{public}@"
- "LanguageCode"
- "Phrase detector result: %@"
- "RecordContext"
- "Report as rejection since the detected phId is not the default"
- "SELF MATCHES %@"
- "Saving %{public}@ at %{public}@ as %{public}@ training."
- "Second pass has required audio, stop feeding"
- "SpeakerRecognition.CSPlainAudioFileWriterHelper"
- "SpeakerRecognition.CSVTUIKeywordDetectorHelper"
- "SpeakerRecognition.CSVTUITrainingSessionHelper"
- "SpeakerRecognition.CSVTUITwoPassKeywordDetectorHelper"
- "SpeakerRecognition.SSRVTUITrainingManagerHelper"
- "TB,N,VisTriggerEvent"
- "TB,N,VisUtteranceSaved"
- "TQ,N,VtriggerEndSampleCount"
- "TQ,N,VtriggerStartSampleCount"
- "TQ,N,VtriggeredPhId"
- "Tf,N,VtriggerScore"
- "Triggered! Event info: %{public}@\n%{public}9lld %{public}9lld %{public}9lld"
- "Waiting for the entire audio.."
- "^"
- "_TtC18SpeakerRecognition27CSVTUIKeywordDetectorHelper"
- "_TtC18SpeakerRecognition27CSVTUITrainingSessionHelper"
- "_TtC18SpeakerRecognition28CSPlainAudioFileWriterHelper"
- "_TtC18SpeakerRecognition28SSRVTUITrainingManagerHelper"
- "_TtC18SpeakerRecognition29SSRVoiceProfileComposerHelper"
- "_TtC18SpeakerRecognition30SSREnrollmentDataManagerHelper"
- "_TtC18SpeakerRecognition33CSVTUITrainingSessionHelperResult"
- "_TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper"
- "_TtP18SpeakerRecognition26CSVTUIKeywordDetectorSwift_"
- "__swift_setObject:forKeyedSubscript:"
- "_audioRecorder"
- "_getBaseNamingWithHashToUse:milName:configVersion:"
- "analyzeWithBuffer:"
- "analyzerTrailingSamples"
- "analyzing.... score so far: %{public}5.3f (%{public}ld)"
- "audioBuffer"
- "audioRecorderDisconnected:"
- "auto"
- "bestTriggerSampleStart"
- "bnnsir"
- "carplay"
- "closeSession"
- "config"
- "currentAsset"
- "fFile"
- "fetchAllVoiceTriggerSecondPassRecognizer:"
- "fileURL"
- "getAnalyzedResults"
- "getBackendTypeFromModelFile:"
- "getCachedIrForPurgingWithMilName:configVersion:hashToUse:compileDir:"
- "getCachedIrsFromCSAsset:cachedIrDir:"
- "getCurrentAsset"
- "getInstalledAssetForLanguage:"
- "getIrNameFromModelNameForCompile:locale:assetVersion:hashToUse:"
- "getMilConfigFromMilFilePath:"
- "getModelNameFromMilFilePath:"
- "handleAudioInputPayloadWithData:"
- "handleAudioInputWithData:"
- "hearst"
- "inASBD"
- "init()"
- "initWithAudioRecorder:forceSupportsRemoteDarwinDisplay:"
- "initWithKey:ascending:"
- "initWithLocale:keywordDetector:trainingManagerHelper:session:"
- "initWithLocaleIdentifier:"
- "initWithMode:deviceUID:"
- "initWithProfile:withDelegate:"
- "isBnnsIrNameForCurrentBuild:"
- "isRecordContextAutoPrompt:"
- "isRecordContextBuiltInVoiceTrigger:"
- "isRecordContextDarwinVoiceTrigger:"
- "isRecordContextHearstDoubleTap:"
- "isRecordContextHearstVoiceTrigger:"
- "isRecordContextHomeButtonPress:"
- "isRecordContextJarvisButtonPress:"
- "isRecordContextJarvisVoiceTrigger:"
- "isRecordContextRaiseToSpeak:"
- "isRecordContextRemoraVoiceTrigger:"
- "isRecordContextSpeakerIdTrainingTrigger:"
- "isRecordContextVoiceTrigger:"
- "isRemoteDarwinWithDeviceId:"
- "isRequestDuringActiveCall"
- "isUtteranceSaved"
- "isValidRecordContext:"
- "isWriting"
- "keywordAnalyzer"
- "keywordDetector"
- "keywordThreshold"
- "languageCodeDarwin"
- "lastKeywordScore"
- "lastModificationTime"
- "mil"
- "model-file"
- "numSamplesFed"
- "numSamplesToWrite %{public}lu"
- "outASBD"
- "pathComponents"
- "phraseDetector"
- "profile"
- "raisetospeak"
- "readMilFilePathFromConfig:"
- "readValuesFromJsonFile:keyword:"
- "recogrecognizerScaleFactornizerScore"
- "recordContextString:"
- "retrieveAndStoreUtteranceWithLocale:"
- "samples, audio sample available"
- "session"
- "sessionProcess"
- "sessionSuspended"
- "setActivationMode:"
- "setAnnounceCallsEnabled:"
- "setIsTriggerEvent:"
- "setIsUtteranceSaved:"
- "setLocaleIdentifierWithLocaleIdentifier:"
- "setProfileAndDelegateWithProfile:withDelegate:"
- "setTriggerEndSampleCount:"
- "setTriggerScore:"
- "setTriggerStartSampleCount:"
- "setTriggeredPhId:"
- "setupPhraseSpotter()"
- "sortCachedIrsByLastAccessTimeStamp:"
- "sortedArrayUsingDescriptors:"
- "status"
- "stringByStandardizingPath"
- "supportHandsFree"
- "supportRingtoneA2DP"
- "supportsMph"
- "trainingManagerHelper"
- "triggeredPhId"
- "triggeredUtteranceWithVoiceTriggerEventInfo:"
- "v24@0:8@\"CSVTUIAudioRecorder\"16"
- "v32@0:8@\"CSVTUIAudioRecorder\"16q24"
- "v40@0:8@\"CSVTUIAudioRecorder\"16Q24q32"
- "v44@0:8@\"CSVTUIAudioRecorder\"16Q24B32@\"NSError\"36"
- "v68@0:8@\"CSVTUIAudioRecorder\"16Q24@\"NSData\"32@\"NSData\"40Q48Q56i64"
- "v68@0:8@16Q24@32@40Q48Q56i64"
- "voic"
- "voiceProfileAudioDirPathForSpidType:toProfile:"
- "\xf0A"

```
