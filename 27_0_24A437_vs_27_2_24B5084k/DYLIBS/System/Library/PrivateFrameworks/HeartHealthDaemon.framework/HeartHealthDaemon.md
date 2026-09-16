## HeartHealthDaemon

> `/System/Library/PrivateFrameworks/HeartHealthDaemon.framework/HeartHealthDaemon`

```diff

-7027.0.72.2.7
-  __TEXT.__text: 0x65f6c
-  __TEXT.__objc_methlist: 0x5104
-  __TEXT.__const: 0x3ca
-  __TEXT.__gcc_except_tab: 0xb4c
-  __TEXT.__cstring: 0x59e2
-  __TEXT.__oslogstring: 0xca8f
+7027.1.36.2.7
+  __TEXT.__text: 0x64e08
+  __TEXT.__objc_methlist: 0x4ee4
+  __TEXT.__const: 0x5e4
+  __TEXT.__gcc_except_tab: 0xae4
+  __TEXT.__cstring: 0x5892
+  __TEXT.__oslogstring: 0xc53e
   __TEXT.__ustring: 0x86
-  __TEXT.__swift5_typeref: 0x47
+  __TEXT.__constg_swiftt: 0xc8
+  __TEXT.__swift5_typeref: 0x99
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_reflstr: 0x3a
+  __TEXT.__swift5_fieldmd: 0x54
+  __TEXT.__swift5_assocty: 0x30
+  __TEXT.__swift5_proto: 0x24
+  __TEXT.__swift5_types: 0xc
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__constg_swiftt: 0x9c
-  __TEXT.__swift5_reflstr: 0x17
-  __TEXT.__swift5_fieldmd: 0x38
-  __TEXT.__swift5_proto: 0xc
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1fa8
-  __TEXT.__eh_frame: 0x78
+  __TEXT.__unwind_info: 0x1f88
+  __TEXT.__eh_frame: 0xc0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x19e0
+  __DATA_CONST.__const: 0x1970
   __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x270
+  __DATA_CONST.__objc_protolist: 0x2a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3610
-  __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x290
+  __DATA_CONST.__objc_selrefs: 0x3538
+  __DATA_CONST.__objc_protorefs: 0x60
+  __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x538
-  __DATA_CONST.__got: 0xee8
-  __AUTH_CONST.__const: 0x620
-  __AUTH_CONST.__cfstring: 0x4820
-  __AUTH_CONST.__objc_const: 0x9c10
-  __AUTH_CONST.__objc_intobj: 0xdc8
+  __DATA_CONST.__got: 0xef0
+  __AUTH_CONST.__const: 0x648
+  __AUTH_CONST.__cfstring: 0x4680
+  __AUTH_CONST.__objc_const: 0x9a28
+  __AUTH_CONST.__objc_intobj: 0xdb0
   __AUTH_CONST.__objc_doubleobj: 0x3d0
   __AUTH_CONST.__objc_arrayobj: 0x138
-  __AUTH_CONST.__auth_got: 0x8a0
+  __AUTH_CONST.__auth_got: 0x960
   __AUTH.__objc_data: 0x868
-  __DATA.__objc_ivar: 0x64c
-  __DATA.__data: 0x1d60
+  __DATA.__objc_ivar: 0x618
+  __DATA.__data: 0x1eb0
   __DATA_DIRTY.__objc_data: 0x1690
   __DATA_DIRTY.__data: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/HeartHealth.framework/HeartHealth
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2153
-  Symbols:   5582
-  CStrings:  1365
+  Functions: 2145
+  Symbols:   5509
+  CStrings:  1332
 
Symbols:
+ -[HDHRHypertensionMeasurementAnalyzer sendAnalyticsEventWithDateInterval:additionalPayload:]
+ -[HDHRHypertensionNotificationManager _sendAnalyticsEventWithType:algorithmVersion:]
+ -[HDHRHypertensionNotificationsRescindedAlertManager _sendAnalyticsEventWithType:]
+ -[HDHRIrregularRhythmNotificationsV1FeatureAvailabilityManager _onboardedCountryCodeSupportedStateWithError:]
+ -[HDHeartbeatSeriesFeatureStatusManager initWithDatabase:aFibBurdenFeatureStatusManager:irregularRhythmNotificationsFeatureStatusManager:]
+ GCC_except_table21
+ _HKBloodPressureClassificationCategoryAHASevereHypertension
+ _OBJC_CLASS_$_HDHRHypertensionNotificationsAnalyticsUtilities
+ _OBJC_IVAR_$_HDHeartbeatSeriesFeatureStatusManager._database
+ _OBJC_METACLASS_$_HDHRHypertensionNotificationsAnalyticsUtilities
+ __CATEGORY_HKFeatureAvailabilityRequirementSet_$_HeartHealthDaemon
+ __HDIsUnitTesting
+ __OBJC_$_CLASS_METHODS_HKFeatureAvailabilityRequirementSet(HeartHealthDaemon|HeartHealthDaemon1|HeartHealthDaemon2)
+ __OBJC_$_CLASS_PROP_LIST_HKFeatureAvailabilityRequirement
+ __OBJC_$_PROP_LIST_HKFeatureAvailabilityRequirement
+ __OBJC_$_PROTOCOL_CLASS_METHODS_HKFeatureAvailabilityRequirement
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKFeatureAvailabilityRequirement
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKFeatureAvailabilityRequirementsProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKFeatureAvailabilityRequirement
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKFeatureAvailabilityRequirementsProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_$_PROTOCOL_REFS_HKFeatureAvailabilityRequirement
+ __OBJC_CLASS_RO_$_HDHRHypertensionNotificationsAnalyticsUtilities
+ __OBJC_LABEL_PROTOCOL_$_HKFeatureAvailabilityRequirement
+ __OBJC_LABEL_PROTOCOL_$_HKFeatureAvailabilityRequirementsProviding
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_METACLASS_RO_$_HDHRHypertensionNotificationsAnalyticsUtilities
+ __OBJC_PROTOCOL_$_HKFeatureAvailabilityRequirement
+ __OBJC_PROTOCOL_$_HKFeatureAvailabilityRequirementsProviding
+ __OBJC_PROTOCOL_$_NSCopying
+ ___104-[HDHRHypertensionNotificationsRescindedAlertManager _unitTesting_callNotificationNotPostedHandlerIfSet]_block_invoke
+ __swiftEmptyArrayStorage
+ _associated conformance So28HKFeatureAvailabilityContextaSHSCSQ
+ _associated conformance So28HKFeatureAvailabilityContextas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So28HKFeatureAvailabilityContextas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _objc_msgSend$_onboardedCountryCodeSupportedStateWithError:
+ _objc_msgSend$_sendAnalyticsEventWithType:
+ _objc_msgSend$hkhr_bloodPressureJournalRequirementSet
+ _objc_msgSend$hkhr_heartRateNotificationsRequirementSetForFeatureWithIdentifier:
+ _objc_msgSend$hkhr_irregularRhythmNotificationsV2RequirementSet
+ _objc_msgSend$initWithDatabase:aFibBurdenFeatureStatusManager:irregularRhythmNotificationsFeatureStatusManager:
+ _objc_retain_x9
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_bridgeObjectRelease_n
+ _swift_dynamicCastMetatype
+ _swift_dynamicCastObjCProtocolConditional
+ _swift_getExistentialTypeMetadata
+ _swift_getForeignTypeMetadata
+ _swift_getTupleTypeMetadata2
+ _swift_initStackObject
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
+ _swift_release_x19
+ _swift_setDeallocating
+ _symbolic $sSY
+ _symbolic $ss21_ObjectiveCBridgeableP
+ _symbolic SS
+ _symbolic So8NSStringC
+ _symbolic _____ So28HKFeatureAvailabilityContexta
+ _type_layout_string So28HKFeatureAvailabilityContexta
- +[HKFeatureAvailabilityRequirementSet(BPJ) bloodPressureJournalFeatureAvailabilityRequirementSet]
- -[HDHRElectrocardiogramRecordingCommonFeatureAvailabilityManager earliestDateLowestOnboardingVersionCompletedWithError:]
- -[HDHRElectrocardiogramRecordingCommonFeatureAvailabilityManager isCurrentOnboardingVersionCompletedWithCompletion:]
- -[HDHRElectrocardiogramRecordingCommonFeatureAvailabilityManager isCurrentOnboardingVersionCompletedWithError:]
- -[HDHRElectrocardiogramRecordingCommonFeatureAvailabilityManager onboardedCountryCodeSupportedStateWithError:]
- -[HDHRElectrocardiogramRecordingFeatureAvailabilityManager earliestDateLowestOnboardingVersionCompletedWithError:]
- -[HDHRElectrocardiogramRecordingFeatureAvailabilityManager isCurrentOnboardingVersionCompletedWithCompletion:]
- -[HDHRElectrocardiogramRecordingFeatureAvailabilityManager isCurrentOnboardingVersionCompletedWithError:]
- -[HDHRElectrocardiogramRecordingFeatureAvailabilityManager onboardedCountryCodeSupportedStateWithError:]
- -[HDHRHealthLiteDataCollector .cxx_destruct]
- -[HDHRHealthLiteDataCollector _queue_createHealthLiteManager]
- -[HDHRHealthLiteDataCollector _queue_handleBradycardiaEventWithDateInterval:threshold:heartRateUUIDs:]
- -[HDHRHealthLiteDataCollector _queue_handleTachycardiaEventWithDateInterval:threshold:heartRateUUIDs:]
- -[HDHRHealthLiteDataCollector _queue_privacyPreferencesDidChange]
- -[HDHRHealthLiteDataCollector _queue_updateAllCollectionTypes]
- -[HDHRHealthLiteDataCollector _queue_updateBradycardiaCollectionType]
- -[HDHRHealthLiteDataCollector _queue_updateTachycardiaCollectionType]
- -[HDHRHealthLiteDataCollector _registerPowerLogEvent:]
- -[HDHRHealthLiteDataCollector beginCollectionForDataAggregator:lastPersistedSensorDatum:]
- -[HDHRHealthLiteDataCollector daemonReady:]
- -[HDHRHealthLiteDataCollector dataAggregator:wantsCollectionWithConfiguration:]
- -[HDHRHealthLiteDataCollector dealloc]
- -[HDHRHealthLiteDataCollector deviceForDataAggregator:]
- -[HDHRHealthLiteDataCollector diagnosticDescription]
- -[HDHRHealthLiteDataCollector identifierForDataAggregator:]
- -[HDHRHealthLiteDataCollector initWithProfile:]
- -[HDHRHealthLiteDataCollector sourceForDataAggregator:]
- -[HDHRHeartRateNotificationsFeatureAvailabilityManager earliestDateLowestOnboardingVersionCompletedWithError:]
- -[HDHRHeartRateNotificationsFeatureAvailabilityManager isCurrentOnboardingVersionCompletedWithCompletion:]
- -[HDHRHeartRateNotificationsFeatureAvailabilityManager isCurrentOnboardingVersionCompletedWithError:]
- -[HDHRHeartRateNotificationsFeatureAvailabilityManager onboardedCountryCodeSupportedStateWithError:]
- -[HDHRHypertensionNotificationsFeatureAvailabilityManager earliestDateLowestOnboardingVersionCompletedWithError:]
- -[HDHRHypertensionNotificationsFeatureAvailabilityManager isCurrentOnboardingVersionCompletedWithCompletion:]
- -[HDHRHypertensionNotificationsFeatureAvailabilityManager isCurrentOnboardingVersionCompletedWithError:]
- -[HDHRHypertensionNotificationsFeatureAvailabilityManager onboardedCountryCodeSupportedStateWithError:]
- -[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager earliestDateLowestOnboardingVersionCompletedWithError:]
- -[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager isCurrentOnboardingVersionCompletedWithCompletion:]
- -[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager isCurrentOnboardingVersionCompletedWithError:]
- -[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager onboardedCountryCodeSupportedStateWithError:]
- -[HDHRIrregularRhythmNotificationsV1FeatureAvailabilityManager earliestDateLowestOnboardingVersionCompletedWithError:]
- -[HDHRIrregularRhythmNotificationsV1FeatureAvailabilityManager isCurrentOnboardingVersionCompletedWithCompletion:]
- -[HDHRIrregularRhythmNotificationsV1FeatureAvailabilityManager isCurrentOnboardingVersionCompletedWithError:]
- -[HDHRIrregularRhythmNotificationsV1FeatureAvailabilityManager onboardedCountryCodeSupportedStateWithError:]
- -[HDHeartProfileExtension healthLiteDataCollector]
- -[HDHeartProfileExtension setHealthLiteDataCollector:]
- -[HDHeartbeatSeriesFeatureStatusManager initWithProfile:aFibBurdenFeatureStatusManager:irregularRhythmNotificationsFeatureStatusManager:heartNotificationsUserDefaults:]
- GCC_except_table18
- GCC_except_table22
- GCC_except_table26
- GCC_except_table29
- GCC_except_table30
- GCC_except_table34
- _HKBloodPressureClassificationCategoryAHAHypertensiveCrisis
- _HKDataCollectionTypeToString
- _HKIsHeartRateEnabled
- _OBJC_CLASS_$_HDHRHealthLiteDataCollector
- _OBJC_CLASS_$_HDHeartEventSensorDatum
- _OBJC_CLASS_$_HKDataCollectorState
- _OBJC_CLASS_$_HKSource
- _OBJC_IVAR_$_HDHRHealthLiteDataCollector._bradycardiaAggregator
- _OBJC_IVAR_$_HDHRHealthLiteDataCollector._bradycardiaCollectionConfiguration
- _OBJC_IVAR_$_HDHRHealthLiteDataCollector._bradycardiaCollectionState
- _OBJC_IVAR_$_HDHRHealthLiteDataCollector._heartRateEnabledInPrivacy
- _OBJC_IVAR_$_HDHRHealthLiteDataCollector._localDeviceEntity
- _OBJC_IVAR_$_HDHRHealthLiteDataCollector._privacyPreferencesNotificationToken
- _OBJC_IVAR_$_HDHRHealthLiteDataCollector._profile
- _OBJC_IVAR_$_HDHRHealthLiteDataCollector._queue
- _OBJC_IVAR_$_HDHRHealthLiteDataCollector._tachycardiaAggregator
- _OBJC_IVAR_$_HDHRHealthLiteDataCollector._tachycardiaCollectionConfiguration
- _OBJC_IVAR_$_HDHRHealthLiteDataCollector._tachycardiaCollectionState
- _OBJC_IVAR_$_HDHeartProfileExtension._healthLiteDataCollector
- _OBJC_IVAR_$_HDHeartbeatSeriesFeatureStatusManager._heartNotificationsUserDefaults
- _OBJC_IVAR_$_HDHeartbeatSeriesFeatureStatusManager._profile
- _OBJC_METACLASS_$_HDHRHealthLiteDataCollector
- _OUTLINED_FUNCTION_8
- __OBJC_$_CATEGORY_CLASS_METHODS_HKFeatureAvailabilityRequirementSet_$_BPJ
- __OBJC_$_CATEGORY_HKFeatureAvailabilityRequirementSet_$_BPJ
- __OBJC_$_INSTANCE_METHODS_HDHRHealthLiteDataCollector
- __OBJC_$_INSTANCE_VARIABLES_HDHRHealthLiteDataCollector
- __OBJC_$_PROP_LIST_HDHRHealthLiteDataCollector
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDDataCollector
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HDDataCollector
- __OBJC_$_PROTOCOL_METHOD_TYPES_HDDataCollector
- __OBJC_$_PROTOCOL_REFS_HDDataCollector
- __OBJC_CLASS_PROTOCOLS_$_HDHRHealthLiteDataCollector
- __OBJC_CLASS_RO_$_HDHRHealthLiteDataCollector
- __OBJC_LABEL_PROTOCOL_$_HDDataCollector
- __OBJC_METACLASS_RO_$_HDHRHealthLiteDataCollector
- __OBJC_PROTOCOL_$_HDDataCollector
- __OBJC_PROTOCOL_REFERENCE_$_HDHRHeartNotificationsUserDefaultsProviding
- ___110-[HDHRElectrocardiogramRecordingFeatureAvailabilityManager isCurrentOnboardingVersionCompletedWithCompletion:]_block_invoke
- ___110-[HDHRElectrocardiogramRecordingFeatureAvailabilityManager isCurrentOnboardingVersionCompletedWithCompletion:]_block_invoke_2
- ___110-[HDHRElectrocardiogramRecordingFeatureAvailabilityManager isCurrentOnboardingVersionCompletedWithCompletion:]_block_invoke_3
- ___112-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager isCurrentOnboardingVersionCompletedWithCompletion:]_block_invoke
- ___112-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager isCurrentOnboardingVersionCompletedWithCompletion:]_block_invoke_2
- ___112-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager isCurrentOnboardingVersionCompletedWithCompletion:]_block_invoke_3
- ___38-[HDHRHealthLiteDataCollector dealloc]_block_invoke
- ___43-[HDHRHealthLiteDataCollector daemonReady:]_block_invoke
- ___47-[HDHRHealthLiteDataCollector initWithProfile:]_block_invoke
- ___79-[HDHRHealthLiteDataCollector dataAggregator:wantsCollectionWithConfiguration:]_block_invoke
- ___block_descriptor_56_e8_32s40r48r_e30_v24?0"NSNumber"8"NSError"16lr40l8r48l8s32l8
- _kHKNanoLifestylePrivacyPreferencesChangedNotification
- _kHLPowerLogActionConnected
- _kHLPowerLogActionDisconnected
- _kHLPowerLogActionKey
- _kHLPowerLogActionStartActive
- _kHLPowerLogActionStartPassive
- _kHLPowerLogActionStopUpdates
- _kHLPowerLogBundleIdentifierKey
- _kHLPowerLogEvent
- _kHLPowerLogPIDKey
- _objc_msgSend$_localDeviceSource
- _objc_msgSend$_queue_createHealthLiteManager
- _objc_msgSend$_queue_privacyPreferencesDidChange
- _objc_msgSend$_queue_updateAllCollectionTypes
- _objc_msgSend$_queue_updateBradycardiaCollectionType
- _objc_msgSend$_queue_updateTachycardiaCollectionType
- _objc_msgSend$aggregatorForType:
- _objc_msgSend$bloodPressureJournalFeatureAvailabilityRequirementSet
- _objc_msgSend$cloneWithNewType:
- _objc_msgSend$collectionType
- _objc_msgSend$dataCollectionManager
- _objc_msgSend$dataCollector:didChangeState:
- _objc_msgSend$dataCollector:didCollectSensorData:device:options:
- _objc_msgSend$earliestDateLowestOnboardingVersionCompletedWithError:
- _objc_msgSend$heartNotificationsUserDefaults
- _objc_msgSend$initWithFeatureAvailabilityProviding:healthDataSource:countryCodeSource:
- _objc_msgSend$initWithIdentifier:dateInterval:heartRateThreshold:associatedSampleUUIDs:resumeContext:
- _objc_msgSend$initWithProfile:aFibBurdenFeatureStatusManager:irregularRhythmNotificationsFeatureStatusManager:heartNotificationsUserDefaults:
- _objc_msgSend$isCurrentOnboardingVersionCompletedWithCompletion:
- _objc_msgSend$isCurrentOnboardingVersionCompletedWithError:
- _objc_msgSend$onboardedCountryCodeSupportedStateWithError:
- _objc_msgSend$registerDataCollector:state:
- _objc_msgSend$unregisterDataCollector:
CStrings:
+ "Initial v2"
+ "Repeat v2"
- "\nHeart enabled in privacy: %@\nTachycardia Collection: %@\nBradycardia Collection: %@"
- "$"
- "%{public}@ persisting bradycardia event with date interval %{public}@"
- "%{public}@ persisting tachycardia event with date interval %{public}@"
- "Error checking onboarded country code supported state for IRN 1.0, returning supported state for 2.0: %{public}@"
- "Error checking onboarded country code supported state for IRN 2.0, returning supported state for 1.0: %{public}@"
- "HDHRHealthLiteDataCollector"
- "HDHRHealthLiteDataCollector.m"
- "Initial"
- "PowerLog %@: %@"
- "Profile extension that provides heart defaults must be installed"
- "Repeat"
- "[%{public}@] Database is inaccessible; can't read ECG onboarding completion"
- "[%{public}@] Error checking onboarded country code supported state for Hypertension Notifications 1.0, returning supported state for 2.0: %{public}@"
- "[%{public}@] Error checking onboarded country code supported state for Hypertension Notifications 2.0, returning supported state for 1.0: %{public}@"
- "[%{public}@] Error reading ECG onboarding completion: %{public}@"
- "[%{public}@] Failed to retrieve lowest onboarding version completed with the 1.0 extension: %{public}@"
- "[%{public}@] Failed to retrieve lowest onboarding version completed with the 2.0 extension: %{public}@"
- "[%{public}@] Predominant feature is IRN"
- "aggregator %{public}@ wants collection with configuration: %{public}@"
- "bradycardia collection transitioning from %{public}@ to %{public}@"
- "bundleid"
- "client_connected"
- "client_disconnected"
- "disabled"
- "enabled"
- "healthlite_event"
- "heart rate collection is disabled due to privacy"
- "heart rate privacy setting changed to %s"
- "pid"
- "profile != nil"
- "start_active"
- "start_passive"
- "stop_updates"
- "tachycardia collection transitioning from %{public}@ to %{public}@"
```
