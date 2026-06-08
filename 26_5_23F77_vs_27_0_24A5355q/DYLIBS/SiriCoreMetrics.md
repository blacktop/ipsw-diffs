## SiriCoreMetrics

> `/System/Library/PrivateFrameworks/SiriCoreMetrics.framework/SiriCoreMetrics`

```diff

-5.4.1.0.0
-  __TEXT.__text: 0x1af84
-  __TEXT.__auth_stubs: 0xf20
+6.0.1.0.0
+  __TEXT.__text: 0x19898
   __TEXT.__const: 0x15cc
-  __TEXT.__swift5_typeref: 0x6fa
+  __TEXT.__swift5_typeref: 0x6a8
   __TEXT.__cstring: 0x716
   __TEXT.__constg_swiftt: 0x678
   __TEXT.__swift5_reflstr: 0x587

   __TEXT.__swift5_assocty: 0x128
   __TEXT.__swift_as_entry: 0x64
   __TEXT.__swift_as_ret: 0x48
-  __TEXT.__unwind_info: 0x6f8
+  __TEXT.__swift_as_cont: 0x68
+  __TEXT.__unwind_info: 0x6f0
   __TEXT.__eh_frame: 0x8a8
-  __TEXT.__objc_classname: 0x247
-  __TEXT.__objc_methname: 0x609
-  __TEXT.__objc_methtype: 0x1
-  __TEXT.__objc_stubs: 0x780
-  __DATA_CONST.__got: 0x1d8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1e0
-  __AUTH_CONST.__auth_got: 0x798
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x6f0
   __AUTH_CONST.__cfstring: 0x3c0
   __AUTH_CONST.__objc_const: 0x720
+  __AUTH_CONST.__auth_got: 0x818
   __AUTH.__objc_data: 0x2d0
   __AUTH.__data: 0xa00
-  __DATA.__data: 0x510
+  __DATA.__data: 0x4f8
   __DATA.__bss: 0x2000
   __DATA.__common: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D659CB32-FF68-381A-BA49-8F83A7DC4B10
+  UUID: 17A420C7-AFE4-32AB-8602-2CE75C76C6A2
   Functions: 578
-  Symbols:   461
-  CStrings:  189
+  Symbols:   483
+  CStrings:  104
 
Symbols:
+ ___swift_async_cont_functlets
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_SiriCoreMetrics
+ _objc_retain_x24
+ _swift_release_x1
+ _swift_release_x12
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x26
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_SiriCoreMetrics
- _objc_retain
- _objc_retain_x19
- _objc_retain_x25
- _objc_retain_x26
- _swift_bridgeObjectRetain_n
- _swift_retain
- _symbolic _____3key_Say_____G5valuetSg 11DeepThought19AggregationIntervalV 15SiriCoreMetrics0E9CountsAllV
- _symbolic _____3key______5valuetSg 11DeepThought19AggregationIntervalV 15SiriCoreMetrics0E13RequestCountsV
- _symbolic _____3key______5valuetSg 15SiriCoreMetrics0abC15AggregationKeysV AA0A13RequestCountsV
CStrings:
- "PrivateLearning"
- "SELFEvent"
- "Siri"
- "SiriRequestCounts"
- "_TtC15SiriCoreMetrics15SiriCoreMetrics"
- "_TtC15SiriCoreMetrics17SiriCoreMetricsV2"
- "_TtC15SiriCoreMetrics23SiriCoreMetricsReporter"
- "_TtC15SiriCoreMetrics25SiriCoreMetricsCalculator"
- "_TtC15SiriCoreMetrics27SiriCoreMetricsCalculatorV2"
- "_TtC15SiriCoreMetrics27SiriCoreMetricsDataProvider"
- "_TtC15SiriCoreMetrics27SiriCoreMetricsSELFReporter"
- "_TtC15SiriCoreMetrics28SiriCoreMetricsBiomeReporter"
- "_TtC15SiriCoreMetrics29SiriCoreMetricsSELFReporterV2"
- "_TtC15SiriCoreMetrics34SiriCoreMetricsJsonLoggingReporter"
- "addSegments:"
- "addSiriCountsAll:"
- "addSiriTurnRestatementScores:"
- "aggregationWindowStartTimestamp"
- "anyEventType"
- "autoupdatingCurrentLocale"
- "biomeDonator"
- "bookmarkService"
- "calendar"
- "conversationTurnType"
- "conversationType"
- "defaultMessageStream"
- "emitMessage:"
- "event"
- "eventData"
- "eventMetadata"
- "featurizedConversationProvider"
- "infoDictionary"
- "init"
- "initWithAllRequestCount:userRequestCount:"
- "initWithBytesAsData:"
- "initWithData:"
- "initWithMetadata:statistics:"
- "initWithNSUUID:"
- "initWithSchedule:aggregationWindowStartTimestamp:odmId:"
- "initWithSuiteName:"
- "isEqualToString:"
- "jsonResult"
- "logger"
- "mainBundle"
- "metadata"
- "odmClientEventsCountsReportedAll"
- "odmClientEventsTurnRestatementScores"
- "odmId"
- "payload"
- "schedule"
- "setAggregationInterval:"
- "setAggregationIntervalInDays:"
- "setAggregationIntervalStartTimestampInSecondsSince2001:"
- "setAllRequestCount:"
- "setAudioInterface:"
- "setCountsReportedAll:"
- "setCurrentTurnId:"
- "setDeploymentId:"
- "setDimensions:"
- "setEventMetadata:"
- "setExperimentId:"
- "setIsUserRequest:"
- "setNextTurnId:"
- "setOdmId:"
- "setPhoneticRestatementScore:"
- "setPluginVersion:"
- "setProduct:"
- "setRequestCounts:"
- "setSiriDataSharingOptInStatus:"
- "setSiriInputLocale:"
- "setTreatmentId:"
- "setTrialExperimentIdentifiers:"
- "setTurnRestatementScoresReported:"
- "setUserRequestCount:"
- "setUtteranceRestatementScore:"
- "setViewMode:"
- "sharedAnalytics"
- "siriCoreMetricsCalculator"
- "siriCoreMetricsDataProvider"
- "siriCoreMetricsReporter"
- "source"
- "statistics"
- "stream"
- "turnID"

```
