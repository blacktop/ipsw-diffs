## ActivitySharingDaemonCore

> `/System/Library/PrivateFrameworks/ActivitySharingDaemonCore.framework/ActivitySharingDaemonCore`

```diff

-2026.3.1.0.0
-  __TEXT.__text: 0x7ddb8
+2026.3.2.0.0
+  __TEXT.__text: 0x7ddc0
   __TEXT.__auth_stubs: 0xee0
   __TEXT.__objc_methlist: 0x45d4
   __TEXT.__const: 0x1d8

   __TEXT.__oslogstring: 0xea47
   __TEXT.__unwind_info: 0x1be0
   __TEXT.__objc_classname: 0x9fd
-  __TEXT.__objc_methname: 0x1150e
+  __TEXT.__objc_methname: 0x1151b
   __TEXT.__objc_methtype: 0x2b08
   __TEXT.__objc_stubs: 0xc700
   __DATA_CONST.__got: 0xa38

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AED10A81-5003-32CA-843B-B772EDCD2760
+  UUID: 9EE47F30-99A7-3E9D-B706-E501D0CCDFE7
   Functions: 2366
   Symbols:   8822
   CStrings:  4225
Symbols:
+ -[ASActivityDataManager findDeletedWorkoutEventsWithAnchor:maxBatchSize:completion:]
+ -[ASActivityDataManager findDeletedWorkoutEventsWithAnchor:maxBatchSize:completion:].cold.1
+ ___84-[ASActivityDataManager findDeletedWorkoutEventsWithAnchor:maxBatchSize:completion:]_block_invoke
+ ___block_literal_global.668
+ ___block_literal_global.671
+ _objc_msgSend$findDeletedWorkoutEventsWithAnchor:maxBatchSize:completion:
- -[ASActivityDataManager findDeletedWorkoutEventsWithAnchor:completion:]
- -[ASActivityDataManager findDeletedWorkoutEventsWithAnchor:completion:].cold.1
- ___71-[ASActivityDataManager findDeletedWorkoutEventsWithAnchor:completion:]_block_invoke
- ___block_literal_global.667
- ___block_literal_global.670
- _objc_msgSend$findDeletedWorkoutEventsWithAnchor:completion:
Functions:
~ -[ASActivityDataManager notificationEventsToPushWithYesterdaySnapshot:todaySnapshot:achievements:workouts:currentDeletedWorkoutAnchor:currentGoalCompletionAnchor:] : 964 -> 968
~ -[ASActivityDataManager findDeletedWorkoutEventsWithAnchor:completion:] -> -[ASActivityDataManager findDeletedWorkoutEventsWithAnchor:maxBatchSize:completion:] : 468 -> 472
CStrings:
+ "findDeletedWorkoutEventsWithAnchor:maxBatchSize:completion:"
- "findDeletedWorkoutEventsWithAnchor:completion:"

```
