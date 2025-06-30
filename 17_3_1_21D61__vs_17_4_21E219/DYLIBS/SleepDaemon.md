## SleepDaemon

> `/System/Library/PrivateFrameworks/SleepDaemon.framework/SleepDaemon`

```diff

-4146.3.2.0.0
-  __TEXT.__text: 0x799a0
+4146.4.18.0.0
+  __TEXT.__text: 0x79ce4
   __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_methlist: 0x7854
+  __TEXT.__objc_methlist: 0x787c
   __TEXT.__const: 0x190
-  __TEXT.__cstring: 0x2b8a
+  __TEXT.__cstring: 0x2bc0
   __TEXT.__oslogstring: 0xb292
-  __TEXT.__gcc_except_tab: 0xb74
-  __TEXT.__unwind_info: 0x2294
+  __TEXT.__gcc_except_tab: 0xb1c
+  __TEXT.__unwind_info: 0x2288
   __TEXT.__objc_classname: 0x2137
-  __TEXT.__objc_methname: 0x10f36
-  __TEXT.__objc_methtype: 0x363f
-  __TEXT.__objc_stubs: 0xca00
+  __TEXT.__objc_methname: 0x10f82
+  __TEXT.__objc_methtype: 0x3613
+  __TEXT.__objc_stubs: 0xca20
   __DATA_CONST.__got: 0x400
-  __DATA_CONST.__const: 0x22b8
+  __DATA_CONST.__const: 0x2290
   __DATA_CONST.__objc_classlist: 0x588
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x328
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xf310
-  __DATA_CONST.__objc_selrefs: 0x3810
-  __AUTH_CONST.__cfstring: 0x2000
+  __DATA_CONST.__objc_const: 0xf318
+  __DATA_CONST.__objc_selrefs: 0x3820
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x890
+  __DATA_CONST.__objc_superrefs: 0x388
+  __AUTH_CONST.__cfstring: 0x2060
   __AUTH_CONST.__objc_const: 0x3e70
   __AUTH_CONST.__const: 0xcc0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__auth_got: 0x5b8
   __AUTH.__objc_data: 0xfa0
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x890
-  __DATA.__objc_superrefs: 0x388
   __DATA.__objc_ivar: 0x590
   __DATA.__data: 0x25f0
   __DATA_DIRTY.__objc_ivar: 0xec

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BFEC54CA-5C37-3B67-8DFC-706716FD548F
-  Functions: 3066
-  Symbols:   10779
-  CStrings:  4747
+  UUID: C39077C4-996C-3B94-9092-90C535942DCE
+  Functions: 3069
+  Symbols:   10784
+  CStrings:  4756
 
Symbols:
+ -[HDSPCFUserNotificationCenter publishNotificationForEvent:]
+ -[HDSPDarwinNotificationCenter publishNotificationForEvent:]
+ -[HDSPIDSServiceManager eventIdentifiers]
+ -[HDSPIDSServiceManager sleepEventIsDue:]
+ -[HDSPSleepEventScheduler notifyForOverdueEvents:]
+ -[HDSPSleepNotificationManager publishNotificationForEvent:]
+ -[HDSPUserNotificationCenter _notificationRequestForEvent:]
+ -[HDSPUserNotificationCenter publishNotificationForEvent:]
+ __OBJC_$_PROP_LIST_HDSPSleepLockScreenAssertionManager.123
+ ___39-[_HDSPBiomeBridge subscribe:callback:]_block_invoke.114
+ ___49-[HDSPSleepEventScheduler _schedulePendingEvents]_block_invoke.83
+ ___49-[HDSPSleepStoreServer processNoLongerSuspended:]_block_invoke.266
+ ___49-[HDSPSleepStoreServer processNoLongerSuspended:]_block_invoke_2.267
+ ___50-[HDSPSleepEventScheduler notifyForOverdueEvents:]_block_invoke
+ ___50-[HDSPSleepEventScheduler notifyForOverdueEvents:]_block_invoke.91
+ ___50-[HDSPSleepEventScheduler notifyForOverdueEvents:]_block_invoke_2
+ ___54-[HKSleepHealthStore(HDSPSleep) hdsp_persistSessions:]_block_invoke.245
+ ___55-[HDSPAnalyticsManager scheduleDailyCollectionActivity]_block_invoke.249
+ ___56-[HDSPSleepEventScheduler eventProviderCancelledEvents:]_block_invoke.96
+ ___56-[HDSPSleepStoreServer _performWhenClientIsReady:block:]_block_invoke.251
+ ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.270
+ ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.272
+ ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.275
+ ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke_2.276
+ ___57-[HDSPTimeInBedTracker computeSleepIntervalsForInterval:]_block_invoke.247
+ ___57-[HDSPTimeInBedTracker computeSleepIntervalsForInterval:]_block_invoke.249
+ ___58-[HDSPSleepEventScheduler eventProviderHasUpcomingEvents:]_block_invoke.95
+ ___60-[HDSPSleepNotificationManager publishNotificationForEvent:]_block_invoke
+ ___60-[HDSPWakeUpResultsNotificationManager scheduleRetryAttempt]_block_invoke.258
+ ___71-[HDSPSleepStoreServer publishWakeUpResultsNotificationWithCompletion:]_block_invoke.256
+ ___73-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepSchedule:]_block_invoke.259
+ ___73-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepSettings:]_block_invoke.261
+ ___76-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepEventRecord:]_block_invoke.262
+ ___block_descriptor_48_e8_32s40s_e43_"NAFuture"16?0"<HDSPSleepEventHandler>"8ls32l8s40l8
+ _objc_msgSend$_notificationRequestForEvent:
+ _objc_msgSend$context
+ _objc_msgSend$notifyForOverdueEvents:
+ _objc_msgSend$publishNotificationForEvent:
+ _objc_msgSend$sleepEventWithIdentifier:dueDate:context:
- -[HDSPCFUserNotificationCenter publishNotificationForEvent:userInfo:]
- -[HDSPDarwinNotificationCenter publishNotificationForEvent:userInfo:]
- -[HDSPSleepNotificationManager publishNotificationForEvent:userInfo:]
- -[HDSPUserNotificationCenter _notificationRequestForEvent:userInfo:]
- -[HDSPUserNotificationCenter publishNotificationForEvent:userInfo:]
- __OBJC_$_PROP_LIST_HDSPSleepLockScreenAssertionManager.122
- ___39-[_HDSPBiomeBridge subscribe:callback:]_block_invoke.113
- ___47-[HDSPSleepEventScheduler _handleOverdueEvents]_block_invoke.87
- ___47-[HDSPSleepEventScheduler _handleOverdueEvents]_block_invoke.92
- ___47-[HDSPSleepEventScheduler _handleOverdueEvents]_block_invoke_2.88
- ___49-[HDSPSleepEventScheduler _schedulePendingEvents]_block_invoke.82
- ___49-[HDSPSleepStoreServer processNoLongerSuspended:]_block_invoke.241
- ___49-[HDSPSleepStoreServer processNoLongerSuspended:]_block_invoke_2.242
- ___54-[HKSleepHealthStore(HDSPSleep) hdsp_persistSessions:]_block_invoke.221
- ___55-[HDSPAnalyticsManager scheduleDailyCollectionActivity]_block_invoke.225
- ___56-[HDSPSleepEventScheduler eventProviderCancelledEvents:]_block_invoke.97
- ___56-[HDSPSleepStoreServer _performWhenClientIsReady:block:]_block_invoke.227
- ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.246
- ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.248
- ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.251
- ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke_2.252
- ___57-[HDSPTimeInBedTracker computeSleepIntervalsForInterval:]_block_invoke.223
- ___57-[HDSPTimeInBedTracker computeSleepIntervalsForInterval:]_block_invoke.225
- ___58-[HDSPSleepEventScheduler eventProviderHasUpcomingEvents:]_block_invoke.96
- ___60-[HDSPWakeUpResultsNotificationManager scheduleRetryAttempt]_block_invoke.234
- ___69-[HDSPSleepNotificationManager publishNotificationForEvent:userInfo:]_block_invoke
- ___71-[HDSPSleepStoreServer publishWakeUpResultsNotificationWithCompletion:]_block_invoke.231
- ___73-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepSchedule:]_block_invoke.234
- ___73-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepSettings:]_block_invoke.236
- ___76-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepEventRecord:]_block_invoke.237
- ___block_descriptor_48_e8_32s40r_e43_"NAFuture"16?0"<HDSPSleepEventHandler>"8lr40l8s32l8
- ___block_descriptor_48_e8_32s40s_e42_v16?0"<HDSPSleepNotificationPublisher>"8ls32l8s40l8
- _objc_msgSend$_notificationRequestForEvent:userInfo:
- _objc_msgSend$idsServiceManager
- _objc_msgSend$notificationManager
- _objc_msgSend$publishNotificationForEvent:userInfo:
CStrings:
+ "HDSPIDSServiceManager.m"
+ "T@\"<NAScheduler>\",?,R,N"
+ "T@\"NSString\",?,R,C"
+ "TB,?,R,N"
+ "Unexpected event received"
+ "_notificationRequestForEvent:"
+ "nil"
+ "notifyForOverdueEvents:"
+ "publishNotificationForEvent:"
+ "sleepEventWithIdentifier:dueDate:context:"
- "T@\"<NAScheduler>\",R,N"
- "_notificationRequestForEvent:userInfo:"
- "publishNotificationForEvent:userInfo:"
- "v32@0:8@\"HKSPSleepEvent\"16@\"NSDictionary\"24"

```
