## Speech

> `/System/Library/Frameworks/Speech.framework/Speech`

```diff

-3301.14.1.1.1
-  __TEXT.__text: 0x10c908
-  __TEXT.__auth_stubs: 0x2550
-  __TEXT.__objc_methlist: 0x2860
-  __TEXT.__const: 0x5ae8
-  __TEXT.__cstring: 0x7b09
-  __TEXT.__constg_swiftt: 0x2f1c
-  __TEXT.__swift5_typeref: 0x3678
-  __TEXT.__swift5_reflstr: 0x19c8
-  __TEXT.__swift5_fieldmd: 0x1ba0
+3302.15.1.0.0
+  __TEXT.__text: 0x117a20
+  __TEXT.__auth_stubs: 0x25d0
+  __TEXT.__objc_methlist: 0x297c
+  __TEXT.__const: 0x5ed0
+  __TEXT.__cstring: 0x8091
+  __TEXT.__constg_swiftt: 0x2fa8
+  __TEXT.__swift5_typeref: 0x38ba
+  __TEXT.__swift5_reflstr: 0x1c38
+  __TEXT.__swift5_fieldmd: 0x1d50
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_assocty: 0x7d0
-  __TEXT.__swift5_capture: 0xd98
-  __TEXT.__swift5_proto: 0x440
-  __TEXT.__swift5_types: 0x230
+  __TEXT.__swift5_capture: 0xe84
+  __TEXT.__swift5_proto: 0x464
+  __TEXT.__swift5_types: 0x23c
   __TEXT.__swift5_protos: 0x44
-  __TEXT.__swift5_acfuncs: 0x1e0
+  __TEXT.__swift5_acfuncs: 0x208
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__gcc_except_tab: 0x4ec
   __TEXT.__oslogstring: 0x14c4
-  __TEXT.__unwind_info: 0x4f88
-  __TEXT.__eh_frame: 0x9384
-  __TEXT.__objc_classname: 0x622
-  __TEXT.__objc_methname: 0x9407
-  __TEXT.__objc_methtype: 0x1c2b
-  __TEXT.__objc_stubs: 0x4820
-  __DATA_CONST.__got: 0x550
+  __TEXT.__unwind_info: 0x5c1c
+  __TEXT.__eh_frame: 0x9cdc
+  __TEXT.__objc_classname: 0x648
+  __TEXT.__objc_methname: 0x977f
+  __TEXT.__objc_methtype: 0x1d3e
+  __TEXT.__objc_stubs: 0x48e0
+  __DATA_CONST.__got: 0x560
   __DATA_CONST.__const: 0x1188
-  __DATA_CONST.__objc_classlist: 0x2c8
+  __DATA_CONST.__objc_classlist: 0x2d0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7710
-  __DATA_CONST.__objc_selrefs: 0x1eb8
+  __DATA_CONST.__objc_const: 0x79f8
+  __DATA_CONST.__objc_selrefs: 0x1f38
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__const: 0x3508
-  __AUTH_CONST.__cfstring: 0x2b60
-  __AUTH_CONST.__objc_const: 0x90
+  __AUTH_CONST.__const: 0x3c18
+  __AUTH_CONST.__cfstring: 0x2cc0
+  __AUTH_CONST.__objc_const: 0x120
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH_CONST.__auth_got: 0x12b8
-  __AUTH.__objc_data: 0x50
+  __AUTH_CONST.__auth_got: 0x12f8
+  __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0x190
   __DATA.__objc_protorefs: 0x70
-  __DATA.__objc_classrefs: 0x590
-  __DATA.__objc_superrefs: 0x138
-  __DATA.__objc_ivar: 0x38c
-  __DATA.__data: 0x3750
-  __DATA.__common: 0x158
-  __DATA.__bss: 0x7450
-  __DATA_DIRTY.__const: 0x2b08
+  __DATA.__objc_classrefs: 0x5a0
+  __DATA.__objc_superrefs: 0x140
+  __DATA.__objc_ivar: 0x3ac
+  __DATA.__data: 0x3820
+  __DATA.__common: 0x170
+  __DATA.__bss: 0x7850
+  __DATA_DIRTY.__const: 0x2830
   __DATA_DIRTY.__objc_const: 0x1668
-  __DATA_DIRTY.__objc_data: 0x15d8
-  __DATA_DIRTY.__data: 0x30b0
+  __DATA_DIRTY.__objc_data: 0x15e0
+  __DATA_DIRTY.__data: 0x3100
   __DATA_DIRTY.__common: 0x10
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
+  - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
   - /System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/EmbeddedAcousticRecognition
   - /System/Library/PrivateFrameworks/Koa.framework/Koa
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 02A0E93B-A13B-3121-83F6-307FE59A04FA
-  Functions: 7509
-  Symbols:   7959
-  CStrings:  3051
+  UUID: 58ED27C8-000C-3756-B965-CBA072FC5284
+  Functions: 7785
+  Symbols:   8187
+  CStrings:  3132
 
Symbols:
+ +[_SFSpeechRecognizerDetectorOptions supportsSecureCoding]
+ -[EARSpeechRecognitionResultPackage endOfSentenceLikelihood]
+ -[EARSpeechRecognitionToken acousticCost]
+ -[EARSpeechRecognitionToken graphCost]
+ -[_SFAnalysisOptions initWithHighPriority:asrID:requestID:aneContext:cpuContext:gpuContext:keepANEModelLoaded:]
+ -[_SFAnalysisOptions keepANEModelLoaded]
+ -[_SFAnalyzerClientInfo dictationUIInteractionId]
+ -[_SFAnalyzerClientInfo initWithID:applicationName:source:inputOrigin:dictationUIInteractionId:]
+ -[_SFAnalyzerClientInfo inputOrigin]
+ -[_SFSpeechRecognizerDetectorOptions copyWithZone:]
+ -[_SFSpeechRecognizerDetectorOptions description]
+ -[_SFSpeechRecognizerDetectorOptions detectAfterTime]
+ -[_SFSpeechRecognizerDetectorOptions encodeWithCoder:]
+ -[_SFSpeechRecognizerDetectorOptions hash]
+ -[_SFSpeechRecognizerDetectorOptions initWithCoder:]
+ -[_SFSpeechRecognizerDetectorOptions initWithDetectAfterTime:]
+ -[_SFSpeechRecognizerDetectorOptions isEqual:]
+ -[_SFSpeechRecognizerModelOptions description]
+ -[_SFSpeechRecognizerModelOptions hash]
+ -[_SFSpeechRecognizerModelOptions isEqual:]
+ -[_SFSpeechRecognizerSupportedFeatures description]
+ -[_SFSpeechRecognizerSupportedFeatures detectionOptions]
+ -[_SFSpeechRecognizerSupportedFeatures featuresWithDetectionOptions:]
+ -[_SFSpeechRecognizerSupportedFeatures initWithLocale:taskHints:voiceCommandActiveSet:modelOptions:detectionOptions:flags:]
+ GCC_except_table1001
+ GCC_except_table1029
+ GCC_except_table1033
+ GCC_except_table1037
+ GCC_except_table1040
+ GCC_except_table1052
+ GCC_except_table133
+ GCC_except_table159
+ GCC_except_table314
+ GCC_except_table436
+ GCC_except_table440
+ GCC_except_table442
+ GCC_except_table444
+ GCC_except_table449
+ GCC_except_table456
+ GCC_except_table459
+ GCC_except_table482
+ GCC_except_table503
+ GCC_except_table507
+ GCC_except_table542
+ GCC_except_table700
+ GCC_except_table783
+ GCC_except_table820
+ GCC_except_table834
+ GCC_except_table909
+ GCC_except_table912
+ _CMTimeGetSeconds
+ _OBJC_CLASS_$_ASRSchemaASRAudioSpeechPacketArrivalStarted
+ _OBJC_CLASS_$__EAREmojiRecognition
+ _OBJC_CLASS_$__SFSpeechRecognizerDetectorOptions
+ _OBJC_IVAR_$_EARSpeechRecognitionResultPackage._endOfSentenceLikelihood
+ _OBJC_IVAR_$_EARSpeechRecognitionToken._acousticCost
+ _OBJC_IVAR_$_EARSpeechRecognitionToken._graphCost
+ _OBJC_IVAR_$__SFAnalysisOptions._keepANEModelLoaded
+ _OBJC_IVAR_$__SFAnalyzerClientInfo._dictationUIInteractionId
+ _OBJC_IVAR_$__SFAnalyzerClientInfo._inputOrigin
+ _OBJC_IVAR_$__SFSpeechRecognizerDetectorOptions._detectAfterTime
+ _OBJC_IVAR_$__SFSpeechRecognizerSupportedFeatures._detectionOptions
+ _OBJC_METACLASS_$__SFSpeechRecognizerDetectorOptions
+ _OUTLINED_FUNCTION_262
+ _OUTLINED_FUNCTION_263
+ _OUTLINED_FUNCTION_264
+ _OUTLINED_FUNCTION_265
+ _OUTLINED_FUNCTION_266
+ _OUTLINED_FUNCTION_267
+ _OUTLINED_FUNCTION_268
+ _OUTLINED_FUNCTION_269
+ _OUTLINED_FUNCTION_270
+ _OUTLINED_FUNCTION_271
+ _OUTLINED_FUNCTION_272
+ _OUTLINED_FUNCTION_273
+ _OUTLINED_FUNCTION_274
+ _OUTLINED_FUNCTION_275
+ _OUTLINED_FUNCTION_276
+ _OUTLINED_FUNCTION_277
+ _OUTLINED_FUNCTION_278
+ _OUTLINED_FUNCTION_279
+ __OBJC_$_CLASS_METHODS__SFSpeechRecognizerDetectorOptions
+ __OBJC_$_CLASS_PROP_LIST__SFSpeechRecognizerDetectorOptions
+ __OBJC_$_INSTANCE_METHODS__SFSpeechRecognizerDetectorOptions
+ __OBJC_$_INSTANCE_VARIABLES__SFSpeechRecognizerDetectorOptions
+ __OBJC_$_PROP_LIST__SFSpeechRecognizerDetectorOptions
+ __OBJC_CLASS_PROTOCOLS_$__SFSpeechRecognizerDetectorOptions
+ __OBJC_CLASS_RO_$__SFSpeechRecognizerDetectorOptions
+ __OBJC_METACLASS_RO_$__SFSpeechRecognizerDetectorOptions
+ ___Block_byref_object_copy_.1548
+ ___Block_byref_object_copy_.1700
+ ___Block_byref_object_copy_.1925
+ ___Block_byref_object_copy_.2062
+ ___Block_byref_object_copy_.2301
+ ___Block_byref_object_copy_.332
+ ___Block_byref_object_copy_.735
+ ___Block_byref_object_dispose_.1549
+ ___Block_byref_object_dispose_.1701
+ ___Block_byref_object_dispose_.1926
+ ___Block_byref_object_dispose_.2063
+ ___Block_byref_object_dispose_.2302
+ ___Block_byref_object_dispose_.333
+ ___Block_byref_object_dispose_.736
+ ___block_literal_global.1068
+ ___block_literal_global.1601
+ ___block_literal_global.1767
+ ___block_literal_global.1936
+ ___block_literal_global.2098
+ ___block_literal_global.2341
+ ___block_literal_global.820
+ ___swift_allocate_boxed_opaque_existential_0Tm
+ ___swift_memcpy137_8
+ ___swift_memcpy160_8
+ ___swift_memcpy25_4
+ _associated conformance 6Speech15AnalysisOptionsV14ModelRetentionOSHAASQ
+ _associated conformance 6Speech16EndpointDetectorC16DetectionOptionsVSHAASQ
+ _block_copy_helper.101
+ _block_copy_helper.110
+ _block_copy_helper.121
+ _block_copy_helper.132
+ _block_copy_helper.145
+ _block_copy_helper.156
+ _block_copy_helper.168
+ _block_copy_helper.179
+ _block_copy_helper.192
+ _block_copy_helper.204
+ _block_copy_helper.216
+ _block_copy_helper.228
+ _block_copy_helper.240
+ _block_copy_helper.251
+ _block_copy_helper.264
+ _block_copy_helper.276
+ _block_copy_helper.288
+ _block_copy_helper.300
+ _block_copy_helper.313
+ _block_copy_helper.89
+ _block_copy_helper.95
+ _block_descriptor.103
+ _block_descriptor.112
+ _block_descriptor.123
+ _block_descriptor.134
+ _block_descriptor.147
+ _block_descriptor.158
+ _block_descriptor.170
+ _block_descriptor.181
+ _block_descriptor.194
+ _block_descriptor.206
+ _block_descriptor.218
+ _block_descriptor.230
+ _block_descriptor.242
+ _block_descriptor.253
+ _block_descriptor.266
+ _block_descriptor.278
+ _block_descriptor.290
+ _block_descriptor.302
+ _block_descriptor.315
+ _block_descriptor.91
+ _block_descriptor.97
+ _block_destroy_helper.102
+ _block_destroy_helper.111
+ _block_destroy_helper.122
+ _block_destroy_helper.133
+ _block_destroy_helper.146
+ _block_destroy_helper.157
+ _block_destroy_helper.169
+ _block_destroy_helper.180
+ _block_destroy_helper.193
+ _block_destroy_helper.205
+ _block_destroy_helper.217
+ _block_destroy_helper.229
+ _block_destroy_helper.241
+ _block_destroy_helper.252
+ _block_destroy_helper.265
+ _block_destroy_helper.277
+ _block_destroy_helper.289
+ _block_destroy_helper.301
+ _block_destroy_helper.314
+ _block_destroy_helper.90
+ _block_destroy_helper.96
+ _get_witness_table Scsy6Speech16EndpointDetectorC12ModuleOutputVs5Error_pGSciHPyHC.17
+ _objc_msgSend$acousticCost
+ _objc_msgSend$endOfSentenceLikelihood
+ _objc_msgSend$graphCost
+ _objc_msgSend$initWithLocale:taskHints:voiceCommandActiveSet:modelOptions:detectionOptions:flags:
+ _objc_msgSend$isEqualToArray:
+ _objc_msgSend$isMemberOfClass:
+ _objc_msgSend$taskNames
+ _objectdestroy.108Tm
+ _objectdestroy.177Tm
+ _objectdestroy.213Tm
+ _objectdestroy.228Tm
+ _objectdestroy.309Tm
+ _objectdestroy.340Tm
+ _objectdestroy.59Tm
+ _objectdestroy.66Tm
+ _sCleanupQueue.1695
+ _sSupportedLocaleIdentifiers.1042
+ _sSupportedLocales.1066
+ _sharedInstance.onceToken.1766
+ _sharedInstance.sharedManager.1768
+ _symbolic SaySay_____GG 6Speech18TranscriptionTokenV
+ _symbolic Say_____G 6Speech18TranscriptionTokenV
+ _symbolic Say______Sby_____yAA______pGYaYbctG So6CMTimea s6ResultO s5ErrorP
+ _symbolic Sayx8instance______Sg10expirationtG s15ContinuousClockV7InstantV
+ _symbolic Sf________________pIetMHygdzo_ 6Speech31EARSpeechRecognitionAudioBufferC s6UInt64V s5ErrorP
+ _symbolic Sfm
+ _symbolic So20_EAREmojiRecognitionCSg
+ _symbolic So26EARSpeechRecognitionResultC
+ _symbolic Su
+ _symbolic _____ 6Speech15AnalysisOptionsV14ModelRetentionO
+ _symbolic _____ 6Speech16EndpointDetectorC16DetectionOptionsV
+ _symbolic _____ 6Speech18TranscriptionTokenV
+ _symbolic _____8instance______Sg10expirationt 6Speech0A16RecognizerWorkerC s15ContinuousClockV7InstantV
+ _symbolic _____8instance______Sg10expirationtSg 6Speech0A16RecognizerWorkerC s15ContinuousClockV7InstantV
+ _symbolic _____Sg 6Speech16EndpointDetectorC16DetectionOptionsV
+ _symbolic _____SgSo36_SFSpeechRecognizerSupportedFeaturesCSo30_SFAnalysisContextCodingObjectCSo01_E7OptionsCSg___________pIetMHnggggzo_ 10Foundation4UUIDV 6Speech19EARSpeechRecognizerC s5ErrorP
+ _symbolic _____Sg_ABt 6Speech15AnalysisOptionsV11LoggingInfoV
+ _symbolic _____Sgm 10Foundation4UUIDV
+ _symbolic ______Sby_____yAA______pGYaYbct So6CMTimea s6ResultO s5ErrorP
+ _symbolic ______pSgIeghg_ s5ErrorP
+ _symbolic _____ySay_____GG s23_ContiguousArrayStorageC 6Speech18TranscriptionTokenV
+ _symbolic _____ySay______pGSgG 2os21OSAllocatedUnfairLockV 6Speech14ModuleProtocolP
+ _symbolic _____ySay______pGSg_____G s13ManagedBufferC 6Speech14ModuleProtocolP So16os_unfair_lock_sV
+ _symbolic _____ySbG 2os21OSAllocatedUnfairLockV
+ _symbolic _____ySb_____G s13ManagedBufferC So16os_unfair_lock_sV
+ _symbolic _____yScTyyt_____GSgG 2os21OSAllocatedUnfairLockV s5NeverO
+ _symbolic _____yScTyyt_____GSg_____G s13ManagedBufferC s5NeverO So16os_unfair_lock_sV
+ _symbolic _____ySfG 11Distributed18RemoteCallArgumentV
+ _symbolic _____y_____8instance______Sg10expirationtG s23_ContiguousArrayStorageC 6Speech0D16RecognizerWorkerC s15ContinuousClockV7InstantV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 6Speech18TranscriptionTokenV
+ _symbolic _____y_____SgG 11Distributed18RemoteCallArgumentV 10Foundation4UUIDV
+ _symbolic _____y______Sby_____yAB______pGYaYbctG s23_ContiguousArrayStorageC So6CMTimea s6ResultO s5ErrorP
+ _symbolic _____y___________pGIeghHg_ s6ResultO So6CMTimea s5ErrorP
+ _symbolic _____yy_____y___________pGYaYbcG s23_ContiguousArrayStorageC s6ResultO So6CMTimea s5ErrorP
+ _symbolic yxcSg
- -[_SFAnalysisOptions initWithHighPriority:asrID:requestID:aneContext:cpuContext:gpuContext:]
- -[_SFAnalyzerClientInfo initWithID:applicationName:source:]
- -[_SFSpeechRecognizerSupportedFeatures initWithLocale:taskHints:voiceCommandActiveSet:modelOptions:flags:]
- GCC_except_table1008
- GCC_except_table1012
- GCC_except_table1016
- GCC_except_table1019
- GCC_except_table1031
- GCC_except_table118
- GCC_except_table144
- GCC_except_table299
- GCC_except_table418
- GCC_except_table422
- GCC_except_table424
- GCC_except_table426
- GCC_except_table428
- GCC_except_table431
- GCC_except_table438
- GCC_except_table441
- GCC_except_table485
- GCC_except_table489
- GCC_except_table524
- GCC_except_table679
- GCC_except_table762
- GCC_except_table799
- GCC_except_table813
- GCC_except_table888
- GCC_except_table891
- GCC_except_table959
- ___Block_byref_object_copy_.1515
- ___Block_byref_object_copy_.1664
- ___Block_byref_object_copy_.1855
- ___Block_byref_object_copy_.1988
- ___Block_byref_object_copy_.2222
- ___Block_byref_object_copy_.320
- ___Block_byref_object_copy_.720
- ___Block_byref_object_dispose_.1516
- ___Block_byref_object_dispose_.1665
- ___Block_byref_object_dispose_.1856
- ___Block_byref_object_dispose_.1989
- ___Block_byref_object_dispose_.2223
- ___Block_byref_object_dispose_.321
- ___Block_byref_object_dispose_.721
- ___block_literal_global.1052
- ___block_literal_global.1568
- ___block_literal_global.1706
- ___block_literal_global.1866
- ___block_literal_global.2025
- ___block_literal_global.2263
- ___block_literal_global.805
- ___swift_allocate_boxed_opaque_existential_1Tm
- ___swift_memcpy124_8
- _block_copy_helper.102
- _block_copy_helper.113
- _block_copy_helper.126
- _block_copy_helper.138
- _block_copy_helper.150
- _block_copy_helper.161
- _block_copy_helper.174
- _block_copy_helper.186
- _block_copy_helper.198
- _block_copy_helper.210
- _block_copy_helper.222
- _block_copy_helper.233
- _block_copy_helper.246
- _block_copy_helper.258
- _block_copy_helper.270
- _block_copy_helper.283
- _block_copy_helper.295
- _block_copy_helper.59
- _block_copy_helper.65
- _block_copy_helper.92
- _block_descriptor.104
- _block_descriptor.115
- _block_descriptor.128
- _block_descriptor.140
- _block_descriptor.152
- _block_descriptor.163
- _block_descriptor.176
- _block_descriptor.188
- _block_descriptor.200
- _block_descriptor.212
- _block_descriptor.224
- _block_descriptor.235
- _block_descriptor.248
- _block_descriptor.260
- _block_descriptor.272
- _block_descriptor.285
- _block_descriptor.297
- _block_descriptor.61
- _block_descriptor.67
- _block_descriptor.94
- _block_destroy_helper.103
- _block_destroy_helper.114
- _block_destroy_helper.127
- _block_destroy_helper.139
- _block_destroy_helper.151
- _block_destroy_helper.162
- _block_destroy_helper.175
- _block_destroy_helper.187
- _block_destroy_helper.199
- _block_destroy_helper.211
- _block_destroy_helper.223
- _block_destroy_helper.234
- _block_destroy_helper.247
- _block_destroy_helper.259
- _block_destroy_helper.271
- _block_destroy_helper.284
- _block_destroy_helper.296
- _block_destroy_helper.60
- _block_destroy_helper.66
- _block_destroy_helper.93
- _get_witness_table Scsy6Speech16EndpointDetectorC12ModuleOutputVs5Error_pGSciHPyHC.14
- _objc_msgSend$initWithLocale:taskHints:voiceCommandActiveSet:modelOptions:flags:
- _objectdestroy.100Tm
- _objectdestroy.106Tm
- _objectdestroy.172Tm
- _objectdestroy.211Tm
- _objectdestroy.226Tm
- _objectdestroy.326Tm
- _objectdestroy.90Tm
- _sCleanupQueue.1662
- _sSupportedLocaleIdentifiers.1026
- _sSupportedLocales.1050
- _sharedInstance.onceToken.1705
- _sharedInstance.sharedManager.1707
- _symbolic SaySo26EARSpeechRecognitionResultCG
- _symbolic Say______SbySay______pGYbctG So6CMTimea 6Speech14WorkerProtocolP
- _symbolic Say______pGIeghg_ 6Speech14WorkerProtocolP
- _symbolic Say______pGSg 6Speech14ModuleProtocolP
- _symbolic Sayx______SgtG s15ContinuousClockV7InstantV
- _symbolic ______SbySay______pGYbct So6CMTimea 6Speech14WorkerProtocolP
- _symbolic ___________Sgt 6Speech0A16RecognizerWorkerC s15ContinuousClockV7InstantV
- _symbolic ___________SgtSg 6Speech0A16RecognizerWorkerC s15ContinuousClockV7InstantV
- _symbolic ______pSgIeghHg_ s5ErrorP
- _symbolic _____y_____GSgXw 6Speech14KeepAliveCacheC AA0A16RecognizerWorkerC
- _symbolic _____y______SbySay______pGYbctG s23_ContiguousArrayStorageC So6CMTimea 6Speech14WorkerProtocolP
- _symbolic _____y___________SgtG s23_ContiguousArrayStorageC 6Speech0D16RecognizerWorkerC s15ContinuousClockV7InstantV
CStrings:
+ "\x14\x11"
+ "\x14\x14"
+ ",\neosLikelihood "
+ ", eosLikelihood "
+ ", silencePosterior "
+ "<Speech.CommandRecognizer.Argument: "
+ "<Speech.CommandRecognizer.Interpretation: "
+ "<Speech.CommandRecognizer.Result: range "
+ "<Speech.EndpointDetector.ModuleOutput: range "
+ "<Speech.Transcriber.MultisegmentResult: "
+ "<Speech.Transcriber.Result: range "
+ "<_SFSpeechRecognizerDetectorOptions: detectAfterTime %f>"
+ "<_SFSpeechRecognizerModelOptions: farField %d, supplementalModelURL %@, modelOverrideURL %@, speechProfileURLs %@, taskForMemoryLock %@>"
+ "<_SFSpeechRecognizerSupportedFeatures (%p): locale %@, taskNames %@, modelOptions %@, detectionOptions %@, flags %#lx>"
+ "@\"_SFSpeechRecognizerDetectorOptions\""
+ "@24@0:8d16"
+ "@56@0:8@16@24@32@40@48"
+ "@64@0:8@16@24@32@40@48Q56"
+ "@64@0:8B16@20@28@36@44@52B60"
+ "ES: Frame Processing Ready"
+ "ES: Last Speech Audio Packet"
+ "EndpointDetector: Yielded result %s"
+ "Speech.EARSpeechRecognitionAudioBuffer.packetArrivalTimestamp(fromAudioTimestamp:)"
+ "Speech.EARSpeechRecognizer.prepareForReuse(withNewAsrID:supportedFeatures:analysisContext:analysisOptions:)"
+ "Speech/EARSpeechRecognitionAudioBuffer.swift"
+ "SpeechAnalyzer: Finishing after input barrier"
+ "SpeechAnalyzer: Finishing immediately"
+ "SpeechAnalyzer: Setting finisher input barrier at %@"
+ "SpeechRecognizerWorker: Making new EARSpeechRecognizer"
+ "SpeechRecognizerWorker: Reusing EARSpeechRecognizer"
+ "T@\"NSNumber\",R,N,V_endOfSentenceLikelihood"
+ "T@\"NSString\",R,C,N,V_dictationUIInteractionId"
+ "T@\"NSString\",R,C,N,V_inputOrigin"
+ "T@\"_SFSpeechRecognizerDetectorOptions\",R,C,N,V_detectionOptions"
+ "TB,R,N,V_keepANEModelLoaded"
+ "Td,R,N,V_acousticCost"
+ "Td,R,N,V_detectAfterTime"
+ "Td,R,N,V_graphCost"
+ "Vv28@0:8f16@?20"
+ "Vv28@0:8f16@?<v@?Q>20"
+ "Vv48@0:8@\"NSUUID\"16@\"_SFSpeechRecognizerSupportedFeatures\"24@\"_SFAnalysisContextCodingObject\"32@\"_SFAnalysisOptions\"40"
+ "Vv48@0:8@16@24@32@40"
+ "_SFSpeechRecognizerDetectorOptions"
+ "_acousticCost"
+ "_detectAfterTime"
+ "_detectionOptions"
+ "_dictationUIInteractionId"
+ "_endOfSentenceLikelihood"
+ "_graphCost"
+ "_inputOrigin"
+ "_keepANEModelLoaded"
+ "acousticCost"
+ "baseStringForEmojiString:"
+ "detectAfterTime"
+ "detectionOptions"
+ "dictationUIInteractionId"
+ "didFinishInputOnce"
+ "emojiUtils"
+ "endOfSentenceLikelihood"
+ "featuresWithDetectionOptions:"
+ "finalize(workers:at:willFinishAfter:)"
+ "fromAudioTimestamp"
+ "graphCost"
+ "hasContextChangesMutex"
+ "initWithDetectAfterTime:"
+ "initWithHighPriority:asrID:requestID:aneContext:cpuContext:gpuContext:keepANEModelLoaded:"
+ "initWithID:applicationName:source:inputOrigin:dictationUIInteractionId:"
+ "initWithLocale:taskHints:voiceCommandActiveSet:modelOptions:detectionOptions:flags:"
+ "inputOrigin"
+ "inputTaskMutex"
+ "isEqualToArray:"
+ "isFinishedMutex"
+ "isInputFinished"
+ "keepANEModelLoaded"
+ "packetArrivalTimestampFromAudioTimestamp:reply:"
+ "pendingNewModulesMutex"
+ "prepareForReuseWithNewAsrID:supportedFeatures:analysisContext:analysisOptions:"
+ "resultCandidateId"
+ "speechRecognizerDidProcessAudioDuration(_:)"
+ "speechRecognizerDidProduceEndpointFeatures(withWordCount:trailingSilenceDuration:eosLikelihood:pauseCounts:silencePosterior:processedAudioDurationInMilliseconds:)"
+ "speechRecognizerDidRecognizePartialResult:"
+ "speechRecognizerDidReportStatus(_:)"
+ "speechRecognizerDidReportStatus:"
+ "v24@0:8@\"EARSpeechRecognitionResult\"16"
+ "willEvictInstance"
- "\x14\x13"
- "<Speech.CommandRecognizer.Argument> "
- "<Speech.CommandRecognizer.Interpretation> "
- "<Speech.CommandRecognizer.Result> range "
- "<Speech.Transcription.MultisegmentResult> "
- "<Speech.Transcription.Result> range "
- "@56@0:8@16@24@32@40Q48"
- "@60@0:8B16@20@28@36@44@52"
- "SpeechAnalyzer: Clearing volatile range barriers to %@"
- "didFinishOnce"
- "finalize(workers:at:finishing:)"
- "finalizeAndFinish(through:)"
- "hasContextChanges"
- "initWithHighPriority:asrID:requestID:aneContext:cpuContext:gpuContext:"
- "initWithID:applicationName:source:"
- "initWithLocale:taskHints:voiceCommandActiveSet:modelOptions:flags:"
- "inputTask"
- "isFinished"
- "pendingNewModules"
- "speechRecognizerDidFinishRecognitionWithError(_:)"
- "speechRecognizerDidProduceLoggablePackage(_:)"
- "speechRecognizerDidRecognizeFinalResultCandidatePackage(_:)"
- "speechRecognizerDidRecognizePartialResultNbest(_:)"
- "speechRecognizerDidRecognizePartialResultNbest:"
- "v24@0:8@\"NSArray\"16"

```
