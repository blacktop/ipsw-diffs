## HealthHearingDaemon

> `/System/Library/PrivateFrameworks/HealthHearingDaemon.framework/HealthHearingDaemon`

```diff

-5200.5.1.0.0
-  __TEXT.__text: 0x21d48
-  __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__objc_methlist: 0x1b0c
+6074.1.2.4.0
+  __TEXT.__text: 0x216c0
+  __TEXT.__auth_stubs: 0xbd0
+  __TEXT.__objc_methlist: 0x1aac
   __TEXT.__const: 0x3f2
-  __TEXT.__cstring: 0x22c2
-  __TEXT.__oslogstring: 0x295b
+  __TEXT.__cstring: 0x22d2
+  __TEXT.__oslogstring: 0x2a2b
   __TEXT.__gcc_except_tab: 0x284
   __TEXT.__constg_swiftt: 0xd8
   __TEXT.__swift5_typeref: 0xbc

   __TEXT.__swift5_types: 0x8
   __TEXT.__unwind_info: 0x780
   __TEXT.__eh_frame: 0x80
-  __TEXT.__objc_classname: 0x6b9
-  __TEXT.__objc_methname: 0x707d
-  __TEXT.__objc_methtype: 0x1266
-  __TEXT.__objc_stubs: 0x4a20
-  __DATA_CONST.__got: 0x500
+  __TEXT.__objc_classname: 0x6bb
+  __TEXT.__objc_methname: 0x7015
+  __TEXT.__objc_methtype: 0x11df
+  __TEXT.__objc_stubs: 0x4a40
+  __DATA_CONST.__got: 0x4e0
   __DATA_CONST.__const: 0x698
-  __DATA_CONST.__objc_classlist: 0xf8
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x17a0
+  __DATA_CONST.__objc_selrefs: 0x1798
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0xb0
-  __DATA_CONST.__objc_arraydata: 0x640
-  __AUTH_CONST.__auth_got: 0x608
-  __AUTH_CONST.__const: 0x2e8
-  __AUTH_CONST.__cfstring: 0x1ce0
-  __AUTH_CONST.__objc_const: 0x3158
-  __AUTH_CONST.__objc_intobj: 0xd20
-  __AUTH_CONST.__objc_arrayobj: 0x120
+  __DATA_CONST.__objc_superrefs: 0xa8
+  __DATA_CONST.__objc_arraydata: 0x668
+  __AUTH_CONST.__auth_got: 0x600
+  __AUTH_CONST.__const: 0x310
+  __AUTH_CONST.__cfstring: 0x1d00
+  __AUTH_CONST.__objc_const: 0x3010
+  __AUTH_CONST.__objc_intobj: 0xd50
+  __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x1b4
-  __DATA.__data: 0x8f0
+  __DATA.__objc_ivar: 0x1a8
+  __DATA.__data: 0x910
   __DATA.__bss: 0x300
-  __DATA_DIRTY.__objc_data: 0x968
-  __DATA_DIRTY.__data: 0xd0
+  __DATA_DIRTY.__objc_data: 0x918
+  __DATA_DIRTY.__data: 0xc8
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 72687384-5D47-35FE-8810-D301889C6506
-  Functions: 689
-  Symbols:   2731
-  CStrings:  1845
+  UUID: 7DB19F8D-76D5-3214-8EEC-30C1234B45A7
+  Functions: 682
+  Symbols:   2698
+  CStrings:  1834
 
Symbols:
+ +[HDFeatureAvailabilityManager(Hearing) hearingAidV2FeatureAvailabilityManagerWithProfile:]
+ +[HKCountrySet(HearingAidV2) localAvailabilityForHearingAidV2]
+ +[HKCountrySet(HearingAidV2) localAvailabilityForHearingAidV2].cold.1
+ +[HKFeatureAvailabilityRequirementSet(Hearing) hearingAidV2RequirementSet]
+ -[HDAudioAnalyticsManager _lastSuccessfulCalculation]
+ -[HDAudioAnalyticsManager _successfulCalculationAt:]
+ -[HDAudioAnalyticsManager capturePhoneAnalyticsWithError:]
+ -[HDAudioAnalyticsManager reportDailyAnalyticsWithCoordinator:completion:]
+ _HKFeatureIdentifierHearingAidV2
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_IVAR_$_HDHearingProfileExtension._hearingAidV2BackgroundFeatureDeliveryManager
+ _OBJC_IVAR_$_HDHearingProfileExtension._hearingAidV2FeatureAvailabilityManager
+ __OBJC_$_CATEGORY_HKCountrySet_$_HearingAidV2
+ __OBJC_$_CLASS_METHODS_HKCountrySet(HearingAidV2|HearingProtection|HearingTest|HearingAid)
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDAnalyticsSubmissionCoordinatorDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HDAnalyticsSubmissionCoordinatorDelegate
+ __OBJC_$_PROTOCOL_REFS_HDAnalyticsSubmissionCoordinatorDelegate
+ __OBJC_LABEL_PROTOCOL_$_HDAnalyticsSubmissionCoordinatorDelegate
+ __OBJC_PROTOCOL_$_HDAnalyticsSubmissionCoordinatorDelegate
+ __PROTOCOLS__TtC19HealthHearingDaemon32HDHearingTestDailyAnalyticsEvent.5
+ ___58-[HDAudioAnalyticsManager capturePhoneAnalyticsWithError:]_block_invoke
+ ___58-[HDAudioAnalyticsManager capturePhoneAnalyticsWithError:]_block_invoke.cold.1
+ ___58-[HDAudioAnalyticsManager capturePhoneAnalyticsWithError:]_block_invoke.cold.2
+ ___87-[HDHeadphoneDoseManager _lock_updateCurrentDoseUsingStatisticsResult:assertion:error:]_block_invoke.401
+ ___98-[HDHeadphoneExposureNotificationCenter postSevenDayDoseNotification:nowDate:analyticsInfo:error:]_block_invoke.315
+ ___98-[HDHeadphoneExposureNotificationCenter postSevenDayDoseNotification:nowDate:analyticsInfo:error:]_block_invoke.315.cold.1
+ ___block_literal_global.301
+ ___block_literal_global.306
+ ___block_literal_global.311
+ ___block_literal_global.313
+ ___block_literal_global.318
+ ___block_literal_global.320
+ ___block_literal_global.326
+ ___block_literal_global.365
+ ___block_literal_global.404
+ ___block_literal_global.459
+ ___block_literal_global.492
+ ___block_literal_global.517
+ ___block_literal_global.528
+ ___block_literal_global.557
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_HealthHearingDaemon
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_HealthHearingDaemon
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_HealthHearingDaemon
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_HealthHearingDaemon
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_HealthHearingDaemon
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_HealthHearingDaemon
+ _objc_msgSend$_lastSuccessfulCalculation
+ _objc_msgSend$_successfulCalculationAt:
+ _objc_msgSend$analyticsSubmissionCoordinator
+ _objc_msgSend$capturePhoneAnalyticsWithError:
+ _objc_msgSend$dataCollectionObserverStateInForeground:hasRunningWorkout:hasBackgroundObserver:shouldTakeWorkoutDatabaseAssertion:
+ _objc_msgSend$hearingAidV2FeatureAvailabilityManagerWithProfile:
+ _objc_msgSend$hearingAidV2RequirementSet
+ _objc_msgSend$localAvailabilityForHearingAidV2
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$standardUserDefaults
- -[HDAudioAnalyticsManager calculationPeriod]
- -[HDAudioAnalyticsManager capturePhoneAnalytics]
- -[HDAudioAnalyticsManager lastSuccessfulCalculation]
- -[HDAudioAnalyticsManager performPeriodicActivity:completion:]
- -[HDAudioAnalyticsManager periodicActivity:configureXPCActivityCriteria:]
- -[HDAudioAnalyticsManager periodicActivityRequiresProtectedData:]
- -[HDAudioAnalyticsManager periodicActivity]
- -[HDAudioAnalyticsManager retryPeriod]
- -[HDAudioAnalyticsManager setPeriodicActivity:]
- -[HDAudioAnalyticsResult .cxx_destruct]
- -[HDAudioAnalyticsResult error]
- -[HDAudioAnalyticsResult initWithStatus:error:]
- -[HDAudioAnalyticsResult status]
- _OBJC_CLASS_$_HDAudioAnalyticsResult
- _OBJC_CLASS_$_HDPeriodicActivity
- _OBJC_IVAR_$_HDAudioAnalyticsManager._calculationPeriod
- _OBJC_IVAR_$_HDAudioAnalyticsManager._periodicActivity
- _OBJC_IVAR_$_HDAudioAnalyticsManager._retryPeriod
- _OBJC_IVAR_$_HDAudioAnalyticsResult._error
- _OBJC_IVAR_$_HDAudioAnalyticsResult._status
- _OBJC_METACLASS_$_HDAudioAnalyticsResult
- _XPC_ACTIVITY_INTERVAL_1_DAY
- _XPC_ACTIVITY_INTERVAL_1_HOUR
- __OBJC_$_CATEGORY_HKCountrySet_$_HearingProtection
- __OBJC_$_CLASS_METHODS_HKCountrySet(HearingProtection|HearingTest|HearingAid)
- __OBJC_$_INSTANCE_METHODS_HDAudioAnalyticsResult
- __OBJC_$_INSTANCE_VARIABLES_HDAudioAnalyticsResult
- __OBJC_$_PROP_LIST_HDAudioAnalyticsResult
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDPeriodicActivityDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HDPeriodicActivityDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_HDPeriodicActivityDelegate
- __OBJC_$_PROTOCOL_REFS_HDPeriodicActivityDelegate
- __OBJC_CLASS_RO_$_HDAudioAnalyticsResult
- __OBJC_LABEL_PROTOCOL_$_HDPeriodicActivityDelegate
- __OBJC_METACLASS_RO_$_HDAudioAnalyticsResult
- __OBJC_PROTOCOL_$_HDPeriodicActivityDelegate
- __PROTOCOLS__TtC19HealthHearingDaemon32HDHearingTestDailyAnalyticsEvent.4
- ___48-[HDAudioAnalyticsManager capturePhoneAnalytics]_block_invoke
- ___48-[HDAudioAnalyticsManager capturePhoneAnalytics]_block_invoke.cold.1
- ___48-[HDAudioAnalyticsManager capturePhoneAnalytics]_block_invoke.cold.2
- ___87-[HDHeadphoneDoseManager _lock_updateCurrentDoseUsingStatisticsResult:assertion:error:]_block_invoke.398
- ___98-[HDHeadphoneExposureNotificationCenter postSevenDayDoseNotification:nowDate:analyticsInfo:error:]_block_invoke.312
- ___98-[HDHeadphoneExposureNotificationCenter postSevenDayDoseNotification:nowDate:analyticsInfo:error:]_block_invoke.312.cold.1
- ___block_literal_global.298
- ___block_literal_global.300
- ___block_literal_global.308
- ___block_literal_global.310
- ___block_literal_global.315
- ___block_literal_global.317
- ___block_literal_global.323
- ___block_literal_global.378
- ___block_literal_global.417
- ___block_literal_global.472
- ___block_literal_global.505
- ___block_literal_global.530
- ___block_literal_global.541
- ___block_literal_global.570
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_HealthHearingDaemon
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_HealthHearingDaemon
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_HealthHearingDaemon
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_HealthHearingDaemon
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_HealthHearingDaemon
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_HealthHearingDaemon
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_HealthHearingDaemon
- _objc_msgSend$calculationPeriod
- _objc_msgSend$capturePhoneAnalytics
- _objc_msgSend$dataCollectionObserverStateInForeground:hasRunningWorkout:hasBackgroundObserver:
- _objc_msgSend$featureFlagIsEnabled:
- _objc_msgSend$initWithProfile:name:interval:delegate:loggingCategory:
- _objc_msgSend$initWithStatus:error:
- _objc_msgSend$lastSuccessfulCalculation
- _objc_msgSend$lastSuccessfulRunDate
- _objc_msgSend$periodicActivity
- _objc_msgSend$retryPeriod
- _objc_msgSend$status
- _objc_retain_x9
- _swift_bridgeObjectRelease_n
- _swift_retain
CStrings:
+ "\v"
+ "%{public}@: HDAudioAnalyticsManager HDAudioAnalyticsStatusIgnore"
+ "%{public}@: HDAudioAnalyticsManager HDAudioAnalyticsStatusRetry %{public}@"
+ "%{public}@: HDAudioAnalyticsManager HDAudioAnalyticsStatusSuccess"
+ "HDAnalyticsSubmissionCoordinatorDelegate"
+ "HDAudioAnalyticsManager-LastSuccessfulRun"
+ "HKCountrySet+HearingAidV2.m"
+ "HearingAidV2"
+ "T@\"HDProfile\",W,N,V_profile"
+ "_hearingAidV2BackgroundFeatureDeliveryManager"
+ "_hearingAidV2FeatureAvailabilityManager"
+ "_lastSuccessfulCalculation"
+ "_successfulCalculationAt:"
+ "analyticsSubmissionCoordinator"
+ "associationsUpdatedForObject:subObject:type:behavior:objects:anchor:"
+ "capturePhoneAnalyticsWithError:"
+ "dataCollectionObserverStateInForeground:hasRunningWorkout:hasBackgroundObserver:shouldTakeWorkoutDatabaseAssertion:"
+ "hardwareVersion"
+ "hearingAidV2FeatureAvailabilityManagerWithProfile:"
+ "hearingAidV2RequirementSet"
+ "invalidateAndWait"
+ "localAvailabilityForHearingAidV2"
+ "localizedDescription"
+ "objectForKey:"
+ "q24@0:8^@16"
+ "reportDailyAnalyticsWithCoordinator:completion:"
+ "setObject:forKey:"
+ "standardUserDefaults"
+ "v32@0:8@\"HDAnalyticsSubmissionCoordinator\"16@?<v@?@\"NSMutableDictionary\"q@\"NSError\">24"
+ "v64@0:8@\"<HKAssociatableObject>\"16@\"<HKAssociatableObject>\"24Q32Q40@\"NSArray\"48@\"NSNumber\"56"
+ "v64@0:8@16@24Q32Q40@48@56"
- "\t"
- "@\"HDPeriodicActivity\""
- "@\"NSError\""
- "B24@0:8@\"HDPeriodicActivity\"16"
- "HDAudioAnalyticsResult"
- "HDPeriodicActivityDelegate"
- "T@\"HDPeriodicActivity\",&,N,V_periodicActivity"
- "T@\"HDProfile\",&,N,V_profile"
- "T@\"NSError\",R,N,V_error"
- "Td,R,N,V_calculationPeriod"
- "Td,R,N,V_retryPeriod"
- "Tq,R,N,V_status"
- "_calculationPeriod"
- "_error"
- "_periodicActivity"
- "_retryPeriod"
- "_status"
- "calculationPeriod"
- "capturePhoneAnalytics"
- "com.apple.healthd.hearing.HDAudioAnalyticsCalculator"
- "d16@0:8"
- "dataCollectionObserverStateInForeground:hasRunningWorkout:hasBackgroundObserver:"
- "featureFlagIsEnabled:"
- "initWithProfile:name:interval:delegate:loggingCategory:"
- "initWithStatus:error:"
- "lastSuccessfulCalculation"
- "lastSuccessfulRunDate"
- "nextSyncAnchorWithSession:predicate:startSyncAnchor:profile:error:"
- "performPeriodicActivity:completion:"
- "periodicActivity"
- "periodicActivity:configureXPCActivityCriteria:"
- "periodicActivityRequiresProtectedData:"
- "q48@0:8@\"NSArray\"16@\"<HDSyncStore>\"24@\"HDProfile\"32^@40"
- "q48@0:8@16@24@32^@40"
- "q56@0:8@\"HDSyncSession\"16@\"HDSQLitePredicate\"24q32@\"HDProfile\"40^@48"
- "q56@0:8@16@24q32@40^@48"
- "receiveSyncObjects:syncStore:profile:error:"
- "retryPeriod"
- "setPeriodicActivity:"
- "status"
- "v32@0:8@\"HDPeriodicActivity\"16@\"NSObject<OS_xpc_object>\"24"
- "v32@0:8@\"HDPeriodicActivity\"16@?<v@?qd@\"NSError\">24"

```
