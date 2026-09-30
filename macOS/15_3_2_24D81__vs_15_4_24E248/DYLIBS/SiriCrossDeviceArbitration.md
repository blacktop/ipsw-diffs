## SiriCrossDeviceArbitration

> `/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/Versions/A/SiriCrossDeviceArbitration`

```diff

-3402.17.1.0.0
-  __TEXT.__text: 0x315e4
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0x2ae4
-  __TEXT.__const: 0x188
-  __TEXT.__gcc_except_tab: 0x418
-  __TEXT.__oslogstring: 0x47e7
-  __TEXT.__cstring: 0x5820
+3404.36.2.0.0
+  __TEXT.__text: 0x331d4
+  __TEXT.__auth_stubs: 0x660
+  __TEXT.__objc_methlist: 0x2fbc
   __TEXT.__dlopen_cstrs: 0xc2
-  __TEXT.__unwind_info: 0xca8
-  __TEXT.__objc_classname: 0x68d
-  __TEXT.__objc_methname: 0x7980
-  __TEXT.__objc_methtype: 0x18e0
-  __TEXT.__objc_stubs: 0x58c0
-  __DATA_CONST.__got: 0x308
-  __DATA_CONST.__const: 0x618
-  __DATA_CONST.__objc_classlist: 0x160
+  __TEXT.__const: 0x1f0
+  __TEXT.__gcc_except_tab: 0x420
+  __TEXT.__oslogstring: 0x5285
+  __TEXT.__cstring: 0x5967
+  __TEXT.__unwind_info: 0xcb8
+  __TEXT.__objc_classname: 0x696
+  __TEXT.__objc_methname: 0x7b57
+  __TEXT.__objc_methtype: 0x1912
+  __TEXT.__objc_stubs: 0x5a40
+  __DATA_CONST.__got: 0x310
+  __DATA_CONST.__const: 0x638
+  __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bf8
-  __DATA_CONST.__objc_superrefs: 0x148
+  __DATA_CONST.__objc_selrefs: 0x1ce0
+  __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x148
-  __AUTH_CONST.__auth_got: 0x338
+  __AUTH_CONST.__auth_got: 0x340
   __AUTH_CONST.__const: 0xf80
-  __AUTH_CONST.__cfstring: 0x2640
-  __AUTH_CONST.__objc_const: 0x5dc0
+  __AUTH_CONST.__cfstring: 0x2680
+  __AUTH_CONST.__objc_const: 0x57d0
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH.__objc_data: 0xdc0
-  __DATA.__objc_ivar: 0x53c
+  __AUTH.__objc_data: 0xe10
+  __DATA.__objc_ivar: 0x534
   __DATA.__data: 0x6a8
-  __DATA.__bss: 0x168
+  __DATA.__bss: 0x178
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: BB396FCF-61A8-395A-807F-E1B7A0411266
-  Functions: 1189
-  Symbols:   3049
-  CStrings:  2821
+  UUID: 6234DEFE-B67D-3710-BD1E-1FE40F7BE8A0
+  Functions: 1201
+  Symbols:   3083
+  CStrings:  2897
 
Symbols:
+ +[SCDADevice cdaDeviceClassForSCDADeviceClass:andProducType:]
+ -[SCDAAdvertisementContextRecord _advertisementPayloadSizeForVersion:]
+ -[SCDAAdvertisementContextRecord _getAdvertisementRecordTypeForVersion:data:]
+ -[SCDACoordinator _startAdvertisingFromSetupMode]
+ -[SCDADevice .cxx_destruct]
+ -[SCDADevice _getDeviceAdjust_DEPRECATED]
+ -[SCDADevice _getDeviceClass]
+ -[SCDADevice _getInEarDelay]
+ -[SCDADevice _getInEarInterval]
+ -[SCDADevice _getProductType]
+ -[SCDADevice _getTrumpDelay]
+ -[SCDADevice cdaDeviceClass]
+ -[SCDADevice description]
+ -[SCDADevice deviceAdjust_DEPRECATED]
+ -[SCDADevice deviceClassName]
+ -[SCDADevice deviceClass]
+ -[SCDADevice inEarDelay]
+ -[SCDADevice inEarInterval]
+ -[SCDADevice initWithDeviceClass:deviceClassName:productType:productTypeName:]
+ -[SCDADevice init]
+ -[SCDADevice overrideLocalConfiguration:deviceAdjust:trumpDelay:]
+ -[SCDADevice productTypeName]
+ -[SCDADevice productType]
+ -[SCDADevice trumpDelay]
+ -[SCDAMetrics _createEndAnalyticContextFromIntermediateContext:forVersion:sessionId:]
+ -[SCDARecord hasEqualAdvertisementData:]
+ -[SCDARecord isALateSuppressionTrumpFor:]
+ GCC_except_table1039
+ GCC_except_table1108
+ GCC_except_table621
+ GCC_except_table731
+ GCC_except_table847
+ GCC_except_table862
+ GCC_except_table916
+ GCC_except_table947
+ GCC_except_table999
+ OBJC_IVAR_$_SCDACoordinator._device
+ OBJC_IVAR_$_SCDADevice._deviceAdjust_DEPRECATED
+ OBJC_IVAR_$_SCDADevice._deviceClass
+ OBJC_IVAR_$_SCDADevice._deviceClassName
+ OBJC_IVAR_$_SCDADevice._inEarDelay
+ OBJC_IVAR_$_SCDADevice._inEarInterval
+ OBJC_IVAR_$_SCDADevice._productType
+ OBJC_IVAR_$_SCDADevice._productTypeName
+ OBJC_IVAR_$_SCDADevice._trumpDelay
+ SCDALogForCategory.categories
+ _MGGetProductType
+ _OBJC_CLASS_$_SCDADevice
+ _OBJC_METACLASS_$_SCDADevice
+ __31-[SCDACoordinator _enterState:]_block_invoke.243
+ __36-[SCDACoordinator _advertiseTrigger]_block_invoke.345
+ __36-[SCDACoordinator _advertiseTrigger]_block_invoke.350
+ __36-[SCDACoordinator _advertiseTrigger]_block_invoke.351
+ __42-[SCDACoordinator _waitWiProx:andExecute:]_block_invoke.390
+ __51-[SCDACoordinator _endAdvertisingAnalyticsContext:]_block_invoke.199
+ __52-[SCDACoordinator _createWaitWiProxTimer:waitBlock:]_block_invoke.388
+ __89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.360
+ __89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.371
+ __Block_byref_object_copy_.1098
+ __Block_byref_object_copy_.1670
+ __Block_byref_object_copy_.2393
+ __Block_byref_object_dispose_.1099
+ __Block_byref_object_dispose_.1671
+ __Block_byref_object_dispose_.2394
+ __OBJC_$_CLASS_METHODS_SCDADevice
+ __OBJC_$_INSTANCE_METHODS_SCDADevice
+ __OBJC_$_INSTANCE_VARIABLES_SCDADevice
+ __OBJC_$_PROP_LIST_SCDADevice
+ __OBJC_CLASS_RO_$_SCDADevice
+ __OBJC_METACLASS_RO_$_SCDADevice
+ ___block_descriptor_56_e8_32s40s48r_e27_v32?0"SCDARecord"8Q16^B24l
+ ___block_descriptor_65_e8_32r40r48r56r_e27_v32?0"SCDARecord"8Q16^B24l
+ ___copy_helper_block_e8_32r40r48r56r
+ ___copy_helper_block_e8_32s40s48r
+ ___destroy_helper_block_e8_32r40r48r56r
+ ___destroy_helper_block_e8_32s40s48r
+ __block_literal_global.1050
+ __block_literal_global.1134
+ __block_literal_global.12
+ __block_literal_global.1209
+ __block_literal_global.1236
+ __block_literal_global.1269
+ __block_literal_global.1544
+ __block_literal_global.17
+ __block_literal_global.1748
+ __block_literal_global.231
+ __block_literal_global.233
+ __block_literal_global.2382
+ __block_literal_global.2665
+ __block_literal_global.2788
+ __block_literal_global.32
+ __block_literal_global.376
+ __block_literal_global.379
+ __block_literal_global.387
+ __block_literal_global.6
+ __block_literal_global.7
+ __block_literal_global.764
+ _objc_msgSend$_advertisementPayloadSizeForVersion:
+ _objc_msgSend$_createEndAnalyticContextFromIntermediateContext:forVersion:sessionId:
+ _objc_msgSend$_getAdvertisementRecordTypeForVersion:data:
+ _objc_msgSend$_getDeviceAdjust_DEPRECATED
+ _objc_msgSend$_getDeviceClass
+ _objc_msgSend$_getInEarDelay
+ _objc_msgSend$_getInEarInterval
+ _objc_msgSend$_getProductType
+ _objc_msgSend$_getTrumpDelay
+ _objc_msgSend$_startAdvertisingFromSetupMode
+ _objc_msgSend$cdaDeviceClass
+ _objc_msgSend$cdaDeviceClassForSCDADeviceClass:andProducType:
+ _objc_msgSend$deviceAdjust_DEPRECATED
+ _objc_msgSend$deviceClassName
+ _objc_msgSend$hasEqualAdvertisementData:
+ _objc_msgSend$inEarDelay
+ _objc_msgSend$inEarInterval
+ _objc_msgSend$isALateSuppressionTrumpFor:
+ _objc_msgSend$myriadCoordinator:didReceiveAdvertisement:
+ _objc_msgSend$overrideLocalConfiguration:deviceAdjust:trumpDelay:
+ _objc_msgSend$productTypeName
+ _objc_msgSend$trumpDelay
- -[SCDAAdvertisementContextRecord _advertismentPayloadSizeForVersion:]
- -[SCDAAdvertisementContextRecord _getAdvertismentRecordTypeForVersion:data:]
- -[SCDACoordinator _cdaParticipantForDeviceClass:andProducType:]
- -[SCDACoordinator _isAPhone:]
- -[SCDACoordinator deviceClass]
- -[SCDACoordinator deviceTrumpDelay]
- -[SCDAMetrics _createEndAnalyticContexFromIntermediateContext:forVersion:sessionId:]
- -[SCDARecord hasEqualAdvertismentData:]
- -[SCDARecord isALateSupressionTrumpFor:]
- GCC_except_table1002
- GCC_except_table1045
- GCC_except_table1113
- GCC_except_table622
- GCC_except_table732
- GCC_except_table850
- GCC_except_table865
- GCC_except_table924
- GCC_except_table951
- OBJC_IVAR_$_SCDACoordinator._deviceAdjust_DEPRECATED
- OBJC_IVAR_$_SCDACoordinator._deviceClass
- OBJC_IVAR_$_SCDACoordinator._deviceClassName
- OBJC_IVAR_$_SCDACoordinator._deviceDelay
- OBJC_IVAR_$_SCDACoordinator._deviceInEarDelay
- OBJC_IVAR_$_SCDACoordinator._deviceInEarInterval
- OBJC_IVAR_$_SCDACoordinator._deviceTrumpDelay
- OBJC_IVAR_$_SCDACoordinator._ignoreInTaskTimer
- OBJC_IVAR_$_SCDACoordinator._inTask
- OBJC_IVAR_$_SCDACoordinator._productType
- OBJC_IVAR_$_SCDACoordinator._productTypeName
- _SCDAProductType
- __36-[SCDACoordinator _advertiseTrigger]_block_invoke.348
- __36-[SCDACoordinator _advertiseTrigger]_block_invoke.354
- __36-[SCDACoordinator _advertiseTrigger]_block_invoke.355
- __42-[SCDACoordinator _waitWiProx:andExecute:]_block_invoke.394
- __51-[SCDACoordinator _endAdvertisingAnalyticsContext:]_block_invoke.204
- __52-[SCDACoordinator _createWaitWiProxTimer:waitBlock:]_block_invoke.392
- __89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.364
- __89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.375
- __Block_byref_object_copy_.1094
- __Block_byref_object_copy_.1668
- __Block_byref_object_copy_.2391
- __Block_byref_object_dispose_.1095
- __Block_byref_object_dispose_.1669
- __Block_byref_object_dispose_.2392
- ___25-[SCDACoordinator inTask]_block_invoke
- ___29-[SCDACoordinator setInTask:]_block_invoke
- ___block_descriptor_64_e8_32s40s48s56r_e27_v32?0"SCDARecord"8Q16^B24l
- ___block_descriptor_73_e8_32s40r48r56r64r_e27_v32?0"SCDARecord"8Q16^B24l
- ___copy_helper_block_e8_32s40r48r56r64r
- ___copy_helper_block_e8_32s40s48s56r
- ___destroy_helper_block_e8_32s40r48r56r64r
- ___destroy_helper_block_e8_32s40s48s56r
- __block_literal_global.10
- __block_literal_global.1046
- __block_literal_global.1130
- __block_literal_global.1205
- __block_literal_global.1233
- __block_literal_global.1263
- __block_literal_global.15
- __block_literal_global.1542
- __block_literal_global.1746
- __block_literal_global.20
- __block_literal_global.236
- __block_literal_global.238
- __block_literal_global.2386
- __block_literal_global.2580
- __block_literal_global.2700
- __block_literal_global.35
- __block_literal_global.380
- __block_literal_global.383
- __block_literal_global.391
- __block_literal_global.5
- __block_literal_global.760
- __lastRandomTieBreakerGenerated
- _hammingDistance
- _objc_msgSend$_advertismentPayloadSizeForVersion:
- _objc_msgSend$_cdaParticipantForDeviceClass:andProducType:
- _objc_msgSend$_createEndAnalyticContexFromIntermediateContext:forVersion:sessionId:
- _objc_msgSend$_getAdvertismentRecordTypeForVersion:data:
- _objc_msgSend$_isAPhone:
- _objc_msgSend$deviceDelay
- _objc_msgSend$hasEqualAdvertismentData:
- _objc_msgSend$isALateSupressionTrumpFor:
- _objc_msgSend$myriadCoordinator:didReceiveAdvertisment:
- _objc_msgSend$valueForKey:
CStrings:
+ "%s #scda Voice Trigger Replacing new (empty) record with DT record for in progress request %@ with VT Time %llu"
+ "%s #scda Voice Trigger stored record replaced (%{public}@) with record: %{public}@"
+ "%s #scda Voice trigger after Direct Trigger generated new tiebreaker: %@"
+ "%s #scda Voice trigger in-ear trigger overridden to: %@"
+ "%s #scda Voice trigger with active record (%@), replaced with record: %@"
+ "%s #scda Voice trigger with active record (%@), using new record: %@"
+ "%s #scda Voice trigger with active record (%@), using original with adjusted TB: %@"
+ "%s #scda Voice trigger with lower goodness (%du) arrived, replacing with goodness from: %@"
+ "%s #scda _shouldUseContextCollector is false"
+ "%s #scda adv dispatch time: %f, voice trigger end time: %f, time since voice trigger: %f (curr time: %llu, time since device boot: %llu), advertisement: %@"
+ "%s #scda attention Original confidence was 0"
+ "%s #scda attention Original goodness before attention arrived was zero - likely an invalid Myriad advertisement from this device could make it lose an election"
+ "%s #scda attention boost arrived in wrong state: %{public}@"
+ "%s #scda attention boost arrived with nil _triggerRecord, likely Siri was dismissed already."
+ "%s #scda attention original record: %@"
+ "%s #scda attention originalTB and originalConfidence collision, generating a new random TB"
+ "%s #scda attention reformulated record: %@"
+ "%s #scda clearing trigger record"
+ "%s #scda endTime from a file is too old, secondsSinceTrigger=%f; Siri might respond from multiple devices"
+ "%s #scda force win on this device with context: %{public}@, triggerRecord: %{public}@"
+ "%s #scda leaving existing trump signal intact %d"
+ "%s #scda watch trumping due to score being 0; watch might win election for little reason"
+ "%s %@, vt_endtime threshold %f"
+ "%s BTLE Updating record table with a late suppression ( %hhu -> %hhu), data= %@, for %@"
+ "%s BTLE daemon wiprox state signaling"
+ "%s BTLE setup-mode voice trigger heard"
+ "%s BTLE startFromVoiceTrigger inTask=REMOVED, inSetupMode=%d, context=%@"
+ "%s BTLE startFromVoiceTrigger inTask=REMOVED, inSetupMode=%d, incomingAdjustment=%d,  context=%@, goodnessScoreContext=%@"
+ "%s CRITICAL ERROR: BTLE error: attempting to readvertise %@; Myriad to stop advertising and proceed as if win occurred, multi-response likely"
+ "%s Clearing trigger record"
+ "%s Dropping stale VT: %f"
+ "%s In-task trigger detected while direct activating. We shouldn't demote direct triggers."
+ "%s Myriad _inTask is removed. This method is deprecated and always returns NO."
+ "%s Myriad _inTask is removed. This method is deprecated and does nothing."
+ "%s Skipping advertising requested with nil _triggerRecord %@"
+ "%s Unexpectedly lowering goodness score %du for in ear trigger"
+ "%s canceling advertising with nil trigger record, this likely means Siri UI was already dismissed %{public}@"
+ "-[SCDACoordinator _initDeviceClassAndAdjustments]"
+ "-[SCDACoordinator _startAdvertisingFromSetupMode]"
+ "-[SCDACoordinator directTriggerRecord]"
+ "-[SCDACoordinator inTask]"
+ "-[SCDACoordinator setInTask:]"
+ "-[SCDACoordinator voiceTriggerRecord]"
+ "@\"SCDADevice\""
+ "@40@0:8C16@20C28@32"
+ "Adding advertisement to replies: %{public}@"
+ "Advertise"
+ "Advertising continuation: %{public}@"
+ "Advertising emergency handled record: %{public}@"
+ "Advertising emergency record: %{public}@"
+ "Advertising ~OUTGOING_TRIGGER: %{public}@"
+ "BTLE device class: %@ (%hhu), productType: %@ (%hhu), device adjust: %hhd, trump delay %0.3f"
+ "BTLE end advertising.\nPotential winner = %{public}@\nSummary: %{public}@"
+ "Entry"
+ "Overriden Device"
+ "Overriden Product"
+ "SCDADevice"
+ "Sending suppression(DT) advertisement: %{public}@"
+ "Suppressing late arriver with advertisement: %{public}@"
+ "T@\"NSString\",R,N,V_deviceClassName"
+ "T@\"NSString\",R,N,V_productTypeName"
+ "Tc,R,N,V_deviceAdjust_DEPRECATED"
+ "Td,R,N,V_inEarDelay"
+ "Td,R,N,V_inEarInterval"
+ "Td,R,N,V_trumpDelay"
+ "Ti,R,N"
+ "_advertisementPayloadSizeForVersion:"
+ "_createEndAnalyticContextFromIntermediateContext:forVersion:sessionId:"
+ "_device"
+ "_getAdvertisementRecordTypeForVersion:data:"
+ "_getDeviceAdjust_DEPRECATED"
+ "_getDeviceClass"
+ "_getInEarDelay"
+ "_getInEarInterval"
+ "_getProductType"
+ "_getTrumpDelay"
+ "_inEarDelay"
+ "_inEarInterval"
+ "_startAdvertisingFromSetupMode"
+ "_trumpDelay"
+ "c"
+ "c16@0:8"
+ "cdaDeviceClass"
+ "cdaDeviceClassForSCDADeviceClass:andProducType:"
+ "deviceAdjust_DEPRECATED"
+ "deviceClassName"
+ "faceDetectedBoostWithContext: %{public}@"
+ "hasEqualAdvertisementData:"
+ "inEarDelay"
+ "inEarInterval"
+ "initWithDeviceClass:deviceClassName:productType:productTypeName:"
+ "isALateSuppressionTrumpFor:"
+ "myriadCoordinator:didReceiveAdvertisement:"
+ "overrideLocalConfiguration:deviceAdjust:trumpDelay:"
+ "productTypeName"
+ "reset state machine"
+ "scdaRequestTypeContinuousVoiceTrigger"
+ "startAdvertisingFromAlertFiringVoiceTriggerWithContext: %{public}@"
+ "startAdvertisingFromDirectTriggerWithContext: %{public}@"
+ "startAdvertisingFromInTaskTriggerWithContext: %{public}@"
+ "startAdvertisingFromInTaskVoiceTriggerWithContext: %{public}@"
+ "startAdvertisingFromOutgoingTrigger: %{public}@"
+ "startAdvertisingFromVoiceTrigger: %{public}@"
+ "startAdvertisingFromVoiceTriggerAdjusted: %du"
+ "startAdvertisingFromVoiceTriggerAdjusted: %du context: %{public}@"
+ "startAdvertisingFromVoiceTriggerWithGoodnessScoreContext: %{public}@ context: %{public}@"
+ "trumpDelay"
+ "v32@0:8C16c20d24"
+ "winner_sent_suppression"
- "%s #scda _shouldUseContextCollector is fslse"
- "%s #scda adv dispatch time: %f, voice trigger end time: %f, time since voice trigger: %f (curr time: %llu, time since device boot: %llu), advertisment: %@"
- "%s #scda attention boost arrived in wrong state: %@"
- "%s #scda endTime from a file is too old, secondsSinceTrigger=%f"
- "%s #scda force win on this device with context: %@, triggerRecord: %@"
- "%s #scda reading defaults: BTLE device class: %@ (%@) detected, category %ld, adjusting goodness by %ld, std delay %f, trump delay %f, vt_endtime threshold %f"
- "%s #scda watch trumping due to score being 0"
- "%s BTLE Updating record table with a late supression ( %hhu -> %hhu), data= %@, for %@"
- "%s BTLE daemon wiprox state signalling"
- "%s BTLE editDist: %d > allowed, ignoring this advert "
- "%s BTLE error: attempting to readvertise %@"
- "%s BTLE startFromVoiceTrigger inTask=%d, inSetupMode=%d, context=%@"
- "%s BTLE startFromVoiceTrigger inTask=%d, inSetupMode=%d, incomingAdjustment=%d,  context=%@, goodnessScoreContext=%@"
- "%s inTask=%d"
- "-[SCDACoordinator setInTask:]_block_invoke"
- "B20@0:8C16"
- "BTLE end advertising.\nPotential winner = %@\nSummary: %@"
- "_advertismentPayloadSizeForVersion:"
- "_cdaParticipantForDeviceClass:andProducType:"
- "_createEndAnalyticContexFromIntermediateContext:forVersion:sessionId:"
- "_deviceDelay"
- "_deviceInEarDelay"
- "_deviceInEarInterval"
- "_deviceTrumpDelay"
- "_getAdvertismentRecordTypeForVersion:data:"
- "_ignoreInTaskTimer"
- "_inTask"
- "_isAPhone:"
- "hasEqualAdvertismentData:"
- "isALateSupressionTrumpFor:"
- "macOS"
- "myriadCoordinator:didReceiveAdvertisment:"
- "scdaRequestTypeContiniousVoiceTrigger"
- "valueForKey:"
- "winner_sent_suppresssion"

```
