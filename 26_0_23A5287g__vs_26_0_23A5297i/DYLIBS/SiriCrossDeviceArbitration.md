## SiriCrossDeviceArbitration

> `/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration`

```diff

-3500.55.1.0.0
-  __TEXT.__text: 0x2fc5c
+3500.59.1.0.0
+  __TEXT.__text: 0x2f9ac
   __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_methlist: 0x2f24
+  __TEXT.__objc_methlist: 0x3134
   __TEXT.__dlopen_cstrs: 0x118
   __TEXT.__const: 0x1e0
-  __TEXT.__gcc_except_tab: 0x4a4
-  __TEXT.__oslogstring: 0x52e8
-  __TEXT.__cstring: 0x59e1
-  __TEXT.__unwind_info: 0xcc8
-  __TEXT.__objc_classname: 0x5f5
-  __TEXT.__objc_methname: 0x7bd5
-  __TEXT.__objc_methtype: 0x1895
-  __TEXT.__objc_stubs: 0x5aa0
-  __DATA_CONST.__got: 0x2f8
-  __DATA_CONST.__const: 0x10d8
-  __DATA_CONST.__objc_classlist: 0x150
+  __TEXT.__gcc_except_tab: 0x4e0
+  __TEXT.__oslogstring: 0x5080
+  __TEXT.__cstring: 0x5952
+  __TEXT.__unwind_info: 0xd08
+  __TEXT.__objc_classname: 0x61d
+  __TEXT.__objc_methname: 0x8011
+  __TEXT.__objc_methtype: 0x1907
+  __TEXT.__objc_stubs: 0x5ec0
+  __DATA_CONST.__got: 0x300
+  __DATA_CONST.__const: 0x1108
+  __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d08
+  __DATA_CONST.__objc_selrefs: 0x1e68
   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0xa8
   __AUTH_CONST.__auth_got: 0x428
-  __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x2720
-  __AUTH_CONST.__objc_const: 0x5378
+  __AUTH_CONST.__const: 0x340
+  __AUTH_CONST.__cfstring: 0x2900
+  __AUTH_CONST.__objc_const: 0x5478
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x4ec
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x4f4
   __DATA.__data: 0x5d0
-  __DATA.__bss: 0x180
+  __DATA.__bss: 0x1a0
   __DATA_DIRTY.__objc_data: 0xbe0
   __DATA_DIRTY.__bss: 0x8
   __DATA_DIRTY.__common: 0x10

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 024C33B3-E010-3581-982B-97A180B0D5F7
-  Functions: 1158
-  Symbols:   4117
-  CStrings:  2889
+  UUID: 71600471-CFED-38D4-8C16-A5D58E39C2A1
+  Functions: 1200
+  Symbols:   4245
+  CStrings:  2958
 
Symbols:
+ +[SCDADevice(Internal) debugStringForSCDADeviceClass:andProductType:]
+ +[SCDAUtilities isIPad]
+ +[SCDAUtilities isVirtualDevice]
+ +[SCDAVoiceTriggerCalculation _adjustRecord:withBoostAdjust:constantGoodness:oldRecord:evaluator:device:]
+ +[SCDAVoiceTriggerCalculation _changeNewRecord:tiebreakerIfIdenticalToOldRecord:]
+ +[SCDAVoiceTriggerCalculation calculateRepeatVoiceTrigger:withOldRecord:device:adjustment:constantGoodness:evaluator:andContext:]
+ -[SCDACoordinator _forceLocalWinner:withRecord:]
+ -[SCDACoordinator _shouldCreateMyriadSessionInCurrentState]
+ -[SCDACoordinator alertFiringRecord]
+ -[SCDACoordinator carplayRecord]
+ -[SCDACoordinator inEarRecord]
+ -[SCDACoordinator inTaskRecord]
+ -[SCDACoordinator outgoingRecord]
+ -[SCDACoordinator overrideRecord]
+ -[SCDACoordinator thresholdTriggerRecordLoudnessMissing:]
+ -[SCDADevice designatedSelfID]
+ -[SCDADevice deviceGroup]
+ -[SCDADevice initWithSelfID:]
+ -[SCDADevice(Internal) overrideDeviceGroup:]
+ -[SCDARecord _assignDeviceDetails:]
+ -[SCDARecord _generateConfidenceWithinLowerBound:andUpperBound:]
+ -[SCDARecord _initWithPerceptualAudioHash:type:device:]
+ -[SCDARecord _initWithRecordType:device:]
+ -[SCDARecord _initWithVoiceTriggerTime:]
+ -[SCDARecord adjustByAdding:]
+ -[SCDARecord generateCarPlayConfidence]
+ -[SCDARecord generateSiriSpeakingConfidence]
+ -[SCDARecord generateUIShowingConfidence]
+ -[SCDARecord generateVisionProConfidence]
+ -[SCDARecord initWithAlertFiringTrigger:device:]
+ -[SCDARecord initWithCarPlayTrigger:device:]
+ -[SCDARecord initWithContinuation:]
+ -[SCDARecord initWithDirectTrigger:device:]
+ -[SCDARecord initWithEmergency:]
+ -[SCDARecord initWithEmergencyHandled:]
+ -[SCDARecord initWithEmpty:]
+ -[SCDARecord initWithInEarTrigger:device:]
+ -[SCDARecord initWithInTaskTrigger:device:]
+ -[SCDARecord initWithLateSuppression:device:]
+ -[SCDARecord initWithOutgoing:device:]
+ -[SCDARecord initWithOverrideTrigger:device:]
+ -[SCDARecord initWithPHS:]
+ -[SCDARecord initWithRTS:]
+ -[SCDARecord initWithResponse:device:]
+ -[SCDARecord initWithSlowdown:device:]
+ -[SCDARecord initWithThreshold:isLoudnessMissing:device:]
+ -[SCDARecord initWithVoiceTrigger:device:]
+ -[SCDARecord isValid]
+ -[SCDARecord recordType]
+ -[SCDARecord setRecordType:]
+ GCC_except_table1021
+ GCC_except_table1041
+ GCC_except_table1103
+ GCC_except_table478
+ GCC_except_table531
+ GCC_except_table532
+ GCC_except_table538
+ GCC_except_table636
+ GCC_except_table741
+ GCC_except_table744
+ GCC_except_table851
+ GCC_except_table866
+ GCC_except_table923
+ GCC_except_table927
+ GCC_except_table954
+ GCC_except_table998
+ _OBJC_CLASS_$_SCDAVoiceTriggerCalculation
+ _OBJC_IVAR_$_SCDADevice._designatedSelfID
+ _OBJC_IVAR_$_SCDADevice._deviceGroup
+ _OBJC_IVAR_$_SCDARecord._recordType
+ _OBJC_METACLASS_$_SCDAVoiceTriggerCalculation
+ __OBJC_$_CLASS_METHODS_SCDADevice(Internal)
+ __OBJC_$_CLASS_METHODS_SCDAVoiceTriggerCalculation
+ __OBJC_$_INSTANCE_METHODS_SCDADevice(Internal)
+ __OBJC_CLASS_RO_$_SCDAVoiceTriggerCalculation
+ __OBJC_METACLASS_RO_$_SCDAVoiceTriggerCalculation
+ ___23+[SCDAUtilities isIPad]_block_invoke
+ ___31-[SCDACoordinator _enterState:]_block_invoke.234
+ ___32+[SCDAUtilities isVirtualDevice]_block_invoke
+ ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.328
+ ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.329
+ ___42-[SCDACoordinator _waitWiProx:andExecute:]_block_invoke.358
+ ___48-[SCDACoordinator _forceLocalWinner:withRecord:]_block_invoke
+ ___51-[SCDACoordinator _endAdvertisingAnalyticsContext:]_block_invoke.190
+ ___52-[SCDACoordinator _createWaitWiProxTimer:waitBlock:]_block_invoke.357
+ ___89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.336
+ ___89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.345
+ ___Block_byref_object_copy_.1114
+ ___Block_byref_object_copy_.1684
+ ___Block_byref_object_copy_.2351
+ ___Block_byref_object_dispose_.1115
+ ___Block_byref_object_dispose_.1685
+ ___Block_byref_object_dispose_.2352
+ ___block_literal_global.1068
+ ___block_literal_global.1129
+ ___block_literal_global.1162
+ ___block_literal_global.1187
+ ___block_literal_global.1238
+ ___block_literal_global.15
+ ___block_literal_global.1554
+ ___block_literal_global.1762
+ ___block_literal_global.20
+ ___block_literal_global.22
+ ___block_literal_global.223
+ ___block_literal_global.225
+ ___block_literal_global.2341
+ ___block_literal_global.2702
+ ___block_literal_global.352
+ ___block_literal_global.356
+ ___block_literal_global.42
+ ___block_literal_global.772
+ _isIPad.isIPad
+ _isIPad.onceToken
+ _isVirtualDevice.isVM
+ _isVirtualDevice.onceToken
+ _objc_msgSend$_adjustRecord:withBoostAdjust:constantGoodness:oldRecord:evaluator:device:
+ _objc_msgSend$_assignDeviceDetails:
+ _objc_msgSend$_changeNewRecord:tiebreakerIfIdenticalToOldRecord:
+ _objc_msgSend$_forceLocalWinner:withRecord:
+ _objc_msgSend$_generateConfidenceWithinLowerBound:andUpperBound:
+ _objc_msgSend$_initWithPerceptualAudioHash:type:device:
+ _objc_msgSend$_initWithRecordType:device:
+ _objc_msgSend$_initWithVoiceTriggerTime:
+ _objc_msgSend$_shouldCreateMyriadSessionInCurrentState
+ _objc_msgSend$adjustByAdding:
+ _objc_msgSend$alertFiringRecord
+ _objc_msgSend$calculateRepeatVoiceTrigger:withOldRecord:device:adjustment:constantGoodness:evaluator:andContext:
+ _objc_msgSend$carplayRecord
+ _objc_msgSend$debugStringForSCDADeviceClass:andProductType:
+ _objc_msgSend$designatedSelfID
+ _objc_msgSend$generateCarPlayConfidence
+ _objc_msgSend$generateUIShowingConfidence
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$inEarRecord
+ _objc_msgSend$inTaskRecord
+ _objc_msgSend$initWithAlertFiringTrigger:device:
+ _objc_msgSend$initWithCarPlayTrigger:device:
+ _objc_msgSend$initWithContinuation:
+ _objc_msgSend$initWithDirectTrigger:device:
+ _objc_msgSend$initWithEmergency:
+ _objc_msgSend$initWithEmergencyHandled:
+ _objc_msgSend$initWithEmpty:
+ _objc_msgSend$initWithInEarTrigger:device:
+ _objc_msgSend$initWithInTaskTrigger:device:
+ _objc_msgSend$initWithLateSuppression:device:
+ _objc_msgSend$initWithOutgoing:device:
+ _objc_msgSend$initWithOverrideTrigger:device:
+ _objc_msgSend$initWithPHS:
+ _objc_msgSend$initWithRTS:
+ _objc_msgSend$initWithResponse:device:
+ _objc_msgSend$initWithSelfID:
+ _objc_msgSend$initWithSlowdown:device:
+ _objc_msgSend$initWithThreshold:isLoudnessMissing:device:
+ _objc_msgSend$initWithVoiceTrigger:device:
+ _objc_msgSend$isValid
+ _objc_msgSend$outgoingRecord
+ _objc_msgSend$overrideDeviceGroup:
+ _objc_msgSend$overrideRecord
+ _objc_msgSend$recordType
+ _objc_msgSend$setRecordType:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$thresholdTriggerRecordLoudnessMissing:
- -[SCDACoordinator _forceLocalWinner:]
- -[SCDACoordinator _pushMyriadAdvertisementContextToContextCollectorWithAdvertisementInterval:advertisementDelay:]
- -[SCDACoordinator _suppressDeviceIfNeededWithVoiceTriggerEndTime:adverisementDispatchTime:]
- -[SCDADevice init]
- -[SCDARecord _generateConfidenceWithinLowerBounds:andUpperBounds:]
- -[SCDARecord generateRandomInTaskConfidence]
- -[SCDARecord initWithPerceptualAudioHash:]
- GCC_except_table1003
- GCC_except_table1065
- GCC_except_table450
- GCC_except_table499
- GCC_except_table500
- GCC_except_table506
- GCC_except_table601
- GCC_except_table709
- GCC_except_table816
- GCC_except_table831
- GCC_except_table881
- GCC_except_table885
- GCC_except_table912
- GCC_except_table961
- GCC_except_table983
- _OBJC_IVAR_$_SCDACoordinator._clientIsDirectActivating
- __OBJC_$_CLASS_METHODS_SCDADevice
- __OBJC_$_INSTANCE_METHODS_SCDADevice
- ___113-[SCDACoordinator _pushMyriadAdvertisementContextToContextCollectorWithAdvertisementInterval:advertisementDelay:]_block_invoke
- ___113-[SCDACoordinator _pushMyriadAdvertisementContextToContextCollectorWithAdvertisementInterval:advertisementDelay:]_block_invoke_2
- ___31-[SCDACoordinator _enterState:]_block_invoke.227
- ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.322
- ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.326
- ___37-[SCDACoordinator _forceLocalWinner:]_block_invoke
- ___42-[SCDACoordinator _waitWiProx:andExecute:]_block_invoke.355
- ___51-[SCDACoordinator _endAdvertisingAnalyticsContext:]_block_invoke.189
- ___52-[SCDACoordinator _createWaitWiProxTimer:waitBlock:]_block_invoke.354
- ___89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.333
- ___89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.342
- ___91-[SCDACoordinator _suppressDeviceIfNeededWithVoiceTriggerEndTime:adverisementDispatchTime:]_block_invoke
- ___Block_byref_object_copy_.1088
- ___Block_byref_object_copy_.1620
- ___Block_byref_object_copy_.2280
- ___Block_byref_object_dispose_.1089
- ___Block_byref_object_dispose_.1621
- ___Block_byref_object_dispose_.2281
- ___block_descriptor_72_e8_32s40s48s_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s_e27_v32?08"SCDARecord"16^B24ls32l8
- ___block_descriptor_88_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.1042
- ___block_literal_global.1103
- ___block_literal_global.1137
- ___block_literal_global.1161
- ___block_literal_global.1205
- ___block_literal_global.1498
- ___block_literal_global.1698
- ___block_literal_global.18
- ___block_literal_global.216
- ___block_literal_global.218
- ___block_literal_global.2275
- ___block_literal_global.2584
- ___block_literal_global.33
- ___block_literal_global.346
- ___block_literal_global.353
- ___block_literal_global.744
- _objc_msgSend$_contextFetchDelayForAdvertimentInterval:advertisementDelay:
- _objc_msgSend$_forceLocalWinner:
- _objc_msgSend$_generateConfidenceWithinLowerBounds:andUpperBounds:
- _objc_msgSend$_pushMyriadAdvertisementContextToContextCollectorWithAdvertisementInterval:advertisementDelay:
- _objc_msgSend$_suppressDeviceIfNeededWithVoiceTriggerEndTime:adverisementDispatchTime:
- _objc_msgSend$_testAndFilterAdvertisementsFromContextCollector:voiceTriggerEndTime:advertisementDispatchTime:advertisement:
- _objc_msgSend$adjustByMultiplier:adding:
- _objc_msgSend$generateRandomInTaskConfidence
- _objc_msgSend$init
- _objc_msgSend$initWithAdvertisementRecordType:voiceTriggerEndTime:advertisementPayload:deviceID:electionParticipantId:
- _objc_msgSend$initWithPerceptualAudioHash:
- _objc_msgSend$myriadAdvertisementContextAsData
- _objc_msgSend$setAdvertisementDispatchTime:
- _objc_msgSend$timeIntervalSinceReferenceDate
CStrings:
+ "#scda BTLE CarPlay trigger signal received"
+ "#scda BTLE audio data signal received (CVT)"
+ "#scda BTLE emergency signal received"
+ "#scda BTLE in ear trigger signal received"
+ "#scda BTLE myriad decision fetch signal received"
+ "%02d (%@)"
+ "%s #scda BTLE device class: %@ (%@) detected, deviceAdjust: %d incomingAdjustment %d, original rawAudioGoodnessScore: %d"
+ "%s #scda Voice trigger with lower goodness (%du) arrived, but ignoring old record: %@ in favor of new: %@"
+ "%s #scda Voice trigger, activation with no previous record, proceeding to calculate adjustments"
+ "%s #scda adjustByMultipler deprecated: Multiplier value of %f will be droped!"
+ "%s #scda not initializing myriad session, myriad is in state %@ (_myriadSession is %@)"
+ "%s #scda overriding device group: %du"
+ "%s #scda removed the context collector push that was not working since SCDA extraction"
+ "%s BTLE Incrementing record count for %@ to %@"
+ "%s BTLE Updating record table with a newer advertisement ( %@ -> %@ )"
+ "%s BTLE deviceShouldContinue:%ld coordinationDisabled:%ld, isDirectlyActivating:%ld, isInEarTrigger:%ld, suppressLateTrigger:removed setupRecordSuppression:%ld."
+ "+[SCDAVoiceTriggerCalculation _adjustRecord:withBoostAdjust:constantGoodness:oldRecord:evaluator:device:]"
+ "+[SCDAVoiceTriggerCalculation _changeNewRecord:tiebreakerIfIdenticalToOldRecord:]"
+ "+[SCDAVoiceTriggerCalculation calculateRepeatVoiceTrigger:withOldRecord:device:adjustment:constantGoodness:evaluator:andContext:]"
+ "-Invalidated"
+ "-[SCDACoordinator _forceLocalWinner:withRecord:]_block_invoke"
+ "-[SCDARecord adjustByAdding:]"
+ "@20@0:8B16"
+ "@24@0:8C16C20"
+ "@28@0:8S16@20"
+ "@36@0:8@16B24@28"
+ "@40@0:8@16q24@32"
+ "@56@0:8@16i24i28@32@40@48"
+ "@64@0:8@16@24@32i40i44@48@56"
+ "Apple TV"
+ "HomePod"
+ "Internal"
+ "Mac Bridge"
+ "Mac Obsolete"
+ "Mac Regular"
+ "MrC93gcyPVLHmEbzUu9uzQ"
+ "Reality Device"
+ "SCDAVoiceTriggerCalculation"
+ "T@\"NSData\",&,N,V_data"
+ "T@\"NSUUID\",R,N,V_designatedSelfID"
+ "Third Party"
+ "Tq,N,V_recordType"
+ "Watch"
+ "Watch Audio"
+ "_adjustRecord:withBoostAdjust:constantGoodness:oldRecord:evaluator:device:"
+ "_assignDeviceDetails:"
+ "_changeNewRecord:tiebreakerIfIdenticalToOldRecord:"
+ "_forceLocalWinner:withRecord:"
+ "_generateConfidenceWithinLowerBound:andUpperBound:"
+ "_initWithPerceptualAudioHash:type:device:"
+ "_initWithRecordType:device:"
+ "_initWithVoiceTriggerTime:"
+ "_shouldCreateMyriadSessionInCurrentState"
+ "adjustByAdding:"
+ "alertFiringRecord"
+ "calculateRepeatVoiceTrigger:withOldRecord:device:adjustment:constantGoodness:evaluator:andContext:"
+ "carplayRecord"
+ "cc=%d epId=%@ MyriadRecord: hash=%#06X,good=%03d,conf=%d,dc=%@,pt=%d,tb=%d,isMe=%@,g=%d"
+ "debugStringForSCDADeviceClass:andProductType:"
+ "designatedSelfID"
+ "generateCarPlayConfidence"
+ "generateSiriSpeakingConfidence"
+ "generateUIShowingConfidence"
+ "generateVisionProConfidence"
+ "hasSuffix:"
+ "iPad"
+ "iPhone"
+ "inEarRecord"
+ "inTaskRecord"
+ "initWithAlertFiringTrigger:device:"
+ "initWithCarPlayTrigger:device:"
+ "initWithContinuation:"
+ "initWithDirectTrigger:device:"
+ "initWithEmergency:"
+ "initWithEmergencyHandled:"
+ "initWithEmpty:"
+ "initWithInEarTrigger:device:"
+ "initWithInTaskTrigger:device:"
+ "initWithLateSuppression:device:"
+ "initWithOutgoing:device:"
+ "initWithOverrideTrigger:device:"
+ "initWithPHS:"
+ "initWithRTS:"
+ "initWithResponse:device:"
+ "initWithSelfID:"
+ "initWithSlowdown:device:"
+ "initWithThreshold:isLoudnessMissing:device:"
+ "initWithVoiceTrigger:device:"
+ "isIPad"
+ "isValid"
+ "isVirtualDevice"
+ "nil"
+ "not nil"
+ "outgoingRecord"
+ "overrideDeviceGroup:"
+ "overrideRecord"
+ "recordType"
+ "setRecordType:"
+ "stringByAppendingString:"
+ "thresholdTriggerRecordLoudnessMissing:"
- "%@-Invalidated"
- "%s #scda BTLE CarPlay trigger signal received"
- "%s #scda BTLE address initialized to %@ lastChange:%@"
- "%s #scda BTLE audio data signal received"
- "%s #scda BTLE device class: %@ (%@) detected, adjusting goodness by %d incomingAdjustment %d, rawAudioGoodnessScore: %d"
- "%s #scda BTLE emergency signal received"
- "%s #scda BTLE in ear trigger signal received"
- "%s #scda BTLE myriad decision fetch signal received"
- "%s #scda BTLE self trigger signal received"
- "%s #scda Error: %@"
- "%s #scda Not pushing myriad advertisement context - HAL enabled: %d, direct activation: %d"
- "%s #scda Not pushing myriad advertisement context - Valid voicetrigger endtime: %d (curr time: %llu, time since device boot: %llu)"
- "%s #scda Pushing Myriad advertisement context is complete"
- "%s #scda Suppressing the current device due to late trigger (voicetrigger endtime: %f, advertisement dispatch time: %f, advertisement delay: %f, myriad record count: %ld)"
- "%s #scda Voice Trigger stored record replaced (%{public}@) with record: %{public}@"
- "%s #scda Voice trigger with active record (%@), replaced with record: %@"
- "%s #scda Voice trigger with lower goodness (%du) arrived, replacing with goodness from: %@"
- "%s #scda _shouldUseContextCollector is false"
- "%s #scda adv dispatch time: %f, voice trigger end time: %f, time since voice trigger: %f (curr time: %llu, time since device boot: %llu), advertisement: %@"
- "%s #scda current advId: %@ is different from the advId for which the myriad context was dispatched: %@"
- "%s #scda not initializing myriad session, myriad is in state %@"
- "%s BTLE deviceShouldContinue:%ld coordinationDisabled:%ld, isDirectlyActivating:%ld, isInEarTrigger:%ld, suppressLateTrigger:%ld setupRecordSuppression:%ld."
- "%s BTLE heard advert from: %@ data= %@"
- "-[SCDACoordinator _forceLocalWinner:]_block_invoke"
- "-[SCDACoordinator _pushMyriadAdvertisementContextToContextCollectorWithAdvertisementInterval:advertisementDelay:]"
- "-[SCDACoordinator _pushMyriadAdvertisementContextToContextCollectorWithAdvertisementInterval:advertisementDelay:]_block_invoke"
- "-[SCDACoordinator _pushMyriadAdvertisementContextToContextCollectorWithAdvertisementInterval:advertisementDelay:]_block_invoke_2"
- "-[SCDACoordinator _suppressDeviceIfNeededWithVoiceTriggerEndTime:adverisementDispatchTime:]_block_invoke"
- "T@\"NSData\",C,N,V_data"
- "_clientIsDirectActivating"
- "_forceLocalWinner:"
- "_generateConfidenceWithinLowerBounds:andUpperBounds:"
- "_pushMyriadAdvertisementContextToContextCollectorWithAdvertisementInterval:advertisementDelay:"
- "_suppressDeviceIfNeededWithVoiceTriggerEndTime:adverisementDispatchTime:"
- "carplayTriggerSeenCallback"
- "cc=%d epId=%@ MyriadRecord: hash=%#06X,good=%d,conf=%d,dc=%d,pt=%d,tb=%d,isMe=%@,g=%d"
- "emergencyCallback"
- "generateRandomInTaskConfidence"
- "inEarTriggerSeenCallback"
- "initWithPerceptualAudioHash:"
- "myriadDecisionRequestCallback"
- "notificationCallback"
- "outputTriggerSeenCallback"
- "timeIntervalSinceReferenceDate"
- "v24@?0@\"NSDictionary\"8@\"NSError\"16"
- "v32@0:8d16d24"

```
