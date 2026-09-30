## AppPredictionFoundation

> `/System/Library/PrivateFrameworks/AppPredictionFoundation.framework/AppPredictionFoundation`

```diff

-619.1.0.2.0
-  __TEXT.__text: 0x1aba0
-  __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__objc_methlist: 0x198c
-  __TEXT.__const: 0x420
-  __TEXT.__gcc_except_tab: 0x3dc
-  __TEXT.__cstring: 0x20ca
-  __TEXT.__oslogstring: 0x1b82
-  __TEXT.__unwind_info: 0x828
-  __TEXT.__objc_classname: 0x498
-  __TEXT.__objc_methname: 0x481f
-  __TEXT.__objc_methtype: 0x8f4
-  __TEXT.__objc_stubs: 0x3040
-  __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0xb20
-  __DATA_CONST.__objc_classlist: 0x148
+619.5.1.0.0
+  __TEXT.__text: 0x1efc4
+  __TEXT.__auth_stubs: 0x700
+  __TEXT.__objc_methlist: 0x1e94
+  __TEXT.__const: 0x430
+  __TEXT.__gcc_except_tab: 0x494
+  __TEXT.__cstring: 0x239a
+  __TEXT.__oslogstring: 0x1fb9
+  __TEXT.__unwind_info: 0x990
+  __TEXT.__objc_classname: 0x5ad
+  __TEXT.__objc_methname: 0x563d
+  __TEXT.__objc_methtype: 0x9b2
+  __TEXT.__objc_stubs: 0x39a0
+  __DATA_CONST.__got: 0x310
+  __DATA_CONST.__const: 0xcf0
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1158
+  __DATA_CONST.__objc_selrefs: 0x1420
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xb8
-  __AUTH_CONST.__auth_got: 0x370
-  __AUTH_CONST.__const: 0x8e0
-  __AUTH_CONST.__cfstring: 0x2080
-  __AUTH_CONST.__objc_const: 0x71f8
+  __DATA_CONST.__objc_superrefs: 0xe8
+  __AUTH_CONST.__auth_got: 0x390
+  __AUTH_CONST.__const: 0x980
+  __AUTH_CONST.__cfstring: 0x21c0
+  __AUTH_CONST.__objc_const: 0x8998
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x174
+  __AUTH.__objc_data: 0xbe0
+  __DATA.__objc_ivar: 0x1d0
   __DATA.__data: 0x360
-  __DATA.__bss: 0x2e8
+  __DATA.__bss: 0x300
   __DATA_DIRTY.__objc_data: 0x410
-  __DATA_DIRTY.__bss: 0x60
+  __DATA_DIRTY.__bss: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A1ED36D0-BF09-39E9-9934-2529B552BFDC
-  Functions: 847
-  Symbols:   3142
-  CStrings:  1604
+  UUID: E54991F9-0B8A-3E96-88D3-3D6C0BEA3497
+  Functions: 975
+  Symbols:   3627
+  CStrings:  1801
 
Symbols:
+ +[ATXMicroLocationVisitScheduler sharedInstance]
+ +[ATXMicroLocationVisitScheduler sharedInstance].cold.1
+ +[ATXMicroLocationVisitStream atxMicroLocationVisitEventFromBiomeEvent:]
+ +[ATXMicroLocationVisitStream convertNumDevicesVectorFromBMArray:]
+ +[ATXMicroLocationVisitStream convertProbabilityVectorFromBMArray:]
+ +[ATXPaths _getDirectoryCreating:clientIdentifier:]
+ +[ATXPaths appPredictionDirectoryFile:forClientWithIdentifier:]
+ +[ATXPaths appPredictionDirectoryForClientWithIdentifier:]
+ -[ATXCallbackInfo .cxx_destruct]
+ -[ATXCallbackInfo callback]
+ -[ATXCallbackInfo queue]
+ -[ATXCallbackInfo setCallback:]
+ -[ATXCallbackInfo setQueue:]
+ -[ATXGlobalStateForTesting setTemporaryPathForTesting:]
+ -[ATXGlobalStateForTesting temporaryPathForTesting]
+ -[ATXMicroLocationVisitEvent .cxx_destruct]
+ -[ATXMicroLocationVisitEvent domain]
+ -[ATXMicroLocationVisitEvent hash]
+ -[ATXMicroLocationVisitEvent initWithDomain:maxProbabilityMicroLocationIdentifier:maxProbability:probabilityVector:isStable:numDevicesVector:timestamp:]
+ -[ATXMicroLocationVisitEvent init]
+ -[ATXMicroLocationVisitEvent isEqual:]
+ -[ATXMicroLocationVisitEvent isEqualToATXMicroLocationVisitEvent:]
+ -[ATXMicroLocationVisitEvent isStable]
+ -[ATXMicroLocationVisitEvent maxProbabilityMicroLocationIdentifier]
+ -[ATXMicroLocationVisitEvent maxProbability]
+ -[ATXMicroLocationVisitEvent numDevicesVector]
+ -[ATXMicroLocationVisitEvent probabilityVector]
+ -[ATXMicroLocationVisitEvent timestamp]
+ -[ATXMicroLocationVisitNumDevicesPerTechnology .cxx_destruct]
+ -[ATXMicroLocationVisitNumDevicesPerTechnology hash]
+ -[ATXMicroLocationVisitNumDevicesPerTechnology initWithTechnology:numDevices:]
+ -[ATXMicroLocationVisitNumDevicesPerTechnology init]
+ -[ATXMicroLocationVisitNumDevicesPerTechnology isEqual:]
+ -[ATXMicroLocationVisitNumDevicesPerTechnology isEqualToATXMicroLocationVisitNumDevicesPerTechnology:]
+ -[ATXMicroLocationVisitNumDevicesPerTechnology numDevices]
+ -[ATXMicroLocationVisitNumDevicesPerTechnology technology]
+ -[ATXMicroLocationVisitProbabilityPerLocation .cxx_destruct]
+ -[ATXMicroLocationVisitProbabilityPerLocation hash]
+ -[ATXMicroLocationVisitProbabilityPerLocation initWithMicroLocationIdentifier:probability:]
+ -[ATXMicroLocationVisitProbabilityPerLocation init]
+ -[ATXMicroLocationVisitProbabilityPerLocation isEqual:]
+ -[ATXMicroLocationVisitProbabilityPerLocation isEqualToATXMicroLocationVisitProbabilityPerLocation:]
+ -[ATXMicroLocationVisitProbabilityPerLocation microLocationIdentifier]
+ -[ATXMicroLocationVisitProbabilityPerLocation probability]
+ -[ATXMicroLocationVisitScheduler .cxx_destruct]
+ -[ATXMicroLocationVisitScheduler _handleCompletion:]
+ -[ATXMicroLocationVisitScheduler _handleCompletion:].cold.1
+ -[ATXMicroLocationVisitScheduler _handleMicroLocationEvent:]
+ -[ATXMicroLocationVisitScheduler _onStateQueue_cancelSubscription]
+ -[ATXMicroLocationVisitScheduler _onStateQueue_setupSubscription]
+ -[ATXMicroLocationVisitScheduler biomeQueue]
+ -[ATXMicroLocationVisitScheduler callbacks]
+ -[ATXMicroLocationVisitScheduler dealloc]
+ -[ATXMicroLocationVisitScheduler hasActiveSubscribers]
+ -[ATXMicroLocationVisitScheduler init]
+ -[ATXMicroLocationVisitScheduler isSubscribed]
+ -[ATXMicroLocationVisitScheduler microLocationScheduler]
+ -[ATXMicroLocationVisitScheduler microLocationSink]
+ -[ATXMicroLocationVisitScheduler removeAllSubscribers]
+ -[ATXMicroLocationVisitScheduler setBiomeQueue:]
+ -[ATXMicroLocationVisitScheduler setCallbacks:]
+ -[ATXMicroLocationVisitScheduler setMicroLocationScheduler:]
+ -[ATXMicroLocationVisitScheduler setMicroLocationSink:]
+ -[ATXMicroLocationVisitScheduler setStateQueue:]
+ -[ATXMicroLocationVisitScheduler stateQueue]
+ -[ATXMicroLocationVisitScheduler subscribeWithCallback:]
+ -[ATXMicroLocationVisitScheduler subscribeWithCallback:onQueue:]
+ -[ATXMicroLocationVisitScheduler subscribeWithCallback:onQueue:].cold.1
+ -[ATXMicroLocationVisitScheduler unSubscribeWithToken:]
+ -[ATXMicroLocationVisitStream _publisherWithStartDate:endDate:shouldReverse:]
+ -[ATXMicroLocationVisitStream enumerateMicroLocationVisitEventsFromStartDate:endDate:filterBlock:limit:ascending:block:]
+ -[ATXMicroLocationVisitStream mostRecentMicroLocationWithinSeconds:]
+ -[ATXMicroLocationVisitStream mostRecentMicroLocation]
+ -[ATXRelevantShortcutsEvent .cxx_destruct]
+ -[ATXRelevantShortcutsEvent bundleID]
+ -[ATXRelevantShortcutsEvent hash]
+ -[ATXRelevantShortcutsEvent initWithBundleID:relevantShortcut:]
+ -[ATXRelevantShortcutsEvent init]
+ -[ATXRelevantShortcutsEvent isEqual:]
+ -[ATXRelevantShortcutsEvent isEqualToATXRelevantShortcutsEvent:]
+ -[ATXRelevantShortcutsEvent relevantShortcut]
+ -[ATXRelevantShortcutsStream _relevantShortcutsPublisherWithStartDate:endDate:limit:]
+ -[ATXRelevantShortcutsStream atx_efficientRelevantShortcut:]
+ -[ATXRelevantShortcutsStream atx_efficientRelevantShortcut:].cold.1
+ -[ATXRelevantShortcutsStream enumerateEventsFromStartDate:endDate:limit:block:]
+ -[ATXRelevantShortcutsStream enumerateEventsFromStartDate:endDate:limit:block:].cold.1
+ -[ATXSleepEvent .cxx_destruct]
+ -[ATXSleepEvent description]
+ -[ATXSleepEvent duration]
+ -[ATXSleepEvent hash]
+ -[ATXSleepEvent initWithSleepStart:wakeUp:]
+ -[ATXSleepEvent init]
+ -[ATXSleepEvent isEqual:]
+ -[ATXSleepEvent isEqualToATXSleepEvent:]
+ -[ATXSleepEvent sleepStartTime]
+ -[ATXSleepEvent wakeUpTime]
+ -[ATXSleepStream backlightPublisherWithStartDate:endDate:]
+ -[ATXSleepStream enumerateSleepEventsFromStartDate:endDate:limit:block:]
+ -[ATXSleepStream hasAlreadyDetectedSleepEventOnGivenDay:sleepEvents:withCalendar:]
+ -[ATXSleepStream isFirstBacklightOnAfterWakeup:sleepStartTime:existingSleepEventsToday:withCalendar:]
+ -[ATXSleepStream isIdlePeriodLongEnough:]
+ -[ATXSleepStream isTimeInEligibleNotificationWindow:withCalendar:]
+ -[ATXSleepStream screenLockedPublisherWithStartDate:endDate:]
+ GCC_except_table16
+ GCC_except_table18
+ _ATXBGSTDeferAfterSecondsKey
+ _ATXBGSTStatusDeferKey
+ _ATXBGSTStatusDoneKey
+ _ATXBGSTStatusRanForSecondsKey
+ _OBJC_CLASS_$_ATXCallbackInfo
+ _OBJC_CLASS_$_ATXMicroLocationVisitEvent
+ _OBJC_CLASS_$_ATXMicroLocationVisitNumDevicesPerTechnology
+ _OBJC_CLASS_$_ATXMicroLocationVisitProbabilityPerLocation
+ _OBJC_CLASS_$_ATXMicroLocationVisitScheduler
+ _OBJC_CLASS_$_ATXMicroLocationVisitStream
+ _OBJC_CLASS_$_ATXRelevantShortcutsEvent
+ _OBJC_CLASS_$_ATXRelevantShortcutsStream
+ _OBJC_CLASS_$_ATXSleepEvent
+ _OBJC_CLASS_$_ATXSleepStream
+ _OBJC_CLASS_$_BMBiomeScheduler
+ _OBJC_CLASS_$_BMDeviceBacklight
+ _OBJC_CLASS_$_BMDeviceScreenLocked
+ _OBJC_CLASS_$_INRelevantShortcut
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$_NSTimeZone
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_IVAR_$_ATXCallbackInfo._callback
+ _OBJC_IVAR_$_ATXCallbackInfo._queue
+ _OBJC_IVAR_$_ATXGlobalStateForTesting._temporaryPathForTesting
+ _OBJC_IVAR_$_ATXMicroLocationVisitEvent._domain
+ _OBJC_IVAR_$_ATXMicroLocationVisitEvent._isStable
+ _OBJC_IVAR_$_ATXMicroLocationVisitEvent._maxProbability
+ _OBJC_IVAR_$_ATXMicroLocationVisitEvent._maxProbabilityMicroLocationIdentifier
+ _OBJC_IVAR_$_ATXMicroLocationVisitEvent._numDevicesVector
+ _OBJC_IVAR_$_ATXMicroLocationVisitEvent._probabilityVector
+ _OBJC_IVAR_$_ATXMicroLocationVisitEvent._timestamp
+ _OBJC_IVAR_$_ATXMicroLocationVisitNumDevicesPerTechnology._numDevices
+ _OBJC_IVAR_$_ATXMicroLocationVisitNumDevicesPerTechnology._technology
+ _OBJC_IVAR_$_ATXMicroLocationVisitProbabilityPerLocation._microLocationIdentifier
+ _OBJC_IVAR_$_ATXMicroLocationVisitProbabilityPerLocation._probability
+ _OBJC_IVAR_$_ATXMicroLocationVisitScheduler._biomeQueue
+ _OBJC_IVAR_$_ATXMicroLocationVisitScheduler._callbacks
+ _OBJC_IVAR_$_ATXMicroLocationVisitScheduler._microLocationScheduler
+ _OBJC_IVAR_$_ATXMicroLocationVisitScheduler._microLocationSink
+ _OBJC_IVAR_$_ATXMicroLocationVisitScheduler._stateQueue
+ _OBJC_IVAR_$_ATXRelevantShortcutsEvent._bundleID
+ _OBJC_IVAR_$_ATXRelevantShortcutsEvent._relevantShortcut
+ _OBJC_IVAR_$_ATXSleepEvent._sleepStartTime
+ _OBJC_IVAR_$_ATXSleepEvent._wakeUpTime
+ _OBJC_METACLASS_$_ATXCallbackInfo
+ _OBJC_METACLASS_$_ATXMicroLocationVisitEvent
+ _OBJC_METACLASS_$_ATXMicroLocationVisitNumDevicesPerTechnology
+ _OBJC_METACLASS_$_ATXMicroLocationVisitProbabilityPerLocation
+ _OBJC_METACLASS_$_ATXMicroLocationVisitScheduler
+ _OBJC_METACLASS_$_ATXMicroLocationVisitStream
+ _OBJC_METACLASS_$_ATXRelevantShortcutsEvent
+ _OBJC_METACLASS_$_ATXRelevantShortcutsStream
+ _OBJC_METACLASS_$_ATXSleepEvent
+ _OBJC_METACLASS_$_ATXSleepStream
+ __OBJC_$_CLASS_METHODS_ATXMicroLocationVisitScheduler
+ __OBJC_$_CLASS_METHODS_ATXMicroLocationVisitStream
+ __OBJC_$_INSTANCE_METHODS_ATXCallbackInfo
+ __OBJC_$_INSTANCE_METHODS_ATXMicroLocationVisitEvent
+ __OBJC_$_INSTANCE_METHODS_ATXMicroLocationVisitNumDevicesPerTechnology
+ __OBJC_$_INSTANCE_METHODS_ATXMicroLocationVisitProbabilityPerLocation
+ __OBJC_$_INSTANCE_METHODS_ATXMicroLocationVisitScheduler
+ __OBJC_$_INSTANCE_METHODS_ATXMicroLocationVisitStream
+ __OBJC_$_INSTANCE_METHODS_ATXRelevantShortcutsEvent
+ __OBJC_$_INSTANCE_METHODS_ATXRelevantShortcutsStream
+ __OBJC_$_INSTANCE_METHODS_ATXSleepEvent
+ __OBJC_$_INSTANCE_METHODS_ATXSleepStream
+ __OBJC_$_INSTANCE_VARIABLES_ATXCallbackInfo
+ __OBJC_$_INSTANCE_VARIABLES_ATXMicroLocationVisitEvent
+ __OBJC_$_INSTANCE_VARIABLES_ATXMicroLocationVisitNumDevicesPerTechnology
+ __OBJC_$_INSTANCE_VARIABLES_ATXMicroLocationVisitProbabilityPerLocation
+ __OBJC_$_INSTANCE_VARIABLES_ATXMicroLocationVisitScheduler
+ __OBJC_$_INSTANCE_VARIABLES_ATXRelevantShortcutsEvent
+ __OBJC_$_INSTANCE_VARIABLES_ATXSleepEvent
+ __OBJC_$_PROP_LIST_ATXCallbackInfo
+ __OBJC_$_PROP_LIST_ATXMicroLocationVisitEvent
+ __OBJC_$_PROP_LIST_ATXMicroLocationVisitNumDevicesPerTechnology
+ __OBJC_$_PROP_LIST_ATXMicroLocationVisitProbabilityPerLocation
+ __OBJC_$_PROP_LIST_ATXMicroLocationVisitScheduler
+ __OBJC_$_PROP_LIST_ATXMicroLocationVisitStream
+ __OBJC_$_PROP_LIST_ATXRelevantShortcutsEvent
+ __OBJC_$_PROP_LIST_ATXRelevantShortcutsStream
+ __OBJC_$_PROP_LIST_ATXSleepEvent
+ __OBJC_CLASS_PROTOCOLS_$_ATXMicroLocationVisitEvent
+ __OBJC_CLASS_PROTOCOLS_$_ATXMicroLocationVisitStream
+ __OBJC_CLASS_PROTOCOLS_$_ATXRelevantShortcutsEvent
+ __OBJC_CLASS_PROTOCOLS_$_ATXRelevantShortcutsStream
+ __OBJC_CLASS_RO_$_ATXCallbackInfo
+ __OBJC_CLASS_RO_$_ATXMicroLocationVisitEvent
+ __OBJC_CLASS_RO_$_ATXMicroLocationVisitNumDevicesPerTechnology
+ __OBJC_CLASS_RO_$_ATXMicroLocationVisitProbabilityPerLocation
+ __OBJC_CLASS_RO_$_ATXMicroLocationVisitScheduler
+ __OBJC_CLASS_RO_$_ATXMicroLocationVisitStream
+ __OBJC_CLASS_RO_$_ATXRelevantShortcutsEvent
+ __OBJC_CLASS_RO_$_ATXRelevantShortcutsStream
+ __OBJC_CLASS_RO_$_ATXSleepEvent
+ __OBJC_CLASS_RO_$_ATXSleepStream
+ __OBJC_METACLASS_RO_$_ATXCallbackInfo
+ __OBJC_METACLASS_RO_$_ATXMicroLocationVisitEvent
+ __OBJC_METACLASS_RO_$_ATXMicroLocationVisitNumDevicesPerTechnology
+ __OBJC_METACLASS_RO_$_ATXMicroLocationVisitProbabilityPerLocation
+ __OBJC_METACLASS_RO_$_ATXMicroLocationVisitScheduler
+ __OBJC_METACLASS_RO_$_ATXMicroLocationVisitStream
+ __OBJC_METACLASS_RO_$_ATXRelevantShortcutsEvent
+ __OBJC_METACLASS_RO_$_ATXRelevantShortcutsStream
+ __OBJC_METACLASS_RO_$_ATXSleepEvent
+ __OBJC_METACLASS_RO_$_ATXSleepStream
+ ___120-[ATXMicroLocationVisitStream enumerateMicroLocationVisitEventsFromStartDate:endDate:filterBlock:limit:ascending:block:]_block_invoke
+ ___120-[ATXMicroLocationVisitStream enumerateMicroLocationVisitEventsFromStartDate:endDate:filterBlock:limit:ascending:block:]_block_invoke.12
+ ___120-[ATXMicroLocationVisitStream enumerateMicroLocationVisitEventsFromStartDate:endDate:filterBlock:limit:ascending:block:]_block_invoke.cold.1
+ ___46-[ATXMicroLocationVisitScheduler isSubscribed]_block_invoke
+ ___48+[ATXMicroLocationVisitScheduler sharedInstance]_block_invoke
+ ___54-[ATXMicroLocationVisitScheduler hasActiveSubscribers]_block_invoke
+ ___54-[ATXMicroLocationVisitScheduler removeAllSubscribers]_block_invoke
+ ___55-[ATXMicroLocationVisitScheduler unSubscribeWithToken:]_block_invoke
+ ___58+[ATXPaths appPredictionDirectoryForClientWithIdentifier:]_block_invoke
+ ___60-[ATXMicroLocationVisitScheduler _handleMicroLocationEvent:]_block_invoke
+ ___60-[ATXMicroLocationVisitScheduler _handleMicroLocationEvent:]_block_invoke.57
+ ___64-[ATXMicroLocationVisitScheduler subscribeWithCallback:onQueue:]_block_invoke
+ ___65-[ATXMicroLocationVisitScheduler _onStateQueue_setupSubscription]_block_invoke
+ ___65-[ATXMicroLocationVisitScheduler _onStateQueue_setupSubscription]_block_invoke_2
+ ___68-[ATXMicroLocationVisitStream mostRecentMicroLocationWithinSeconds:]_block_invoke
+ ___72-[ATXSleepStream enumerateSleepEventsFromStartDate:endDate:limit:block:]_block_invoke
+ ___72-[ATXSleepStream enumerateSleepEventsFromStartDate:endDate:limit:block:]_block_invoke.17
+ ___72-[ATXSleepStream enumerateSleepEventsFromStartDate:endDate:limit:block:]_block_invoke_2
+ ___72-[ATXSleepStream enumerateSleepEventsFromStartDate:endDate:limit:block:]_block_invoke_2.cold.1
+ ___79-[ATXRelevantShortcutsStream enumerateEventsFromStartDate:endDate:limit:block:]_block_invoke
+ ___79-[ATXRelevantShortcutsStream enumerateEventsFromStartDate:endDate:limit:block:]_block_invoke.5
+ ___79-[ATXRelevantShortcutsStream enumerateEventsFromStartDate:endDate:limit:block:]_block_invoke.5.cold.1
+ ___79-[ATXRelevantShortcutsStream enumerateEventsFromStartDate:endDate:limit:block:]_block_invoke.cold.1
+ ___block_descriptor_32_e39_q24?0"BMStoreEvent"8"BMStoreEvent"16l
+ ___block_descriptor_40_e8_32r_e36_B16?0"ATXMicroLocationVisitEvent"8lr32l8
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32w_e22_v16?0"BMStoreEvent"8lw32l8
+ ___block_descriptor_40_e8_32w_e23_v16?0"BPSCompletion"8lw32l8
+ ___block_descriptor_48_e8_32s40bs_e22_B16?0"BMStoreEvent"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32bs40bs48r_e22_B16?0"BMStoreEvent"8lr48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
+ ___block_descriptor_88_e8_32s40s48bs56r64r72r_e22_B16?0"BMStoreEvent"8lr56l8r64l8s32l8r72l8s40l8s48l8
+ ___block_literal_global.16
+ _appPredictionDirectoryForClientWithIdentifier:.dir
+ _appPredictionDirectoryForClientWithIdentifier:.onceToken
+ _dispatch_assert_queue$V2
+ _dispatch_async
+ _dispatch_sync
+ _objc_msgSend$Location
+ _objc_msgSend$MicroLocationVisit
+ _objc_msgSend$RelevantShortcuts
+ _objc_msgSend$UUIDString
+ _objc_msgSend$_getDirectoryCreating:clientIdentifier:
+ _objc_msgSend$_handleCompletion:
+ _objc_msgSend$_handleMicroLocationEvent:
+ _objc_msgSend$_onStateQueue_cancelSubscription
+ _objc_msgSend$_onStateQueue_setupSubscription
+ _objc_msgSend$_relevantShortcutsPublisherWithStartDate:endDate:limit:
+ _objc_msgSend$appPredictionDirectoryForClientWithIdentifier:
+ _objc_msgSend$array
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$atxMicroLocationVisitEventFromBiomeEvent:
+ _objc_msgSend$atx_DSLPublisher
+ _objc_msgSend$atx_efficientRelevantShortcut:
+ _objc_msgSend$backlightPublisherWithStartDate:endDate:
+ _objc_msgSend$callback
+ _objc_msgSend$callbacks
+ _objc_msgSend$cancel
+ _objc_msgSend$containsDate:
+ _objc_msgSend$convertNumDevicesVectorFromBMArray:
+ _objc_msgSend$convertProbabilityVectorFromBMArray:
+ _objc_msgSend$currentCalendar
+ _objc_msgSend$dateByAddingTimeInterval:
+ _objc_msgSend$dateBySettingHour:minute:second:ofDate:options:
+ _objc_msgSend$defaultTimeZone
+ _objc_msgSend$domain
+ _objc_msgSend$enumerateMicroLocationVisitEventsFromStartDate:endDate:filterBlock:limit:ascending:block:
+ _objc_msgSend$hasAlreadyDetectedSleepEventOnGivenDay:sleepEvents:withCalendar:
+ _objc_msgSend$initWithBundleID:relevantShortcut:
+ _objc_msgSend$initWithDomain:maxProbabilityMicroLocationIdentifier:maxProbability:probabilityVector:isStable:numDevicesVector:timestamp:
+ _objc_msgSend$initWithIdentifier:targetQueue:
+ _objc_msgSend$initWithMicroLocationIdentifier:probability:
+ _objc_msgSend$initWithSleepStart:wakeUp:
+ _objc_msgSend$initWithTechnology:numDevices:
+ _objc_msgSend$isDate:inSameDayAsDate:
+ _objc_msgSend$isEqualToATXMicroLocationVisitEvent:
+ _objc_msgSend$isEqualToATXMicroLocationVisitNumDevicesPerTechnology:
+ _objc_msgSend$isEqualToATXMicroLocationVisitProbabilityPerLocation:
+ _objc_msgSend$isEqualToATXRelevantShortcutsEvent:
+ _objc_msgSend$isEqualToATXSleepEvent:
+ _objc_msgSend$isFirstBacklightOnAfterWakeup:sleepStartTime:existingSleepEventsToday:withCalendar:
+ _objc_msgSend$isIdlePeriodLongEnough:
+ _objc_msgSend$isStable
+ _objc_msgSend$isTimeInEligibleNotificationWindow:withCalendar:
+ _objc_msgSend$lastObject
+ _objc_msgSend$maxProbability
+ _objc_msgSend$maxProbabilityMicroLocationIdentifier
+ _objc_msgSend$microLocationIdentifier
+ _objc_msgSend$microLocationSink
+ _objc_msgSend$mostRecentMicroLocationWithinSeconds:
+ _objc_msgSend$numDevices
+ _objc_msgSend$numDevicesVector
+ _objc_msgSend$objectEnumerator
+ _objc_msgSend$orderedMergeWithOther:comparator:
+ _objc_msgSend$probability
+ _objc_msgSend$probabilityVector
+ _objc_msgSend$queue
+ _objc_msgSend$relevantShortcut
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeAllSubscribers
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$screenLockedPublisherWithStartDate:endDate:
+ _objc_msgSend$serializedRelevantShortcut
+ _objc_msgSend$setCallback:
+ _objc_msgSend$setMicroLocationScheduler:
+ _objc_msgSend$setMicroLocationSink:
+ _objc_msgSend$setQueue:
+ _objc_msgSend$setTimeZone:
+ _objc_msgSend$sleepStartTime
+ _objc_msgSend$stateQueue
+ _objc_msgSend$subscribeOn:
+ _objc_msgSend$subscribeWithCallback:onQueue:
+ _objc_msgSend$technology
+ _objc_msgSend$wakeUpTime
+ _objc_setProperty_nonatomic_copy
- +[ATXPaths _getDirectoryCreating:]
- ___34+[ATXPaths appPredictionDirectory]_block_invoke
- _appPredictionDirectory.dir
- _appPredictionDirectory.onceToken
- _objc_msgSend$_getDirectoryCreating:
CStrings:
+ "%s: Error fetching BMLibrary.Location.MicroLocationVisit events %@"
+ "%s: error fetching biome events: %@"
+ "-[ATXMicroLocationVisitStream enumerateMicroLocationVisitEventsFromStartDate:endDate:filterBlock:limit:ascending:block:]_block_invoke"
+ "-[ATXSleepStream enumerateSleepEventsFromStartDate:endDate:limit:block:]_block_invoke_2"
+ "<ATXSleepEvent %@ -> %@ (%.1f hours)>"
+ "@\"BMBiomeScheduler\""
+ "@\"BPSSink\""
+ "@\"INRelevantShortcut\""
+ "@\"NSArray\""
+ "@24@0:8@?16"
+ "@32@0:8@?16@24"
+ "@68@0:8@16@24@32@40B48@52@60"
+ "@?"
+ "@?16@0:8"
+ "ATXCallbackInfo"
+ "ATXMicroLocationVisitEvent"
+ "ATXMicroLocationVisitNumDevicesPerTechnology"
+ "ATXMicroLocationVisitProbabilityPerLocation"
+ "ATXMicroLocationVisitScheduler"
+ "ATXMicroLocationVisitScheduler.MicroLocationDonation"
+ "ATXMicroLocationVisitScheduler.m"
+ "ATXMicroLocationVisitScheduler: Added callback with identifier %@. Total callbacks: %lu"
+ "ATXMicroLocationVisitScheduler: Completed listening to micro-location events"
+ "ATXMicroLocationVisitScheduler: Error listening to micro-location events: %@"
+ "ATXMicroLocationVisitScheduler: Notifying %lu callbacks"
+ "ATXMicroLocationVisitScheduler: Received new micro-location event: %@"
+ "ATXMicroLocationVisitScheduler: Removed all callbacks"
+ "ATXMicroLocationVisitScheduler: Removed callback %@. Remaining: %lu"
+ "ATXMicroLocationVisitScheduler: Setting up micro-location subscription"
+ "ATXMicroLocationVisitScheduler: Subscription cancelled"
+ "ATXMicroLocationVisitScheduler: Successfully subscribed to micro-location events"
+ "ATXMicroLocationVisitStream"
+ "ATXRelevantShortcutsEvent"
+ "ATXRelevantShortcutsStream"
+ "ATXRelevantShortcutsStream.m"
+ "ATXRelevantShortcutsStream: Error querying App.RelevantShortcuts stream: %@"
+ "ATXRelevantShortcutsStream: Error unarchiving relevant shortcut: %@"
+ "ATXRelevantShortcutsStream: Invalid event App.RelevantShortcuts stream: %@"
+ "ATXSleepEvent"
+ "ATXSleepStream"
+ "B16@?0@\"ATXMicroLocationVisitEvent\"8"
+ "B24@0:8d16"
+ "B40@0:8@16@24@32"
+ "B48@0:8@16@24@32@40"
+ "DeferAfterSeconds"
+ "Emitted Sleep event: %@"
+ "Location"
+ "MicroLocationVisit"
+ "RelevantShortcuts"
+ "Started enumeration of Sleep events"
+ "StatusDefer"
+ "StatusDone"
+ "StatusRanForSeconds"
+ "T@\"BMBiomeScheduler\",&,N,V_microLocationScheduler"
+ "T@\"BPSSink\",&,N,V_microLocationSink"
+ "T@\"INRelevantShortcut\",R,N,V_relevantShortcut"
+ "T@\"NSArray\",R,N,V_numDevicesVector"
+ "T@\"NSArray\",R,N,V_probabilityVector"
+ "T@\"NSDate\",R,C,N,V_sleepStartTime"
+ "T@\"NSDate\",R,C,N,V_wakeUpTime"
+ "T@\"NSDate\",R,N,V_timestamp"
+ "T@\"NSMutableDictionary\",&,N,V_callbacks"
+ "T@\"NSNumber\",R,N,V_maxProbability"
+ "T@\"NSNumber\",R,N,V_numDevices"
+ "T@\"NSNumber\",R,N,V_probability"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_biomeQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_stateQueue"
+ "T@\"NSString\",C,N,V_temporaryPathForTesting"
+ "T@\"NSString\",R,N,V_domain"
+ "T@\"NSString\",R,N,V_maxProbabilityMicroLocationIdentifier"
+ "T@\"NSString\",R,N,V_microLocationIdentifier"
+ "T@\"NSString\",R,N,V_technology"
+ "T@?,C,N,V_callback"
+ "TB,R,N,V_isStable"
+ "UUIDString"
+ "_biomeQueue"
+ "_callback"
+ "_callbacks"
+ "_domain"
+ "_getDirectoryCreating:clientIdentifier:"
+ "_handleCompletion:"
+ "_handleMicroLocationEvent:"
+ "_isStable"
+ "_maxProbability"
+ "_maxProbabilityMicroLocationIdentifier"
+ "_microLocationIdentifier"
+ "_microLocationScheduler"
+ "_microLocationSink"
+ "_numDevices"
+ "_numDevicesVector"
+ "_onStateQueue_cancelSubscription"
+ "_onStateQueue_setupSubscription"
+ "_probability"
+ "_probabilityVector"
+ "_queue"
+ "_relevantShortcut"
+ "_relevantShortcutsPublisherWithStartDate:endDate:limit:"
+ "_sleepStartTime"
+ "_stateQueue"
+ "_technology"
+ "_temporaryPathForTesting"
+ "_wakeUpTime"
+ "appPredictionDirectoryFile:forClientWithIdentifier:"
+ "appPredictionDirectoryForClientWithIdentifier:"
+ "array"
+ "arrayWithCapacity:"
+ "atxMicroLocationVisitEventFromBiomeEvent:"
+ "atx_efficientRelevantShortcut:"
+ "backlightPublisherWithStartDate:endDate:"
+ "biomeQueue"
+ "callback"
+ "callbacks"
+ "cancel"
+ "com.apple.duetexpertcenter.ATXMicroLocationVisitScheduler.Biome"
+ "com.apple.duetexpertcenter.ATXMicroLocationVisitScheduler.Callback.%@"
+ "com.apple.duetexpertcenter.ATXMicroLocationVisitScheduler.State"
+ "containsDate:"
+ "convertNumDevicesVectorFromBMArray:"
+ "convertProbabilityVectorFromBMArray:"
+ "currentCalendar"
+ "dateByAddingTimeInterval:"
+ "dateBySettingHour:minute:second:ofDate:options:"
+ "defaultTimeZone"
+ "domain"
+ "enumerateEventsFromStartDate:endDate:limit:block:"
+ "enumerateMicroLocationVisitEventsFromStartDate:endDate:filterBlock:limit:ascending:block:"
+ "enumerateSleepEventsFromStartDate:endDate:limit:block:"
+ "hasActiveSubscribers"
+ "hasAlreadyDetectedSleepEventOnGivenDay:sleepEvents:withCalendar:"
+ "initWithBundleID:relevantShortcut:"
+ "initWithDomain:maxProbabilityMicroLocationIdentifier:maxProbability:probabilityVector:isStable:numDevicesVector:timestamp:"
+ "initWithIdentifier:targetQueue:"
+ "initWithMicroLocationIdentifier:probability:"
+ "initWithSleepStart:wakeUp:"
+ "initWithTechnology:numDevices:"
+ "isDate:inSameDayAsDate:"
+ "isEqualToATXMicroLocationVisitEvent:"
+ "isEqualToATXMicroLocationVisitNumDevicesPerTechnology:"
+ "isEqualToATXMicroLocationVisitProbabilityPerLocation:"
+ "isEqualToATXRelevantShortcutsEvent:"
+ "isEqualToATXSleepEvent:"
+ "isFirstBacklightOnAfterWakeup:sleepStartTime:existingSleepEventsToday:withCalendar:"
+ "isIdlePeriodLongEnough:"
+ "isStable"
+ "isSubscribed"
+ "isTimeInEligibleNotificationWindow:withCalendar:"
+ "lastObject"
+ "maxProbability"
+ "maxProbabilityMicroLocationIdentifier"
+ "microLocationIdentifier"
+ "microLocationScheduler"
+ "microLocationSink"
+ "mostRecentMicroLocation"
+ "mostRecentMicroLocationWithinSeconds:"
+ "numDevices"
+ "numDevicesVector"
+ "objectEnumerator"
+ "orderedMergeWithOther:comparator:"
+ "probability"
+ "probabilityVector"
+ "q24@?0@\"BMStoreEvent\"8@\"BMStoreEvent\"16"
+ "queue"
+ "relevantShortcut"
+ "removeAllObjects"
+ "removeAllSubscribers"
+ "removeObjectForKey:"
+ "screenLockedPublisherWithStartDate:endDate:"
+ "serializedRelevantShortcut"
+ "setBiomeQueue:"
+ "setCallback:"
+ "setCallbacks:"
+ "setMicroLocationScheduler:"
+ "setMicroLocationSink:"
+ "setQueue:"
+ "setStateQueue:"
+ "setTemporaryPathForTesting:"
+ "setTimeZone:"
+ "sleepStartTime"
+ "stateQueue"
+ "subscribeOn:"
+ "subscribeWithCallback:"
+ "subscribeWithCallback:onQueue:"
+ "technology"
+ "temporaryPathForTesting"
+ "unSubscribeWithToken:"
+ "v48@0:8@16@24Q32@?40"
+ "wakeUpTime"
- "@20@0:8B16"
- "_getDirectoryCreating:"

```
