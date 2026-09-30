## BacklightServicesHost

> `/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`

```diff

-4.0.34.0.0
-  __TEXT.__text: 0x7ba60
-  __TEXT.__auth_stubs: 0xa50
-  __TEXT.__objc_methlist: 0x5a40
-  __TEXT.__const: 0x388
-  __TEXT.__oslogstring: 0xe199
-  __TEXT.__cstring: 0x5d90
-  __TEXT.__gcc_except_tab: 0xcc8
-  __TEXT.__ustring: 0x1f4
-  __TEXT.__unwind_info: 0x1e68
-  __TEXT.__objc_classname: 0x1db5
-  __TEXT.__objc_methname: 0x1054e
-  __TEXT.__objc_methtype: 0x4075
-  __TEXT.__objc_stubs: 0x94e0
-  __DATA_CONST.__got: 0x6e0
-  __DATA_CONST.__const: 0x2208
-  __DATA_CONST.__objc_classlist: 0x4f0
+4.1.3.0.0
+  __TEXT.__text: 0x7e290
+  __TEXT.__auth_stubs: 0xa70
+  __TEXT.__objc_methlist: 0x5b78
+  __TEXT.__const: 0x398
+  __TEXT.__oslogstring: 0xe746
+  __TEXT.__cstring: 0x5ec3
+  __TEXT.__gcc_except_tab: 0xd04
+  __TEXT.__ustring: 0x2ae
+  __TEXT.__unwind_info: 0x1ef8
+  __TEXT.__objc_classname: 0x1e3a
+  __TEXT.__objc_methname: 0x10857
+  __TEXT.__objc_methtype: 0x40d8
+  __TEXT.__objc_stubs: 0x96c0
+  __DATA_CONST.__got: 0x6f0
+  __DATA_CONST.__const: 0x22f0
+  __DATA_CONST.__objc_classlist: 0x500
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x280
+  __DATA_CONST.__objc_protolist: 0x290
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ca8
-  __DATA_CONST.__objc_superrefs: 0x418
+  __DATA_CONST.__objc_selrefs: 0x2d20
+  __DATA_CONST.__objc_superrefs: 0x420
   __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__auth_got: 0x538
-  __AUTH_CONST.__const: 0xa20
-  __AUTH_CONST.__cfstring: 0x5b20
-  __AUTH_CONST.__objc_const: 0x14980
+  __AUTH_CONST.__auth_got: 0x548
+  __AUTH_CONST.__const: 0xb20
+  __AUTH_CONST.__cfstring: 0x5c60
+  __AUTH_CONST.__objc_const: 0x14e10
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0xeb0
-  __DATA.__objc_ivar: 0xccc
-  __DATA.__data: 0x1e00
-  __DATA.__bss: 0x78
-  __DATA_DIRTY.__objc_data: 0x22b0
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0xd08
+  __DATA.__data: 0x1ec0
+  __DATA.__bss: 0x88
+  __DATA_DIRTY.__objc_data: 0x31b0
   __DATA_DIRTY.__bss: 0xf8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
   - /System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
+  - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /System/Library/PrivateFrameworks/PowerExperience.framework/PowerExperience
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SystemWake.framework/SystemWake

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 2894
-  Symbols:   3542
-  CStrings:  4665
+  Functions: 2949
+  Symbols:   3608
+  CStrings:  4723
 
Symbols:
+ _BLSHBacklightCoreAnimationCallbackWatchdogInternalInstallTimeout
+ _CFPreferencesAppSynchronize
+ _OBJC_CLASS_$_BLSHSystemWaker
+ _OBJC_METACLASS_$_BLSHSystemWaker
+ _OSLogFlushBuffers
+ ___kCFBooleanTrue
CStrings:
+ "\x01\x12\xf0\xe2"
+ "\x1f\v"
+ "%!@(MISSING) called after initialization"
+ "%!@(MISSING):%!@(MISSING) already waking"
+ "%!p(MISSING) (localHostUpdater) [environmentStateMachine performEvent:withInitialSpecifier:performBacklightRamp:] finished, event:%!{(MISSING)public}@, duration:%!f(MISSING)"
+ "%!p(MISSING) (localHostUpdater) calling [environmentStateMachine performEvent:withInitialSpecifier:performBacklightRamp:], event:%!{(MISSING)public}@, dateSpecifier:%!{(MISSING)public}@"
+ "%!p(MISSING) (localHostUpdater) calling [environmentStateMachine updateToSpecifier:], dateSpecifier:%!{(MISSING)public}@"
+ "%!p(MISSING) (localHostUpdater) created alwaysOnSession:%!{(MISSING)public}@ for updatedEnvironment:%!{(MISSING)public}@ withDelta:%!{(MISSING)public}@"
+ "%!p(MISSING) (localHostUpdater) destroying alwaysOnSession:%!{(MISSING)public}@ for updatedEnvironment:%!{(MISSING)public}@ withDelta:%!{(MISSING)public}@"
+ "%!p(MISSING) (localHostUpdater) updatedEnvironmentWithDelta: doPerformEvent:%!{(MISSING)BOOL}u inactiveEnvSession:%!p(MISSING) presentation:%!{(MISSING)public}@"
+ "%!p(MISSING) system awoke  %!@(MISSING):\"%!{(MISSING)public}@\" elapsed:%!l(MISSING)fs hasSleepBeenRequested:%!{(MISSING)BOOL}u"
+ "%!p(MISSING) system waker activity acquired:\"%!{(MISSING)public}@\" elapsed:%!l(MISSING)fs hasSleepBeenRequested:%!{(MISSING)BOOL}u error:%!{(MISSING)public}@"
+ "%!p(MISSING) waited for system awake :\"%!{(MISSING)public}@\" details:%!{(MISSING)public}@ elapsed:%!l(MISSING)fs hasSleepBeenRequested:%!{(MISSING)BOOL}u activityActive:%!{(MISSING)BOOL}u"
+ "%!p(MISSING):%!{(MISSING)public}@ invalidate flipbook for source:%!{(MISSING)public}@ reason:%!{(MISSING)public}@ frameCount:%!u(MISSING) didClearDateSpecifiers:%!{(MISSING)BOOL}u wasReset:%!{(MISSING)BOOL}u %!s(MISSING):%!{(MISSING)public}@ zeroedFrameCount:%!u(MISSING)"
+ "%!p(MISSING):%!{(MISSING)public}@ willBeginRenderSession:%!p(MISSING) oldAssertion:%!p(MISSING)"
+ "%!p(MISSING):%!{(MISSING)public}@ willEndRenderSession:%!p(MISSING) assertion:%!p(MISSING)"
+ "(same)"
+ ".delayCATransitions-7"
+ "@\"<BLSHSystemActivityAsserting>\"32@0:8@\"NSString\"16@?<v@?@\"<SWSystemActivityAssertionConfiguring>\">24"
+ "B16@?0@\"BLSHEnvironmentDateSpecifier\"8"
+ "BLSHSystemActivityAssertionConfiguration"
+ "BLSHSystemActivityAssertionConfiguring"
+ "BLSHSystemWaker"
+ "BLSHSystemWaker.m"
+ "BacklightServices.liveRendering"
+ "DSM:%!p(MISSING) already have live rendering system activity assertion %!{(MISSING)public}@"
+ "DSM:%!p(MISSING) dropping live rendering system activity assertion %!{(MISSING)public}@"
+ "DSM:%!p(MISSING) live rendering system activity assertion callback elapsed:%!l(MISSING)fs details:%!{(MISSING)public}@ error:%!{(MISSING)public}@"
+ "ESM:%!p(MISSING) setPresentation: staleEnvironmentsThatNeedDeferredUpdate:%!{(MISSING)public}@"
+ "Failed to sync com.apple.BacklightServices after writing %!{(MISSING)public}@ key"
+ "SWSystemActivityAssertionConfiguring"
+ "T@\"<BLSHOSInterfaceProviding>\",W,N,SsetOSInterfaceProvider:,V_osInterfaceProvider"
+ "TB,N,V_acquireWaitsToAbortSleepRequested"
+ "TSM:%!p(MISSING) (findNextOperation) did not stop  presentation engine:%!{(MISSING)public}@ (displayMode:%!{(MISSING)public}@)"
+ "TSM:%!p(MISSING) onScreenSpecifierForDisplayMode:%!{(MISSING)public}@ will use current:%!{(MISSING)public}@"
+ "TSM:%!p(MISSING) specifier environment:%!{(MISSING)public}@ not in presentation:%!{(MISSING)public}@ or target:%!{(MISSING)public}@"
+ "TSM:%!p(MISSING) will amend scene %!{(MISSING)public}@ for backlightState:%!{(MISSING)public}@ with visualState:%!{(MISSING)public}@ – willBeForeground:%!{(MISSING)BOOL}u containsEnv:%!{(MISSING)BOOL}u presentation:%!{(MISSING)public}@ oldVisualState:%!{(MISSING)public}@ oldPresentationDate:%!{(MISSING)public}@ settingsVisualState:%!{(MISSING)public}@ settingsPresentationDate:%!{(MISSING)public}@"
+ "TSM:%!p(MISSING) will not amend scene %!{(MISSING)public}@ for backlightState:%!{(MISSING)public}@ with settingsVisualState:%!{(MISSING)public}@ willBeForeground:%!{(MISSING)BOOL}u containsEnv:%!{(MISSING)BOOL}u presentation:%!{(MISSING)public}@ oldVisualState:%!{(MISSING)public}@"
+ "TSM:%!p(MISSING) would have (but will not) amend scene %!{(MISSING)public}@ for backlightState:%!{(MISSING)public}@ with visualState:%!{(MISSING)public}@ – willBeForeground:%!{(MISSING)BOOL}u containsEnv:%!{(MISSING)BOOL}u presentation:%!{(MISSING)public}@ oldVisualState:%!{(MISSING)public}@ oldPresentationDate:%!{(MISSING)public}@ settingsVisualState:%!{(MISSING)public}@ settingsPresentationDate:%!{(MISSING)public}@"
+ "_acquireWaitsToAbortSleepRequested"
+ "_initializing"
+ "_lock_aggregateAssertions"
+ "_lock_completion"
+ "_lock_frameOnGlassWhenFlipbookCancelled"
+ "_lock_frameOnGlassWhenFlipbookLastCancelledAndReset"
+ "_lock_liveRenderingSystemActivityAssertion"
+ "_lock_systemActivity"
+ "_lock_waitStartTimestamp"
+ "_lock_waking"
+ "_osInterfaceProvider != nil"
+ "acquireWaitsToAbortSleepRequested"
+ "alreadyAwake"
+ "callCompletionForReason:"
+ "createAggregatedSystemActivityAssertionWithIdentifier:configurator:"
+ "createSystemActivityAssertionWithIdentifier:configurator:"
+ "failed:%!d(MISSING)"
+ "filter:"
+ "initWithConfigurator:"
+ "initWithIdentifier:configurator:"
+ "invalidateOnGlassFlipbookFrame"
+ "liveAssertion"
+ "onGlassFlipbookFrame"
+ "panicForWatchdog: OSLogFlushBuffers() %!{(MISSING)public}@"
+ "panicForWatchdog: flushing os log buffers"
+ "panicForWatchdog: triggering panic after %!l(MISSING)fs delay: %!{(MISSING)public}@"
+ "panicForWatchdog:completion:"
+ "performConfigurator:"
+ "previousOnGlassFrame"
+ "setAcquireWaitsToAbortSleepRequested:"
+ "setCompletion:"
+ "setOSInterfaceProvider:"
+ "sharedSystemActivityFactory"
+ "succeeded"
+ "v16@?0@\"<BLSHSystemActivityAssertionConfiguring>\"8"
+ "v16@?0@\"<SWSystemActivityAssertionConfiguring>\"8"
+ "v24@0:8@\"<BLSHOSInterfaceProviding>\"16"
+ "v32@0:8@\"NSString\"16@?<v@?B>24"
+ "waitWithSystemSleepMonitor:completion:"
+ "wakeWithCompletion:"
+ "wakerWithIdentifier:osInterfaceProvider:"
+ "\xf0\xf0\x81"
- "\x01\x12\xf0\xe1"
- "\x1f\n"
- "%!p(MISSING) (localHostUpdater) [environmentStateMachine performEvent:withInitialSpecifier:performBacklightRamp:] finished, event:%!@(MISSING), duration:%!f(MISSING)"
- "%!p(MISSING) (localHostUpdater) calling [environmentStateMachine performEvent:withInitialSpecifier:performBacklightRamp:], event:%!@(MISSING), dateSpecifier:%!@(MISSING)"
- "%!p(MISSING) (localHostUpdater) calling [environmentStateMachine updateToSpecifier:], dateSpecifier:%!@(MISSING)"
- "%!p(MISSING) (localHostUpdater) created alwaysOnSession:%!{(MISSING)public}@ for updatedEnvironment:%!@(MISSING) withDelta:%!@(MISSING)"
- "%!p(MISSING) (localHostUpdater) destroying alwaysOnSession:%!{(MISSING)public}@ for updatedEnvironment:%!@(MISSING) withDelta:%!@(MISSING)"
- "%!p(MISSING) (localHostUpdater) updatedEnvironmentWithDelta: doPerformEvent:%!{(MISSING)BOOL}u inactiveEnvSession:%!@(MISSING) presentationEntries:%!@(MISSING)"
- "%!p(MISSING) system activity acquired %!@(MISSING):\"%!{(MISSING)public}@\" elapsed:%!l(MISSING)fs hasSleepBeenRequested:%!{(MISSING)BOOL}u error:%!{(MISSING)public}@"
- "%!p(MISSING):%!{(MISSING)public}@ invalidate flipbook for source:%!{(MISSING)public}@ reason:%!{(MISSING)public}@ frameCount:%!u(MISSING) didClearDateSpecifiers:%!{(MISSING)BOOL}u wasReset:%!{(MISSING)BOOL}u onGlassFrame:%!{(MISSING)public}@ zeroedFrameCount:%!u(MISSING)"
- ".delayCATransitions-15"
- "@\"<BLSHSystemActivityAsserting>\"24@0:8@\"NSString\"16"
- "B24@0:8@\"NSString\"16"
- "ESM:%!p(MISSING) setPresentation: _lock_removedEnvsForStateUpdateLater:%!{(MISSING)public}@"
- "TSM:%!p(MISSING) (findNextOperation) will use current presentation specifier:%!{(MISSING)public}@ for events:%!{(MISSING)public}@"
- "TSM:%!p(MISSING) amend scene %!{(MISSING)public}@ for backlightState:%!{(MISSING)public}@ with visualState:%!{(MISSING)public}@ willBeForeground:%!{(MISSING)BOOL}u containsEnv:%!{(MISSING)BOOL}u presentation:%!{(MISSING)public}@ environment:%!{(MISSING)public}@"
- "TSM:%!p(MISSING) will not amend scene %!{(MISSING)public}@ for backlightState:%!{(MISSING)public}@ with visualState:%!{(MISSING)public}@ willBeForeground:%!{(MISSING)BOOL}u containsEnv:%!{(MISSING)BOOL}u presentation:%!{(MISSING)public}@ environment:%!{(MISSING)public}@"
- "_lock_frameOnGlassWhenFlipbookLastCancelled"
- "_lock_renderSessionAssertion == nil"
- "createAggregatedSystemActivityAssertionWithIdentifier:usingOSInterfaceProvider:"
- "createSystemActivityAssertionWithIdentifier:"
- "panicForWatchdog:"
- "\xf0\xf0q"

```
