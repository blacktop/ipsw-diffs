## RespiratoryHealthDaemon

> `/System/Library/PrivateFrameworks/RespiratoryHealthDaemon.framework/RespiratoryHealthDaemon`

```diff

-6106.1.2.5.0
-  __TEXT.__text: 0x5638
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_methlist: 0x85c
-  __TEXT.__const: 0xa8
-  __TEXT.__oslogstring: 0x8af
-  __TEXT.__cstring: 0x5d9
-  __TEXT.__unwind_info: 0x1e0
-  __TEXT.__objc_classname: 0x243
-  __TEXT.__objc_methname: 0x2288
-  __TEXT.__objc_methtype: 0x61c
-  __TEXT.__objc_stubs: 0x1540
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x178
-  __DATA_CONST.__objc_classlist: 0x38
+6106.1.2.9.0
+  __TEXT.__text: 0x879c
+  __TEXT.__auth_stubs: 0x4e0
+  __TEXT.__objc_methlist: 0x914
+  __TEXT.__const: 0xb8
+  __TEXT.__oslogstring: 0xb66
+  __TEXT.__cstring: 0x88e
+  __TEXT.__gcc_except_tab: 0x27c
+  __TEXT.__unwind_info: 0x288
+  __TEXT.__objc_classname: 0x292
+  __TEXT.__objc_methname: 0x2da6
+  __TEXT.__objc_methtype: 0x84a
+  __TEXT.__objc_stubs: 0x1e40
+  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__const: 0x1c0
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x58
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x768
-  __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x228
-  __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x620
-  __AUTH_CONST.__objc_const: 0xf20
+  __DATA_CONST.__objc_selrefs: 0x9d8
+  __DATA_CONST.__objc_superrefs: 0x30
+  __AUTH_CONST.__auth_got: 0x280
+  __AUTH_CONST.__const: 0xa0
+  __AUTH_CONST.__cfstring: 0x840
+  __AUTH_CONST.__objc_const: 0x11e8
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x98
-  __DATA.__data: 0x420
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0xc4
+  __DATA.__data: 0x4e0
   __DATA_DIRTY.__objc_data: 0x140
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/HealthAlgorithms.framework/HealthAlgorithms
   - /System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon
   - /System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/RespiratoryHealth.framework/RespiratoryHealth
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 736922DB-497A-3ED0-B3B1-887DE0A34F77
-  Functions: 154
-  Symbols:   767
-  CStrings:  537
+  UUID: B8B00019-7894-37E1-B87D-C7C88461A671
+  Functions: 199
+  Symbols:   1006
+  CStrings:  688
 
Symbols:
+ -[HDRPOxygenSaturationAnalyzer .cxx_destruct]
+ -[HDRPOxygenSaturationAnalyzer _analyzeSample:transaction:error:]
+ -[HDRPOxygenSaturationAnalyzer _analyzeUnprocessedSamples]
+ -[HDRPOxygenSaturationAnalyzer _bloodOxygenAnalysisWithUnprocessedSample:]
+ -[HDRPOxygenSaturationAnalyzer _bloodOxygenSampleWithBloodOxygenMeasurement:unprocessedSample:]
+ -[HDRPOxygenSaturationAnalyzer _dataTypeDetailsRoomUrlWithSample:]
+ -[HDRPOxygenSaturationAnalyzer _deleteUnprocessedSample:error:]
+ -[HDRPOxygenSaturationAnalyzer _heartRateSampleWithBloodOxygenMeasurement:]
+ -[HDRPOxygenSaturationAnalyzer _insertAnalyzedSamplesWithBloodOxygenAnalysis:unprocessedSample:provenance:error:]
+ -[HDRPOxygenSaturationAnalyzer _insertUnsuccessfulAnalysisSampleWithUnprocessedSample:provenance:analyticsPayload:error:]
+ -[HDRPOxygenSaturationAnalyzer _postMultipleMixedResultsNotification]
+ -[HDRPOxygenSaturationAnalyzer _postMultipleSuccessfullResultsNotification:]
+ -[HDRPOxygenSaturationAnalyzer _postNotificationWithTitle:body:categoryIdentifier:subtitle:domain:url:completion:]
+ -[HDRPOxygenSaturationAnalyzer _postSingleSuccessfulResultNotification:]
+ -[HDRPOxygenSaturationAnalyzer _postSingleUnsuccessfulMeasurementNotification:]
+ -[HDRPOxygenSaturationAnalyzer _sendAnalyticEventsForAnalysisSummaryIfNeeded:]
+ -[HDRPOxygenSaturationAnalyzer _shouldAnalyzeSamples]
+ -[HDRPOxygenSaturationAnalyzer initWithProfile:oxygenSaturationFeatureStatusProvider:oxygenSaturationCompanionAnalysisFeatureStatusProvider:]
+ -[HDRPOxygenSaturationAnalyzer initWithProfile:oxygenSaturationFeatureStatusProvider:oxygenSaturationCompanionAnalysisFeatureStatusProvider:unitTestDelegate:]
+ -[HDRPOxygenSaturationAnalyzer performWorkForOperation:profile:databaseAccessibilityAssertion:completion:]
+ -[HDRPOxygenSaturationAnalyzer profileDidBecomeReady:]
+ -[HDRPOxygenSaturationAnalyzer samplesAdded:anchor:]
+ -[HDRPOxygenSaturationAnalyzer samplesAdded:anchor:].cold.1
+ -[HDRespiratoryProfileExtension initWithProfile:featureAvailabilityManager:companionAnalysisAvailabilityManager:ageGatingDefaults:]
+ GCC_except_table13
+ GCC_except_table17
+ GCC_except_table18
+ GCC_except_table28
+ GCC_except_table4
+ GCC_except_table6
+ _HDRPOxygenSaturationRecordingCompanionAnalysisFeatureAvailabilityProvider
+ _HDRPOxygenSaturationRecordingCompanionAnalysisPairedFeaturePropertiesSyncManager
+ _HKCategoryTypeIdentifierUnsuccessfulBloodOxygenSaturationAnalysisEvent
+ _HKFeatureAvailabilityContextAnalysis
+ _HKFeatureAvailabilityContextUsage
+ _HKFeatureIdentifierOxygenSaturationRecordingCompanionAnalysis
+ _HKHROxygenSaturationShowAllDataLinkUrlPathComponent
+ _HKHROxygenSaturationUnsuccessfulAnalysisEventSampleDetailsLinkUrlPathComponent
+ _HKQuantityTypeIdentifierOxygenSaturation
+ _HKRPOxygenSaturationCompanionAnalysisLocalFeatureAttributes
+ _HKRPOxygenSaturationDataTypeRoomLink
+ _HKRPOxygenSaturationRecordingCompanionAnalysisFeatureAvailabilityRequirements
+ _HKRPOxygenSaturationShowAllDataRoomLink
+ _HKRPOxygenSaturationUnsuccessfulAnalysisEventSampleDetailsLink
+ _NSStringFromClass
+ _OBJC_CLASS_$_HABloodOxygenCalculator
+ _OBJC_CLASS_$_HDBinarySampleEntity
+ _OBJC_CLASS_$_HDDataDeletionConfiguration
+ _OBJC_CLASS_$_HDProtectedDataOperation
+ _OBJC_CLASS_$_HDRPOxygenSaturationAnalyzer
+ _OBJC_CLASS_$_HDRegionAvailabilityProvider
+ _OBJC_CLASS_$_HKCategorySample
+ _OBJC_CLASS_$_HKCategoryType
+ _OBJC_CLASS_$_HKCountrySet
+ _OBJC_CLASS_$_HKFeatureStatusManager
+ _OBJC_CLASS_$_HKQuantitySample
+ _OBJC_CLASS_$_HKQuantityType
+ _OBJC_CLASS_$_HKUnprocessedBloodOxygenDataType
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_NSURLQueryItem
+ _OBJC_CLASS_$_UNMutableNotificationContent
+ _OBJC_CLASS_$_UNNotificationSound
+ _OBJC_IVAR_$_HDRPOxygenSaturationAnalyzer._lock
+ _OBJC_IVAR_$_HDRPOxygenSaturationAnalyzer._lock_shouldReRequestAnalysisWork
+ _OBJC_IVAR_$_HDRPOxygenSaturationAnalyzer._oxygenSaturationCompanionAnalysisStatusProvider
+ _OBJC_IVAR_$_HDRPOxygenSaturationAnalyzer._oxygenSaturationStatusProvider
+ _OBJC_IVAR_$_HDRPOxygenSaturationAnalyzer._profile
+ _OBJC_IVAR_$_HDRPOxygenSaturationAnalyzer._protectedDataOperation
+ _OBJC_IVAR_$_HDRPOxygenSaturationAnalyzer._unitTestDelegate
+ _OBJC_IVAR_$_HDRPOxygenSaturationAnalyzer._unprocessedSampleType
+ _OBJC_IVAR_$_HDRespiratoryProfileExtension._companionAnalysisFeatureAvailabilityManager
+ _OBJC_IVAR_$_HDRespiratoryProfileExtension._companionAnalysisFeatureStatusManager
+ _OBJC_IVAR_$_HDRespiratoryProfileExtension._oxygenSaturationAnalyzer
+ _OBJC_METACLASS_$_HDRPOxygenSaturationAnalyzer
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ __Block_object_dispose
+ __HKCreateURLForSampleType
+ __OBJC_$_INSTANCE_METHODS_HDRPOxygenSaturationAnalyzer
+ __OBJC_$_INSTANCE_VARIABLES_HDRPOxygenSaturationAnalyzer
+ __OBJC_$_PROP_LIST_HDRPOxygenSaturationAnalyzer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDDataObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDProtectedDataOperationDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HDDataObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HDDataObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HDProtectedDataOperationDelegate
+ __OBJC_$_PROTOCOL_REFS_HDDataObserver
+ __OBJC_$_PROTOCOL_REFS_HDProtectedDataOperationDelegate
+ __OBJC_CLASS_PROTOCOLS_$_HDRPOxygenSaturationAnalyzer
+ __OBJC_CLASS_RO_$_HDRPOxygenSaturationAnalyzer
+ __OBJC_LABEL_PROTOCOL_$_HDDataObserver
+ __OBJC_LABEL_PROTOCOL_$_HDProtectedDataOperationDelegate
+ __OBJC_METACLASS_RO_$_HDRPOxygenSaturationAnalyzer
+ __OBJC_PROTOCOL_$_HDDataObserver
+ __OBJC_PROTOCOL_$_HDProtectedDataOperationDelegate
+ __Unwind_Resume
+ ___58-[HDRPOxygenSaturationAnalyzer _analyzeUnprocessedSamples]_block_invoke
+ ___69-[HDRPOxygenSaturationAnalyzer _postMultipleMixedResultsNotification]_block_invoke
+ ___72-[HDRPOxygenSaturationAnalyzer _postSingleSuccessfulResultNotification:]_block_invoke
+ ___76-[HDRPOxygenSaturationAnalyzer _postMultipleSuccessfullResultsNotification:]_block_invoke
+ ___79-[HDRPOxygenSaturationAnalyzer _postSingleUnsuccessfulMeasurementNotification:]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_104_e8_32s40r48r56r64r72r80r88r96r_e35_B24?0"HDDatabaseTransaction"8^16ls32l8r40l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8
+ ___block_descriptor_32_e20_v20?0B8"NSError"12l
+ ___block_literal_global.327
+ ___block_literal_global.335
+ ___block_literal_global.349
+ ___copy_constructor_8_8_t0w24_s24_s32_s40_s48
+ ___destructor_8_s0_s16
+ ___destructor_8_s24_s32_s40_s48
+ ___kCFBooleanTrue
+ ___move_assignment_8_8_t0w24_s24_s32_s40_s48
+ ___objc_personality_v0
+ _kHKNotificationsDomainKey
+ _kHKNotificationsSuppressNotificationForwardingKey
+ _kHKNotificationsURLKey
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_msgSend$URL
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$UUID
+ _objc_msgSend$UUIDString
+ _objc_msgSend$_unitTest_didRunAnalysis:summary:
+ _objc_msgSend$absoluteString
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$addObserver:forDataType:
+ _objc_msgSend$analyzeBloodOxygenFromRawData:withPressureInKilopascals:
+ _objc_msgSend$areAllRequirementsSatisfied
+ _objc_msgSend$associateObjectUUIDs:objectUUID:error:
+ _objc_msgSend$associationManager
+ _objc_msgSend$averageHeartRate
+ _objc_msgSend$bundleForClass:
+ _objc_msgSend$categorySampleWithType:value:startDate:endDate:
+ _objc_msgSend$countUnit
+ _objc_msgSend$dataManager
+ _objc_msgSend$dataProvenanceManager
+ _objc_msgSend$database
+ _objc_msgSend$date
+ _objc_msgSend$defaultLocalDataProvenanceWithDeviceEntity:
+ _objc_msgSend$deleteObjectsWithUUIDCollection:configuration:error:
+ _objc_msgSend$device
+ _objc_msgSend$deviceEntityForDevice:error:
+ _objc_msgSend$deviceManager
+ _objc_msgSend$dictionary
+ _objc_msgSend$doubleValueForUnit:
+ _objc_msgSend$emptyCountrySet
+ _objc_msgSend$endDate
+ _objc_msgSend$featureStatusWithError:
+ _objc_msgSend$hk_isAfterDate:
+ _objc_msgSend$initWithFeatureAvailabilityProviding:healthDataSource:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$initWithProfile:debugIdentifier:delegate:
+ _objc_msgSend$initWithProfile:featureAvailabilityManager:companionAnalysisAvailabilityManager:ageGatingDefaults:
+ _objc_msgSend$initWithProfile:featureIdentifier:availabilityRequirements:currentOnboardingVersion:pairedDeviceCapability:pairedFeatureAttributesProvider:regionAvailabilityProvider:disableAndExpiryProvider:loggingCategory:
+ _objc_msgSend$initWithProfile:oxygenSaturationFeatureStatusProvider:oxygenSaturationCompanionAnalysisFeatureStatusProvider:
+ _objc_msgSend$initWithProfile:oxygenSaturationFeatureStatusProvider:oxygenSaturationCompanionAnalysisFeatureStatusProvider:unitTestDelegate:
+ _objc_msgSend$initWithURL:resolvingAgainstBaseURL:
+ _objc_msgSend$initWithUserDefaults:userDefaultsSyncProvider:companionAnalysisFeatureStatusManager:
+ _objc_msgSend$insertDataObjects:withProvenance:creationDate:skipInsertionFilter:updateSourceOrder:resolveAssociations:error:
+ _objc_msgSend$isCompanionAnalysisEnabled
+ _objc_msgSend$isOnboardingRecordPresent
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$localizedStringForKey:value:table:
+ _objc_msgSend$minuteUnit
+ _objc_msgSend$mostRecentSampleWithType:profile:encodingOptions:predicate:anchor:error:
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$notificationManager
+ _objc_msgSend$payload
+ _objc_msgSend$performWriteTransactionWithHealthDatabase:error:block:
+ _objc_msgSend$postNotificationWithIdentifier:content:trigger:completion:
+ _objc_msgSend$quantitySampleWithType:quantity:startDate:endDate:
+ _objc_msgSend$quantitySampleWithType:quantity:startDate:endDate:device:metadata:
+ _objc_msgSend$queryItemWithName:value:
+ _objc_msgSend$queryItems
+ _objc_msgSend$requestWorkWithPriority:error:
+ _objc_msgSend$setBody:
+ _objc_msgSend$setCategoryIdentifier:
+ _objc_msgSend$setFailIfNotFound:
+ _objc_msgSend$setGenerateDeletedObjects:
+ _objc_msgSend$setNotifyObservers:
+ _objc_msgSend$setQueryItems:
+ _objc_msgSend$setSound:
+ _objc_msgSend$setSubtitle:
+ _objc_msgSend$setTitle:
+ _objc_msgSend$setUserInfo:
+ _objc_msgSend$soundWithAlertType:
+ _objc_msgSend$stringValue
+ _objc_msgSend$timeIntervalSinceReferenceDate
+ _objc_msgSend$uncheckedAvailability
+ _objc_msgSend$unitDividedByUnit:
+ _objc_msgSend$unprocessedBloodOxygenDataType
+ _objc_msgSend$unsatisfiedRequirementIdentifiers
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- -[HDRespiratoryProfileExtension initWithProfile:featureAvailabilityManager:ageGatingDefaults:]
- _objc_msgSend$initWithProfile:featureAvailabilityManager:ageGatingDefaults:
- _objc_msgSend$initWithUserDefaults:userDefaultsSyncProvider:
CStrings:
+ ""
+ "198711C2-6CC8-43B9-A882-6670CC787272"
+ "2D6D2220-64DB-408A-89ED-ED05391073E8"
+ "@\"<HDRPOxygenSaturationAnalyzerUnitTestDelegate>\""
+ "@\"<HKFeatureStatusProviding>\""
+ "@\"HDProtectedDataOperation\""
+ "@\"HDRPOxygenSaturationAnalyzer\""
+ "@\"HKFeatureStatusManager\""
+ "@\"HKObjectType\""
+ "B24@?0@\"HDDatabaseTransaction\"8^@16"
+ "HDDataObserver"
+ "HDProtectedDataOperationDelegate"
+ "HDRPOxygenSaturationAnalyzer"
+ "Localizable-Windbreaker"
+ "MULTIPLE_RESULTS_AVAILABLE_NOTIFICATION_BODY"
+ "MULTIPLE_RESULTS_AVAILABLE_NOTIFICATION_TITLE"
+ "SINGLE_RESULT_AVAILABLE_NOTIFICATION_BODY"
+ "SINGLE_RESULT_AVAILABLE_NOTIFICATION_TITLE"
+ "UNSUCCESSFUL_MEASUREMENT_NOTIFICATION_BODY"
+ "UNSUCCESSFUL_MEASUREMENT_NOTIFICATION_TITLE"
+ "URL"
+ "URLWithString:"
+ "UUID"
+ "UUIDString"
+ "[%{public}@ Failed to get Oxygen Saturation feature status with error: %@]"
+ "[%{public}@ Failed to get companion analysis feature status with error: %@]"
+ "[%{public}@] Blood Oxygen Analysis is complete. %@ sample(s) processed, of them %@ is/are user initiated, and of those %@ is/are unsuccessful measurements"
+ "[%{public}@] Companion Analysis feature is not onboarded"
+ "[%{public}@] Companion Analysis in enabled"
+ "[%{public}@] Failed to analyze with error: %@"
+ "[%{public}@] Failed to request protected data operation work error: %@"
+ "[%{public}@] Oxygen Saturation analysis is not enabled, unsatisfied requirements: %@"
+ "[%{public}@] Oxygen Saturation feature is not onboarded"
+ "[%{public}@] Skipping analysis"
+ "_companionAnalysisFeatureAvailabilityManager"
+ "_companionAnalysisFeatureStatusManager"
+ "_lock"
+ "_lock_shouldReRequestAnalysisWork"
+ "_oxygenSaturationAnalyzer"
+ "_oxygenSaturationCompanionAnalysisStatusProvider"
+ "_oxygenSaturationStatusProvider"
+ "_protectedDataOperation"
+ "_unitTestDelegate"
+ "_unitTest_didRunAnalysis:summary:"
+ "_unprocessedSampleType"
+ "absoluteString"
+ "addObjectsFromArray:"
+ "addObserver:forDataType:"
+ "analyzeBloodOxygenFromRawData:withPressureInKilopascals:"
+ "areAllRequirementsSatisfied"
+ "associateObjectUUIDs:objectUUID:error:"
+ "associationManager"
+ "associationsUpdatedForObject:subObject:type:behavior:objects:anchor:"
+ "averageHeartRate"
+ "bundleForClass:"
+ "categorySampleWithType:value:startDate:endDate:"
+ "com.apple.hid.scandium.background"
+ "com.apple.hid.scandium.on_demand"
+ "com.apple.private.health.respiratory.phoneonly"
+ "countUnit"
+ "dataManager"
+ "dataProvenanceManager"
+ "database"
+ "date"
+ "defaultLocalDataProvenanceWithDeviceEntity:"
+ "deleteObjectsWithUUIDCollection:configuration:error:"
+ "device"
+ "deviceEntityForDevice:error:"
+ "deviceManager"
+ "dictionary"
+ "didAddSamplesOfTypes:anchor:"
+ "doubleValueForUnit:"
+ "emptyCountrySet"
+ "endDate"
+ "featureStatusWithError:"
+ "hk_isAfterDate:"
+ "initWithFeatureAvailabilityProviding:healthDataSource:"
+ "initWithIdentifier:"
+ "initWithProfile:debugIdentifier:delegate:"
+ "initWithProfile:featureAvailabilityManager:companionAnalysisAvailabilityManager:ageGatingDefaults:"
+ "initWithProfile:featureIdentifier:availabilityRequirements:currentOnboardingVersion:pairedDeviceCapability:pairedFeatureAttributesProvider:regionAvailabilityProvider:disableAndExpiryProvider:loggingCategory:"
+ "initWithProfile:oxygenSaturationFeatureStatusProvider:oxygenSaturationCompanionAnalysisFeatureStatusProvider:"
+ "initWithProfile:oxygenSaturationFeatureStatusProvider:oxygenSaturationCompanionAnalysisFeatureStatusProvider:unitTestDelegate:"
+ "initWithURL:resolvingAgainstBaseURL:"
+ "initWithUserDefaults:userDefaultsSyncProvider:companionAnalysisFeatureStatusManager:"
+ "insertDataObjects:withProvenance:creationDate:skipInsertionFilter:updateSourceOrder:resolveAssociations:error:"
+ "isCompanionAnalysisEnabled"
+ "isCompanionAnalysisEnabled: %@\n"
+ "isOnboardingRecordPresent"
+ "localizedDescription"
+ "localizedStringForKey:value:table:"
+ "minuteUnit"
+ "mostRecentSampleWithType:profile:encodingOptions:predicate:anchor:error:"
+ "mutableCopy"
+ "notificationManager"
+ "payload"
+ "performWorkForOperation:profile:databaseAccessibilityAssertion:completion:"
+ "performWriteTransactionWithHealthDatabase:error:block:"
+ "postNotificationWithIdentifier:content:trigger:completion:"
+ "quantitySampleWithType:quantity:startDate:endDate:"
+ "quantitySampleWithType:quantity:startDate:endDate:device:metadata:"
+ "queryItemWithName:value:"
+ "queryItems"
+ "requestWorkWithPriority:error:"
+ "samplesAdded:anchor:"
+ "samplesJournaled:type:"
+ "samplesOfTypesWereRemoved:anchor:"
+ "setBody:"
+ "setCategoryIdentifier:"
+ "setFailIfNotFound:"
+ "setGenerateDeletedObjects:"
+ "setNotifyObservers:"
+ "setQueryItems:"
+ "setSound:"
+ "setSubtitle:"
+ "setTitle:"
+ "setUserInfo:"
+ "soundWithAlertType:"
+ "stringValue"
+ "timeIntervalSinceReferenceDate"
+ "uncheckedAvailability"
+ "unitDividedByUnit:"
+ "unprocessedBloodOxygenDataType"
+ "unsatisfiedRequirementIdentifiers"
+ "v20@?0B8@\"NSError\"12"
+ "v32@0:8@\"NSArray\"16@\"HKSampleType\"24"
+ "v32@0:8@\"NSArray\"16@\"NSNumber\"24"
+ "v32@0:8@\"NSSet\"16@\"NSNumber\"24"
+ "v32@0:8@16@24"
+ "v48@0:8@\"HDProtectedDataOperation\"16@\"HDProfile\"24@\"HDAssertion\"32@?<v@?>40"
+ "v48@0:8@16@24@32@?40"
+ "v64@0:8@\"<HKAssociatableObject>\"16@\"<HKAssociatableObject>\"24Q32Q40@\"NSArray\"48@\"NSNumber\"56"
+ "v64@0:8@16@24Q32Q40@48@56"
+ "x-apple-health://RespiratoryHealthAppPlugin.healthplugin/%@"
+ "x-apple-health://RespiratoryHealthAppPlugin.healthplugin/%@/%@"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
+ "\x81"
- "initWithProfile:featureAvailabilityManager:ageGatingDefaults:"
- "initWithUserDefaults:userDefaultsSyncProvider:"

```
