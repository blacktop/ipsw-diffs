## SleepHealthDaemon

> `/System/Library/PrivateFrameworks/SleepHealthDaemon.framework/SleepHealthDaemon`

```diff

 5139.0.1.11.0
-  __TEXT.__text: 0x4890
-  __TEXT.__auth_stubs: 0x420
-  __TEXT.__objc_methlist: 0x2f8
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
+ _HKFeatureAvailabilityContextOnboardingPromotion
+ _OBJC_CLASS_$_HKFeatureAvailabilityRequirements
+ _HKSampleSortIdentifierStartDate
+ _OBJC_CLASS_$_HDPrimaryProfile
+ ___NSArray0__struct
+ _xpc_dictionary_set_int64
+ _OBJC_CLASS_$_UNMutableNotificationSound
+ _HKSHBreathingDisturbanceAnalysisSchedulerSuccessfulAnalysisAttemptCountKey
+ _HKSHSleepApneaNotificationCategoryRescindedSeedExpired
+ _OBJC_CLASS_$_HDSHBreathingDisturbanceAnalysisScheduler
+ _OBJC_CLASS_$_HKFeatureAvailabilityRequirementFeatureSetting
+ _HKSHSleepApneaNotificationCategoryRescindedRemoteDisabled
+ _HKSleepApneaNotificationsFeatureVersion
+ _os_unfair_lock_unlock
+ _HKIsAgeGatedUserDefaultsSleepApneaNotificationsKey
+ _HKSHSleepApneaNotificationCategoryRescindedNoLongerSupportedOnLocalDevice
+ _HKSHCreatePossibleSleepApneaDetectedNotificationRequest
+ _OBJC_METACLASS_$_HDSHBreathingDisturbanceAnalysisScheduler
+ _OBJC_METACLASS_$_HDSHSleepApneaControlServer
+ _OBJC_CLASS_$__HKBehavior
+ _HKFeatureIdentifierSleepApneaNotifications
+ _os_unfair_lock_lock
+ _HKCategoryTypeIdentifierSleepApneaEvent
+ _HKFeatureAvailabilityContextSettingsUserInteractionEnabled
+ _HKFeatureAvailabilityRequirementIdentifierCountryIsSupportedOnActiveRemoteDevice
+ _HKSHSleepApneaNotificationRequestIdentifier
+ _objc_retain_x3
+ _objc_retain_x26
+ _OBJC_CLASS_$_HKCountrySet
+ _HKCreateSerialUtilityDispatchQueue
+ _OBJC_CLASS_$_HDPairedFeaturePropertiesSyncManager
+ _OBJC_CLASS_$_HDWatchAndCompanionCountrySetIntersectionAvailabilityProvider
+ __dispatch_main_q
+ _xpc_dictionary_set_bool
+ _OBJC_CLASS_$_HKFeatureAvailabilityRequirementSet
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_HKAnalyticsEventSubmissionManager
+ _HDSHSleepApneaRescindedNotificationDateShownKey
+ _OBJC_CLASS_$_HDLocalCountrySetAvailabilityProvider
+ _OBJC_METACLASS_$_HDSHSleepApneaRescindedNotificationManager
+ _XPC_ACTIVITY_REPEATING
+ _HKSHSleepApneaControlClientInterface
+ _OBJC_CLASS_$_UNMutableNotificationContent
+ _OBJC_CLASS_$_UNNotificationRequest
+ _OBJC_METACLASS_$_HDSHBreathingDisturbanceAnalyzer
+ _XPC_ACTIVITY_ALLOW_BATTERY
+ _MGGetBoolAnswer
+ _objc_setProperty_nonatomic_copy
+ _OBJC_CLASS_$_HKFeatureAttributes
+ _XPC_ACTIVITY_INTERVAL_1_DAY
+ _HKSHSleepApneaControlServerInterface
+ __ProtectedOperationDebugIdentifier
+ _HKFeatureAvailabilityRequirementIdentifierCountryIsSupportedOnLocalDevice
+ _HKFeatureAvailabilityRequirementIdentifierSeedIsNotExpired
+ _kHKNotificationsDomainKey
+ _objc_retain_x5
+ _HKSHBreathingDisturbanceAnalysisSchedulerLastSuccessfulAnalysisAttemptDateKey
+ _OBJC_CLASS_$_HDSHBreathingDisturbanceAnalyzer
+ _OBJC_CLASS_$_NSDictionary
+ _HKMetadataKeyAlgorithmVersion
+ _OBJC_CLASS_$_HDFeatureAvailabilityManager
+ _OBJC_CLASS_$_HDPeriodicActivity
+ _OBJC_CLASS_$_HKFeatureStatusManager
+ _OBJC_CLASS_$_NSConstantArray
+ _HKFeatureAvailabilityContextUsage
+ _HKSleepApneaNotificationswatchOSDeviceIdentifierPortion
+ _OBJC_CLASS_$_HKTaskConfiguration
+ __os_log_fault_impl
+ _HKSHBreathingDisturbanceAnalysisWindowLength
+ _OBJC_CLASS_$_HDOTAFeatureDisableAndExpiryProvider
+ _OBJC_CLASS_$_NSCalendar
+ _HKQuantityTypeIdentifierAppleSleepingBreathingDisturbances
+ _OBJC_CLASS_$_NSSortDescriptor
+ _OBJC_CLASS_$_NSUUID
+ _HKSPCurrentDateProvider
+ _OBJC_CLASS_$_BABreathingDisturbanceAnalyzer
+ _OBJC_CLASS_$_HDProtectedDataOperation
+ _OBJC_CLASS_$_NSDateInterval
+ _HKFeatureAvailabilityContextOnboardingInitiation
+ _HKSleepApneaNotificationsiOSDeviceIdentifierPortion
+ _XPC_ACTIVITY_INTERVAL
+ _OBJC_CLASS_$_NSDateComponents
+ _HKFeatureIdentifierSleepTracking
+ _HKSHSleepApneaControlServerIdentifier
+ _HKFeatureAvailabilityRequirementIdentifierFeatureIsNotRemotelyDisabled
+ _HKSHBreathingDisturbanceKeyValueDomainName
+ _HKSHSleepApneaNotificationCategoryFeatureIsAvailableAgainAndEnabled
+ _objc_retain_x4
+ _HKSHSleepApneaNotificationCategoryRescindedNoLongerSupportedOnActiveRemoteDevice
+ _HKFeatureAvailabilityContextSettingsVisibility
+ _OBJC_CLASS_$_HDSHSleepApneaControlServer
+ _OBJC_CLASS_$_HDSHSleepApneaRescindedNotificationManager
CStrings:
+ "_writeDateOfMostRecentSuccessfulAnalysisAttempt"
+ "seedIsNotExpiredForFeatureWithIdentifier:"
+ "hk_error:format:"
+ "initWithProfile:featureStatusProvider:queueOverride:"
+ "[%!{(MISSING)public}@] Number of analysis attempts: %!l(MISSING)d."
+ "capabilityIsSupportedOnActiveRemoteDeviceForFeatureWithIdentifier:"
+ "initWithCountryBitmasks:compatibilityVersion:contentVersion:provenance:"
+ "@64@0:8@16@24@32@?40@48@?56"
+ "HKFeatureAvailabilityProvidingObserver"
+ "[%!{(MISSING)public}@] Could not write date of last analysis attempt with error %!@(MISSING)"
+ "onboardingState"
+ "[%!{(MISSING)public}@] Error posting rescinded notification: %!@(MISSING)"
+ "defaultOnboardingEligibilityRequirementsForFeatureIdentifier:"
+ "numberOfExpectedAnalysisAttemptsStartingFromAnchorDate:referenceDate:calendar:"
+ "@\"HDSHBreathingDisturbanceAnalyzer\""
+ "[%!{(MISSING)public}@] Fetched %!l(MISSING)u samples, filtered to %!l(MISSING)u samples."
+ "now"
+ "TB,R,N"
+ "_areNotificationsEnabled"
+ "endDateFromMostRecentlyAnalyzedDateIntervalWithDate:numberOfAnalysisAttempts:calendar:"
+ "initWithStartDate:endDate:"
+ "makeUnrestrictedEventPayloadWithDataSource:error:"
+ "samplesFilteredBySleepDay:"
+ "@\"HDKeyValueDomain\""
+ "featureAvailabilityProvidingDidUpdateOnboardingCompletion:"
+ "overrideAnalysisTimeIntervalAndResetActivityWithTimeInterval:"
+ "@\"NSDictionary\"32@0:8@\"HKAnalyticsDataSource\"16^@24"
+ "[%!{(MISSING)public}@] Failed to write sleep apnea event sample with error: %!@(MISSING). Not sending notification and will attempt to retry in one day."
+ "initWithProfile:name:interval:delegate:loggingCategory:"
+ "v32@0:8@\"HDPeriodicActivity\"16@\"NSObject<OS_xpc_object>\"24"
+ "@\"HDFeatureAvailabilityManager\""
+ "@64@0:8@16@24@32@40@48@56"
+ "initWithAllowedCountriesDataSource:profile:featureCapability:loggingCategory:"
+ "_unitTesting_postNotificationHandler"
+ "enumerateWithError:handler:"
+ "B40@0:8@16@24@32"
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_BODY_SEED_EXPIRED"
+ "featureIsNotRemotelyDisabledWithIdentifier:"
+ "setWithObject:"
+ "wristDetectionIsEnabledForActiveWatch"
+ "[%!{(MISSING)public}@] Request was not processed with error: %!@(MISSING)\nWill try analysis again in a day."
+ "featureStatusWithError:"
+ "setSortDescriptors:"
+ "setUserInfo:"
+ "@\"HDSHSleepApneaNotificationUITriggerObserver\""
+ "[%!{(MISSING)public}@] Error resetting last shown date for notification: %!@(MISSING)"
+ "\x03"
+ "[%!{(MISSING)public}@] Unexpected activity received; not performing activity."
+ "setUnitTesting_postNotificationHandler:"
+ "@\"HDProtectedDataOperation\""
+ "T@\"NSString\",R,N"
+ "[%!{(MISSING)public}@] Successfully wrote possible sleep apnea event sample with source %!@(MISSING)"
+ "_requestBreathingDisturbanceAnalysisWithSamples:analysisInterval:"
+ "featureStatusProviding:didUpdateFeatureStatus:"
+ "quantityTypeForIdentifier:"
+ "registerObserver:queue:"
+ "initWithDefaultAnalyticsPayload:"
+ "components:fromDate:toDate:options:"
+ "B"
+ "[%!{(MISSING)public}@] Overriding old time interval of %!f(MISSING) with new time interval of %!f(MISSING)."
+ "activeRemoteDeviceIsPresentWhenRequiredForRegionAvailabilityOrDeviceCapabilityForFeatureWithIdentifier:"
+ "i"
+ "nebula"
+ "@\"NSDictionary\""
+ "_value"
+ "initWithDictionary:"
+ "initWithProfile:featureStatusProvider:"
+ "initWithProfile:featureStatusProvider:featureAvailabilityProviding:currentDateProvider:protectedDataOperation:profileDidBecomeReadyBlock:"
+ "performPeriodicActivity:completion:"
+ "@\"HKAnalyticsEventSubmissionManager\""
+ "@?16@0:8"
+ "B32@?0@\"HKObject\"8q16^@24"
+ "[%!{(MISSING)public}@] Possible sleep apnea NOT detected from breathing disturbance samples."
+ "[%!{(MISSING)public}@] Request was processed, but completion exists before capture."
+ "[%!{(MISSING)public}@] Using time interval override of %!f(MISSING)."
+ "_isFeatureRescindedWithRequirementsEvaluation:"
+ "initWithRequirementsByContext:"
+ "[%!{(MISSING)public}@] Sleep apnea notifications are rescinded. Notification was last shown: %!@(MISSING)"
+ "@\"HDSHSleepApneaRescindedNotificationManager\""
+ "_completion"
+ "configurationClass"
+ "HDSHSleepApneaControlServer"
+ "SLEEP_APNEA_REENABLED_NOTIFICATION_BODY"
+ "_categoryIdentifierFromRescindedReason:"
+ "_sampleWithHighestDurationWithFirstSample:secondSample:"
+ "_createEnumeratorWithAnalysisInterval:profile:"
+ "_isFeatureUnavailableForNonRescindedReasonWithRequirementsEvaluation:"
+ "isAnalysisNeededWithAnchorDate:referenceDate:calendar:"
+ "localDeviceSourceWithError:"
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_TITLE_REMOTELY_DISABLED"
+ "_clientRemoteObjectProxy"
+ "com.apple.health.Sleep.SleepApneaRescindedNotification"
+ "initWithProfile:debugIdentifier:delegate:"
+ "eventName"
+ "profileIsNotFamilySetupPairingProfile"
+ "_featureStatusProvider"
+ "constructAnalysisDateIntervalFromDate:withCalendar:"
+ "[%!{(MISSING)public}@] Onboarding record has updated. Recalculating activity criteria."
+ "initWithArray:"
+ "setTitle:"
+ "@32@0:8@16@24"
+ "_analysisScheduler"
+ "countryIsSupportedOnLocalDeviceForFeatureWithIdentifier:"
+ "periodicActivityRequiresProtectedData:"
+ "setPredicate:"
+ "_isFeatureOnboardedWithFeatureOnboardingRecord:"
+ "countryIsSupportedOnActiveRemoteDeviceForFeatureWithIdentifier:isSupportedIfCountryListMissing:"
+ "BreathingDisturbanceAnalysisProtectedDataOperation"
+ "@\"<HKFeatureStatusProviding>\""
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_TITLE_WATCH_UNSUPPORTED_REGION"
+ "[%!{(MISSING)public}@] Error getting feature status: %!@(MISSING)"
+ "[%!{(MISSING)public}@] Error posting notification: %!@(MISSING)"
+ "[%!{(MISSING)public}@] Possible sleep apnea detected from breathing disturbance samples."
+ "onboardingRecordIsNotPresentForFeatureWithIdentifier:"
+ "subarrayWithRange:"
+ "_sendAnalyticsWithPayload:"
+ "performBreathingDisturbanceAnalysisWithIsForced:date:numberOfAnalysisAttempts:"
+ "remote_forceBreathingDisturbanceAnalysis"
+ "v48@0:8@16@24@32@?40"
+ "[%!{(MISSING)public}@] Failed to perform successful analysis.\nWill retry in one day."
+ "[%!{(MISSING)public}@] Request was not processed with error: %!@(MISSING)"
+ "_updateActivityCriteriaAndResetActivity"
+ "[%!{(MISSING)public}@] Analysis successfully performed!"
+ "_currentDateProvider"
+ "analyzeSamples:dateInterval:"
+ "A"
+ "_completionLock"
+ "_writePossibleSleepApneaNotificationSampleWithAnalysisInterval:algorithmVersion:error:"
+ "HDPeriodicActivityDelegate"
+ "[%!{(MISSING)public}@] Unexpected activity received; not setting activity criteria."
+ "earliestDateOfAnyOnboardingCompletion"
+ "fetchSamplesWithAnalysisInterval:profile:error:"
+ "periodicActivity:configureXPCActivityCriteria:"
+ "@?"
+ "[%!{(MISSING)public}@] Feature is disabled; not going to check if analysis is overdue."
+ "_rescindedNotificationManager"
+ "featureIsOnWithIdentifier:isOnIfSettingIsAbsent:"
+ "initWithFeatureIdentifier:defaultCountrySet:healthDaemon:"
+ "isImproveHealthAndActivityEnabled"
+ "removeValuesForKeys:error:"
+ "v24@0:8@\"<HKFeatureAvailabilityProviding>\"16"
+ "dateByAddingComponents:toDate:options:"
+ "initWithFeatureIdentifier:localFeatureAttributes:localCountrySetAvailabilityProvider:"
+ "setCategoryIdentifier:"
+ "HDSHSleepApneaRescindedNotificationDateShownKey"
+ "HKAnalyticsEvent"
+ "activity"
+ "environmentDataSource"
+ "healthAppIsNotHidden"
+ "T@?,C,N,V_unitTesting_postNotificationHandler"
+ "areAllRequirementsSatisfied"
+ "remoteObjectProxy"
+ "@\"<HKFeatureAvailabilityProviding>\""
+ "[%!{(MISSING)public}@] Got nil onboarding date, not checking if analysis is overdue."
+ "[%!{(MISSING)public}@] Successfully sent analytics payload!"
+ "localizedUserNotificationStringForKey:arguments:"
+ "onboardingRecordIsPresentForFeatureWithIdentifier:"
+ "setDate:"
+ "v32@0:8@\"HDPeriodicActivity\"16@?<v@?qd@\"NSError\">24"
+ "setBody:"
+ "UUIDString"
+ "createTaskServerWithUUID:configuration:client:delegate:error:"
+ "featureAvailabilityProvidingDidUpdateSettings:"
+ "[%!{(MISSING)public}@] Wrote date of last analysis attempt: %!@(MISSING)"
+ "highestPriorityUnsatisfiedRequirement"
+ "setObject:atIndexedSubscript:"
+ "46F59960-D16A-4E76-B7D1-A1B0BBC73923"
+ "_defaultAnalyticsPayload"
+ "_runCompletionIfExistsWithResult:retryInterval:"
+ "hdsh_sleepApneaNotificationsAvailabilityManagerWithProfile:"
+ "updateCriteria"
+ "B36@0:8B16@20q28"
+ "dictionary"
+ "requestWithIdentifier:content:trigger:"
+ "v24@0:8@?16"
+ "HDSHSleepApneaNotificationUITriggerObserver"
+ "_rescindedRequirementIdentifiers"
+ "[%!{(MISSING)public}@] Number of days since last analysis: %!l(MISSING)d"
+ "_getEarliestOnboardingDate"
+ "v48@0:8@\"HDProtectedDataOperation\"16@\"HDProfile\"24@\"HDAssertion\"32@?<v@?>40"
+ "requestWorkWithPriority:error:"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
+ "connection"
+ "unitTesting_postNotificationHandler"
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_TITLE_SEED_EXPIRED"
+ "breathingDisturbanceAnalysisScheduler"
+ "day"
+ "B24@0:8@\"HDPeriodicActivity\"16"
+ "componentsJoinedByString:"
+ "D6770323-EBBB-4867-A1A7-99F207C64094"
+ "_keyValueDomain"
+ "v32@0:8q16d24"
+ "[%!{(MISSING)public}@] About to show rescinded notification for sleep apnea notifications."
+ "[%!{(MISSING)public}@] Successfully performed analysis! Attempting to update count."
+ "[%!{(MISSING)public}@] With date %!@(MISSING) and number of analysis attempts %!l(MISSING)d, end date of most recently analyzed date interval is %!@(MISSING)."
+ "_deregisterUITriggers"
+ "synchronizeLocalProperties"
+ "client"
+ "copy"
+ "entityEnumeratorWithType:profile:"
+ "remote_overridePreviousTimeIntervalWithTimeInterval:"
+ "\x14$\x12"
+ "_showRescindedNotificationWithTitleAndBodyKeys:rescindedReason:"
+ "_triggerObserver"
+ "soundWithAlertType:"
+ "\x14"
+ "[%!{(MISSING)public}@] Failed to write updated count of analysis attempts with error: %!@(MISSING)\nWill retry this window in one day."
+ "categorySampleWithType:value:startDate:endDate:metadata:"
+ "HDSHBreathingDisturbanceAnalysisScheduler"
+ "HKCountrySet+SleepApneaNotifications.m"
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_BODY_WATCH_UNSUPPORTED_REGION"
+ "_typeWithIdentifier:"
+ "[%!{(MISSING)public}@] About to post possible sleep apnea detected notification."
+ "@\"HDSHBreathingDisturbanceAnalysisScheduler\""
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_BODY_REMOTELY_DISABLED"
+ "_localKeyValueDomain"
+ "isEventSubmissionIHAGated"
+ "v32@0:8@\"NSDateInterval\"16@?<v@?@\"NSArray\">24"
+ "initWithDaemon:featureIdentifier:"
+ "postNotificationWithRequest:completion:"
+ "v24@0:8d16"
+ "_breathingDisturbanceAnalysisScheduler"
+ "initWithFeatureIdentifier:isOnWhenSettingIsAbsent:"
+ "_featureAvailabilityProviding"
+ "initWithLoggingCategory:healthDataSource:"
+ "_areSamplesInSameSleepDayWithFirstSample:secondSample:calendar:"
+ "objectAtIndexedSubscript:"
+ "_requestBreathingDisturbanceAnalysisIfNeeded"
+ "v32@0:8@\"<HKFeatureStatusProviding>\"16@\"HKFeatureStatus\"24"
+ "@40@0:8@16@24^@32"
+ "_analyzer"
+ "@56@0:8@16@24@32@40^@48"
+ "[%!{(MISSING)public}@] Activity criteria will be updated and reset."
+ "[%!{(MISSING)public}@] Could not get breathing disturbance samples with error: %!@(MISSING)"
+ "[%!{(MISSING)public}@] Error writing last shown date for notification: %!@(MISSING)"
+ "[%!{(MISSING)public}@] Periodic activity interval has been met."
+ "[%!{(MISSING)public}@] Received nil onboarding record. Will assume feature is not onboarded."
+ "[%!{(MISSING)public}@] User is not onboarded in a supported region."
+ "setBreathingDisturbanceAnalysisScheduler:"
+ "[%!{(MISSING)public}@] Error fetching number of analysis attempts: %!@(MISSING)."
+ "hk_morningIndexWithCalendar:"
+ "performWorkForOperation:profile:databaseAccessibilityAssertion:completion:"
+ "requirementsEvaluationByContext"
+ "HDSHSleepApneaRescindedNotificationManager"
+ "initWithProfile:featureIdentifier:availabilityRequirements:currentOnboardingVersion:pairedDeviceCapability:pairedFeatureAttributesProvider:regionAvailabilityProvider:disableAndExpiryProvider:loggingCategory:"
+ "@40@0:8@16q24@32"
+ "bd_count"
+ "com.apple.hid.bd.sleepnotification"
+ "debugIdentifier"
+ "localAvailabilityForSleepApneaNotifications"
+ "HDSHBreathingDisturbanceAnalyzer"
+ "[%!{(MISSING)public}@] Feature status changed to: %!@(MISSING)"
+ "featureAttributesDerivedFromOSBuildAndFeatureVersion:watchDeviceIdentifier:phoneDeviceIdentifier:"
+ "notificationManager"
+ "_unitTesting_profileDidBecomeReadyBlock"
+ "hk_gregorianCalendar"
+ "hk_sleepDayStartWithCalendar:"
+ "q"
+ "submitEvent:completion:"
+ "@\"NSCalendar\""
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_BODY_UNSUPPORTED_REGION"
+ "deviceManager"
+ "currentDeviceEntityWithError:"
+ "name"
+ "[%!{(MISSING)public}@] Feature status is nil with error: %!@(MISSING)"
+ "[%!{(MISSING)public}@] Number of expected analysis attempts: %!l(MISSING)d"
+ "currentCalendar"
+ "DeviceSupportsBreathingDisturbancesMeasurements"
+ "[%!{(MISSING)public}@] Analysis is needed. Analyzing over date intervals that have not been analyzed."
+ "_activity"
+ "_analyticsEventSubmissionManager"
+ "hk_dateByAddingDays:toDate:"
+ "setNumber:forKey:error:"
+ "sharedBehavior"
+ "unsatisfiedRequirementIdentifiers"
+ "[%!{(MISSING)public}@] Unexpectedly filtered to more than %!d(MISSING) samples, will only return that amount starting from the first sample."
+ "_registerUITriggers"
+ "@48@0:8@16@24@32@?40"
+ "_useTimeIntervalOverride"
+ "featureOnboardingRecordWithError:"
+ "_analysisTimeInterval"
+ "features"
+ "initWithFeatureAvailabilityProviding:healthDataSource:"
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_BODY"
+ "someRegionIsSupportedForFeatureWithIdentifier:"
+ "v32@0:8@16@?24"
+ "HKFeatureStatusProvidingObserver"
+ "[%!{(MISSING)public}@] Error attempting to send analytics payload: %!@(MISSING)"
+ "@\"HDPeriodicActivity\""
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_TITLE"
+ ", "
+ "T@\"HDSHBreathingDisturbanceAnalysisScheduler\",&,N,V_breathingDisturbanceAnalysisScheduler"
+ "HDProtectedDataOperationDelegate"
+ "_cachedCalendar"
+ "T@\"HDPeriodicActivity\",R,N,V_activity"
+ "[%!{(MISSING)public}@] Sleep apnea notifications are unavailable for non-rescinded reasons."
+ "dictionaryWithObjects:forKeys:count:"
+ "\x04\x12"
+ "HDSHBreathingDisturbanceAnalysisAnalyticsEvent"
+ "[%!{(MISSING)public}@] Checking feature status for non-rescinded reasons: %!@(MISSING)"
+ "_queue_checkFeatureStatus"
+ "endDate"
+ "initWithProfile:featureStatusProvider:featureAvailabilityProviding:currentDateProvider:"
+ "prerequisiteFeaturesAreOnWithFeatureSettings:"
+ "validateConfiguration:client:error:"
+ "HKSHSleepApneaControlServer"
+ "featureAvailabilityProvidingDidUpdatePairedDeviceCapability:"
+ "Profile extension not found for class %!@(MISSING)"
+ "[%!{(MISSING)public}@] Analysis is not needed."
+ "featureFlagIsEnabled:"
+ "[%!{(MISSING)public}@] Checking feature status for rescinded reasons: %!@(MISSING)"
+ "[%!{(MISSING)public}@] Number of expected analysis attempts between %!@(MISSING) and %!@(MISSING) is: %!l(MISSING)d"
+ "isAppleWatch"
+ "[%!{(MISSING)public}@] Attempting to send analytics."
+ "_queue_sendNotificationRequestIfNeededWithFeatureStatus:"
+ "numberForKey:error:"
+ "[%!{(MISSING)public}@] Date write failed while performing analysis."
+ "_rescindedNotificationTitleAndBodyKeysWithHighestPriorityUnsatisfiedRequirementIdentifier:"
+ "_sleepApneaNotificationsAvailabilityManager"
+ "initWithUUIDString:"
+ "notAgeGatedForUserDefaultsKey:"
+ "_protectedDataOperation"
+ "arrayWithArray:"
+ "d"
+ "setExpirationDate:"
+ "[%!{(MISSING)public}@] Constructed query for breathing disturbance samples with analysis window for start date: %!@(MISSING), end date: %!@(MISSING)"
+ "hk_isBeforeDate:"
+ "sortDescriptorWithKey:ascending:"
+ "[%!{(MISSING)public}@] Error fetching onboarding record: %!@(MISSING)\nReturning nil onboarding date."
+ "com.apple.healthd.sleep.breathingdisturbanceanalysisactivity"
+ "setDay:"
+ "@40@0:8@16@24@32"
+ "Local generated country set should never be nil"
+ "capabilityIsSupportedOnActiveWatchForFeatureWithIdentifier:supportedOnLocalDevice:"
+ "[%!{(MISSING)public}@] Could not fetch notification last shown date with error: %!@(MISSING)"
+ "is_improve_health_and_activity_allowed"
+ "makeIHAGatedEventPayloadWithDataSource:error:"
+ "[%!{(MISSING)public}@] Unexpected operation received; not performing operation."
+ "remote_getBreathingDisturbanceSamplesInDateInterval:completion:"
+ "setSound:"
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_TITLE_UNSUPPORTED_REGION"
+ "[%!{(MISSING)public}@] Requesting analysis with %!l(MISSING)u samples and analysis interval of %!@(MISSING)"
+ "resetInterval"
+ "B32@0:8@16@24"
+ "initWithUUID:configuration:client:delegate:analyzer:analysisScheduler:"
+ "SLEEP_APNEA_REENABLED_NOTIFICATION_TITLE"
+ "SleepApneaNotifications"
+ "_sendPossibleSleepApneaNotificationWithRequest:"
+ "q40@0:8@16@24@32"
- "\x01\x11"

```
