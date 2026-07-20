## HeartHealth

> `/System/Library/PrivateFrameworks/HeartHealth.framework/HeartHealth`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-7027.0.64.0.0
-  __TEXT.__text: 0x266f4
-  __TEXT.__objc_methlist: 0x2f7c
-  __TEXT.__const: 0x272
+7027.0.67.2.1
+  __TEXT.__text: 0x26f08
+  __TEXT.__objc_methlist: 0x2fec
+  __TEXT.__const: 0x2f8
   __TEXT.__oslogstring: 0x17d4
-  __TEXT.__cstring: 0x34ee
+  __TEXT.__cstring: 0x361a
   __TEXT.__gcc_except_tab: 0x190
-  __TEXT.__swift5_typeref: 0x23
+  __TEXT.__constg_swiftt: 0x90
+  __TEXT.__swift5_typeref: 0x29
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_types: 0xc
   __TEXT.__swift5_reflstr: 0x57
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__constg_swiftt: 0x64
   __TEXT.__swift5_fieldmd: 0x74
-  __TEXT.__swift5_proto: 0xc
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xbd8
+  __TEXT.__swift5_proto: 0x14
+  __TEXT.__unwind_info: 0xbe0
   __TEXT.__eh_frame: 0x70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ba8
+  __DATA_CONST.__objc_selrefs: 0x1be8
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x28
-  __DATA_CONST.__got: 0x5c8
-  __AUTH_CONST.__const: 0x370
-  __AUTH_CONST.__cfstring: 0x2bc0
-  __AUTH_CONST.__objc_const: 0x5da8
+  __DATA_CONST.__got: 0x5f0
+  __AUTH_CONST.__const: 0x390
+  __AUTH_CONST.__cfstring: 0x2ce0
+  __AUTH_CONST.__objc_const: 0x5e68
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x4e8
   __AUTH.__objc_data: 0xf00
   __AUTH.__data: 0xa8
-  __DATA.__objc_ivar: 0x304
-  __DATA.__data: 0x920
-  __DATA.__bss: 0x1c0
+  __DATA.__objc_ivar: 0x314
+  __DATA.__data: 0x928
+  __DATA.__bss: 0x2c0
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__bss: 0x38

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1211
-  Symbols:   2959
-  CStrings:  496
+  Functions: 1227
+  Symbols:   2980
+  CStrings:  506
 
Symbols:
+ -[HKHRAFibBurdenSevenDayAnalysisBreadcrumbs initWithAlarmFiredDate:xpcActivityFiredDate:protectedDataOperationRunDate:analysisStartedDate:tachogramsClassifiedDate:analysisEndedDate:analysisRetryLaterRequestedDate:lastAnalysisResultDate:lastAnalysisResultContext:lastNotificationDecision:lastNotificationSentDate:lastAnalysisCompletedDate:runHistory:]
+ -[HKHRAFibBurdenSevenDayAnalysisBreadcrumbs lastAnalysisCompletedDate]
+ -[HKHRAFibBurdenSevenDayAnalysisBreadcrumbs lastNotificationDecision]
+ -[HKHRAFibBurdenSevenDayAnalysisBreadcrumbs lastNotificationSentDate]
+ -[HKHRAFibBurdenSevenDayAnalysisBreadcrumbs runHistory]
+ -[HKHRAFibBurdenSevenDayAnalysisBreadcrumbs setLastAnalysisCompletedDate:]
+ -[HKHRAFibBurdenSevenDayAnalysisBreadcrumbs setLastNotificationDecision:]
+ -[HKHRAFibBurdenSevenDayAnalysisBreadcrumbs setLastNotificationSentDate:]
+ -[HKHRAFibBurdenSevenDayAnalysisBreadcrumbs setRunHistory:]
+ _OBJC_IVAR_$_HKHRAFibBurdenSevenDayAnalysisBreadcrumbs._lastAnalysisCompletedDate
+ _OBJC_IVAR_$_HKHRAFibBurdenSevenDayAnalysisBreadcrumbs._lastNotificationDecision
+ _OBJC_IVAR_$_HKHRAFibBurdenSevenDayAnalysisBreadcrumbs._lastNotificationSentDate
+ _OBJC_IVAR_$_HKHRAFibBurdenSevenDayAnalysisBreadcrumbs._runHistory
+ __appendBreadcrumbTables
+ __dateStringOrNull
+ _objc_msgSend$initWithAlarmFiredDate:xpcActivityFiredDate:protectedDataOperationRunDate:analysisStartedDate:tachogramsClassifiedDate:analysisEndedDate:analysisRetryLaterRequestedDate:lastAnalysisResultDate:lastAnalysisResultContext:lastNotificationDecision:lastNotificationSentDate:lastAnalysisCompletedDate:runHistory:
+ _objc_msgSend$lastAnalysisCompletedDate
+ _objc_msgSend$lastNotificationDecision
+ _objc_msgSend$lastNotificationSentDate
+ _objc_msgSend$runHistory
+ _swift_getForeignTypeMetadata
+ _symbolic _____ So24HKHeartbeatSeriesFeatureV
- _objc_msgSend$isEqualToDate:
CStrings:
+ "\n-------- Run %lu --------\n"
+ "\n======== Previous Runs (oldest first, %lu) ========\n"
+ "\r"
+ "HKHeartbeatSeriesFeature."
+ "Last Analysis Completed Date"
+ "Last Notification Decision"
+ "Last Notification Sent Date"
+ "LastAnalysisCompletedDateKey"
+ "LastNotificationDecisionKey"
+ "LastNotificationSentDateKey"
+ "RunHistoryKey"
- "\t"
```
