## SiriCrossDeviceArbitration

> `/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration`

```diff

-3302.9.1.0.0
-  __TEXT.__text: 0x2c164
-  __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__objc_methlist: 0x265c
-  __TEXT.__const: 0x135
-  __TEXT.__cstring: 0x5274
-  __TEXT.__constg_swiftt: 0x50
-  __TEXT.__swift5_typeref: 0x6
-  __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x2cc
-  __TEXT.__oslogstring: 0x42f7
-  __TEXT.__dlopen_cstrs: 0x25f
-  __TEXT.__unwind_info: 0xc18
-  __TEXT.__objc_classname: 0x602
-  __TEXT.__objc_methname: 0x6902
-  __TEXT.__objc_methtype: 0x15f6
-  __TEXT.__objc_stubs: 0x4ec0
-  __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0x10a0
-  __DATA_CONST.__objc_classlist: 0x148
+3304.38.2.1.1
+  __TEXT.__text: 0x2f1d4
+  __TEXT.__auth_stubs: 0x800
+  __TEXT.__objc_methlist: 0x2974
+  __TEXT.__const: 0x138
+  __TEXT.__gcc_except_tab: 0x320
+  __TEXT.__oslogstring: 0x4796
+  __TEXT.__cstring: 0x587c
+  __TEXT.__dlopen_cstrs: 0x1ac
+  __TEXT.__unwind_info: 0xc9c
+  __TEXT.__objc_classname: 0x651
+  __TEXT.__objc_methname: 0x774e
+  __TEXT.__objc_methtype: 0x18c9
+  __TEXT.__objc_stubs: 0x55e0
+  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__const: 0x1120
+  __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6488
-  __DATA_CONST.__objc_selrefs: 0x18d8
-  __DATA_CONST.__objc_arraydata: 0x100
-  __AUTH_CONST.__objc_const: 0xea0
+  __DATA_CONST.__objc_const: 0x6a20
+  __DATA_CONST.__objc_selrefs: 0x1b48
+  __DATA_CONST.__objc_classrefs: 0x2d0
+  __DATA_CONST.__objc_superrefs: 0x140
+  __DATA_CONST.__objc_arraydata: 0x148
+  __AUTH_CONST.__objc_const: 0xf78
   __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x2640
-  __AUTH_CONST.__objc_intobj: 0x1e0
+  __AUTH_CONST.__cfstring: 0x27e0
+  __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH_CONST.__auth_got: 0x400
+  __AUTH_CONST.__objc_arrayobj: 0xd8
+  __AUTH_CONST.__auth_got: 0x410
   __AUTH.__objc_data: 0xc80
-  __AUTH.__data: 0xa0
-  __DATA.__objc_classrefs: 0x290
-  __DATA.__objc_superrefs: 0x130
-  __DATA.__objc_ivar: 0x49c
+  __DATA.__objc_ivar: 0x520
   __DATA.__data: 0x6a8
   __DATA.__common: 0x10
-  __DATA.__bss: 0x178
+  __DATA.__bss: 0x168
+  __DATA_DIRTY.__objc_data: 0xa0
+  - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
+  - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
   - /System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics
+  - /System/Library/PrivateFrameworks/SiriCrossDeviceArbitrationFeedback.framework/SiriCrossDeviceArbitrationFeedback
   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
-  - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A8908DA1-C101-30CE-AC8C-7B5B1FFE0CA4
-  Functions: 1078
-  Symbols:   3892
-  CStrings:  2626
+  UUID: 3E4258CA-D5E5-37A1-A163-9FE66680C5A7
+  Functions: 1140
+  Symbols:   4150
+  CStrings:  2843
 
Symbols:
+ +[SCDAArbitrationParticipationContext _convertBoosts:]
+ +[SCDAArbitrationParticipationContext _convertLastActivationTime:]
+ +[SCDAArbitrationParticipationContext _convertTriggerType:]
+ +[SCDAArbitrationParticipationContext _convertTrumpReason:]
+ -[SCDAAccessoryMetricMessage _decodeMetricDataPayload:into:expectedPayloadSize:]
+ -[SCDAAccessoryMetricMessage deviceElectionParticipantIdHighBits]
+ -[SCDAAccessoryMetricMessage deviceElectionParticipantIdLowBits]
+ -[SCDAAccessoryMetricMessage deviceRotatedElectionParticipantIdHighBits]
+ -[SCDAAccessoryMetricMessage deviceRotatedElectionParticipantIdLowBits]
+ -[SCDAAccessoryMetricMessage electionParticipantIdHighBits]
+ -[SCDAAccessoryMetricMessage electionParticipantIdLowBits]
+ -[SCDAAdvertisementContextManager pushSCDAAdvertisementContext:completionHandler:]
+ -[SCDAAdvertisementContextRecord _UUIDFromBytes:]
+ -[SCDAAdvertisementContextRecord _getElectionParticipantIdForVersion:data:]
+ -[SCDAAdvertisementContextRecord electionParticipantId]
+ -[SCDAAdvertisementContextRecord initWithAdvertisementRecordType:voiceTriggerEndTime:advertisementPayload:deviceID:electionParticipantId:]
+ -[SCDAArbitrationParticipationContext .cxx_destruct]
+ -[SCDAArbitrationParticipationContext _processAdvertisements:winnerAdvertisement:]
+ -[SCDAArbitrationParticipationContext boosts]
+ -[SCDAArbitrationParticipationContext cdaId]
+ -[SCDAArbitrationParticipationContext initAdvertisements:decision:requestStartDate:session:voiceTriggerTime:winnerAdvertisement:]
+ -[SCDAArbitrationParticipationContext msSinceLastWin]
+ -[SCDAArbitrationParticipationContext msSinceTrigger]
+ -[SCDAArbitrationParticipationContext myAdvertisement]
+ -[SCDAArbitrationParticipationContext rawGoodnessScore]
+ -[SCDAArbitrationParticipationContext requestStartDate]
+ -[SCDAArbitrationParticipationContext result]
+ -[SCDAArbitrationParticipationContext seenAdvertisements]
+ -[SCDAArbitrationParticipationContext triggerType]
+ -[SCDAArbitrationParticipationContext trumpReasons]
+ -[SCDAArbitrationParticipationContext updateBoosts:triggerType:lastWin:lastDecision:]
+ -[SCDAArbitrationParticipationContext voiceTriggerDate]
+ -[SCDAArbitrationParticipationContext winnerAdvertisement]
+ -[SCDAArbitrationParticipationController .cxx_destruct]
+ -[SCDAArbitrationParticipationController _publishFeedbackArbitrationRecordForNearMiss]
+ -[SCDAArbitrationParticipationController _resetSettingsConnection]
+ -[SCDAArbitrationParticipationController dealloc]
+ -[SCDAArbitrationParticipationController init]
+ -[SCDAArbitrationParticipationController publishArbitrationParticipationContext:]
+ -[SCDAArbitrationParticipationController queue]
+ -[SCDAArbitrationParticipationController setQueue:]
+ -[SCDAArbitrationParticipationController setSettingsConnection:]
+ -[SCDAArbitrationParticipationController setXpcConnectionQueue:]
+ -[SCDAArbitrationParticipationController settingsConnection]
+ -[SCDAArbitrationParticipationController xpcConnectionQueue]
+ -[SCDACoordinator _trackHeySiriStartedAdvertisingAt:]
+ -[SCDACoordinator heySiriStartedAdvertisingAt:timeStamp:]
+ -[SCDACoordinator observeValueForKeyPath:ofObject:change:context:]
+ -[SCDAGoodnessScoreEvaluator _findSidekickBoost:isSpeaker:model:]
+ -[SCDAGoodnessScoreEvaluator _readSidekickBoostsFile:]
+ -[SCDAGoodnessScoreEvaluator _reloadTrialConfiguredBoostValues]
+ -[SCDAGoodnessScoreEvaluator _setSidekickPlatformBiasForSpeaker:model:]
+ -[SCDAGoodnessScoreEvaluator _updateDeviceAdjust:]
+ -[SCDAGoodnessScoreEvaluator _updateDeviceAdjustTrialEnabled:]
+ -[SCDAGoodnessScoreEvaluator _updateMediaPlaybackBoost:]
+ -[SCDAGoodnessScoreEvaluator _updateRecentSiriBoostTrialEnabled:]
+ -[SCDAGoodnessScoreEvaluator _updateRecentSiriExponentialBoostDefined:withSecondDegree:andFirstDegree:andIntercept:]
+ -[SCDAGoodnessScoreEvaluator _updateSidekickBoosts:]
+ -[SCDAGoodnessScoreEvaluator dealloc]
+ -[SCDAGoodnessScoreEvaluator deviceAdjustTrialEnabled]
+ -[SCDAGoodnessScoreEvaluator deviceAdjustTrialValue]
+ -[SCDAGoodnessScoreEvaluator myriadTrialBoostsUpdated:]
+ -[SCDAInstrumentation userFeedbackPublishArbitrationParticipationContext:]
+ -[SCDAMetrics _getElectionParticipantIdWithLowBits:withHighBits:]
+ -[SCDAMetrics getDeviceElectionParticipantId:]
+ -[SCDAMetrics getDeviceRotatedElectionParticipantId:]
+ -[SCDAMetrics getElectionParticipantId:forParticipant:]
+ -[SCDARecord electionParticipantId]
+ -[SCDARecord initWithDeviceID:data:electionParticipantId:]
+ -[SCDARecord setElectionParticipantId:]
+ GCC_except_table1064
+ GCC_except_table213
+ GCC_except_table219
+ GCC_except_table36
+ GCC_except_table435
+ GCC_except_table485
+ GCC_except_table496
+ GCC_except_table506
+ GCC_except_table507
+ GCC_except_table57
+ GCC_except_table604
+ GCC_except_table805
+ GCC_except_table820
+ GCC_except_table827
+ GCC_except_table879
+ GCC_except_table908
+ GCC_except_table957
+ GCC_except_table999
+ _AFMyriadTrialBoostsUpdatedNotification
+ _CBPeripheralManagerOptionShowPowerAlertKey
+ _CC_SHA1_Final
+ _CC_SHA1_Init
+ _CC_SHA1_Update
+ _CFNotificationCenterRemoveObserver
+ _NSStringFromClass
+ _OBJC_CLASS_$_AFFeatureFlags
+ _OBJC_CLASS_$_CBPeripheralManager
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$_SCDAArbitrationParticipationContext
+ _OBJC_CLASS_$_SCDAArbitrationParticipationController
+ _OBJC_CLASS_$_SCDAFAdvertisement
+ _OBJC_CLASS_$_SCDAFBoost
+ _OBJC_CLASS_$_SCDAFParticipation
+ _OBJC_IVAR_$_SCDAAdvertisementContextRecord._electionParticipantId
+ _OBJC_IVAR_$_SCDAArbitrationParticipationContext._boosts
+ _OBJC_IVAR_$_SCDAArbitrationParticipationContext._cdaId
+ _OBJC_IVAR_$_SCDAArbitrationParticipationContext._msSinceLastWin
+ _OBJC_IVAR_$_SCDAArbitrationParticipationContext._msSinceTrigger
+ _OBJC_IVAR_$_SCDAArbitrationParticipationContext._myAdvertisement
+ _OBJC_IVAR_$_SCDAArbitrationParticipationContext._rawGoodnessScore
+ _OBJC_IVAR_$_SCDAArbitrationParticipationContext._requestStartDate
+ _OBJC_IVAR_$_SCDAArbitrationParticipationContext._result
+ _OBJC_IVAR_$_SCDAArbitrationParticipationContext._seenAdvertisements
+ _OBJC_IVAR_$_SCDAArbitrationParticipationContext._triggerType
+ _OBJC_IVAR_$_SCDAArbitrationParticipationContext._trumpReasons
+ _OBJC_IVAR_$_SCDAArbitrationParticipationContext._voiceTriggerDate
+ _OBJC_IVAR_$_SCDAArbitrationParticipationContext._winnerAdvertisement
+ _OBJC_IVAR_$_SCDAArbitrationParticipationController._queue
+ _OBJC_IVAR_$_SCDAArbitrationParticipationController._settingsConnection
+ _OBJC_IVAR_$_SCDAArbitrationParticipationController._xpcConnectionQueue
+ _OBJC_IVAR_$_SCDACoordinator._bleAddress
+ _OBJC_IVAR_$_SCDACoordinator._deviceAdjust_DEPRECATED
+ _OBJC_IVAR_$_SCDACoordinator._rotatedBLEAddress
+ _OBJC_IVAR_$_SCDACoordinator.btPeripheralManager
+ _OBJC_IVAR_$_SCDAGoodnessScoreEvaluator._deviceAdjust
+ _OBJC_IVAR_$_SCDAGoodnessScoreEvaluator._endpointModelName
+ _OBJC_IVAR_$_SCDAGoodnessScoreEvaluator._isDeviceAdjustTrialEnabled
+ _OBJC_IVAR_$_SCDAGoodnessScoreEvaluator._isExponentialBoostDefined
+ _OBJC_IVAR_$_SCDAGoodnessScoreEvaluator._isRecentSiriBoostTrialEnabled
+ _OBJC_IVAR_$_SCDAGoodnessScoreEvaluator._isSpeakerEndpoint
+ _OBJC_IVAR_$_SCDAGoodnessScoreEvaluator._mediaPlaybackBoost
+ _OBJC_IVAR_$_SCDAGoodnessScoreEvaluator._recentSiriFirstDegreeCoefficient
+ _OBJC_IVAR_$_SCDAGoodnessScoreEvaluator._recentSiriIntercept
+ _OBJC_IVAR_$_SCDAGoodnessScoreEvaluator._recentSiriSecondDegreeCoefficient
+ _OBJC_IVAR_$_SCDAInstrumentation._arbitrationParticipationController
+ _OBJC_IVAR_$_SCDAInstrumentation._currentTrigger
+ _OBJC_IVAR_$_SCDAInstrumentation._lastDecisionMachTime
+ _OBJC_IVAR_$_SCDAInstrumentation._lastWinMachTime
+ _OBJC_IVAR_$_SCDARecord._electionParticipantId
+ _OBJC_METACLASS_$_SCDAArbitrationParticipationContext
+ _OBJC_METACLASS_$_SCDAArbitrationParticipationController
+ _SCDAComputeElectionParticipantId
+ _SCDAGoodnessComputeExponentialBoost
+ _SCDAMachAbsoluteTimeGetMilliseconds
+ _SCDAToSISchemaUUID
+ __OBJC_$_CLASS_METHODS_SCDAArbitrationParticipationContext
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.1023
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.2181
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.268
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.362
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.885
+ __OBJC_$_INSTANCE_METHODS_SCDAArbitrationParticipationContext
+ __OBJC_$_INSTANCE_METHODS_SCDAArbitrationParticipationController
+ __OBJC_$_INSTANCE_VARIABLES_SCDAArbitrationParticipationContext
+ __OBJC_$_INSTANCE_VARIABLES_SCDAArbitrationParticipationController
+ __OBJC_$_PROP_LIST_NSObject.1024
+ __OBJC_$_PROP_LIST_NSObject.1512
+ __OBJC_$_PROP_LIST_NSObject.2182
+ __OBJC_$_PROP_LIST_NSObject.2340
+ __OBJC_$_PROP_LIST_NSObject.2501
+ __OBJC_$_PROP_LIST_NSObject.269
+ __OBJC_$_PROP_LIST_NSObject.363
+ __OBJC_$_PROP_LIST_NSObject.499
+ __OBJC_$_PROP_LIST_NSObject.886
+ __OBJC_$_PROP_LIST_SCDAArbitrationParticipationContext
+ __OBJC_$_PROP_LIST_SCDAArbitrationParticipationController
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.1025
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.2183
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.270
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.364
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.887
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.1026
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.2184
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.271
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.365
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.888
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.1027
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.1983
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.2185
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.272
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.366
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.640
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.889
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1028
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1513
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2186
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2341
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2502
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.273
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.367
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.500
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.890
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1029
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1514
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2187
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2342
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2503
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.274
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.368
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.501
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.891
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SCDANotifyObserverDelegate.2504
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.1030
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.2188
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.275
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.369
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.892
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.1031
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.1984
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.2189
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.276
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.370
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.641
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.893
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1032
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1515
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2190
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2343
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2505
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.277
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.371
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.502
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.894
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.1033
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.2191
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.278
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.372
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.895
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SCDANotifyObserverDelegate.2506
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.1034
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.2192
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.279
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.373
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.896
+ __OBJC_$_PROTOCOL_REFS_SCDANotifyObserverDelegate.2507
+ __OBJC_CLASS_RO_$_SCDAArbitrationParticipationContext
+ __OBJC_CLASS_RO_$_SCDAArbitrationParticipationController
+ __OBJC_METACLASS_RO_$_SCDAArbitrationParticipationContext
+ __OBJC_METACLASS_RO_$_SCDAArbitrationParticipationController
+ ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.437
+ ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.441
+ ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.442
+ ___42-[SCDAAssertionCoordinator _addAssertion:]_block_invoke.105
+ ___42-[SCDACoordinator _enterBLEDiagnosticMode]_block_invoke.481
+ ___42-[SCDACoordinator _waitWiProx:andExecute:]_block_invoke.475
+ ___51-[SCDACoordinator _endAdvertisingAnalyticsContext:]_block_invoke.274
+ ___51-[SCDACoordinator _endAdvertisingAnalyticsContext:]_block_invoke.305
+ ___51-[SCDACoordinator _endAdvertisingAnalyticsContext:]_block_invoke.306
+ ___52-[SCDACoordinator _createWaitWiProxTimer:waitBlock:]_block_invoke.474
+ ___55-[SCDAAssertionCoordinator _activateAssertionWithUUID:]_block_invoke.107
+ ___55-[SCDAGoodnessScoreEvaluator myriadTrialBoostsUpdated:]_block_invoke
+ ___63-[SCDAGoodnessScoreEvaluator _reloadTrialConfiguredBoostValues]_block_invoke
+ ___69-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:thenExecute:]_block_invoke.452
+ ___69-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:thenExecute:]_block_invoke.461
+ ___74-[SCDAInstrumentation userFeedbackPublishArbitrationParticipationContext:]_block_invoke
+ ___81-[SCDAArbitrationParticipationController publishArbitrationParticipationContext:]_block_invoke
+ ___82-[SCDAAdvertisementContextManager pushSCDAAdvertisementContext:completionHandler:]_block_invoke
+ ___82-[SCDAAdvertisementContextManager pushSCDAAdvertisementContext:completionHandler:]_block_invoke.1
+ ___82-[SCDAAdvertisementContextManager pushSCDAAdvertisementContext:completionHandler:]_block_invoke_2
+ ___82-[SCDAArbitrationParticipationContext _processAdvertisements:winnerAdvertisement:]_block_invoke
+ ___86-[SCDAArbitrationParticipationController _publishFeedbackArbitrationRecordForNearMiss]_block_invoke
+ ___Block_byref_object_copy_.1088
+ ___Block_byref_object_copy_.1661
+ ___Block_byref_object_dispose_.1089
+ ___Block_byref_object_dispose_.1662
+ ___block_descriptor_48_e8_32r40w_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24lw40l8r32l8
+ ___block_descriptor_48_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_56_e8_32s40s48s_e27_v32?0"SCDARecord"8Q16^B24ls32l8s40l8s48l8
+ ___block_literal_global.1037
+ ___block_literal_global.1121
+ ___block_literal_global.1193
+ ___block_literal_global.1218
+ ___block_literal_global.1245
+ ___block_literal_global.1528
+ ___block_literal_global.16
+ ___block_literal_global.1730
+ ___block_literal_global.2273
+ ___block_literal_global.24
+ ___block_literal_global.2461
+ ___block_literal_global.2581
+ ___block_literal_global.31
+ ___block_literal_global.332
+ ___block_literal_global.334
+ ___block_literal_global.446
+ ___block_literal_global.464
+ ___block_literal_global.466
+ ___block_literal_global.469
+ ___block_literal_global.473
+ ___block_literal_global.49
+ ___block_literal_global.508
+ ___block_literal_global.743
+ ___getWPHeySiriKeyDeviceAddressSymbolLoc_block_invoke
+ ___kCFBooleanFalse
+ ___libAccessibilityLibraryCore_block_invoke
+ __unnamed_array_storage.14.1937
+ __unnamed_array_storage.1532
+ __unnamed_array_storage.1734
+ __unnamed_array_storage.19.1936
+ __unnamed_array_storage.1938
+ __unnamed_array_storage.24
+ __unnamed_array_storage.2585
+ __unnamed_array_storage.29
+ __unnamed_array_storage.34
+ __unnamed_array_storage.39
+ __unnamed_array_storage.44
+ __unnamed_array_storage.9
+ _exp
+ _getWPHeySiriKeyDeviceAddressSymbolLoc.ptr
+ _libAccessibilityLibraryCore.frameworkLibrary
+ _notificationNearMissCallback
+ _objc_msgSend$_UUIDFromBytes:
+ _objc_msgSend$_convertBoosts:
+ _objc_msgSend$_convertTriggerType:
+ _objc_msgSend$_convertTrumpReason:
+ _objc_msgSend$_decodeMetricDataPayload:into:expectedPayloadSize:
+ _objc_msgSend$_getElectionParticipantIdForVersion:data:
+ _objc_msgSend$_getElectionParticipantIdWithLowBits:withHighBits:
+ _objc_msgSend$_processAdvertisements:winnerAdvertisement:
+ _objc_msgSend$_publishFeedbackArbitrationRecordForNearMiss
+ _objc_msgSend$_reloadTrialConfiguredBoostValues
+ _objc_msgSend$_trackHeySiriStartedAdvertisingAt:
+ _objc_msgSend$_updateDeviceAdjust:
+ _objc_msgSend$_updateDeviceAdjustTrialEnabled:
+ _objc_msgSend$_updateMediaPlaybackBoost:
+ _objc_msgSend$_updateRecentSiriBoostTrialEnabled:
+ _objc_msgSend$_updateRecentSiriExponentialBoostDefined:withSecondDegree:andFirstDegree:andIntercept:
+ _objc_msgSend$addObserver:forKeyPath:options:context:
+ _objc_msgSend$array
+ _objc_msgSend$boosts
+ _objc_msgSend$cdaId
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$deviceAdjustTrialEnabled
+ _objc_msgSend$deviceAdjustTrialValue
+ _objc_msgSend$deviceBoost
+ _objc_msgSend$electionParticipantId
+ _objc_msgSend$getDeviceElectionParticipantId:
+ _objc_msgSend$getDeviceRotatedElectionParticipantId:
+ _objc_msgSend$getElectionParticipantId:forParticipant:
+ _objc_msgSend$getTrialEnables:doubleFactors:withCompletion:
+ _objc_msgSend$initAdvertisements:decision:requestStartDate:session:voiceTriggerTime:winnerAdvertisement:
+ _objc_msgSend$initNearMiss
+ _objc_msgSend$initWithAdvertisement:boosts:cdaId:rawGoodnessScore:requestStartDate:result:seenAdvertisements:timeSinceLastTriggerInMilliseconds:timeSinceLastWinInMilliseconds:triggerType:trumpReasons:voiceTriggerDate:winnerAdvertisement:
+ _objc_msgSend$initWithAdvertisementRecordType:voiceTriggerEndTime:advertisementPayload:deviceID:electionParticipantId:
+ _objc_msgSend$initWithContentsOfFile:
+ _objc_msgSend$initWithDelegate:queue:options:
+ _objc_msgSend$initWithDeviceID:data:electionParticipantId:
+ _objc_msgSend$initWithUUIDBytes:
+ _objc_msgSend$isCrossDeviceArbitrationFeedbackEnabled
+ _objc_msgSend$isTrump
+ _objc_msgSend$msSinceLastWin
+ _objc_msgSend$msSinceTrigger
+ _objc_msgSend$myAdvertisement
+ _objc_msgSend$nonConnectableAdvertisingAddress
+ _objc_msgSend$numberWithUnsignedShort:
+ _objc_msgSend$propertyListWithData:options:format:error:
+ _objc_msgSend$publishArbitrationParticipationContext:
+ _objc_msgSend$publishFeedbackArbitrationParticipation:
+ _objc_msgSend$pushSCDAAdvertisementContext:completionHandler:
+ _objc_msgSend$recentAlarmBoost
+ _objc_msgSend$recentMotionBoost
+ _objc_msgSend$recentPlaybackBoost
+ _objc_msgSend$recentRaiseToWakeBoost
+ _objc_msgSend$recentSiriRequestBoost
+ _objc_msgSend$recentUnlockBoost
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$requestStartDate
+ _objc_msgSend$result
+ _objc_msgSend$seenAdvertisements
+ _objc_msgSend$setAdvertHash:
+ _objc_msgSend$setBoostValue:
+ _objc_msgSend$setConfidence:
+ _objc_msgSend$setElectionParticipantId:
+ _objc_msgSend$setKind:
+ _objc_msgSend$setRotatedElectionParticipantId:
+ _objc_msgSend$setType:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$settingsConnection
+ _objc_msgSend$triggerType
+ _objc_msgSend$trumpReasons
+ _objc_msgSend$updateBoosts:triggerType:lastWin:lastDecision:
+ _objc_msgSend$userFeedbackPublishArbitrationParticipationContext:
+ _objc_msgSend$voiceTriggerDate
+ _objc_msgSend$winnerAdvertisement
- -[SCDAAdvertisementContextManager pushMyriadAdvertisementContext:completionHandler:]
- -[SCDAAdvertisementContextRecord _deviceIDFromBytes:]
- -[SCDAAdvertisementContextRecord initWithAdvertisementRecordType:voiceTriggerEndTime:advertisementPayload:deviceID:]
- -[SCDAGoodnessScoreEvaluator _supportsConfigurableBoost]
- -[SCDAGoodnessScoreEvaluator _updateBiasValueWithDefault:]
- -[SCDARecord initWithDeviceID:data:]
- GCC_except_table204
- GCC_except_table210
- GCC_except_table29
- GCC_except_table424
- GCC_except_table470
- GCC_except_table483
- GCC_except_table493
- GCC_except_table50
- GCC_except_table586
- GCC_except_table733
- GCC_except_table752
- GCC_except_table803
- GCC_except_table832
- GCC_except_table881
- GCC_except_table923
- GCC_except_table989
- _AccessibilityLibraryCore.frameworkLibrary
- _AttentionAwarenessLibrary
- _AttentionAwarenessLibraryCore.frameworkLibrary
- _OBJC_CLASS_$__TtCs12_SwiftObject
- _OBJC_IVAR_$_SCDACoordinator._attentionClient
- _OBJC_IVAR_$_SCDACoordinator._deviceAdjust
- _OBJC_IVAR_$_SCDACoordinator._myriadAttentionQueue
- _OBJC_METACLASS_$__TtCs12_SwiftObject
- __DATA__TtC26SiriCrossDeviceArbitration28EntityKitAttentionController
- __METACLASS_DATA__TtC26SiriCrossDeviceArbitration28EntityKitAttentionController
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.1965
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.262
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.353
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.862
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.993
- __OBJC_$_PROP_LIST_NSObject.1508
- __OBJC_$_PROP_LIST_NSObject.1966
- __OBJC_$_PROP_LIST_NSObject.2080
- __OBJC_$_PROP_LIST_NSObject.2245
- __OBJC_$_PROP_LIST_NSObject.263
- __OBJC_$_PROP_LIST_NSObject.354
- __OBJC_$_PROP_LIST_NSObject.491
- __OBJC_$_PROP_LIST_NSObject.863
- __OBJC_$_PROP_LIST_NSObject.994
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.1967
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.264
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.355
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.864
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.995
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.1968
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.265
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.356
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.865
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.996
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.1809
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.1969
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.266
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.357
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.619
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.866
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.997
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1509
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1970
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2081
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2246
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.267
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.358
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.492
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.867
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.998
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1510
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1971
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2082
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2247
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.268
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.359
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.493
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.868
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.999
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SCDANotifyObserverDelegate.2248
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.1000
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.1972
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.269
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.360
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.869
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.1001
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.1810
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.1973
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.270
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.361
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.620
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.870
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1002
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1511
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1974
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2083
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2249
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.271
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.362
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.494
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.871
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.1003
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.1975
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.272
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.363
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.872
- __OBJC_$_PROTOCOL_METHOD_TYPES_SCDANotifyObserverDelegate.2250
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.1004
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.1976
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.273
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.364
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.873
- __OBJC_$_PROTOCOL_REFS_SCDANotifyObserverDelegate.2251
- ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.431
- ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.435
- ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.436
- ___42-[SCDAAssertionCoordinator _addAssertion:]_block_invoke.104
- ___42-[SCDACoordinator _enterBLEDiagnosticMode]_block_invoke.471
- ___42-[SCDACoordinator _waitWiProx:andExecute:]_block_invoke.465
- ___51-[SCDACoordinator _endAdvertisingAnalyticsContext:]_block_invoke.269
- ___51-[SCDACoordinator _endAdvertisingAnalyticsContext:]_block_invoke.300
- ___51-[SCDACoordinator _endAdvertisingAnalyticsContext:]_block_invoke.301
- ___52-[SCDACoordinator _createWaitWiProxTimer:waitBlock:]_block_invoke.464
- ___55-[SCDAAssertionCoordinator _activateAssertionWithUUID:]_block_invoke.106
- ___58-[SCDAGoodnessScoreEvaluator _updateBiasValueWithDefault:]_block_invoke
- ___58-[SCDAGoodnessScoreEvaluator _updateBiasValueWithDefault:]_block_invoke.62
- ___69-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:thenExecute:]_block_invoke.442
- ___69-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:thenExecute:]_block_invoke.451
- ___84-[SCDAAdvertisementContextManager pushMyriadAdvertisementContext:completionHandler:]_block_invoke
- ___84-[SCDAAdvertisementContextManager pushMyriadAdvertisementContext:completionHandler:]_block_invoke.1
- ___84-[SCDAAdvertisementContextManager pushMyriadAdvertisementContext:completionHandler:]_block_invoke_2
- ___88-[SCDACoordinator startAdvertisingFromVoiceTriggerWithGoodnessScoreContext:withContext:]_block_invoke.216
- ___AccessibilityLibraryCore_block_invoke
- ___AttentionAwarenessLibraryCore_block_invoke
- ___Block_byref_object_copy_.1056
- ___Block_byref_object_dispose_.1057
- ___block_descriptor_48_e8_32w_e30_v24?0"NSNumber"8"NSError"16lw32l8
- ___block_literal_global.1007
- ___block_literal_global.1098
- ___block_literal_global.1170
- ___block_literal_global.1196
- ___block_literal_global.1222
- ___block_literal_global.13
- ___block_literal_global.1524
- ___block_literal_global.1660
- ___block_literal_global.2054
- ___block_literal_global.21
- ___block_literal_global.2206
- ___block_literal_global.2325
- ___block_literal_global.26
- ___block_literal_global.326
- ___block_literal_global.328
- ___block_literal_global.37
- ___block_literal_global.441
- ___block_literal_global.454
- ___block_literal_global.456
- ___block_literal_global.459
- ___block_literal_global.463
- ___block_literal_global.500
- ___block_literal_global.722
- ___getAWAttentionAwarenessClientClass_block_invoke
- ___getAWAttentionAwarenessConfigurationClass_block_invoke
- __unnamed_array_storage.1528
- __unnamed_array_storage.1664
- __unnamed_array_storage.2329
- _audit_stringAccessibility
- _audit_stringAttentionAwareness
- _getAWAttentionAwarenessClientClass.softClass
- _getAWAttentionAwarenessConfigurationClass.softClass
- _objc_msgSend$_createSettingsConnectionIfRequired
- _objc_msgSend$_deviceIDFromBytes:
- _objc_msgSend$_supportsConfigurableBoost
- _objc_msgSend$_updateBiasValueWithDefault:
- _objc_msgSend$faceDetectedBoostWithContext:
- _objc_msgSend$getPlatformBiasValue:
- _objc_msgSend$initWithAdvertisementRecordType:voiceTriggerEndTime:advertisementPayload:deviceID:
- _objc_msgSend$initWithDeviceID:data:
- _objc_msgSend$isMetadataValid
- _objc_msgSend$pollForAttentionWithTimeout:event:error:
- _objc_msgSend$pushMyriadAdvertisementContext:completionHandler:
- _objc_msgSend$resumeWithError:
- _objc_msgSend$setConfiguration:
- _objc_msgSend$setEventMask:
- _objc_msgSend$setIdentifier:
- _objc_msgSend$suspendWithError:
- _objc_opt_self
- _swift_allocObject
- _swift_deallocClassInstance
- _swift_lookUpClassMethod
- _symbolic _____ 26SiriCrossDeviceArbitration28EntityKitAttentionControllerC
CStrings:
+ "\x01a\x13\x11"
+ "\x12("
+ "#"
+ "%s #myriad CarPlay override"
+ "%s #myriad CarPlay override %@"
+ "%s #scda"
+ "%s #scda #feedback"
+ "%s #scda #feedback near miss!"
+ "%s #scda %@"
+ "%s #scda BTLE CarPlay trigger signal received"
+ "%s #scda BTLE WiProx readiness timer timed out, WiProx not called"
+ "%s #scda BTLE audio data signal received"
+ "%s #scda BTLE could not open audio data file"
+ "%s #scda BTLE could not read 4 bytes from audio data file"
+ "%s #scda BTLE could open audio data file, MYR_EXT_FINGERPRINT_LEN: %d"
+ "%s #scda BTLE device class: %@ (%@) detected, adjusting goodness by %d incomingAdjustment %d, rawAudioGoodnessScore: %d"
+ "%s #scda BTLE done waiting on WiProx to execute"
+ "%s #scda BTLE emergency signal received"
+ "%s #scda BTLE in ear trigger signal received"
+ "%s #scda BTLE in-task continious voice trigger heard. NOT ignoring."
+ "%s #scda BTLE in-task continuous voice trigger heard too soon. Ignoring."
+ "%s #scda BTLE myriad decision fetch signal received"
+ "%s #scda BTLE not ready, waiting to execute for up to %ld msecs (current HeySiri WPState %ld)"
+ "%s #scda BTLE opening audio file at path %{private}s"
+ "%s #scda BTLE overriding to constant goodness %d"
+ "%s #scda BTLE overriding to goodness %@"
+ "%s #scda BTLE self trigger signal received"
+ "%s #scda Clearing myriad session %@"
+ "%s #scda Context collector returned 0 SCDAAdvertisementContextRecords instances"
+ "%s #scda CurrentTime: %f TrigerTime: %f, ElectionAdvertisementTime: %f, triggerDelta: %f, electionAdvertisementRemainingTime: %f [isIntaskTooSoonForVoiceTriggerActivation = %d, isIntaskTooSoonForDirectActivation = %d, currentElectionAdvertisementIsSane = %d]"
+ "%s #scda Device Adjust Trial Enable not loaded"
+ "%s #scda Device Adjust Trial Value not loaded"
+ "%s #scda Downgrading goodness as HS invocation too soon %f for score %d"
+ "%s #scda Dropped %@ from %@ because there's no device ID."
+ "%s #scda Election advertisement %@ -> %@"
+ "%s #scda Election advertisement %@ added to myriad session %@"
+ "%s #scda Error loading Trial factors: %@"
+ "%s #scda Error updating sidekick boosts: unsupported platform"
+ "%s #scda Error: %@"
+ "%s #scda Error: Attempting to assign out of bounds device adjust: %ld"
+ "%s #scda Error: Unexpected device class %du masked to: %du"
+ "%s #scda Event token: %@, current event token: %@"
+ "%s #scda Force stopping BTLE scan"
+ "%s #scda Goodness score override state %@"
+ "%s #scda Initialized myriad session %@ when myriad is in state %@"
+ "%s #scda Logging Trial defined Device Adjust Value: %du"
+ "%s #scda Method called on unexpected thread (curr:%{private}s expected:%{private}s)"
+ "%s #scda Not pushing myriad advertisement context - HAL enabled: %d, direct activation: %d"
+ "%s #scda Not pushing myriad advertisement context - Valid voicetrigger endtime: %d (curr time: %llu, time since device boot: %llu)"
+ "%s #scda Pushing Myriad advertisement context is complete"
+ "%s #scda Recent Siri Boost Trial Enable Not Loaded"
+ "%s #scda Recent Siri exponential factors not loaded: %@ %@ %@"
+ "%s #scda Suppressing the current device due to late trigger (voicetrigger endtime: %f, advertisement dispatch time: %f, advertisement delay: %f, myriad record count: %ld)"
+ "%s #scda Trial HomePod Boost not loaded: %@"
+ "%s #scda Trial Playback Boost not loaded: %@"
+ "%s #scda Using Trial defined Device Adjust Value: %du"
+ "%s #scda WiProx readiness timer initialized"
+ "%s #scda WiProx readiness timer suspended"
+ "%s #scda WiProx readiness timer wait block cleared"
+ "%s #scda Won by a small margin, storing state to mitigate recency boost"
+ "%s #scda _AXSAttentionAwarenessFeaturesEnabled %@"
+ "%s #scda _deviceAdjust=%d, adjustment= %d"
+ "%s #scda _shouldUseContextCollector is fslse"
+ "%s #scda _voiceTriggerTime: %llu"
+ "%s #scda adjusted score: %ld"
+ "%s #scda adv dispatch time: %f, voice trigger end time: %f, time since voice trigger: %f (curr time: %llu, time since device boot: %llu), advertisment: %@"
+ "%s #scda alarm/timer boosting is no longer allowed"
+ "%s #scda attention is boosting goodness score, rawAudioGoodnessScore %u, goodness:%u bump: %u, tieBreaker:%u, _myriadState: %@"
+ "%s #scda bumping goodness score (reason: media playback active, adjusted score: %d)"
+ "%s #scda bumping goodness score (reason: media playback interrupted, last playback time: %f seconds ago, adjusted score: %d)"
+ "%s #scda bumping goodness score (reason: platform bias, adjusted bias: %d)"
+ "%s #scda bumptoGoodness secsAgo=%f yields %d = %f(act) + %f(siri)"
+ "%s #scda coordinationEnabled=%d, BLEActivityEnabled=%d "
+ "%s #scda current advId: %@ is different from the advId for which the myriad context was dispatched: %@"
+ "%s #scda device adjust trial enabled: %du"
+ "%s #scda device adjust value: %ld"
+ "%s #scda device is unlocked, compute bump"
+ "%s #scda didRequestForBTLEAdvertisement: %s -> %s, didRequestForBTLEScan: %s -> %s"
+ "%s #scda endTime from a file is good, secondsSinceTrigger=%f"
+ "%s #scda endTime from a file is too old, secondsSinceTrigger=%f"
+ "%s #scda exponential bump %f"
+ "%s #scda force win on this device with context: %@, triggerRecord: %@"
+ "%s #scda got attention, ignoring too-soon time limit."
+ "%s #scda ignoring advert from other deviceGroup %d: %@ data=%@"
+ "%s #scda ignoring recent event bump"
+ "%s #scda newGoodness: %d"
+ "%s #scda not initializing myriad session, myriad is in state %@"
+ "%s #scda overrideContext: %@, _incomingAdjustment %d"
+ "%s #scda payload adjusted score: %ld"
+ "%s #scda previous close win: canceling recency bump from secsAgo=%f yields %f = %f(act) + %f(siri)"
+ "%s #scda reading defaults"
+ "%s #scda reading defaults: BTLE device class: %@ (%@) detected, category %ld, adjusting goodness by %ld, std delay %f, trump delay %f, vt_endtime threshold %f"
+ "%s #scda reading server provisioned defaults"
+ "%s #scda removing negative iPad device boost (adding %d back) due to activationSource"
+ "%s #scda requestIdNotification: %@"
+ "%s #scda setupEnabled: %d, current state: %@"
+ "%s #scda trial exponential boost configured, replacing %f with %du"
+ "%s #scda triggerABCForSubType failed: %@"
+ "%s #scda unlock bump is ignored due to awareness being on"
+ "%s #scda updated Trial Device Adjust to (Enabled: %@) Value %ld"
+ "%s #scda updated Trial recent Siri exponential boost to %du %.12f %.12f %.12f"
+ "%s #scda updated _isRecentSiriBoostTrialEnabled to %@"
+ "%s #scda updated _mediaPlaybackBoost to %d"
+ "%s #scda updated isDeviceAdjustTrialEnabled to Enabled: %@ (Value: %ld)"
+ "%s #scda updated platform bias to %d"
+ "%s #scda watch trumping due to score being 0"
+ "%s #scda watch trumping due to threshold for rawAudioGoodnessScore: %u >= %u"
+ "%s #scda-advertisementcontext: Received wedged Myriad advertisement context record %@"
+ "%s BTLE address changed from %@ to %@"
+ "%s BTLE address initialized to %@ "
+ "%s BTLE daemon advertising begins at: %lld"
+ "%s BTLE daemon advertising ends at: %lld"
+ "%s BTLE daemon asked to start advertise at: %lld"
+ "%s BTLE delay finished, advertising: %@ address: %@"
+ "%s BTLE duplicate address change ignored"
+ "%s No longer used by this device."
+ "%s Not yet supported on this device."
+ "%s SCDARecord initfrom: %@ - %@ - %@"
+ "%s Trial Boosts Updated Notification"
+ "%s Unable to find sidekick boosts plist at path %@."
+ "%s Unable to initialize sidekick boosts from plist file at path %@ due to error %@"
+ "%s Unable to read sidekick boosts plist file at path %@."
+ "%s Unexpected type of initialized sidekick boosts plist %@."
+ "%s _readSidekickBoostsFile: called with empty filepath"
+ "-[SCDAAdvertisementContextManager pushSCDAAdvertisementContext:completionHandler:]_block_invoke"
+ "-[SCDAAdvertisementContextManager pushSCDAAdvertisementContext:completionHandler:]_block_invoke_2"
+ "-[SCDAArbitrationParticipationController _publishFeedbackArbitrationRecordForNearMiss]_block_invoke"
+ "-[SCDACoordinator _advertiseIndefinite:]_block_invoke"
+ "-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:thenExecute:]_block_invoke_2"
+ "-[SCDACoordinator heySiriStartedAdvertisingAt:timeStamp:]"
+ "-[SCDACoordinator observeValueForKeyPath:ofObject:change:context:]"
+ "-[SCDAGoodnessScoreEvaluator _readSidekickBoostsFile:]"
+ "-[SCDAGoodnessScoreEvaluator _reloadTrialConfiguredBoostValues]_block_invoke"
+ "-[SCDAGoodnessScoreEvaluator _updateDeviceAdjust:]"
+ "-[SCDAGoodnessScoreEvaluator _updateDeviceAdjustTrialEnabled:]"
+ "-[SCDAGoodnessScoreEvaluator _updateMediaPlaybackBoost:]"
+ "-[SCDAGoodnessScoreEvaluator _updateRecentSiriBoostTrialEnabled:]"
+ "-[SCDAGoodnessScoreEvaluator _updateRecentSiriExponentialBoostDefined:withSecondDegree:andFirstDegree:andIntercept:]"
+ "-[SCDAGoodnessScoreEvaluator _updateSidekickBoosts:]"
+ "-[SCDAGoodnessScoreEvaluator deviceAdjustTrialEnabled]"
+ "-[SCDAGoodnessScoreEvaluator deviceAdjustTrialValue]"
+ "-[SCDAGoodnessScoreEvaluator myriadTrialBoostsUpdated:]_block_invoke"
+ "-[SCDARecord initWithDeviceID:data:electionParticipantId:]"
+ "-[SCDARecord setDeviceClass:]"
+ "/usr/lib/libAccessibility.dylib"
+ "/usr/local/lib/libAccessibility.dylib"
+ "3"
+ "7\x11\x11w\x11Q\x136\x11B\x12\x1c\x12\x14"
+ "73fa281b-4376-5284-8d9f-dc7ec5ad068f"
+ "@\"CBPeripheralManager\""
+ "@\"NSArray\""
+ "@\"NSNumber\""
+ "@\"SCDAArbitrationParticipationController\""
+ "@\"SCDAFAdvertisement\""
+ "@24@0:8^{MyriadMetricsDataV2=CQCQCddCCCCCCdCCC[50C][50C][50C]CQQQQ[50Q][50Q]}16"
+ "@28@0:8^{MyriadMetricsDataV2=CQCQCddCCCCCCdCCC[50C][50C][50C]CQQQQ[50Q][50Q]}16i24"
+ "@32@0:8Q16Q24"
+ "@56@0:8q16d24@32@40@48"
+ "@60@0:8@16B24@28@36d44@52"
+ "AFArbitrationParticipationQueue"
+ "AFArbitrationParticipationXPCConnectionQueue"
+ "B32@0:8@16^{MyriadMetricsDataV2=CQCQCddCCCCCCdCCC[50C][50C][50C]CQQQQ[50Q][50Q]}24"
+ "B40@0:8@16^{MyriadMetricsDataV2=CQCQCddCCCCCCdCCC[50C][50C][50C]CQQQQ[50Q][50Q]}24Q32"
+ "CarPlay request"
+ "DEVICE_ADJUST"
+ "DEVICE_ADJUST_ENABLE"
+ "HOMEPOD_BOOST"
+ "I24@0:8^{MyriadMetricsDataV2=CQCQCddCCCCCCdCCC[50C][50C][50C]CQQQQ[50Q][50Q]}16"
+ "Q20@0:8i16"
+ "Q36@0:8@16B24@28"
+ "RECENT_PLAYBACK_BOOST"
+ "RECENT_SIRI_BOOST_FIRST_DEGREE_COEFF"
+ "RECENT_SIRI_BOOST_INTERCEPT"
+ "RECENT_SIRI_BOOST_SECOND_DEGREE_COEFF"
+ "RECENT_SIRI_BOOST_TRIAL_ENABLE"
+ "SCDA"
+ "SCDAAdvertisementContextRecord: contextVersion=%ld vtEndTime=%f advRecordType=%ld advPayload=0x%@ deviceID=%@ electionParticipantId=%@"
+ "SCDAArbitrationParticipationContext"
+ "SCDAArbitrationParticipationController"
+ "SCDAGoodnessComputeExponentialBoost"
+ "T@\"AFSettingsConnection\",&,N,V_settingsConnection"
+ "T@\"NSArray\",R,N,V_boosts"
+ "T@\"NSArray\",R,N,V_seenAdvertisements"
+ "T@\"NSArray\",R,N,V_trumpReasons"
+ "T@\"NSDate\",R,C,N,V_requestStartDate"
+ "T@\"NSDate\",R,C,N,V_voiceTriggerDate"
+ "T@\"NSNumber\",R,N,V_msSinceLastWin"
+ "T@\"NSNumber\",R,N,V_msSinceTrigger"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_xpcConnectionQueue"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C,N,V_cdaId"
+ "T@\"NSUUID\",C,N,V_electionParticipantId"
+ "T@\"NSUUID\",R,C,N,V_electionParticipantId"
+ "T@\"SCDAFAdvertisement\",R,N,V_myAdvertisement"
+ "T@\"SCDAFAdvertisement\",R,N,V_winnerAdvertisement"
+ "TQ,R,N,V_result"
+ "TQ,R,N,V_triggerType"
+ "T^Q,R,N"
+ "Tq,R,N"
+ "WPHeySiriKeyDeviceAddress"
+ "^Q16@0:8"
+ "_UUIDFromBytes:"
+ "_arbitrationParticipationController"
+ "_bleAddress"
+ "_boosts"
+ "_cdaId"
+ "_convertBoosts:"
+ "_convertLastActivationTime:"
+ "_convertTriggerType:"
+ "_convertTrumpReason:"
+ "_currentTrigger"
+ "_decodeMetricDataPayload:into:expectedPayloadSize:"
+ "_deviceAdjust_DEPRECATED"
+ "_electionParticipantId"
+ "_endpointModelName"
+ "_findSidekickBoost:isSpeaker:model:"
+ "_getElectionParticipantIdForVersion:data:"
+ "_getElectionParticipantIdWithLowBits:withHighBits:"
+ "_isDeviceAdjustTrialEnabled"
+ "_isExponentialBoostDefined"
+ "_isRecentSiriBoostTrialEnabled"
+ "_isSpeakerEndpoint"
+ "_lastDecisionMachTime"
+ "_lastWinMachTime"
+ "_mediaPlaybackBoost"
+ "_msSinceLastWin"
+ "_msSinceTrigger"
+ "_myAdvertisement"
+ "_processAdvertisements:winnerAdvertisement:"
+ "_publishFeedbackArbitrationRecordForNearMiss"
+ "_readSidekickBoostsFile:"
+ "_recentSiriFirstDegreeCoefficient"
+ "_recentSiriIntercept"
+ "_recentSiriSecondDegreeCoefficient"
+ "_reloadTrialConfiguredBoostValues"
+ "_requestStartDate"
+ "_result"
+ "_rotatedBLEAddress"
+ "_seenAdvertisements"
+ "_setSidekickPlatformBiasForSpeaker:model:"
+ "_trackHeySiriStartedAdvertisingAt:"
+ "_triggerType"
+ "_trumpReasons"
+ "_updateDeviceAdjust:"
+ "_updateDeviceAdjustTrialEnabled:"
+ "_updateMediaPlaybackBoost:"
+ "_updateRecentSiriBoostTrialEnabled:"
+ "_updateRecentSiriExponentialBoostDefined:withSecondDegree:andFirstDegree:andIntercept:"
+ "_updateSidekickBoosts:"
+ "_voiceTriggerDate"
+ "_winnerAdvertisement"
+ "_xpcConnectionQueue"
+ "addObserver:forKeyPath:options:context:"
+ "advertisingAddress"
+ "array"
+ "boosts"
+ "btPeripheralManager"
+ "cc=%d epId=%@ MyriadRecord: hash=%#04x,good=%d,conf=%d,dc=%d,pt=%d,tb=%d,isMe=%@,g=%d"
+ "cdaId"
+ "com.apple.voicetrigger.NearTrigger"
+ "d24@0:8^{MyriadMetricsDataV2=CQCQCddCCCCCCdCCC[50C][50C][50C]CQQQQ[50Q][50Q]}16"
+ "dateWithTimeIntervalSinceNow:"
+ "deviceAdjustTrialEnabled"
+ "deviceAdjustTrialValue"
+ "deviceBoost"
+ "deviceElectionParticipantIdHighBits"
+ "deviceElectionParticipantIdLowBits"
+ "deviceRotatedElectionParticipantIdHighBits"
+ "deviceRotatedElectionParticipantIdLowBits"
+ "electionParticipantId"
+ "electionParticipantIdHighBits"
+ "electionParticipantIdLowBits"
+ "getDeviceElectionParticipantId:"
+ "getDeviceRotatedElectionParticipantId:"
+ "getElectionParticipantId:forParticipant:"
+ "getTrialEnables:doubleFactors:withCompletion:"
+ "id"
+ "initAdvertisements:decision:requestStartDate:session:voiceTriggerTime:winnerAdvertisement:"
+ "initNearMiss"
+ "initWithAdvertisement:boosts:cdaId:rawGoodnessScore:requestStartDate:result:seenAdvertisements:timeSinceLastTriggerInMilliseconds:timeSinceLastWinInMilliseconds:triggerType:trumpReasons:voiceTriggerDate:winnerAdvertisement:"
+ "initWithAdvertisementRecordType:voiceTriggerEndTime:advertisementPayload:deviceID:electionParticipantId:"
+ "initWithContentsOfFile:"
+ "initWithDelegate:queue:options:"
+ "initWithDeviceID:data:electionParticipantId:"
+ "initWithUUIDBytes:"
+ "isCrossDeviceArbitrationFeedbackEnabled"
+ "isTrump"
+ "msSinceLastWin"
+ "msSinceTrigger"
+ "myAdvertisement"
+ "myriadTrialBoostsUpdated:"
+ "nonConnectableAdvertisingAddress"
+ "notificationNearMissCallback"
+ "numberWithUnsignedShort:"
+ "observeValueForKeyPath:ofObject:change:context:"
+ "propertyListWithData:options:format:error:"
+ "publishArbitrationParticipationContext:"
+ "publishFeedbackArbitrationParticipation:"
+ "pushSCDAAdvertisementContext:completionHandler:"
+ "queue"
+ "recentAlarmBoost"
+ "recentMotionBoost"
+ "recentPlaybackBoost"
+ "recentRaiseToWakeBoost"
+ "recentSiriRequestBoost"
+ "recentUnlockBoost"
+ "removeObserver:"
+ "requestStartDate"
+ "result"
+ "scdaAdvertisementContext"
+ "seenAdvertisements"
+ "setAdvertHash:"
+ "setBoostValue:"
+ "setConfidence:"
+ "setElectionParticipantId:"
+ "setKind:"
+ "setQueue:"
+ "setRotatedElectionParticipantId:"
+ "setSettingsConnection:"
+ "setType:"
+ "setValue:forKey:"
+ "setXpcConnectionQueue:"
+ "settingsConnection"
+ "triggerType"
+ "trumpReasons"
+ "updateBoosts:triggerType:lastWin:lastDecision:"
+ "userFeedbackPublishArbitrationParticipationContext:"
+ "v28@0:8B16@20"
+ "v32@?0@\"NSDictionary\"8@\"NSDictionary\"16@\"NSError\"24"
+ "v44@0:8@16i24Q28Q36"
+ "v44@0:8B16d20d28d36"
+ "v48@0:8@16@24@32^v40"
+ "v48@0:8^{MyriadMetricsDataV2=CQCQCddCCCCCCdCCC[50C][50C][50C]CQQQQ[50Q][50Q]}16@24@32@?40"
+ "voiceTriggerDate"
+ "winnerAdvertisement"
+ "winner_election_participant_id"
+ "xpcConnectionQueue"
+ "{MyriadMetricsDataV2=\"version\"C\"sessionId\"Q\"eventType\"C\"requestType\"Q\"state\"C\"advDelay\"d\"advInterval\"d\"coordinationAllowed\"C\"winnerGoodnessScore\"C\"winnerProductType\"C\"winnerDeviceClass\"C\"homepodInvolved\"C\"previousDecision\"C\"previousDecisionTime\"d\"deviceGroup\"C\"decision\"C\"lateToElection\"C\"electionParticipantGoodnessScore\"[50C]\"electionParticipantDeviceType\"[50C]\"electionParticipantProductType\"[50C]\"electionParticipantCount\"C\"deviceElectionParticipantIdLowBits\"Q\"deviceElectionParticipantIdHighBits\"Q\"deviceRotatedElectionParticipantIdLowBits\"Q\"deviceRotatedElectionParticipantIdHighBits\"Q\"electionParticipantIdLowBits\"[50Q]\"electionParticipantIdHighBits\"[50Q]}"
+ "{MyriadMetricsDataV2=CQCQCddCCCCCCdCCC[50C][50C][50C]CQQQQ[50Q][50Q]}16@0:8"
- "\x01\x11\x13"
- "\""
- "%s #myriad"
- "%s #myriad %@"
- "%s #myriad BTLE CarPlay trigger signal received"
- "%s #myriad BTLE WiProx readiness timer timed out, WiProx not called"
- "%s #myriad BTLE audio data signal received"
- "%s #myriad BTLE could not open audio data file"
- "%s #myriad BTLE could not read 4 bytes from audio data file"
- "%s #myriad BTLE could open audio data file, MYR_EXT_FINGERPRINT_LEN: %d"
- "%s #myriad BTLE device class: %@ (%@) detected, adjusting goodness by %d incomingAdjustment %d, rawAudioGoodnessScore: %d"
- "%s #myriad BTLE done waiting on WiProx to execute"
- "%s #myriad BTLE emergency signal received"
- "%s #myriad BTLE in ear trigger signal received"
- "%s #myriad BTLE in-task continious voice trigger heard. NOT ignoring."
- "%s #myriad BTLE in-task continuous voice trigger heard too soon. Ignoring."
- "%s #myriad BTLE myriad decision fetch signal received"
- "%s #myriad BTLE not ready, waiting to execute for up to %ld msecs (current HeySiri WPState %ld)"
- "%s #myriad BTLE opening audio file at path %{private}s"
- "%s #myriad BTLE overriding to constant goodness %d"
- "%s #myriad BTLE overriding to goodness %@"
- "%s #myriad BTLE self trigger signal received"
- "%s #myriad Clearing myriad session %@"
- "%s #myriad Context collector returned 0 SCDAAdvertisementContextRecords instances"
- "%s #myriad CurrentTime: %f TrigerTime: %f, ElectionAdvertisementTime: %f, triggerDelta: %f, electionAdvertisementRemainingTime: %f [isIntaskTooSoonForVoiceTriggerActivation = %d, isIntaskTooSoonForDirectActivation = %d, currentElectionAdvertisementIsSane = %d]"
- "%s #myriad Downgrading goodness as HS invocation too soon %f for score %d"
- "%s #myriad Dropped %@ from %@ because there's no device ID."
- "%s #myriad Election advertisement %@ -> %@"
- "%s #myriad Election advertisement %@ added to myriad session %@"
- "%s #myriad Error: %@"
- "%s #myriad Event token: %@, current event token: %@"
- "%s #myriad Failed to fetch platform bias from Trial: %@ using %lu as platform boost."
- "%s #myriad Force stopping BTLE scan"
- "%s #myriad Goodness score override state %@"
- "%s #myriad Initialized myriad session %@ when myriad is in state %@"
- "%s #myriad Method called on unexpected thread (curr:%{private}s expected:%{private}s)"
- "%s #myriad Not pushing myriad advertisement context - HAL enabled: %d, direct activation: %d"
- "%s #myriad Not pushing myriad advertisement context - Valid voicetrigger endtime: %d (curr time: %llu, time since device boot: %llu)"
- "%s #myriad Pushing Myriad advertisement context is complete"
- "%s #myriad Suppressing the current device due to late trigger (voicetrigger endtime: %f, advertisement dispatch time: %f, advertisement delay: %f, myriad record count: %ld)"
- "%s #myriad WiProx readiness timer initialized"
- "%s #myriad WiProx readiness timer suspended"
- "%s #myriad WiProx readiness timer wait block cleared"
- "%s #myriad Won by a small margin, storing state to mitigate recency boost"
- "%s #myriad _AXSAttentionAwarenessFeaturesEnabled %@"
- "%s #myriad _deviceAdjust=%d, adjustment= %d"
- "%s #myriad _shouldUseContextCollector is fslse"
- "%s #myriad _voiceTriggerTime: %llu"
- "%s #myriad adjusted score: %ld"
- "%s #myriad adv dispatch time: %f, voice trigger end time: %f, time since voice trigger: %f (curr time: %llu, time since device boot: %llu), advertisment: %@"
- "%s #myriad attention awareness received attention event: %@, error: %@"
- "%s #myriad attention end"
- "%s #myriad attention failed suspendWithError: %@"
- "%s #myriad attention failed with resumeWithError: %@"
- "%s #myriad attention is boosting goodness score, rawAudioGoodnessScore %u, goodness:%u bump: %u, tieBreaker:%u, _myriadState: %@"
- "%s #myriad attention start"
- "%s #myriad attention timed out with event: %@, error: %@"
- "%s #myriad bumping goodness score (reason: alarm/timer firing, adjusted score: %d)"
- "%s #myriad bumping goodness score (reason: media playback active, adjusted score: %d)"
- "%s #myriad bumping goodness score (reason: media playback interrupted, last playback time: %f seconds ago, adjusted score: %d)"
- "%s #myriad bumping goodness score (reason: platform bias, adjusted bias: %d)"
- "%s #myriad bumptoGoodness secsAgo=%f yields %d = %f(act) + %f(siri)"
- "%s #myriad coordinationEnabled=%d, BLEActivityEnabled=%d "
- "%s #myriad current advId: %@ is different from the advId for which the myriad context was dispatched: %@"
- "%s #myriad device is unlocked, compute bump"
- "%s #myriad didRequestForBTLEAdvertisement: %s -> %s, didRequestForBTLEScan: %s -> %s"
- "%s #myriad endTime from a file is good, secondsSinceTrigger=%f"
- "%s #myriad endTime from a file is too old, secondsSinceTrigger=%f"
- "%s #myriad force win on this device with context: %@, triggerRecord: %@"
- "%s #myriad got attention, ignoring too-soon time limit."
- "%s #myriad ignoring advert from other deviceGroup %d: %@ data=%@"
- "%s #myriad ignoring recent event bump"
- "%s #myriad newGoodness: %d"
- "%s #myriad not initializing myriad session, myriad is in state %@"
- "%s #myriad overrideContext: %@, _incomingAdjustment %d"
- "%s #myriad payload adjusted score: %ld"
- "%s #myriad platform bias value fetched from Trial: %lu"
- "%s #myriad platform bias value:%@, error: %@"
- "%s #myriad previous close win: canceling recency bump from secsAgo=%f yields %f = %f(act) + %f(siri)"
- "%s #myriad reading defaults"
- "%s #myriad reading defaults: BTLE device class: %@ (%@) detected, category %ld, adjusting goodness by %ld, std delay %f, trump delay %f, vt_endtime threshold %f"
- "%s #myriad reading server provisioned defaults"
- "%s #myriad removing negative iPad device boost (adding %d back) due to activationSource"
- "%s #myriad requestIdNotification: %@"
- "%s #myriad setupEnabled: %d, current state: %@"
- "%s #myriad triggerABCForSubType failed: %@"
- "%s #myriad unlock bump is ignored due to awareness being on"
- "%s #myriad updating platform bias to %d"
- "%s #myriad watch trumping due to score being 0"
- "%s #myriad watch trumping due to threshold for rawAudioGoodnessScore: %u >= %u"
- "%s #myriad-advertisementcontext: Received wedged Myriad advertisement context record %@"
- "%s BTLE daemon advertising begins"
- "%s BTLE daemon advertising ends"
- "%s BTLE delay finished, advertising: %@"
- "%s SCDARecord initfrom: %@ - %@"
- "-[SCDAAdvertisementContextManager pushMyriadAdvertisementContext:completionHandler:]_block_invoke"
- "-[SCDAAdvertisementContextManager pushMyriadAdvertisementContext:completionHandler:]_block_invoke_2"
- "-[SCDAGoodnessScoreEvaluator _updateBiasValueWithDefault:]_block_invoke"
- "-[SCDARecord initWithDeviceID:data:]"
- "2"
- "7\x11\x11x\x11Q\x115\x11B\x12\x1c\x13\x14"
- "@\"AWAttentionAwarenessClient\""
- "@24@0:8^{MyriadMetricsDataV1=CQCQCddCCCCCCdCCC[50C][50C][50C]C}16"
- "@48@0:8q16d24@32@40"
- "AWAttentionAwarenessClient"
- "AWAttentionAwarenessConfiguration"
- "B32@0:8@16^{MyriadMetricsDataV1=CQCQCddCCCCCCdCCC[50C][50C][50C]C}24"
- "I24@0:8^{MyriadMetricsDataV1=CQCQCddCCCCCCdCCC[50C][50C][50C]C}16"
- "MyriadRecord: hash=%#04x,good=%d,conf=%d,dc=%d,pt=%d,tb=%d,isMe=%@,g=%d,cc=%d"
- "SCDAAdvertisementContextRecord: contextVersion=%ld vtEndTime=%f advRecordType=%ld advPayload=0x%@ deviceID=%@"
- "_TtC26SiriCrossDeviceArbitration28EntityKitAttentionController"
- "_attentionClient"
- "_deviceIDFromBytes:"
- "_myriadAttentionQueue"
- "_supportsConfigurableBoost"
- "_updateBiasValueWithDefault:"
- "com.apple.siri.SCDACoordinator"
- "d24@0:8^{MyriadMetricsDataV1=CQCQCddCCCCCCdCCC[50C][50C][50C]C}16"
- "getPlatformBiasValue:"
- "initWithAdvertisementRecordType:voiceTriggerEndTime:advertisementPayload:deviceID:"
- "initWithDeviceID:data:"
- "isMetadataValid"
- "myriadAdvertisementContext"
- "pollForAttentionWithTimeout:event:error:"
- "pushMyriadAdvertisementContext:completionHandler:"
- "resumeWithError:"
- "setConfiguration:"
- "setEventMask:"
- "setIdentifier:"
- "softlink:r:path:/System/Library/Frameworks/Accessibility.framework/Accessibility"
- "softlink:r:path:/System/Library/PrivateFrameworks/AttentionAwareness.framework/AttentionAwareness"
- "suspendWithError:"
- "v24@?0@\"NSNumber\"8@\"NSError\"16"
- "v48@0:8^{MyriadMetricsDataV1=CQCQCddCCCCCCdCCC[50C][50C][50C]C}16@24@32@?40"
- "{MyriadMetricsDataV1=\"version\"C\"sessionId\"Q\"eventType\"C\"requestType\"Q\"state\"C\"advDelay\"d\"advInterval\"d\"coordinationAllowed\"C\"winnerGoodnessScore\"C\"winnerProductType\"C\"winnerDeviceClass\"C\"homepodInvolved\"C\"previousDecision\"C\"previousDecisionTime\"d\"deviceGroup\"C\"decision\"C\"lateToElection\"C\"electionParticipantGoodnessScore\"[50C]\"electionParticipantDeviceType\"[50C]\"electionParticipantProductType\"[50C]\"electionParticipantCount\"C}"
- "{MyriadMetricsDataV1=CQCQCddCCCCCCdCCC[50C][50C][50C]C}16@0:8"

```
