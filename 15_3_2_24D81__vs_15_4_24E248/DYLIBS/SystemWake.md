## SystemWake

> `/System/Library/PrivateFrameworks/SystemWake.framework/Versions/A/SystemWake`

```diff

-694.3.4.0.0
-  __TEXT.__text: 0xc9b4
+694.5.5.0.0
+  __TEXT.__text: 0xc874
   __TEXT.__auth_stubs: 0x3e0
-  __TEXT.__objc_methlist: 0x5d0
+  __TEXT.__objc_methlist: 0x8ac
   __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0x1314
+  __TEXT.__gcc_except_tab: 0x12f0
   __TEXT.__cstring: 0xad1
   __TEXT.__oslogstring: 0x15a4
-  __TEXT.__unwind_info: 0x590
+  __TEXT.__unwind_info: 0x578
   __TEXT.__objc_classname: 0x2ab
   __TEXT.__objc_methname: 0x149c
   __TEXT.__objc_methtype: 0x5e5

   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a8
+  __DATA_CONST.__objc_selrefs: 0x440
   __DATA_CONST.__objc_superrefs: 0x50
   __AUTH_CONST.__auth_got: 0x200
   __AUTH_CONST.__const: 0x470
   __AUTH_CONST.__cfstring: 0xa60
-  __AUTH_CONST.__objc_const: 0x1e80
+  __AUTH_CONST.__objc_const: 0x1978
   __AUTH.__objc_data: 0x3c0
   __DATA.__objc_ivar: 0x138
   __DATA.__data: 0x4e0

   - /System/Library/PrivateFrameworks/BaseBoard.framework/Versions/A/BaseBoard
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2D9D1D89-E185-37F1-9CE5-50EFE7A26533
-  Functions: 185
-  Symbols:   737
+  UUID: 151C3913-364E-30F1-B0B6-E361D5A0FC81
+  Functions: 183
+  Symbols:   736
   CStrings:  573
 
Symbols:
- GCC_except_table65
Functions:
~ -[SWSystemSleepMonitor initWithIdentifier:queue:allowsInvalidation:monitorProvider:sleepAssertionProvider:activeSystemActivityRegistry:] : 632 -> 628
~ -[SWSystemSleepMonitor description] : 472 -> 468
~ -[SWSystemSleepMonitor hasSleepBeenRequested] : 68 -> 64
~ -[SWSystemSleepMonitor isSleepImminent] : 68 -> 64
~ -[SWSystemSleepMonitor isAwakeOrAbortingSleep] : 68 -> 64
~ -[SWSystemSleepMonitor systemActivityRegistryCountDidIncrementToOne:] : 852 -> 848
~ -[SWSystemSleepMonitor systemActivityRegistryCountDidDecrementToZero:] : 588 -> 564
~ -[SWSystemSleepMonitor aggregateState] : 100 -> 96
~ -[SWSystemSleepMonitor setSleepSlate:powerManagementPhase:notificationID:] : 1872 -> 1868
~ -[SWSystemSleepMonitor setSleepSlate:forPowerManagementNotificationID:notificationTimestamp:] : 980 -> 908
~ -[SWSystemSleepMonitor systemPowerChanged:notificationID:] : 1608 -> 1612
- sub_250809df4
~ -[SWSystemSleepMonitor observersOfSelector:performObserverBlock:completion:] : 1312 -> 1292
~ -[SWSystemSleepMonitor observersRespondingToSelector:] : 284 -> 280
~ ___76-[SWSystemSleepMonitor observersOfSelector:performObserverBlock:completion:]_block_invoke_2 : 736 -> 740
~ -[SWSystemSleepMonitorProvider registerForSystemPowerOnQueue:withDelegate:] : 1136 -> 1140
~ -[SWSystemSleepMonitorProvider invalidate] : 468 -> 464
~ -[SWSystemSleepMonitorProvider allowPowerChange:] : 488 -> 492
~ -[SWSystemSleepMonitorProvider cancelPowerChange:] : 488 -> 492
~ ___62-[SWSystemSleepMonitorAggregateState descriptionForTimestamp:]_block_invoke : 252 -> 240
~ -[SWActiveSystemActivityRegistry description] : 400 -> 396
~ -[SWActiveSystemActivityRegistry registerActiveSystemActivity:] : 228 -> 224
~ -[SWActiveSystemActivityRegistry notifyObserversWithBlock:] : 396 -> 392
~ -[SWActiveSystemActivityRegistry unregisterInactiveSystemActivity:] : 228 -> 224
~ -[SWSystemActivityAssertion isActive] : 68 -> 64
~ ___56-[SWSystemActivityAssertion acquireWithTimeout:handler:]_block_invoke : 3644 -> 3656
~ -[SWSystemActivityAssertion callbackAcquisitionHandlerWithError:] : 472 -> 460
~ -[SWSystemActivityAssertion invalidate] : 84 -> 80
~ -[SWSystemActivityAssertion invalidateWithReason:] : 1684 -> 1660
~ -[SWSystemActivityAssertion setAcquireWaitsToAbortSleepRequested:] : 484 -> 488
~ -[SWSystemActivityAssertion setAcquireWaitsToAbortSleepImminent:] : 484 -> 488
~ -[SWSystemActivityAssertion setSleepMonitor:] : 568 -> 572
~ -[SWSystemActivityAssertion setSystemActivityProvider:] : 540 -> 544
~ -[SWSystemActivityAssertion _checkIfCompleteForAction:] : 660 -> 656
~ -[SWWakingTimer dealloc] : 604 -> 608
~ -[SWWakingTimer isScheduled] : 80 -> 76
~ -[SWWakingTimer timeRemaining] : 92 -> 88
~ -[SWWakingTimer scheduleWithFireInterval:leewayInterval:queue:handler:] : 1624 -> 1632
~ -[SWWakingTimer _timerFired:] : 432 -> 420
~ -[SWWakingTimer _updateScheduledWakeAndCheckCanSleep] : 720 -> 716
~ -[SWWakingTimer scheduleForDate:leewayInterval:queue:handler:] : 1308 -> 1312
~ -[SWWakingTimer cancel] : 72 -> 68
~ -[SWWakingTimer invalidate] : 112 -> 108
~ -[SWWakingTimer _setPreventSleepAssertion:] : 304 -> 300
~ -[SWScheduledSystemWake isScheduled] : 68 -> 64
~ -[SWScheduledSystemWake wakeTime] : 88 -> 84
~ -[SWScheduledSystemWake leeway] : 80 -> 76
~ -[SWScheduledSystemWake scheduleWake:leeway:] : 876 -> 880
~ -[SWScheduledSystemWake cancelWake] : 248 -> 236
~ -[SWScheduledSystemWake invalidate] : 80 -> 76
~ -[SWPreventSystemSleepAssertion acquireWithTimeout:handler:] : 672 -> 668
~ ___60-[SWPreventSystemSleepAssertion acquireWithTimeout:handler:]_block_invoke : 944 -> 940
~ -[SWPreventSystemSleepAssertion isActive] : 112 -> 108
~ -[SWPreventSystemSleepAssertion invalidate] : 1200 -> 1184
- sub_250814110

```
