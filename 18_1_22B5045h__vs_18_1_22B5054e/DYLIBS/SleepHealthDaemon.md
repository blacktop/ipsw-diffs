## SleepHealthDaemon

> `/System/Library/PrivateFrameworks/SleepHealthDaemon.framework/SleepHealthDaemon`

```diff

-5200.1.7.0.0
-  __TEXT.__text: 0x4890
-  __TEXT.__auth_stubs: 0x420
-  __TEXT.__objc_methlist: 0x2f8
+5200.1.9.1.2
+  __TEXT.__text: 0xac10
+  __TEXT.__auth_stubs: 0x520
+  __TEXT.__objc_methlist: 0x6f0
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x169
-  __TEXT.__oslogstring: 0x84b
-  __TEXT.__gcc_except_tab: 0xdc
-  __TEXT.__unwind_info: 0x150
-  __TEXT.__objc_classname: 0x18d
-  __TEXT.__objc_methname: 0x1396
-  __TEXT.__objc_methtype: 0x4b6
-  __TEXT.__objc_stubs: 0xf20
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0x178
-  __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x58
+  __TEXT.__cstring: 0x62a
+  __TEXT.__oslogstring: 0x17fe
+  __TEXT.__gcc_except_tab: 0x1f0
+  __TEXT.__unwind_info: 0x250
+  __TEXT.__objc_classname: 0x34d
+  __TEXT.__objc_methname: 0x30e7
+  __TEXT.__objc_methtype: 0x95f
+  __TEXT.__objc_stubs: 0x2240
+  __DATA_CONST.__got: 0x348
+  __DATA_CONST.__const: 0x1d8
+  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x490
-  __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x220
+  __DATA_CONST.__objc_selrefs: 0xa00
+  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_arraydata: 0x48
+  __AUTH_CONST.__auth_got: 0x2a0
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x120
-  __AUTH_CONST.__objc_const: 0xdf0
-  __AUTH_CONST.__objc_intobj: 0x18
-  __DATA.__objc_ivar: 0x38
-  __DATA.__data: 0x420
-  __DATA_DIRTY.__objc_data: 0x190
+  __AUTH_CONST.__cfstring: 0x460
+  __AUTH_CONST.__objc_const: 0x1a30
+  __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0xb0
+  __DATA.__data: 0x660
+  __DATA_DIRTY.__objc_data: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
+  - /System/Library/PrivateFrameworks/BreathingAlgorithms.framework/BreathingAlgorithms
   - /System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon
   - /System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation
   - /System/Library/PrivateFrameworks/Sleep.framework/Sleep

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 72
-  Symbols:   188
-  CStrings:  325
+  Functions: 156
+  Symbols:   364
+  CStrings:  673
 
Symbols:
+ _OBJC_CLASS_$_UNNotificationRequest
+ _kHKNotificationsDomainKey
+ _HKSleepApneaNotificationsiOSDeviceIdentifierPortion
+ _HKQuantityTypeIdentifierAppleSleepingBreathingDisturbances
+ _XPC_ACTIVITY_REPEATING
+ _objc_retain_x4
+ _objc_retain_x5
+ _HKIsAgeGatedUserDefaultsSleepApneaNotificationsKey
+ _OBJC_CLASS_$_NSDateComponents
+ _objc_setProperty_nonatomic_copy
+ _HKSHSleepApneaNotificationCategoryRescindedNoLongerSupportedOnLocalDevice
+ _OBJC_CLASS_$_HKFeatureAvailabilityRequirements
+ _HKSHBreathingDisturbanceAnalysisWindowLength
+ _HKSPCurrentDateProvider
+ _OBJC_CLASS_$_HKAnalyticsEventSubmissionManager
+ _OBJC_CLASS_$_HDSHSleepApneaRescindedNotificationManager
+ _HKSHBreathingDisturbanceKeyValueDomainName
+ _HKSleepApneaNotificationswatchOSDeviceIdentifierPortion
+ _OBJC_CLASS_$_HKFeatureAvailabilityRequirementFeatureSetting
+ _HKFeatureAvailabilityContextSettingsUserInteractionEnabled
+ _OBJC_CLASS_$_HKFeatureAvailabilityRequirementSet
+ _OBJC_CLASS_$_UNMutableNotificationContent
+ _OBJC_CLASS_$_HDProtectedDataOperation
+ _OBJC_METACLASS_$_HDSHBreathingDisturbanceAnalysisScheduler
+ _HKSHSleepApneaNotificationCategoryRescindedSeedExpired
+ _HKFeatureAvailabilityRequirementIdentifierCountryIsSupportedOnLocalDevice
+ _HKFeatureAvailabilityRequirementIdentifierFeatureIsNotRemotelyDisabled
+ _OBJC_CLASS_$_HDSHSleepApneaControlServer
+ _objc_retain_x26
+ _OBJC_CLASS_$_NSSortDescriptor
+ _HKFeatureAvailabilityContextSettingsVisibility
+ _XPC_ACTIVITY_INTERVAL_1_DAY
+ _OBJC_METACLASS_$_HDSHSleepApneaControlServer
+ _OBJC_CLASS_$_HDPairedFeaturePropertiesSyncManager
+ _OBJC_METACLASS_$_HDSHBreathingDisturbanceAnalyzer
+ _HKSHSleepApneaControlServerInterface
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_HDFeatureAvailabilityManager
+ _OBJC_CLASS_$_HKFeatureStatusManager
+ _MGGetBoolAnswer
+ _HKCreateSerialUtilityDispatchQueue
+ _HKCategoryTypeIdentifierSleepApneaEvent
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$_HDPeriodicActivity
+ _HKFeatureIdentifierSleepTracking
+ _HKSHCreatePossibleSleepApneaDetectedNotificationRequest
+ _HKSHBreathingDisturbanceAnalysisSchedulerSuccessfulAnalysisAttemptCountKey
+ _OBJC_CLASS_$_BABreathingDisturbanceAnalyzer
+ _HDSHSleepApneaRescindedNotificationDateShownKey
+ _HKSHBreathingDisturbanceAnalysisSchedulerLastSuccessfulAnalysisAttemptDateKey
+ _HKSHSleepApneaNotificationCategoryFeatureIsAvailableAgainAndEnabled
+ _HKSampleSortIdentifierStartDate
+ _OBJC_CLASS_$_HDLocalCountrySetAvailabilityProvider
+ _HKFeatureIdentifierSleepApneaNotifications
+ __dispatch_main_q
+ _OBJC_CLASS_$__HKBehavior
+ _HKSHSleepApneaNotificationCategoryRescindedNoLongerSupportedOnActiveRemoteDevice
+ _HKSleepApneaNotificationsFeatureVersion
+ _OBJC_CLASS_$_HDSHBreathingDisturbanceAnalyzer
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_UNMutableNotificationSound
+ _OBJC_CLASS_$_HDOTAFeatureDisableAndExpiryProvider
+ _HKFeatureAvailabilityRequirementIdentifierSeedIsNotExpired
+ _HKSHSleepApneaNotificationRequestIdentifier
+ _OBJC_CLASS_$_HDWatchAndCompanionCountrySetIntersectionAvailabilityProvider
+ _OBJC_CLASS_$_NSDictionary
+ _HKFeatureAvailabilityContextOnboardingInitiation
+ _OBJC_CLASS_$_HDSHBreathingDisturbanceAnalysisScheduler
+ __os_log_fault_impl
+ _objc_retain_x3
+ _XPC_ACTIVITY_ALLOW_BATTERY
+ _HKFeatureAvailabilityContextUsage
+ _OBJC_CLASS_$_HKFeatureAttributes
+ _HKSHSleepApneaControlClientInterface
+ _OBJC_METACLASS_$_HDSHSleepApneaRescindedNotificationManager
+ _OBJC_CLASS_$_HDPrimaryProfile
+ _OBJC_CLASS_$_HKCountrySet
+ _OBJC_CLASS_$_HKTaskConfiguration
+ _OBJC_CLASS_$_NSCalendar
+ _HKSHSleepApneaControlServerIdentifier
+ _XPC_ACTIVITY_INTERVAL
+ ___NSArray0__struct
+ _xpc_dictionary_set_bool
+ _HKSHSleepApneaNotificationCategoryRescindedRemoteDisabled
+ _HKFeatureAvailabilityContextOnboardingPromotion
+ _HKFeatureAvailabilityRequirementIdentifierCountryIsSupportedOnActiveRemoteDevice
+ _HKMetadataKeyAlgorithmVersion
+ _OBJC_CLASS_$_NSDateInterval
+ __ProtectedOperationDebugIdentifier
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _xpc_dictionary_set_int64
CStrings:
+ "[%!{(MISSING)public}@] Requesting analysis with %!l(MISSING)u samples and analysis interval of %!@(MISSING)"
+ "featureIsOnWithIdentifier:isOnIfSettingIsAbsent:"
+ "@32@0:8@16@24"
+ "initWithDefaultAnalyticsPayload:"
+ "updateCriteria"
+ "@\"NSDictionary\"32@0:8@\"HKAnalyticsDataSource\"16^@24"
+ "@56@0:8@16@24@32@40^@48"
+ "SleepApneaNotifications"
+ "[%!{(MISSING)public}@] Sleep apnea notifications are unavailable for non-rescinded reasons."
+ "[%!{(MISSING)public}@] Unexpectedly filtered to more than %!d(MISSING) samples, will only return that amount starting from the first sample."
+ "_showRescindedNotificationWithTitleAndBodyKeys:rescindedReason:"
+ "bd_count"
+ "day"
+ "debugIdentifier"
+ "HDSHSleepApneaRescindedNotificationDateShownKey"
+ "[%!{(MISSING)public}@] Got nil onboarding date, not checking if analysis is overdue."
+ "componentsJoinedByString:"
+ "[%!{(MISSING)public}@] Possible sleep apnea NOT detected from breathing disturbance samples."
+ "entityEnumeratorWithType:profile:"
+ "numberForKey:error:"
+ "v32@0:8@\"<HKFeatureStatusProviding>\"16@\"HKFeatureStatus\"24"
+ "requestWorkWithPriority:error:"
+ "setCategoryIdentifier:"
+ "@40@0:8@16@24^@32"
+ "_rescindedRequirementIdentifiers"
+ "initWithProfile:featureIdentifier:availabilityRequirements:currentOnboardingVersion:pairedDeviceCapability:pairedFeatureAttributesProvider:regionAvailabilityProvider:disableAndExpiryProvider:loggingCategory:"
+ "[%!{(MISSING)public}@] Sleep apnea notifications are rescinded. Notification was last shown: %!@(MISSING)"
+ "[%!{(MISSING)public}@] Could not write date of last analysis attempt with error %!@(MISSING)"
+ "_isFeatureRescindedWithRequirementsEvaluation:"
+ "featureAvailabilityProvidingDidUpdatePairedDeviceCapability:"
+ "categorySampleWithType:value:startDate:endDate:metadata:"
+ "@48@0:8@16@24@32@?40"
+ "initWithProfile:debugIdentifier:delegate:"
+ "_runCompletionIfExistsWithResult:retryInterval:"
+ "notAgeGatedForUserDefaultsKey:"
+ "v32@0:8@\"NSDateInterval\"16@?<v@?@\"NSArray\">24"
+ "HDSHBreathingDisturbanceAnalyzer"
+ "_rescindedNotificationTitleAndBodyKeysWithHighestPriorityUnsatisfiedRequirementIdentifier:"
+ "_updateActivityCriteriaAndResetActivity"
+ "dictionaryWithObjects:forKeys:count:"
+ "@\"HDSHSleepApneaNotificationUITriggerObserver\""
+ "arrayWithArray:"
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_BODY_SEED_EXPIRED"
+ "[%!{(MISSING)public}@] Fetched %!l(MISSING)u samples, filtered to %!l(MISSING)u samples."
+ "\x14"
+ "HDSHBreathingDisturbanceAnalysisScheduler"
+ "HDSHSleepApneaNotificationUITriggerObserver"
+ "[%!{(MISSING)public}@] Error posting notification: %!@(MISSING)"
+ "constructAnalysisDateIntervalFromDate:withCalendar:"
+ "highestPriorityUnsatisfiedRequirement"
+ "_defaultAnalyticsPayload"
+ "setBody:"
+ "setExpirationDate:"
+ "B32@?0@\"HKObject\"8q16^@24"
+ "quantityTypeForIdentifier:"
+ "[%!{(MISSING)public}@] Possible sleep apnea detected from breathing disturbance samples."
+ "remote_overridePreviousTimeIntervalWithTimeInterval:"
+ "[%!{(MISSING)public}@] With date %!@(MISSING) and number of analysis attempts %!l(MISSING)d, end date of most recently analyzed date interval is %!@(MISSING)."
+ "endDateFromMostRecentlyAnalyzedDateIntervalWithDate:numberOfAnalysisAttempts:calendar:"
+ "hk_sleepDayStartWithCalendar:"
+ "[%!{(MISSING)public}@] Feature is disabled; not going to check if analysis is overdue."
+ "[%!{(MISSING)public}@] Number of expected analysis attempts between %!@(MISSING) and %!@(MISSING) is: %!l(MISSING)d"
+ "postNotificationWithRequest:completion:"
+ "[%!{(MISSING)public}@] Analysis successfully performed!"
+ "_localKeyValueDomain"
+ "resetInterval"
+ "HDSHSleepApneaControlServer"
+ "HKSHSleepApneaControlServer"
+ "dateByAddingComponents:toDate:options:"
+ "initWithFeatureIdentifier:isOnWhenSettingIsAbsent:"
+ "unitTesting_postNotificationHandler"
+ "d"
+ "hk_dateByAddingDays:toDate:"
+ "hk_gregorianCalendar"
+ "isEventSubmissionIHAGated"
+ "T@?,C,N,V_unitTesting_postNotificationHandler"
+ "[%!{(MISSING)public}@] Feature status is nil with error: %!@(MISSING)"
+ "_analyzer"
+ "initWithProfile:name:interval:delegate:loggingCategory:"
+ "isAnalysisNeededWithAnchorDate:referenceDate:calendar:"
+ "seedIsNotExpiredForFeatureWithIdentifier:"
+ "[%!{(MISSING)public}@] Activity criteria will be updated and reset."
+ "@\"HKAnalyticsEventSubmissionManager\""
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_BODY_UNSUPPORTED_REGION"
+ "[%!{(MISSING)public}@] Failed to perform successful analysis.\nWill retry in one day."
+ "_categoryIdentifierFromRescindedReason:"
+ "healthAppIsNotHidden"
+ "v24@0:8d16"
+ "[%!{(MISSING)public}@] Analysis is needed. Analyzing over date intervals that have not been analyzed."
+ "requirementsEvaluationByContext"
+ "setDate:"
+ "setSound:"
+ "_completionLock"
+ "now"
+ "objectAtIndexedSubscript:"
+ "registerObserver:queue:"
+ "eventName"
+ "v24@0:8@\"<HKFeatureAvailabilityProviding>\"16"
+ "@\"NSDictionary\""
+ "initWithDaemon:featureIdentifier:"
+ "@\"HDSHBreathingDisturbanceAnalyzer\""
+ "_completion"
+ "_keyValueDomain"
+ "periodicActivityRequiresProtectedData:"
+ "initWithRequirementsByContext:"
+ "B32@0:8@16@24"
+ "Local generated country set should never be nil"
+ "[%!{(MISSING)public}@] Error fetching onboarding record: %!@(MISSING)\nReturning nil onboarding date."
+ "_isFeatureOnboardedWithFeatureOnboardingRecord:"
+ "periodicActivity:configureXPCActivityCriteria:"
+ "soundWithAlertType:"
+ "[%!{(MISSING)public}@] Checking feature status for non-rescinded reasons: %!@(MISSING)"
+ "@64@0:8@16@24@32@?40@48@?56"
+ "[%!{(MISSING)public}@] User is not onboarded in a supported region."
+ "_writePossibleSleepApneaNotificationSampleWithAnalysisInterval:algorithmVersion:error:"
+ "performPeriodicActivity:completion:"
+ "TB,R,N"
+ "_clientRemoteObjectProxy"
+ "dictionary"
+ "q40@0:8@16@24@32"
+ "remoteObjectProxy"
+ "@40@0:8@16q24@32"
+ "B36@0:8B16@20q28"
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_TITLE_UNSUPPORTED_REGION"
+ "_requestBreathingDisturbanceAnalysisWithSamples:analysisInterval:"
+ "@\"<HKFeatureStatusProviding>\""
+ "SLEEP_APNEA_REENABLED_NOTIFICATION_TITLE"
+ "initWithUUID:configuration:client:delegate:analyzer:analysisScheduler:"
+ "nebula"
+ "@\"HDPeriodicActivity\""
+ "@\"HDSHSleepApneaRescindedNotificationManager\""
+ "HDProtectedDataOperationDelegate"
+ "Profile extension not found for class %!@(MISSING)"
+ "is_improve_health_and_activity_allowed"
+ "unsatisfiedRequirementIdentifiers"
+ "_areSamplesInSameSleepDayWithFirstSample:secondSample:calendar:"
+ "HDSHBreathingDisturbanceAnalysisAnalyticsEvent"
+ "synchronizeLocalProperties"
+ "[%!{(MISSING)public}@] Feature status changed to: %!@(MISSING)"
+ "countryIsSupportedOnActiveRemoteDeviceForFeatureWithIdentifier:isSupportedIfCountryListMissing:"
+ "remote_forceBreathingDisturbanceAnalysis"
+ "HKAnalyticsEvent"
+ "HKFeatureStatusProvidingObserver"
+ "[%!{(MISSING)public}@] Successfully sent analytics payload!"
+ "_featureAvailabilityProviding"
+ "_queue_sendNotificationRequestIfNeededWithFeatureStatus:"
+ "initWithStartDate:endDate:"
+ "_breathingDisturbanceAnalysisScheduler"
+ "initWithDictionary:"
+ "onboardingRecordIsPresentForFeatureWithIdentifier:"
+ "featureIsNotRemotelyDisabledWithIdentifier:"
+ "localAvailabilityForSleepApneaNotifications"
+ "requestWithIdentifier:content:trigger:"
+ "[%!{(MISSING)public}@] Failed to write sleep apnea event sample with error: %!@(MISSING). Not sending notification and will attempt to retry in one day."
+ "performWorkForOperation:profile:databaseAccessibilityAssertion:completion:"
+ "profileIsNotFamilySetupPairingProfile"
+ "HDPeriodicActivityDelegate"
+ "[%!{(MISSING)public}@] Error getting feature status: %!@(MISSING)"
+ "validateConfiguration:client:error:"
+ "[%!{(MISSING)public}@] About to post possible sleep apnea detected notification."
+ "_activity"
+ "currentCalendar"
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_TITLE_REMOTELY_DISABLED"
+ "[%!{(MISSING)public}@] Attempting to send analytics."
+ "[%!{(MISSING)public}@] Request was processed, but completion exists before capture."
+ "featureAvailabilityProvidingDidUpdateSettings:"
+ "_getEarliestOnboardingDate"
+ "featureStatusProviding:didUpdateFeatureStatus:"
+ "v32@0:8@16@?24"
+ "featureAttributesDerivedFromOSBuildAndFeatureVersion:watchDeviceIdentifier:phoneDeviceIdentifier:"
+ "sharedBehavior"
+ "[%!{(MISSING)public}@] About to show rescinded notification for sleep apnea notifications."
+ "[%!{(MISSING)public}@] Analysis is not needed."
+ "[%!{(MISSING)public}@] Error posting rescinded notification: %!@(MISSING)"
+ "_analyticsEventSubmissionManager"
+ "enumerateWithError:handler:"
+ "[%!{(MISSING)public}@] Could not fetch notification last shown date with error: %!@(MISSING)"
+ "UUIDString"
+ "hk_isBeforeDate:"
+ "initWithFeatureAvailabilityProviding:healthDataSource:"
+ "_typeWithIdentifier:"
+ "com.apple.hid.bd.sleepnotification"
+ "hk_error:format:"
+ "submitEvent:completion:"
+ "v32@0:8q16d24"
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_BODY_WATCH_UNSUPPORTED_REGION"
+ "@?16@0:8"
+ "HKCountrySet+SleepApneaNotifications.m"
+ "areAllRequirementsSatisfied"
+ "initWithCountryBitmasks:compatibilityVersion:contentVersion:provenance:"
+ "_sleepApneaNotificationsAvailabilityManager"
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_BODY"
+ "initWithArray:"
+ "initWithProfile:featureStatusProvider:"
+ "makeIHAGatedEventPayloadWithDataSource:error:"
+ "notificationManager"
+ "DeviceSupportsBreathingDisturbancesMeasurements"
+ "[%!{(MISSING)public}@] Number of analysis attempts: %!l(MISSING)d."
+ "createTaskServerWithUUID:configuration:client:delegate:error:"
+ "deviceManager"
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_BODY_REMOTELY_DISABLED"
+ "_currentDateProvider"
+ "_sendAnalyticsWithPayload:"
+ "defaultOnboardingEligibilityRequirementsForFeatureIdentifier:"
+ "@\"HDProtectedDataOperation\""
+ "_useTimeIntervalOverride"
+ "earliestDateOfAnyOnboardingCompletion"
+ "sortDescriptorWithKey:ascending:"
+ "[%!{(MISSING)public}@] Using time interval override of %!f(MISSING)."
+ "com.apple.health.Sleep.SleepApneaRescindedNotification"
+ "performBreathingDisturbanceAnalysisWithIsForced:date:numberOfAnalysisAttempts:"
+ "v24@0:8@?16"
+ "capabilityIsSupportedOnActiveWatchForFeatureWithIdentifier:supportedOnLocalDevice:"
+ "@\"<HKFeatureAvailabilityProviding>\""
+ "_rescindedNotificationManager"
+ "initWithProfile:featureStatusProvider:featureAvailabilityProviding:currentDateProvider:protectedDataOperation:profileDidBecomeReadyBlock:"
+ "v32@0:8@\"HDPeriodicActivity\"16@?<v@?qd@\"NSError\">24"
+ "[%!{(MISSING)public}@] Successfully wrote possible sleep apnea event sample with source %!@(MISSING)"
+ "_createEnumeratorWithAnalysisInterval:profile:"
+ "A"
+ "configurationClass"
+ "connection"
+ "initWithProfile:featureStatusProvider:featureAvailabilityProviding:currentDateProvider:"
+ "[%!{(MISSING)public}@] Number of days since last analysis: %!l(MISSING)d"
+ "isImproveHealthAndActivityEnabled"
+ "initWithUUIDString:"
+ "wristDetectionIsEnabledForActiveWatch"
+ "_sampleWithHighestDurationWithFirstSample:secondSample:"
+ "\x03"
+ "[%!{(MISSING)public}@] Successfully performed analysis! Attempting to update count."
+ "_areNotificationsEnabled"
+ "_writeDateOfMostRecentSuccessfulAnalysisAttempt"
+ "prerequisiteFeaturesAreOnWithFeatureSettings:"
+ "setTitle:"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
+ "@\"HDSHBreathingDisturbanceAnalysisScheduler\""
+ "activity"
+ "currentDeviceEntityWithError:"
+ "fetchSamplesWithAnalysisInterval:profile:error:"
+ "initWithAllowedCountriesDataSource:profile:featureCapability:loggingCategory:"
+ "initWithLoggingCategory:healthDataSource:"
+ "client"
+ "copy"
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_TITLE_WATCH_UNSUPPORTED_REGION"
+ "T@\"HDSHBreathingDisturbanceAnalysisScheduler\",&,N,V_breathingDisturbanceAnalysisScheduler"
+ "[%!{(MISSING)public}@] Request was not processed with error: %!@(MISSING)\nWill try analysis again in a day."
+ "hdsh_sleepApneaNotificationsAvailabilityManagerWithProfile:"
+ "_requestBreathingDisturbanceAnalysisIfNeeded"
+ "\x14$\x12"
+ "@\"NSCalendar\""
+ "[%!{(MISSING)public}@] Unexpected activity received; not setting activity criteria."
+ "_unitTesting_profileDidBecomeReadyBlock"
+ "setUserInfo:"
+ "@40@0:8@16@24@32"
+ "_sendPossibleSleepApneaNotificationWithRequest:"
+ "v32@0:8@\"HDPeriodicActivity\"16@\"NSObject<OS_xpc_object>\"24"
+ "[%!{(MISSING)public}@] Failed to write updated count of analysis attempts with error: %!@(MISSING)\nWill retry this window in one day."
+ "_cachedCalendar"
+ "setNumber:forKey:error:"
+ "[%!{(MISSING)public}@] Number of expected analysis attempts: %!l(MISSING)d"
+ "[%!{(MISSING)public}@] Received nil onboarding record. Will assume feature is not onboarded."
+ "i"
+ "capabilityIsSupportedOnActiveRemoteDeviceForFeatureWithIdentifier:"
+ "featureStatusWithError:"
+ "removeValuesForKeys:error:"
+ "v48@0:8@\"HDProtectedDataOperation\"16@\"HDProfile\"24@\"HDAssertion\"32@?<v@?>40"
+ "onboardingState"
+ "[%!{(MISSING)public}@] Request was not processed with error: %!@(MISSING)"
+ "hk_morningIndexWithCalendar:"
+ "isAppleWatch"
+ "localDeviceSourceWithError:"
+ "setPredicate:"
+ "setWithObject:"
+ "_registerUITriggers"
+ "someRegionIsSupportedForFeatureWithIdentifier:"
+ "[%!{(MISSING)public}@] Unexpected activity received; not performing activity."
+ "setSortDescriptors:"
+ "D6770323-EBBB-4867-A1A7-99F207C64094"
+ "HDSHSleepApneaRescindedNotificationManager"
+ "[%!{(MISSING)public}@] Error writing last shown date for notification: %!@(MISSING)"
+ "B24@0:8@\"HDPeriodicActivity\"16"
+ "_value"
+ "featureOnboardingRecordWithError:"
+ "localizedUserNotificationStringForKey:arguments:"
+ "numberOfExpectedAnalysisAttemptsStartingFromAnchorDate:referenceDate:calendar:"
+ "setObject:atIndexedSubscript:"
+ "@?"
+ "B40@0:8@16@24@32"
+ "subarrayWithRange:"
+ "[%!{(MISSING)public}@] Checking feature status for rescinded reasons: %!@(MISSING)"
+ "setUnitTesting_postNotificationHandler:"
+ "T@\"NSString\",R,N"
+ "initWithProfile:featureStatusProvider:queueOverride:"
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_TITLE_SEED_EXPIRED"
+ "_unitTesting_postNotificationHandler"
+ "com.apple.healthd.sleep.breathingdisturbanceanalysisactivity"
+ "q"
+ "@\"HDFeatureAvailabilityManager\""
+ "endDate"
+ "v48@0:8@16@24@32@?40"
+ "_deregisterUITriggers"
+ "T@\"HDPeriodicActivity\",R,N,V_activity"
+ "makeUnrestrictedEventPayloadWithDataSource:error:"
+ "setDay:"
+ "initWithFeatureIdentifier:defaultCountrySet:healthDaemon:"
+ "name"
+ "[%!{(MISSING)public}@] Error resetting last shown date for notification: %!@(MISSING)"
+ "_analysisScheduler"
+ "_queue_checkFeatureStatus"
+ "SLEEP_APNEA_REENABLED_NOTIFICATION_BODY"
+ "[%!{(MISSING)public}@] Overriding old time interval of %!f(MISSING) with new time interval of %!f(MISSING)."
+ "overrideAnalysisTimeIntervalAndResetActivityWithTimeInterval:"
+ "HKFeatureAvailabilityProvidingObserver"
+ "[%!{(MISSING)public}@] Periodic activity interval has been met."
+ "[%!{(MISSING)public}@] Wrote date of last analysis attempt: %!@(MISSING)"
+ "countryIsSupportedOnLocalDeviceForFeatureWithIdentifier:"
+ "[%!{(MISSING)public}@] Unexpected operation received; not performing operation."
+ "_triggerObserver"
+ "[%!{(MISSING)public}@] Constructed query for breathing disturbance samples with analysis window for start date: %!@(MISSING), end date: %!@(MISSING)"
+ "featureAvailabilityProvidingDidUpdateOnboardingCompletion:"
+ "[%!{(MISSING)public}@] Error fetching number of analysis attempts: %!@(MISSING)."
+ "@64@0:8@16@24@32@40@48@56"
+ "BreathingDisturbanceAnalysisProtectedDataOperation"
+ ", "
+ "_isFeatureUnavailableForNonRescindedReasonWithRequirementsEvaluation:"
+ "breathingDisturbanceAnalysisScheduler"
+ "featureFlagIsEnabled:"
+ "initWithFeatureIdentifier:localFeatureAttributes:localCountrySetAvailabilityProvider:"
+ "[%!{(MISSING)public}@] Onboarding record has updated. Recalculating activity criteria."
+ "_featureStatusProvider"
+ "_protectedDataOperation"
+ "analyzeSamples:dateInterval:"
+ "features"
+ "B"
+ "components:fromDate:toDate:options:"
+ "setBreathingDisturbanceAnalysisScheduler:"
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_TITLE"
+ "samplesFilteredBySleepDay:"
+ "[%!{(MISSING)public}@] Date write failed while performing analysis."
+ "[%!{(MISSING)public}@] Error attempting to send analytics payload: %!@(MISSING)"
+ "\x04\x12"
+ "environmentDataSource"
+ "onboardingRecordIsNotPresentForFeatureWithIdentifier:"
+ "remote_getBreathingDisturbanceSamplesInDateInterval:completion:"
+ "@\"HDKeyValueDomain\""
+ "[%!{(MISSING)public}@] Could not get breathing disturbance samples with error: %!@(MISSING)"
+ "_analysisTimeInterval"
+ "activeRemoteDeviceIsPresentWhenRequiredForRegionAvailabilityOrDeviceCapabilityForFeatureWithIdentifier:"
+ "46F59960-D16A-4E76-B7D1-A1B0BBC73923"
- "\x01\x11"

```
