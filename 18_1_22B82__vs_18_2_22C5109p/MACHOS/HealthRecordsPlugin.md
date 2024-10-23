## HealthRecordsPlugin

> `/System/Library/Health/Plugins/HealthRecordsPlugin.bundle/HealthRecordsPlugin`

```diff

-5200.1.18.0.0
-  __TEXT.__text: 0xb1ef4
-  __TEXT.__auth_stubs: 0xda0
-  __TEXT.__objc_stubs: 0x130a0
-  __TEXT.__objc_methlist: 0x7bbc
-  __TEXT.__objc_methname: 0x1d11a
-  __TEXT.__objc_classname: 0x1bee
-  __TEXT.__objc_methtype: 0x3571
-  __TEXT.__const: 0x1f4
-  __TEXT.__gcc_except_tab: 0x22c0
-  __TEXT.__cstring: 0xa0b8
-  __TEXT.__oslogstring: 0xebc9
+5200.2.4.1.5
+  __TEXT.__text: 0xb0530
+  __TEXT.__auth_stubs: 0xf90
+  __TEXT.__objc_stubs: 0x12c20
+  __TEXT.__objc_methlist: 0x7854
+  __TEXT.__objc_methname: 0x1cb7d
+  __TEXT.__objc_classname: 0x1a7d
+  __TEXT.__objc_methtype: 0x3433
+  __TEXT.__const: 0x248
+  __TEXT.__gcc_except_tab: 0x2154
+  __TEXT.__cstring: 0x9e45
+  __TEXT.__oslogstring: 0xea45
   __TEXT.__ustring: 0x7e
-  __TEXT.__unwind_info: 0x2818
-  __DATA_CONST.__auth_got: 0x6e0
-  __DATA_CONST.__got: 0xef0
-  __DATA_CONST.__const: 0x3828
-  __DATA_CONST.__cfstring: 0x7780
-  __DATA_CONST.__objc_classlist: 0x4d8
+  __TEXT.__constg_swiftt: 0x38
+  __TEXT.__swift5_typeref: 0xfc
+  __TEXT.__swift5_reflstr: 0xc
+  __TEXT.__swift5_fieldmd: 0x1c
+  __TEXT.__swift5_capture: 0xac
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__unwind_info: 0x27d8
+  __TEXT.__eh_frame: 0x1d0
+  __DATA_CONST.__auth_got: 0x7d8
+  __DATA_CONST.__got: 0xf58
+  __DATA_CONST.__auth_ptr: 0x20
+  __DATA_CONST.__const: 0x39b8
+  __DATA_CONST.__cfstring: 0x7320
+  __DATA_CONST.__objc_classlist: 0x4a8
   __DATA_CONST.__objc_catlist: 0x128
-  __DATA_CONST.__objc_protolist: 0x158
+  __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x3a8
-  __DATA_CONST.__objc_intobj: 0x6c0
+  __DATA_CONST.__objc_superrefs: 0x370
+  __DATA_CONST.__objc_intobj: 0x5d0
   __DATA_CONST.__objc_arraydata: 0x1d8
   __DATA_CONST.__objc_arrayobj: 0x120
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0xeb20
-  __DATA.__objc_selrefs: 0x55e0
-  __DATA.__objc_ivar: 0x71c
-  __DATA.__objc_data: 0x25d0
-  __DATA.__data: 0x1028
+  __DATA.__objc_const: 0xe118
+  __DATA.__objc_selrefs: 0x5498
+  __DATA.__objc_ivar: 0x6d8
+  __DATA.__objc_data: 0x24d8
+  __DATA.__data: 0xfd0
   __DATA.__bss: 0x60
-  __DATA_DIRTY.__objc_data: 0xaa0
+  __DATA_DIRTY.__objc_data: 0xa20
+  __DATA_DIRTY.__data: 0x28
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/HealthRecordServices.framework/HealthRecordServices
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3385
-  Symbols:   1088
-  CStrings:  5966
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 3363
+  Symbols:   1103
+  CStrings:  5848
 
Symbols:
+ _OBJC_CLASS_$_HKAsynchronousOperation
+ __Block_copy
+ __Block_release
+ ___chkstk_darwin
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _swift_allocObject
+ _swift_bridgeObjectRelease
+ _swift_deallocObject
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getWitnessTable
+ _swift_release
+ _swift_retain
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
- _HDClinicalAnalyticsInferredInteractionTypeFromFHIRResourcePathComponents
- _HDClinicalAnalyticsResourceTypeNil
- _NSStringFromClinicalIngestionAnalyticsInteractionType
- _OBJC_CLASS_$_HDClinicalIngestionAnalyticsAccumulator
- _OBJC_CLASS_$_HDClinicalIngestionAnalyticsMetricKey
- _OBJC_CLASS_$_HDClinicalIngestionRequestFailureMetric
- _OBJC_CLASS_$_HDClinicalIngestionRequestFailureMetricElement
- _OBJC_CLASS_$_HDClinicalIngestionResponseTimeMetric
- _OBJC_CLASS_$_HDClinicalIngestionResponseTimeMetricElement
- _OBJC_CLASS_$__HDClinicalIngestionResponseTimeMetricValue
- _OBJC_METACLASS_$_HDClinicalIngestionAnalyticsAccumulator
- _OBJC_METACLASS_$_HDClinicalIngestionAnalyticsMetricKey
- _OBJC_METACLASS_$_HDClinicalIngestionRequestFailureMetric
- _OBJC_METACLASS_$_HDClinicalIngestionRequestFailureMetricElement
- _OBJC_METACLASS_$_HDClinicalIngestionResponseTimeMetric
- _OBJC_METACLASS_$_HDClinicalIngestionResponseTimeMetricElement
- _OBJC_METACLASS_$__HDClinicalIngestionResponseTimeMetricValue
- __HistoryPathComponent
- __MetadataPathComponent
- __SearchPathComponent
CStrings:
+ "\x032"
+ "%!@(MISSING) failed to retrieve account %!@(MISSING) for record %!@(MISSING): %!@(MISSING)"
+ "%!{(MISSING)public}@: %!l(MISSING)d ingestion analytics submitted"
+ "%!{(MISSING)public}@: checking to submit ingestion analytics"
+ "%!{(MISSING)public}@: metric on gateway from %!{(MISSING)public}@ may not be submitted, discarding"
+ "%!{(MISSING)public}@: not submitting ingestion analytics: %!{(MISSING)public}@"
+ "%!{(MISSING)public}@: submitting ingestion analytics"
+ "%!{(MISSING)public}@: submitting payload"
+ "B32@?0@\"NSString\"8@\"NSString\"16@\"NSDictionary\"24"
+ "IHR data submission has not been allowed by the user"
+ "T@\"HDClinicalIngestionAnalyticsAccumulator\",R,N,V_analyticsAccumulator"
+ "_accumulateMetricsFromTaskEndStates:gateway:"
+ "_addMetricElementsForRulesVersion:hostURL:resourceType:failureInfo:"
+ "_analyticsAccumulator"
+ "_analyticsStringAfterCollectingAndSubmittingIngestionAnalyticsOnQueue:"
+ "_submitPayload:forEvent:usingCoordinator:"
+ "accumulateIngestionAnalyticsFromTaskStates:gateway:"
+ "accumulateIngestionAnalyticsFromTaskStates:gateway:completion:"
+ "analyticsAccumulator"
+ "asErrorEndStateWithErrorCode:"
+ "consumeMetricsFromHandler:completion:"
+ "createClinicalAnalyticsManager"
+ "endStateForCanceledRequestAtURL:resourceType:interactionType:"
+ "enumerateForCoreAnalyticsAndResetWithBlock:completion:"
+ "hk_OAuth2_errorCode"
+ "http://localhost/error-retrieving-account-for-resource"
+ "http://localhost/gateway-without-baseURL"
+ "http://localhost/unable-to-retrieve-account-for-resource"
+ "ingestion-analytics-submission"
+ "initWithName:operationBlock:"
+ "initWithRequestedURL:resourceType:interactionType:responseStatusCode:requestEndTime:requestDuration:hadError:errorCode:"
+ "submitClinicalIngestionAnalyticsFromAccumulator:completion:"
+ "v16@?0@\"NSString\"8"
+ "v32@0:8@?16@?24"
- "\x031"
- "%!@(MISSING)\n%!@(MISSING)"
- "%!@(MISSING) %!l(MISSING)u ms"
- "%!@(MISSING) -- %!@(MISSING)"
- "%!@(MISSING) --> %!@(MISSING)"
- "%!@(MISSING) --> %!@(MISSING)x"
- "%!@(MISSING) failed to retrieve original FHIR resource matching record %!@(MISSING) on account %!@(MISSING): %!@(MISSING)"
- "%!@(MISSING) submitting %!z(MISSING)d request failure metrics as \"com.apple.HealthRecords.ProcessingIngestionRequestFailureEvent\" to CoreAnalytics"
- "%!@(MISSING) submitting %!z(MISSING)d response time metrics as \"com.apple.HealthRecords.ProcessingIngestionResponseTimeEvent\" to CoreAnalytics"
- "%!@(MISSING), %!l(MISSING)u elements:\n\t%!@(MISSING)"
- "%!l(MISSING)u responses [%!@(MISSING) ms, %!@(MISSING) ms, %!@(MISSING) ms]"
- "%!{(MISSING)public}@ consumeAndResetIngestionAnalyticsMetricsFromAccumulator can only consume analytics from an accumulator that has the same country code setup (%!{(MISSING)public}@) as has the receiver (%!{(MISSING)public}@)"
- "%!{(MISSING)public}@ ingestion analytics metrics for country \"%!{(MISSING)public}@\" are not enabled, dropping metric: %!{(MISSING)public}@"
- "%!{(MISSING)public}@ unable to accumulate unknown metric element: %!{(MISSING)public}@"
- "(%!@(MISSING), %!@(MISSING), %!@(MISSING))"
- "(%!@(MISSING), %!@(MISSING), %!l(MISSING)u, %!@(MISSING))"
- "/%!@(MISSING)"
- "1 response [%!@(MISSING) ms]"
- "<%!@(MISSING) %!p(MISSING)> 0 elements"
- "@\"HDClinicalIngestionAnalyticsMetricKey\""
- "@\"HDClinicalIngestionAnalyticsMetricKey\"16@0:8"
- "@\"HDClinicalIngestionRequestFailureMetric\""
- "@\"HDClinicalIngestionResponseTimeMetric\""
- "@\"NSNumber\"16@0:8"
- "@32@0:8@16Q24"
- "@40@0:8@16@24Q32"
- "@40@0:8@16@24d32"
- "@40@0:8@16@24q32"
- "@48@0:8@16@24q32Q40"
- "@56@0:8@16@24q32Q40@48"
- "@avg.self"
- "B16@?0@\"NSString\"8"
- "FHIRRead"
- "FHIRSearch"
- "HDClinicalIngestionAnalyticsAccumulator.m"
- "HDClinicalIngestionAnalyticsMetric"
- "HDClinicalIngestionAnalyticsMetricElement"
- "HDClinicalIngestionAnalyticsMetricKey"
- "HDClinicalIngestionRequestFailureMetric"
- "HDClinicalIngestionRequestFailureMetric.m"
- "HDClinicalIngestionRequestFailureMetricElement"
- "HDClinicalIngestionResponseTimeMetric"
- "HDClinicalIngestionResponseTimeMetric.m"
- "HDClinicalIngestionResponseTimeMetricElement"
- "Ingestion Analytics:\n%!{(MISSING)public}@\n%!{(MISSING)public}@"
- "OAuth2CodeExchange"
- "OAuth2TokenRefresh"
- "T@\"HDClinicalIngestionAnalyticsMetricKey\",R,C,N"
- "T@\"HDClinicalIngestionAnalyticsMetricKey\",R,C,N,V_keyElement"
- "T@\"HDClinicalIngestionRequestFailureMetric\",R,N,V_requestFailures"
- "T@\"HDClinicalIngestionResponseTimeMetric\",R,N,V_responseTimes"
- "T@\"NSDate\",R,C,N,V_observedDate"
- "T@\"NSDictionary\",&,N,V_collectedMetrics"
- "T@\"NSDictionary\",R,N"
- "T@\"NSMutableArray\",&,N,V_mutableResponseTimes"
- "T@\"NSMutableDictionary\",&,N,V_elements"
- "T@\"NSNumber\",R,C,N"
- "T@\"NSNumber\",R,C,N,V_max"
- "T@\"NSNumber\",R,C,N,V_median"
- "T@\"NSNumber\",R,C,N,V_min"
- "TQ,R,N"
- "TQ,R,N,V_responseTime"
- "TQ,R,N,V_statusCode"
- "Tq,R,N,V_interactionType"
- "Unknown"
- "UnknownResourceType"
- "[element isKindOfClass:[HDClinicalIngestionRequestFailureMetricElement class]]"
- "[element isKindOfClass:[HDClinicalIngestionResponseTimeMetricElement class]]"
- "_HDClinicalIngestionResponseTimeMetricValue"
- "_accumulateMetricsFromTaskEndStates:resourceType:interactionType:gateway:"
- "_addMetricElementsForRulesVersion:sourceURL:resourceType:failureInfo:"
- "_calculate"
- "_collectCurrentIngestionAnalytics"
- "_collectedMetrics"
- "_history"
- "_interactionType"
- "_keyElement"
- "_max"
- "_median"
- "_min"
- "_mutableResponseTimes"
- "_observedDate"
- "_requestFailures"
- "_responseTime"
- "_responseTimes"
- "_search"
- "_statusCode"
- "accumulateIngestionAnalyticsMetric:gatewayCountryCode:"
- "addRequestFailureMetricElement:"
- "addResponseTime:"
- "addResponseTimeMetricElement:"
- "addResponseTimesFromMetricValue:"
- "analyticsMetricKeyWithResourceURL:baseURL:"
- "arrayWithObject:"
- "asErrorEndState"
- "caseInsensitiveCompare:"
- "collectedMetrics"
- "com.apple.HealthRecords.ProcessingIngestionRequestFailureEvent"
- "com.apple.HealthRecords.ProcessingIngestionResponseTimeEvent"
- "combineWithMetric:"
- "consumeAndResetIngestionAnalyticsMetricsFromAccumulator:"
- "endStateForCanceledRequestAtURL:"
- "gatewayCountryCode"
- "hadError"
- "hk_removeObjectsPassingTest:"
- "hk_rfc3339String"
- "hrs_fhirResourcePathComponentsAgainstBaseURL:"
- "ingestionEventCount"
- "ingestionFailureEventCount"
- "ingestionTimeStamp"
- "initWithKeyElement:responseTime:"
- "initWithReportedHost:resourceType:interactionType:"
- "initWithReportedHost:resourceType:interactionType:statusCode:observedDate:"
- "initWithRequestedURL:responseStatusCode:requestDuration:hadError:"
- "initWithResponseTime:"
- "initWithTimeIntervalSinceReferenceDate:"
- "isEqualToSet:"
- "keyElement"
- "logMetrics"
- "lowercaseString"
- "max"
- "maxTime"
- "median"
- "medianTime"
- "metric"
- "metricElement"
- "metricWithSourceURL:baseURL:statusCode:"
- "metricWithSourceURL:baseURL:timeInterval:"
- "metricWithSourceURL:resourceType:interactionType:statusCode:"
- "metricWithSourceURL:resourceType:interactionType:timeInterval:"
- "min"
- "minTime"
- "mutableResponseTimes"
- "observedDate"
- "removeLastObject"
- "reportableObservedDateString"
- "reportedHostFromSourceURL:resourceType:"
- "requestDuration"
- "requestFailures"
- "responseStatusCode"
- "responseTime"
- "responseTimes"
- "setCollectedMetrics:"
- "setElements:"
- "setFragment:"
- "setMutableResponseTimes:"
- "setQuery:"
- "sortUsingSelector:"
- "sortedArrayUsingSelector:"
- "v32@?0@\"HDClinicalIngestionAnalyticsMetricKey\"8@\"NSNumber\"16^B24"
- "v32@?0@\"HDClinicalIngestionAnalyticsMetricKey\"8@\"_HDClinicalIngestionResponseTimeMetricValue\"16^B24"
- "v48@0:8@16@24q32@40"
- "valueForKeyPath:"

```
