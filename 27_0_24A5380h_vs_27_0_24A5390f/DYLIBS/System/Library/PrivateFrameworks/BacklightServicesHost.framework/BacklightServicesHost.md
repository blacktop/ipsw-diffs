## BacklightServicesHost

> `/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_floatobj`

```diff

-6.0.36.0.0
-  __TEXT.__text: 0x9a7b0
-  __TEXT.__objc_methlist: 0x9c74
+6.0.38.0.0
+  __TEXT.__text: 0x9b29c
+  __TEXT.__objc_methlist: 0x9d1c
   __TEXT.__const: 0x4a0
   __TEXT.__gcc_except_tab: 0xf18
-  __TEXT.__cstring: 0x7cfb
-  __TEXT.__oslogstring: 0x1289d
+  __TEXT.__cstring: 0x7e30
+  __TEXT.__oslogstring: 0x129e6
   __TEXT.__ustring: 0x570
-  __TEXT.__unwind_info: 0x2818
+  __TEXT.__unwind_info: 0x2860
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2cc8
+  __DATA_CONST.__const: 0x2d90
   __DATA_CONST.__objc_classlist: 0x638
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x300
+  __DATA_CONST.__objc_protolist: 0x308
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3bf0
+  __DATA_CONST.__objc_selrefs: 0x3c28
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x518
   __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__got: 0x820
   __AUTH_CONST.__const: 0xd00
   __AUTH_CONST.__cfstring: 0x7c80
-  __AUTH_CONST.__objc_const: 0x19048
+  __AUTH_CONST.__objc_const: 0x190f8
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x11d0
-  __DATA.__objc_ivar: 0x12dc
-  __DATA.__data: 0x2400
-  __DATA.__bss: 0xf0
-  __DATA_DIRTY.__objc_data: 0x2c60
-  __DATA_DIRTY.__bss: 0x110
+  __DATA.__objc_ivar: 0x12e0
+  __DATA.__data: 0x2460
+  __DATA.__bss: 0xe0
+  __DATA_DIRTY.__objc_data: 0x3e30
+  __DATA_DIRTY.__bss: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 4204
-  Symbols:   9050
-  CStrings:  1982
+  Functions: 4227
+  Symbols:   9089
+  CStrings:  1989
 
Symbols:
+ -[BLSHAggregateBacklightHost internalTelemetryDelegate]
+ -[BLSHAggregateBacklightHost setInternalTelemetryDelegate:]
+ -[BLSHAlwaysOnPresentationEngine _lock_shouldUseLowPowerRenderingForPresentation:]
+ -[BLSHAlwaysOnPresentationEngine _lock_updateLowPowerRendering:]
+ -[BLSHAlwaysOnPresentationEngine hostEnvironment:hostDidSetLowPowerRenderingRequested:]
+ -[BLSHAlwaysOnPresentationEngine inactiveEnvironmentSession:willUpdateToPresentation:]
+ -[BLSHAlwaysOnPresentationEngine isLowPowerRendering]
+ -[BLSHBacklightEnvironmentPresentation wantsLowPowerRendering]
+ -[BLSHBacklightEnvironmentStateMachine _lock_isLowPowerRendering]
+ -[BLSHBacklightEnvironmentStateMachine isLowPowerRendering]
+ -[BLSHBacklightFBSceneHostEnvironment clientSupportsLowPowerRendering]
+ -[BLSHBacklightFBSceneHostEnvironment isLowPowerRenderingRequested]
+ -[BLSHBacklightFBSceneHostEnvironment setLowPowerRenderingRequested:]
+ -[BLSHBacklightFBSceneHostEnvironment updateToDateSpecifier:lowPowerRendering:sceneContentsUpdated:]
+ -[BLSHBacklightStateMachine internalTelemetryDelegate]
+ -[BLSHBacklightStateMachine notifyTelemetryDelegatesWithBlock:]
+ -[BLSHBacklightStateMachine setInternalTelemetryDelegate:]
+ -[BLSHBacklightTransitionStateMachine isLowPowerRendering]
+ -[BLSHBacklightWakeTelemetryTracker didUnblankForEvents:]
+ -[BLSHBaseSceneHostEnvironment clientSupportsLowPowerRendering]
+ -[BLSHBaseSceneHostEnvironment isLowPowerRenderingRequested]
+ -[BLSHBaseSceneHostEnvironment setLowPowerRenderingRequested:]
+ -[BLSHBaseSceneHostEnvironment updateToDateSpecifier:lowPowerRendering:sceneContentsUpdated:]
+ -[BLSHDisplayWakeTelemetry backlightTelemetrySource:didUnblankToDisplayMode:fromDisplayMode:activeEvents:abortedEvents:]
+ -[BLSHEnvironmentTransitionState isUpdatedToBacklightState:lowPowerRendering:]
+ -[BLSHEnvironmentTransitionState visualStateForBacklightState:requestedFidelity:lowPowerRendering:]
+ -[BLSHLocalHostSceneEnvironment updateToDateSpecifier:lowPowerRendering:sceneContentsUpdated:]
+ GCC_except_table149
+ GCC_except_table150
+ GCC_except_table43
+ GCC_except_table76
+ GCC_except_table84
+ GCC_except_table91
+ GCC_except_table93
+ _BLSClientSupportsLowPowerRenderingForEnvironment
+ _BLSHUpdateEnvironmentToDateSpecifier
+ _BLSIsLowPowerRenderingRequestedForEnvironment
+ _OBJC_IVAR_$_BLSHAlwaysOnPresentationEngine._lock_flipbookWillUseLowPowerRendering
+ _OBJC_IVAR_$_BLSHAlwaysOnPresentationEngine._lock_flipbookWillUseLowPowerRenderingDisabled
+ _OBJC_IVAR_$_BLSHBacklightFBSceneHostEnvironment._lock_lowPowerRenderingRequested
+ _OBJC_IVAR_$_BLSHBacklightStateMachine._internalTelemetryDelegate
+ _OBJC_IVAR_$_BLSHBaseSceneHostEnvironment._lock_lowPowerRenderingRequested
+ _PLLogRegisteredEvent
+ __OBJC_$_PROP_LIST_BLSHBacklightHostInternalTelemetrySource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BLSHBacklightHostInternalTelemetrySource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSHBacklightHostInternalTelemetrySource
+ __OBJC_$_PROTOCOL_REFS_BLSHBacklightHostInternalTelemetrySource
+ __OBJC_LABEL_PROTOCOL_$_BLSHBacklightHostInternalTelemetrySource
+ __OBJC_PROTOCOL_$_BLSHBacklightHostInternalTelemetrySource
+ ___100-[BLSHBacklightFBSceneHostEnvironment updateToDateSpecifier:lowPowerRendering:sceneContentsUpdated:]_block_invoke
+ ___105-[BLSHBacklightStateMachine backlight:didUpdateToDisplayMode:fromDisplayMode:activeEvents:abortedEvents:]_block_invoke_2
+ ___111-[BLSHBacklightStateMachine backlight:didUpdateVisualContentsToBeginTransitionToState:forEvents:abortedEvents:]_block_invoke_2
+ ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke_5
+ ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke_6
+ ___59-[BLSHBacklightInactiveEnvironmentSession setPresentation:]_block_invoke_3
+ ___62-[BLSHBaseSceneHostEnvironment setLowPowerRenderingRequested:]_block_invoke
+ ___69-[BLSHBacklightFBSceneHostEnvironment setLowPowerRenderingRequested:]_block_invoke
+ ___88-[BLSHBacklightStateMachine backlight:didCompleteUpdateToState:forEvents:abortedEvents:]_block_invoke_2
+ ___94-[BLSHLocalHostSceneEnvironment updateToDateSpecifier:lowPowerRendering:sceneContentsUpdated:]_block_invoke
+ ___96-[BLSHBacklightStateMachine backlight:didCompleteUpdateToFlipbookState:forEvents:abortedEvents:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40s_e46_v16?0"<BLSHBacklightHostTelemetryDelegate>"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e46_v16?0"<BLSHBacklightHostTelemetryDelegate>"8ls32l8s40l8
+ ___block_descriptor_65_e8_32s40s48s56s_e46_v16?0"<BLSHBacklightHostTelemetryDelegate>"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s_e46_v16?0"<BLSHBacklightHostTelemetryDelegate>"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_81_e8_32s40s48s56s_e46_v16?0"<BLSHBacklightHostTelemetryDelegate>"8ls32l8s40l8s48l8s56l8
+ _objc_msgSend$bls_supportsLowPowerRendering
+ _objc_msgSend$clientSupportsLowPowerRendering
+ _objc_msgSend$didUnblankForEvents:
+ _objc_msgSend$hostEnvironment:hostDidSetLowPowerRenderingRequested:
+ _objc_msgSend$inactiveEnvironmentSession:willUpdateToPresentation:
+ _objc_msgSend$internalTelemetryDelegate
+ _objc_msgSend$isLowPowerRenderingRequested
+ _objc_msgSend$isUpdatedToBacklightState:lowPowerRendering:
+ _objc_msgSend$setInternalTelemetryDelegate:
+ _objc_msgSend$setLowPowerRenderingRequested:
+ _objc_msgSend$updateToDateSpecifier:lowPowerRendering:sceneContentsUpdated:
+ _objc_msgSend$wantsLowPowerRendering
+ _objc_release_x3
- -[BLSHAlwaysOnPresentationEngine _lock_updateLowPowerRenderingFromPresentation:]
- -[BLSHAlwaysOnPresentationEngine hostEnvironment:hostDidSetLowPowerRendering:]
- -[BLSHBacklightEnvironmentPresentation isLowPowerRendering]
- -[BLSHBacklightEnvironmentStateMachine _lock_isLowPowerRenderingDisabled]
- -[BLSHBacklightEnvironmentStateMachine isLowPowerRenderingDisabled]
- -[BLSHBacklightFBSceneHostEnvironment isLowPowerRendering]
- -[BLSHBacklightFBSceneHostEnvironment setLowPowerRendering:]
- -[BLSHBacklightFBSceneHostEnvironment updateToDateSpecifier:sceneContentsUpdated:lowPowerRenderingDisabled:]
- -[BLSHBacklightTransitionStateMachine isLowPowerRenderingDisabled]
- -[BLSHBacklightWakeTelemetryTracker didUnblankForEvent:]
- -[BLSHBaseSceneHostEnvironment isLowPowerRendering]
- -[BLSHBaseSceneHostEnvironment setLowPowerRendering:]
- -[BLSHBaseSceneHostEnvironment updateToDateSpecifier:sceneContentsUpdated:lowPowerRenderingDisabled:]
- -[BLSHDisplayWakeTelemetry backlightTelemetrySource:didUnblankToDisplayMode:forEvents:abortedEvents:]
- -[BLSHEnvironmentTransitionState isUpdatedToBacklightState:lowPowerRenderingDisabled:]
- -[BLSHEnvironmentTransitionState visualStateForBacklightState:requestedFidelity:lowPowerRenderingDisabled:]
- -[BLSHLocalHostSceneEnvironment updateToDateSpecifier:sceneContentsUpdated:lowPowerRenderingDisabled:]
- GCC_except_table146
- GCC_except_table147
- GCC_except_table44
- GCC_except_table75
- GCC_except_table83
- GCC_except_table88
- GCC_except_table90
- _BLSIsLowPowerRenderingForEnvironment
- _OBJC_IVAR_$_BLSHAlwaysOnPresentationEngine._lock_lowPowerRendering
- _OBJC_IVAR_$_BLSHAlwaysOnPresentationEngine._lock_lowPowerRenderingDisabled
- _OBJC_IVAR_$_BLSHBacklightFBSceneHostEnvironment._lock_lowPowerRendering
- _OBJC_IVAR_$_BLSHBaseSceneHostEnvironment._lock_lowPowerRendering
- ___101-[BLSHDisplayWakeTelemetry backlightTelemetrySource:didUnblankToDisplayMode:forEvents:abortedEvents:]_block_invoke
- ___102-[BLSHLocalHostSceneEnvironment updateToDateSpecifier:sceneContentsUpdated:lowPowerRenderingDisabled:]_block_invoke
- ___108-[BLSHBacklightFBSceneHostEnvironment updateToDateSpecifier:sceneContentsUpdated:lowPowerRenderingDisabled:]_block_invoke
- ___53-[BLSHBaseSceneHostEnvironment setLowPowerRendering:]_block_invoke
- ___60-[BLSHBacklightFBSceneHostEnvironment setLowPowerRendering:]_block_invoke
- _objc_msgSend$didUnblankForEvent:
- _objc_msgSend$hostEnvironment:hostDidSetLowPowerRendering:
- _objc_msgSend$isLowPowerRenderingDisabled
- _objc_msgSend$isUpdatedToBacklightState:lowPowerRenderingDisabled:
- _objc_msgSend$setTelemetryDelegate:
CStrings:
+ "%p class %@ does not respond to selector setLowPowerRenderingRequested:, cannot acquire assertion with BLSLowPowerRenderingAttribute : %@"
+ "%p class %@ does not respond to selector setLowPowerRenderingRequested:, cannot deactivate assertion with BLSLowPowerRenderingAttribute : %@"
+ "%p:%{public}@:%{public}@ updateLowPowerRendering newLPR:%{BOOL}u oldLPR:%{BOOL}u"
+ "%{public}@ does not implement updateToDateSpecifier:lowPowerRendering:sceneContentsUpdated: or legacy updateToDateSpecifier:sceneContentsUpdated:lowPowerRenderingDisabled:"
+ "-[BLSHEnvironmentTransitionState updateToTarget:touchTargetable:presentationDate:sceneUpdate:requestedFidelity:]"
+ "-[BLSHEnvironmentTransitionState updateToTarget:touchTargetable:presentationDate:sceneUpdate:requestedFidelity:]_block_invoke"
+ "ETS:%p:%{public}@ updateToFlipbookVisualState:%{BOOL}u presentation date falling back to now:%{public}@ "
+ "[%d] WakeTelemetry didUnblank – shouldCapture:%{BOOL}u pending:%{BOOL}u commitPending:%{BOOL}u didMeasure:%{BOOL}u invalidated:%{BOOL}u events:%{public}@"
+ "didSetLowPowerRenderingRequested:%u"
+ "didUnblankToDisplayMode: %lu events succeeded, %lu events aborted (displayMode:%ld from:%ld)"
+ "incorrect usage - internal telemetry delegate should be set on a specific backlight host, not the aggregate one"
+ "incorrect usage - system shell should set telemetry delegate on a specific backlight host, not the aggregate one"
+ "target != nil"
+ "v16@?0@\"<BLSHBacklightHostTelemetryDelegate>\"8"
+ "\xf0\""
- "%p class %@ does not respond to selector setLowPowerRendering:, cannot acquire assertion with BLSLowPowerRenderingAttribute : %@"
- "%p class %@ does not respond to selector setLowPowerRendering:, cannot deactivate assertion with BLSLowPowerRenderingAttribute : %@"
- "%p:%{public}@:%{public}@ updateLowPowerRenderingFromPresentation newLPR:%{BOOL}u oldLPR:%{BOOL}u disabled:%{BOOL}u presentationLPR:%{BOOL}u presentation:%{public}@"
- "[%d] WakeTelemetry didUnblank – shouldCapture:%{BOOL}u pending:%{BOOL}u commitPending:%{BOOL}u didMeasure:%{BOOL}u invalidated:%{BOOL}u event:%{public}@"
- "didSetLowPowerRendering:%u"
- "didUnblankToDisplayMode: %lu events succeeded, %lu events aborted for state:%{public}@"
- "incorrect usage - system shell should set telemetry delegate on specific backlight host, not use the aggregate one"
- "\xf0!"
```
