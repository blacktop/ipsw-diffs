## RespiratoryHealthDaemon

> `/System/Library/PrivateFrameworks/RespiratoryHealthDaemon.framework/RespiratoryHealthDaemon`

```diff

-6200.6.8.2.1
-  __TEXT.__text: 0x865c
-  __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_methlist: 0x8f4
+7027.0.52.2.6
+  __TEXT.__text: 0x80ec
+  __TEXT.__objc_methlist: 0x954
   __TEXT.__const: 0xb0
-  __TEXT.__gcc_except_tab: 0x258
-  __TEXT.__cstring: 0x88e
-  __TEXT.__oslogstring: 0xa10
-  __TEXT.__unwind_info: 0x2a8
-  __TEXT.__objc_classname: 0x292
-  __TEXT.__objc_methname: 0x2c9e
-  __TEXT.__objc_methtype: 0x82e
-  __TEXT.__objc_stubs: 0x1d80
-  __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0x198
-  __DATA_CONST.__objc_classlist: 0x40
+  __TEXT.__gcc_except_tab: 0x23c
+  __TEXT.__cstring: 0x8a9
+  __TEXT.__oslogstring: 0xa8a
+  __TEXT.__unwind_info: 0x288
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x1c0
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x68
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9a0
-  __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x240
+  __DATA_CONST.__objc_selrefs: 0x9e0
+  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__got: 0x2b8
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x840
-  __AUTH_CONST.__objc_const: 0x11b0
+  __AUTH_CONST.__objc_const: 0x1328
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0xbc
-  __DATA.__data: 0x4e0
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0xc8
+  __DATA.__data: 0x540
   __DATA_DIRTY.__objc_data: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/RespiratoryHealth.framework/RespiratoryHealth
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8AA392FC-3890-3040-B0F7-2DD6DD81034B
-  Functions: 200
-  Symbols:   990
-  CStrings:  674
+  UUID: CF371DE5-1FFB-3D66-B064-AC479CC03E60
+  Functions: 209
+  Symbols:   1040
+  CStrings:  179
 
Symbols:
+ -[HDRPOxygenSaturationAnalysisEvent .cxx_destruct]
+ -[HDRPOxygenSaturationAnalysisEvent eventName]
+ -[HDRPOxygenSaturationAnalysisEvent initWithPrefilteredEventPayload:isForeground:]
+ -[HDRPOxygenSaturationAnalysisEvent isEventSubmissionIHAGated]
+ -[HDRPOxygenSaturationAnalysisEvent makeIHAGatedEventPayloadWithDataSource:error:]
+ -[HDRPOxygenSaturationAnalysisEvent makeUnrestrictedEventPayloadWithDataSource:error:]
+ -[HDRPOxygenSaturationAnalyzer initWithProfile:oxygenSaturationFeatureStatusProvider:oxygenSaturationCompanionAnalysisFeatureStatusProvider:analyticsEventSubmissionManager:unitTestDelegate:]
+ GCC_except_table19
+ GCC_except_table20
+ GCC_except_table30
+ _HKAnalyticsPropertyNameActiveWatchBuildVersion
+ _HKAnalyticsPropertyNameActiveWatchProductType
+ _OBJC_CLASS_$_HDRPOxygenSaturationAnalysisEvent
+ _OBJC_CLASS_$_HKAnalyticsEventSubmissionManager
+ _OBJC_IVAR_$_HDRPOxygenSaturationAnalysisEvent._isForeground
+ _OBJC_IVAR_$_HDRPOxygenSaturationAnalysisEvent._preFilteredEventPayload
+ _OBJC_IVAR_$_HDRPOxygenSaturationAnalyzer._analyticsEventSubmissionManager
+ _OBJC_METACLASS_$_HDRPOxygenSaturationAnalysisEvent
+ _OUTLINED_FUNCTION_11
+ __OBJC_$_INSTANCE_METHODS_HDRPOxygenSaturationAnalysisEvent
+ __OBJC_$_INSTANCE_VARIABLES_HDRPOxygenSaturationAnalysisEvent
+ __OBJC_$_PROP_LIST_HDRPOxygenSaturationAnalysisEvent
+ __OBJC_$_PROP_LIST_HKAnalyticsEvent
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKAnalyticsEvent
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKAnalyticsEvent
+ __OBJC_CLASS_PROTOCOLS_$_HDRPOxygenSaturationAnalysisEvent
+ __OBJC_CLASS_RO_$_HDRPOxygenSaturationAnalysisEvent
+ __OBJC_LABEL_PROTOCOL_$_HKAnalyticsEvent
+ __OBJC_METACLASS_RO_$_HDRPOxygenSaturationAnalysisEvent
+ __OBJC_PROTOCOL_$_HKAnalyticsEvent
+ ___78-[HDRPOxygenSaturationAnalyzer _sendAnalyticEventsForAnalysisSummaryIfNeeded:]_block_invoke
+ ___78-[HDRPOxygenSaturationAnalyzer _sendAnalyticEventsForAnalysisSummaryIfNeeded:]_block_invoke.373
+ ___78-[HDRPOxygenSaturationAnalyzer _sendAnalyticEventsForAnalysisSummaryIfNeeded:]_block_invoke.373.cold.1
+ ___78-[HDRPOxygenSaturationAnalyzer _sendAnalyticEventsForAnalysisSummaryIfNeeded:]_block_invoke.cold.1
+ ___block_descriptor_40_e8_32s_e20_v20?0B8"NSError"12ls32l8
+ ___block_literal_global.393
+ ___block_literal_global.401
+ ___block_literal_global.415
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$activePairedDeviceOSBuildNumber
+ _objc_msgSend$activePairedDeviceProductType
+ _objc_msgSend$environmentDataSource
+ _objc_msgSend$initWithLoggingCategory:healthDataSource:
+ _objc_msgSend$initWithPrefilteredEventPayload:isForeground:
+ _objc_msgSend$initWithProfile:featureIdentifier:availabilityRequirements:currentOnboardingVersion:pairedDeviceCapability:pairedFeatureAttributesProvider:regionAvailabilityProvider:disableAndExpiryProvider:onboardingRecordConfiguration:loggingCategory:
+ _objc_msgSend$initWithProfile:oxygenSaturationFeatureStatusProvider:oxygenSaturationCompanionAnalysisFeatureStatusProvider:analyticsEventSubmissionManager:unitTestDelegate:
+ _objc_msgSend$submitEvent:completion:
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x8
- -[HDRPOxygenSaturationAnalyzer initWithProfile:oxygenSaturationFeatureStatusProvider:oxygenSaturationCompanionAnalysisFeatureStatusProvider:unitTestDelegate:]
- -[HDRespiratoryProfileExtension featureAvailabilityExtensionDidUpdatePairedDeviceCapability:]
- GCC_except_table17
- GCC_except_table18
- GCC_except_table28
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HDFeatureAvailabilityExtensionObserver
- ___block_literal_global.375
- ___block_literal_global.383
- ___block_literal_global.397
- _objc_msgSend$analyzeSampleResultForSample:
- _objc_msgSend$initWithProfile:featureIdentifier:availabilityRequirements:currentOnboardingVersion:pairedDeviceCapability:pairedFeatureAttributesProvider:regionAvailabilityProvider:disableAndExpiryProvider:loggingCategory:
- _objc_msgSend$initWithProfile:oxygenSaturationFeatureStatusProvider:oxygenSaturationCompanionAnalysisFeatureStatusProvider:unitTestDelegate:
- _objc_opt_respondsToSelector
CStrings:
+ "[%{public}@] Failed to submit background analytics event: %@"
+ "[%{public}@] Failed to submit foreground analytics event: %@"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<HDFeatureAvailabilityExtension>\""
- "@\"<HDFeatureAvailabilityExtension>\"24@0:8@\"NSString\"16"
- "@\"<HDRPOxygenSaturationAnalyzerUnitTestDelegate>\""
- "@\"<HKFeatureAvailabilityProviding>\""
- "@\"<HKFeatureStatusProviding>\""
- "@\"<HLOxygenSaturationSessionDelegate>\""
- "@\"HDBackgroundFeatureDeliveryManager\""
- "@\"HDProfile\""
- "@\"HDProtectedDataOperation\""
- "@\"HDRPOxygenSaturationAnalyzer\""
- "@\"HDRPRespiratoryDailyAnalytics\""
- "@\"HKFeatureStatusManager\""
- "@\"HKObjectType\""
- "@\"HKRPOxygenSaturationSettings\""
- "@\"HLHeartRateData\""
- "@\"HLOxygenSaturationSession\""
- "@\"NRPairedDeviceRegistry\""
- "@\"NSCalendar\""
- "@\"NSDate\""
- "@\"NSDateInterval\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@\"NSUUID\""
- "@\"NSUserDefaults\""
- "@\"NSXPCListenerEndpoint\"32@0:8@\"HDXPCClient\"16^@24"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@32@0:8Q16^@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24^@32"
- "@48@0:8@16@24@32@40"
- "@56@0:8@16@24@32@40^@48"
- "@68@0:8@16@24@32@40@48@56B64"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "HDAnalyticsSubmissionCoordinatorDelegate"
- "HDDataObserver"
- "HDDiagnosticObject"
- "HDFeatureAvailabilityExtensionObserver"
- "HDFeatureAvailabilityExtensionProvider"
- "HDHealthDaemonReadyObserver"
- "HDProfileExtension"
- "HDProfileReadyObserver"
- "HDProtectedDataOperationDelegate"
- "HDRPDailyAnalyticsReport"
- "HDRPOxygenSaturationAnalyzer"
- "HDRPOxygenSaturationSessionServer"
- "HDRPRespiratoryDailyAnalytics"
- "HKFeatureAvailabilityProvidingObserver"
- "HKRPOxygenSaturationSessionServerInterface"
- "HLHeartRateData"
- "HLOxygenSaturationMeasurement"
- "HLOxygenSaturationSession"
- "HLOxygenSaturationSessionDelegate"
- "NSObject"
- "Q"
- "Q16@0:8"
- "RespiratoryHealthDaemonPlugin"
- "T#,R"
- "T@\"<HDFeatureAvailabilityExtension>\",&,N,V_featureAvailabilityManager"
- "T@\"<HKFeatureAvailabilityProviding>\",R,N,V_featureAvailabilityProvider"
- "T@\"<HLOxygenSaturationSessionDelegate>\",W,N,V_delegate"
- "T@\"HDProfile\",R,W,N,V_profile"
- "T@\"HDRPRespiratoryDailyAnalytics\",R,N,V_dailyAnalytics"
- "T@\"HDRespiratoryProfileExtension\",R,N"
- "T@\"HKRPOxygenSaturationSettings\",R,N,V_oxygenSaturationSettings"
- "T@\"HLHeartRateData\",&,N,V_averageHeartRateData"
- "T@\"HLOxygenSaturationSession\",&,N,V_sensorSession"
- "T@\"NRPairedDeviceRegistry\",R,N,V_pairedDeviceRegistry"
- "T@\"NSCalendar\",R,N,V_calendar"
- "T@\"NSDate\",&,N,V_expectedEndDate"
- "T@\"NSDate\",R,N,V_endTime"
- "T@\"NSDate\",R,N,V_startTime"
- "T@\"NSDate\",R,V_timestamp"
- "T@\"NSDateInterval\",&,N,V_dateInterval"
- "T@\"NSNumber\",&,N,V_oxygenSaturationPercentage"
- "T@\"NSNumber\",&,N,V_pressureInKilopascals"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSUUID\",&,N,V_uuid"
- "T@\"NSUserDefaults\",R,N,V_controlCenterUserDefaults"
- "T@?,C,N,V_unitTesting_healthLiteSessionWithDelegateHandler"
- "TB,R,N,GisHealthDataCollectionAllowed,V_healthDataCollectionAllowed"
- "TQ,R"
- "TQ,R,V_confidenceLevel"
- "Td,N,V_expectedDuration"
- "Td,N,V_heartRate"
- "Td,N,V_startTime"
- "Td,R,V_confidence"
- "Ti,R,V_context"
- "Tq,N,V_sessionState"
- "URL"
- "URLWithString:"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_activePairedWatchBuild"
- "_ageGatingDefaults"
- "_averageHeartRateData"
- "_calendar"
- "_companionAnalysisFeatureAvailabilityManager"
- "_companionAnalysisFeatureStatusManager"
- "_confidence"
- "_confidenceLevel"
- "_context"
- "_controlCenterUserDefaults"
- "_countPerMinuteUnit"
- "_dailyAnalytics"
- "_dateInterval"
- "_dateIntervalForPreviousDays:"
- "_delegate"
- "_endTime"
- "_expectedDuration"
- "_expectedEndDate"
- "_featureAvailabilityManager"
- "_featureAvailabilityProvider"
- "_featureDeliveryManager"
- "_gatherAndSendDailyAnalyticsAndReturnError:"
- "_gatherDiagnosticAndUsageReportFromBackgroundOxygenSaturationSamplesInPreviousDay:wasWorn:error:"
- "_gatherImproveHealthAndActivityReportFromBackgroundOxygenSaturationSamplesInPreviousDay:backgroundSamplesInPrevious30Days:oxygenSaturationSamplesInPreviousDay:oxygenSaturationSamplesInPrevious30Days:error:"
- "_hasCompatiblePairedAppleWatch"
- "_healthDataCollectionAllowed"
- "_heartRate"
- "_numberOfEveningSamplesFromSamples:"
- "_numberOfForegroundSamplesFromSamples:"
- "_numberOfSamplesByTruncatedOxygenSaturationValueFromSamples:keyPrefix:"
- "_numberOfSamplesWithExerciseMinute5MinutesPriorInPreviousDayAndReturnError:"
- "_numberOfSamplesWithHeartRateGreaterThan100BPMFromSamples:"
- "_numberOfSamplesWithHighElevationTakeFromSamples:"
- "_numberOfWeeksSinceOnboardedAndReturnError:"
- "_oxygenSaturationAnalyzer"
- "_oxygenSaturationCompanionAnalysisStatusProvider"
- "_oxygenSaturationPercentage"
- "_oxygenSaturationSettings"
- "_oxygenSaturationStatusProvider"
- "_pairedDeviceRegistry"
- "_pressureInKilopascals"
- "_profile"
- "_protectedDataOperation"
- "_queryForBackgroundOxygenSaturationSamplesInPreviousDays:error:"
- "_queryForHasWornWatchInPreviousDayAndReturnError:"
- "_queryForOxygenSaturationSamplesInPreviousDays:error:"
- "_queue"
- "_queue_abortSensorSession"
- "_queue_abortWithCompletion:"
- "_queue_notifyClientDidEndWithReason:saturation:barometricPressure:averageHeartRate:averageHeartRateUUID:error:"
- "_queue_notifyClientDidSendFeedback:"
- "_queue_notifyClientDidStartWithStartTime:expectedDuration:"
- "_queue_startWithCompletion:"
- "_sensorSession"
- "_sessionState"
- "_settings"
- "_settingsWithProfile:"
- "_setupOrResetSettingsIfNeededWithFeatureAvailabilityManager:"
- "_setupSettingsWithProfile:"
- "_startTime"
- "_timestamp"
- "_unitTestDelegate"
- "_unitTest_didRunAnalysis:summary:"
- "_unitTesting_healthLiteSessionWithDelegateHandler"
- "_unprocessedSampleType"
- "_uuid"
- "_value"
- "abort"
- "absoluteString"
- "activateDefaultValuesIfNeeded"
- "addEntriesFromDictionary:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:forDataType:"
- "addObserver:queue:"
- "allKeys"
- "allowedCountrySet"
- "analyticsSubmissionCoordinator"
- "analyzeBloodOxygenFromRawData:withPressureInKilopascals:"
- "analyzeSampleResultForSample:"
- "appendFormat:"
- "areAllRequirementsSatisfied"
- "arrayWithObjects:count:"
- "associateObjectUUIDs:objectUUID:error:"
- "associationManager"
- "associationsUpdatedForObject:subObject:type:behavior:objects:anchor:"
- "autorelease"
- "averageHeartRate"
- "averageHeartRateData"
- "backgroundRecordingsDuringSleepMode"
- "backgroundRecordingsDuringTheaterMode"
- "backgroundRecordingsEnabled"
- "begin"
- "boolForKey:"
- "bundleForClass:"
- "bundleIdentifier"
- "calendar"
- "categorySampleWithType:value:startDate:endDate:"
- "class"
- "clientInterface"
- "clientRemote_didEndWithReason:saturation:barometricPressure:averageHeartRate:averageHeartRateUUID:error:"
- "clientRemote_didSendFeedback:"
- "clientRemote_didStartWithStartTime:expectedDuration:"
- "component:fromDate:"
- "components:fromDate:toDate:options:"
- "confidence"
- "confidenceLevel"
- "conformsToProtocol:"
- "connectionInterrupted"
- "connectionInvalidated"
- "context"
- "controlCenterUserDefaults"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countUnit"
- "currentHandler"
- "d"
- "d16@0:8"
- "daemon"
- "daemonReady:"
- "dailyAnalytics"
- "dataManager"
- "dataProvenanceManager"
- "database"
- "dateByAddingTimeInterval:"
- "dateInterval"
- "debugDescription"
- "defaultLocalDataProvenanceWithDeviceEntity:"
- "delegate"
- "deleteObjectsWithUUIDCollection:configuration:error:"
- "description"
- "device"
- "deviceEntityForDevice:error:"
- "deviceManager"
- "diagnosticDescription"
- "dictionary"
- "didAddSamplesOfTypes:anchor:"
- "doubleValue"
- "doubleValueForUnit:"
- "earliestDateLowestOnboardingVersionCompletedWithError:"
- "emptyCountrySet"
- "endDate"
- "endTime"
- "expectedDuration"
- "expectedEndDate"
- "exportedInterface"
- "featureAvailabilityExtensionDidUpdatePairedDeviceCapability:"
- "featureAvailabilityExtensionDidUpdateRegionAvailability:"
- "featureAvailabilityExtensionForFeatureIdentifier:"
- "featureAvailabilityExtensionOnboardingCompletionDataDidBecomeAvailable:"
- "featureAvailabilityManager"
- "featureAvailabilityProvider"
- "featureAvailabilityProvidingDidUpdateOnboardingCompletion:"
- "featureAvailabilityProvidingDidUpdateSettings:"
- "featureOnboardingRecordWithError:"
- "featureStatusWithError:"
- "generatePayloadAndReturnError:"
- "getActivePairedDevice"
- "getSetupCompletedDevices"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hash"
- "healthDataCollectionAllowed"
- "heartRate"
- "hk_error:format:"
- "hk_filter:"
- "hk_gregorianCalendar"
- "hk_gregorianCalendarWithLocalTimeZone"
- "hk_isAfterDate:"
- "hk_isLessThanQuantity:"
- "hk_startOfDateBySubtractingDays:fromDate:"
- "hkrp_oxygenSaturationType"
- "hkrp_respiratoryDefaults"
- "i"
- "i16@0:8"
- "init"
- "initWithAllowedCountriesDataSource:profile:featureCapability:loggingCategory:"
- "initWithDaemon:allowedCountriesDataSource:loggingCategory:"
- "initWithDaemon:featureIdentifier:"
- "initWithDate:profile:pairedDeviceRegistry:featureAvailabilityProvider:oxygenSaturationSettings:controlCenterUserDefaults:healthDataCollectionAllowed:"
- "initWithDelegate:onQueue:"
- "initWithFeatureAvailabilityProviding:healthDataSource:"
- "initWithFeatureIdentifier:defaultCountrySet:healthDaemon:"
- "initWithFeatureIdentifier:localFeatureAttributes:localCountrySetAvailabilityProvider:"
- "initWithIdentifier:"
- "initWithProfile:"
- "initWithProfile:debugIdentifier:delegate:"
- "initWithProfile:featureAvailabilityExtension:loggingCategory:"
- "initWithProfile:featureAvailabilityManager:companionAnalysisAvailabilityManager:ageGatingDefaults:"
- "initWithProfile:featureAvailabilityProvider:"
- "initWithProfile:featureIdentifier:availabilityRequirements:currentOnboardingVersion:pairedDeviceCapability:pairedFeatureAttributesProvider:regionAvailabilityProvider:disableAndExpiryProvider:loggingCategory:"
- "initWithProfile:featureIdentifier:availabilityRequirements:currentOnboardingVersion:pairedDeviceCapability:regionAvailabilityProvider:disableAndExpiryProvider:loggingCategory:"
- "initWithProfile:oxygenSaturationFeatureStatusProvider:oxygenSaturationCompanionAnalysisFeatureStatusProvider:"
- "initWithProfile:oxygenSaturationFeatureStatusProvider:oxygenSaturationCompanionAnalysisFeatureStatusProvider:unitTestDelegate:"
- "initWithStartDate:endDate:"
- "initWithSuiteName:"
- "initWithURL:resolvingAgainstBaseURL:"
- "initWithUUID:configuration:client:delegate:"
- "initWithUUIDString:"
- "initWithUserDefaults:userDefaultsSyncProvider:companionAnalysisFeatureStatusManager:"
- "initWithUserDefaultsDomain:"
- "insertDataObjects:withProvenance:creationDate:skipInsertionFilter:updateSourceOrder:resolveAssociations:error:"
- "integerValue"
- "invalidateAndWait"
- "isAppleInternalInstall"
- "isAppleWatch"
- "isCompanionAnalysisEnabled"
- "isCompanionCapable"
- "isEqual:"
- "isEqualToString:"
- "isHealthDataCollectionAllowed"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isOnboardingRecordPresent"
- "isProxy"
- "listenerEndpointForClient:error:"
- "localizedDescription"
- "localizedStringByJoiningStrings:"
- "localizedStringForKey:value:table:"
- "metadata"
- "metadataManager"
- "minuteUnit"
- "mostRecentSampleWithType:profile:encodingOptions:predicate:anchor:error:"
- "mutableCopy"
- "notificationManager"
- "now"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectForKeyedSubscript:"
- "onboardingState"
- "overrideIsRemoteDisabled"
- "oxygenSaturationDisabled"
- "oxygenSaturationPercentage"
- "oxygenSaturationSession:didBeginWithStartTime:expectedDuration:"
- "oxygenSaturationSession:didEndForReason:measurement:"
- "oxygenSaturationSession:feedbackDidChange:"
- "oxygenSaturationSessionWithDelegate:queue:"
- "oxygenSaturationSettings"
- "pairedDeviceRegistry"
- "pascalUnitWithMetricPrefix:"
- "payload"
- "percentUnit"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performWorkForOperation:profile:databaseAccessibilityAssertion:completion:"
- "performWriteTransactionWithHealthDatabase:error:block:"
- "postNotificationWithIdentifier:content:trigger:completion:"
- "predicateMatchingAllPredicates:"
- "predicateWithMetadataKey:allowedValues:"
- "prepareForObliteration"
- "pressureInKilopascals"
- "profile"
- "profileDidBecomeReady:"
- "profileExtensionWithIdentifier:"
- "q16@0:8"
- "q24@0:8^@16"
- "quantity"
- "quantitySampleWithType:quantity:startDate:endDate:"
- "quantitySampleWithType:quantity:startDate:endDate:device:metadata:"
- "quantityTypeForIdentifier:"
- "quantityWithUnit:doubleValue:"
- "queryItemWithName:value:"
- "queryItems"
- "registerDaemonReadyObserver:queue:"
- "registerObserver:queue:"
- "registerProfileReadyObserver:queue:"
- "release"
- "remoteInterface"
- "remoteObjectProxyWithErrorHandler:"
- "remote_abortWithCompletion:"
- "remote_startWithCompletion:"
- "reportDailyAnalyticsWithCoordinator:completion:"
- "requestWorkWithPriority:error:"
- "requiredEntitlements"
- "reset"
- "respiratoryExtension"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "samplesAdded:anchor:"
- "samplesJournaled:type:"
- "samplesMapWereRemoved:anchor:"
- "samplesOfTypesWereRemoved:anchor:"
- "samplesWithType:profile:encodingOptions:predicate:limit:anchor:error:"
- "self"
- "sensorSession"
- "serverInterface"
- "sessionState"
- "setAverageHeartRateData:"
- "setBody:"
- "setCategoryIdentifier:"
- "setDateInterval:"
- "setDelegate:"
- "setExpectedDuration:"
- "setExpectedEndDate:"
- "setFailIfNotFound:"
- "setFeatureAvailabilityManager:"
- "setGenerateDeletedObjects:"
- "setHeartRate:"
- "setNotifyObservers:"
- "setObject:forKeyedSubscript:"
- "setOxygenSaturationPercentage:"
- "setPressureInKilopascals:"
- "setQueryItems:"
- "setQueue:"
- "setSensorSession:"
- "setSessionState:"
- "setSound:"
- "setStartTime:"
- "setSubtitle:"
- "setTitle:"
- "setUnitTesting_healthLiteSessionWithDelegateHandler:"
- "setUserInfo:"
- "setUuid:"
- "setWithObject:"
- "sharedBehavior"
- "sharedDiagnosticManager"
- "sharedInstance"
- "soundWithAlertType:"
- "source"
- "sourceRevision"
- "startDate"
- "startOfDayForDate:"
- "startTime"
- "stringValue"
- "stringWithFormat:"
- "superclass"
- "supportsCapability:"
- "synchronizeLocalProperties"
- "taskIdentifier"
- "timeIntervalSinceReferenceDate"
- "timestamp"
- "uncheckedAvailability"
- "unitDividedByUnit:"
- "unitTesting_deliverFeedback:"
- "unitTesting_endSessionWithReason:saturation:barometricPressure:averageHeartRate:averageHeartRateUUID:"
- "unitTesting_healthLiteSessionWithDelegateHandler"
- "unprocessedBloodOxygenDataType"
- "unsatisfiedRequirementIdentifiers"
- "uuid"
- "v16@0:8"
- "v24@0:8@\"<HDFeatureAvailabilityExtension>\"16"
- "v24@0:8@\"<HDHealthDaemon>\"16"
- "v24@0:8@\"<HKFeatureAvailabilityProviding>\"16"
- "v24@0:8@\"HDProfile\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v32@0:8@\"HDAnalyticsSubmissionCoordinator\"16@?<v@?@\"NSMutableDictionary\"q@\"NSError\">24"
- "v32@0:8@\"HLOxygenSaturationSession\"16Q24"
- "v32@0:8@\"NSArray\"16@\"HKSampleType\"24"
- "v32@0:8@\"NSArray\"16@\"NSNumber\"24"
- "v32@0:8@\"NSDictionary\"16@\"NSNumber\"24"
- "v32@0:8@\"NSSet\"16@\"NSNumber\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8d16d24"
- "v40@0:8@\"HLOxygenSaturationSession\"16Q24@\"HLOxygenSaturationMeasurement\"32"
- "v40@0:8@\"HLOxygenSaturationSession\"16d24d32"
- "v40@0:8@16Q24@32"
- "v40@0:8@16d24d32"
- "v48@0:8@\"HDProtectedDataOperation\"16@\"HDProfile\"24@\"HDAssertion\"32@?<v@?>40"
- "v48@0:8@16@24@32@?40"
- "v56@0:8Q16@24@32@40@48"
- "v64@0:8@\"<HKAssociatableObject>\"16@\"<HKAssociatableObject>\"24Q32Q40@\"NSArray\"48@\"NSNumber\"56"
- "v64@0:8@16@24Q32Q40@48@56"
- "v64@0:8q16@24@32@40@48@56"
- "valueForProperty:"
- "weekOfYear"
- "zone"

```
