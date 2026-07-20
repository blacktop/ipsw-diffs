## HeartHealthDaemon

> `/System/Library/PrivateFrameworks/HeartHealthDaemon.framework/HeartHealthDaemon`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-7027.0.64.0.0
-  __TEXT.__text: 0x64174
-  __TEXT.__objc_methlist: 0x4ecc
+7027.0.67.2.1
+  __TEXT.__text: 0x64dd4
+  __TEXT.__objc_methlist: 0x4f24
   __TEXT.__const: 0x34a
   __TEXT.__gcc_except_tab: 0xadc
-  __TEXT.__cstring: 0x55d2
-  __TEXT.__oslogstring: 0xc175
+  __TEXT.__cstring: 0x57d2
+  __TEXT.__oslogstring: 0xc32f
   __TEXT.__ustring: 0x86
   __TEXT.__swift5_typeref: 0x47
   __TEXT.__swift5_capture: 0x30

   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1678
+  __TEXT.__unwind_info: 0x1688
   __TEXT.__eh_frame: 0x78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3520
+  __DATA_CONST.__objc_selrefs: 0x35c0
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x510
-  __DATA_CONST.__got: 0xeb8
+  __DATA_CONST.__got: 0xec0
   __AUTH_CONST.__const: 0x620
-  __AUTH_CONST.__cfstring: 0x4600
-  __AUTH_CONST.__objc_const: 0x99a0
+  __AUTH_CONST.__cfstring: 0x4760
+  __AUTH_CONST.__objc_const: 0x9a00
   __AUTH_CONST.__objc_intobj: 0xdb0
   __AUTH_CONST.__objc_doubleobj: 0x3d0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__auth_got: 0x890
   __AUTH.__objc_data: 0x868
-  __DATA.__objc_ivar: 0x62c
+  __DATA.__objc_ivar: 0x634
   __DATA.__data: 0x1d60
   __DATA.__bss: 0x1c0
   __DATA_DIRTY.__objc_data: 0x1640

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2062
-  Symbols:   5467
-  CStrings:  1320
+  Functions: 2077
+  Symbols:   5498
+  CStrings:  1338
 
Symbols:
+ -[HDHRAFibBurdenNotificationModeDeterminer breadcrumbManager]
+ -[HDHRAFibBurdenNotificationModeDeterminer setBreadcrumbManager:]
+ -[HDHRAFibBurdenSevenDayAnalysisBreadcrumbManager _currentRunSnapshotWithError:]
+ -[HDHRAFibBurdenSevenDayAnalysisBreadcrumbManager _loadRunHistoryWithError:]
+ -[HDHRAFibBurdenSevenDayAnalysisBreadcrumbManager _queue_rollCurrentRunIntoHistoryAndStartNewRunWithAlarmFiredDate:]
+ -[HDHRAFibBurdenSevenDayAnalysisBreadcrumbManager _queue_saveRunHistory:]
+ -[HDHRAFibBurdenSevenDayAnalysisBreadcrumbManager dropNotificationDecisionBreadcrumb:]
+ -[HDHRAFibBurdenSevenDayAnalysisBreadcrumbManager initWithLocalKeyValueDomain:syncedKeyValueDomain:dateGenerator:queue:]
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_IVAR_$_HDHRAFibBurdenNotificationModeDeterminer._breadcrumbManager
+ _OBJC_IVAR_$_HDHRAFibBurdenSevenDayAnalysisBreadcrumbManager._localKeyValueDomain
+ _OBJC_IVAR_$_HDHRAFibBurdenSevenDayAnalysisBreadcrumbManager._syncedKeyValueDomain
+ __OBJC_$_PROP_LIST_HDHRAFibBurdenNotificationModeDeterminer
+ ___86-[HDHRAFibBurdenSevenDayAnalysisBreadcrumbManager dropNotificationDecisionBreadcrumb:]_block_invoke
+ _objc_msgSend$_currentRunSnapshotWithError:
+ _objc_msgSend$_loadRunHistoryWithError:
+ _objc_msgSend$_queue_rollCurrentRunIntoHistoryAndStartNewRunWithAlarmFiredDate:
+ _objc_msgSend$_queue_saveRunHistory:
+ _objc_msgSend$alarmFiredDate
+ _objc_msgSend$analysisEndedDate
+ _objc_msgSend$analysisRetryLaterRequestedDate
+ _objc_msgSend$analysisStartedDate
+ _objc_msgSend$dropNotificationDecisionBreadcrumb:
+ _objc_msgSend$initWithAlarmFiredDate:xpcActivityFiredDate:protectedDataOperationRunDate:analysisStartedDate:tachogramsClassifiedDate:analysisEndedDate:analysisRetryLaterRequestedDate:lastAnalysisResultDate:lastAnalysisResultContext:lastNotificationDecision:lastNotificationSentDate:lastAnalysisCompletedDate:runHistory:
+ _objc_msgSend$initWithLocalKeyValueDomain:syncedKeyValueDomain:dateGenerator:queue:
+ _objc_msgSend$lastAnalysisResultContext
+ _objc_msgSend$lastAnalysisResultDate
+ _objc_msgSend$lastNotificationDecision
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$protectedDataOperationRunDate
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$setBreadcrumbManager:
+ _objc_msgSend$tachogramsClassifiedDate
+ _objc_msgSend$unarchivedObjectOfClasses:fromData:error:
+ _objc_msgSend$xpcActivityFiredDate
- -[HDHRAFibBurdenSevenDayAnalysisBreadcrumbManager initWithKeyValueDomain:dateGenerator:queue:]
- _OBJC_IVAR_$_HDHRAFibBurdenSevenDayAnalysisBreadcrumbManager._keyValueDomain
- _objc_msgSend$initWithAlarmFiredDate:xpcActivityFiredDate:protectedDataOperationRunDate:analysisStartedDate:tachogramsClassifiedDate:analysisEndedDate:analysisRetryLaterRequestedDate:lastAnalysisResultDate:lastAnalysisResultContext:
- _objc_msgSend$initWithKeyValueDomain:dateGenerator:queue:
CStrings:
+ "Posted: no-data notification (forwarded to watch)"
+ "Posted: no-data notification (phone only)"
+ "Posted: value notification (current and previous week)"
+ "Posted: value notification (current week)"
+ "SevenDayAnalysisBreadcrumbNotificationDecision"
+ "SevenDayAnalysisBreadcrumbRunHistory"
+ "Suppressed: after weekday cutoff"
+ "Suppressed: analysis requirements not satisfied"
+ "Suppressed: most recent sample not for previous calendar week"
+ "Suppressed: onboarded within analysis interval"
+ "Suppressed: weekly notifications disabled"
+ "[%{public}@] Error archiving run history: %{public}@"
+ "[%{public}@] Error loading run history to append, starting fresh: %{public}@"
+ "[%{public}@] Error resetting prior run breadcrumbs: %{public}@"
+ "[%{public}@] Error saving run history: %{public}@"
+ "[%{public}@] Error snapshotting run for history: %{public}@"
+ "[%{public}@] Error unarchiving run history, treating as empty: %{public}@"
+ "[%{public}@] Error when saving notification decision: %{public}@"
```
