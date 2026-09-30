## ActivitySharingDaemonCore

> `/System/Library/PrivateFrameworks/ActivitySharingDaemonCore.framework/ActivitySharingDaemonCore`

```diff

-2026.0.2.0.0
-  __TEXT.__text: 0x7d4dc
+2026.1.1.0.0
+  __TEXT.__text: 0x7d72c
   __TEXT.__auth_stubs: 0xee0
-  __TEXT.__objc_methlist: 0x457c
+  __TEXT.__objc_methlist: 0x45ac
   __TEXT.__const: 0x1d8
-  __TEXT.__cstring: 0x2f1d
+  __TEXT.__cstring: 0x2ffc
   __TEXT.__gcc_except_tab: 0xfec
   __TEXT.__oslogstring: 0xe93b
-  __TEXT.__unwind_info: 0x1bc0
+  __TEXT.__unwind_info: 0x1bd8
   __TEXT.__objc_classname: 0x9fd
-  __TEXT.__objc_methname: 0x113bd
+  __TEXT.__objc_methname: 0x1143d
   __TEXT.__objc_methtype: 0x2a59
-  __TEXT.__objc_stubs: 0xc5c0
+  __TEXT.__objc_stubs: 0xc6c0
   __DATA_CONST.__got: 0xa30
   __DATA_CONST.__const: 0x3b60
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x37b0
+  __DATA_CONST.__objc_selrefs: 0x37f0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__auth_got: 0x780
   __AUTH_CONST.__const: 0xdc0
-  __AUTH_CONST.__cfstring: 0x1de0
+  __AUTH_CONST.__cfstring: 0x1e40
   __AUTH_CONST.__objc_const: 0xdcd8
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0xc0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 970DEBF4-B393-3C35-A429-84206E7B0A14
-  Functions: 2358
-  Symbols:   8791
-  CStrings:  4198
+  UUID: FA13222A-ED03-330D-B903-25FB5F8EE822
+  Functions: 2361
+  Symbols:   8805
+  CStrings:  4212
 
Symbols:
+ -[_HKFitnessFriendAchievement(Filterable) filter_description]
+ -[_HKFitnessFriendActivitySnapshot(Filterable) filter_description]
+ -[_HKFitnessFriendWorkout(Filterable) filter_description]
+ GCC_except_table108
+ GCC_except_table114
+ GCC_except_table116
+ GCC_except_table53
+ GCC_except_table55
+ ___108-[ASActivityDataManager cloudKitManager:didReceiveNewNotificationEvents:moreComing:changesProcessedHandler:]_block_invoke.346
+ ___108-[ASActivityDataManager cloudKitManager:didReceiveNewNotificationEvents:moreComing:changesProcessedHandler:]_block_invoke.348
+ ___72-[ASActivityDataManager _ckQueue_handleDeletedWorkoutEvents:completion:]_block_invoke.393
+ ___97-[ASActivityDataManager _workoutsToPushWithYesterdaySnapshot:todaySnapshot:currentWorkoutAnchor:]_block_invoke.378
+ ___97-[ASActivityDataManager _workoutsToPushWithYesterdaySnapshot:todaySnapshot:currentWorkoutAnchor:]_block_invoke.379
+ ___98-[ASActivityDataManager currentActivitySummaryHelper:didUpdateTodayActivitySummary:changedFields:]_block_invoke.367
+ ___block_literal_global.382
+ ___block_literal_global.386
+ ___block_literal_global.391
+ ___block_literal_global.667
+ ___block_literal_global.670
+ _objc_msgSend$activeHours
+ _objc_msgSend$activeHoursGoal
+ _objc_msgSend$briskMinutes
+ _objc_msgSend$briskMinutesGoal
+ _objc_msgSend$filter_description
+ _objc_msgSend$isWatchWorkout
+ _objc_msgSend$stepCount
+ _objc_msgSend$walkingAndRunningDistance
- GCC_except_table111
- GCC_except_table113
- GCC_except_table132
- GCC_except_table50
- GCC_except_table52
- ___108-[ASActivityDataManager cloudKitManager:didReceiveNewNotificationEvents:moreComing:changesProcessedHandler:]_block_invoke.335
- ___108-[ASActivityDataManager cloudKitManager:didReceiveNewNotificationEvents:moreComing:changesProcessedHandler:]_block_invoke.337
- ___72-[ASActivityDataManager _ckQueue_handleDeletedWorkoutEvents:completion:]_block_invoke.382
- ___97-[ASActivityDataManager _workoutsToPushWithYesterdaySnapshot:todaySnapshot:currentWorkoutAnchor:]_block_invoke.367
- ___97-[ASActivityDataManager _workoutsToPushWithYesterdaySnapshot:todaySnapshot:currentWorkoutAnchor:]_block_invoke.368
- ___98-[ASActivityDataManager currentActivitySummaryHelper:didUpdateTodayActivitySummary:changedFields:]_block_invoke.356
- ___block_literal_global.371
- ___block_literal_global.375
- ___block_literal_global.380
- ___block_literal_global.656
- ___block_literal_global.659
Functions:
~ +[ASActivityDataValidator validatedSamplesFromAchievements:workouts:activitySnapshots:friendListManager:isInvitationData:] : 1704 -> 1700
+ -[_HKFitnessFriendActivitySnapshot(Filterable) filter_description]
+ -[_HKFitnessFriendWorkout(Filterable) filter_description]
+ -[_HKFitnessFriendAchievement(Filterable) filter_description]
~ -[ASActivityDataManager cloudKitManager:didReceiveNewNotificationEvents:moreComing:changesProcessedHandler:] : 364 -> 344
CStrings:
+ "Received new notification events: %@"
+ "_HKFitnessFriendAchievement: %@ friend: %@, completion date: %@, value: %@"
+ "_HKFitnessFriendActivitySnapshot: %lld, %f/%f, %f/%f, %f/%f, %f/%f, %lu, %f"
+ "_HKFitnessFriendWorkout: %@, type: %ld, duration: %f, watch workout: %d"
+ "activeHours"
+ "activeHoursGoal"
+ "briskMinutes"
+ "briskMinutesGoal"
+ "filter_description"
+ "isWatchWorkout"
+ "stepCount"
+ "walkingAndRunningDistance"
- "Recieved %lu new notification events"

```
