## RespiratoryHealthDaemon

> `/System/Library/PrivateFrameworks/RespiratoryHealthDaemon.framework/RespiratoryHealthDaemon`

```diff

-5200.5.1.0.0
-  __TEXT.__text: 0x589c
+6074.1.2.4.0
+  __TEXT.__text: 0x5638
   __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_methlist: 0x8ac
-  __TEXT.__const: 0xb0
-  __TEXT.__oslogstring: 0x891
-  __TEXT.__cstring: 0x5e1
-  __TEXT.__unwind_info: 0x1d0
-  __TEXT.__objc_classname: 0x246
-  __TEXT.__objc_methname: 0x245f
-  __TEXT.__objc_methtype: 0x69c
-  __TEXT.__objc_stubs: 0x1600
-  __DATA_CONST.__got: 0x208
+  __TEXT.__objc_methlist: 0x85c
+  __TEXT.__const: 0xa8
+  __TEXT.__oslogstring: 0x8af
+  __TEXT.__cstring: 0x5d9
+  __TEXT.__unwind_info: 0x1e0
+  __TEXT.__objc_classname: 0x243
+  __TEXT.__objc_methname: 0x2288
+  __TEXT.__objc_methtype: 0x61c
+  __TEXT.__objc_stubs: 0x1540
+  __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__const: 0x178
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7a8
+  __DATA_CONST.__objc_selrefs: 0x768
   __DATA_CONST.__objc_superrefs: 0x28
   __AUTH_CONST.__auth_got: 0x228
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x620
-  __AUTH_CONST.__objc_const: 0x1068
+  __AUTH_CONST.__objc_const: 0xf20
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0xa8
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x98
   __DATA.__data: 0x420
   __DATA_DIRTY.__objc_data: 0x140
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/RespiratoryHealth.framework/RespiratoryHealth
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0621A0DF-1064-3857-B050-CEDC1E63BA2E
-  Functions: 161
-  Symbols:   810
-  CStrings:  558
+  UUID: 1A24FF4D-B205-3157-8A9E-83B2E5BB01D3
+  Functions: 154
+  Symbols:   767
+  CStrings:  537
 
Symbols:
+ -[HDRPDailyAnalyticsReport _gatherImproveHealthAndActivityReportFromBackgroundOxygenSaturationSamplesInPreviousDay:backgroundSamplesInPrevious30Days:oxygenSaturationSamplesInPreviousDay:oxygenSaturationSamplesInPrevious30Days:error:]
+ -[HDRPDailyAnalyticsReport _queryForBackgroundOxygenSaturationSamplesInPreviousDays:error:]
+ -[HDRPDailyAnalyticsReport generatePayloadAndReturnError:].cold.7
+ -[HDRPRespiratoryDailyAnalytics reportDailyAnalyticsWithCoordinator:completion:]
+ -[HDRespiratoryProfileExtension featureAvailabilityExtensionDidUpdatePairedDeviceCapability:]
+ _HKLogRespiratoryCategory
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDAnalyticsSubmissionCoordinatorDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HDFeatureAvailabilityExtensionObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HDAnalyticsSubmissionCoordinatorDelegate
+ __OBJC_$_PROTOCOL_REFS_HDAnalyticsSubmissionCoordinatorDelegate
+ __OBJC_LABEL_PROTOCOL_$_HDAnalyticsSubmissionCoordinatorDelegate
+ __OBJC_PROTOCOL_$_HDAnalyticsSubmissionCoordinatorDelegate
+ _objc_msgSend$_gatherImproveHealthAndActivityReportFromBackgroundOxygenSaturationSamplesInPreviousDay:backgroundSamplesInPrevious30Days:oxygenSaturationSamplesInPreviousDay:oxygenSaturationSamplesInPrevious30Days:error:
+ _objc_msgSend$_queryForBackgroundOxygenSaturationSamplesInPreviousDays:error:
+ _objc_msgSend$addObserver:queue:
+ _objc_msgSend$analyticsSubmissionCoordinator
+ _objc_retain_x25
+ _objc_retain_x5
- -[HDRPDailyAnalyticsReport _gatherImproveHealthAndActivityReportFromBackgroundOxygenSaturationSamplesInPreviousDay:oxygenSaturationSamplesInPreviousDay:oxygenSaturationSamplesInPrevious30Days:error:]
- -[HDRPDailyAnalyticsReport _queryForBackgroundOxygenSaturationSamplesInPreviousDayAndReturnError:]
- -[HDRPRespiratoryDailyAnalytics _hasAnalyticsBeenReportedForToday:]
- -[HDRPRespiratoryDailyAnalytics calculationPeriod]
- -[HDRPRespiratoryDailyAnalytics performPeriodicActivity:completion:]
- -[HDRPRespiratoryDailyAnalytics periodicActivity:configureXPCActivityCriteria:]
- -[HDRPRespiratoryDailyAnalytics periodicActivityRequiresProtectedData:]
- -[HDRPRespiratoryDailyAnalytics periodicActivity]
- -[HDRPRespiratoryDailyAnalytics retryPeriod]
- -[HDRPRespiratoryDailyAnalytics setPeriodicActivity:]
- -[HDRespiratoryProfileExtension featureAvailabilityProvidingDidUpdatePairedDeviceCapability:]
- _HKLogRespiratory
- _OBJC_CLASS_$_HDPeriodicActivity
- _OBJC_CLASS_$_HKRPOxygenSaturationOnboardingCacher
- _OBJC_CLASS_$_MockHDRPHealthLite
- _OBJC_IVAR_$_HDRPRespiratoryDailyAnalytics._calculationPeriod
- _OBJC_IVAR_$_HDRPRespiratoryDailyAnalytics._periodicActivity
- _OBJC_IVAR_$_HDRPRespiratoryDailyAnalytics._retryPeriod
- _OBJC_IVAR_$_HDRespiratoryProfileExtension._onboardingCacher
- _OBJC_METACLASS_$_MockHDRPHealthLite
- _OUTLINED_FUNCTION_3
- _XPC_ACTIVITY_ALLOW_BATTERY
- _XPC_ACTIVITY_GRACE_PERIOD
- _XPC_ACTIVITY_INTERVAL_1_HOUR
- _XPC_ACTIVITY_INTERVAL_8_HOURS
- _XPC_ACTIVITY_PRIORITY
- _XPC_ACTIVITY_PRIORITY_UTILITY
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDPeriodicActivityDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HDPeriodicActivityDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_HDPeriodicActivityDelegate
- __OBJC_$_PROTOCOL_REFS_HDPeriodicActivityDelegate
- __OBJC_CLASS_RO_$_MockHDRPHealthLite
- __OBJC_LABEL_PROTOCOL_$_HDPeriodicActivityDelegate
- __OBJC_METACLASS_RO_$_MockHDRPHealthLite
- __OBJC_PROTOCOL_$_HDPeriodicActivityDelegate
- _objc_msgSend$_gatherImproveHealthAndActivityReportFromBackgroundOxygenSaturationSamplesInPreviousDay:oxygenSaturationSamplesInPreviousDay:oxygenSaturationSamplesInPrevious30Days:error:
- _objc_msgSend$_hasAnalyticsBeenReportedForToday:
- _objc_msgSend$_queryForBackgroundOxygenSaturationSamplesInPreviousDayAndReturnError:
- _objc_msgSend$calculationPeriod
- _objc_msgSend$hk_isDate:withinNumberOfCalendarDays:ofDate:
- _objc_msgSend$initWithFeatureAvailabilityProviding:userDefaults:userDefaultsSyncProvider:
- _objc_msgSend$initWithProfile:name:interval:delegate:loggingCategory:
- _objc_msgSend$lastSuccessfulRunDate
- _objc_msgSend$periodicActivity
- _objc_msgSend$retryPeriod
- _xpc_dictionary_set_bool
- _xpc_dictionary_set_double
- _xpc_dictionary_set_string
CStrings:
+ "@56@0:8@16@24@32@40^@48"
+ "A"
+ "HDAnalyticsSubmissionCoordinatorDelegate"
+ "[%{public}@] Could not fetch backgroundOxygenSaturationSamplesInPrevious30Days: %{public}@"
+ "_gatherImproveHealthAndActivityReportFromBackgroundOxygenSaturationSamplesInPreviousDay:backgroundSamplesInPrevious30Days:oxygenSaturationSamplesInPreviousDay:oxygenSaturationSamplesInPrevious30Days:error:"
+ "_queryForBackgroundOxygenSaturationSamplesInPreviousDays:error:"
+ "addObserver:queue:"
+ "analyticsSubmissionCoordinator"
+ "featureAvailabilityExtensionDidUpdatePairedDeviceCapability:"
+ "invalidateAndWait"
+ "reportDailyAnalyticsWithCoordinator:completion:"
+ "totalNumberOfBackgroundSamplesInPrevious30Days"
+ "v32@0:8@\"HDAnalyticsSubmissionCoordinator\"16@?<v@?@\"NSMutableDictionary\"q@\"NSError\">24"
- "@\"HDPeriodicActivity\""
- "@\"HKRPOxygenSaturationOnboardingCacher\""
- "@48@0:8@16@24@32^@40"
- "B24@0:8@\"HDPeriodicActivity\"16"
- "HDPeriodicActivityDelegate"
- "MockHDRPHealthLite"
- "T@\"HDPeriodicActivity\",&,N,V_periodicActivity"
- "T@\"HDProfile\",R,N,V_profile"
- "Td,R,N,V_calculationPeriod"
- "Td,R,N,V_retryPeriod"
- "[%{public}@] Analytics have already been gathered for today."
- "_calculationPeriod"
- "_gatherImproveHealthAndActivityReportFromBackgroundOxygenSaturationSamplesInPreviousDay:oxygenSaturationSamplesInPreviousDay:oxygenSaturationSamplesInPrevious30Days:error:"
- "_hasAnalyticsBeenReportedForToday:"
- "_onboardingCacher"
- "_periodicActivity"
- "_queryForBackgroundOxygenSaturationSamplesInPreviousDayAndReturnError:"
- "_retryPeriod"
- "a"
- "calculationPeriod"
- "com.apple.healthd.respiratory.DailyAnalyticsCalculator"
- "featureAvailabilityProvidingDidUpdatePairedDeviceCapability:"
- "hk_isDate:withinNumberOfCalendarDays:ofDate:"
- "initWithFeatureAvailabilityProviding:userDefaults:userDefaultsSyncProvider:"
- "initWithProfile:name:interval:delegate:loggingCategory:"
- "lastSuccessfulRunDate"
- "performPeriodicActivity:completion:"
- "periodicActivity"
- "periodicActivity:configureXPCActivityCriteria:"
- "periodicActivityRequiresProtectedData:"
- "retryPeriod"
- "setPeriodicActivity:"
- "v32@0:8@\"HDPeriodicActivity\"16@\"NSObject<OS_xpc_object>\"24"
- "v32@0:8@\"HDPeriodicActivity\"16@?<v@?qd@\"NSError\">24"
- "v32@0:8@16@24"

```
