## Sleep

> `/System/Library/PrivateFrameworks/Sleep.framework/Sleep`

```diff

-7027.0.72.2.7
-  __TEXT.__text: 0x58a48
-  __TEXT.__objc_methlist: 0x752c
-  __TEXT.__const: 0x830
+7027.1.36.2.7
+  __TEXT.__text: 0x5742c
+  __TEXT.__objc_methlist: 0x71bc
+  __TEXT.__const: 0xa20
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__constg_swiftt: 0x178
-  __TEXT.__swift5_typeref: 0x161
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0xc5
-  __TEXT.__swift5_assocty: 0x50
-  __TEXT.__swift5_proto: 0x50
-  __TEXT.__swift5_types: 0x20
-  __TEXT.__swift5_fieldmd: 0x130
-  __TEXT.__cstring: 0x4c09
-  __TEXT.__oslogstring: 0x43da
-  __TEXT.__gcc_except_tab: 0x7b4
-  __TEXT.__unwind_info: 0x2560
+  __TEXT.__constg_swiftt: 0x198
+  __TEXT.__swift5_typeref: 0x1ad
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_reflstr: 0xe5
+  __TEXT.__swift5_assocty: 0x80
+  __TEXT.__swift5_fieldmd: 0x14c
+  __TEXT.__swift5_proto: 0x68
+  __TEXT.__swift5_types: 0x24
+  __TEXT.__cstring: 0x498d
+  __TEXT.__oslogstring: 0x3fb7
+  __TEXT.__gcc_except_tab: 0x798
+  __TEXT.__unwind_info: 0x2508
   __TEXT.__eh_frame: 0x128
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2c70
-  __DATA_CONST.__objc_classlist: 0x310
-  __DATA_CONST.__objc_catlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x1d8
+  __DATA_CONST.__const: 0x2b78
+  __DATA_CONST.__objc_classlist: 0x2e0
+  __DATA_CONST.__objc_catlist: 0x90
+  __DATA_CONST.__objc_protolist: 0x1f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3828
-  __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_superrefs: 0x280
+  __DATA_CONST.__objc_selrefs: 0x3660
+  __DATA_CONST.__objc_protorefs: 0x78
+  __DATA_CONST.__objc_superrefs: 0x250
   __DATA_CONST.__objc_arraydata: 0xa8
-  __DATA_CONST.__got: 0x5a0
-  __AUTH_CONST.__const: 0x9c8
-  __AUTH_CONST.__cfstring: 0x5260
-  __AUTH_CONST.__objc_const: 0xc158
-  __AUTH_CONST.__objc_intobj: 0x18
+  __DATA_CONST.__got: 0x598
+  __AUTH_CONST.__const: 0x950
+  __AUTH_CONST.__cfstring: 0x4fc0
+  __AUTH_CONST.__objc_const: 0xbb10
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x5f0
-  __AUTH.__objc_data: 0x598
+  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__auth_got: 0x670
+  __AUTH.__objc_data: 0x4f8
   __AUTH.__data: 0x110
-  __DATA.__objc_ivar: 0x62c
-  __DATA.__data: 0x16b0
+  __DATA.__objc_ivar: 0x5f0
+  __DATA.__data: 0x1830
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_ivar: 0x34
-  __DATA_DIRTY.__objc_data: 0x1978
+  __DATA_DIRTY.__objc_data: 0x1838
   __DATA_DIRTY.__data: 0xf8
-  __DATA_DIRTY.__bss: 0x128
-  __DATA_DIRTY.__common: 0xd0
+  __DATA_DIRTY.__bss: 0x130
+  __DATA_DIRTY.__common: 0xd8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2891
-  Symbols:   6424
-  CStrings:  1122
+  Functions: 2845
+  Symbols:   6245
+  CStrings:  1080
 
Symbols:
+ +[HKSPSleepScheduleModel templateModelForSchedule:eventRecord:]
+ -[HKSPAnalyticsDailyReportEvent setSleepScoreAlgorithmVersion:]
+ -[HKSPAnalyticsDailyReportEvent sleepScoreAlgorithmVersion]
+ -[HKSPAnalyticsManager initWithSleepDataSource:]
+ -[HKSPAnalyticsManager initWithSleepDataSource:ihaOptInStatusProvider:diagnosticsOptInStatusProvider:analyticsEventConsumer:]
+ -[HKSPAnalyticsManager init]
+ -[HKSPAnalyticsManager setSleepDataSource:]
+ -[HKSPAnalyticsManager sleepDataSource]
+ -[HKSPAnalyticsManager(HKSPSleepScheduleAnalyticsReporting) trackSleepScheduleChangeWithContext:isSleepTrackingEnabled:]
+ -[HKSPAnalyticsManager(SleepDataInteraction) trackSleepDataInteractionEventWithType:isOnboardedVitals:date:completion:]
+ -[HKSPAnalyticsManager(SleepDataInteraction) trackSleepRoomEntryEventWithProvenanceInfo:isOnboardedSleep:date:completion:]
+ -[HKSPSleepScheduleChange .cxx_destruct]
+ -[HKSPSleepScheduleChange analyticsContext]
+ -[HKSPSleepScheduleChange date]
+ -[HKSPSleepScheduleChange initWithSchedule:date:shouldForceSave:isSleepTrackingEnabled:analyticsContext:]
+ -[HKSPSleepScheduleChange isSleepTrackingEnabled]
+ -[HKSPSleepScheduleChange schedule]
+ -[HKSPSleepScheduleChange shouldForceSave]
+ -[HKSPSleepScheduleModel(OverrideGeneration) isProposedOccurrenceUpcoming:currentDate:gregorianCalendar:]
+ -[HKSPSleepScheduleOccurrence(OverrideGeneration) occurrenceForPreviousDayWithGregorianCalendar:]
+ -[HKSPSleepStore _recordScheduleChange:options:context:]
+ -[HKSPSleepStore initWithConnectionProviderProvider:identifier:scheduleHistoryWriter:options:]
+ -[HKSPSleepStore initWithConnectionProviderProvider:identifier:scheduleHistoryWriter:options:throttlerProvider:callbackScheduler:sleepFocusModeBridgeProvider:widgetTimelineControllersProvider:widgetRelevanceControllerProvider:currentDateProvider:]
+ -[HKSPSleepStore initWithIdentifier:options:]
+ -[HKSPSleepStore initWithIdentifier:scheduleHistoryWriter:]
+ -[HKSPSleepStore initWithIdentifier:scheduleHistoryWriter:options:]
+ -[HKSPSleepStore initWithScheduleHistoryWriter:]
+ -[HKSPSleepStore scheduleHistoryWriter]
+ -[HKSPSleepStore(HealthKit) initWithHealthStore:]
+ -[HKSPSleepStore(HealthKit) initWithIdentifier:healthStore:]
+ -[HKSPSleepStore(HealthKit) initWithIdentifier:healthStore:options:]
+ -[HKSleepHealthStore(HKSPSleepScheduleHistoryWriting) recordSleepScheduleChange:completion:]
+ GCC_except_table46
+ _HKAnalyticsAllowed
+ _HKIsAgeGatedUserDefaultsSleepTrackingKey
+ _HKSPAnalyticsActivePairedWatchProductType
+ _HKSPAnalyticsCurrentDevice
+ _HKSPSleepLogCategoryCharts
+ _OBJC_CLASS_$_HKSPSleepScheduleChange
+ _OBJC_IVAR_$_HKSPAnalyticsDailyReportEvent._sleepScoreAlgorithmVersion
+ _OBJC_IVAR_$_HKSPAnalyticsManager._sleepDataSource
+ _OBJC_IVAR_$_HKSPSleepScheduleChange._analyticsContext
+ _OBJC_IVAR_$_HKSPSleepScheduleChange._date
+ _OBJC_IVAR_$_HKSPSleepScheduleChange._isSleepTrackingEnabled
+ _OBJC_IVAR_$_HKSPSleepScheduleChange._schedule
+ _OBJC_IVAR_$_HKSPSleepScheduleChange._shouldForceSave
+ _OBJC_IVAR_$_HKSPSleepStore._scheduleHistoryWriter
+ _OBJC_METACLASS_$_HKSPSleepScheduleChange
+ __CATEGORY_CLASS_METHODS_HKFeatureAvailabilityRequirementSet_$_Sleep
+ __CATEGORY_HKFeatureAvailabilityRequirementSet_$_Sleep
+ __OBJC_$_CATEGORY_HKSleepHealthStore_$_HKSPSleepScheduleHistoryWriting
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_HKSleepHealthStore_$_HKSPSleepScheduleHistoryWriting
+ __OBJC_$_INSTANCE_METHODS_HKSPAnalyticsManager(HKSPSleepScheduleAnalyticsReporting|SleepDataInteraction)
+ __OBJC_$_INSTANCE_METHODS_HKSPSleepScheduleChange
+ __OBJC_$_INSTANCE_METHODS_HKSPSleepScheduleOccurrence(OverrideGeneration)
+ __OBJC_$_INSTANCE_METHODS_HKSPSleepStore(Proactive|HealthKit)
+ __OBJC_$_INSTANCE_METHODS_NSError(HKSPSleepEventTimelineResults|HKSPXPCConnectionProvider)
+ __OBJC_$_INSTANCE_VARIABLES_HKSPSleepScheduleChange
+ __OBJC_$_PROP_LIST_HKSPSleepConnectionProviding
+ __OBJC_$_PROP_LIST_HKSPSleepScheduleChange
+ __OBJC_$_PROP_LIST_HKSleepHealthStore_$_HKSPSleepScheduleHistoryWriting
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKFeatureAvailabilityRequirementsProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKSPSleepConnectionProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKSPSleepScheduleHistoryWriting
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKFeatureAvailabilityRequirementsProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKSPSleepConnectionProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKSPSleepScheduleHistoryWriting
+ __OBJC_$_PROTOCOL_REFS_HKSPSleepConnectionProviding
+ __OBJC_$_PROTOCOL_REFS_HKSPSleepScheduleHistoryWriting
+ __OBJC_CATEGORY_PROTOCOLS_$_HKSleepHealthStore_$_HKSPSleepScheduleHistoryWriting
+ __OBJC_CLASS_RO_$_HKSPSleepScheduleChange
+ __OBJC_LABEL_PROTOCOL_$_HKFeatureAvailabilityRequirementsProviding
+ __OBJC_LABEL_PROTOCOL_$_HKSPSleepConnectionProviding
+ __OBJC_LABEL_PROTOCOL_$_HKSPSleepScheduleHistoryWriting
+ __OBJC_METACLASS_RO_$_HKSPSleepScheduleChange
+ __OBJC_PROTOCOL_$_HKFeatureAvailabilityRequirementsProviding
+ __OBJC_PROTOCOL_$_HKSPSleepConnectionProviding
+ __OBJC_PROTOCOL_$_HKSPSleepScheduleHistoryWriting
+ ___119-[HKSPAnalyticsManager(SleepDataInteraction) trackSleepDataInteractionEventWithType:isOnboardedVitals:date:completion:]_block_invoke
+ ___122-[HKSPAnalyticsManager(SleepDataInteraction) trackSleepRoomEntryEventWithProvenanceInfo:isOnboardedSleep:date:completion:]_block_invoke
+ ___247-[HKSPSleepStore initWithConnectionProviderProvider:identifier:scheduleHistoryWriter:options:throttlerProvider:callbackScheduler:sleepFocusModeBridgeProvider:widgetTimelineControllersProvider:widgetRelevanceControllerProvider:currentDateProvider:]_block_invoke
+ ___48-[HKSPAnalyticsManager initWithSleepDataSource:]_block_invoke
+ ___48-[HKSPAnalyticsManager initWithSleepDataSource:]_block_invoke_2
+ ___48-[HKSPAnalyticsManager initWithSleepDataSource:]_block_invoke_3
+ ___56-[HKSPSleepStore _recordScheduleChange:options:context:]_block_invoke
+ ___67-[HKSPSleepStore initWithIdentifier:scheduleHistoryWriter:options:]_block_invoke
+ ___92-[HKSleepHealthStore(HKSPSleepScheduleHistoryWriting) recordSleepScheduleChange:completion:]_block_invoke
+ ___94-[HKSPSleepStore initWithConnectionProviderProvider:identifier:scheduleHistoryWriter:options:]_block_invoke
+ ___94-[HKSPSleepStore initWithConnectionProviderProvider:identifier:scheduleHistoryWriter:options:]_block_invoke_2
+ ___94-[HKSPSleepStore initWithConnectionProviderProvider:identifier:scheduleHistoryWriter:options:]_block_invoke_3
+ ___94-[HKSPSleepStore initWithConnectionProviderProvider:identifier:scheduleHistoryWriter:options:]_block_invoke_4
+ ___HKSPHealthKitSchedulesFromSleepSchedule_block_invoke
+ ___HKSPHealthKitSchedulesFromSleepSchedule_block_invoke_2
+ ___block_descriptor_32_e56_"<HKSPSleepConnectionProviding>"16?0"HKSPSleepStore"8l
+ ___block_descriptor_40_e8_32s_e20_v24?08"NSError"16ls32l8
+ ___block_descriptor_65_e8_32s40s48bs_e44_v24?0"HKSPSleepScheduleModel"8"NSError"16ls48l8s32l8s40l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e44_v24?0"HKSPSleepScheduleModel"8"NSError"16ls56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s_e39_v24?0"HKSPSleepSettings"8"NSError"16ls32l8s40l8s48l8s56l8
+ __swiftEmptyDictionarySingleton
+ _associated conformance So28HKFeatureAvailabilityContextaSHSCSQ
+ _associated conformance So28HKFeatureAvailabilityContextas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So28HKFeatureAvailabilityContextas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _objc_msgSend$_recordScheduleChange:options:context:
+ _objc_msgSend$analyticsContext
+ _objc_msgSend$hksp_generalSleepFeatureRequirementSetForFeatureIdentifier:
+ _objc_msgSend$hksp_sleepTrackingRequirementSetForFeatureIdentifier:
+ _objc_msgSend$initWithConnectionProviderProvider:identifier:scheduleHistoryWriter:options:
+ _objc_msgSend$initWithConnectionProviderProvider:identifier:scheduleHistoryWriter:options:throttlerProvider:callbackScheduler:sleepFocusModeBridgeProvider:widgetTimelineControllersProvider:widgetRelevanceControllerProvider:currentDateProvider:
+ _objc_msgSend$initWithIdentifier:scheduleHistoryWriter:
+ _objc_msgSend$initWithIdentifier:scheduleHistoryWriter:options:
+ _objc_msgSend$initWithSchedule:date:shouldForceSave:isSleepTrackingEnabled:analyticsContext:
+ _objc_msgSend$initWithSleepDataSource:
+ _objc_msgSend$initWithSleepDataSource:ihaOptInStatusProvider:diagnosticsOptInStatusProvider:analyticsEventConsumer:
+ _objc_msgSend$modelByApplyingChangesFromOccurrence:
+ _objc_msgSend$recordSleepScheduleChange:completion:
+ _objc_msgSend$shouldForceSave
+ _objc_msgSend$sleepDataSource
+ _objc_msgSend$sleepScoreAlgorithmVersion
+ _objc_msgSend$templateModelForSchedule:eventRecord:
+ _objc_msgSend$trackSleepScheduleChangeWithContext:isSleepTrackingEnabled:
+ _swift_arrayInitWithCopy
+ _swift_getExistentialTypeMetadata
+ _swift_initStackObject
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
+ _swift_retain_x20
+ _swift_setDeallocating
+ _symbolic $ss21_ObjectiveCBridgeableP
+ _symbolic SS
+ _symbolic So8NSStringC
+ _symbolic _____ So28HKFeatureAvailabilityContexta
+ _type_layout_string So28HKFeatureAvailabilityContexta
- +[HKSPAnalyticsManager activePairedWatchProductType]
- +[HKSPAnalyticsManager currentDeviceType]
- +[HKSPAnalyticsManager defaultIsDiagnosticDataSubmissionAllowed]
- +[HKSPAnalyticsWindDownEvent _payloadValueForWindDownAction:]
- +[HKSPAnalyticsWindDownEventData supportsSecureCoding]
- +[HKSPAnalyticsWindDownEventDataWrapper supportsSecureCoding]
- +[HKSPHealthStoreProvider _initializedLocalDeviceHealthStore]
- +[HKSPSleepStore _updatedHistoricalSleepGoalForSleepSchedule:options:date:]
- +[HKSPSleepStore _updatedHistoricalSleepSchedulesFromSleepSchedule:options:date:]
- +[HKSPSleepStoreCache strongCache]
- +[HKSPSleepStoreCache weakCache]
- -[HKSPAnalyticsDailyReportEvent interactedWithWindDownLast24Hrs]
- -[HKSPAnalyticsDailyReportEvent setInteractedWithWindDownLast24Hrs:]
- -[HKSPAnalyticsDailyReportEvent setWeeksSinceOnboardedWindDownActions:]
- -[HKSPAnalyticsDailyReportEvent weeksSinceOnboardedWindDownActions]
- -[HKSPAnalyticsManager analyticsStore]
- -[HKSPAnalyticsManager initWithUserDefaults:]
- -[HKSPAnalyticsManager initWithUserDefaults:ihaOptInStatusProvider:diagnosticsOptInStatusProvider:analyticsEventConsumer:]
- -[HKSPAnalyticsManager setAnalyticsEventConsumer:]
- -[HKSPAnalyticsManager setAnalyticsStore:]
- -[HKSPAnalyticsManager setDiagnosticsOptInStatusProvider:]
- -[HKSPAnalyticsManager setIhaOptInStatusProvider:]
- -[HKSPAnalyticsStore .cxx_destruct]
- -[HKSPAnalyticsStore _setWindDownActions:forMorningIndex:overwriteExisting:]
- -[HKSPAnalyticsStore diagnosticsOptInStatusProvider]
- -[HKSPAnalyticsStore initWithUserDefaults:]
- -[HKSPAnalyticsStore initWithUserDefaults:diagnosticsOptInStatusProvider:]
- -[HKSPAnalyticsStore markAllActionsAsCollected]
- -[HKSPAnalyticsStore readAllWindDownActions]
- -[HKSPAnalyticsStore removeAllWindDownActionsBeforeMorningIndex:]
- -[HKSPAnalyticsStore setBaselineForWindDownActions:onMorningIndex:]
- -[HKSPAnalyticsStore setDiagnosticsOptInStatusProvider:]
- -[HKSPAnalyticsStore uncollectedWindDownActions]
- -[HKSPAnalyticsStore updateWindDownActions:onMorningIndex:]
- -[HKSPAnalyticsStore userDefaults]
- -[HKSPAnalyticsStore windDownActionsAfterMorningIndex:]
- -[HKSPAnalyticsStore windDownActionsForMorningIndex:]
- -[HKSPAnalyticsStore writeWindDownActions:]
- -[HKSPAnalyticsWindDownEvent .cxx_destruct]
- -[HKSPAnalyticsWindDownEvent eventName]
- -[HKSPAnalyticsWindDownEvent eventPayload]
- -[HKSPAnalyticsWindDownEvent initWithWindDownEventData:watchProductType:weeksSinceOnboarded:]
- -[HKSPAnalyticsWindDownEvent setEventName:]
- -[HKSPAnalyticsWindDownEvent setEventPayload:]
- -[HKSPAnalyticsWindDownEventData .cxx_destruct]
- -[HKSPAnalyticsWindDownEventData action]
- -[HKSPAnalyticsWindDownEventData collectedEventDataCopy]
- -[HKSPAnalyticsWindDownEventData encodeWithCoder:]
- -[HKSPAnalyticsWindDownEventData hash]
- -[HKSPAnalyticsWindDownEventData identifier]
- -[HKSPAnalyticsWindDownEventData initWithCoder:]
- -[HKSPAnalyticsWindDownEventData initWithWindDownAction:wasUsed:identifier:]
- -[HKSPAnalyticsWindDownEventData initWithWindDownAction:wasUsed:identifier:wasCollected:]
- -[HKSPAnalyticsWindDownEventData isEqual:]
- -[HKSPAnalyticsWindDownEventData isEqualEventData:]
- -[HKSPAnalyticsWindDownEventData wasCollected]
- -[HKSPAnalyticsWindDownEventData wasUsed]
- -[HKSPAnalyticsWindDownEventDataWrapper .cxx_destruct]
- -[HKSPAnalyticsWindDownEventDataWrapper encodeWithCoder:]
- -[HKSPAnalyticsWindDownEventDataWrapper eventDatums]
- -[HKSPAnalyticsWindDownEventDataWrapper initWithCoder:]
- -[HKSPAnalyticsWindDownEventDataWrapper initWithEventDatums:]
- -[HKSPAnalyticsWindDownEventDataWrapper setEventDatums:]
- -[HKSPFeatureAvailabilityStore _defaultRequirements]
- -[HKSPFeatureAvailabilityStore _defaultSleepTrackingRequirements]
- -[HKSPFeatureAvailabilityStore _onboardSleepTrackingRequirements]
- -[HKSPFeatureAvailabilityStore _sleepTrackingRequirements]
- -[HKSPFeatureAvailabilityStore _useSleepTrackingRequirements]
- -[HKSPFeatureAvailabilityStore earliestDateLowestOnboardingVersionCompletedWithError:]
- -[HKSPFeatureAvailabilityStore onboardedCountryCodeSupportedStateWithError:]
- -[HKSPHealthStoreProvider .cxx_destruct]
- -[HKSPHealthStoreProvider healthStore]
- -[HKSPHealthStoreProvider initWithLocalDeviceHealthStore]
- -[HKSPHealthStoreProvider initWithSleepHealthStore:healthStore:]
- -[HKSPHealthStoreProvider sleepHealthStore]
- -[HKSPSleepModeButtonModel .cxx_destruct]
- -[HKSPSleepModeButtonModel _checkSleepModeState]
- -[HKSPSleepModeButtonModel _launchAppForOnboarding]
- -[HKSPSleepModeButtonModel _queue_updateStateWithSleepMode:]
- -[HKSPSleepModeButtonModel _updateStateWithSleepMode:]
- -[HKSPSleepModeButtonModel behavior]
- -[HKSPSleepModeButtonModel delegate]
- -[HKSPSleepModeButtonModel initWithDelegate:]
- -[HKSPSleepModeButtonModel initWithSleepStore:delegate:behavior:]
- -[HKSPSleepModeButtonModel isSelected]
- -[HKSPSleepModeButtonModel setSelected:]
- -[HKSPSleepModeButtonModel sleepMode]
- -[HKSPSleepModeButtonModel sleepStore:sleepModeOnDidChange:]
- -[HKSPSleepModeButtonModel sleepStore]
- -[HKSPSleepStore _sendScheduleChangedAnalyticsWithContext:]
- -[HKSPSleepStore _writeHistoricalSchedule:options:]
- -[HKSPSleepStore analyticsManager]
- -[HKSPSleepStore healthStore]
- -[HKSPSleepStore initWithConnectionProviderProvider:identifier:healthStore:options:]
- -[HKSPSleepStore initWithConnectionProviderProvider:identifier:healthStore:options:analyticsManager:throttlerProvider:callbackScheduler:sleepFocusModeBridgeProvider:widgetTimelineControllersProvider:widgetRelevanceControllerProvider:currentDateProvider:]
- -[HKSPSleepStore initWithHealthStore:]
- -[HKSPSleepStore initWithIdentifier:healthStore:]
- -[HKSPSleepStore initWithIdentifier:healthStore:options:]
- -[HKSPSleepStore sleepHealthStore]
- -[HKSPSleepStore(Analytics) trackSleepDataInteractionEventWithType:isOnboardedVitals:completion:]
- -[HKSPSleepStoreCache .cxx_destruct]
- -[HKSPSleepStoreCache initWithSleepStoreProvider:]
- -[HKSPSleepStoreCache initWithSleepStoreProvider:useWeakReferences:]
- -[HKSPSleepStoreCache init]
- -[HKSPSleepStoreCache sleepStoreForIdentifier:]
- -[HKSPSleepStoreCache sleepStoreForIdentifier:healthStore:]
- -[NSError(HKSPSleep) hksp_isHealthDatabaseInaccessibleError]
- -[_HKBehavior(HKSPSleep) hksp_supportsSleepTracking]
- GCC_except_table50
- _HKCreateSerialDispatchQueue
- _HKDaysInAWeek
- _HKErrorDomain
- _HKSHSleepScoreResultsNotificationEventIdentifier
- _HKSPAnalyticsEventNameWindDown
- _HKSPAnalyticsPayloadKeyWindDownActionPresented
- _HKSPAnalyticsPayloadKeyWindDownActionUsed
- _HKSPAnalyticsPayloadKeyWindDownWeeksSinceOnboarded
- _HKSPAnalyticsStoreUserDefaultsKey
- _HKSPSleepEventIdentifierSleepScoreResultsNotification
- _HKSPSleepScoreIntroductionCategory
- _HKSPSleepScoreResultsCategory
- _HKSPSleepScoreResultsIdentifier
- _OBJC_CLASS_$_HKHealthStore
- _OBJC_CLASS_$_HKSPAnalyticsStore
- _OBJC_CLASS_$_HKSPAnalyticsWindDownEvent
- _OBJC_CLASS_$_HKSPAnalyticsWindDownEventData
- _OBJC_CLASS_$_HKSPAnalyticsWindDownEventDataWrapper
- _OBJC_CLASS_$_HKSPHealthStoreProvider
- _OBJC_CLASS_$_HKSPSleepModeButtonModel
- _OBJC_CLASS_$_HKSPSleepStoreCache
- _OBJC_CLASS_$_MCProfileConnection
- _OBJC_CLASS_$_NSKeyedUnarchiver
- _OBJC_IVAR_$_HKSPAnalyticsDailyReportEvent._interactedWithWindDownLast24Hrs
- _OBJC_IVAR_$_HKSPAnalyticsDailyReportEvent._weeksSinceOnboardedWindDownActions
- _OBJC_IVAR_$_HKSPAnalyticsManager._analyticsStore
- _OBJC_IVAR_$_HKSPAnalyticsStore._diagnosticsOptInStatusProvider
- _OBJC_IVAR_$_HKSPAnalyticsStore._userDefaults
- _OBJC_IVAR_$_HKSPAnalyticsWindDownEvent._eventName
- _OBJC_IVAR_$_HKSPAnalyticsWindDownEvent._eventPayload
- _OBJC_IVAR_$_HKSPAnalyticsWindDownEventData._action
- _OBJC_IVAR_$_HKSPAnalyticsWindDownEventData._identifier
- _OBJC_IVAR_$_HKSPAnalyticsWindDownEventData._wasCollected
- _OBJC_IVAR_$_HKSPAnalyticsWindDownEventData._wasUsed
- _OBJC_IVAR_$_HKSPAnalyticsWindDownEventDataWrapper._eventDatums
- _OBJC_IVAR_$_HKSPHealthStoreProvider._healthStore
- _OBJC_IVAR_$_HKSPHealthStoreProvider._sleepHealthStore
- _OBJC_IVAR_$_HKSPSleepModeButtonModel._behavior
- _OBJC_IVAR_$_HKSPSleepModeButtonModel._delegate
- _OBJC_IVAR_$_HKSPSleepModeButtonModel._sleepMode
- _OBJC_IVAR_$_HKSPSleepModeButtonModel._sleepStore
- _OBJC_IVAR_$_HKSPSleepStore._analyticsManager
- _OBJC_IVAR_$_HKSPSleepStore._sleepHealthStore
- _OBJC_IVAR_$_HKSPSleepStoreCache._lock
- _OBJC_IVAR_$_HKSPSleepStoreCache._sleepStoreProvider
- _OBJC_IVAR_$_HKSPSleepStoreCache._sleepStoresByIdentifier
- _OBJC_METACLASS_$_HKSPAnalyticsStore
- _OBJC_METACLASS_$_HKSPAnalyticsWindDownEvent
- _OBJC_METACLASS_$_HKSPAnalyticsWindDownEventData
- _OBJC_METACLASS_$_HKSPAnalyticsWindDownEventDataWrapper
- _OBJC_METACLASS_$_HKSPHealthStoreProvider
- _OBJC_METACLASS_$_HKSPSleepModeButtonModel
- _OBJC_METACLASS_$_HKSPSleepStoreCache
- __HKLogDroppedError
- __OBJC_$_CLASS_METHODS_HKSPAnalyticsManager
- __OBJC_$_CLASS_METHODS_HKSPAnalyticsWindDownEvent
- __OBJC_$_CLASS_METHODS_HKSPAnalyticsWindDownEventData
- __OBJC_$_CLASS_METHODS_HKSPAnalyticsWindDownEventDataWrapper
- __OBJC_$_CLASS_METHODS_HKSPHealthStoreProvider
- __OBJC_$_CLASS_METHODS_HKSPSleepStoreCache
- __OBJC_$_CLASS_PROP_LIST_HKSPAnalyticsWindDownEventData
- __OBJC_$_CLASS_PROP_LIST_HKSPAnalyticsWindDownEventDataWrapper
- __OBJC_$_INSTANCE_METHODS_HKSPAnalyticsManager
- __OBJC_$_INSTANCE_METHODS_HKSPAnalyticsStore
- __OBJC_$_INSTANCE_METHODS_HKSPAnalyticsWindDownEvent
- __OBJC_$_INSTANCE_METHODS_HKSPAnalyticsWindDownEventData
- __OBJC_$_INSTANCE_METHODS_HKSPAnalyticsWindDownEventDataWrapper
- __OBJC_$_INSTANCE_METHODS_HKSPHealthStoreProvider
- __OBJC_$_INSTANCE_METHODS_HKSPSleepModeButtonModel
- __OBJC_$_INSTANCE_METHODS_HKSPSleepScheduleOccurrence
- __OBJC_$_INSTANCE_METHODS_HKSPSleepStore(Proactive|Analytics)
- __OBJC_$_INSTANCE_METHODS_HKSPSleepStoreCache
- __OBJC_$_INSTANCE_METHODS_NSError(HKSPSleepEventTimelineResults|HKSPSleep|HKSPXPCConnectionProvider)
- __OBJC_$_INSTANCE_VARIABLES_HKSPAnalyticsStore
- __OBJC_$_INSTANCE_VARIABLES_HKSPAnalyticsWindDownEvent
- __OBJC_$_INSTANCE_VARIABLES_HKSPAnalyticsWindDownEventData
- __OBJC_$_INSTANCE_VARIABLES_HKSPAnalyticsWindDownEventDataWrapper
- __OBJC_$_INSTANCE_VARIABLES_HKSPHealthStoreProvider
- __OBJC_$_INSTANCE_VARIABLES_HKSPSleepModeButtonModel
- __OBJC_$_INSTANCE_VARIABLES_HKSPSleepStoreCache
- __OBJC_$_PROP_LIST_HKSPAnalyticsStore
- __OBJC_$_PROP_LIST_HKSPAnalyticsWindDownEvent
- __OBJC_$_PROP_LIST_HKSPAnalyticsWindDownEventData
- __OBJC_$_PROP_LIST_HKSPAnalyticsWindDownEventDataWrapper
- __OBJC_$_PROP_LIST_HKSPHealthStoreProvider
- __OBJC_$_PROP_LIST_HKSPSleepModeButtonModel
- __OBJC_CLASS_PROTOCOLS_$_HKSPAnalyticsWindDownEvent
- __OBJC_CLASS_PROTOCOLS_$_HKSPAnalyticsWindDownEventData
- __OBJC_CLASS_PROTOCOLS_$_HKSPAnalyticsWindDownEventDataWrapper
- __OBJC_CLASS_PROTOCOLS_$_HKSPSleepModeButtonModel
- __OBJC_CLASS_RO_$_HKSPAnalyticsStore
- __OBJC_CLASS_RO_$_HKSPAnalyticsWindDownEvent
- __OBJC_CLASS_RO_$_HKSPAnalyticsWindDownEventData
- __OBJC_CLASS_RO_$_HKSPAnalyticsWindDownEventDataWrapper
- __OBJC_CLASS_RO_$_HKSPHealthStoreProvider
- __OBJC_CLASS_RO_$_HKSPSleepModeButtonModel
- __OBJC_CLASS_RO_$_HKSPSleepStoreCache
- __OBJC_METACLASS_RO_$_HKSPAnalyticsStore
- __OBJC_METACLASS_RO_$_HKSPAnalyticsWindDownEvent
- __OBJC_METACLASS_RO_$_HKSPAnalyticsWindDownEventData
- __OBJC_METACLASS_RO_$_HKSPAnalyticsWindDownEventDataWrapper
- __OBJC_METACLASS_RO_$_HKSPHealthStoreProvider
- __OBJC_METACLASS_RO_$_HKSPSleepModeButtonModel
- __OBJC_METACLASS_RO_$_HKSPSleepStoreCache
- ___254-[HKSPSleepStore initWithConnectionProviderProvider:identifier:healthStore:options:analyticsManager:throttlerProvider:callbackScheduler:sleepFocusModeBridgeProvider:widgetTimelineControllersProvider:widgetRelevanceControllerProvider:currentDateProvider:]_block_invoke
- ___27-[HKSPSleepStoreCache init]_block_invoke
- ___32+[HKSPSleepStoreCache weakCache]_block_invoke
- ___40-[HKSPSleepModeButtonModel setSelected:]_block_invoke
- ___40-[HKSPSleepModeButtonModel setSelected:]_block_invoke_2
- ___43-[HKSPAnalyticsStore initWithUserDefaults:]_block_invoke
- ___45-[HKSPAnalyticsManager initWithUserDefaults:]_block_invoke
- ___45-[HKSPAnalyticsManager initWithUserDefaults:]_block_invoke_2
- ___45-[HKSPAnalyticsManager initWithUserDefaults:]_block_invoke_3
- ___47-[HKSPAnalyticsStore markAllActionsAsCollected]_block_invoke
- ___48-[HKSPAnalyticsStore uncollectedWindDownActions]_block_invoke
- ___48-[HKSPSleepModeButtonModel _checkSleepModeState]_block_invoke
- ___51-[HKSPSleepStore _writeHistoricalSchedule:options:]_block_invoke
- ___54-[HKSPSleepModeButtonModel _updateStateWithSleepMode:]_block_invoke
- ___55-[HKSPAnalyticsStore windDownActionsAfterMorningIndex:]_block_invoke
- ___57-[HKSPSleepStore initWithIdentifier:healthStore:options:]_block_invoke
- ___59-[HKSPSleepStore _sendScheduleChangedAnalyticsWithContext:]_block_invoke
- ___59-[HKSPSleepStore saveCurrentSleepSchedule:options:context:]_block_invoke_2
- ___81+[HKSPSleepStore _updatedHistoricalSleepSchedulesFromSleepSchedule:options:date:]_block_invoke
- ___81+[HKSPSleepStore _updatedHistoricalSleepSchedulesFromSleepSchedule:options:date:]_block_invoke_2
- ___84-[HKSPSleepStore initWithConnectionProviderProvider:identifier:healthStore:options:]_block_invoke
- ___84-[HKSPSleepStore initWithConnectionProviderProvider:identifier:healthStore:options:]_block_invoke_2
- ___84-[HKSPSleepStore initWithConnectionProviderProvider:identifier:healthStore:options:]_block_invoke_3
- ___84-[HKSPSleepStore initWithConnectionProviderProvider:identifier:healthStore:options:]_block_invoke_4
- ___97-[HKSPSleepStore(Analytics) trackSleepDataInteractionEventWithType:isOnboardedVitals:completion:]_block_invoke
- ___block_descriptor_32_e40_16?0"HKSPAnalyticsWindDownEventData"8l
- ___block_descriptor_32_e40_B16?0"HKSPAnalyticsWindDownEventData"8l
- ___block_descriptor_32_e51_"HKSPXPCConnectionProvider"16?0"HKSPSleepStore"8l
- ___block_descriptor_32_e52_"HKSPSleepStore"24?0"NSString"8"HKHealthStore"16l
- ___block_descriptor_40_e30_B24?0"NSNumber"8"NSArray"16l
- ___block_descriptor_48_e8_32s40s_e26_"NAFuture"16?0"NSNull"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e39_v24?0"HKSPSleepSettings"8"NSError"16ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e20_v24?08"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_57_e8_32s40bs_e44_v24?0"HKSPSleepScheduleModel"8"NSError"16ls40l8s32l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- _kHKAgeGatingKeyEnableSleepTracking
- _objc_msgSend$_checkSleepModeState
- _objc_msgSend$_defaultRequirements
- _objc_msgSend$_defaultSleepTrackingRequirements
- _objc_msgSend$_initializedLocalDeviceHealthStore
- _objc_msgSend$_launchAppForOnboarding
- _objc_msgSend$_onboardSleepTrackingRequirements
- _objc_msgSend$_payloadValueForWindDownAction:
- _objc_msgSend$_queue_updateStateWithSleepMode:
- _objc_msgSend$_sendScheduleChangedAnalyticsWithContext:
- _objc_msgSend$_setWindDownActions:forMorningIndex:overwriteExisting:
- _objc_msgSend$_sleepTrackingRequirements
- _objc_msgSend$_updateStateWithSleepMode:
- _objc_msgSend$_updatedHistoricalSleepGoalForSleepSchedule:options:date:
- _objc_msgSend$_updatedHistoricalSleepSchedulesFromSleepSchedule:options:date:
- _objc_msgSend$_useSleepTrackingRequirements
- _objc_msgSend$_writeHistoricalSchedule:options:
- _objc_msgSend$analyticsManager
- _objc_msgSend$arrayByAddingObjectsFromArray:
- _objc_msgSend$canConnectToSystemMachService
- _objc_msgSend$collectedEventDataCopy
- _objc_msgSend$currentDeviceType
- _objc_msgSend$decodeArrayOfObjectsOfClass:forKey:
- _objc_msgSend$defaultIsDiagnosticDataSubmissionAllowed
- _objc_msgSend$diagnosticsOptInStatusProvider
- _objc_msgSend$eventDatums
- _objc_msgSend$healthStore
- _objc_msgSend$hksp_dataForKey:
- _objc_msgSend$indexOfObject:
- _objc_msgSend$initWithCapacity:
- _objc_msgSend$initWithConnectionProviderProvider:identifier:healthStore:options:
- _objc_msgSend$initWithConnectionProviderProvider:identifier:healthStore:options:analyticsManager:throttlerProvider:callbackScheduler:sleepFocusModeBridgeProvider:widgetTimelineControllersProvider:widgetRelevanceControllerProvider:currentDateProvider:
- _objc_msgSend$initWithEventDatums:
- _objc_msgSend$initWithSleepHealthStore:healthStore:
- _objc_msgSend$initWithSleepStore:delegate:behavior:
- _objc_msgSend$initWithSleepStoreProvider:
- _objc_msgSend$initWithSleepStoreProvider:useWeakReferences:
- _objc_msgSend$initWithUserDefaults:diagnosticsOptInStatusProvider:
- _objc_msgSend$initWithUserDefaults:ihaOptInStatusProvider:diagnosticsOptInStatusProvider:analyticsEventConsumer:
- _objc_msgSend$initWithWindDownAction:wasUsed:identifier:wasCollected:
- _objc_msgSend$interactedWithWindDownLast24Hrs
- _objc_msgSend$isDiagnosticSubmissionAllowed
- _objc_msgSend$isEqualEventData:
- _objc_msgSend$readAllWindDownActions
- _objc_msgSend$replaceObjectAtIndex:withObject:
- _objc_msgSend$setSleepModeOn:completion:
- _objc_msgSend$setSourceBundleIdentifier:
- _objc_msgSend$shareAcrossDevices
- _objc_msgSend$sharedConnection
- _objc_msgSend$sleepModeButtonModel:launchURL:
- _objc_msgSend$sleepModeButtonModelChanged:
- _objc_msgSend$sleepStoreForIdentifier:healthStore:
- _objc_msgSend$strongToStrongObjectsMapTable
- _objc_msgSend$timeInBedTracking
- _objc_msgSend$unarchivedDictionaryWithKeysOfClass:objectsOfClass:fromData:error:
- _objc_msgSend$userDefaults
- _objc_msgSend$wasCollected
- _objc_msgSend$wasUsed
- _objc_msgSend$weakCache
- _objc_msgSend$weeksSinceOnboardedWindDownActions
- _objc_msgSend$windDownActionsAfterMorningIndex:
- _objc_msgSend$writeWindDownActions:
CStrings:
+ "@\"<HKSPSleepConnectionProviding>\"16@?0@\"HKSPSleepStore\"8"
+ "Attempted to save a sleep schedule without a history writer"
+ "NO"
+ "Sleep duration goal changed"
+ "YES"
+ "[%{public}@] Failed to update historical sleep schedule record in HealthKit with error: %{public}@"
+ "[%{public}@] Updated historical sleep schedule record in HealthKit"
+ "[%{public}@] proposed wake up %{public}@, upcoming wake up %{public}@, proposed occurrence is upcoming: %{public}@"
+ "charts"
+ "sleepScoreAlgorithmVersion"
- "%@"
- "%@ - %p"
- "%{public}@ caching a new sleep store with identifier %@"
- "%{public}@ sleep duration goal changed"
- "@\"HKSPSleepStore\"24@?0@\"NSString\"8@\"HKHealthStore\"16"
- "@\"HKSPXPCConnectionProvider\"16@?0@\"HKSPSleepStore\"8"
- "@16@?0@\"HKSPAnalyticsWindDownEventData\"8"
- "AlarmSetting"
- "Attempted to save a sleep schedule without a sleep health store"
- "B16@?0@\"HKSPAnalyticsWindDownEventData\"8"
- "B24@?0@\"NSNumber\"8@\"NSArray\"16"
- "HKSPSleepStoreCache.m"
- "HomeScene"
- "LaunchApp"
- "Shortcut"
- "SleepHealthAppPlugin.SleepScoreIntroduction"
- "SleepHealthAppPlugin.SleepScoreResults"
- "SleepScoreResultsIdentifier"
- "Unabled to unarchive wind down actions with error: %{public}@"
- "WasCollected"
- "WasUsed"
- "WindDownAction"
- "WindDownEvents"
- "WindDownIdentifier"
- "[%{public}@] Cannot persist new actions"
- "[%{public}@] Failed to update current sleep schedules in HealthKit with error: %{public}@"
- "[%{public}@] Fetched current sleep settings: %@"
- "[%{public}@] No wind down actions stored in defaults"
- "[%{public}@] Reading wind down actions from defaults: %{public}@"
- "[%{public}@] Removing all wind down actions"
- "[%{public}@] Removing all wind down actions before morning index %{public}@ except for %{public}@"
- "[%{public}@] Setting baseline wind down actions for morning index %{public}@: %{public}@"
- "[%{public}@] Unable to read stored actions"
- "[%{public}@] Unabled to archive wind down actions with error: %{public}@"
- "[%{public}@] Updated current sleep schedules: %@ and sleep goal: %@ in HealthKit"
- "[%{public}@] Updating wind down actions for morning index %{public}@: %{public}@"
- "[%{public}@] Wind down actions after morning index %{public}@: %{public}@"
- "[%{public}@] Wind down actions for morning index %{public}@: %{public}@"
- "[%{public}@] Writing wind down actions to defaults: %{public}@"
- "[%{public}@] failed to get onboarding version: %{public}@"
- "[%{public}@] failed to set sleep mode: %{public}@"
- "[%{public}@] onboarding not completed"
- "[%{public}@] updating sleep mode state: %{public}@"
- "com.apple.SleepHealth.WindDownActionsEvent"
- "com.apple.private.health.localdevice"
- "identifier != nil"
- "interactedWithWindDownLast24Hrs"
- "sleepAnalyticWindDownActions"
- "sleepModeButton"
- "weeksSinceOnboardedWindDownActions"
- "windDownActionPresented"
- "windDownActionUsed"
```
