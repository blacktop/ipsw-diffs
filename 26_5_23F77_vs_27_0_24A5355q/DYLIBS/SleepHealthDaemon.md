## SleepHealthDaemon

> `/System/Library/PrivateFrameworks/SleepHealthDaemon.framework/SleepHealthDaemon`

```diff

-6200.6.8.2.1
-  __TEXT.__text: 0xb7bc
-  __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_methlist: 0xae4
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x64a
-  __TEXT.__oslogstring: 0x1b77
-  __TEXT.__gcc_except_tab: 0x1f0
+7027.0.52.2.6
+  __TEXT.__text: 0xaf58
+  __TEXT.__objc_methlist: 0xab4
+  __TEXT.__const: 0x90
+  __TEXT.__cstring: 0x663
+  __TEXT.__oslogstring: 0x1bef
+  __TEXT.__gcc_except_tab: 0x184
   __TEXT.__unwind_info: 0x270
-  __TEXT.__objc_classname: 0x36e
-  __TEXT.__objc_methname: 0x3221
-  __TEXT.__objc_methtype: 0x9e0
-  __TEXT.__objc_stubs: 0x2240
-  __DATA_CONST.__got: 0x378
-  __DATA_CONST.__const: 0x1d8
-  __DATA_CONST.__objc_classlist: 0x60
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x278
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb00
-  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__objc_selrefs: 0xb18
+  __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x278
+  __DATA_CONST.__got: 0x380
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x4c0
-  __AUTH_CONST.__objc_const: 0x1520
+  __AUTH_CONST.__objc_const: 0x14b0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0xa8
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0xbc
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0xc0
   __DATA.__data: 0x660
   __DATA_DIRTY.__objc_data: 0x280
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 535BEB63-1211-3522-AC08-0CF2892C903D
-  Functions: 160
-  Symbols:   1040
-  CStrings:  731
+  - /usr/lib/swift/libswiftCompression.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: E73AB366-D17F-3671-8C11-07BEAEA55C1D
+  Functions: 158
+  Symbols:   1073
+  CStrings:  201
 
Symbols:
+ +[HDSHSleepHealthDaemonPlugin shouldLoadPluginForBehavior:]
+ -[HDSHWidgetSchedulingManager initWithProfile:workoutStateProvider:unitTest_didSkipWidgetReload:unitTest_didReloadWidgets:]
+ GCC_except_table1
+ GCC_except_table16
+ GCC_except_table9
+ _OBJC_IVAR_$_HDSHWidgetSchedulingManager._queue_workoutStateProvider
+ _OBJC_IVAR_$_HDSHWidgetSchedulingManager._unitTest_didReloadWidgets
+ _OBJC_IVAR_$_HDSHWidgetSchedulingManager._unitTest_didSkipWidgetReload
+ ___109-[HDSHSleepApneaRescindedNotificationManager _showRescindedNotificationWithTitleAndBodyKeys:rescindedReason:]_block_invoke.420
+ ___123-[HDSHWidgetSchedulingManager initWithProfile:workoutStateProvider:unitTest_didSkipWidgetReload:unitTest_didReloadWidgets:]_block_invoke
+ ___43-[HDSHWidgetSchedulingManager daemonReady:]_block_invoke.373
+ ___43-[HDSHWidgetSchedulingManager daemonReady:]_block_invoke_2
+ ___83-[HDSHBreathingDisturbanceAnalyzer _sendPossibleSleepApneaNotificationWithRequest:]_block_invoke.380
+ ___83-[HDSHBreathingDisturbanceAnalyzer _sendPossibleSleepApneaNotificationWithRequest:]_block_invoke.382
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_literal_global.378
+ ___swift_reflection_version
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_SleepHealthDaemon
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_SleepHealthDaemon
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_SleepHealthDaemon
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_SleepHealthDaemon
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_SleepHealthDaemon
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_SleepHealthDaemon
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_SleepHealthDaemon
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_SleepHealthDaemon
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_SleepHealthDaemon
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_SleepHealthDaemon
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_SleepHealthDaemon
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_SleepHealthDaemon
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_SleepHealthDaemon
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_SleepHealthDaemon
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_SleepHealthDaemon
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$hasActiveWorkoutSession
+ _objc_msgSend$initWithProfile:featureIdentifier:availabilityRequirements:currentOnboardingVersion:pairedDeviceCapability:pairedFeatureAttributesProvider:regionAvailabilityProvider:disableAndExpiryProvider:onboardingRecordConfiguration:loggingCategory:
+ _objc_msgSend$initWithProfile:workoutStateProvider:unitTest_didSkipWidgetReload:unitTest_didReloadWidgets:
+ _objc_msgSend$performWhenPostLaunchSessionRecoveryHasCompleted:
+ _objc_msgSend$workoutManager
+ _objc_retainAutoreleaseReturnValue
+ _objc_retainBlock
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x8
- +[HDSHSleepHealthDaemonPlugin shouldLoadPluginForDaemon:]
- -[HDSHSleepApneaNotificationUITriggerObserver .cxx_destruct]
- -[HDSHSleepApneaNotificationUITriggerObserver _deregisterUITriggers]
- -[HDSHSleepApneaNotificationUITriggerObserver _registerUITriggers]
- -[HDSHSleepApneaNotificationUITriggerObserver dealloc]
- -[HDSHSleepApneaNotificationUITriggerObserver initWithProfile:]
- GCC_except_table0
- GCC_except_table13
- _OBJC_CLASS_$_HDSHSleepApneaNotificationUITriggerObserver
- _OBJC_IVAR_$_HDSHProfileExtension._triggerObserver
- _OBJC_IVAR_$_HDSHSleepApneaNotificationUITriggerObserver._profile
- _OBJC_METACLASS_$_HDSHSleepApneaNotificationUITriggerObserver
- __OBJC_$_INSTANCE_METHODS_HDSHSleepApneaNotificationUITriggerObserver
- __OBJC_$_INSTANCE_VARIABLES_HDSHSleepApneaNotificationUITriggerObserver
- __OBJC_CLASS_RO_$_HDSHSleepApneaNotificationUITriggerObserver
- __OBJC_METACLASS_RO_$_HDSHSleepApneaNotificationUITriggerObserver
- ___109-[HDSHSleepApneaRescindedNotificationManager _showRescindedNotificationWithTitleAndBodyKeys:rescindedReason:]_block_invoke.399
- ___47-[HDSHWidgetSchedulingManager initWithProfile:]_block_invoke
- ___83-[HDSHBreathingDisturbanceAnalyzer _sendPossibleSleepApneaNotificationWithRequest:]_block_invoke.359
- ___83-[HDSHBreathingDisturbanceAnalyzer _sendPossibleSleepApneaNotificationWithRequest:]_block_invoke.361
- ___block_literal_global.355
- _objc_msgSend$_deregisterUITriggers
- _objc_msgSend$_registerUITriggers
- _objc_msgSend$initWithProfile:featureIdentifier:availabilityRequirements:currentOnboardingVersion:pairedDeviceCapability:pairedFeatureAttributesProvider:regionAvailabilityProvider:disableAndExpiryProvider:loggingCategory:
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "1"
+ "[%{public}@] skipping widget reload due to active workout"
+ "[%{public}@] waiting for post-launch workout session recovery"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<HDFeatureAvailabilityExtension>\"24@0:8@\"NSString\"16"
- "@\"<HDHealthDaemonExtension>\"24@0:8@\"<HDHealthDaemon>\"16"
- "@\"<HDProfileExtension>\"24@0:8@\"HDProfile\"16"
- "@\"<HKFeatureAvailabilityProviding>\""
- "@\"<HKFeatureStatusProviding>\""
- "@\"HDAssertion\""
- "@\"HDFeatureAvailabilityManager\""
- "@\"HDHealthStoreClient\""
- "@\"HDKeyValueDomain\""
- "@\"HDPeriodicActivity\""
- "@\"HDProfile\""
- "@\"HDProtectedDataOperation\""
- "@\"HDSHAccessibilityAssertionManager\""
- "@\"HDSHBreathingDisturbanceAnalysisScheduler\""
- "@\"HDSHBreathingDisturbanceAnalyzer\""
- "@\"HDSHProfileExtension\""
- "@\"HDSHSleepApneaNotificationUITriggerObserver\""
- "@\"HDSHSleepApneaRescindedNotificationManager\""
- "@\"HDSHWidgetSchedulingManager\""
- "@\"HKAnalyticsEventSubmissionManager\""
- "@\"HKSPSleepStore\""
- "@\"HKSPThrottler\""
- "@\"HKSource\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSCalendar\""
- "@\"NSDateInterval\""
- "@\"NSDictionary\""
- "@\"NSDictionary\"32@0:8@\"HKAnalyticsDataSource\"16^@24"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCListenerEndpoint\"32@0:8@\"HDXPCClient\"16^@24"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@36@0:8@16@24B32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16q24@32"
- "@44@0:8@16@24B32^@36"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24@32@?40"
- "@56@0:8@16@24@32@40^@48"
- "@64@0:8@16@24@32@40@48@56"
- "@64@0:8@16@24@32@?40@48@?56"
- "@?"
- "@?16@0:8"
- "A"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"<HDHealthDaemon>\"16"
- "B24@0:8@\"HDPeriodicActivity\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B36@0:8B16@20q28"
- "B40@0:8@16@24@32"
- "B40@0:8@16@24^@32"
- "B48@0:8@16@24@32^@40"
- "HDContentProtectionObserver"
- "HDDataObserver"
- "HDDiagnosticObject"
- "HDFeatureAvailabilityExtensionProvider"
- "HDHealthDaemonReadyObserver"
- "HDPeriodicActivityDelegate"
- "HDPlugin"
- "HDProfileExtension"
- "HDProfileReadyObserver"
- "HDProtectedDataOperationDelegate"
- "HDSHAccessibilityAssertionManager"
- "HDSHBreathingDisturbanceAnalysisAnalyticsEvent"
- "HDSHBreathingDisturbanceAnalysisScheduler"
- "HDSHBreathingDisturbanceAnalyzer"
- "HDSHPluginServer"
- "HDSHProfileExtension"
- "HDSHReplaceSleepSamplesOperation"
- "HDSHSleepApneaControlServer"
- "HDSHSleepApneaNotificationUITriggerObserver"
- "HDSHSleepApneaRescindedNotificationManager"
- "HDSHSleepHealthDaemonPlugin"
- "HDSHWidgetSchedulingManager"
- "HDSleepHealthDaemonPluginServerInterface"
- "HDTaskServerClassProvider"
- "HKAnalyticsEvent"
- "HKFeatureAvailabilityProvidingObserver"
- "HKFeatureStatusProvidingObserver"
- "HKSHSleepApneaControlServer"
- "NSObject"
- "Q16@0:8"
- "SleepApneaNotifications"
- "T#,R"
- "T@\"HDAssertion\",R,N"
- "T@\"HDPeriodicActivity\",R,N,V_activity"
- "T@\"HDProfile\",R,W,N,V_profile"
- "T@\"HDSHAccessibilityAssertionManager\",R,N,V_accessibilityAssertionManager"
- "T@\"HDSHBreathingDisturbanceAnalysisScheduler\",&,N,V_breathingDisturbanceAnalysisScheduler"
- "T@\"HDSHWidgetSchedulingManager\",R,N,V_widgetSchedulingManager"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,N"
- "T@?,C,N,V_unitTesting_postNotificationHandler"
- "TB,N"
- "TB,R,N"
- "TQ,R"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_accessibilityAssertion"
- "_accessibilityAssertionManager"
- "_activity"
- "_analysisScheduler"
- "_analysisTimeInterval"
- "_analyticsEventSubmissionManager"
- "_analyzer"
- "_areNotificationsEnabled"
- "_areSamplesInSameSleepDayWithFirstSample:secondSample:calendar:"
- "_breathingDisturbanceAnalysisScheduler"
- "_cachedCalendar"
- "_categoryIdentifierFromRescindedReason:"
- "_client"
- "_clientRemoteObjectProxy"
- "_createEnumeratorWithAnalysisInterval:profile:includeTimeZones:"
- "_currentDateProvider"
- "_defaultAnalyticsPayload"
- "_deleteSamples:error:"
- "_deregisterUITriggers"
- "_featureAvailabilityProviding"
- "_featureStatusProvider"
- "_getEarliestOnboardingDate"
- "_insertSamplesWithClientSource:error:"
- "_isAppleWatch"
- "_isFeatureOnboardedWithFeatureOnboardingRecord:"
- "_isFeatureRescindedWithRequirementsEvaluation:"
- "_isFeatureUnavailableForNonRescindedReasonWithRequirementsEvaluation:"
- "_keyValueDomain"
- "_localKeyValueDomain"
- "_logSleepSampleStatistics:"
- "_periodicActivityCompletion"
- "_periodicActivityCompletionLock"
- "_populateSamplesToInsert:samplesToDelete:forSleepDurationGoal:error:"
- "_populateSamplesToInsert:samplesToDelete:forSleepSchedules:error:"
- "_profile"
- "_profileExtension"
- "_protectedDataOperation"
- "_queue"
- "_queue_checkFeatureStatus"
- "_queue_sendNotificationRequestIfNeededWithFeatureStatus:"
- "_queue_takeAccessibilityAssertion"
- "_registerUITriggers"
- "_reloadThrottler"
- "_reloadWidgetsWithReasons:"
- "_replaceSamples:withSamples:error:"
- "_replacementInterval"
- "_requestBreathingDisturbanceAnalysisIfNeeded"
- "_requestBreathingDisturbanceAnalysisWithSamples:analysisInterval:"
- "_rescindedNotificationManager"
- "_rescindedNotificationTitleAndBodyKeysWithHighestPriorityUnsatisfiedRequirementIdentifier:"
- "_rescindedRequirementIdentifiers"
- "_restoreContentProtectionObservingState"
- "_runCompletionIfExistsWithResult:retryInterval:shouldUpdateActivityCriteria:"
- "_sampleWithHighestDurationWithFirstSample:secondSample:"
- "_saveSleepTrackingSamplesAfterFirstUnlock:replacingSamplesInDateInterval:completion:"
- "_sendAnalyticsWithPayload:"
- "_sendPossibleSleepApneaNotificationWithRequest:"
- "_serializer"
- "_showRescindedNotificationWithTitleAndBodyKeys:rescindedReason:"
- "_sleepApneaNotificationsAvailabilityManager"
- "_sleepSamples"
- "_sleepStore"
- "_source"
- "_startObservingSleep"
- "_stopObservingSleep"
- "_triggerObserver"
- "_typeWithIdentifier:"
- "_unitTesting_postNotificationHandler"
- "_unitTesting_profileDidBecomeReadyBlock"
- "_updateActivityCriteriaAndResetActivity"
- "_updateWidgetRelevances"
- "_useTimeIntervalOverride"
- "_value"
- "_widgetSchedulingManager"
- "_writeDateOfMostRecentSuccessfulAnalysisAttempt"
- "_writePossibleSleepApneaNotificationSampleWithAnalysisInterval:algorithmVersion:error:"
- "accessibilityAssertion"
- "accessibilityAssertionManager"
- "activeRemoteDeviceIsPresentWhenRequiredForRegionAvailabilityOrDeviceCapabilityForFeatureWithIdentifier:"
- "activity"
- "addContentProtectionObserver:withQueue:"
- "addEncodingOptionsFromDictionary:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:forDataType:"
- "analyzeSamples:dateInterval:"
- "areAllRequirementsSatisfied"
- "arrayByAddingObject:"
- "arrayWithArray:"
- "arrayWithObjects:count:"
- "associationsUpdatedForObject:subObject:type:behavior:objects:anchor:"
- "autorelease"
- "bedTimeComponents"
- "beginObservingContentProtectionState"
- "behavior"
- "breathingDisturbanceAnalysisScheduler"
- "canPerformCloudSyncWithError:"
- "capabilityIsSupportedOnActiveWatchForFeatureWithIdentifier:supportedOnLocalDevice:"
- "categorySampleWithType:value:startDate:endDate:metadata:"
- "categoryType"
- "categoryTypeForIdentifier:"
- "class"
- "client"
- "cloudSyncManager"
- "components:fromDate:toDate:options:"
- "componentsJoinedByString:"
- "configurationClass"
- "conformsToProtocol:"
- "connection"
- "connectionInvalidated"
- "constructAnalysisDateIntervalFromDate:withCalendar:"
- "containsObject:"
- "contentProtectionManager"
- "contentProtectionStateChanged:previousState:"
- "contextForWritingProtectedData"
- "contextWithAccessibilityAssertion:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countryIsSupportedOnActiveRemoteDeviceForFeatureWithIdentifier:isSupportedIfCountryListMissing:"
- "countryIsSupportedOnLocalDeviceForFeatureWithIdentifier:"
- "createOrUpdateSourceForClient:error:"
- "createTaskServerWithUUID:configuration:client:delegate:error:"
- "currentCalendar"
- "currentDeviceEntityWithError:"
- "currentHandler"
- "d"
- "daemon"
- "daemonReady:"
- "dataManager"
- "dataProvenanceManager"
- "database"
- "date"
- "dateByAddingComponents:toDate:options:"
- "dateForKey:error:"
- "day"
- "dealloc"
- "debugDescription"
- "debugIdentifier"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultOnboardingEligibilityRequirementsForFeatureIdentifier:"
- "deleteDataObjectsOfClass:predicate:limit:deletedSampleCount:notifyObservers:generateDeletedObjects:recursiveDeleteAuthorizationBlock:error:"
- "deleteObjectsWithUUIDCollection:configuration:error:"
- "description"
- "deviceManager"
- "diagnosticDescription"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "didAddSamplesOfTypes:anchor:"
- "earliestDateOfAnyOnboardingCompletion"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endDate"
- "endDateFromMostRecentlyAnalyzedDateIntervalWithDate:numberOfAnalysisAttempts:calendar:"
- "entityEnumeratorWithType:profile:"
- "enumerateWithError:handler:"
- "environmentDataSource"
- "eventName"
- "execute"
- "exportedInterface"
- "extensionForHealthDaemon:"
- "extensionForProfile:"
- "featureAttributesDerivedFromOSBuildAndFeatureVersion:watchDeviceIdentifier:phoneDeviceIdentifier:"
- "featureAvailabilityExtensionForFeatureIdentifier:"
- "featureAvailabilityProvidingDidUpdateOnboardingCompletion:"
- "featureAvailabilityProvidingDidUpdateSettings:"
- "featureIsNotRemotelyDisabledWithIdentifier:"
- "featureIsOnWithIdentifier:isOnIfSettingIsAbsent:"
- "featureOnboardingRecordWithError:"
- "featureStatusProviding:didUpdateFeatureStatus:"
- "featureStatusWithError:"
- "fetchSamplesWithAnalysisInterval:profile:includeTimeZones:error:"
- "firstObject"
- "handleDatabaseObliteration"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hasEquivalentOverrideDayToSleepSchedule:"
- "hasEquivalentTimesToSleepSchedule:"
- "hash"
- "hd_sourceForClient:bundleIdentifier:"
- "hdsh_sleepApneaNotificationsAvailabilityManagerWithProfile:"
- "healthAppIsNotHidden"
- "highestPriorityUnsatisfiedRequirement"
- "hk_dateByAddingDays:toDate:"
- "hk_error:format:"
- "hk_gregorianCalendar"
- "hk_isBeforeDate:"
- "hk_isDatabaseAccessibilityError"
- "hk_map:"
- "hk_minus:"
- "hk_morningIndexWithCalendar:"
- "hk_sleepDayStartWithCalendar:"
- "hk_timeZoneEncodingOptions"
- "hksp_supportsHealthData"
- "identifier"
- "init"
- "initWithAllowedCountriesDataSource:profile:featureCapability:loggingCategory:"
- "initWithArray:"
- "initWithCategory:domainName:profile:"
- "initWithChangesSyncRequest:"
- "initWithCoder:"
- "initWithCountryBitmasks:compatibilityVersion:contentVersion:provenance:"
- "initWithDaemon:featureIdentifier:"
- "initWithDefaultAnalyticsPayload:"
- "initWithDictionary:"
- "initWithFeatureAvailabilityProviding:healthDataSource:"
- "initWithFeatureIdentifier:defaultCountrySet:healthDaemon:"
- "initWithFeatureIdentifier:isOnWhenSettingIsAbsent:"
- "initWithFeatureIdentifier:localFeatureAttributes:localCountrySetAvailabilityProvider:"
- "initWithIdentifier:healthStore:options:"
- "initWithInterval:executeBlock:"
- "initWithLoggingCategory:healthDataSource:"
- "initWithNotificationRequest:actionIdentifier:"
- "initWithProfile:"
- "initWithProfile:debugIdentifier:delegate:"
- "initWithProfile:featureIdentifier:availabilityRequirements:currentOnboardingVersion:pairedDeviceCapability:pairedFeatureAttributesProvider:regionAvailabilityProvider:disableAndExpiryProvider:loggingCategory:"
- "initWithProfile:featureStatusProvider:"
- "initWithProfile:featureStatusProvider:featureAvailabilityProviding:currentDateProvider:"
- "initWithProfile:featureStatusProvider:featureAvailabilityProviding:currentDateProvider:protectedDataOperation:profileDidBecomeReadyBlock:"
- "initWithProfile:featureStatusProvider:queueOverride:"
- "initWithProfile:name:interval:delegate:loggingCategory:"
- "initWithPush:pull:lite:"
- "initWithRequirementsByContext:"
- "initWithSleepSamplesToInsert:source:replacementInterval:accessibilityAssertion:"
- "initWithStartDate:endDate:"
- "initWithUUID:configuration:client:delegate:"
- "initWithUUID:configuration:client:delegate:analyzer:analysisScheduler:"
- "initWithUUIDString:"
- "insertDataObjects:withProvenance:creationDate:skipInsertionFilter:error:"
- "integerValue"
- "invalidate"
- "invalidateAccessibilityAssertion"
- "invalidateAndWait"
- "invalidateRelevances"
- "isAnalysisNeededWithAnchorDate:referenceDate:calendar:"
- "isAppleWatch"
- "isEqual:"
- "isEqualToString:"
- "isEventSubmissionIHAGated"
- "isImproveHealthAndActivityEnabled"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isRealityDevice"
- "listenerEndpointForClient:error:"
- "localAvailabilityForSleepApneaNotifications"
- "localDataProvenanceForSourceEntity:version:deviceEntity:"
- "localDeviceSourceWithError:"
- "localizedUserNotificationStringForKey:arguments:"
- "makeIHAGatedEventPayloadWithDataSource:error:"
- "makeUnrestrictedEventPayloadWithDataSource:error:"
- "mostRecentSampleWithType:profile:encodingOptions:predicate:anchor:error:"
- "mostRecentSleepScheduleForWeekday:beforeDate:profile:encodingOptions:error:"
- "na_any:"
- "na_each:"
- "na_filter:"
- "name"
- "nanoSyncManager"
- "notAgeGatedForUserDefaultsKey:"
- "notificationManager"
- "now"
- "numberForKey:error:"
- "numberOfExpectedAnalysisAttemptsStartingFromAnchorDate:referenceDate:calendar:"
- "numberWithBool:"
- "numberWithInteger:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "onCommit:orRollback:"
- "onboardingRecordIsNotPresentForFeatureWithIdentifier:"
- "onboardingRecordIsPresentForFeatureWithIdentifier:"
- "onboardingState"
- "overrideAnalysisTimeIntervalAndResetActivityWithTimeInterval:"
- "performBreathingDisturbanceAnalysisWithIsForced:date:numberOfAnalysisAttempts:"
- "performOrJournalWithProfile:error:"
- "performPeriodicActivity:completion:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performWhenDataProtectedByFirstUnlockIsAvailable:"
- "performWhenDataProtectedByFirstUnlockIsAvailableOnQueue:block:"
- "performWithProfile:transaction:error:"
- "performWorkForOperation:profile:databaseAccessibilityAssertion:completion:"
- "periodicActivity:configureXPCActivityCriteria:"
- "periodicActivityRequiresProtectedData:"
- "pluginIdentifier"
- "postNotificationWithRequest:completion:"
- "predicateMatchingAllPredicates:"
- "prepareForObliteration"
- "prerequisiteFeaturesAreOnWithFeatureSettings:"
- "profile"
- "profileDidBecomeReady:"
- "profileExtensionWithIdentifier:"
- "profileIsNotFamilySetupPairingProfile"
- "profileType"
- "q40@0:8@16@24@32"
- "quantity"
- "quantityTypeForIdentifier:"
- "registerDaemonReadyObserver:queue:"
- "registerObserver:queue:"
- "registerProfileReadyObserver:queue:"
- "release"
- "reloadWidgetsWithReason:"
- "remoteInterface"
- "remoteObjectProxy"
- "remote_forceBreathingDisturbanceAnalysis"
- "remote_getBreathingDisturbanceSamplesInDateInterval:includeTimeZones:completion:"
- "remote_overridePreviousTimeIntervalWithTimeInterval:"
- "remote_saveSleepTrackingSamples:replacingSamplesInDateInterval:completion:"
- "remote_startSleepTrackingSession"
- "remote_stopSleepTrackingSession"
- "remote_updateCurrentSleepSchedules:sleepDurationGoal:completion:"
- "removeContentProtectionObserver:"
- "removeObserver:forDataType:"
- "removeValuesForKeys:error:"
- "requestWithIdentifier:content:trigger:"
- "requestWorkWithPriority:error:"
- "requiredEntitlements"
- "requirementsEvaluationByContext"
- "resetInterval"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "samplesAdded:anchor:"
- "samplesFilteredBySleepDay:"
- "samplesJournaled:type:"
- "samplesMapWereRemoved:anchor:"
- "samplesOfTypesWereRemoved:anchor:"
- "seedIsNotExpiredForFeatureWithIdentifier:"
- "self"
- "setBody:"
- "setBreathingDisturbanceAnalysisScheduler:"
- "setCategoryIdentifier:"
- "setDate:"
- "setDate:forKey:error:"
- "setDay:"
- "setExpirationDate:"
- "setNumber:forKey:error:"
- "setObject:atIndexedSubscript:"
- "setObject:forKeyedSubscript:"
- "setPredicate:"
- "setShouldBeObservingContentProtectionState:"
- "setSortDescriptors:"
- "setSound:"
- "setTitle:"
- "setUnitTesting_postNotificationHandler:"
- "setUserInfo:"
- "setWithArray:"
- "setWithObject:"
- "sharedBehavior"
- "sharedDiagnosticManager"
- "shouldBeObservingContentProtectionState"
- "shouldLoadPluginForDaemon:"
- "sleepDurationGoalType"
- "someRegionIsSupportedForFeatureWithIdentifier:"
- "sortDescriptorWithKey:ascending:"
- "soundWithAlertType:"
- "sourceEntityForClientSource:createOrUpdateIfNecessary:error:"
- "sourceManager"
- "sourceRevision"
- "startDate"
- "stopObservingContentProtectionState"
- "stringWithFormat:"
- "subarrayWithRange:"
- "submitEvent:completion:"
- "superclass"
- "supportsSecureCoding"
- "syncHealthDataWithOptions:reason:accessibilityAssertion:completion:"
- "syncWithRequest:reason:completion:"
- "synchronizeLocalProperties"
- "takeAccessibilityAssertionWithOwnerIdentifier:timeout:error:"
- "taskIdentifier"
- "taskServerClasses"
- "timeIntervalSinceDate:"
- "timeIntervalSinceNow"
- "transactionContext"
- "unitTesting_postNotificationHandler"
- "unsatisfiedRequirementIdentifiers"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"<HDHealthDaemon>\"16"
- "v24@0:8@\"<HKFeatureAvailabilityProviding>\"16"
- "v24@0:8@\"HDProfile\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v32@0:8@\"<HKFeatureStatusProviding>\"16@\"HKFeatureStatus\"24"
- "v32@0:8@\"HDPeriodicActivity\"16@\"NSObject<OS_xpc_object>\"24"
- "v32@0:8@\"HDPeriodicActivity\"16@?<v@?qd@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@\"HKSampleType\"24"
- "v32@0:8@\"NSArray\"16@\"NSNumber\"24"
- "v32@0:8@\"NSDictionary\"16@\"NSNumber\"24"
- "v32@0:8@\"NSSet\"16@\"NSNumber\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8q16q24"
- "v36@0:8@\"NSDateInterval\"16B24@?<v@?@\"NSArray\">28"
- "v36@0:8@16B24@?28"
- "v36@0:8q16d24B32"
- "v40@0:8@\"NSArray\"16@\"HKQuantitySample\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"NSArray\"16@\"NSDateInterval\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"HDProtectedDataOperation\"16@\"HDProfile\"24@\"HDAssertion\"32@?<v@?>40"
- "v48@0:8@16@24@32@?40"
- "v64@0:8@\"<HKAssociatableObject>\"16@\"<HKAssociatableObject>\"24Q32Q40@\"NSArray\"48@\"NSNumber\"56"
- "v64@0:8@16@24Q32Q40@48@56"
- "validateConfiguration:client:error:"
- "value"
- "wakeTimeComponents"
- "weekdays"
- "widgetManager"
- "wristDetectionIsEnabledForActiveWatch"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
