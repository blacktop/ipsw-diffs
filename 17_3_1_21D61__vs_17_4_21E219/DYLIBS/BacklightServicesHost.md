## BacklightServicesHost

> `/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`

```diff

-3.2.4.0.0
-  __TEXT.__text: 0x76ebc
-  __TEXT.__auth_stubs: 0xa60
-  __TEXT.__objc_methlist: 0x545c
+3.4.9.0.0
+  __TEXT.__text: 0x77f34
+  __TEXT.__auth_stubs: 0xa40
+  __TEXT.__objc_methlist: 0x548c
   __TEXT.__const: 0x228
-  __TEXT.__oslogstring: 0xd709
-  __TEXT.__cstring: 0x5938
-  __TEXT.__gcc_except_tab: 0x818
+  __TEXT.__oslogstring: 0xdd13
+  __TEXT.__cstring: 0x59da
+  __TEXT.__gcc_except_tab: 0x838
   __TEXT.__ustring: 0x1f4
-  __TEXT.__unwind_info: 0x1c5c
-  __TEXT.__objc_classname: 0x1c0e
-  __TEXT.__objc_methname: 0xf8e2
-  __TEXT.__objc_methtype: 0x3e81
-  __TEXT.__objc_stubs: 0x8f40
+  __TEXT.__unwind_info: 0x1c80
+  __TEXT.__objc_classname: 0x1c2a
+  __TEXT.__objc_methname: 0xf994
+  __TEXT.__objc_methtype: 0x3f84
+  __TEXT.__objc_stubs: 0x8fc0
   __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0x2048
-  __DATA_CONST.__objc_classlist: 0x4a0
+  __DATA_CONST.__const: 0x2020
+  __DATA_CONST.__objc_classlist: 0x4a8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xfdc0
-  __DATA_CONST.__objc_selrefs: 0x2a90
+  __DATA_CONST.__objc_const: 0xfd88
+  __DATA_CONST.__objc_selrefs: 0x2ac0
+  __DATA_CONST.__objc_classrefs: 0x7d8
+  __DATA_CONST.__objc_superrefs: 0x3d8
   __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__objc_const: 0x39c0
+  __AUTH_CONST.__objc_const: 0x3a08
   __AUTH_CONST.__cfstring: 0x5860
   __AUTH_CONST.__const: 0x9a0
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x540
-  __AUTH.__objc_data: 0x1540
-  __DATA.__objc_classrefs: 0x7d0
-  __DATA.__objc_superrefs: 0x3d0
-  __DATA.__objc_ivar: 0xc34
+  __AUTH_CONST.__auth_got: 0x530
+  __AUTH.__objc_data: 0x1360
+  __DATA.__objc_ivar: 0xc2c
   __DATA.__data: 0x1d40
-  __DATA.__bss: 0x90
-  __DATA_DIRTY.__objc_data: 0x1900
-  __DATA_DIRTY.__bss: 0xd0
+  __DATA.__bss: 0x88
+  __DATA_DIRTY.__objc_data: 0x1b30
+  __DATA_DIRTY.__bss: 0xd8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 4C1EC8CA-7E31-3CD6-8F9A-41E4FDCD042F
-  Functions: 2901
-  Symbols:   9943
-  CStrings:  5180
+  UUID: F3DBDA60-391E-3C5C-A897-55BB2614574E
+  Functions: 2907
+  Symbols:   9962
+  CStrings:  5203
 
Symbols:
+ -[BLSHBacklightDisplayStateMachine acquireDisplayPowerAssertionForReason:]
+ -[BLSHBacklightDisplayStateMachine osInterfaceProvider:didCompleteSwitchToCBFlipbookState:withError:]
+ -[BLSHBacklightDisplayStateMachine osInterfaceProvider:didCompleteSwitchToCBFlipbookState:withError:].cold.1
+ -[BLSHBacklightDisplayStateMachine osInterfaceProvider:didCompleteTransitionToCADisplayState:currentState:transitionStatus:]
+ -[BLSHBacklightDisplayStateMachine osInterfaceProvider:didCompleteTransitionToCBDisplayMode:withError:]
+ -[BLSHBacklightDisplayStateMachine osInterfaceProvider:didCompleteTransitionToCBDisplayMode:withError:].cold.1
+ -[BLSHBacklightDisplayStateMachine osInterfaceProvider:didCompleteTransitionToCBDisplayMode:withError:].cold.2
+ -[BLSHBacklightDisplayStateMachine releaseDisplayPowerAssertion]
+ -[BLSHBacklightDisplayStateMachine switchToFlipbookState:].cold.1
+ -[BLSHBacklightDisplayStateMachine transitionToCADisplayState:]
+ -[BLSHBacklightDisplayStateMachine transitionToCADisplayState:].cold.1
+ -[BLSHBacklightDisplayStateMachineAbortContext initWithDisplayMode:prewarmingDisplayMode:lastSteadyStateDisplayMode:caDisplayState:cbDisplayMode:showingBlankingWindow:sleepRequested:sleepImminent:timeInSleepImminent:hasEnsureFlipbookCurrent:]
+ -[BLSHBacklightOSInterfaceProvider acquireDisplayPowerAssertionForReason:]
+ -[BLSHBacklightOSInterfaceProvider caDisplayPowerState]
+ -[BLSHBacklightOSInterfaceProvider caDisplayState]
+ -[BLSHBacklightOSInterfaceProvider displayStateDelegate]
+ -[BLSHBacklightOSInterfaceProvider initWithPlatformProvider:].cold.1
+ -[BLSHBacklightOSInterfaceProvider notifyDisplayBlankedIfChangedForCADisplayState:]
+ -[BLSHBacklightOSInterfaceProvider setDisplayStateDelegate:]
+ -[BLSHBacklightOSInterfaceProvider transitionToCADisplayState:]
+ -[BLSHBacklightOSInterfaceProvider transitionToCADisplayState:].cold.1
+ -[BLSHEnvironmentTransitionState performBacklightRampIfPendingForReason:]
+ -[BLSHEnvironmentTransitionState updateToTarget:touchTargetable:presentationDate:sceneUpdate:requestedFidelity:]
+ -[BLSHEnvironmentTransitionState updateToTarget:touchTargetable:presentationDate:sceneUpdate:requestedFidelity:].cold.1
+ -[BLSHEnvironmentTransitionStateTarget initWithSequenceID:backlightState:triggerEvent:backlightRampBlock:forIdentifier:previousTarget:]
+ -[BLSHEnvironmentTransitionStateTarget initWithSequenceID:backlightState:visualState:presentationDate:triggerEvent:pendingBacklightRamp:]
+ -[BLSHEnvironmentTransitionStateTarget pendingBacklightRamp]
+ -[BLSHOSInterfaceProviderAbortContext initWithWatchdogType:cbDisplayMode:cbFlipbookState:caDisplayState:completedCADisplayState:suppressionServiceActive:flipbookTransparent:deviceSupportsAlwaysOn:kernelSpecialMode:displayStateClientSupported:backlightDimmedFactor:]
+ -[BLSHPendingBacklightRamp .cxx_destruct]
+ -[BLSHPendingBacklightRamp description]
+ -[BLSHPendingBacklightRamp hasPendingRamp]
+ -[BLSHPendingBacklightRamp initWithBacklightRampBlock:]
+ -[BLSHPendingBacklightRamp performBacklightRampIfNeededWithDuration:]
+ GCC_except_table37
+ _BKSDisplayServicesNotifyDisplayBlanked
+ _BKSHIDServicesNotifyBacklightFactorWithFadeDurationAsync
+ _NSStringFromCADisplayState
+ _NSStringFromCADisplayStateTransitionStatus
+ _OBJC_CLASS_$_BLSHPendingBacklightRamp
+ _OBJC_IVAR_$_BLSHBacklightDisplayStateMachine._lock_caDisplayPowerAssertion
+ _OBJC_IVAR_$_BLSHBacklightDisplayStateMachine._lock_caDisplayStateChangeOperation
+ _OBJC_IVAR_$_BLSHBacklightDisplayStateMachine._lock_completedCADisplayState
+ _OBJC_IVAR_$_BLSHBacklightDisplayStateMachineAbortContext._caDisplayState
+ _OBJC_IVAR_$_BLSHBacklightDisplayStateMachineAbortContext._cbDisplayMode
+ _OBJC_IVAR_$_BLSHBacklightDisplayStateMachineAbortContext._prewarmingDisplayMode
+ _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._displayStateControl
+ _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._displayStateDelegate
+ _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._lock_caDisplayState
+ _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._lock_notifiedCADisplayState
+ _OBJC_IVAR_$_BLSHEnvironmentTransitionStateTarget._pendingBacklightRamp
+ _OBJC_IVAR_$_BLSHOSInterfaceProviderAbortContext._caDisplayState
+ _OBJC_IVAR_$_BLSHOSInterfaceProviderAbortContext._completedCADisplayState
+ _OBJC_IVAR_$_BLSHPendingBacklightRamp._lock
+ _OBJC_IVAR_$_BLSHPendingBacklightRamp._lock_backlightRampBlock
+ _OBJC_METACLASS_$_BLSHPendingBacklightRamp
+ __OBJC_$_INSTANCE_METHODS_BLSHPendingBacklightRamp
+ __OBJC_$_INSTANCE_VARIABLES_BLSHPendingBacklightRamp
+ __OBJC_$_PROP_LIST_BLSHFlipbook.82
+ __OBJC_$_PROP_LIST_BLSHPendingBacklightRamp
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BLSDisplayStateDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSDisplayStateDelegate
+ __OBJC_$_PROTOCOL_REFS_BLSDisplayStateDelegate
+ __OBJC_CLASS_RO_$_BLSHPendingBacklightRamp
+ __OBJC_LABEL_PROTOCOL_$_BLSDisplayStateDelegate
+ __OBJC_METACLASS_RO_$_BLSHPendingBacklightRamp
+ __OBJC_PROTOCOL_$_BLSDisplayStateDelegate
+ ___101-[BLSHBacklightDisplayStateMachine osInterfaceProvider:didCompleteSwitchToCBFlipbookState:withError:]_block_invoke
+ ___102-[BLSHBacklightEnvironmentStateMachine transitionState:didCompleteUpdateToBacklightState:visualState:]_block_invoke.141
+ ___103-[BLSHBacklightDisplayStateMachine osInterfaceProvider:didCompleteTransitionToCBDisplayMode:withError:]_block_invoke
+ ___112-[BLSHEnvironmentTransitionState updateToTarget:touchTargetable:presentationDate:sceneUpdate:requestedFidelity:]_block_invoke
+ ___112-[BLSHEnvironmentTransitionState updateToTarget:touchTargetable:presentationDate:sceneUpdate:requestedFidelity:]_block_invoke_2
+ ___112-[BLSHEnvironmentTransitionState updateToTarget:touchTargetable:presentationDate:sceneUpdate:requestedFidelity:]_block_invoke_3
+ ___124-[BLSHBacklightDisplayStateMachine osInterfaceProvider:didCompleteTransitionToCADisplayState:currentState:transitionStatus:]_block_invoke
+ ___59-[BLSHBacklightOSInterfaceProvider setFlipbookTransparent:]_block_invoke
+ ___63-[BLSHBacklightOSInterfaceProvider transitionToCADisplayState:]_block_invoke
+ ___77-[BLSHEngineRenderFlipbookSession renderFrameSpecifier:timedOutEnvironments:]_block_invoke.516
+ ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke.97
+ ___89-[BLSHLocalHostSceneEnvironmentUpdater updatedEnvironmentWithDelta:backlightSceneUpdate:]_block_invoke.131
+ ___89-[BLSHLocalHostSceneEnvironmentUpdater updatedEnvironmentWithDelta:backlightSceneUpdate:]_block_invoke.131.cold.1
+ ___block_descriptor_32_e35_16?0"BLSAlwaysOnFrameSpecifier"8l
+ ___block_descriptor_41_e8_32s_e11_v24?0q8q16ls32l8
+ ___block_descriptor_48_e8_32s_e11_v24?0q8q16ls32l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSArray"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_65_e8_32s40s48s56s_e8_v16?0q8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_65_e8_32s40s48s56w_e5_v8?0ls32l8s40l8s48l8w56l8
+ ___block_descriptor_72_e8_32s40s48s56s64w_e5_v8?0ls32l8s40l8w64l8s48l8s56l8
+ ___block_literal_global.100
+ ___block_literal_global.117
+ ___block_literal_global.121
+ ___block_literal_global.143
+ ___block_literal_global.506
+ ___block_literal_global.635
+ _objc_msgSend$acquire
+ _objc_msgSend$acquireDisplayPowerAssertionForReason:
+ _objc_msgSend$caDisplayState
+ _objc_msgSend$constructFrameSpecifiersForTimelines:dateInterval:shouldConstructStartSpecifier:framesPerSecond:previousSpecifier:
+ _objc_msgSend$createPowerAssertionWithReason:identifier:
+ _objc_msgSend$displayState
+ _objc_msgSend$displayStateDelegate
+ _objc_msgSend$hasPendingRamp
+ _objc_msgSend$initWithBacklightRampBlock:
+ _objc_msgSend$initWithDisplayMode:prewarmingDisplayMode:lastSteadyStateDisplayMode:caDisplayState:cbDisplayMode:showingBlankingWindow:sleepRequested:sleepImminent:timeInSleepImminent:hasEnsureFlipbookCurrent:
+ _objc_msgSend$initWithSequenceID:backlightState:triggerEvent:backlightRampBlock:forIdentifier:previousTarget:
+ _objc_msgSend$initWithSequenceID:backlightState:visualState:presentationDate:triggerEvent:pendingBacklightRamp:
+ _objc_msgSend$initWithWatchdogType:cbDisplayMode:cbFlipbookState:caDisplayState:completedCADisplayState:suppressionServiceActive:flipbookTransparent:deviceSupportsAlwaysOn:kernelSpecialMode:displayStateClientSupported:backlightDimmedFactor:
+ _objc_msgSend$osInterfaceProvider:didCompleteSwitchToCBFlipbookState:withError:
+ _objc_msgSend$osInterfaceProvider:didCompleteTransitionToCADisplayState:currentState:transitionStatus:
+ _objc_msgSend$osInterfaceProvider:didCompleteTransitionToCBDisplayMode:withError:
+ _objc_msgSend$pendingBacklightRamp
+ _objc_msgSend$performBacklightRampIfNeededWithDuration:
+ _objc_msgSend$performBacklightRampIfPendingForReason:
+ _objc_msgSend$powerState
+ _objc_msgSend$setDisplayStateDelegate:
+ _objc_msgSend$stateControl
+ _objc_msgSend$transitionToCADisplayState:
+ _objc_msgSend$transitionToDisplayState:withCompletion:
- -[BLSHBacklightDisplayStateMachine osInterfaceProvider:didCompleteSwitchToFlipbookState:withError:]
- -[BLSHBacklightDisplayStateMachine osInterfaceProvider:didCompleteSwitchToFlipbookState:withError:].cold.1
- -[BLSHBacklightDisplayStateMachine osInterfaceProvider:didCompleteTransitionToDisplayMode:withError:]
- -[BLSHBacklightDisplayStateMachine osInterfaceProvider:didCompleteTransitionToDisplayMode:withError:].cold.1
- -[BLSHBacklightDisplayStateMachine osInterfaceProvider:didCompleteTransitionToDisplayMode:withError:].cold.2
- -[BLSHBacklightDisplayStateMachineAbortContext initWithDisplayMode:transitioningToDisplayMode:lastSteadyStateDisplayMode:isFlipbookEnabled:showingBlankingWindow:backlightFactor:isCABlanked:displayIsOff:sleepRequested:sleepImminent:timeInSleepImminent:hasEnsureFlipbookCurrent:]
- -[BLSHBacklightOSInterfaceProvider cbDisplayStateDelegate]
- -[BLSHBacklightOSInterfaceProvider isCABlanked]
- -[BLSHBacklightOSInterfaceProvider isCAFlipbookEnabled]
- -[BLSHBacklightOSInterfaceProvider isCAFlipbookSuppressed]
- -[BLSHBacklightOSInterfaceProvider setCABlanked:]
- -[BLSHBacklightOSInterfaceProvider setCABlanked:].cold.1
- -[BLSHBacklightOSInterfaceProvider setCAFlipbookEnabled:]
- -[BLSHBacklightOSInterfaceProvider setCAFlipbookSuppressed:]
- -[BLSHBacklightOSInterfaceProvider setCBDisplayStateDelegate:]
- -[BLSHBacklightOSInterfaceProvider willUnblank]
- -[BLSHEnvironmentTransitionState updateToTarget:forEvent:touchTargetable:presentationDate:sceneUpdate:requestedFidelity:performBacklightRamp:]
- -[BLSHEnvironmentTransitionState updateToTarget:forEvent:touchTargetable:presentationDate:sceneUpdate:requestedFidelity:performBacklightRamp:].cold.1
- -[BLSHEnvironmentTransitionStateTarget backlightRampBlock]
- -[BLSHEnvironmentTransitionStateTarget initWithSequenceID:backlightState:triggerEvent:backlightRampBlock:]
- -[BLSHEnvironmentTransitionStateTarget initWithSequenceID:backlightState:visualState:presentationDate:triggerEvent:backlightRampBlock:]
- -[BLSHEnvironmentTransitionStateTarget setAndTestDidPerformBacklightRamp]
- -[BLSHOSInterfaceProviderAbortContext initWithWatchdogType:cbDisplayMode:cbFlipbookState:suppressionServiceActive:caFlipbookEnabled:caFlipbookSuppressed:caBlanked:flipbookTransparent:deviceSupportsAlwaysOn:kernelSpecialMode:displayStateClientSupported:backlightDimmedFactor:]
- _BKSDisplayServicesIsFlipBookEnabled
- _BKSDisplayServicesIsFlipBookSuppressed
- _BKSDisplayServicesSetFlipBookEnabled
- _BKSDisplayServicesSetFlipBookSuppressed
- _BKSDisplayServicesSetScreenBlanked
- _BKSDisplayServicesWillUnblank
- _OBJC_IVAR_$_BLSHBacklightDisplayStateMachine._lock_updatingCA
- _OBJC_IVAR_$_BLSHBacklightDisplayStateMachine._lock_updatingCA_startTimestamp
- _OBJC_IVAR_$_BLSHBacklightDisplayStateMachineAbortContext._backlightFactor
- _OBJC_IVAR_$_BLSHBacklightDisplayStateMachineAbortContext._displayIsOff
- _OBJC_IVAR_$_BLSHBacklightDisplayStateMachineAbortContext._isCABlanked
- _OBJC_IVAR_$_BLSHBacklightDisplayStateMachineAbortContext._isFlipbookEnabled
- _OBJC_IVAR_$_BLSHBacklightDisplayStateMachineAbortContext._transitioningToDisplayMode
- _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._cbDisplayStateDelegate
- _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._lock_caBlanked
- _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._lock_caFlipbookEnabled
- _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._lock_caFlipbookSuppressed
- _OBJC_IVAR_$_BLSHEnvironmentTransitionStateTarget._backlightRampBlock
- _OBJC_IVAR_$_BLSHEnvironmentTransitionStateTarget._lock
- _OBJC_IVAR_$_BLSHEnvironmentTransitionStateTarget._lock_performedBacklightRamp
- _OBJC_IVAR_$_BLSHOSInterfaceProviderAbortContext._caBlanked
- _OBJC_IVAR_$_BLSHOSInterfaceProviderAbortContext._caFlipbookEnabled
- _OBJC_IVAR_$_BLSHOSInterfaceProviderAbortContext._caFlipbookSuppressed
- __OBJC_$_PROP_LIST_BLSHFlipbook.81
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BLSCBDisplayStateDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_BLSCBDisplayStateDelegate
- __OBJC_$_PROTOCOL_REFS_BLSCBDisplayStateDelegate
- __OBJC_LABEL_PROTOCOL_$_BLSCBDisplayStateDelegate
- __OBJC_PROTOCOL_$_BLSCBDisplayStateDelegate
- ___101-[BLSHBacklightDisplayStateMachine osInterfaceProvider:didCompleteTransitionToDisplayMode:withError:]_block_invoke
- ___102-[BLSHBacklightEnvironmentStateMachine transitionState:didCompleteUpdateToBacklightState:visualState:]_block_invoke.138
- ___118-[BLSHLocalHostSceneEnvironment requestDateSpecifiersForDateInterval:previousPresentationDate:shouldReset:completion:]_block_invoke_3
- ___142-[BLSHEnvironmentTransitionState updateToTarget:forEvent:touchTargetable:presentationDate:sceneUpdate:requestedFidelity:performBacklightRamp:]_block_invoke
- ___142-[BLSHEnvironmentTransitionState updateToTarget:forEvent:touchTargetable:presentationDate:sceneUpdate:requestedFidelity:performBacklightRamp:]_block_invoke_2
- ___142-[BLSHEnvironmentTransitionState updateToTarget:forEvent:touchTargetable:presentationDate:sceneUpdate:requestedFidelity:performBacklightRamp:]_block_invoke_3
- ___74-[BLSHBacklightDisplayStateMachine onMain_performNextStepInModeTransition]_block_invoke
- ___74-[BLSHBacklightDisplayStateMachine onMain_performNextStepInModeTransition]_block_invoke.110
- ___74-[BLSHBacklightDisplayStateMachine onMain_performNextStepInModeTransition]_block_invoke_2
- ___74-[BLSHBacklightDisplayStateMachine onMain_performNextStepInModeTransition]_block_invoke_2.cold.1
- ___77-[BLSHEngineRenderFlipbookSession renderFrameSpecifier:timedOutEnvironments:]_block_invoke.514
- ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke.94
- ___89-[BLSHLocalHostSceneEnvironmentUpdater updatedEnvironmentWithDelta:backlightSceneUpdate:]_block_invoke.130
- ___89-[BLSHLocalHostSceneEnvironmentUpdater updatedEnvironmentWithDelta:backlightSceneUpdate:]_block_invoke.130.cold.1
- ___99-[BLSHBacklightDisplayStateMachine osInterfaceProvider:didCompleteSwitchToFlipbookState:withError:]_block_invoke
- ___block_descriptor_32_e34_16?0"BLSAlwaysOnTimelineEntry"8l
- ___block_descriptor_40_e8_32s_e29_16?0"BLSAlwaysOnTimeline"8ls32l8
- ___block_descriptor_46_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSArray"8ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e8_v16?0d8ls32l8s40l8s48l8s56l8
- ___block_descriptor_73_e8_32s40s48s56bs64w_e5_v8?0ls32l8s40l8s56l8s48l8w64l8
- ___block_descriptor_80_e8_32s40s48s56s64bs72w_e5_v8?0ls32l8s40l8w72l8s64l8s48l8s56l8
- ___block_descriptor_81_e8_32s40s48s56s64s72bs_e8_v16?0q8ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.114
- ___block_literal_global.118
- ___block_literal_global.137
- ___block_literal_global.505
- ___block_literal_global.634
- _objc_msgSend$backlightRampBlock
- _objc_msgSend$bs_flatten
- _objc_msgSend$cbDisplayStateDelegate
- _objc_msgSend$configuredEntriesForDateInterval:previousEntry:shouldConstructStartEntry:
- _objc_msgSend$dispatchToMainQueueAfterSecondsDelay:identifier:block:
- _objc_msgSend$initWithDisplayMode:transitioningToDisplayMode:lastSteadyStateDisplayMode:isFlipbookEnabled:showingBlankingWindow:backlightFactor:isCABlanked:displayIsOff:sleepRequested:sleepImminent:timeInSleepImminent:hasEnsureFlipbookCurrent:
- _objc_msgSend$initWithSequenceID:backlightState:triggerEvent:backlightRampBlock:
- _objc_msgSend$initWithSequenceID:backlightState:visualState:presentationDate:triggerEvent:backlightRampBlock:
- _objc_msgSend$initWithWatchdogType:cbDisplayMode:cbFlipbookState:suppressionServiceActive:caFlipbookEnabled:caFlipbookSuppressed:caBlanked:flipbookTransparent:deviceSupportsAlwaysOn:kernelSpecialMode:displayStateClientSupported:backlightDimmedFactor:
- _objc_msgSend$isCABlanked
- _objc_msgSend$isCAFlipbookEnabled
- _objc_msgSend$isCAFlipbookSuppressed
- _objc_msgSend$osInterfaceProvider:didCompleteSwitchToFlipbookState:withError:
- _objc_msgSend$osInterfaceProvider:didCompleteTransitionToDisplayMode:withError:
- _objc_msgSend$setAndTestDidPerformBacklightRamp
- _objc_msgSend$setCABlanked:
- _objc_msgSend$setCAFlipbookEnabled:
- _objc_msgSend$setCAFlipbookSuppressed:
- _objc_msgSend$setCBDisplayStateDelegate:
- _objc_msgSend$willUnblank
CStrings:
+ "\x01\x11\xf0\xe1"
+ "\nqA"
+ "%@, targetDisplayIsOff = %u, but %@ != {CADisplayStateFlipBookSuppressed || CADisplayStateOff}"
+ "@\"<BLSCADisplayPowerAssertion>\""
+ "@\"<BLSCADisplayPowerAssertion>\"24@0:8q16"
+ "@\"<BLSDisplayStateDelegate>\""
+ "@\"<BLSDisplayStateDelegate>\"16@0:8"
+ "@\"BLSHPendingBacklightRamp\""
+ "@\"CADisplayStateControl\""
+ "@16@?0@\"BLSAlwaysOnFrameSpecifier\"8"
+ "@64@0:8Q16q24@32@40@48@56"
+ "@64@0:8Q16q24@32@?40@48@56"
+ "@80@0:8Q16q24q32q40q48B56B60B64B68B72f76"
+ "@80@0:8q16q24q32q40q48B56B60B64d68B76"
+ "B24@0:8d16"
+ "BLSDisplayStateDelegate"
+ "BLSHPendingBacklightRamp"
+ "CADisplayStateControl nil - this process needs entitlement: 'com.apple.QuartzCore.display-state'"
+ "DSM:%p (completed except CB target:%{public}@) waited %lfs for CB callback to cbDisplayMode:%{public}@->%{public}@"
+ "DSM:%p (likely initialization) core animation completed(%{public}@) switch to display state:%{public}@ currentState:%{public}@"
+ "DSM:%p (pending change flipbook state for %{public}@) still waiting to update CA to %@ (waited %lfs)"
+ "DSM:%p (pending change flipbook state for %{public}@) waited %lfs for CB callback to cbDisplayMode:%{public}@->%{public}@"
+ "DSM:%p core animation completed transition to display state:%{public}@ (currentState:%{public}@) elapsed:%lfs"
+ "DSM:%p core animation completed transition to wrong display state:%{public}@ (currentState:%{public}@), waiting for display state:%{public}@ phase:%u elapsed:%lfs"
+ "DSM:%p core animation completed(%{public}@) transition to matching display state:%{public}@, (currentState:%{public}@), but operation is not started"
+ "DSM:%p core animation reporting interrupted transition to display state:%{public}@, current display state:%{public}@ – pending transition to display state:%{public}@ phase:%u elapsed:%lfs"
+ "DSM:%p core animation state transition status:%@ to display state:%{public}@, current display state:%{public}@ – pending transition to display state:%{public}@ phase:%u elapsed:%lfs"
+ "DSM:%p prewarmForDisplayMode:%{public}@->%{public}@%s previousPrewarm:%{public}@ hasAssertion:%{BOOL}u isPrewarmOn:%{BOOL}u requiresModeChange:%{BOOL}u shouldSignalPowerOn:%{BOOL}u shouldCleanup:%{BOOL}u cbDisplayMode:%{public}@"
+ "DSM:%p replacing pending switch to caDisplayState:%{public}@ from %lfs ago with switch to caDisplayState:%{public}@"
+ "DSM:%p waiting to update CA to %@ (waited %lfs)"
+ "ETS:%p:%{public}@ (%@) did perform backlightRamp duration:%.2f to target:%{public}@ "
+ "ETS:%p:%{public}@ target:%{public}@ snapped because client failed to perform backlight ramp for event:%{public}@"
+ "Notify"
+ "OSIP:%p %sBacklightFactor:%f WithFadeDuration:%fs"
+ "OSIP:%p completed(%d) setFlipbookTransparent:%{BOOL}u"
+ "OSIP:%p completed(%d) transitionToDisplayState:%{public}@"
+ "OSIP:%p flipbook no longer transparent, will transition to real flipbook"
+ "OSIP:%p flipbook set transparent, will transition to active"
+ "OSIP:%p flipbook transparent, will transition to CADisplayStateOn not CADisplayStateFlipBook"
+ "OSIP:%p transitionToCADisplayState:%{public}@"
+ "Set"
+ "T@\"<BLSDisplayStateDelegate>\",&,SsetDisplayStateDelegate:"
+ "T@\"<BLSDisplayStateDelegate>\",&,SsetDisplayStateDelegate:,V_displayStateDelegate"
+ "T@\"<BLSHFlipbookTelemetry>\",?,R,N"
+ "T@\"BLSHFlipbookSpecification\",?,R,N"
+ "T@\"BLSHPendingBacklightRamp\",R,N,V_pendingBacklightRamp"
+ "T@\"NSString\",?,R,C"
+ "TB,?,R,GisLocal"
+ "TB,?,R,N"
+ "TB,?,R,N,GisAlwaysOnEnabled"
+ "TB,?,R,N,GisTesting"
+ "TB,?,R,N,GisUsingAlwaysOnBrightnessCurve"
+ "TI,?,R,N"
+ "Td,?,N"
+ "Td,?,R,N"
+ "Td,?,R,N,V_backlightDimmingDuration"
+ "Tf,?,R,N"
+ "Tf,?,R,N,V_backlightDimmedFactor"
+ "Tr^v,?,R,N"
+ "_caDisplayState"
+ "_completedCADisplayState"
+ "_displayStateControl"
+ "_displayStateDelegate"
+ "_lock_backlightRampBlock"
+ "_lock_caDisplayPowerAssertion"
+ "_lock_caDisplayState"
+ "_lock_caDisplayStateChangeOperation"
+ "_lock_completedCADisplayState"
+ "_lock_notifiedCADisplayState"
+ "_pendingBacklightRamp"
+ "_prewarmingDisplayMode"
+ "acquire"
+ "acquireDisplayPowerAssertionForReason:"
+ "backlightRamp"
+ "caDisplayPowerState"
+ "caDisplayState"
+ "completedCADisplayState"
+ "constructFrameSpecifiersForTimelines:dateInterval:shouldConstructStartSpecifier:framesPerSecond:previousSpecifier:"
+ "createPowerAssertionWithReason:identifier:"
+ "displayState"
+ "displayStateDelegate"
+ "hasPendingBacklightRamp"
+ "hasPendingRamp"
+ "initWithBacklightRampBlock:"
+ "initWithDisplayMode:prewarmingDisplayMode:lastSteadyStateDisplayMode:caDisplayState:cbDisplayMode:showingBlankingWindow:sleepRequested:sleepImminent:timeInSleepImminent:hasEnsureFlipbookCurrent:"
+ "initWithSequenceID:backlightState:triggerEvent:backlightRampBlock:forIdentifier:previousTarget:"
+ "initWithSequenceID:backlightState:visualState:presentationDate:triggerEvent:pendingBacklightRamp:"
+ "initWithWatchdogType:cbDisplayMode:cbFlipbookState:caDisplayState:completedCADisplayState:suppressionServiceActive:flipbookTransparent:deviceSupportsAlwaysOn:kernelSpecialMode:displayStateClientSupported:backlightDimmedFactor:"
+ "osInterfaceProvider:didCompleteSwitchToCBFlipbookState:withError:"
+ "osInterfaceProvider:didCompleteTransitionToCADisplayState:currentState:transitionStatus:"
+ "osInterfaceProvider:didCompleteTransitionToCBDisplayMode:withError:"
+ "pendingBacklightRamp"
+ "pendingCADisplayState"
+ "pendingRamp"
+ "performBacklightRampIfNeededWithDuration:"
+ "performBacklightRampIfPendingForReason:"
+ "powerState"
+ "removed"
+ "setDisplayStateDelegate:"
+ "stateControl"
+ "transitionToCADisplayState:"
+ "transitionToDisplayState:withCompletion:"
+ "updateToTarget:touchTargetable:presentationDate:sceneUpdate:requestedFidelity:"
+ "v24@0:8@\"<BLSDisplayStateDelegate>\"16"
+ "v24@?0q8q16"
+ "v48@0:8@\"<BLSHBacklightOSInterfaceProviding>\"16q24q32q40"
+ "v48@0:8@16q24q32q40"
+ "{?=\"sequenceNumber\"i\"caDisplayState\"q\"phase\"q\"startTimestamp\"Q}"
+ "\xf0\xf0a"
- "\tQA"
- "@\"<BLSCBDisplayStateDelegate>\""
- "@\"<BLSCBDisplayStateDelegate>\"16@0:8"
- "@16@?0@\"BLSAlwaysOnTimeline\"8"
- "@16@?0@\"BLSAlwaysOnTimelineEntry\"8"
- "@48@0:8Q16q24@32@?40"
- "@64@0:8Q16q24@32@40@48@?56"
- "@76@0:8Q16q24q32B40B44B48B52B56B60B64B68f72"
- "@84@0:8q16q24q32B40B44q48B56B60B64B68d72B80"
- "@?16@0:8"
- "BLSCBDisplayStateDelegate"
- "DSM:%p did wait 35ms to update CA"
- "DSM:%p prewarmForDisplayMode:%{public}@->%{public}@%s previousPrewarm:%{public}@ requiresModeChange:%{BOOL}u shouldSignalPowerOn:%{BOOL}u shouldCleanup:%{BOOL}u cbDisplayMode:%{public}@"
- "DSM:%p still waiting 35ms to update CA (waited %lfs)"
- "DSM:%p waiting to complete transition to cbDisplayMode:%{public}@"
- "DSM:WaitForCA"
- "ETS:%p:%{public}@ target:%{public}@ failed to perform backlight ramp for event:%{public}@"
- "OSIP:%p SetBacklightFactor:%f WithFadeDuration:%fs"
- "OSIP:%p flipbook no longer transparent, will blank"
- "OSIP:%p flipbook set transparent, will unblank"
- "OSIP:%p flipbook transparent, will not blank"
- "OSIP:%p set ca blanked:%{BOOL}u"
- "OSIP:%p set ca flipbook enabled:%{BOOL}u"
- "OSIP:%p set ca flipbook suppressed:%{BOOL}u"
- "T@\"<BLSCBDisplayStateDelegate>\",&,SsetCBDisplayStateDelegate:"
- "T@\"<BLSCBDisplayStateDelegate>\",&,SsetCBDisplayStateDelegate:,V_cbDisplayStateDelegate"
- "T@\"<BLSHFlipbookTelemetry>\",R,N"
- "T@\"BLSHFlipbookSpecification\",R,N"
- "T@?,R,C,N,V_backlightRampBlock"
- "TB,N,GisCABlanked,SsetCABlanked:"
- "TB,N,GisCAFlipbookEnabled,SsetCAFlipbookEnabled:"
- "TB,N,GisCAFlipbookSuppressed,SsetCAFlipbookSuppressed:"
- "TB,R,GisLocal"
- "TB,R,N,GisTesting"
- "TB,R,N,GisUsingAlwaysOnBrightnessCurve"
- "Td,R,N,V_backlightDimmingDuration"
- "Tf,R,N,V_backlightDimmedFactor"
- "Tr^v,R,N"
- "_backlightFactor"
- "_backlightRampBlock"
- "_caBlanked"
- "_caFlipbookEnabled"
- "_caFlipbookSuppressed"
- "_cbDisplayStateDelegate"
- "_displayIsOff"
- "_isCABlanked"
- "_isFlipbookEnabled"
- "_lock_caBlanked"
- "_lock_caFlipbookEnabled"
- "_lock_caFlipbookSuppressed"
- "_lock_performedBacklightRamp"
- "_lock_updatingCA"
- "_lock_updatingCA_startTimestamp"
- "_transitioningToDisplayMode"
- "backlightFactor"
- "backlightRampBlock"
- "bs_flatten"
- "caBlanked"
- "caFlipbookEnabled"
- "caFlipbookSuppressed"
- "cbDisplayStateDelegate"
- "configuredEntriesForDateInterval:previousEntry:shouldConstructStartEntry:"
- "displayIsOff"
- "initWithDisplayMode:transitioningToDisplayMode:lastSteadyStateDisplayMode:isFlipbookEnabled:showingBlankingWindow:backlightFactor:isCABlanked:displayIsOff:sleepRequested:sleepImminent:timeInSleepImminent:hasEnsureFlipbookCurrent:"
- "initWithSequenceID:backlightState:triggerEvent:backlightRampBlock:"
- "initWithSequenceID:backlightState:visualState:presentationDate:triggerEvent:backlightRampBlock:"
- "initWithWatchdogType:cbDisplayMode:cbFlipbookState:suppressionServiceActive:caFlipbookEnabled:caFlipbookSuppressed:caBlanked:flipbookTransparent:deviceSupportsAlwaysOn:kernelSpecialMode:displayStateClientSupported:backlightDimmedFactor:"
- "isCABlanked"
- "isCAFlipbookEnabled"
- "isCAFlipbookSuppressed"
- "isFlipbookEnabled"
- "isFlipbookSuppressed"
- "osInterfaceProvider:didCompleteSwitchToFlipbookState:withError:"
- "osInterfaceProvider:didCompleteTransitionToDisplayMode:withError:"
- "setAndTestDidPerformBacklightRamp"
- "setCABlanked:"
- "setCAFlipbookEnabled:"
- "setCAFlipbookSuppressed:"
- "setCBDisplayStateDelegate:"
- "updateToTarget:forEvent:touchTargetable:presentationDate:sceneUpdate:requestedFidelity:performBacklightRamp:"
- "v24@0:8@\"<BLSCBDisplayStateDelegate>\"16"
- "willUnblank"
- "\xf0\xf0\x11"

```
