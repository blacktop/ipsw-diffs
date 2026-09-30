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
+ _HKFeatureAvailabilityRequirementIdentifierCountryIsSupportedOnLocalDevice
+ _HKIsAgeGatedUserDefaultsSleepApneaNotificationsKey
+ _OBJC_CLASS_$_HDLocalCountrySetAvailabilityProvider
+ _OBJC_CLASS_$_UNMutableNotificationContent
+ _OBJC_CLASS_$_HKCountrySet
+ _os_unfair_lock_unlock
+ _OBJC_CLASS_$_NSCalendar
+ _HKSHSleepApneaControlServerIdentifier
+ _OBJC_CLASS_$_HDSHSleepApneaControlServer
+ _xpc_dictionary_set_int64
+ _HKFeatureIdentifierSleepTracking
+ _OBJC_CLASS_$_HDPeriodicActivity
+ _OBJC_CLASS_$_HDPrimaryProfile
+ _HKSleepApneaNotificationsiOSDeviceIdentifierPortion
+ _OBJC_METACLASS_$_HDSHSleepApneaControlServer
+ _XPC_ACTIVITY_INTERVAL
+ _OBJC_CLASS_$_NSError
+ _HKSHSleepApneaNotificationRequestIdentifier
+ _OBJC_CLASS_$_NSDictionary
+ _HKFeatureAvailabilityRequirementIdentifierSeedIsNotExpired
+ __os_log_fault_impl
+ _HKSHSleepApneaNotificationCategoryRescindedNoLongerSupportedOnActiveRemoteDevice
+ _HKSHBreathingDisturbanceAnalysisWindowLength
+ _HKSHBreathingDisturbanceKeyValueDomainName
+ _OBJC_CLASS_$_HDSHBreathingDisturbanceAnalyzer
+ _OBJC_CLASS_$_HKAnalyticsEventSubmissionManager
+ _HKSampleSortIdentifierStartDate
+ _HKFeatureAvailabilityContextSettingsVisibility
+ _XPC_ACTIVITY_REPEATING
+ _objc_retain_x5
+ _objc_setProperty_nonatomic_copy
+ _HKSHSleepApneaControlServerInterface
+ _HKSHBreathingDisturbanceAnalysisSchedulerSuccessfulAnalysisAttemptCountKey
+ _OBJC_CLASS_$_HDProtectedDataOperation
+ _OBJC_CLASS_$_HDSHBreathingDisturbanceAnalysisScheduler
+ _OBJC_CLASS_$_UNMutableNotificationSound
+ _HKCategoryTypeIdentifierSleepApneaEvent
+ _HKSHSleepApneaNotificationCategoryRescindedNoLongerSupportedOnLocalDevice
+ _HDSHSleepApneaRescindedNotificationDateShownKey
+ __ProtectedOperationDebugIdentifier
+ _OBJC_CLASS_$_HDPairedFeaturePropertiesSyncManager
+ ___NSArray0__struct
+ _HKSHSleepApneaNotificationCategoryFeatureIsAvailableAgainAndEnabled
+ _OBJC_CLASS_$_HKFeatureAvailabilityRequirementFeatureSetting
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_HDOTAFeatureDisableAndExpiryProvider
+ _HKFeatureAvailabilityContextUsage
+ _objc_retain_x26
+ _OBJC_CLASS_$_HDSHSleepApneaRescindedNotificationManager
+ _OBJC_CLASS_$_HKFeatureStatusManager
+ _OBJC_METACLASS_$_HDSHSleepApneaRescindedNotificationManager
+ _OBJC_CLASS_$_HKTaskConfiguration
+ _kHKNotificationsDomainKey
+ _HKFeatureAvailabilityContextOnboardingInitiation
+ _OBJC_CLASS_$_HKFeatureAttributes
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_HKFeatureAvailabilityRequirementSet
+ __dispatch_main_q
+ _OBJC_CLASS_$_HKFeatureAvailabilityRequirements
+ _OBJC_CLASS_$_NSDateComponents
+ _HKFeatureAvailabilityContextOnboardingPromotion
+ _HKFeatureIdentifierSleepApneaNotifications
+ _HKSleepApneaNotificationswatchOSDeviceIdentifierPortion
+ _HKCreateSerialUtilityDispatchQueue
+ _HKFeatureAvailabilityRequirementIdentifierFeatureIsNotRemotelyDisabled
+ _OBJC_CLASS_$_HDFeatureAvailabilityManager
+ _xpc_dictionary_set_bool
+ _OBJC_CLASS_$_UNNotificationRequest
+ _HKQuantityTypeIdentifierAppleSleepingBreathingDisturbances
+ _HKSPCurrentDateProvider
+ _XPC_ACTIVITY_ALLOW_BATTERY
+ _HKSHCreatePossibleSleepApneaDetectedNotificationRequest
+ _OBJC_CLASS_$_NSDateInterval
+ _OBJC_CLASS_$_NSSortDescriptor
+ _objc_retain_x3
+ _HKSHSleepApneaNotificationCategoryRescindedRemoteDisabled
+ _HKSHSleepApneaNotificationCategoryRescindedSeedExpired
+ _HKSleepApneaNotificationsFeatureVersion
+ _OBJC_METACLASS_$_HDSHBreathingDisturbanceAnalyzer
+ _HKFeatureAvailabilityContextSettingsUserInteractionEnabled
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$__HKBehavior
+ _HKSHBreathingDisturbanceAnalysisSchedulerLastSuccessfulAnalysisAttemptDateKey
+ _HKSHSleepApneaControlClientInterface
+ _os_unfair_lock_lock
+ _HKFeatureAvailabilityRequirementIdentifierCountryIsSupportedOnActiveRemoteDevice
+ _HKMetadataKeyAlgorithmVersion
+ _OBJC_CLASS_$_HDWatchAndCompanionCountrySetIntersectionAvailabilityProvider
+ _OBJC_METACLASS_$_HDSHBreathingDisturbanceAnalysisScheduler
+ _OBJC_CLASS_$_BABreathingDisturbanceAnalyzer
+ _XPC_ACTIVITY_INTERVAL_1_DAY
+ _objc_retain_x4
CStrings:
+ "@56@0:8@16@24@32@40^@48"
+ "T@\"HDSHBreathingDisturbanceAnalysisScheduler\",&,N,V_breathingDisturbanceAnalysisScheduler"
+ "@64@0:8@16@24@32@40@48@56"
+ "[%!{(MISSING)public}@] Error fetching number of analysis attempts: %!@(MISSING)."
+ "client"
+ "isEventSubmissionIHAGated"
+ "B32@?0@\"HKObject\"8q16^@24"
+ "registerObserver:queue:"
+ "synchronizeLocalProperties"
+ "v24@0:8@\"<HKFeatureAvailabilityProviding>\"16"
+ "[%!{(MISSING)public}@] Periodic activity interval has been met."
+ "featureIsNotRemotelyDisabledWithIdentifier:"
+ "B40@0:8@16@24@32"
+ "connection"
+ "dateByAddingComponents:toDate:options:"
+ "@\"HDSHBreathingDisturbanceAnalysisScheduler\""
+ "soundWithAlertType:"
+ "_breathingDisturbanceAnalysisScheduler"
+ "setUnitTesting_postNotificationHandler:"
+ "[%!{(MISSING)public}@] Constructed query for breathing disturbance samples with analysis window for start date: %!@(MISSING), end date: %!@(MISSING)"
+ "[%!{(MISSING)public}@] Unexpected operation received; not performing operation."
+ "[%!{(MISSING)public}@] Using time interval override of %!f(MISSING)."
+ "performWorkForOperation:profile:databaseAccessibilityAssertion:completion:"
+ "requestWithIdentifier:content:trigger:"
+ "HKFeatureStatusProvidingObserver"
+ "[%!{(MISSING)public}@] Fetched %!l(MISSING)u samples, filtered to %!l(MISSING)u samples."
+ "constructAnalysisDateIntervalFromDate:withCalendar:"
+ "initWithDaemon:featureIdentifier:"
+ "setBody:"
+ "v48@0:8@16@24@32@?40"
+ "@\"<HKFeatureStatusProviding>\""
+ "setBreathingDisturbanceAnalysisScheduler:"
+ "someRegionIsSupportedForFeatureWithIdentifier:"
+ "[%!{(MISSING)public}@] Error posting notification: %!@(MISSING)"
+ "_analysisScheduler"
+ "@\"NSCalendar\""
+ "[%!{(MISSING)public}@] Number of days since last analysis: %!l(MISSING)d"
+ "[%!{(MISSING)public}@] With date %!@(MISSING) and number of analysis attempts %!l(MISSING)d, end date of most recently analyzed date interval is %!@(MISSING)."
+ "countryIsSupportedOnLocalDeviceForFeatureWithIdentifier:"
+ "featureAvailabilityProvidingDidUpdatePairedDeviceCapability:"
+ "setUserInfo:"
+ "[%!{(MISSING)public}@] Error fetching onboarding record: %!@(MISSING)\nReturning nil onboarding date."
+ "endDate"
+ "sharedBehavior"
+ "[%!{(MISSING)public}@] Number of analysis attempts: %!l(MISSING)d."
+ "_isFeatureUnavailableForNonRescindedReasonWithRequirementsEvaluation:"
+ "_sendPossibleSleepApneaNotificationWithRequest:"
+ "featureStatusProviding:didUpdateFeatureStatus:"
+ "B32@0:8@16@24"
+ "HDSHSleepApneaRescindedNotificationDateShownKey"
+ "_featureStatusProvider"
+ "initWithProfile:featureStatusProvider:"
+ "profileIsNotFamilySetupPairingProfile"
+ "HDSHSleepApneaNotificationUITriggerObserver"
+ "T@\"NSString\",R,N"
+ "_sampleWithHighestDurationWithFirstSample:secondSample:"
+ "now"
+ "v32@0:8@16@?24"
+ "requirementsEvaluationByContext"
+ "isAppleWatch"
+ "_protectedDataOperation"
+ "_sendAnalyticsWithPayload:"
+ "healthAppIsNotHidden"
+ "A"
+ "[%!{(MISSING)public}@] Failed to perform successful analysis.\nWill retry in one day."
+ "@\"HDFeatureAvailabilityManager\""
+ "[%!{(MISSING)public}@] Requesting analysis with %!l(MISSING)u samples and analysis interval of %!@(MISSING)"
+ "[%!{(MISSING)public}@] Wrote date of last analysis attempt: %!@(MISSING)"
+ "dictionary"
+ "setWithObject:"
+ "D6770323-EBBB-4867-A1A7-99F207C64094"
+ "SLEEP_APNEA_REENABLED_NOTIFICATION_BODY"
+ "SleepApneaNotifications"
+ "activity"
+ "performPeriodicActivity:completion:"
+ "updateCriteria"
+ "day"
+ "initWithDefaultAnalyticsPayload:"
+ "initWithUUIDString:"
+ "HDSHSleepApneaControlServer"
+ "setDay:"
+ "@\"HDProtectedDataOperation\""
+ "seedIsNotExpiredForFeatureWithIdentifier:"
+ "@?16@0:8"
+ "Profile extension not found for class %!@(MISSING)"
+ "resetInterval"
+ "localAvailabilityForSleepApneaNotifications"
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_TITLE_REMOTELY_DISABLED"
+ "[%!{(MISSING)public}@] Unexpectedly filtered to more than %!d(MISSING) samples, will only return that amount starting from the first sample."
+ "[%!{(MISSING)public}@] User is not onboarded in a supported region."
+ "_value"
+ "numberOfExpectedAnalysisAttemptsStartingFromAnchorDate:referenceDate:calendar:"
+ "v32@0:8@\"<HKFeatureStatusProviding>\"16@\"HKFeatureStatus\"24"
+ "[%!{(MISSING)public}@] Analysis is not needed."
+ "features"
+ "localizedUserNotificationStringForKey:arguments:"
+ "setPredicate:"
+ "HKAnalyticsEvent"
+ "setDate:"
+ "initWithFeatureIdentifier:localFeatureAttributes:localCountrySetAvailabilityProvider:"
+ "initWithProfile:featureStatusProvider:featureAvailabilityProviding:currentDateProvider:"
+ "v24@0:8@?16"
+ "[%!{(MISSING)public}@] Possible sleep apnea NOT detected from breathing disturbance samples."
+ "@40@0:8@16q24@32"
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_TITLE_SEED_EXPIRED"
+ "_isFeatureOnboardedWithFeatureOnboardingRecord:"
+ "localDeviceSourceWithError:"
+ "submitEvent:completion:"
+ "@64@0:8@16@24@32@?40@48@?56"
+ "HDSHBreathingDisturbanceAnalyzer"
+ "_useTimeIntervalOverride"
+ "categorySampleWithType:value:startDate:endDate:metadata:"
+ "_typeWithIdentifier:"
+ "_currentDateProvider"
+ "highestPriorityUnsatisfiedRequirement"
+ "remoteObjectProxy"
+ "@\"NSDictionary\"32@0:8@\"HKAnalyticsDataSource\"16^@24"
+ "wristDetectionIsEnabledForActiveWatch"
+ "@\"<HKFeatureAvailabilityProviding>\""
+ "HKFeatureAvailabilityProvidingObserver"
+ "d"
+ "_unitTesting_postNotificationHandler"
+ "\x03"
+ "debugIdentifier"
+ "_analysisTimeInterval"
+ "initWithProfile:debugIdentifier:delegate:"
+ "[%!{(MISSING)public}@] Activity criteria will be updated and reset."
+ "_completionLock"
+ "breathingDisturbanceAnalysisScheduler"
+ "initWithProfile:featureStatusProvider:featureAvailabilityProviding:currentDateProvider:protectedDataOperation:profileDidBecomeReadyBlock:"
+ "onboardingRecordIsPresentForFeatureWithIdentifier:"
+ "B24@0:8@\"HDPeriodicActivity\"16"
+ "_writeDateOfMostRecentSuccessfulAnalysisAttempt"
+ "initWithFeatureIdentifier:defaultCountrySet:healthDaemon:"
+ "_getEarliestOnboardingDate"
+ "_unitTesting_profileDidBecomeReadyBlock"
+ "featureAvailabilityProvidingDidUpdateSettings:"
+ "notificationManager"
+ "quantityTypeForIdentifier:"
+ "[%!{(MISSING)public}@] Checking feature status for non-rescinded reasons: %!@(MISSING)"
+ "removeValuesForKeys:error:"
+ "setSound:"
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_TITLE_WATCH_UNSUPPORTED_REGION"
+ "[%!{(MISSING)public}@] Successfully sent analytics payload!"
+ "notAgeGatedForUserDefaultsKey:"
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_TITLE"
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_TITLE_UNSUPPORTED_REGION"
+ "_deregisterUITriggers"
+ "_keyValueDomain"
+ "onboardingRecordIsNotPresentForFeatureWithIdentifier:"
+ "remote_forceBreathingDisturbanceAnalysis"
+ "DeviceSupportsBreathingDisturbancesMeasurements"
+ "[%!{(MISSING)public}@] Error posting rescinded notification: %!@(MISSING)"
+ "[%!{(MISSING)public}@] Sleep apnea notifications are unavailable for non-rescinded reasons."
+ "_rescindedRequirementIdentifiers"
+ "_writePossibleSleepApneaNotificationSampleWithAnalysisInterval:algorithmVersion:error:"
+ "initWithFeatureIdentifier:isOnWhenSettingIsAbsent:"
+ "B36@0:8B16@20q28"
+ "HKCountrySet+SleepApneaNotifications.m"
+ "_cachedCalendar"
+ "com.apple.healthd.sleep.breathingdisturbanceanalysisactivity"
+ "objectAtIndexedSubscript:"
+ "@\"HDSHBreathingDisturbanceAnalyzer\""
+ "initWithLoggingCategory:healthDataSource:"
+ "makeIHAGatedEventPayloadWithDataSource:error:"
+ "v32@0:8@\"HDPeriodicActivity\"16@?<v@?qd@\"NSError\">24"
+ "_defaultAnalyticsPayload"
+ "_registerUITriggers"
+ "com.apple.health.Sleep.SleepApneaRescindedNotification"
+ "[%!{(MISSING)public}@] Number of expected analysis attempts between %!@(MISSING) and %!@(MISSING) is: %!l(MISSING)d"
+ "_updateActivityCriteriaAndResetActivity"
+ "_createEnumeratorWithAnalysisInterval:profile:"
+ "capabilityIsSupportedOnActiveRemoteDeviceForFeatureWithIdentifier:"
+ "copy"
+ "fetchSamplesWithAnalysisInterval:profile:error:"
+ "q40@0:8@16@24@32"
+ "HDSHSleepApneaRescindedNotificationManager"
+ "[%!{(MISSING)public}@] Successfully performed analysis! Attempting to update count."
+ "componentsJoinedByString:"
+ "currentCalendar"
+ "featureAvailabilityProvidingDidUpdateOnboardingCompletion:"
+ "@\"HDPeriodicActivity\""
+ "46F59960-D16A-4E76-B7D1-A1B0BBC73923"
+ "[%!{(MISSING)public}@] Possible sleep apnea detected from breathing disturbance samples."
+ "_triggerObserver"
+ "hk_sleepDayStartWithCalendar:"
+ "initWithCountryBitmasks:compatibilityVersion:contentVersion:provenance:"
+ "performBreathingDisturbanceAnalysisWithIsForced:date:numberOfAnalysisAttempts:"
+ "prerequisiteFeaturesAreOnWithFeatureSettings:"
+ "v24@0:8d16"
+ "@48@0:8@16@24@32@?40"
+ "initWithAllowedCountriesDataSource:profile:featureCapability:loggingCategory:"
+ "[%!{(MISSING)public}@] Error getting feature status: %!@(MISSING)"
+ "i"
+ "Local generated country set should never be nil"
+ "capabilityIsSupportedOnActiveWatchForFeatureWithIdentifier:supportedOnLocalDevice:"
+ "_areSamplesInSameSleepDayWithFirstSample:secondSample:calendar:"
+ "_areNotificationsEnabled"
+ "postNotificationWithRequest:completion:"
+ "validateConfiguration:client:error:"
+ "remote_overridePreviousTimeIntervalWithTimeInterval:"
+ "_showRescindedNotificationWithTitleAndBodyKeys:rescindedReason:"
+ "featureFlagIsEnabled:"
+ "hk_dateByAddingDays:toDate:"
+ "_analyzer"
+ "_categoryIdentifierFromRescindedReason:"
+ "defaultOnboardingEligibilityRequirementsForFeatureIdentifier:"
+ "eventName"
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_BODY"
+ "TB,R,N"
+ "hdsh_sleepApneaNotificationsAvailabilityManagerWithProfile:"
+ "@\"HKAnalyticsEventSubmissionManager\""
+ "_completion"
+ "featureOnboardingRecordWithError:"
+ "is_improve_health_and_activity_allowed"
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_BODY_UNSUPPORTED_REGION"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
+ "[%!{(MISSING)public}@] Overriding old time interval of %!f(MISSING) with new time interval of %!f(MISSING)."
+ "earliestDateOfAnyOnboardingCompletion"
+ "periodicActivityRequiresProtectedData:"
+ "[%!{(MISSING)public}@] Error resetting last shown date for notification: %!@(MISSING)"
+ "[%!{(MISSING)public}@] Successfully wrote possible sleep apnea event sample with source %!@(MISSING)"
+ "_localKeyValueDomain"
+ "hk_isBeforeDate:"
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_BODY_SEED_EXPIRED"
+ "[%!{(MISSING)public}@] Unexpected activity received; not performing activity."
+ "featureIsOnWithIdentifier:isOnIfSettingIsAbsent:"
+ "v32@0:8@\"HDPeriodicActivity\"16@\"NSObject<OS_xpc_object>\"24"
+ "[%!{(MISSING)public}@] Number of expected analysis attempts: %!l(MISSING)d"
+ "_queue_checkFeatureStatus"
+ "onboardingState"
+ "[%!{(MISSING)public}@] Received nil onboarding record. Will assume feature is not onboarded."
+ "analyzeSamples:dateInterval:"
+ "createTaskServerWithUUID:configuration:client:delegate:error:"
+ "[%!{(MISSING)public}@] About to post possible sleep apnea detected notification."
+ "com.apple.hid.bd.sleepnotification"
+ "setNumber:forKey:error:"
+ "_requestBreathingDisturbanceAnalysisIfNeeded"
+ "currentDeviceEntityWithError:"
+ "requestWorkWithPriority:error:"
+ "_isFeatureRescindedWithRequirementsEvaluation:"
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_BODY_REMOTELY_DISABLED"
+ "subarrayWithRange:"
+ "[%!{(MISSING)public}@] About to show rescinded notification for sleep apnea notifications."
+ "_rescindedNotificationTitleAndBodyKeysWithHighestPriorityUnsatisfiedRequirementIdentifier:"
+ "T@?,C,N,V_unitTesting_postNotificationHandler"
+ "[%!{(MISSING)public}@] Attempting to send analytics."
+ "[%!{(MISSING)public}@] Error writing last shown date for notification: %!@(MISSING)"
+ "[%!{(MISSING)public}@] Sleep apnea notifications are rescinded. Notification was last shown: %!@(MISSING)"
+ "_analyticsEventSubmissionManager"
+ "@40@0:8@16@24@32"
+ "HDSHBreathingDisturbanceAnalysisAnalyticsEvent"
+ "[%!{(MISSING)public}@] Feature is disabled; not going to check if analysis is overdue."
+ "[%!{(MISSING)public}@] Error attempting to send analytics payload: %!@(MISSING)"
+ "deviceManager"
+ "samplesFilteredBySleepDay:"
+ "HDPeriodicActivityDelegate"
+ "hk_gregorianCalendar"
+ "initWithFeatureAvailabilityProviding:healthDataSource:"
+ "remote_getBreathingDisturbanceSamplesInDateInterval:completion:"
+ "numberForKey:error:"
+ "q"
+ "HDProtectedDataOperationDelegate"
+ "[%!{(MISSING)public}@] Analysis is needed. Analyzing over date intervals that have not been analyzed."
+ "entityEnumeratorWithType:profile:"
+ "\x14"
+ "[%!{(MISSING)public}@] Feature status changed to: %!@(MISSING)"
+ "setObject:atIndexedSubscript:"
+ "v48@0:8@\"HDProtectedDataOperation\"16@\"HDProfile\"24@\"HDAssertion\"32@?<v@?>40"
+ "name"
+ "@\"NSDictionary\""
+ "initWithProfile:featureStatusProvider:queueOverride:"
+ "makeUnrestrictedEventPayloadWithDataSource:error:"
+ "[%!{(MISSING)public}@] Feature status is nil with error: %!@(MISSING)"
+ ", "
+ "[%!{(MISSING)public}@] Unexpected activity received; not setting activity criteria."
+ "_clientRemoteObjectProxy"
+ "components:fromDate:toDate:options:"
+ "hk_error:format:"
+ "[%!{(MISSING)public}@] Failed to write updated count of analysis attempts with error: %!@(MISSING)\nWill retry this window in one day."
+ "_queue_sendNotificationRequestIfNeededWithFeatureStatus:"
+ "bd_count"
+ "SLEEP_APNEA_REENABLED_NOTIFICATION_TITLE"
+ "[%!{(MISSING)public}@] Got nil onboarding date, not checking if analysis is overdue."
+ "enumerateWithError:handler:"
+ "hk_morningIndexWithCalendar:"
+ "SLEEP_APNEA_RESCINDED_NOTIFICATION_BODY_WATCH_UNSUPPORTED_REGION"
+ "initWithStartDate:endDate:"
+ "[%!{(MISSING)public}@] Request was processed, but completion exists before capture."
+ "[%!{(MISSING)public}@] Could not write date of last analysis attempt with error %!@(MISSING)"
+ "[%!{(MISSING)public}@] Request was not processed with error: %!@(MISSING)"
+ "[%!{(MISSING)public}@] Request was not processed with error: %!@(MISSING)\nWill try analysis again in a day."
+ "\x04\x12"
+ "nebula"
+ "setExpirationDate:"
+ "sortDescriptorWithKey:ascending:"
+ "setSortDescriptors:"
+ "_featureAvailabilityProviding"
+ "dictionaryWithObjects:forKeys:count:"
+ "@\"HDSHSleepApneaRescindedNotificationManager\""
+ "UUIDString"
+ "@\"HDSHSleepApneaNotificationUITriggerObserver\""
+ "[%!{(MISSING)public}@] Checking feature status for rescinded reasons: %!@(MISSING)"
+ "_rescindedNotificationManager"
+ "endDateFromMostRecentlyAnalyzedDateIntervalWithDate:numberOfAnalysisAttempts:calendar:"
+ "featureAttributesDerivedFromOSBuildAndFeatureVersion:watchDeviceIdentifier:phoneDeviceIdentifier:"
+ "B"
+ "[%!{(MISSING)public}@] Failed to write sleep apnea event sample with error: %!@(MISSING). Not sending notification and will attempt to retry in one day."
+ "setTitle:"
+ "initWithArray:"
+ "isAnalysisNeededWithAnchorDate:referenceDate:calendar:"
+ "overrideAnalysisTimeIntervalAndResetActivityWithTimeInterval:"
+ "@\"HDKeyValueDomain\""
+ "areAllRequirementsSatisfied"
+ "initWithProfile:name:interval:delegate:loggingCategory:"
+ "unitTesting_postNotificationHandler"
+ "v32@0:8q16d24"
+ "T@\"HDPeriodicActivity\",R,N,V_activity"
+ "_requestBreathingDisturbanceAnalysisWithSamples:analysisInterval:"
+ "initWithUUID:configuration:client:delegate:analyzer:analysisScheduler:"
+ "periodicActivity:configureXPCActivityCriteria:"
+ "@40@0:8@16@24^@32"
+ "[%!{(MISSING)public}@] Date write failed while performing analysis."
+ "initWithRequirementsByContext:"
+ "isImproveHealthAndActivityEnabled"
+ "arrayWithArray:"
+ "v32@0:8@\"NSDateInterval\"16@?<v@?@\"NSArray\">24"
+ "_sleepApneaNotificationsAvailabilityManager"
+ "activeRemoteDeviceIsPresentWhenRequiredForRegionAvailabilityOrDeviceCapabilityForFeatureWithIdentifier:"
+ "featureStatusWithError:"
+ "\x14$\x12"
+ "configurationClass"
+ "initWithDictionary:"
+ "HKSHSleepApneaControlServer"
+ "_activity"
+ "unsatisfiedRequirementIdentifiers"
+ "BreathingDisturbanceAnalysisProtectedDataOperation"
+ "HDSHBreathingDisturbanceAnalysisScheduler"
+ "countryIsSupportedOnActiveRemoteDeviceForFeatureWithIdentifier:isSupportedIfCountryListMissing:"
+ "[%!{(MISSING)public}@] Onboarding record has updated. Recalculating activity criteria."
+ "_runCompletionIfExistsWithResult:retryInterval:"
+ "initWithProfile:featureIdentifier:availabilityRequirements:currentOnboardingVersion:pairedDeviceCapability:pairedFeatureAttributesProvider:regionAvailabilityProvider:disableAndExpiryProvider:loggingCategory:"
+ "setCategoryIdentifier:"
+ "@32@0:8@16@24"
+ "@?"
+ "[%!{(MISSING)public}@] Analysis successfully performed!"
+ "[%!{(MISSING)public}@] Could not fetch notification last shown date with error: %!@(MISSING)"
+ "[%!{(MISSING)public}@] Could not get breathing disturbance samples with error: %!@(MISSING)"
+ "environmentDataSource"
- "\x01\x11"

```
