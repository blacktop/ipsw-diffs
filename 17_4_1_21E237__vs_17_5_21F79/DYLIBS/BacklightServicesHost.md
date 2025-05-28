## BacklightServicesHost

> `/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`

```diff

-3.4.9.0.0
-  __TEXT.__text: 0x77f34
+3.5.7.0.0
+  __TEXT.__text: 0x78708
   __TEXT.__auth_stubs: 0xa40
-  __TEXT.__objc_methlist: 0x548c
-  __TEXT.__const: 0x228
-  __TEXT.__oslogstring: 0xdd13
-  __TEXT.__cstring: 0x59da
-  __TEXT.__gcc_except_tab: 0x838
+  __TEXT.__objc_methlist: 0x5494
+  __TEXT.__const: 0x258
+  __TEXT.__oslogstring: 0xdeaf
+  __TEXT.__cstring: 0x5a61
+  __TEXT.__gcc_except_tab: 0x850
   __TEXT.__ustring: 0x1f4
-  __TEXT.__unwind_info: 0x1c80
+  __TEXT.__unwind_info: 0x1c98
   __TEXT.__objc_classname: 0x1c2a
-  __TEXT.__objc_methname: 0xf994
-  __TEXT.__objc_methtype: 0x3f84
-  __TEXT.__objc_stubs: 0x8fc0
+  __TEXT.__objc_methname: 0xfa8a
+  __TEXT.__objc_methtype: 0x3f9d
+  __TEXT.__objc_stubs: 0x9000
   __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0x2020
+  __DATA_CONST.__const: 0x20f8
   __DATA_CONST.__objc_classlist: 0x4a8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xfd88
-  __DATA_CONST.__objc_selrefs: 0x2ac0
+  __DATA_CONST.__objc_const: 0xfe68
+  __DATA_CONST.__objc_selrefs: 0x2ad0
   __DATA_CONST.__objc_classrefs: 0x7d8
   __DATA_CONST.__objc_superrefs: 0x3d8
   __DATA_CONST.__objc_arraydata: 0x78
   __AUTH_CONST.__objc_const: 0x3a08
-  __AUTH_CONST.__cfstring: 0x5860
+  __AUTH_CONST.__cfstring: 0x5920
   __AUTH_CONST.__const: 0x9a0
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28

   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x530
   __AUTH.__objc_data: 0x1360
-  __DATA.__objc_ivar: 0xc2c
+  __DATA.__objc_ivar: 0xc38
   __DATA.__data: 0x1d40
   __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x1b30
-  __DATA_DIRTY.__bss: 0xd8
+  __DATA_DIRTY.__bss: 0xd0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 2907
-  Symbols:   9962
-  CStrings:  4496
+  Functions: 2913
+  Symbols:   9984
+  CStrings:  4513
 
Symbols:
+ -[BLSHBacklightDisplayStateMachine abortContextForTimer:]
+ -[BLSHBacklightOSInterfaceProvider abortContextForTimer:]
+ -[BLSHBacklightOSInterfaceProvider clearCAWatchdog]
+ -[BLSHBacklightOSInterfaceProvider setCATransitionsDelayForTesting:]
+ -[BLSHBacklightOSInterfaceProvider setCBTransitionsDelayForTesting:]
+ -[BLSHBacklightOSInterfaceProvider timeoutForWatchdogType:]
+ -[BLSHBacklightTransitionStateMachine abortContextForTimer:]
+ GCC_except_table40
+ GCC_except_table72
+ _BLSHBacklightCoreAnimationCallbackSleepImminentWatchdogTimeout
+ _BLSHBacklightCoreAnimationCallbackWatchdogTimeout
+ _BLSHWatchdogTesterDelayCATransitions
+ _BLSHWatchdogTesterDelayCBTransitions
+ _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._caTransitionsDelayForTesting
+ _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._cbTransitionsDelayForTesting
+ _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._lock_CAWatchdogTimer
+ _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._lock_CAWatchdogType
+ _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._lock_CBWatchdogTimer
+ _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._lock_CBWatchdogType
+ ___43-[BLSHWatchdogTester _triggerTestWatchdog:]_block_invoke.67
+ ___43-[BLSHWatchdogTester _triggerTestWatchdog:]_block_invoke.71
+ ___63-[BLSHBacklightOSInterfaceProvider transitionToCADisplayState:]_block_invoke.106
+ ___63-[BLSHBacklightOSInterfaceProvider transitionToCADisplayState:]_block_invoke.108
+ ___63-[BLSHBacklightOSInterfaceProvider transitionToCADisplayState:]_block_invoke.108.cold.1
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32s_e5_v8?0ls32l8
+ _objc_msgSend$abortContextForTimer:
+ _objc_msgSend$setCATransitionsDelayForTesting:
+ _objc_msgSend$setCBTransitionsDelayForTesting:
- -[BLSHBacklightDisplayStateMachine abortContext]
- -[BLSHBacklightOSInterfaceProvider abortContext]
- -[BLSHBacklightOSInterfaceProvider setCompletionDelayForTesting:]
- -[BLSHBacklightTransitionStateMachine abortContext]
- GCC_except_table37
- _BLSHWatchdogTesterDelayCompletions
- _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._completionDelayForTesting
- _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._lock_watchdogTimer
- _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._lock_watchdogType
- ___43-[BLSHWatchdogTester _triggerTestWatchdog:]_block_invoke.61
- ___43-[BLSHWatchdogTester _triggerTestWatchdog:]_block_invoke.62
- _objc_msgSend$setCompletionDelayForTesting:
CStrings:
+ "\nra"
+ ".delayCATransitions-15"
+ ".delayCBTransitions-15"
+ "@\"<BLSHWatchdogAbortContext>\"24@0:8@\"<BLSHWatchdogTiming>\"16"
+ "CATransitionToDisplayState"
+ "CA_DS"
+ "CA_DS_SI"
+ "OSIP: setCATransitionsDelayForTesting:%.02fs"
+ "OSIP: setCBTransitionsDelayForTesting:%.02fs"
+ "OSIP:%p completion(%{public}@->%{public}@) transitionToDisplayState:%{public}@"
+ "OSIP:%p delayCompletionsForTesting:YES, completing delayed CATransitionToDisplayState:%{public}@"
+ "OSIP:%p delayCompletionsForTesting:YES, completing delayed didCompleteCBTransitionToDisplayMode"
+ "OSIP:%p delayCompletionsForTesting:YES, delaying CATransitionToDisplayState:%{public}@ completion by %.2fs"
+ "OSIP:%p delayCompletionsForTesting:YES, delaying didCompleteCBTransitionToDisplayMode by %.2fs"
+ "OSIP:%p transitionToCADisplayState:%@"
+ "Td,?,N,SsetCATransitionsDelayForTesting:"
+ "Td,?,N,SsetCBTransitionsDelayForTesting:"
+ "_abortReason=%llu (%{public}@) com.apple.BacklightServices panicOnCoreAnimationWatchdog:YES wantsPanic:YES"
+ "_abortReason=%llu (%{public}@) com.apple.BacklightServices panicOnCoreBrightnessWatchdog:YES wantsPanic:YES"
+ "_abortReason=%llu (%{public}@) wantsPanic:NO"
+ "_caTransitionsDelayForTesting"
+ "_cbTransitionsDelayForTesting"
+ "_lock_CAWatchdogTimer"
+ "_lock_CAWatchdogType"
+ "_lock_CBWatchdogTimer"
+ "_lock_CBWatchdogType"
+ "abortContextForTimer:"
+ "caTransitionsDelayForTesting"
+ "cbTransitionsDelayForTesting"
+ "panicOnCoreAnimationWatchdog"
+ "setCATransitionsDelayForTesting:"
+ "setCBTransitionsDelayForTesting:"
- "\nqA"
- ".delayCompletions-8"
- "@\"<BLSHWatchdogAbortContext>\"16@0:8"
- "OSIP: setCompletionDelayForTesting:%.02fs"
- "OSIP:%p _delayCompletionsForTesting:YES, completing delayed didCompleteTransitionToDisplayMode"
- "OSIP:%p _delayCompletionsForTesting:YES, delaying didCompleteTransitionToDisplayMode by %.2fs"
- "OSIP:%p completed(%d) transitionToDisplayState:%{public}@"
- "OSIP:%p transitionToCADisplayState:%{public}@"
- "Td,?,N"
- "_completionDelayForTesting"
- "_lock_watchdogTimer"
- "_lock_watchdogType"
- "com.apple.BacklightServices panicOnCoreBrightnessWatchdog:YES wantsPanic:YES"
- "completionDelayForTesting"
- "setCompletionDelayForTesting:"

```
