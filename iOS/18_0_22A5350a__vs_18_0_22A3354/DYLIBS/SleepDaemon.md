## SleepDaemon

> `/System/Library/PrivateFrameworks/SleepDaemon.framework/SleepDaemon`

```diff

 5139.0.1.11.0
-  __TEXT.__text: 0x78128
+  __TEXT.__text: 0x790f4
   __TEXT.__auth_stubs: 0xc10
-  __TEXT.__objc_methlist: 0x7214
+  __TEXT.__objc_methlist: 0x72ec
   __TEXT.__const: 0x1c8
-  __TEXT.__cstring: 0x2a77
-  __TEXT.__oslogstring: 0xb6e5
-  __TEXT.__gcc_except_tab: 0x11c4
-  __TEXT.__unwind_info: 0x2180
-  __TEXT.__objc_classname: 0x1efd
-  __TEXT.__objc_methname: 0x10e9b
-  __TEXT.__objc_methtype: 0x3570
-  __TEXT.__objc_stubs: 0xcc40
-  __DATA_CONST.__got: 0xa00
-  __DATA_CONST.__const: 0x23e0
-  __DATA_CONST.__objc_classlist: 0x530
+  __TEXT.__cstring: 0x2aed
+  __TEXT.__oslogstring: 0xb811
+  __TEXT.__gcc_except_tab: 0x1248
+  __TEXT.__unwind_info: 0x21a8
+  __TEXT.__objc_classname: 0x1f1c
+  __TEXT.__objc_methname: 0x11427
+  __TEXT.__objc_methtype: 0x35ee
+  __TEXT.__objc_stubs: 0xd000
+  __DATA_CONST.__got: 0xa60
+  __DATA_CONST.__const: 0x2430
+  __DATA_CONST.__objc_classlist: 0x538
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x310
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x38e0
+  __DATA_CONST.__objc_selrefs: 0x39d8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x350
+  __DATA_CONST.__objc_superrefs: 0x358
   __AUTH_CONST.__auth_got: 0x618
   __AUTH_CONST.__const: 0xce0
-  __AUTH_CONST.__cfstring: 0x1e60
-  __AUTH_CONST.__objc_const: 0x123a0
+  __AUTH_CONST.__cfstring: 0x1ec0
+  __AUTH_CONST.__objc_const: 0x12530
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH.__objc_data: 0xc80
-  __DATA.__objc_ivar: 0x570
+  __AUTH.__objc_data: 0xcd0
+  __DATA.__objc_ivar: 0x584
   __DATA.__data: 0x24d0
   __DATA_DIRTY.__objc_ivar: 0xd0
   __DATA_DIRTY.__objc_data: 0x2760

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2929
-  Symbols:   3554
-  CStrings:  4483
+  Functions: 2948
+  Symbols:   3586
+  CStrings:  4538
 
Symbols:
+ _OBJC_CLASS_$_HKSampleQuery
+ _OBJC_CLASS_$_HKFeatureStatusManager
+ _OBJC_CLASS_$_HDSPSleepApneaAnalyticsBuilder
+ _OBJC_CLASS_$_NSSortDescriptor
+ _HKFeatureAvailabilityRequirementIdentifierFeatureIsOn
+ _HKFeatureAvailabilityContextUsage
+ _OBJC_CLASS_$_HKSampleType
+ _OBJC_METACLASS_$_HDSPSleepApneaAnalyticsBuilder
+ _HKFeatureIdentifierSleepApneaNotifications
+ _HKSampleSortIdentifierStartDate
+ _HKQuantityTypeIdentifierAppleSleepingBreathingDisturbances
+ _OBJC_CLASS_$_HKQueryDescriptor
+ _OBJC_CLASS_$_NSPredicate
CStrings:
+ "_maxTimeBetweenBDSessionsPastNight:"
+ "initWithBreathingDisturbanceSamples:sleepApneaFeatureStatus:morningIndexRange:gregorianCalendar:"
+ "_meanTimeBetweenBDSessionsPastNight:"
+ "_typeWithIdentifier:"
+ "T@\"HKFeatureStatus\",R,N,V_sleepApneaFeatureStatus"
+ "sleepApneaFeatureStatus"
+ "featureStatusWithError:"
+ "[%!{(MISSING)public}@] Error while querying fetching apnea feature status: %!@(MISSING)"
+ "_isEnabledBD"
+ "v32@?0@\"HKSampleQuery\"8@\"NSArray\"16@\"NSError\"24"
+ "T@\"NSArray\",R,N,V_breathingDisturbanceSamples"
+ "setIsOnboardedBD:"
+ "initWithEnvironment:daySummaries:breathingDisturbanceSamples:sleepApneaFeatureStatus:morningIndexRange:"
+ "_breathingDisturbanceSamplesInPastNight"
+ "sortDescriptorWithKey:ascending:"
+ "gregorianCalendar"
+ "hk_predicateForSamplesInDayIndexRange:"
+ "setMaxTimeBetweenBDSessionsPastNight:"
+ "isOnboardingRecordPresent"
+ "@56@0:8@16@24{?=qq}32@48"
+ "[%!{(MISSING)public}@] Error while querying for breathing disturbance samples: %!@(MISSING)"
+ "@64@0:8@16@24@32@40{?=qq}48"
+ "setMinTimeBetweenBDSessionsPastNight:"
+ "isRequirementSatisfiedWithIdentifier:"
+ "breathingDisturbanceSamples"
+ "nebula"
+ "setNumBDValuesInPastNight:"
+ "_processQueryResultsWithSummaries:breathingDisturbanceSamples:sleepApneaFeatureStatus:queryRange:error:"
+ "@\"HDSPSleepApneaAnalyticsBuilder\""
+ "@\"NSCalendar\""
+ "_sleepApneaAnalyticsBuilder"
+ "_numBDValuesInPastNight:"
+ "initWithQueryDescriptors:limit:sortDescriptors:resultsHandler:"
+ "initWithFeatureIdentifier:healthStore:"
+ "valueForKeyPath:"
+ "@\"HKFeatureStatus\""
+ "B16@?0@\"HKSample\"8"
+ "setMeanTimeBetweenBDSessionsPastNight:"
+ "_gregorianCalendar"
+ "T@\"NSCalendar\",R,N,V_gregorianCalendar"
+ "T@\"HDSPSleepApneaAnalyticsBuilder\",R,N,V_sleepApneaAnalyticsBuilder"
+ "[%!{(MISSING)public}@] Queries succeeded"
+ "_breathingDisturbanceSamples"
+ "updateDailyReportWithSleepApneaAnalytics:"
+ "@avg.doubleValue"
+ "_minTimeBetweenBDSessionsPastNight:"
+ "v64@0:8@16@24@32{?=qq}40@56"
+ "[%!{(MISSING)public}@] Building daily analytics report from %!{(MISSING)public}lu bd samples"
+ "@max.doubleValue"
+ "HDSPSleepApneaAnalyticsBuilder"
+ "_timesBetweenBDSessions:"
+ "_sleepApneaFeatureStatus"
+ "initWithSampleType:predicate:"
+ "_isOnboardedBD"
+ "@min.doubleValue"
+ "sleepApneaAnalyticsBuilder"
+ "[%!{(MISSING)public}@] Queries failed with error: %!{(MISSING)public}@"
+ "[%!{(MISSING)public}@] Beginning bd queries"
- "[%!{(MISSING)public}@] Query succeeded"
- "_processQueryResultsWithSummaries:queryRange:error:"
- "v48@0:8@16{?=qq}24@40"

```
