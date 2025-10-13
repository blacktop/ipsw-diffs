## ActivitySharingDaemonCore

> `/System/Library/PrivateFrameworks/ActivitySharingDaemonCore.framework/ActivitySharingDaemonCore`

```diff

-2026.1.2.0.0
-  __TEXT.__text: 0x7d8c8
+2026.1.4.0.0
+  __TEXT.__text: 0x7ddb8
   __TEXT.__auth_stubs: 0xee0
-  __TEXT.__objc_methlist: 0x45b4
+  __TEXT.__objc_methlist: 0x45c4
   __TEXT.__const: 0x1d8
   __TEXT.__cstring: 0x2ffc
-  __TEXT.__gcc_except_tab: 0xfec
-  __TEXT.__oslogstring: 0xe96d
-  __TEXT.__unwind_info: 0x1bd8
+  __TEXT.__gcc_except_tab: 0x1004
+  __TEXT.__oslogstring: 0xea47
+  __TEXT.__unwind_info: 0x1be0
   __TEXT.__objc_classname: 0x9fd
-  __TEXT.__objc_methname: 0x1144f
-  __TEXT.__objc_methtype: 0x2a59
-  __TEXT.__objc_stubs: 0xc6e0
-  __DATA_CONST.__got: 0xa30
-  __DATA_CONST.__const: 0x3b60
+  __TEXT.__objc_methname: 0x114c6
+  __TEXT.__objc_methtype: 0x2aa5
+  __TEXT.__objc_stubs: 0xc700
+  __DATA_CONST.__got: 0xa38
+  __DATA_CONST.__const: 0x3b88
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x37f8
+  __DATA_CONST.__objc_selrefs: 0x3808
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__auth_got: 0x780
   __AUTH_CONST.__const: 0xdc0
   __AUTH_CONST.__cfstring: 0x1e40
-  __AUTH_CONST.__objc_const: 0xdcd8
+  __AUTH_CONST.__objc_const: 0xdd00
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x5d8
+  __DATA.__objc_ivar: 0x5dc
   __DATA.__data: 0xd20
   __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_data: 0xc30

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BA81C56E-8C27-3E2F-8DEA-BF0F6CE22A89
-  Functions: 2364
-  Symbols:   8814
-  CStrings:  4214
+  UUID: D436078D-E553-3D92-838E-C7D49159182F
+  Functions: 2366
+  Symbols:   8822
+  CStrings:  4222
 
Symbols:
+ -[ASDatabaseClient _observerQueue_handleYesterdayActivitySummaryUpdate]
+ -[ASDatabaseClient addActivitySummaryObserver:]
+ -[ASDatabaseClient removeActivitySummaryObserver:]
+ GCC_except_table10
+ GCC_except_table103
+ GCC_except_table107
+ GCC_except_table18
+ GCC_except_table47
+ GCC_except_table66
+ GCC_except_table71
+ GCC_except_table75
+ GCC_except_table79
+ GCC_except_table83
+ GCC_except_table90
+ GCC_except_table95
+ GCC_except_table99
+ _OBJC_IVAR_$_ASDatabaseClient._activitySummaryObservers
+ _OBJC_IVAR_$_ASDatabaseClient._yesterdaySummaryDidUpdateToken
+ ___40-[ASDatabaseClient initWithHealthStore:]_block_invoke_2
+ ___43-[ASDatabaseClient performWhenDaemonReady:]_block_invoke.317
+ ___47-[ASDatabaseClient addActivitySummaryObserver:]_block_invoke
+ ___50-[ASDatabaseClient addSampleObserver:sampleTypes:]_block_invoke.346
+ ___50-[ASDatabaseClient removeActivitySummaryObserver:]_block_invoke
+ ___69-[ASDatabaseClient performWhenDataProtectedByFirstUnlockIsAvailable:]_block_invoke.320
+ ___70-[ASDatabaseClient allCodableDatabaseCompetitionListEntriesWithError:]_block_invoke.359
+ ___93-[ASDatabaseClient deletedHealthKitWorkoutsWithinLastNumberOfDays:maxBatchSize:anchor:error:]_block_invoke.333
+ ___block_descriptor_48_e8_32s40w_e8_v12?0i8ls32l8w40l8
+ ___block_literal_global.363
+ _kASActivitySharingYesterdaySummaryDidUpdateNotification
+ _objc_msgSend$_observerQueue_handleYesterdayActivitySummaryUpdate
+ _objc_msgSend$addActivitySummaryObserver:
+ _objc_msgSend$removeActivitySummaryObserver:
- -[ASDatabaseClient addCurrentActivitySummaryObserver:]
- -[ASDatabaseClient removeCurrentActivitySummaryObserver:]
- GCC_except_table101
- GCC_except_table105
- GCC_except_table17
- GCC_except_table28
- GCC_except_table34
- GCC_except_table58
- GCC_except_table64
- GCC_except_table69
- GCC_except_table73
- GCC_except_table77
- GCC_except_table81
- GCC_except_table88
- GCC_except_table9
- GCC_except_table93
- GCC_except_table97
- _OBJC_IVAR_$_ASDatabaseClient._currentActivitySummaryObservers
- ___43-[ASDatabaseClient performWhenDaemonReady:]_block_invoke.316
- ___50-[ASDatabaseClient addSampleObserver:sampleTypes:]_block_invoke.344
- ___54-[ASDatabaseClient addCurrentActivitySummaryObserver:]_block_invoke
- ___57-[ASDatabaseClient removeCurrentActivitySummaryObserver:]_block_invoke
- ___69-[ASDatabaseClient performWhenDataProtectedByFirstUnlockIsAvailable:]_block_invoke.319
- ___70-[ASDatabaseClient allCodableDatabaseCompetitionListEntriesWithError:]_block_invoke.358
- ___93-[ASDatabaseClient deletedHealthKitWorkoutsWithinLastNumberOfDays:maxBatchSize:anchor:error:]_block_invoke.332
- _objc_msgSend$addCurrentActivitySummaryObserver:
- _objc_msgSend$removeCurrentActivitySummaryObserver:
Functions:
~ -[ASDatabaseClient initWithHealthStore:] : 596 -> 760
+ ___40-[ASDatabaseClient initWithHealthStore:]_block_invoke_2
~ -[ASDatabaseClient dealloc] : 288 -> 308
+ -[ASDatabaseClient _observerQueue_handleYesterdayActivitySummaryUpdate]
~ -[ASDaemonWakeCoordinator initWithProfile:] : 644 -> 756
~ -[ASDaemonWakeCoordinator dealloc] : 244 -> 308
~ -[ASDaemonWakeCoordinator currentActivitySummaryHelper:didUpdateTodayActivitySummary:changedFields:] : 192 -> 308
~ -[ASDaemonWakeCoordinator currentActivitySummaryHelper:didUpdateYesterdayActivitySummary:changedFields:] : 192 -> 328
CStrings:
+ "%{public}@ Notifying observers of yesterday summary update: %@"
+ "%{public}@ Received yesterday summary updated notification"
+ "ASDaemonWakeCoordinator today summary changed"
+ "ASDaemonWakeCoordinator yesterday summary changed"
+ "_activitySummaryObservers"
+ "_observerQueue_handleYesterdayActivitySummaryUpdate"
+ "_yesterdaySummaryDidUpdateToken"
+ "addActivitySummaryObserver:"
+ "removeActivitySummaryObserver:"
+ "service:account:inviteDroppedForSessionID:fromID:error:"
+ "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSError\"48"
- "_currentActivitySummaryObservers"
- "addCurrentActivitySummaryObserver:"
- "removeCurrentActivitySummaryObserver:"

```
