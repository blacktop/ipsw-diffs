## SpeakerRecognition

> `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/SpeakerRecognition`

```diff

-3403.7.3.0.0
-  __TEXT.__text: 0x8053c
-  __TEXT.__auth_stubs: 0xab0
-  __TEXT.__objc_methlist: 0x51f0
-  __TEXT.__const: 0x370
-  __TEXT.__gcc_except_tab: 0x2434
-  __TEXT.__cstring: 0xd46a
-  __TEXT.__oslogstring: 0xba4f
-  __TEXT.__unwind_info: 0x1628
-  __TEXT.__objc_classname: 0xd95
-  __TEXT.__objc_methname: 0x10564
-  __TEXT.__objc_methtype: 0x236c
-  __TEXT.__objc_stubs: 0x9700
-  __DATA_CONST.__got: 0x898
-  __DATA_CONST.__const: 0x770
-  __DATA_CONST.__objc_classlist: 0x2a8
+3404.82.3.0.0
+  __TEXT.__text: 0x84804
+  __TEXT.__auth_stubs: 0xd60
+  __TEXT.__objc_methlist: 0x5cc8
+  __TEXT.__const: 0x408
+  __TEXT.__cstring: 0xdfb2
+  __TEXT.__swift5_typeref: 0xe8
+  __TEXT.__swift5_fieldmd: 0xc0
+  __TEXT.__constg_swiftt: 0x204
+  __TEXT.__swift5_reflstr: 0xf4
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__gcc_except_tab: 0x2504
+  __TEXT.__oslogstring: 0xbabc
+  __TEXT.__unwind_info: 0x16d8
+  __TEXT.__objc_classname: 0xd73
+  __TEXT.__objc_methname: 0x10839
+  __TEXT.__objc_methtype: 0x2357
+  __TEXT.__objc_stubs: 0x9880
+  __DATA_CONST.__got: 0x8f8
+  __DATA_CONST.__const: 0x788
+  __DATA_CONST.__objc_classlist: 0x2b0
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x130
+  __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3590
-  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_selrefs: 0x3778
+  __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x370
-  __AUTH_CONST.__auth_got: 0x570
-  __AUTH_CONST.__const: 0x1b20
-  __AUTH_CONST.__cfstring: 0x5180
-  __AUTH_CONST.__objc_const: 0xaac8
+  __AUTH_CONST.__auth_got: 0x6c8
+  __AUTH_CONST.__const: 0x1b60
+  __AUTH_CONST.__cfstring: 0x5220
+  __AUTH_CONST.__objc_const: 0x9cc8
   __AUTH_CONST.__objc_dictobj: 0x898
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x1a90
-  __DATA.__objc_ivar: 0x71c
-  __DATA.__data: 0xe48
-  __DATA.__bss: 0x138
-  __DATA.__common: 0x8
+  __AUTH.__objc_data: 0x1d90
+  __AUTH.__data: 0x50
+  __DATA.__objc_ivar: 0x738
+  __DATA.__data: 0xf48
+  __DATA.__bss: 0x130
+  __DATA.__common: 0x60
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: AB42F7A5-D839-3335-8BBA-512F9E3FA3FF
-  Functions: 2125
-  Symbols:   5468
-  CStrings:  5661
+  UUID: 0310CD06-54D2-3FE4-A18E-1EC7DE4C0432
+  Functions: 2193
+  Symbols:   5552
+  CStrings:  5751
 
Symbols:
+ +[SSREnrollmentSamplingMetaDataHelper getEnrollmentMetaDataWithVoiceProfileId:]
+ -[CSVTUIKeywordDetector isRunningTwoPass]
+ -[CSVTUISelfLoggingDigitalZeroReporter initWithSiriSetupID:PageNumber:withPhId:withLocale:withVTAssetConfigVersion:withSessionStatus:didDetectSpeechStart:didUseTwoPassDetector:didFirstPassTrigger:]
+ -[CSVTUITwoPassKeywordDetector isRunningTwoPass]
+ -[SSRSpeakerProfileEmbedding description]
+ -[SSRSpeakerProfileEmbedding initWithVoiceProfileId:embeddings:numEmbedding:dimension:speakerRecognizerType:]
+ -[SSRSpeakerProfileEmbedding voiceProfileId]
+ -[SSRVTUITrainingManager _createAudioSessionRecorder]
+ -[SSRVTUITrainingManager _logSessionSummary]
+ -[SSRVTUITrainingManager _updateAttemptForPageNumber:]
+ -[SSRVTUITrainingManager initWithLocaleIdentifier:withAppDomain:]
+ -[SSRVTUITrainingManager initWithLocaleIdentifier:withAppDomain:withSiriSharedUserId:shouldTrainViaXPC:]
+ -[SSRVoiceProfileManager cleanupVoiceProfileModelFilesForLocale:withAssets:]
+ -[SSRVoiceProfileManager updateVoiceProfileIDInUserProfile:]
+ -[SSRVoiceProfileRetrainerPSR _psrProcessorResetSync:]
+ -[SSRVoiceProfileStore cleanupVoiceProfileModelFilesForLocale:withAssets:]
+ GCC_except_table1010
+ GCC_except_table1066
+ GCC_except_table1070
+ GCC_except_table1088
+ GCC_except_table1174
+ GCC_except_table1176
+ GCC_except_table1194
+ GCC_except_table1198
+ GCC_except_table1207
+ GCC_except_table1217
+ GCC_except_table1223
+ GCC_except_table1274
+ GCC_except_table1280
+ GCC_except_table1287
+ GCC_except_table1316
+ GCC_except_table1329
+ GCC_except_table1359
+ GCC_except_table1365
+ GCC_except_table1434
+ GCC_except_table1543
+ GCC_except_table1558
+ GCC_except_table1570
+ GCC_except_table1580
+ GCC_except_table1585
+ GCC_except_table1602
+ GCC_except_table1615
+ GCC_except_table1630
+ GCC_except_table1705
+ GCC_except_table1709
+ GCC_except_table1748
+ GCC_except_table177
+ GCC_except_table178
+ GCC_except_table1783
+ GCC_except_table182
+ GCC_except_table1848
+ GCC_except_table1868
+ GCC_except_table1879
+ GCC_except_table188
+ GCC_except_table1889
+ GCC_except_table1906
+ GCC_except_table308
+ GCC_except_table327
+ GCC_except_table358
+ GCC_except_table366
+ GCC_except_table371
+ GCC_except_table450
+ GCC_except_table478
+ GCC_except_table550
+ GCC_except_table558
+ GCC_except_table560
+ GCC_except_table564
+ GCC_except_table650
+ GCC_except_table731
+ GCC_except_table771
+ GCC_except_table778
+ GCC_except_table808
+ GCC_except_table811
+ GCC_except_table885
+ GCC_except_table886
+ GCC_except_table889
+ GCC_except_table898
+ GCC_except_table903
+ GCC_except_table908
+ GCC_except_table985
+ OBJC_IVAR_$_CSVTUISelfLoggingDigitalZeroReporter._didDetectSpeechStart
+ OBJC_IVAR_$_CSVTUISelfLoggingDigitalZeroReporter._didFirstPassTrigger
+ OBJC_IVAR_$_CSVTUISelfLoggingDigitalZeroReporter._didUseTwoPassDetector
+ OBJC_IVAR_$_CSVTUITrainingSession._didFirstPassTrigger
+ OBJC_IVAR_$_CSVTUITrainingSession._speechStartDetected
+ OBJC_IVAR_$_SSRSpeakerProfileEmbedding._voiceProfileId
+ OBJC_IVAR_$_SSRVTUITrainingManager._lastAttemptedUtterance
+ OBJC_IVAR_$_SSRVTUITrainingManager._pageAttemptMap
+ _OBJC_CLASS_$_CSAudioProviderSelectingProxy
+ _OBJC_CLASS_$_CSKeywordAnalyzerNDAPIResult
+ _OBJC_CLASS_$__TtC18SpeakerRecognition27CSVTUIKeywordDetectorHelper
+ _OBJC_CLASS_$__TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper
+ _OBJC_METACLASS_$__TtC18SpeakerRecognition27CSVTUIKeywordDetectorHelper
+ _OBJC_METACLASS_$__TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper
+ _PROTOCOLS__TtC18SpeakerRecognition27CSVTUIKeywordDetectorHelper.2
+ _PROTOCOLS__TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper.2
+ __118-[SSRVoiceProfileStore addImplicitUtterance:toVoiceProfile:withAsset:withTriggerSource:withAudioInput:withCompletion:]_block_invoke.72
+ __118-[SSRVoiceProfileStore addImplicitUtterance:toVoiceProfile:withAsset:withTriggerSource:withAudioInput:withCompletion:]_block_invoke.77
+ __37-[SSRVTUITrainingManager audioSource]_block_invoke.97
+ __46-[SSRVTUITrainingManager cancelTrainingForID:]_block_invoke.90
+ __48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.37
+ __48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.39
+ __48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.42
+ __48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.43
+ __48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.46
+ __48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.47
+ __48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke_2.38
+ __48-[SSRVTUITrainingManager prepareWithCompletion:]_block_invoke.32
+ __48-[SSRVTUITrainingManager prepareWithCompletion:]_block_invoke_2.33
+ __49-[SSRVoiceProfileStore cleanupDuplicatedProfiles]_block_invoke.36
+ __49-[SSRVoiceProfileStore cleanupVoiceProfileStore:]_block_invoke.41
+ __49-[SSRVoiceProfileStore cleanupVoiceProfileStore:]_block_invoke_2.45
+ __53-[SSRVoiceProfileStore saveVoiceProfiles:completion:]_block_invoke.106
+ __55-[SSRVTUITrainingManager playSoundEffectWithAudioTone:]_block_invoke.87
+ __66-[SSRSpeakerProfileEmbeddingServiceClient _createClientConnection]_block_invoke.12
+ __66-[SSRSpeakerProfileEmbeddingServiceClient _createClientConnection]_block_invoke.13
+ __66-[SSRSpeakerProfileEmbeddingServiceClient _createClientConnection]_block_invoke.14
+ __66-[SSRVoiceProfileStore _synchronizeSiriVoiceProfilesWithAssistant]_block_invoke.53
+ __69-[CSVTUIAudioSessionRecorder _forceFetchAudioProvider:recordContext:]_block_invoke.16
+ __82-[SSRVTUITrainingManager trainUtterance:shouldUseASR:mhUUID:completionWithResult:]_block_invoke.53
+ __82-[SSRVTUITrainingManager trainUtterance:shouldUseASR:mhUUID:completionWithResult:]_block_invoke_2.54
+ __91-[SSRSpeakerProfileEmbeddingServiceClient refreshEmbeddingsforLanguageCode:withCompletion:]_block_invoke.5
+ __Block_byref_object_copy_.1073
+ __Block_byref_object_copy_.1669
+ __Block_byref_object_copy_.1880
+ __Block_byref_object_copy_.2041
+ __Block_byref_object_copy_.2694
+ __Block_byref_object_copy_.3243
+ __Block_byref_object_copy_.3397
+ __Block_byref_object_copy_.3565
+ __Block_byref_object_copy_.4322
+ __Block_byref_object_copy_.4638
+ __Block_byref_object_copy_.4828
+ __Block_byref_object_copy_.4914
+ __Block_byref_object_copy_.5148
+ __Block_byref_object_copy_.6006
+ __Block_byref_object_copy_.6410
+ __Block_byref_object_copy_.6524
+ __Block_byref_object_copy_.6750
+ __Block_byref_object_copy_.7115
+ __Block_byref_object_copy_.740
+ __Block_byref_object_copy_.7623
+ __Block_byref_object_copy_.851
+ __Block_byref_object_copy_.99
+ __Block_byref_object_dispose_.100
+ __Block_byref_object_dispose_.1074
+ __Block_byref_object_dispose_.1670
+ __Block_byref_object_dispose_.1881
+ __Block_byref_object_dispose_.2042
+ __Block_byref_object_dispose_.2695
+ __Block_byref_object_dispose_.3244
+ __Block_byref_object_dispose_.3398
+ __Block_byref_object_dispose_.3566
+ __Block_byref_object_dispose_.4323
+ __Block_byref_object_dispose_.4639
+ __Block_byref_object_dispose_.4829
+ __Block_byref_object_dispose_.4915
+ __Block_byref_object_dispose_.5149
+ __Block_byref_object_dispose_.6007
+ __Block_byref_object_dispose_.6411
+ __Block_byref_object_dispose_.6525
+ __Block_byref_object_dispose_.6751
+ __Block_byref_object_dispose_.7116
+ __Block_byref_object_dispose_.741
+ __Block_byref_object_dispose_.7624
+ __Block_byref_object_dispose_.852
+ __DATA__TtC18SpeakerRecognition27CSVTUIKeywordDetectorHelper
+ __DATA__TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper
+ __INSTANCE_METHODS__TtC18SpeakerRecognition27CSVTUIKeywordDetectorHelper
+ __INSTANCE_METHODS__TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper
+ __IVARS__TtC18SpeakerRecognition27CSVTUIKeywordDetectorHelper
+ __IVARS__TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper
+ __METACLASS_DATA__TtC18SpeakerRecognition27CSVTUIKeywordDetectorHelper
+ __METACLASS_DATA__TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper
+ __PROTOCOLS__TtC18SpeakerRecognition27CSVTUIKeywordDetectorHelper
+ __PROTOCOLS__TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper
+ __PROTOCOL_INSTANCE_METHODS__TtP18SpeakerRecognition26CSVTUIKeywordDetectorSwift_
+ __PROTOCOL_METHOD_TYPES__TtP18SpeakerRecognition26CSVTUIKeywordDetectorSwift_
+ __PROTOCOL__TtP18SpeakerRecognition26CSVTUIKeywordDetectorSwift_
+ ___47-[CSVTUITrainingSession didDetectBeginOfSpeech]_block_invoke
+ ___74-[SSRVoiceProfileStore cleanupVoiceProfileModelFilesForLocale:withAssets:]_block_invoke
+ ___78-[SSRVTUITrainingMessageHandler setupWithLocaleID:appDomain:siriSharedUserId:]_block_invoke
+ ___79+[SSREnrollmentSamplingMetaDataHelper getEnrollmentMetaDataWithVoiceProfileId:]_block_invoke
+ ___80-[CSVTUITrainingSession handleAudioBufferForVTWithAudioInput:withDetectedBlock:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSArray"8l
+ ___block_descriptor_48_e8_32s40r_e56_v32?0"NSString"8"SSREnrollmentSamplingMetaData"16^B24l
+ ___chkstk_darwin
+ ___swift_instantiateConcreteTypeFromMangledName
+ __block_literal_global.1415
+ __block_literal_global.1676
+ __block_literal_global.2610
+ __block_literal_global.3420
+ __block_literal_global.3482
+ __block_literal_global.4370
+ __block_literal_global.45
+ __block_literal_global.48
+ __block_literal_global.5234
+ __block_literal_global.5442
+ __block_literal_global.6190
+ __block_literal_global.6533
+ __block_literal_global.6785
+ __block_literal_global.7000
+ __block_literal_global.7304
+ __block_literal_global.7797
+ __block_literal_global.8144
+ __swiftEmptyArrayStorage
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_SpeakerRecognition
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_SpeakerRecognition
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_SpeakerRecognition
+ __swift_stdlib_reportUnimplementedInitializer
+ _kSSRVoiceProfileUpdatedNotification
+ _objc_allocWithZone
+ _objc_msgSend$_createAudioSessionRecorder
+ _objc_msgSend$_logSessionSummary
+ _objc_msgSend$_psrProcessorResetSync:
+ _objc_msgSend$_updateAttemptForPageNumber:
+ _objc_msgSend$addAudioSync:
+ _objc_msgSend$audioProviderWithContext:error:
+ _objc_msgSend$cleanupVoiceProfileModelFilesForLocale:withAssets:
+ _objc_msgSend$getEnrollmentMetaDataWithVoiceProfileId:
+ _objc_msgSend$initWithLocaleIdentifier:withAppDomain:withSiriSharedUserId:shouldTrainViaXPC:
+ _objc_msgSend$initWithSiriSetupID:PageNumber:withPhId:withLocale:withVTAssetConfigVersion:withSessionStatus:didDetectSpeechStart:didUseTwoPassDetector:didFirstPassTrigger:
+ _objc_msgSend$initWithVoiceProfileId:embeddings:numEmbedding:dimension:speakerRecognizerType:
+ _objc_msgSend$isRunningTwoPass
+ _objc_msgSend$logSiriSetupEnrollmentSessionSummaryWithSiriSetupID:lastOpenedPage:completedPage:pageAttemptsMap:
+ _objc_msgSend$logSiriSetupPHSEnrollmentDigitalZeroDetectionCompletedWithSiriSetupID:withPageNumber:withPhId:withMaxNumContinuousZeros:withMaxNumAllowedContinuousZeros:withIsMaxNumContinuousZerosOverThreshold:withLocale:withVTAssetConfigVersion:withStageStatus:didDetectSpeechStart:didUseTwoPassDetector:didFirstPassTrigger:
+ _objc_msgSend$resetForNewRequestSync
+ _objc_msgSend$sharedContollerProxy
+ _objc_msgSend$supportsSecureAssetForSpeakerRecognition
+ _objc_msgSend$supportsVoiceProfileIDInUserProfile
+ _objc_opt_self
+ _swift_allocObject
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_deallocPartialClassInstance
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_getObjCClassMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_once
+ _swift_release
+ _swift_unknownObjectRelease
+ _symbolic $s18SpeakerRecognition26CSVTUIKeywordDetectorSwiftP
+ _symbolic Sb
+ _symbolic Sf
+ _symbolic So16CSPhraseDetectorCSg
+ _symbolic So21CSAudioCircularBufferC
+ _symbolic So22CSKeywordAnalyzerNDAPICSg
+ _symbolic So29SSRTriggerPhraseDetectorNDAPICSg
+ _symbolic So8NSObjectC
+ _symbolic Su
+ _symbolic _____ 18SpeakerRecognition27CSVTUIKeywordDetectorHelperC
+ _symbolic _____ 18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelperC
+ _symbolic _____y______pG s23_ContiguousArrayStorageC s7CVarArgP
+ _symbolic ypSg
+ sharedInstance.onceToken.1414
+ sharedInstance.onceToken.3481
+ sharedInstance.onceToken.7303
+ sharedManager.onceToken.6784
- +[SSREnrollmentSamplingMetaDataHelper markFinishStatusForAllWithCompletion:]
- +[SSRVTUIHelperFunctionsForSwift createDirectoryIfDoesNotExist:]
- +[SSRVTUIHelperFunctionsForSwift getInstalledAssetForLanguage:]
- +[SSRVTUIHelperFunctionsForSwift saveEncryptedData:atFilepath:]
- +[SSRVTUIHelperFunctionsForSwift voiceProfileAudioDirPathForSpidType:toProfile:]
- -[CSVTUISelfLoggingDigitalZeroReporter initWithSiriSetupID:PageNumber:withPhId:withLocale:withVTAssetConfigVersion:withSessionStatus:]
- -[SSRRPISampler markFinishStatusForAllWithCompletion:]
- -[SSRVTUITrainingManager initWithLocaleIdentifier:withAudioSession:withAppDomain:]
- -[SSRVTUITrainingManager initWithLocaleIdentifier:withAudioSession:withAppDomain:shouldTrainViaXPC:withSiriSharedUserId:]
- -[SSRVTUITrainingMessageHandler audioSession]
- -[SSRVTUITrainingMessageHandler setAudioSession:]
- CSSecureLogInitIfNeeded.once
- GCC_except_table1007
- GCC_except_table1063
- GCC_except_table1067
- GCC_except_table1085
- GCC_except_table1170
- GCC_except_table1171
- GCC_except_table1191
- GCC_except_table1195
- GCC_except_table1204
- GCC_except_table1214
- GCC_except_table1220
- GCC_except_table1277
- GCC_except_table1284
- GCC_except_table1313
- GCC_except_table1326
- GCC_except_table1360
- GCC_except_table1429
- GCC_except_table1535
- GCC_except_table1549
- GCC_except_table1561
- GCC_except_table1571
- GCC_except_table1576
- GCC_except_table1593
- GCC_except_table1597
- GCC_except_table1621
- GCC_except_table1696
- GCC_except_table1700
- GCC_except_table1739
- GCC_except_table1774
- GCC_except_table181
- GCC_except_table1839
- GCC_except_table185
- GCC_except_table1850
- GCC_except_table1870
- GCC_except_table1880
- GCC_except_table189
- GCC_except_table1896
- GCC_except_table191
- GCC_except_table311
- GCC_except_table330
- GCC_except_table361
- GCC_except_table369
- GCC_except_table374
- GCC_except_table453
- GCC_except_table481
- GCC_except_table553
- GCC_except_table561
- GCC_except_table563
- GCC_except_table567
- GCC_except_table651
- GCC_except_table730
- GCC_except_table770
- GCC_except_table777
- GCC_except_table807
- GCC_except_table810
- GCC_except_table883
- GCC_except_table884
- GCC_except_table887
- GCC_except_table890
- GCC_except_table891
- GCC_except_table982
- OBJC_IVAR_$_SSRVTUITrainingMessageHandler._audioSession
- _CSLogContextFacilityCoreSpeechExclave
- _CSSecureLogInitIfNeeded
- _OBJC_CLASS_$_SSRVTUIHelperFunctionsForSwift
- _OBJC_METACLASS_$_SSRVTUIHelperFunctionsForSwift
- __118-[SSRVoiceProfileStore addImplicitUtterance:toVoiceProfile:withAsset:withTriggerSource:withAudioInput:withCompletion:]_block_invoke.71
- __118-[SSRVoiceProfileStore addImplicitUtterance:toVoiceProfile:withAsset:withTriggerSource:withAudioInput:withCompletion:]_block_invoke.76
- __37-[SSRVTUITrainingManager audioSource]_block_invoke.92
- __46-[SSRVTUITrainingManager cancelTrainingForID:]_block_invoke.85
- __48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.36
- __48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.38
- __48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.41
- __48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.44
- __48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.45
- __48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke_2.37
- __48-[SSRVTUITrainingManager prepareWithCompletion:]_block_invoke.31
- __48-[SSRVTUITrainingManager prepareWithCompletion:]_block_invoke_2.32
- __49-[SSRVoiceProfileStore cleanupDuplicatedProfiles]_block_invoke.35
- __49-[SSRVoiceProfileStore cleanupVoiceProfileStore:]_block_invoke.40
- __49-[SSRVoiceProfileStore cleanupVoiceProfileStore:]_block_invoke_2.44
- __53-[SSRVoiceProfileStore saveVoiceProfiles:completion:]_block_invoke.105
- __55-[SSRVTUITrainingManager playSoundEffectWithAudioTone:]_block_invoke.82
- __66-[SSRSpeakerProfileEmbeddingServiceClient _createClientConnection]_block_invoke.10
- __66-[SSRSpeakerProfileEmbeddingServiceClient _createClientConnection]_block_invoke.8
- __66-[SSRSpeakerProfileEmbeddingServiceClient _createClientConnection]_block_invoke.9
- __66-[SSRVoiceProfileStore _synchronizeSiriVoiceProfilesWithAssistant]_block_invoke.52
- __69-[CSVTUIAudioSessionRecorder _forceFetchAudioProvider:recordContext:]_block_invoke.14
- __82-[SSRVTUITrainingManager trainUtterance:shouldUseASR:mhUUID:completionWithResult:]_block_invoke.51
- __82-[SSRVTUITrainingManager trainUtterance:shouldUseASR:mhUUID:completionWithResult:]_block_invoke_2.52
- __Block_byref_object_copy_.1072
- __Block_byref_object_copy_.1653
- __Block_byref_object_copy_.1868
- __Block_byref_object_copy_.2032
- __Block_byref_object_copy_.2682
- __Block_byref_object_copy_.3227
- __Block_byref_object_copy_.3379
- __Block_byref_object_copy_.3547
- __Block_byref_object_copy_.4289
- __Block_byref_object_copy_.4602
- __Block_byref_object_copy_.4788
- __Block_byref_object_copy_.4875
- __Block_byref_object_copy_.5976
- __Block_byref_object_copy_.6381
- __Block_byref_object_copy_.6494
- __Block_byref_object_copy_.6720
- __Block_byref_object_copy_.7079
- __Block_byref_object_copy_.738
- __Block_byref_object_copy_.7566
- __Block_byref_object_copy_.847
- __Block_byref_object_copy_.98
- __Block_byref_object_dispose_.1073
- __Block_byref_object_dispose_.1654
- __Block_byref_object_dispose_.1869
- __Block_byref_object_dispose_.2033
- __Block_byref_object_dispose_.2683
- __Block_byref_object_dispose_.3228
- __Block_byref_object_dispose_.3380
- __Block_byref_object_dispose_.3548
- __Block_byref_object_dispose_.4290
- __Block_byref_object_dispose_.4603
- __Block_byref_object_dispose_.4789
- __Block_byref_object_dispose_.4876
- __Block_byref_object_dispose_.5977
- __Block_byref_object_dispose_.6382
- __Block_byref_object_dispose_.6495
- __Block_byref_object_dispose_.6721
- __Block_byref_object_dispose_.7080
- __Block_byref_object_dispose_.739
- __Block_byref_object_dispose_.7567
- __Block_byref_object_dispose_.848
- __Block_byref_object_dispose_.99
- __OBJC_$_CLASS_METHODS_SSRVTUIHelperFunctionsForSwift
- __OBJC_CLASS_RO_$_SSRVTUIHelperFunctionsForSwift
- __OBJC_METACLASS_RO_$_SSRVTUIHelperFunctionsForSwift
- ___54-[SSRRPISampler markFinishStatusForAllWithCompletion:]_block_invoke
- ___73-[SSRVoiceProfileStore cleanupVoiceProfileModelFilesForLocale:withAsset:]_block_invoke
- ___76+[SSREnrollmentSamplingMetaDataHelper markFinishStatusForAllWithCompletion:]_block_invoke
- ___CSSecureLogInitIfNeeded_block_invoke
- __block_literal_global.1402
- __block_literal_global.1661
- __block_literal_global.2601
- __block_literal_global.3402
- __block_literal_global.3464
- __block_literal_global.35
- __block_literal_global.43
- __block_literal_global.4340
- __block_literal_global.47
- __block_literal_global.5198
- __block_literal_global.5409
- __block_literal_global.6162
- __block_literal_global.6503
- __block_literal_global.6755
- __block_literal_global.6968
- __block_literal_global.7262
- __block_literal_global.7739
- __block_literal_global.8091
- _objc_msgSend$cleanupVoiceProfileModelFilesForLocale:withAsset:
- _objc_msgSend$initWithLocaleIdentifier:withAudioSession:withAppDomain:shouldTrainViaXPC:withSiriSharedUserId:
- _objc_msgSend$initWithSiriSetupID:PageNumber:withPhId:withLocale:withVTAssetConfigVersion:withSessionStatus:
- _objc_msgSend$isValidForRPIWithError:
- _objc_msgSend$logSiriSetupPHSEnrollmentDigitalZeroDetectionCompletedWithSiriSetupID:withPageNumber:withPhId:withMaxNumContinuousZeros:withMaxNumAllowedContinuousZeros:withIsMaxNumContinuousZerosOverThreshold:withLocale:withVTAssetConfigVersion:withStageStatus:
- _objc_msgSend$markFinishStatusForAllWithCompletion:
- _os_log_create
- sharedInstance.onceToken.1401
- sharedInstance.onceToken.3463
- sharedInstance.onceToken.7261
- sharedManager.onceToken.6754
CStrings:
+ " CSVTUITwoPassKeywordDetectorHelper - Init keywordAnalyzer"
+ " CSVTUITwoPassKeywordDetectorHelper - Init phraseDetector"
+ "%s Failed to fetch audio provider with error %@"
+ "%s Fetching audioSessionID: %lu"
+ "%s Sending Profile embeddings: "
+ "%s VoiceProfileId = %@"
+ "%s currentProfile is legacy voice profile before RPI, using voiceprofileId: %@"
+ "%s failed to reset with error: %{public}@"
+ "%s voiceProfileId = %@"
+ "+[SSREnrollmentSamplingMetaDataHelper getEnrollmentIdWithLocale:error:]"
+ "-[SSRVoiceProfileRetrainerPSR _psrProcessorResetSync:]"
+ "-[SSRVoiceProfileStore cleanupVoiceProfileModelFilesForLocale:withAssets:]_block_invoke"
+ "@\"NSData\"24@0:8@\"NSDictionary\"16"
+ "@\"NSDictionary\"24@0:8@\"NSData\"16"
+ "@24@0:8@\"SecureAsset\"16"
+ "@44@0:8@16@24@32B40"
+ "@68@0:8@16i24@28@36@44i52B56B60B64"
+ "CSVTUIKeywordDetectorHelper: Cannot create CSVTUIKeywordDetector since there is no asset available"
+ "CSVTUIKeywordDetectorHelper: Cannot create CSVTUIKeywordDetector since there is no secondPassConfig available"
+ "CSVTUIKeywordDetectorHelper: Invalid Init called"
+ "CSVTUIKeywordDetectorHelper: analyze result is nil!"
+ "CSVTUIKeywordDetectorHelper: analyze result lastKeywordScore: %f"
+ "CSVTUIKeywordDetectorHelper: analyze result score: %f"
+ "CSVTUIKeywordDetectorHelper: keywordAnalyzer:%@ "
+ "CSVTUIKeywordDetectorHelper: phraseConfigs is nil!"
+ "CSVTUIKeywordDetectorHelper: resourcePath, configPath: is non nil"
+ "CSVTUIKeywordDetectorHelper:analyze"
+ "CSVTUIKeywordDetectorHelper:sampleLength, begin:%u, end:%u"
+ "CSVTUIKeywordDetectorHelper:secureAsset non nil"
+ "CSVTUIKeywordDetectorHelper:triggeredUtterance"
+ "CSVTUITwoPassKeywordDetectorHelper: Failed to get secondPass config bailing out"
+ "CSVTUITwoPassKeywordDetectorHelper:secureAsset non nil"
+ "Cannot create CSVTUIKeywordDetectorHelper since we cannot initialize NDAPI"
+ "Cannot create CSVTUIKeywordDetectorHelper since we failed to fetch NDAPI memory Index"
+ "Cannot create CSVTUITwoPassKeywordDetectorHelper since there is no asset available"
+ "Cannot create CSVTUITwoPassKeywordDetectorHelper since we cannot initialize NDAPI"
+ "Cannot create CSVTUITwoPassKeywordDetectorHelper since we failed to NDAP memory Index"
+ "Cannot get VT First pass config"
+ "Cannot initialize phraseDetector"
+ "Faiure in getting the detector info for the phrase"
+ "Phrase detector result: %@"
+ "Platform or device doesn't support User Profiles"
+ "Report as rejection since the detected phId is not the default"
+ "Second pass has required audio, stop feeding"
+ "SpeakerRecognition.CSVTUIKeywordDetectorHelper"
+ "SpeakerRecognition.CSVTUITwoPassKeywordDetectorHelper"
+ "Waiting for the entire audio.."
+ "[dimension = %u]"
+ "[embeddings = %@]"
+ "[numEmbedding = %u]"
+ "[siriSharedUserId = %@]"
+ "[speakerRecognizerType = %lu]"
+ "[voiceProfileId = %@]"
+ "_TtC18SpeakerRecognition27CSVTUIKeywordDetectorHelper"
+ "_TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper"
+ "_TtP18SpeakerRecognition26CSVTUIKeywordDetectorSwift_"
+ "_createAudioSessionRecorder"
+ "_didDetectSpeechStart"
+ "_didFirstPassTrigger"
+ "_didUseTwoPassDetector"
+ "_lastAttemptedUtterance"
+ "_logSessionSummary"
+ "_pageAttemptMap"
+ "_psrProcessorResetSync:"
+ "_speechStartDetected"
+ "_updateAttemptForPageNumber:"
+ "addAudioSync:"
+ "analyzeWithBuffer:"
+ "analyzerTrailingSamples"
+ "audioBuffer"
+ "audioProviderWithContext:error:"
+ "cleanupVoiceProfileModelFilesForLocale:withAssets:"
+ "com.apple.ssr.profile_updated"
+ "getAnalyzedResults"
+ "getEnrollmentMetaDataWithVoiceProfileId:"
+ "init()"
+ "initWithLocaleIdentifier:withAppDomain:"
+ "initWithLocaleIdentifier:withAppDomain:withSiriSharedUserId:shouldTrainViaXPC:"
+ "initWithSecureAsset:"
+ "initWithSecureAsset:supportMph:"
+ "initWithSiriSetupID:PageNumber:withPhId:withLocale:withVTAssetConfigVersion:withSessionStatus:didDetectSpeechStart:didUseTwoPassDetector:didFirstPassTrigger:"
+ "initWithVoiceProfileId:embeddings:numEmbedding:dimension:speakerRecognizerType:"
+ "isMaximized"
+ "isRunningTwoPass"
+ "isTriggerEvent"
+ "keywordAnalyzer"
+ "keywordThreshold"
+ "lastKeywordScore"
+ "logSiriSetupEnrollmentSessionSummaryWithSiriSetupID:lastOpenedPage:completedPage:pageAttemptsMap:"
+ "logSiriSetupPHSEnrollmentDigitalZeroDetectionCompletedWithSiriSetupID:withPageNumber:withPhId:withMaxNumContinuousZeros:withMaxNumAllowedContinuousZeros:withIsMaxNumContinuousZerosOverThreshold:withLocale:withVTAssetConfigVersion:withStageStatus:didDetectSpeechStart:didUseTwoPassDetector:didFirstPassTrigger:"
+ "nil"
+ "phraseDetector"
+ "recognizerThresholdOffset"
+ "recogrecognizerScaleFactornizerScore"
+ "resetForNewRequestSync"
+ "sharedContollerProxy"
+ "supportsMph"
+ "supportsSecureAssetForSpeakerRecognition"
+ "supportsVoiceProfileIDInUserProfile"
+ "totalSampleCount"
+ "triggerEndSampleCount"
+ "triggerFireSampleCount"
+ "triggerScore"
+ "triggerStartSampleCount"
+ "triggeredPhrase"
+ "triggeredPhraseId"
+ "triggeredUtteranceWithVoiceTriggerEventInfo:"
+ "updateVoiceProfileIDInUserProfile:"
+ "\xf0\x91"
- "%s ::: CoreSpeech Secure logging initialized"
- "%s Fetching audioSessionID locally: %lu"
- "%s Get AudioSessionID: %lu"
- "%s markFinishStatusForAllWithCompletion result error : %@"
- "+[SSREnrollmentSamplingMetaDataHelper markFinishStatusForAllWithCompletion:]_block_invoke"
- "-[SSRVTUITrainingMessageHandler getAudioSessionID:]"
- "-[SSRVoiceProfileStore cleanupVoiceProfileModelFilesForLocale:withAsset:]_block_invoke"
- "@52@0:8@16@24@32B40@44"
- "@56@0:8@16i24@28@36@44i52"
- "CSSecureLogInitIfNeeded_block_invoke"
- "ExclaveKit"
- "SSRVTUIHelperFunctionsForSwift"
- "T@\"<CSVTUIAudioSession>\",&,N,V_audioSession"
- "audioSession"
- "getInstalledAssetForLanguage:"
- "initWithLocaleIdentifier:withAudioSession:withAppDomain:"
- "initWithLocaleIdentifier:withAudioSession:withAppDomain:shouldTrainViaXPC:withSiriSharedUserId:"
- "initWithSiriSetupID:PageNumber:withPhId:withLocale:withVTAssetConfigVersion:withSessionStatus:"
- "locale: %@ is found with right domain but donationIds are nil"
- "logSiriSetupPHSEnrollmentDigitalZeroDetectionCompletedWithSiriSetupID:withPageNumber:withPhId:withMaxNumContinuousZeros:withMaxNumAllowedContinuousZeros:withIsMaxNumContinuousZerosOverThreshold:withLocale:withVTAssetConfigVersion:withStageStatus:"
- "markFinishStatusForAllWithCompletion:"
- "profile locale nil for profileId: %@"
- "sampling meta data cannot be created for profileId: %@"
- "saveEncryptedData:atFilepath:"
- "setAudioSession:"
- "v24@0:8@?<v@?@\"NSError\">16"
- "voice profiles cannot be loaded"
- "voiceProfileAudioDirPathForSpidType:toProfile:"
- "\xf0q"

```
