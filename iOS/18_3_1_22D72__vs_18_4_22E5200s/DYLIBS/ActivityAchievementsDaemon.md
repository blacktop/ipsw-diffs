## ActivityAchievementsDaemon

> `/System/Library/PrivateFrameworks/ActivityAchievementsDaemon.framework/ActivityAchievementsDaemon`

```diff

-611.13.0.0.0
-  __TEXT.__text: 0x7cae4
-  __TEXT.__auth_stubs: 0x1240
-  __TEXT.__objc_methlist: 0x665c
-  __TEXT.__const: 0x1c8
-  __TEXT.__cstring: 0x62d9
-  __TEXT.__gcc_except_tab: 0x2828
-  __TEXT.__oslogstring: 0x9e38
-  __TEXT.__unwind_info: 0x2278
-  __TEXT.__objc_classname: 0xd86
-  __TEXT.__objc_methname: 0x13f13
-  __TEXT.__objc_methtype: 0x284f
-  __TEXT.__objc_stubs: 0xba40
-  __DATA_CONST.__got: 0x720
-  __DATA_CONST.__const: 0x2b98
-  __DATA_CONST.__objc_classlist: 0x240
+612.6.0.0.0
+  __TEXT.__text: 0x7b068
+  __TEXT.__auth_stubs: 0x11f0
+  __TEXT.__objc_methlist: 0x6f3c
+  __TEXT.__const: 0x1b0
+  __TEXT.__cstring: 0x61e4
+  __TEXT.__gcc_except_tab: 0x2870
+  __TEXT.__oslogstring: 0x9e17
+  __TEXT.__unwind_info: 0x2230
+  __TEXT.__objc_classname: 0xd57
+  __TEXT.__objc_methname: 0x13976
+  __TEXT.__objc_methtype: 0x2800
+  __TEXT.__objc_stubs: 0xb7e0
+  __DATA_CONST.__got: 0x6f8
+  __DATA_CONST.__const: 0x2af0
+  __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3c60
+  __DATA_CONST.__objc_selrefs: 0x3c20
   __DATA_CONST.__objc_protorefs: 0x90
-  __DATA_CONST.__objc_superrefs: 0x1f0
+  __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x198
-  __AUTH_CONST.__auth_got: 0x930
+  __AUTH_CONST.__auth_got: 0x908
   __AUTH_CONST.__const: 0xa60
-  __AUTH_CONST.__cfstring: 0x2e20
-  __AUTH_CONST.__objc_const: 0x16c08
-  __AUTH_CONST.__objc_intobj: 0x348
+  __AUTH_CONST.__cfstring: 0x2c80
+  __AUTH_CONST.__objc_const: 0x15188
+  __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x82c
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0x800
   __DATA.__data: 0x10e0
-  __DATA.__bss: 0x18
+  __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x1450
-  __DATA_DIRTY.__bss: 0xc8
+  __DATA_DIRTY.__bss: 0xd8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3089
-  Symbols:   3850
-  CStrings:  4173
+  Functions: 3036
+  Symbols:   3789
+  CStrings:  4098
 
Symbols:
+ _FIActivityAnalyticsSubmissionWithPayload
+ _OBJC_CLASS_$_ACHDMetricsReporter
+ _OBJC_METACLASS_$_ACHDMetricsReporter
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _ACHLogMetrics
- _FIActivityAnalyticsSubmission
- _OBJC_CLASS_$_ACHAWDSubmissionManager
- _OBJC_CLASS_$_AWDServerConnection
- _OBJC_CLASS_$_PBCodable
- _OBJC_METACLASS_$_ACHAWDSubmissionManager
- _OBJC_METACLASS_$_PBCodable
- _PBDataWriterWriteBOOLField
- _PBDataWriterWriteInt32Field
- _PBDataWriterWriteUint64Field
- _PBReaderSkipValueWithTag
- _XPC_ACTIVITY_INTERVAL_7_DAYS
CStrings:
+ "@\"NSNumber\"56@0:8@\"NSArray\"16Q24@\"NSDate\"32@\"HDProfile\"40^@48"
+ "ACHDMetricsReporter"
+ "Logging historical processing metric event %@ for source %ld"
+ "com.apple.ActivityAchievements.ActivityAchievements.HistoricalRunProcessingError"
+ "com.apple.ActivityAchievements.HistoricalRunProcessingComplete"
+ "errorString"
+ "errorType"
+ "historicalPeriodType"
+ "pruneSyncedObjectsWithRestrictionPredicates:limit:nowDate:profile:error:"
+ "recordsProcessed"
+ "reportProcessingMetricsWithSourceType:intervalProcessed:processingDuration:recordsProcessed:error:"
+ "v56@0:8q16@24d32Q40@48"
- "%@ %@"
- "(unknown: %i)"
- "(unknown: %u)"
- ".achievementCountEvent"
- ".companionFriendChangeEvent"
- ".companionInvitationEvent"
- ".companionShareEvent"
- ".companionTabVisitEvent"
- ".fitnessDailyEvent"
- ".sharingSnapshotEvent"
- "@20@0:8I16"
- "ACHAWDSubmissionManager"
- "HDActivityAWDActivityAchievementCountEvent"
- "LessThan_2"
- "Metric %08x submission failed"
- "Metric %08x submitted"
- "MoreThan_10"
- "No metric container for achievement count"
- "Range_2_5"
- "Range_6_10"
- "StringAsTotalAchievementCount:"
- "StringAsTotalOTAAchievementCount:"
- "StringAsTotalOTAAchievementViewedCount:"
- "T@\"NSMutableDictionary\",&,N,V_serverConnectionsByComponentId"
- "TB,N"
- "TB,N,V_moreThanOneYearSinceActivitySetup"
- "TQ,N,V_timestamp"
- "Ti,N,V_totalAchievementCount"
- "Ti,N,V_totalOTAAchievementCount"
- "Ti,N,V_totalOTAAchievementViewedCount"
- "_computeAndSubmitAchievementCountMetric"
- "_formatMetricTypeToString:"
- "_has"
- "_moreThanOneYearSinceActivitySetup"
- "_serverConnectionForComponentId:"
- "_serverConnectionsByComponentId"
- "_submitMetric:container:connection:"
- "_timestamp"
- "_totalAchievementCount"
- "_totalOTAAchievementCount"
- "_totalOTAAchievementViewedCount"
- "com.apple.healthd.analytics-submission-manager.weekly"
- "com.apple.healthd.awd-submission-manager.weekly"
- "copyTo:"
- "formattedText"
- "hasMoreThanOneYearSinceActivitySetup"
- "hasTimestamp"
- "hasTotalAchievementCount"
- "hasTotalOTAAchievementCount"
- "hasTotalOTAAchievementViewedCount"
- "i24@0:8@16"
- "initWithComponentId:"
- "initWithProfile:earnedInstanceStore:"
- "isAppleInternalInstall"
- "mergeFrom:"
- "metricId"
- "moreThanOneYearSinceActivitySetup"
- "newMetricContainerWithIdentifier:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedLongLong:"
- "readFrom:"
- "serverConnectionsByComponentId"
- "setHasMoreThanOneYearSinceActivitySetup:"
- "setHasTimestamp:"
- "setHasTotalAchievementCount:"
- "setHasTotalOTAAchievementCount:"
- "setHasTotalOTAAchievementViewedCount:"
- "setMetric:"
- "setMoreThanOneYearSinceActivitySetup:"
- "setServerConnectionsByComponentId:"
- "setTimestamp:"
- "setTotalAchievementCount:"
- "setTotalOTAAchievementCount:"
- "setTotalOTAAchievementViewedCount:"
- "submitMetric:"
- "timestamp"
- "totalAchievementCount"
- "totalAchievementCountAsString:"
- "totalOTAAchievementCount"
- "totalOTAAchievementCountAsString:"
- "totalOTAAchievementViewedCount"
- "totalOTAAchievementViewedCountAsString:"
- "writeTo:"
- "{?=\"timestamp\"b1\"totalAchievementCount\"b1\"totalOTAAchievementCount\"b1\"totalOTAAchievementViewedCount\"b1\"moreThanOneYearSinceActivitySetup\"b1}"

```
