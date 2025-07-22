## Summaries

> `/System/Library/Health/FeedItemPlugins/Summaries.healthplugin/Summaries`

```diff

-6093.0.0.0.0
-  __TEXT.__text: 0x17331c
-  __TEXT.__auth_stubs: 0x6c00
-  __TEXT.__objc_methlist: 0x280
-  __TEXT.__cstring: 0x724d
-  __TEXT.__const: 0x9154
-  __TEXT.__constg_swiftt: 0x405c
-  __TEXT.__swift5_typeref: 0x369e
+6100.0.0.0.0
+  __TEXT.__text: 0x177778
+  __TEXT.__auth_stubs: 0x6ce0
+  __TEXT.__objc_methlist: 0x2f0
+  __TEXT.__cstring: 0x751d
+  __TEXT.__const: 0x9204
+  __TEXT.__constg_swiftt: 0x40a8
+  __TEXT.__swift5_typeref: 0x36e6
   __TEXT.__swift5_builtin: 0x154
-  __TEXT.__swift5_reflstr: 0x36a0
+  __TEXT.__swift5_reflstr: 0x3840
   __TEXT.__swift5_assocty: 0xe08
-  __TEXT.__swift5_fieldmd: 0x26e0
+  __TEXT.__swift5_fieldmd: 0x2774
   __TEXT.__swift5_proto: 0x6fc
-  __TEXT.__swift5_types: 0x398
-  __TEXT.__oslogstring: 0x4e97
+  __TEXT.__swift5_types: 0x39c
+  __TEXT.__oslogstring: 0x4fe7
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__swift5_capture: 0x12b0
+  __TEXT.__swift5_capture: 0x12b4
   __TEXT.__swift5_protos: 0x60
-  __TEXT.__swift_as_entry: 0x14
-  __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0x3398
-  __TEXT.__eh_frame: 0x33a4
-  __TEXT.__objc_classname: 0x99
-  __TEXT.__objc_methname: 0x30df
-  __TEXT.__objc_methtype: 0x282
-  __DATA_CONST.__got: 0x1cc8
+  __TEXT.__swift_as_entry: 0x2c
+  __TEXT.__swift_as_ret: 0x48
+  __TEXT.__unwind_info: 0x3528
+  __TEXT.__eh_frame: 0x3984
+  __TEXT.__objc_classname: 0xaa
+  __TEXT.__objc_methname: 0x3224
+  __TEXT.__objc_methtype: 0x2c5
+  __DATA_CONST.__got: 0x1ce8
   __DATA_CONST.__const: 0x120
-  __DATA_CONST.__objc_classlist: 0x120
-  __DATA_CONST.__objc_protolist: 0x60
+  __DATA_CONST.__objc_classlist: 0x128
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1150
-  __DATA_CONST.__objc_protorefs: 0x30
-  __AUTH_CONST.__auth_got: 0x3600
-  __AUTH_CONST.__const: 0x67b8
-  __AUTH_CONST.__objc_const: 0x2e70
+  __DATA_CONST.__objc_selrefs: 0x1190
+  __DATA_CONST.__objc_protorefs: 0x38
+  __AUTH_CONST.__auth_got: 0x3670
+  __AUTH_CONST.__const: 0x6830
+  __AUTH_CONST.__objc_const: 0x30f8
   __AUTH.__objc_data: 0x758
-  __AUTH.__data: 0x2408
-  __DATA.__data: 0x1ae0
+  __AUTH.__data: 0x24e0
+  __DATA.__data: 0x1ba8
   __DATA.__objc_stublist: 0x40
   __DATA.__bss: 0x7070
   __DATA.__common: 0xf0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1AF4CBCC-BD5F-3920-AD8A-0300959F96C2
-  Functions: 4652
-  Symbols:   461
-  CStrings:  1554
+  UUID: 8D74705C-0E2E-3347-B795-DB4A98D4B875
+  Functions: 4719
+  Symbols:   470
+  CStrings:  1594
 
Symbols:
+ _HKLogAnalytics
+ _HKQuantityTypeIdentifierBloodPressureDiastolic
+ _HKQuantityTypeIdentifierBloodPressureSystolic
+ _OBJC_CLASS_$_HKAnalyticsEventSubmissionManager
+ _objc_autorelease
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _swift_task_create
- _OBJC_CLASS_$_HKCorrelationType
CStrings:
+ "%s]: Failed to submit analytics event: %@"
+ "@\"NSDictionary\"32@0:8@\"HKAnalyticsDataSource\"16^@24"
+ "@32@0:8@16^@24"
+ "Failed to submit analytics event: %@"
+ "Found orphaned blood pressure diastolic sample."
+ "Found orphaned blood pressure systolic sample."
+ "HKAnalyticsEvent"
+ "T@\"NSString\",N,R"
+ "T@\"NSString\",R,N"
+ "TB,N,R"
+ "TB,R,N"
+ "[%s]: Found a correlated blood pressure sample without a diasatolic sample."
+ "[%s]: Found a correlated blood pressure sample without a systolic sample."
+ "[%s]: No correlated blood pressure samples found"
+ "_TtC9Summaries27BloodPressureAnalyticsEvent"
+ "analyticsEventSubmissionManager"
+ "com.apple.health.bp.snippetupdates"
+ "diastolicType"
+ "eventName"
+ "fetchLatestCorrelationSample()"
+ "fetchMostRecentUncorrelatedBloodPressureSample(for:startDate:endDate:)"
+ "filteredOutCorrelationMissingDiastolic"
+ "filteredOutCorrelationMissingDiastolicField"
+ "filteredOutCorrelationMissingSystolic"
+ "filteredOutCorrelationMissingSystolicField"
+ "ignoredOrphanedDiastolicSample"
+ "ignoredOrphanedDiastolicSampleField"
+ "ignoredOrphanedSystolicSample"
+ "ignoredOrphanedSystolicSampleField"
+ "initWithLoggingCategory:healthDataSource:"
+ "initWithSampleType:predicate:limit:sortDescriptors:resultsHandler:"
+ "isEventSubmissionIHAGated"
+ "makeIHAGatedEventPayloadWithDataSource:error:"
+ "makeUnrestrictedEventPayloadWithDataSource:error:"
+ "objectsForType:"
+ "predicateForObjectsWithNoCorrelation"
+ "predicateForSamplesWithStartDate:endDate:options:"
+ "submitEvent:completion:"
+ "systolicType"
- "%ld samples are not enough for %s correlation, returning no data"
- "_setSourceRevision:"
- "correlationWithType:startDate:endDate:objects:"

```
