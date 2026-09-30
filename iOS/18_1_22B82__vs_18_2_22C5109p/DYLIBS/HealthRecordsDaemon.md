## HealthRecordsDaemon

> `/System/Library/PrivateFrameworks/HealthRecordsDaemon.framework/HealthRecordsDaemon`

```diff

-5200.1.18.0.0
-  __TEXT.__text: 0x2d27b8
-  __TEXT.__auth_stubs: 0x2d50
+5200.2.4.1.5
+  __TEXT.__text: 0x2cae58
+  __TEXT.__auth_stubs: 0x2db0
   __TEXT.__objc_methlist: 0x3a0
-  __TEXT.__const: 0x17608
-  __TEXT.__cstring: 0xb51f
-  __TEXT.__constg_swiftt: 0x7270
-  __TEXT.__swift5_typeref: 0x4981
+  __TEXT.__const: 0x17148
+  __TEXT.__cstring: 0xb07f
+  __TEXT.__constg_swiftt: 0x6f6c
+  __TEXT.__swift5_typeref: 0x485b
   __TEXT.__swift5_builtin: 0x21c
-  __TEXT.__swift5_reflstr: 0x5f11
-  __TEXT.__swift5_fieldmd: 0x7478
-  __TEXT.__swift5_assocty: 0xdf0
-  __TEXT.__swift5_proto: 0x1464
-  __TEXT.__swift5_types: 0x6c8
-  __TEXT.__swift5_capture: 0x2280
-  __TEXT.__swift5_protos: 0x60
-  __TEXT.__oslogstring: 0x3bd8
+  __TEXT.__swift5_reflstr: 0x5e01
+  __TEXT.__swift5_fieldmd: 0x72cc
+  __TEXT.__swift5_assocty: 0xdd8
+  __TEXT.__swift5_proto: 0x1434
+  __TEXT.__swift5_types: 0x6a0
+  __TEXT.__swift5_capture: 0x2330
+  __TEXT.__swift5_protos: 0x50
+  __TEXT.__oslogstring: 0x3a28
   __TEXT.__swift5_mpenum: 0x38
-  __TEXT.__unwind_info: 0x9bf0
-  __TEXT.__eh_frame: 0x8290
+  __TEXT.__unwind_info: 0x9aa8
+  __TEXT.__eh_frame: 0x8378
   __TEXT.__objc_classname: 0x16f
-  __TEXT.__objc_methname: 0x2f2d
+  __TEXT.__objc_methname: 0x2fd5
   __TEXT.__objc_methtype: 0x73e
-  __DATA_CONST.__got: 0xfc0
+  __DATA_CONST.__got: 0xfc8
   __DATA_CONST.__const: 0x1740
-  __DATA_CONST.__objc_classlist: 0x290
+  __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf28
+  __DATA_CONST.__objc_selrefs: 0xf40
   __DATA_CONST.__objc_protorefs: 0x58
-  __AUTH_CONST.__auth_got: 0x16a8
-  __AUTH_CONST.__auth_ptr: 0xf50
-  __AUTH_CONST.__const: 0xdb18
-  __AUTH_CONST.__objc_const: 0x5b60
-  __AUTH.__objc_data: 0x1590
-  __AUTH.__data: 0x9fc8
+  __AUTH_CONST.__auth_got: 0x16d8
+  __AUTH_CONST.__auth_ptr: 0xf38
+  __AUTH_CONST.__const: 0xd920
+  __AUTH_CONST.__objc_const: 0x5900
+  __AUTH.__objc_data: 0x1540
+  __AUTH.__data: 0x9c60
   __DATA.__data: 0x7438
-  __DATA.__bss: 0x245e0
-  __DATA.__common: 0x38
+  __DATA.__bss: 0x24360
+  __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x370
   __DATA_DIRTY.__data: 0x2270
   __DATA_DIRTY.__bss: 0xc00

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 14774
-  Symbols:   663
-  CStrings:  2455
+  Functions: 14622
+  Symbols:   665
+  CStrings:  2425
 
Symbols:
+ _OBJC_CLASS_$_HKFHIRRequestTaskEndState
+ _OBJC_CLASS_$_HKFHIRRequestTaskEndStates
- _lround
- _swift_dynamicCastClass
CStrings:
+ "%!s(MISSING) will not submit analytics, submission not enabled"
+ "Analytics to submit: %!s(MISSING)"
+ "asErrorEndStateWithErrorCode:"
+ "initWithEndState:"
+ "initWithRequestedURL:resourceType:interactionType:responseStatusCode:requestEndTime:requestDuration:hadError:errorCode:"
- "%!l(MISSING)u responses [%!f(MISSING) ms, %!f(MISSING) ms, %!f(MISSING) ms]"
- "%!s(MISSING) captured Analytics \n %!s(MISSING)"
- "1 response [%!f(MISSING) ms]"
- "ClinicalIngestionAnalyticsAccumulator submitting %!l(MISSING)d request failures metrics to CoreAnalytics"
- "ClinicalIngestionAnalyticsAccumulator submitting %!l(MISSING)d response time metrics to CoreAnalytics"
- "ClinicalIngestionAnalyticsAccumulator submitting request failure metrics as \"%!s(MISSING)\" to CoreAnalytics"
- "ClinicalIngestionAnalyticsAccumulator submitting response time metrics as \"%!s(MISSING)\" to CoreAnalytics"
- "ClinicalIngestionAnalyticsAccumulator unable to accumulate unknown metric element: %!s(MISSING)"
- "ClinicalIngestionRequestFailureMetric 0 elements"
- "ClinicalIngestionRequestFailureMetric, "
- "ClinicalIngestionResponseTimeMetric 0 elements"
- "ClinicalIngestionResponseTimeMetric, "
- "ClinicalIngestionResponseTimeMetricValue: Error reading response times"
- "HealthRecordsDaemon.ClinicalIngestionRequestFailureMetricElement"
- "UnknownResourceType"
- "_TtC19HealthRecordsDaemon35ClinicalIngestionAnalyticsMetricKey"
- "_TtC19HealthRecordsDaemon37ClinicalIngestionAnalyticsAccumulator"
- "_TtC19HealthRecordsDaemon44ClinicalIngestionRequestFailureMetricElement"
- "com.apple.health.clinical-records.health-card-issue.timeEvent"
- "com.apple.health.clinical-records.unknown"
- "healthCardIssueOperation"
- "ingestionEventCount"
- "ingestionFailureEventCount"
- "ingestionTimeStamp"
- "init(reportedHost:resourceType:interactionType:)"
- "init(with:interactionType:)"
- "interactionType"
- "observedDate"
- "reportedHost"
- "requestFailures"
- "resourceType"
- "responseTimes"
- "unknown"
- "yyyy'-'MM'-'dd'T'HH':'mm':'ss'Z'"

```
