## BacklightServicesHost

> `/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_floatobj`

```diff

-6.0.38.0.0
-  __TEXT.__text: 0x9b29c
-  __TEXT.__objc_methlist: 0x9d1c
-  __TEXT.__const: 0x4a0
-  __TEXT.__gcc_except_tab: 0xf18
-  __TEXT.__cstring: 0x7e30
-  __TEXT.__oslogstring: 0x129e6
+6.0.42.1.0
+  __TEXT.__text: 0x9c220
+  __TEXT.__objc_methlist: 0x9de4
+  __TEXT.__const: 0x488
+  __TEXT.__gcc_except_tab: 0xf10
+  __TEXT.__cstring: 0x7eaf
+  __TEXT.__oslogstring: 0x12edb
   __TEXT.__ustring: 0x570
-  __TEXT.__unwind_info: 0x2860
+  __TEXT.__unwind_info: 0x28c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2d90
-  __DATA_CONST.__objc_classlist: 0x638
+  __DATA_CONST.__const: 0x2e08
+  __DATA_CONST.__objc_classlist: 0x640
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x308
+  __DATA_CONST.__objc_protolist: 0x318
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3c28
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x518
   __DATA_CONST.__objc_arraydata: 0x78
-  __DATA_CONST.__got: 0x820
-  __AUTH_CONST.__const: 0xd00
-  __AUTH_CONST.__cfstring: 0x7c80
-  __AUTH_CONST.__objc_const: 0x190f8
+  __DATA_CONST.__got: 0x840
+  __AUTH_CONST.__const: 0xd40
+  __AUTH_CONST.__cfstring: 0x7d00
+  __AUTH_CONST.__objc_const: 0x19498
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x12e0
-  __DATA.__data: 0x2460
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x130c
+  __DATA.__data: 0x2520
   __DATA.__bss: 0xe0
-  __DATA_DIRTY.__objc_data: 0x3e30
+  __DATA_DIRTY.__objc_data: 0x3de0
   __DATA_DIRTY.__bss: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 4227
-  Symbols:   9089
-  CStrings:  1989
+  Functions: 4234
+  Symbols:   9145
+  CStrings:  2001
 
Symbols:
+ +[BLSHEnvironmentTransitionState createStateForEnvironment:delegate:displayFlipbookStateProvider:]
+ +[BLSHValidOnSystemSleepAttributeEntry activateForAttribute:fromAssertion:forService:attributeHandler:]
+ +[BLSHValidOnSystemSleepAttributeHandler attributeBaseClass]
+ +[BLSHValidOnSystemSleepAttributeHandler attributeClasses]
+ +[BLSHValidOnSystemSleepAttributeHandler entryClass]
+ -[BLSHAggregateBacklightHost settledBacklightState]
+ -[BLSHAggregateBacklightHost targetBacklightDisplayMode]
+ -[BLSHAlwaysOnPresentationEngine flipbookUsesLowPowerRendering]
+ -[BLSHAlwaysOnPresentationEngine main_updateFlipbookUsesLowPowerRendering:shouldInvalidateWhenChanged:reason:source:environment:]
+ -[BLSHAlwaysOnPresentationEngine updateFlipbookUsesLowPowerRendering:shouldInvalidateWhenChanged:reason:source:environment:]
+ -[BLSHBacklightEnvironmentStateMachine delegateLoggingName]
+ -[BLSHBacklightEnvironmentStateMachine initWithPresentation:backlightState:delegate:displayFlipbookStateProvider:inactiveBudgetPolicy:osTimerProvider:platformProvider:]
+ -[BLSHBacklightEnvironmentStateMachine onMain_updateToExplicitVisualState:specifier:]
+ -[BLSHBacklightEnvironmentStateMachine updateToExplicitVisualState:specifier:]
+ -[BLSHBacklightFBSceneHostEnvironment updateToPresentationDate:visualState:sceneContentsUpdated:]
+ -[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDate:]
+ -[BLSHBacklightOSTimerProvider bsContinuousMachTimeNow]
+ -[BLSHBacklightOSTimerProvider dateWithBSContinuousMachTime:]
+ -[BLSHBacklightStateMachine settledBacklightState]
+ -[BLSHBacklightStateMachine targetBacklightDisplayMode]
+ -[BLSHBacklightTransitionStateMachine delegateLoggingName]
+ -[BLSHBacklightTransitionStateMachine flipbookUsesLowPowerRendering]
+ -[BLSHBacklightTransitionStateMachine isFlipbook]
+ -[BLSHBacklightTransitionStateMachine settledBacklightState]
+ -[BLSHBacklightTransitionStateMachine targetBacklightDisplayMode]
+ -[BLSHBaseSceneHostEnvironment updateToPresentationDate:visualState:sceneContentsUpdated:]
+ -[BLSHBaseSceneHostEnvironment updateToVisualState:presentationDate:]
+ -[BLSHDisplayWakeTelemetry _donateBacklightStateChangeForState:startMachTime:endMachTime:changeEvent:]
+ -[BLSHEnvironmentTransitionState initWithEnvironment:delegate:displayFlipbookStateProvider:]
+ -[BLSHEnvironmentTransitionState updateToExplicitVisualState:dateSpecifier:]
+ -[BLSHEnvironmentTransitionStateTarget initWithSequenceID:backlightState:triggerEvent:backlightRampBlock:forIdentifier:displayLoggingName:previousTarget:]
+ -[BLSHInvalidOnSystemSleepAttributeEntry delayTimerIdentifier]
+ -[BLSHInvalidOnSystemSleepAttributeEntry handleSleepMonitorCompletion:]
+ -[BLSHInvalidOnSystemSleepAttributeEntry minimumActiveIntervalTimerFired]
+ -[BLSHLocalHostSceneEnvironment _lock_updateVisualState:]
+ -[BLSHLocalHostSceneEnvironment updateToPresentationDate:visualState:sceneContentsUpdated:]
+ -[BLSHLocalHostSceneEnvironmentUpdater delegateLoggingName]
+ -[BLSHLocalHostSceneEnvironmentUpdater flipbookUsesLowPowerRendering]
+ -[BLSHLocalHostSceneEnvironmentUpdater isFlipbook]
+ -[BLSHValidOnSystemSleepAttributeEntry .cxx_destruct]
+ -[BLSHValidOnSystemSleepAttributeEntry assertion]
+ -[BLSHValidOnSystemSleepAttributeEntry attribute]
+ -[BLSHValidOnSystemSleepAttributeEntry initForAttribute:fromAssertion:forService:]
+ -[BLSHValidOnSystemSleepAttributeEntry invalidate]
+ -[BLSHValidOnSystemSleepAttributeEntry reactivateIfPossible]
+ -[BLSHValidOnSystemSleepAttributeEntry service]
+ GCC_except_table148
+ GCC_except_table44
+ GCC_except_table75
+ _BLSHJSONStringForDictionary
+ _BLSHUpdateEnvironmentFlipbookUsesLowPowerRendering
+ _BLSHUpdateEnvironmentToExplicitVisualStateAndDate
+ _OBJC_CLASS_$_BLSHValidOnSystemSleepAttributeEntry
+ _OBJC_CLASS_$_BLSHValidOnSystemSleepAttributeHandler
+ _OBJC_CLASS_$_BLSValidOnSystemSleepAttribute
+ _OBJC_IVAR_$_BLSHAggregateBacklightHost._lock_alwaysOnEnabled
+ _OBJC_IVAR_$_BLSHAggregateBacklightHost._lock_backlightState
+ _OBJC_IVAR_$_BLSHAggregateBacklightHost._lock_displayMode
+ _OBJC_IVAR_$_BLSHAggregateBacklightHost._lock_flipbookState
+ _OBJC_IVAR_$_BLSHAggregateBacklightHost._lock_targetDisplayMode
+ _OBJC_IVAR_$_BLSHAggregateBacklightHost._lock_willTransitionBacklightState
+ _OBJC_IVAR_$_BLSHAlwaysOnPresentationEngine._lock_flipbookUsesLowPowerRendering
+ _OBJC_IVAR_$_BLSHAlwaysOnPresentationEngine._lock_lowPowerRenderingDisabled
+ _OBJC_IVAR_$_BLSHBacklightEnvironmentStateMachine._delegateLoggingName
+ _OBJC_IVAR_$_BLSHBacklightEnvironmentStateMachine._displayFlipbookStateProvider
+ _OBJC_IVAR_$_BLSHBacklightTransitionStateMachine._lock_settledBacklightState
+ _OBJC_IVAR_$_BLSHBaseBacklightEnvironmentSessionProvider._displayLoggingName
+ _OBJC_IVAR_$_BLSHEnvironmentTransitionState._delegateLoggingName
+ _OBJC_IVAR_$_BLSHEnvironmentTransitionState._displayFlipbookStateProvider
+ _OBJC_IVAR_$_BLSHInvalidOnSystemSleepAttributeEntry._activationDate
+ _OBJC_IVAR_$_BLSHInvalidOnSystemSleepAttributeEntry._lock_delayTimer
+ _OBJC_IVAR_$_BLSHInvalidOnSystemSleepAttributeEntry._lock_pendingSleepCompletion
+ _OBJC_IVAR_$_BLSHInvalidOnSystemSleepAttributeEntry._minimumActiveInterval
+ _OBJC_IVAR_$_BLSHValidOnSystemSleepAttributeEntry._assertion
+ _OBJC_IVAR_$_BLSHValidOnSystemSleepAttributeEntry._attribute
+ _OBJC_IVAR_$_BLSHValidOnSystemSleepAttributeEntry._service
+ _OBJC_METACLASS_$_BLSHValidOnSystemSleepAttributeEntry
+ _OBJC_METACLASS_$_BLSHValidOnSystemSleepAttributeHandler
+ _OUTLINED_FUNCTION_63
+ __OBJC_$_CLASS_METHODS_BLSHValidOnSystemSleepAttributeEntry
+ __OBJC_$_CLASS_METHODS_BLSHValidOnSystemSleepAttributeHandler
+ __OBJC_$_INSTANCE_METHODS_BLSHValidOnSystemSleepAttributeEntry
+ __OBJC_$_INSTANCE_VARIABLES_BLSHValidOnSystemSleepAttributeEntry
+ __OBJC_$_PROP_LIST_BLSHBacklightHostObservable_Private
+ __OBJC_$_PROP_LIST_BLSHDisplayFlipbookStateProvider
+ __OBJC_$_PROP_LIST_BLSHValidOnSystemSleepAttributeEntry
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BLSHBacklightHostObservable_Private
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BLSHDisplayFlipbookStateProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSHBacklightHostObservable_Private
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSHDisplayFlipbookStateProvider
+ __OBJC_$_PROTOCOL_REFS_BLSHBacklightHostObservable_Private
+ __OBJC_$_PROTOCOL_REFS_BLSHDisplayFlipbookStateProvider
+ __OBJC_CLASS_PROTOCOLS_$_BLSHValidOnSystemSleepAttributeEntry
+ __OBJC_CLASS_RO_$_BLSHValidOnSystemSleepAttributeEntry
+ __OBJC_CLASS_RO_$_BLSHValidOnSystemSleepAttributeHandler
+ __OBJC_LABEL_PROTOCOL_$_BLSHBacklightHostObservable_Private
+ __OBJC_LABEL_PROTOCOL_$_BLSHDisplayFlipbookStateProvider
+ __OBJC_METACLASS_RO_$_BLSHValidOnSystemSleepAttributeEntry
+ __OBJC_METACLASS_RO_$_BLSHValidOnSystemSleepAttributeHandler
+ __OBJC_PROTOCOL_$_BLSHBacklightHostObservable_Private
+ __OBJC_PROTOCOL_$_BLSHDisplayFlipbookStateProvider
+ ___102-[BLSHDisplayWakeTelemetry _donateBacklightStateChangeForState:startMachTime:endMachTime:changeEvent:]_block_invoke
+ ___124-[BLSHAlwaysOnPresentationEngine updateFlipbookUsesLowPowerRendering:shouldInvalidateWhenChanged:reason:source:environment:]_block_invoke
+ ___168-[BLSHBacklightEnvironmentStateMachine initWithPresentation:backlightState:delegate:displayFlipbookStateProvider:inactiveBudgetPolicy:osTimerProvider:platformProvider:]_block_invoke
+ ___71-[BLSHInvalidOnSystemSleepAttributeEntry handleSleepMonitorCompletion:]_block_invoke
+ ___76-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDate:]_block_invoke
+ ___76-[BLSHEnvironmentTransitionState updateToExplicitVisualState:dateSpecifier:]_block_invoke
+ ___78-[BLSHBacklightEnvironmentStateMachine updateToExplicitVisualState:specifier:]_block_invoke
+ ___85-[BLSHBacklightEnvironmentStateMachine onMain_updateToExplicitVisualState:specifier:]_block_invoke
+ ___85-[BLSHBacklightEnvironmentStateMachine onMain_updateToExplicitVisualState:specifier:]_block_invoke_2
+ ___85-[BLSHBacklightEnvironmentStateMachine onMain_updateToExplicitVisualState:specifier:]_block_invoke_3
+ ___86-[BLSHInvalidOnSystemSleepAttributeEntry systemSleepMonitor:sleepRequestedWithResult:]_block_invoke
+ ___91-[BLSHInvalidOnSystemSleepAttributeEntry systemSleepMonitor:prepareForSleepWithCompletion:]_block_invoke
+ ___91-[BLSHLocalHostSceneEnvironment updateToPresentationDate:visualState:sceneContentsUpdated:]_block_invoke
+ ___97-[BLSHBacklightFBSceneHostEnvironment updateToPresentationDate:visualState:sceneContentsUpdated:]_block_invoke
+ ___BLSHUpdateEnvironmentFlipbookUsesLowPowerRendering_block_invoke
+ ___block_descriptor_109_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_48_e8_32s40s_e80_v24?0"<BLSHBacklightSceneHostEnvironment>"8"BLSHEnvironmentTransitionState"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e33_v16?0"FBSMutableSceneSettings"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs_e37_v24?0"CAFlipBookFrame"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e17_v16?0"NSArray"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_66_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e31_16?0"BLSHPresentationEntry"8ls32l8r64l8r72l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e60_"FBSSceneTransitionContext"16?0"FBSMutableSceneSettings"8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_88_e8_32s40s48s56bs64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_96_e8_32s40s48s56s64s_e49_v24?0"<BLSHRenderedFlipbookFrame>"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
+ ___kCFBooleanTrue
+ _objc_msgSend$_donateBacklightStateChangeForState:startMachTime:endMachTime:changeEvent:
+ _objc_msgSend$_lock_updateVisualState:
+ _objc_msgSend$bsContinuousMachTimeNow
+ _objc_msgSend$createStateForEnvironment:delegate:displayFlipbookStateProvider:
+ _objc_msgSend$dateWithBSContinuousMachTime:
+ _objc_msgSend$delegateLoggingName
+ _objc_msgSend$flipbookUsesLowPowerRendering
+ _objc_msgSend$initWithPresentation:backlightState:delegate:displayFlipbookStateProvider:inactiveBudgetPolicy:osTimerProvider:platformProvider:
+ _objc_msgSend$initWithSequenceID:backlightState:triggerEvent:backlightRampBlock:forIdentifier:displayLoggingName:previousTarget:
+ _objc_msgSend$minimumActiveInterval
+ _objc_msgSend$newVisualStateWithFlipbookUsesLowPowerRendering:
+ _objc_msgSend$settledBacklightState
+ _objc_msgSend$targetBacklightDisplayMode
+ _objc_msgSend$updateToExplicitVisualState:dateSpecifier:
+ _objc_msgSend$updateToExplicitVisualState:specifier:
+ _objc_msgSend$updateToPresentationDate:visualState:sceneContentsUpdated:
+ _objc_msgSend$updateToVisualState:presentationDate:
- +[BLSHEnvironmentTransitionState createStateForEnvironment:delegate:]
- -[BLSHAggregateHostCachedState alwaysOnEnabled]
- -[BLSHAggregateHostCachedState backlightState]
- -[BLSHAggregateHostCachedState description]
- -[BLSHAggregateHostCachedState displayMode]
- -[BLSHAggregateHostCachedState flipbookState]
- -[BLSHAggregateHostCachedState initWithBacklightHost:]
- -[BLSHAggregateHostCachedState initWithBacklightState:displayMode:flipbookState:alwaysOnEnabled:]
- -[BLSHAggregateHostCachedState setAlwaysOnEnabled:]
- -[BLSHAggregateHostCachedState setBacklightState:]
- -[BLSHAggregateHostCachedState setDisplayMode:]
- -[BLSHAggregateHostCachedState setFlipbookState:]
- -[BLSHAggregateHostCachedState setTargetDisplayMode:]
- -[BLSHAggregateHostCachedState setWillTransitionBacklightState:]
- -[BLSHAggregateHostCachedState targetDisplayMode]
- -[BLSHAggregateHostCachedState willTransitionBacklightState]
- -[BLSHAlwaysOnPresentationEngine _lock_updateLowPowerRendering:]
- -[BLSHAlwaysOnPresentationEngine isLowPowerRendering]
- -[BLSHBacklightEnvironmentStateMachine _lock_isLowPowerRendering]
- -[BLSHBacklightEnvironmentStateMachine initWithPresentation:backlightState:delegate:inactiveBudgetPolicy:osTimerProvider:platformProvider:]
- -[BLSHBacklightEnvironmentStateMachine isLowPowerRendering]
- -[BLSHBacklightFBSceneHostEnvironment updateToDateSpecifier:lowPowerRendering:sceneContentsUpdated:]
- -[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:]
- -[BLSHBacklightTransitionStateMachine isLowPowerRendering]
- -[BLSHBacklightTransitionStateMachine presentationEngine:didChangeLowPowerRenderingDisabled:]
- -[BLSHBaseSceneHostEnvironment updateToDateSpecifier:lowPowerRendering:sceneContentsUpdated:]
- -[BLSHBaseSceneHostEnvironment updateToVisualState:presentationDateSpecifier:]
- -[BLSHEnvironmentTransitionState initWithEnvironment:delegate:]
- -[BLSHEnvironmentTransitionStateTarget initWithSequenceID:backlightState:triggerEvent:backlightRampBlock:forIdentifier:previousTarget:]
- -[BLSHLocalHostSceneEnvironment updateToDateSpecifier:lowPowerRendering:sceneContentsUpdated:]
- GCC_except_table150
- GCC_except_table43
- GCC_except_table69
- _OBJC_CLASS_$_BLSHAggregateHostCachedState
- _OBJC_IVAR_$_BLSHAggregateBacklightHost._lock_cachedState
- _OBJC_IVAR_$_BLSHAggregateBacklightHost._lock_cachedStatesByHost
- _OBJC_IVAR_$_BLSHAggregateHostCachedState._alwaysOnEnabled
- _OBJC_IVAR_$_BLSHAggregateHostCachedState._backlightState
- _OBJC_IVAR_$_BLSHAggregateHostCachedState._displayMode
- _OBJC_IVAR_$_BLSHAggregateHostCachedState._flipbookState
- _OBJC_IVAR_$_BLSHAggregateHostCachedState._targetDisplayMode
- _OBJC_IVAR_$_BLSHAggregateHostCachedState._willTransitionBacklightState
- _OBJC_IVAR_$_BLSHAlwaysOnPresentationEngine._lock_flipbookWillUseLowPowerRendering
- _OBJC_IVAR_$_BLSHAlwaysOnPresentationEngine._lock_flipbookWillUseLowPowerRenderingDisabled
- _OBJC_METACLASS_$_BLSHAggregateHostCachedState
- __OBJC_$_INSTANCE_METHODS_BLSHAggregateHostCachedState
- __OBJC_$_INSTANCE_VARIABLES_BLSHAggregateHostCachedState
- __OBJC_$_PROP_LIST_BLSHAggregateHostCachedState
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BLSHAlwaysOnPresentationEngineDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BLSHBacklightEnvironmentStateMachineDelegate
- __OBJC_CLASS_RO_$_BLSHAggregateHostCachedState
- __OBJC_METACLASS_RO_$_BLSHAggregateHostCachedState
- ___100-[BLSHBacklightFBSceneHostEnvironment updateToDateSpecifier:lowPowerRendering:sceneContentsUpdated:]_block_invoke
- ___139-[BLSHBacklightEnvironmentStateMachine initWithPresentation:backlightState:delegate:inactiveBudgetPolicy:osTimerProvider:platformProvider:]_block_invoke
- ___43-[BLSHAggregateHostCachedState description]_block_invoke
- ___43-[BLSHAggregateHostCachedState description]_block_invoke_2
- ___63-[BLSHAlwaysOnPresentationEngine setLowPowerRenderingDisabled:]_block_invoke
- ___63-[BLSHAlwaysOnPresentationEngine setLowPowerRenderingDisabled:]_block_invoke_2
- ___85-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:]_block_invoke
- ___93-[BLSHDisplayWakeTelemetry _logBacklightTelemetryEventForPendingEvent:duration:endTimestamp:]_block_invoke_2
- ___94-[BLSHLocalHostSceneEnvironment updateToDateSpecifier:lowPowerRendering:sceneContentsUpdated:]_block_invoke
- ___block_descriptor_117_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_56_e8_32s40bs_e37_v24?0"CAFlipBookFrame"8"NSError"16ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSArray"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56s_e33_v16?0"FBSMutableSceneSettings"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e31_16?0"BLSHPresentationEntry"8ls32l8r56l8r64l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48bs56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_88_e8_32s40s48s56s_e49_v24?0"<BLSHRenderedFlipbookFrame>"8"NSError"16ls32l8s40l8s48l8s56l8
- _objc_msgSend$alwaysOnEnabled
- _objc_msgSend$appendString:
- _objc_msgSend$changeEvent
- _objc_msgSend$createStateForEnvironment:delegate:
- _objc_msgSend$initWithBacklightHost:
- _objc_msgSend$initWithBacklightState:displayMode:flipbookState:alwaysOnEnabled:
- _objc_msgSend$initWithIsFlipbook:initialSpecifier:
- _objc_msgSend$initWithPresentation:backlightState:delegate:inactiveBudgetPolicy:osTimerProvider:platformProvider:
- _objc_msgSend$initWithSequenceID:backlightState:triggerEvent:backlightRampBlock:forIdentifier:previousTarget:
- _objc_msgSend$isLowPowerRendering
- _objc_msgSend$mapTableWithKeyOptions:valueOptions:
- _objc_msgSend$presentationEngine:didChangeLowPowerRenderingDisabled:
- _objc_msgSend$setAlwaysOnEnabled:
- _objc_msgSend$setDateSpecifier:
- _objc_msgSend$setFlipbookState:
- _objc_msgSend$setTargetDisplayMode:
- _objc_msgSend$setWillTransitionBacklightState:
- _objc_msgSend$updateToDateSpecifier:lowPowerRendering:sceneContentsUpdated:
- _objc_msgSend$updateToVisualState:presentationDateSpecifier:
- _objc_msgSend$willTransitionBacklightState
CStrings:
+ "%p (localHostUpdater) ESM update to visualState:%{public}@ dateSpecifier:%{public}@"
+ "%p:%{public}@ (localHostEnv) caller visualState:%{public}@ != clientEnvVisualState:%{public}@"
+ "%p:%{public}@ already at date:%{public}@ visualState:%{public}@ (calling through anyway)"
+ "%p:%{public}@ does not respond to selector updateToPresentationDate:visualState:sceneContentsUpdated: - cannot update flipbookUsesLowPowerRendering:%{BOOL}u"
+ "%p:%{public}@ in flipbook state when willUpdateToPresentation:%{public}@"
+ "%p:%{public}@ scene:%{public}@ already at dateSpecifier:%{public}@ visualState:%{public}@"
+ "%p:%{public}@:%{public}@ scheduling timer for %{public}@ (%lfs) nextsUpdateStart:%{public}@"
+ "%p:%{public}@:%{public}@ updateLowPowerRendering:%{public}@ newLPR:%{BOOL}u oldLPR:%{BOOL}u"
+ "BLSInvalidOnSystemSleep minimum active interval assertion:%@"
+ "ESM:%p:%{public}@ %s:%{public}@ for:%{public}@ %sets:%{public}@ ∂env:%d ∂begin:%{BOOL}u/%{BOOL}u ∂end:%{BOOL}u/%{BOOL}u ∂pres:%{BOOL}u/%{BOOL}u %{public}@ stale:%{BOOL}u"
+ "ESM:%p:%{public}@ %supdateTransitionStatesForEnvironments: -> %@ environment %@: %@"
+ "ESM:%p:%{public}@ (dropping didBeginUpdateToState callback) completedOperation:%{public}@ target:%{public}@ performEventTarget:%{public}@ updatingState:%{BOOL}u shouldNotifyUpdatedPresentation:%{BOOL}u shouldNotifyBegan:%{BOOL}u shouldNotifyCompleted:%{BOOL}u eventHistory:%{public}@ updateHistory:%{public}@"
+ "ESM:%p:%{public}@ (dropping didCompleteUpdateToState callback) completedOperation:%{public}@ target:%{public}@ performEventTarget:%{public}@ updatingState:%{BOOL}u shouldNotifyUpdatedPresentation:%{BOOL}u shouldNotifyBegan:%{BOOL}u shouldNotifyCompleted:%{BOOL}u eventHistory:%{public}@ updateHistory:%{public}@"
+ "ESM:%p:%{public}@ (finishing - %s) setPresentation:%p transitionStates:%{public}@"
+ "ESM:%p:%{public}@ (performEvent finishing - %s) performEvent:%{public}@ transitionStates:%{public}@ "
+ "ESM:%p:%{public}@ (stale) etsUpdateTo:%{public}@ for:%{public}@ ets:%{public}@"
+ "ESM:%p:%{public}@ calling performEvent on invalidated state machine:%{public}@ event:%{public}@ initialSpecifier:%{public}@"
+ "ESM:%p:%{public}@ calling setPresentation on invalidated state machine:%{public}@ presentation:%{public}@"
+ "ESM:%p:%{public}@ calling updateAllEnvironmentsInPresentation on invalidated state machine:%{public}@"
+ "ESM:%p:%{public}@ calling updateEnvironment on invalidated state machine:%{public}@ environment:%{public}@"
+ "ESM:%p:%{public}@ calling updateFlipbookVisualState on invalidated state machine:%{public}@"
+ "ESM:%p:%{public}@ checkFlipbookVisualStateCompletion (rdar://175348594) isBeginUpdate:%{BOOL}u transitionState:%{public}@ notInTrackingSet shouldComplete:%{BOOL}u remaining:%lu"
+ "ESM:%p:%{public}@ clearing flipbook/lowPowerRendering on removed environment:%{public}@ %{public}@ -> %{public}@"
+ "ESM:%p:%{public}@ completedOperation:%{public}@ target:%{public}@ performEventTarget:%{public}@ updatingState:%{BOOL}u shouldNotifyUpdatedPresentation:%{BOOL}u shouldNotifyBegan:%{BOOL}u shouldNotifyCompleted:%{BOOL}u, setPresentationOperation:%{public}@ eventHistory:%{public}@ updateHistory:%{public}@"
+ "ESM:%p:%{public}@ etsUpdateTo:%{public}@ dateMatch:%{BOOL}u for:%{public}@ ets:%{public}@"
+ "ESM:%p:%{public}@ finishing (immediate complete - update begin also) setPresentation:%{public}@"
+ "ESM:%p:%{public}@ finishing (immediate complete - update end also) setPresentation:%{public}@"
+ "ESM:%p:%{public}@ finishing (immediate complete) setPresentation:%{public}@"
+ "ESM:%p:%{public}@ finishing (performEvent immediate begin update) performEvent:%{public}@"
+ "ESM:%p:%{public}@ finishing (performEvent immediate complete) performEvent:%{public}@"
+ "ESM:%p:%{public}@ finishing (performEvent immediate setPresentation complete) performEvent:%{public}@"
+ "ESM:%p:%{public}@ flipbookVisualStateUpdateCompleted isFlipbook:%{BOOL}u specifier:%{public}@"
+ "ESM:%p:%{public}@ not will update environment:%{public}@ (unchanged) to backlightState:%{public}@ visualState:%{public}@"
+ "ESM:%p:%{public}@ performEvent: -> %@ environments:%@ event:%@"
+ "ESM:%p:%{public}@ removal— no longer active transitionState:%{public}@"
+ "ESM:%p:%{public}@ setPresentation (redundant) targetBacklightState:%{public}@"
+ "ESM:%p:%{public}@ setPresentation (redundant) targetBacklightState:%{public}@->%{public}@ additions:%{public}@"
+ "ESM:%p:%{public}@ setPresentation by adding:%{public}@ and removing:%{public}@ targetBacklightState:%{public}@"
+ "ESM:%p:%{public}@ setPresentation by adding:%{public}@ targetBacklightState:%{public}@"
+ "ESM:%p:%{public}@ setPresentation by removing:%{public}@ targetBacklightState:%{public}@"
+ "ESM:%p:%{public}@ setPresentation: -> %@ environments %@"
+ "ESM:%p:%{public}@ setPresentation: staleEnvironmentsThatNeedDeferredUpdate:%{public}@"
+ "ESM:%p:%{public}@ updateFlipbookVisualState:%{BOOL}u initialSpecifier:%{public}@ environments:%@ now:%{public}@"
+ "ESM:%p:%{public}@ updateRemovedEnvironmentsToActiveOn:%{public}@"
+ "ESM:%p:%{public}@ will not stop tracking transitionState:%{public}@ (isActiveTransitionState:%{BOOL}u)"
+ "ESM:%p:%{public}@ will not update environment:%{public}@ (not in presentation) to backlightState:%{public}@"
+ "ESM:%p:%{public}@ will skip environment update, no longer in presentation — updateTransitionStatesForReason:%{public}@ environment:%p:%{public}@"
+ "ESM:%p:%{public}@ will stop tracking transitionState:%{public}@"
+ "ESM:%p:%{public}@ will update environment:%{public}@ to backlightState:%{public}@ visualState:%{public}@"
+ "ESP:%p:%{public}@ createdInactiveEnvironmentSession:%p forDisplay:%{public}@ presentation:%{public}@"
+ "ESP:%p:%{public}@ didEndInactiveEnvironmentSession:%p isCurrentSession:%{BOOL}u"
+ "ESP:%p:%{public}@ initForDisplay"
+ "ESP:%p:%{public}@ session:%p didUpdateToPresentation:%{public}@ isCurrentSession:%{BOOL}u didCompleteSetPresentation:%{BOOL}u"
+ "ESP:%p:%{public}@ setPresentation:%{public}@ changed:%{BOOL}u waitForSession:%{BOOL}u session:%p"
+ "ETS:%p:%{public}@ client disabled:%p, pretending state matches:%{public}@"
+ "ETS:%p:%{public}@:%{public}@ (%@) did perform backlightRamp duration:%.2f to target:%{public}@ "
+ "ETS:%p:%{public}@:%{public}@ (now obsolete - will not call backlight ramp or animation completion) redundant update to target:%{public}@ wasUpdating:%{BOOL}u animated:%{BOOL}u hasBacklightRamp:%{BOOL}u event:%{public}@ touchTarget:%{BOOL}u oldInProgress:%{public}@ currentInProgress:%{public}@"
+ "ETS:%p:%{public}@:%{public}@ animationComplete to target:%{public}@ event:%{public}@ animated:%{BOOL}u inProgressUpdateTarget:%{public}@ requestingFidelityTarget:%{public}@"
+ "ETS:%p:%{public}@:%{public}@ did update to dateSpecifier:%{public}@"
+ "ETS:%p:%{public}@:%{public}@ did update to explicitVisualState:%{public}@ date:%{public}@"
+ "ETS:%p:%{public}@:%{public}@ redundant update to target:%{public}@ wasUpdating:%{BOOL}u animated:%{BOOL}u hasBacklightRamp:%{BOOL}u event:%{public}@ touchTarget:%{BOOL}u existingInProgress:%{public}@"
+ "ETS:%p:%{public}@:%{public}@ scene contents updated to target:%{public}@ event:%{public}@ animated:%{BOOL}u inProgressUpdateTarget:%{public}@ requestingFidelityTarget:%{public}@"
+ "ETS:%p:%{public}@:%{public}@ target:%{public}@ snapped because client failed to perform backlight ramp for event:%{public}@"
+ "ETS:%p:%{public}@:%{public}@ transitionState dealloc"
+ "ETS:%p:%{public}@:%{public}@ transitionState init"
+ "ETS:%p:%{public}@:%{public}@ update to dateSpecifier:%{public}@"
+ "ETS:%p:%{public}@:%{public}@ update to explicitVisualState:%{public}@ date:%{public}@"
+ "ETS:%p:%{public}@:%{public}@ update to state:%{public}@ – inheriting old backlight ramp existingInProgress:%{public}@ –\u00a0event:%{public}@"
+ "ETS:%p:%{public}@:%{public}@ update to state:%{public}@ – inheriting old triggerEvent existingInProgress:%{public}@ –\u00a0event:%{public}@"
+ "ETS:%p:%{public}@:%{public}@ updateToFlipbookVisualState:%{BOOL}u presentation date falling back to now:%{public}@ "
+ "ETS:%p:%{public}@:%{public}@ will skip update to oldTarget:%{public}@ was replaced with newPartialTarget:%{public}@ hadBacklightRamp:%{BOOL}u oldEvent:%{public}@ wouldTransitionHaveBeenNeeded:%{BOOL}U"
+ "ETS:%p:%{public}@:%{public}@ will update to target:%{public}@ wasUpdating:%{BOOL}u animated:%{BOOL}u hasBacklightRamp:%{BOOL}u event:%{public}@ touchTarget:%{BOOL}u lprTime:%llu"
+ "TSM:%p:%{public}@ (findNextOperation) no operation needed isBeforeDisplayBlankingChange:%{BOOL}u hasEvents:%{BOOL}u needFlipbookOff:%{BOOL}u"
+ "a\xf1"
+ "didUpdateToPresentation:%p"
+ "endSession"
+ "environment for later update must implement updateToVisualState:presentationDate: from BLSHBacklightSceneHostEnvironment_Private"
+ "localHost"
+ "newSession:%p"
+ "setLowPowerRenderingDisabled:%u"
+ "willUpdateToPresentation"
- "%p (localHostUpdater) calling [environmentStateMachine updateToSpecifier:], dateSpecifier:%{public}@"
- "%p:%{public}@ scene:%{public}@ already at dateSpecifier:%{public}@"
- "%p:%{public}@:%{public}@ scheduling timer for %{public}@ nextsUpdateStart:%{public}@"
- "%p:%{public}@:%{public}@ timer too soon (will just dispatch_async) for %{public}@ nextsUpdateStart:%{public}@"
- "%p:%{public}@:%{public}@ updateLowPowerRendering newLPR:%{BOOL}u oldLPR:%{BOOL}u"
- "%{public}@ does not implement updateToDateSpecifier:lowPowerRendering:sceneContentsUpdated: or legacy updateToDateSpecifier:sceneContentsUpdated:lowPowerRenderingDisabled:"
- "; "
- "BLSHAggregateBacklightHost.m"
- "ESM: %supdateTransitionStatesForEnvironments: -> %@ environment %@: %@"
- "ESM: performEvent: -> %@ environments:%@ event:%@"
- "ESM: setPresentation: -> %@ environments %@"
- "ESM: updateRemovedEnvironmentsToActiveOn:%{public}@"
- "ESM:%p %s:%{public}@ for:%{public}@ %sets:%{public}@ ∂env:%d ∂begin:%{BOOL}u/%{BOOL}u ∂end:%{BOOL}u/%{BOOL}u ∂pres:%{BOOL}u/%{BOOL}u %{public}@ stale:%{BOOL}u"
- "ESM:%p (dropping didBeginUpdateToState callback) completedOperation:%{public}@ target:%{public}@ performEventTarget:%{public}@ updatingState:%{BOOL}u shouldNotifyUpdatedPresentation:%{BOOL}u shouldNotifyBegan:%{BOOL}u shouldNotifyCompleted:%{BOOL}u eventHistory:%{public}@ updateHistory:%{public}@"
- "ESM:%p (dropping didCompleteUpdateToState callback) completedOperation:%{public}@ target:%{public}@ performEventTarget:%{public}@ updatingState:%{BOOL}u shouldNotifyUpdatedPresentation:%{BOOL}u shouldNotifyBegan:%{BOOL}u shouldNotifyCompleted:%{BOOL}u eventHistory:%{public}@ updateHistory:%{public}@"
- "ESM:%p (finishing - %s) setPresentation:%p transitionStates:%{public}@"
- "ESM:%p (performEvent finishing - %s) performEvent:%{public}@ transitionStates:%{public}@ "
- "ESM:%p (stale) etsUpdateTo:%{public}@ for:%{public}@ ets:%{public}@"
- "ESM:%p calling performEvent on invalidated state machine:%{public}@ event:%{public}@ initialSpecifier:%{public}@"
- "ESM:%p calling setPresentation on invalidated state machine:%{public}@ presentation:%{public}@"
- "ESM:%p calling updateAllEnvironmentsInPresentation on invalidated state machine:%{public}@"
- "ESM:%p calling updateEnvironment on invalidated state machine:%{public}@ environment:%{public}@"
- "ESM:%p calling updateFlipbookVisualState on invalidated state machine:%{public}@"
- "ESM:%p checkFlipbookVisualStateCompletion (rdar://175348594) isBeginUpdate:%{BOOL}u transitionState:%{public}@ notInTrackingSet shouldComplete:%{BOOL}u remaining:%lu"
- "ESM:%p completedOperation:%{public}@ target:%{public}@ performEventTarget:%{public}@ updatingState:%{BOOL}u shouldNotifyUpdatedPresentation:%{BOOL}u shouldNotifyBegan:%{BOOL}u shouldNotifyCompleted:%{BOOL}u, setPresentationOperation:%{public}@ eventHistory:%{public}@ updateHistory:%{public}@"
- "ESM:%p etsUpdateTo:%{public}@ dateMatch:%{BOOL}u for:%{public}@ ets:%{public}@"
- "ESM:%p finishing (immediate complete - update begin also) setPresentation:%{public}@"
- "ESM:%p finishing (immediate complete - update end also) setPresentation:%{public}@"
- "ESM:%p finishing (immediate complete) setPresentation:%{public}@"
- "ESM:%p finishing (performEvent immediate begin update) performEvent:%{public}@"
- "ESM:%p finishing (performEvent immediate complete) performEvent:%{public}@"
- "ESM:%p finishing (performEvent immediate setPresentation complete) performEvent:%{public}@"
- "ESM:%p flipbookVisualStateUpdateCompleted isFlipbook:%{BOOL}u specifier:%{public}@"
- "ESM:%p not will update environment:%{public}@ (unchanged) to backlightState:%{public}@ visualState:%{public}@"
- "ESM:%p removal— no longer active transitionState:%{public}@"
- "ESM:%p setPresentation (redundant) targetBacklightState:%{public}@"
- "ESM:%p setPresentation (redundant) targetBacklightState:%{public}@->%{public}@ additions:%{public}@"
- "ESM:%p setPresentation by adding:%{public}@ and removing:%{public}@ targetBacklightState:%{public}@"
- "ESM:%p setPresentation by adding:%{public}@ targetBacklightState:%{public}@"
- "ESM:%p setPresentation by removing:%{public}@ targetBacklightState:%{public}@"
- "ESM:%p setPresentation: staleEnvironmentsThatNeedDeferredUpdate:%{public}@"
- "ESM:%p updateFlipbookVisualState:%{BOOL}u initialSpecifier:%{public}@ environments:%@ now:%{public}@"
- "ESM:%p will not stop tracking transitionState:%{public}@ (isActiveTransitionState:%{BOOL}u)"
- "ESM:%p will not update environment:%{public}@ (not in presentation) to backlightState:%{public}@"
- "ESM:%p will skip environment update, no longer in presentation — updateTransitionStatesForReason:%{public}@ environment:%p:%{public}@"
- "ESM:%p will stop tracking transitionState:%{public}@"
- "ESM:%p will update environment:%{public}@ to backlightState:%{public}@ visualState:%{public}@"
- "ETS:%p: client disabled:%p, pretending state matches:%{public}@"
- "ETS:%p:%{public}@ (%@) did perform backlightRamp duration:%.2f to target:%{public}@ "
- "ETS:%p:%{public}@ (now obsolete - will not call backlight ramp or animation completion) redundant update to target:%{public}@ wasUpdating:%{BOOL}u animated:%{BOOL}u hasBacklightRamp:%{BOOL}u event:%{public}@ touchTarget:%{BOOL}u oldInProgress:%{public}@ currentInProgress:%{public}@"
- "ETS:%p:%{public}@ animationComplete to target:%{public}@ event:%{public}@ animated:%{BOOL}u inProgressUpdateTarget:%{public}@ requestingFidelityTarget:%{public}@"
- "ETS:%p:%{public}@ did update to dateSpecifier:%{public}@"
- "ETS:%p:%{public}@ redundant update to target:%{public}@ wasUpdating:%{BOOL}u animated:%{BOOL}u hasBacklightRamp:%{BOOL}u event:%{public}@ touchTarget:%{BOOL}u existingInProgress:%{public}@"
- "ETS:%p:%{public}@ scene contents updated to target:%{public}@ event:%{public}@ animated:%{BOOL}u inProgressUpdateTarget:%{public}@ requestingFidelityTarget:%{public}@"
- "ETS:%p:%{public}@ target:%{public}@ snapped because client failed to perform backlight ramp for event:%{public}@"
- "ETS:%p:%{public}@ transitionState dealloc"
- "ETS:%p:%{public}@ transitionState init"
- "ETS:%p:%{public}@ update to dateSpecifier:%{public}@"
- "ETS:%p:%{public}@ update to state:%{public}@ – inheriting old backlight ramp existingInProgress:%{public}@ –\u00a0event:%{public}@"
- "ETS:%p:%{public}@ update to state:%{public}@ – inheriting old triggerEvent existingInProgress:%{public}@ –\u00a0event:%{public}@"
- "ETS:%p:%{public}@ updateToFlipbookVisualState:%{BOOL}u presentation date falling back to now:%{public}@ "
- "ETS:%p:%{public}@ will skip update to oldTarget:%{public}@ was replaced with newPartialTarget:%{public}@ hadBacklightRamp:%{BOOL}u oldEvent:%{public}@ wouldTransitionHaveBeenNeeded:%{BOOL}U"
- "ETS:%p:%{public}@ will update to target:%{public}@ wasUpdating:%{BOOL}u animated:%{BOOL}u hasBacklightRamp:%{BOOL}u event:%{public}@ touchTarget:%{BOOL}u lprTime:%llu"
- "TSM:%p:%{public}@ (findNextOperation) no operation needed isBeforeDisplayBlankingChange:%{BOOL}u hasEvents:%{BOOL}u needsFlipbook:%{BOOL}u"
- "TSM:%p:%{public}@ LPR disable state changed disabled:%{BOOL}u"
- "TSM:%p:%{public}@ didAmendSceneSettings: visualState isFlipbook but displayMode is %{public}@ — stripping flipbook, environment:%{public}@ visualState:%{public}@"
- "environment for later update must implement updateToVisualState:presentationDateSpecifier: from BLSHBacklightSceneHostEnvironment_Private"
- "hostCachedState != nil"
- "\xf0Q"
```
