## BacklightServicesHost

> `/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`

```diff

-4.2.16.0.0
-  __TEXT.__text: 0x855e4
+4.2.19.2.0
+  __TEXT.__text: 0x863b0
   __TEXT.__auth_stubs: 0xa80
-  __TEXT.__objc_methlist: 0x6018
+  __TEXT.__objc_methlist: 0x60b8
   __TEXT.__const: 0x398
-  __TEXT.__gcc_except_tab: 0xe70
-  __TEXT.__cstring: 0x64ed
-  __TEXT.__oslogstring: 0xeef7
+  __TEXT.__gcc_except_tab: 0xff4
+  __TEXT.__cstring: 0x6539
+  __TEXT.__oslogstring: 0xf0b9
   __TEXT.__ustring: 0x2fe
-  __TEXT.__unwind_info: 0x2148
-  __TEXT.__objc_classname: 0x1f53
-  __TEXT.__objc_methname: 0x1108c
+  __TEXT.__unwind_info: 0x2168
+  __TEXT.__objc_classname: 0x1f66
+  __TEXT.__objc_methname: 0x11229
   __TEXT.__objc_methtype: 0x41fd
-  __TEXT.__objc_stubs: 0x9c40
-  __DATA_CONST.__got: 0x758
+  __TEXT.__objc_stubs: 0x9d20
+  __DATA_CONST.__got: 0x760
   __DATA_CONST.__const: 0x2440
-  __DATA_CONST.__objc_classlist: 0x538
+  __DATA_CONST.__objc_classlist: 0x540
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2eb0
-  __DATA_CONST.__objc_superrefs: 0x440
+  __DATA_CONST.__objc_selrefs: 0x2ef0
+  __DATA_CONST.__objc_superrefs: 0x448
   __DATA_CONST.__objc_arraydata: 0x78
   __AUTH_CONST.__auth_got: 0x550
   __AUTH_CONST.__const: 0xb40
-  __AUTH_CONST.__cfstring: 0x5fe0
-  __AUTH_CONST.__objc_const: 0x15b70
+  __AUTH_CONST.__cfstring: 0x60c0
+  __AUTH_CONST.__objc_const: 0x15e40
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0xda4
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0xddc
   __DATA.__data: 0x1f20
   __DATA.__bss: 0x90
   __DATA_DIRTY.__objc_data: 0x3390

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 3118
-  Symbols:   3799
-  CStrings:  4896
+  Functions: 3136
+  Symbols:   3822
+  CStrings:  4923
 
Symbols:
+ _OBJC_CLASS_$_BLSHSystemWakeWaiter
+ _OBJC_METACLASS_$_BLSHSystemWakeWaiter
CStrings:
+ "\x05\x14R"
+ "\x12\x12\x11Q"
+ "\x1b"
+ "%!@(MISSING) in %!@(MISSING)"
+ "%!@(MISSING):%!@(MISSING) already waiting"
+ "%!@(MISSING):%!@(MISSING) asked to run block while system is asleep, waiting."
+ "%!@(MISSING):%!@(MISSING) asked to run block while system is awake, running now."
+ "%!@(MISSING):%!@(MISSING) system awake, running pending block, waited:%!l(MISSING)fs."
+ "%!@(MISSING):%!@(MISSING) system did wake but waiter was invalidated (%!@(MISSING)) or completion is nil (%!@(MISSING))"
+ "%!p(MISSING) (localHostEnv) not clearing cached presentation date:%!{(MISSING)public}@ (should be cleared later by host)"
+ "%!p(MISSING) (localHostUpdater) updatedEnvironmentWithDelta: doPerformEvent:%!{(MISSING)BOOL}u inactiveEnvSession:%!p(MISSING) presentation:%!{(MISSING)public}@ %!{(MISSING)public}@ -> %!{(MISSING)public}@"
+ "%!p(MISSING) assertion setPaused:%!{(MISSING)BOOL}u when not acquired %!{(MISSING)public}@"
+ "(n/a)"
+ "BLSHSystemWakeWaiter"
+ "BLSHSystemWakeWaiter.m"
+ "DSM:%!p(MISSING) hadTransition=%!{(MISSING)BOOL}u mode:%!{(MISSING)public}@ isLiveRendering:%!{(MISSING)BOOL}u didReleaseLiveRendering:%!{(MISSING)BOOL}u seqId:%!d(MISSING)"
+ "Live rendering assertion held for > 90 seconds"
+ "NO"
+ "S"
+ "T@\"NSString\",&,V_displayReason"
+ "YES"
+ "_displayReason"
+ "_lock_accumulatedUnpausedDuration"
+ "_lock_acquired"
+ "_lock_acquiredMachContinuousTime"
+ "_lock_canceledMachContinuousTime"
+ "_lock_everPaused"
+ "_lock_invalidate"
+ "_lock_unpauseMachContinuousTime"
+ "_lock_waiting"
+ "activeDuration"
+ "displayReason"
+ "enableSubhostingForEnvironment:withSessionProvider:osTimerProvider:"
+ "initWithIdentifier:osTimerProvider:"
+ "initWithOSTimerProvider:"
+ "initWithSessionProvider:localHostEnvironment:osTimerProvider:"
+ "isPaused"
+ "runWhenAwakeWithCompletion:"
+ "setDisplayReason:"
+ "waiterWithIdentifier:osInterfaceProvider:"
+ "\xe1"
- "\x06\x14R"
- "\x13\x12\x11Q"
- "\x14"
- "\x1a"
- "%!p(MISSING) (localHostUpdater) updatedEnvironmentWithDelta: doPerformEvent:%!{(MISSING)BOOL}u inactiveEnvSession:%!p(MISSING) presentation:%!{(MISSING)public}@"
- "A"
- "BacklightEvent"
- "BacklightServices %!@(MISSING) watchdog failed in %!@(MISSING)"
- "DSM:%!p(MISSING) hadTransition=NO mode:%!{(MISSING)public}@ isLiveRendering:%!{(MISSING)BOOL}u didReleaseLiveRendering:%!{(MISSING)BOOL}u seqId:%!d(MISSING)"
- "RequestDates"
- "TB,R,N,GisAcquired,V_acquired"
- "_acquired"
- "_lock_flipbookPowerSavingAssertion"
- "initWithSessionProvider:localHostEnvironment:"
- "\xf1"

```
