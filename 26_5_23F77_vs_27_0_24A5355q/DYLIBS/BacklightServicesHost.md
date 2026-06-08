## BacklightServicesHost

> `/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`

```diff

-5.4.2.0.0
-  __TEXT.__text: 0x8a5ac
-  __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_methlist: 0x7bcc
-  __TEXT.__const: 0x3b8
-  __TEXT.__gcc_except_tab: 0x112c
-  __TEXT.__cstring: 0x6a9c
-  __TEXT.__oslogstring: 0xfaca
-  __TEXT.__ustring: 0x328
-  __TEXT.__unwind_info: 0x2428
-  __TEXT.__objc_classname: 0x2005
-  __TEXT.__objc_methname: 0x11d9f
-  __TEXT.__objc_methtype: 0x43e9
-  __TEXT.__objc_stubs: 0xa2e0
-  __DATA_CONST.__got: 0x758
-  __DATA_CONST.__const: 0x27d0
-  __DATA_CONST.__objc_classlist: 0x560
-  __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x2a0
+6.0.33.0.0
+  __TEXT.__text: 0x9a87c
+  __TEXT.__objc_methlist: 0x9c44
+  __TEXT.__const: 0x4a0
+  __TEXT.__gcc_except_tab: 0xf18
+  __TEXT.__cstring: 0x7cde
+  __TEXT.__oslogstring: 0x1289d
+  __TEXT.__ustring: 0x570
+  __TEXT.__unwind_info: 0x2840
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x2cc8
+  __DATA_CONST.__objc_classlist: 0x638
+  __DATA_CONST.__objc_catlist: 0x38
+  __DATA_CONST.__objc_protolist: 0x300
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x31b8
-  __DATA_CONST.__objc_superrefs: 0x460
+  __DATA_CONST.__objc_selrefs: 0x3bd8
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x518
   __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__auth_got: 0x560
-  __AUTH_CONST.__const: 0xb60
-  __AUTH_CONST.__cfstring: 0x6600
-  __AUTH_CONST.__objc_const: 0x13e58
+  __DATA_CONST.__got: 0x800
+  __AUTH_CONST.__const: 0xd00
+  __AUTH_CONST.__cfstring: 0x7c60
+  __AUTH_CONST.__objc_const: 0x18fd0
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0xeb0
-  __DATA.__objc_ivar: 0xe84
-  __DATA.__data: 0x1f80
-  __DATA.__bss: 0x98
-  __DATA_DIRTY.__objc_data: 0x2710
-  __DATA_DIRTY.__bss: 0xf8
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x11d0
+  __DATA.__objc_ivar: 0x12dc
+  __DATA.__data: 0x2400
+  __DATA.__bss: 0xf0
+  __DATA_DIRTY.__objc_data: 0x2c60
+  __DATA_DIRTY.__bss: 0x110
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/PowerExperience.framework/PowerExperience
+  - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SystemWake.framework/SystemWake
   - /usr/lib/libIOReport.dylib

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: F9A48110-5DB8-3153-9123-6F2717CA0E0E
-  Functions: 3485
-  Symbols:   12146
-  CStrings:  5885
+  UUID: D4FB51EA-7A1B-39D2-9196-D376D9D49067
+  Functions: 4203
+  Symbols:   14481
+  CStrings:  2962
 
Symbols:
+ +[BLSHAggregateBacklightHost aggregateHostWithBacklightHosts:]
+ +[BLSHBacklightEnvironmentSessionProvider providerWithProviderFactory:]
+ +[BLSHBacklightHost backlightHostForDisplay:]
+ +[BLSHBacklightHost backlightHostForDisplay:].cold.1
+ +[BLSHBacklightHost registerBacklightHost:forDisplay:]
+ +[BLSHBacklightHost(BLSHBacklightHostTelemetry) telemetrySourceForDisplay:]
+ +[BLSHBacklightIdleProvider createProviderforDisplay:withLocalAssertionService:]
+ +[BLSHBacklightIdleProvider createProviderforDisplay:withLocalAssertionService:].cold.1
+ +[BLSHBacklightIdleProvider providerForDisplay:]
+ +[BLSHBacklightIdleProvider providerForDisplay:].cold.1
+ +[BLSHBacklightSceneEnvironmentHosting enableSubhostingForEnvironment:withSessionProvider:osTimerProvider:].cold.2
+ +[BLSHBacklightService serviceWithPlatformProvider:osInterfaceProvider:inactiveBudgetPolicy:localAssertionService:telemetryPlatformDelegate:localOnly:]
+ +[BLSHCATransactionTelemetryContext telemetryContextWithTransactionID:shouldGenerateSeed:]
+ +[BLSHCoreAnalytics sendEventAsync:payloadBuilder:]
+ +[BLSHCoreAnalytics sharedAnalyticsSender]
+ +[BLSHCoreAnalytics workloop]
+ +[BLSHCoreAnalytics workloop].cold.1
+ +[BLSHDisableLowPowerRenderingAttributeHandler attributeBaseClass]
+ +[BLSHDisableLowPowerRenderingAttributeHandler attributeClasses]
+ +[BLSHDisableLowPowerRenderingAttributeHandler registerHandlerForService:provider:]
+ +[BLSHEnvironmentDateSpecifier specifierWithPresentationDate:fidelity:environment:userObject:lowPowerRenderingPresentationTime:]
+ +[BLSHFlipbook createForDisplay:platformProvider:]
+ +[BLSHForceActiveAttributeHandler registerHandlerForService:display:]
+ +[BLSHLowPowerRenderingAttributeHandler attributeBaseClass]
+ +[BLSHLowPowerRenderingAttributeHandler attributeClasses]
+ +[BLSHPresentationDateSpecifier specifierWithPresentationDate:specifiers:lowPowerRenderingPresentationTime:sourceFrameType:]
+ +[BLSHSceneRegistrationExtension hostComponents]
+ +[BLSHSceneRegistrationExtension sceneForIdentityToken:]
+ +[BLSHSceneRegistrationStore sharedInstance]
+ +[BLSHSceneRegistrationStore sharedInstance].cold.1
+ +[BLSHSystemWakeTelemetry defaultServiceWithDelegate:]
+ +[BLSHValidWhenBacklightInactiveAttributeHandler registerHandlerForService:display:]
+ +[BLSHXPCAssertionServiceHostServer serverWithLocalAssertionService:osInterfaceProvider:]
+ +[BLSHXPCAssertionServiceHostServer serverWithLocalAssertionService:osInterfaceProvider:].cold.1
+ -[BLSHAOTSystemWakeTelemetry .cxx_destruct]
+ -[BLSHAOTSystemWakeTelemetry _resetAccumulatedMetrics]
+ -[BLSHAOTSystemWakeTelemetry accumulateMetrics:]
+ -[BLSHAOTSystemWakeTelemetry accumulateOffDuration:isAOT:]
+ -[BLSHAOTSystemWakeTelemetry accumulateOnDuration:]
+ -[BLSHAOTSystemWakeTelemetry backlight:didChangeAlwaysOnEnabled:]
+ -[BLSHAOTSystemWakeTelemetry backlight:didUpdateToDisplayMode:fromDisplayMode:activeEvents:abortedEvents:]
+ -[BLSHAOTSystemWakeTelemetry backlight:willUpdateToDisplayMode:fromDisplayMode:forEvents:abortedEvents:]
+ -[BLSHAOTSystemWakeTelemetry dealloc]
+ -[BLSHAOTSystemWakeTelemetry gatherTelemetryForWakeNumber:]
+ -[BLSHAOTSystemWakeTelemetry logMetricsTimerFired]
+ -[BLSHAOTSystemWakeTelemetry logTelemetryForInvalidation:]
+ -[BLSHAOTSystemWakeTelemetry logTelemetryForInvalidation:].cold.1
+ -[BLSHAOTSystemWakeTelemetry logTelemetryForInvalidation:].cold.2
+ -[BLSHAOTSystemWakeTelemetry logTelemetryForRenderSession:]
+ -[BLSHAOTSystemWakeTelemetry logTelemetryForRenderSession:].cold.1
+ -[BLSHAOTSystemWakeTelemetry logTelemetryForRenderSession:].cold.2
+ -[BLSHAOTSystemWakeTelemetry logTelemetryForRequestDates:]
+ -[BLSHAOTSystemWakeTelemetry logTelemetryForRequestDates:].cold.1
+ -[BLSHAOTSystemWakeTelemetry logTelemetryForRequestDates:].cold.2
+ -[BLSHAOTSystemWakeTelemetry observesUpdateToDisplayMode]
+ -[BLSHAOTSystemWakeTelemetry startObserving]
+ -[BLSHAOTSystemWakeTelemetry startObserving].cold.1
+ -[BLSHAOTSystemWakeTelemetry startObserving].cold.2
+ -[BLSHAOTSystemWakeTelemetry stopObserving]
+ -[BLSHAggregateBacklightHost .cxx_destruct]
+ -[BLSHAggregateBacklightHost addObserver:]
+ -[BLSHAggregateBacklightHost backlight:didChangeAlwaysOnEnabled:]
+ -[BLSHAggregateBacklightHost backlight:didChangeAlwaysOnEnabled:].cold.1
+ -[BLSHAggregateBacklightHost backlight:didChangeAlwaysOnEnabled:].cold.2
+ -[BLSHAggregateBacklightHost backlight:didCompleteUpdateToFlipbookState:forEvents:abortedEvents:]
+ -[BLSHAggregateBacklightHost backlight:didCompleteUpdateToFlipbookState:forEvents:abortedEvents:].cold.1
+ -[BLSHAggregateBacklightHost backlight:didCompleteUpdateToFlipbookState:forEvents:abortedEvents:].cold.2
+ -[BLSHAggregateBacklightHost backlight:didCompleteUpdateToState:forEvents:abortedEvents:]
+ -[BLSHAggregateBacklightHost backlight:didCompleteUpdateToState:forEvents:abortedEvents:].cold.1
+ -[BLSHAggregateBacklightHost backlight:didCompleteUpdateToState:forEvents:abortedEvents:].cold.2
+ -[BLSHAggregateBacklightHost backlight:didUpdateToDisplayMode:fromDisplayMode:activeEvents:abortedEvents:]
+ -[BLSHAggregateBacklightHost backlight:didUpdateToDisplayMode:fromDisplayMode:activeEvents:abortedEvents:].cold.1
+ -[BLSHAggregateBacklightHost backlight:didUpdateToDisplayMode:fromDisplayMode:activeEvents:abortedEvents:].cold.2
+ -[BLSHAggregateBacklightHost backlight:didUpdateVisualContentsToBeginTransitionToState:forEvents:abortedEvents:]
+ -[BLSHAggregateBacklightHost backlight:performingEvent:]
+ -[BLSHAggregateBacklightHost backlight:performingEvent:].cold.1
+ -[BLSHAggregateBacklightHost backlight:willUpdateToDisplayMode:fromDisplayMode:forEvents:abortedEvents:]
+ -[BLSHAggregateBacklightHost backlight:willUpdateToDisplayMode:fromDisplayMode:forEvents:abortedEvents:].cold.1
+ -[BLSHAggregateBacklightHost backlight:willUpdateToDisplayMode:fromDisplayMode:forEvents:abortedEvents:].cold.2
+ -[BLSHAggregateBacklightHost backlightDisplayMode]
+ -[BLSHAggregateBacklightHost backlightHost:willTransitionToState:forEvent:]
+ -[BLSHAggregateBacklightHost backlightHost:willTransitionToState:forEvent:].cold.1
+ -[BLSHAggregateBacklightHost backlightHost:willTransitionToState:forEvent:].cold.2
+ -[BLSHAggregateBacklightHost backlightStateChangeTimestamp]
+ -[BLSHAggregateBacklightHost backlightStateDescription]
+ -[BLSHAggregateBacklightHost backlightState]
+ -[BLSHAggregateBacklightHost dealloc]
+ -[BLSHAggregateBacklightHost deviceSupportsAlwaysOn]
+ -[BLSHAggregateBacklightHost display]
+ -[BLSHAggregateBacklightHost flipbookState]
+ -[BLSHAggregateBacklightHost initWithBacklightHosts:]
+ -[BLSHAggregateBacklightHost isAlwaysOnEnabled]
+ -[BLSHAggregateBacklightHost isTransitioning]
+ -[BLSHAggregateBacklightHost notifyInitialStateForObserver:]
+ -[BLSHAggregateBacklightHost notifyObserversWithBlock:]
+ -[BLSHAggregateBacklightHost observesActivation]
+ -[BLSHAggregateBacklightHost observesBlankingChanges]
+ -[BLSHAggregateBacklightHost observesDeactivation]
+ -[BLSHAggregateBacklightHost observesDidUpdateVisualContents]
+ -[BLSHAggregateBacklightHost observesPerformingAllEvents]
+ -[BLSHAggregateBacklightHost observesUpdateToDisplayMode]
+ -[BLSHAggregateBacklightHost performChangeRequest:]
+ -[BLSHAggregateBacklightHost removeObserver:]
+ -[BLSHAggregateBacklightHost setTelemetryDelegate:]
+ -[BLSHAggregateBacklightHost setTelemetryDelegate:].cold.1
+ -[BLSHAggregateBacklightHost telemetryDelegate]
+ -[BLSHAggregateBacklightHost withLock_backlightStateDescription]
+ -[BLSHAggregateHostCachedState alwaysOnEnabled]
+ -[BLSHAggregateHostCachedState backlightState]
+ -[BLSHAggregateHostCachedState description]
+ -[BLSHAggregateHostCachedState displayMode]
+ -[BLSHAggregateHostCachedState flipbookState]
+ -[BLSHAggregateHostCachedState initWithBacklightHost:]
+ -[BLSHAggregateHostCachedState initWithBacklightState:displayMode:flipbookState:alwaysOnEnabled:]
+ -[BLSHAggregateHostCachedState setAlwaysOnEnabled:]
+ -[BLSHAggregateHostCachedState setBacklightState:]
+ -[BLSHAggregateHostCachedState setDisplayMode:]
+ -[BLSHAggregateHostCachedState setFlipbookState:]
+ -[BLSHAggregateHostCachedState setTargetDisplayMode:]
+ -[BLSHAggregateHostCachedState setWillTransitionBacklightState:]
+ -[BLSHAggregateHostCachedState targetDisplayMode]
+ -[BLSHAggregateHostCachedState willTransitionBacklightState]
+ -[BLSHAlwaysFillFlipbookAttributeHandler display]
+ -[BLSHAlwaysOnPresentationEngine _lock_updateLowPowerRenderingFromPresentation:]
+ -[BLSHAlwaysOnPresentationEngine display]
+ -[BLSHAlwaysOnPresentationEngine hostEnvironment:hostDidSetLowPowerRendering:]
+ -[BLSHAlwaysOnPresentationEngine initForDisplay:delegate:platformProvider:osInterfaceProvider:inactiveBudgetPolicy:]
+ -[BLSHAlwaysOnPresentationEngine isLowPowerRenderingDisabled]
+ -[BLSHAlwaysOnPresentationEngine registerHandlersForService:].cold.5
+ -[BLSHAlwaysOnPresentationEngine setFlipbookTelemetryDelegate:]
+ -[BLSHAlwaysOnPresentationEngine setLowPowerRenderingDisabled:]
+ -[BLSHBacklightDisplayStateMachine display:didCompleteSwitchToCBFlipbookState:withError:]
+ -[BLSHBacklightDisplayStateMachine display:didCompleteSwitchToCBFlipbookState:withError:].cold.1
+ -[BLSHBacklightDisplayStateMachine display:didCompleteTransitionToCADisplayState:currentState:transitionStatus:]
+ -[BLSHBacklightDisplayStateMachine display:didCompleteTransitionToCBDisplayMode:withError:]
+ -[BLSHBacklightDisplayStateMachine display:didCompleteTransitionToCBDisplayMode:withError:].cold.1
+ -[BLSHBacklightDisplayStateMachine display:didCompleteTransitionToCBDisplayMode:withError:].cold.2
+ -[BLSHBacklightDisplayStateMachine displayModeForDisplay:]
+ -[BLSHBacklightDisplayStateMachine initForDisplay:delegate:platformProvider:osInterfaceProvider:]
+ -[BLSHBacklightDisplayStateMachineAbortContext initWithDisplayMode:prewarmingDisplayMode:lastSteadyStateDisplayMode:caDisplayState:cbDisplayMode:sleepMonitorAggregateState:hasEnsureFlipbookCurrent:]
+ -[BLSHBacklightEnvironmentPresentation isLowPowerRendering]
+ -[BLSHBacklightEnvironmentPresentation(FrontBoard) initWithFBScenes:flipbookContext:expirationDate:]
+ -[BLSHBacklightEnvironmentSessionProvider .cxx_destruct]
+ -[BLSHBacklightEnvironmentSessionProvider createInactiveEnvironmentSessionForDisplay:]
+ -[BLSHBacklightEnvironmentSessionProvider createInactiveEnvironmentSession]
+ -[BLSHBacklightEnvironmentSessionProvider initWithProviderFactory:]
+ -[BLSHBacklightEnvironmentSessionProvider init]
+ -[BLSHBacklightEnvironmentSessionProvider providerForDisplay:]
+ -[BLSHBacklightEnvironmentSessionProvider providersByDisplayId]
+ -[BLSHBacklightEnvironmentSessionProvider providersByDisplayId].cold.1
+ -[BLSHBacklightEnvironmentStateMachine _lock_allFlipbookTransitionsDidBeginUpdate]
+ -[BLSHBacklightEnvironmentStateMachine _lock_isLowPowerRenderingDisabled]
+ -[BLSHBacklightEnvironmentStateMachine checkFlipbookVisualStateCompletionForTransitionState:isBeginUpdate:]
+ -[BLSHBacklightEnvironmentStateMachine flipbookVisualStateUpdateCompleted]
+ -[BLSHBacklightEnvironmentStateMachine isLowPowerRenderingDisabled]
+ -[BLSHBacklightEnvironmentStateMachine onMain_updateFlipbookVisualState:backlightState:withInitialSpecifier:]
+ -[BLSHBacklightEnvironmentStateMachine updateFlipbookVisualState:backlightState:withInitialSpecifier:]
+ -[BLSHBacklightEventMetrics .cxx_destruct]
+ -[BLSHBacklightEventMetrics abortedEventsCount]
+ -[BLSHBacklightEventMetrics allEventsToWakeDurationSeconds]
+ -[BLSHBacklightEventMetrics beforeKernelWake]
+ -[BLSHBacklightEventMetrics completedEventsCount]
+ -[BLSHBacklightEventMetrics compressionsDiff]
+ -[BLSHBacklightEventMetrics didCompleteDurationSeconds]
+ -[BLSHBacklightEventMetrics didTimeoutSystemActivity]
+ -[BLSHBacklightEventMetrics displayIdentifier]
+ -[BLSHBacklightEventMetrics durationSeconds]
+ -[BLSHBacklightEventMetrics endpoint]
+ -[BLSHBacklightEventMetrics eventType]
+ -[BLSHBacklightEventMetrics explanation]
+ -[BLSHBacklightEventMetrics pageinDiff]
+ -[BLSHBacklightEventMetrics performEventCount]
+ -[BLSHBacklightEventMetrics platformContext]
+ -[BLSHBacklightEventMetrics secondsAfterKernelWake]
+ -[BLSHBacklightEventMetrics serializedPayload]
+ -[BLSHBacklightEventMetrics setAbortedEventsCount:]
+ -[BLSHBacklightEventMetrics setAllEventsToWakeDurationSeconds:]
+ -[BLSHBacklightEventMetrics setBeforeKernelWake:]
+ -[BLSHBacklightEventMetrics setCompletedEventsCount:]
+ -[BLSHBacklightEventMetrics setCompressionsDiff:]
+ -[BLSHBacklightEventMetrics setDidCompleteDurationSeconds:]
+ -[BLSHBacklightEventMetrics setDidTimeoutSystemActivity:]
+ -[BLSHBacklightEventMetrics setDisplayIdentifier:]
+ -[BLSHBacklightEventMetrics setDurationSeconds:]
+ -[BLSHBacklightEventMetrics setEndpoint:]
+ -[BLSHBacklightEventMetrics setEventType:]
+ -[BLSHBacklightEventMetrics setExplanation:]
+ -[BLSHBacklightEventMetrics setPageinDiff:]
+ -[BLSHBacklightEventMetrics setPerformEventCount:]
+ -[BLSHBacklightEventMetrics setPlatformContext:]
+ -[BLSHBacklightEventMetrics setSecondsAfterKernelWake:]
+ -[BLSHBacklightEventMetrics setSourceEvent:]
+ -[BLSHBacklightEventMetrics setSystemActivityAcquisitionDetails:]
+ -[BLSHBacklightEventMetrics setSystemActivityAcquisitionSeconds:]
+ -[BLSHBacklightEventMetrics setSystemActivityAcquisitionSkipped:]
+ -[BLSHBacklightEventMetrics setSystemActivityAcquisitionSuccess:]
+ -[BLSHBacklightEventMetrics setTimeoutTriggeredBlackFlash:]
+ -[BLSHBacklightEventMetrics setWakeReason:]
+ -[BLSHBacklightEventMetrics setWasInactiveOn:]
+ -[BLSHBacklightEventMetrics sourceEvent]
+ -[BLSHBacklightEventMetrics stringForEventType:]
+ -[BLSHBacklightEventMetrics systemActivityAcquisitionDetails]
+ -[BLSHBacklightEventMetrics systemActivityAcquisitionSeconds]
+ -[BLSHBacklightEventMetrics systemActivityAcquisitionSkipped]
+ -[BLSHBacklightEventMetrics systemActivityAcquisitionSuccess]
+ -[BLSHBacklightEventMetrics timeoutTriggeredBlackFlash]
+ -[BLSHBacklightEventMetrics wakeReason]
+ -[BLSHBacklightEventMetrics wasInactiveOn]
+ -[BLSHBacklightFBSceneHostEnvironment clientNeedsFlipbookStateUpdates]
+ -[BLSHBacklightFBSceneHostEnvironment clientNeedsLowPowerRenderingStateUpdates]
+ -[BLSHBacklightFBSceneHostEnvironment isLowPowerRendering]
+ -[BLSHBacklightFBSceneHostEnvironment lowPowerRenderingPresentationTime]
+ -[BLSHBacklightFBSceneHostEnvironment setLowPowerRendering:]
+ -[BLSHBacklightFBSceneHostEnvironment setLowPowerRendering:].cold.1
+ -[BLSHBacklightFBSceneHostEnvironment setLowPowerRenderingPresentationTime:forwardedToSettings:]
+ -[BLSHBacklightFBSceneHostEnvironment updateToDateSpecifier:sceneContentsUpdated:lowPowerRenderingDisabled:]
+ -[BLSHBacklightIdleProvider display]
+ -[BLSHBacklightOSInterfaceProvider displayInterfaces]
+ -[BLSHBacklightOSInterfaceProvider displayReferences]
+ -[BLSHBacklightOSInterfaceProvider flipbookArbiter]
+ -[BLSHBacklightOSInterfaceProvider platformProvider:didChangeAlwaysOnSetting:]
+ -[BLSHBacklightOSInterfaceProvider platformProviderDidDetectSignificantUserInteraction:]
+ -[BLSHBacklightService displayWakeTelemetries]
+ -[BLSHBacklightService initWithPlatformProvider:osInterfaceProvider:inactiveBudgetPolicy:localAssertionService:telemetryPlatformDelegate:localOnly:]
+ -[BLSHBacklightService initWithPlatformProvider:osInterfaceProvider:inactiveBudgetPolicy:localAssertionService:telemetryPlatformDelegate:localOnly:].cold.1
+ -[BLSHBacklightService setFlipbookTelemetryDelegate:]
+ -[BLSHBacklightStateMachine backlight:rampingToBrightnessCurve:withDuration:forEvents:abortedEvents:]
+ -[BLSHBacklightStateMachine display]
+ -[BLSHBacklightStateMachine initForDisplay:platformProvider:eventPerformer:osInterfaceProvider:]
+ -[BLSHBacklightStateMachine registerHandlersForService:].cold.3
+ -[BLSHBacklightTransitionStateMachine alwaysOnPresentationEngine]
+ -[BLSHBacklightTransitionStateMachine displayState:isUpdatingToBrightnessCurve:withDuration:]
+ -[BLSHBacklightTransitionStateMachine display]
+ -[BLSHBacklightTransitionStateMachine environmentStateMachine:didUpdateFlipbookVisualState:specifier:]
+ -[BLSHBacklightTransitionStateMachine initForDisplay:platformProvider:osInterfaceProvider:inactiveBudgetPolicy:]
+ -[BLSHBacklightTransitionStateMachine initForDisplay:platformProvider:osInterfaceProvider:inactiveBudgetPolicy:].cold.1
+ -[BLSHBacklightTransitionStateMachine isLowPowerRenderingDisabled]
+ -[BLSHBacklightTransitionStateMachine lock_displayModeForBacklightState:].cold.2
+ -[BLSHBacklightTransitionStateMachine lock_displayModeForBacklightState:].cold.3
+ -[BLSHBacklightTransitionStateMachine onMainWithLock_updateOperationNeedsFlipbook:isFlipbook:flipbookFirst:events:]
+ -[BLSHBacklightTransitionStateMachine onMain_startSubOperation:environmentStateMachine:backlightState:currentPresentation:]
+ -[BLSHBacklightTransitionStateMachine onMain_startSubOperation:environmentStateMachine:backlightState:currentPresentation:].cold.1
+ -[BLSHBacklightTransitionStateMachine onMain_startSubOperation:environmentStateMachine:backlightState:currentPresentation:].cold.2
+ -[BLSHBacklightTransitionStateMachine onMain_startSubOperation:environmentStateMachine:backlightState:currentPresentation:].cold.3
+ -[BLSHBacklightTransitionStateMachine onMain_startSubOperation:environmentStateMachine:backlightState:currentPresentation:].cold.4
+ -[BLSHBacklightTransitionStateMachine presentationEngine:didChangeLowPowerRenderingDisabled:]
+ -[BLSHBacklightTransitionStateMachine updateDisplayModeAfterClaimingFlipbook:]
+ -[BLSHBacklightTransitionStateMachine updateDisplayModeAfterClaimingFlipbook:].cold.1
+ -[BLSHBacklightTransitionStateMachine updateDisplayModeAfterClaimingFlipbook:].cold.2
+ -[BLSHBacklightWakeTelemetryEvent .cxx_destruct]
+ -[BLSHBacklightWakeTelemetryEvent abortedEventsCount]
+ -[BLSHBacklightWakeTelemetryEvent allEventsToWakeDurationSeconds]
+ -[BLSHBacklightWakeTelemetryEvent beforeKernelWake]
+ -[BLSHBacklightWakeTelemetryEvent completedEventsCount]
+ -[BLSHBacklightWakeTelemetryEvent compressionsDiff]
+ -[BLSHBacklightWakeTelemetryEvent description]
+ -[BLSHBacklightWakeTelemetryEvent didCompleteDurationSeconds]
+ -[BLSHBacklightWakeTelemetryEvent didTimeoutSystemActivty]
+ -[BLSHBacklightWakeTelemetryEvent endpoint]
+ -[BLSHBacklightWakeTelemetryEvent initWithWakeDurationSeconds:wasInactiveOn:endpoint:wakeReason:beforeKernelWake:secondsAfterKernelWake:pageinDiff:compressionsDiff:performEventCount:completedEventsCount:abortedEventsCount:allEventsToWakeDurationSeconds:didCompleteDurationSeconds:systemActivityAcquisitionSeconds:didTimeoutSystemActivty:timeoutTriggerdBlackFlash:systemActivityAcquisitionSuccess:systemActivityAcquisitionDetails:systemActivityAcquisitionSkipped:]
+ -[BLSHBacklightWakeTelemetryEvent pageinDiff]
+ -[BLSHBacklightWakeTelemetryEvent performEventCount]
+ -[BLSHBacklightWakeTelemetryEvent secondsAfterKernelWake]
+ -[BLSHBacklightWakeTelemetryEvent systemActivityAcquisitionDetails]
+ -[BLSHBacklightWakeTelemetryEvent systemActivityAcquisitionSeconds]
+ -[BLSHBacklightWakeTelemetryEvent systemActivityAcquisitionSkipped]
+ -[BLSHBacklightWakeTelemetryEvent systemActivityAcquisitionSuccess]
+ -[BLSHBacklightWakeTelemetryEvent timeoutTriggeredBlackFlash]
+ -[BLSHBacklightWakeTelemetryEvent wakeDurationSeconds]
+ -[BLSHBacklightWakeTelemetryEvent wakeReason]
+ -[BLSHBacklightWakeTelemetryEvent wasInactiveOn]
+ -[BLSHBacklightWakeTelemetryTracker .cxx_destruct]
+ -[BLSHBacklightWakeTelemetryTracker _lock_captureStatsForPendingEndpoint:timestamp:]
+ -[BLSHBacklightWakeTelemetryTracker _lock_checkAgainstTriggerEvent:]
+ -[BLSHBacklightWakeTelemetryTracker beginForEvent:completion:]
+ -[BLSHBacklightWakeTelemetryTracker beginForEvent:completion:].cold.1
+ -[BLSHBacklightWakeTelemetryTracker checkCompleteForEvent:]
+ -[BLSHBacklightWakeTelemetryTracker completeForEvent:]
+ -[BLSHBacklightWakeTelemetryTracker completeForEvent:].cold.1
+ -[BLSHBacklightWakeTelemetryTracker dealloc]
+ -[BLSHBacklightWakeTelemetryTracker dealloc].cold.1
+ -[BLSHBacklightWakeTelemetryTracker didAcquireSystemActivityWithError:isActive:details:forEvent:]
+ -[BLSHBacklightWakeTelemetryTracker didCompleteUpdateForEvents:abortedEvents:]
+ -[BLSHBacklightWakeTelemetryTracker didUnblankForEvent:]
+ -[BLSHBacklightWakeTelemetryTracker didUpdateVisualContentsToBeginTransitionToActiveOnForEvent:]
+ -[BLSHBacklightWakeTelemetryTracker didUpdateVisualContentsToBeginTransitionToActiveOnForEvent:].cold.1
+ -[BLSHBacklightWakeTelemetryTracker hadExistingSystemActivityForEvent:]
+ -[BLSHBacklightWakeTelemetryTracker incrementPerformEventCounterWithEvent:]
+ -[BLSHBacklightWakeTelemetryTracker init]
+ -[BLSHBacklightWakeTelemetryTracker invalidate]
+ -[BLSHBacklightWakeTelemetryTracker isCommitOnWakeMeasurementDisabled]
+ -[BLSHBacklightWakeTelemetryTracker setCommitOnWakeMeasurementDisabled:]
+ -[BLSHBacklightWakeTelemetryTracker willUnblankForEvent:]
+ -[BLSHBaseBacklightEnvironmentSessionProvider createInactiveEnvironmentSessionForDisplay:]
+ -[BLSHBaseBacklightEnvironmentSessionProvider display]
+ -[BLSHBaseBacklightEnvironmentSessionProvider initForDisplay:]
+ -[BLSHBaseBacklightEnvironmentSessionProvider setPresentation:completion:]
+ -[BLSHBaseBacklightEnvironmentSessionProvider setPresentation:completion:].cold.1
+ -[BLSHBasePlatformProvider setSessionProviderFactory:]
+ -[BLSHBasePlatformProvider setSessionProviderFactory:].cold.1
+ -[BLSHBasePlatformProvider setSessionProviderFactory:].cold.2
+ -[BLSHBaseSceneHostEnvironment clientNeedsFlipbookStateUpdates]
+ -[BLSHBaseSceneHostEnvironment clientNeedsLowPowerRenderingStateUpdates]
+ -[BLSHBaseSceneHostEnvironment isLowPowerRendering]
+ -[BLSHBaseSceneHostEnvironment setLowPowerRendering:]
+ -[BLSHBaseSceneHostEnvironment updateToDateSpecifier:sceneContentsUpdated:lowPowerRenderingDisabled:]
+ -[BLSHCATransactionTelemetryContext begin]
+ -[BLSHCATransactionTelemetryContext begin].cold.1
+ -[BLSHCATransactionTelemetryContext commit]
+ -[BLSHCATransactionTelemetryContext commit].cold.1
+ -[BLSHCATransactionTelemetryContext dealloc]
+ -[BLSHCATransactionTelemetryContext dealloc].cold.1
+ -[BLSHCATransactionTelemetryContext description]
+ -[BLSHCATransactionTelemetryContext elapsedMSActive]
+ -[BLSHCATransactionTelemetryContext elapsedSecondsActive]
+ -[BLSHCATransactionTelemetryContext generatedSeed]
+ -[BLSHCATransactionTelemetryContext initWithTransactionID:shouldGenerateSeed:]
+ -[BLSHCATransactionTelemetryContext isActive]
+ -[BLSHCATransactionTelemetryContext transactionID]
+ -[BLSHCancelWhenBacklightInactivatesAttributeEntry initForAttribute:fromAssertion:forService:attributeHandler:]
+ -[BLSHCoreAnalytics sendEventAsync:payloadBuilder:]
+ -[BLSHDiagnosticsServer _handleIncomingConnection:]
+ -[BLSHDiagnosticsServer _handleIncomingConnection:].cold.1
+ -[BLSHDisableAlwaysOnAttributeHandler display]
+ -[BLSHDisableFlipbookAttributeHandler display]
+ -[BLSHDisableFlipbookPowerSavingAttributeHandler attributeClasses]
+ -[BLSHDisableFlipbookPowerSavingAttributeHandler display]
+ -[BLSHDisableLowPowerRenderingAttributeHandler .cxx_destruct]
+ -[BLSHDisableLowPowerRenderingAttributeHandler activateWithFirstEntry:]
+ -[BLSHDisableLowPowerRenderingAttributeHandler deactivateWithFinalEntry:]
+ -[BLSHDisableLowPowerRenderingAttributeHandler display]
+ -[BLSHDisableLowPowerRenderingAttributeHandler initForService:provider:]
+ -[BLSHDisplayWakeTelemetry .cxx_destruct]
+ -[BLSHDisplayWakeTelemetry _commonInitWithTelemetrySource:analyticsRecorder:]
+ -[BLSHDisplayWakeTelemetry _eventNameForBacklightState:]
+ -[BLSHDisplayWakeTelemetry _handleBacklightDidCompleteUpdateToState:updateTime:forEvents:abortedEvents:]
+ -[BLSHDisplayWakeTelemetry _handleBacklightNewState:sourceEvent:explanation:startedAtContinuousTime:]
+ -[BLSHDisplayWakeTelemetry _handleBacklightNewState:sourceEvent:explanation:startedAtContinuousTime:changeEvent:]
+ -[BLSHDisplayWakeTelemetry _handleBacklightNewState:startedAtContinuousTime:event:]
+ -[BLSHDisplayWakeTelemetry _logAbortedEventsAnalytics:context:targetState:]
+ -[BLSHDisplayWakeTelemetry _logBacklightTelemetryEventForPendingEvent:duration:]
+ -[BLSHDisplayWakeTelemetry backlightTelemetrySource:didAcquireSystemActivityWithError:isActive:details:forEvent:]
+ -[BLSHDisplayWakeTelemetry backlightTelemetrySource:didCompleteUpdateToFlipbookState:forEvent:]
+ -[BLSHDisplayWakeTelemetry backlightTelemetrySource:didCompleteUpdateToState:forEvents:abortedEvents:]
+ -[BLSHDisplayWakeTelemetry backlightTelemetrySource:didUnblankToDisplayMode:forEvents:abortedEvents:]
+ -[BLSHDisplayWakeTelemetry backlightTelemetrySource:didUpdateVisualContentsToBeginTransitionToState:forEvents:abortedEvents:]
+ -[BLSHDisplayWakeTelemetry backlightTelemetrySource:hadExistingSystemActivityForEvent:]
+ -[BLSHDisplayWakeTelemetry backlightTelemetrySource:willPerformEvent:]
+ -[BLSHDisplayWakeTelemetry backlightTelemetrySource:willPerformEvent:].cold.1
+ -[BLSHDisplayWakeTelemetry backlightTelemetrySource:willUpdateDisplayForState:forEvent:]
+ -[BLSHDisplayWakeTelemetry backlightTelemetrySource:willUpdateDisplayForState:forEvent:].cold.1
+ -[BLSHDisplayWakeTelemetry initWithPlatformDelegate:]
+ -[BLSHDisplayWakeTelemetry initWithPlatformDelegate:telemetrySource:]
+ -[BLSHDisplayWakeTelemetry initWithPlatformDelegate:telemetrySource:analyticsRecorder:]
+ -[BLSHDisplayWakeTelemetry isCommitOnWakeMeasurementDisabled]
+ -[BLSHDisplayWakeTelemetry setCommitOnWakeMeasurementDisabled:]
+ -[BLSHDisplayWakeTelemetry setPlatformDelegate:]
+ -[BLSHDisplayWakeTelemetry setPlatformDelegate:].cold.1
+ -[BLSHDisplayWakeTelemetry setPlatformDelegate:].cold.2
+ -[BLSHDisplayWakeTelemetry startObserving]
+ -[BLSHEngineRenderFlipbookSession initWithDelegate:flipbook:presentation:osInterfaceProvider:display:]
+ -[BLSHEnvironmentDateSpecifier initWithPresentationDate:fidelity:environment:userObject:lowPowerRenderingPresentationTime:]
+ -[BLSHEnvironmentDateSpecifier lowPowerRenderingPresentationTime]
+ -[BLSHEnvironmentTransitionState isUpdatedToBacklightState:lowPowerRenderingDisabled:]
+ -[BLSHEnvironmentTransitionState updateToBacklightState:forEvent:touchTargetable:presentationDate:sceneUpdate:lowPowerRenderingPresentationTime:performBacklightRamp:]
+ -[BLSHEnvironmentTransitionState updateToFlipbookVisualState:backlightState:presentationDate:sceneUpdate:lowPowerRenderingPresentationTime:]
+ -[BLSHEnvironmentTransitionState visualStateForBacklightState:requestedFidelity:isFlipbook:]
+ -[BLSHEnvironmentTransitionState visualStateForBacklightState:requestedFidelity:lowPowerRenderingDisabled:]
+ -[BLSHEnvironmentTransitionStateTarget hasExplicitFlipbook]
+ -[BLSHEnvironmentTransitionStateTarget initWithTarget:visualState:presentationDate:isFlipbook:hasExplicitFlipbook:]
+ -[BLSHEnvironmentTransitionStateTarget isFlipbook]
+ -[BLSHEnvironmentTransitionStateTarget lowPowerRenderingPresentationTime]
+ -[BLSHEnvironmentTransitionStateTarget setHasExplicitFlipbook:]
+ -[BLSHEnvironmentTransitionStateTarget setIsFlipbook:]
+ -[BLSHEnvironmentTransitionStateTarget setLowPowerRenderingPresentationTime:]
+ -[BLSHFlipbook display]
+ -[BLSHFlipbook initForDisplay:platformProvider:]
+ -[BLSHFlipbook initForDisplay:platformProvider:].cold.1
+ -[BLSHFlipbook isCompositingWithLowPowerRenderer]
+ -[BLSHFlipbook setCompositingWithLowPowerRenderer:]
+ -[BLSHFlipbookFramesHistogram(CoreAnalytics) blsh_analyticsPayload]
+ -[BLSHFlipbookInvalidationTelemetryData(CoreAnalytics) blsh_analyticsEventName]
+ -[BLSHFlipbookInvalidationTelemetryData(CoreAnalytics) blsh_analyticsPayload]
+ -[BLSHFlipbookPowerSavingProvider display]
+ -[BLSHFlipbookPowerSavingProvider initForDisplay:]
+ -[BLSHFlipbookRenderSessionTelemetryData(CoreAnalytics) blsh_analyticsEventName]
+ -[BLSHFlipbookRenderSessionTelemetryData(CoreAnalytics) blsh_analyticsPayload]
+ -[BLSHFlipbookRequestDatesTelemetryData(CoreAnalytics) blsh_analyticsEventName]
+ -[BLSHFlipbookRequestDatesTelemetryData(CoreAnalytics) blsh_analyticsPayload]
+ -[BLSHForceActiveAttributeHandler .cxx_destruct]
+ -[BLSHForceActiveAttributeHandler display]
+ -[BLSHForceActiveAttributeHandler initForService:display:]
+ -[BLSHGlobal1HzFlipbookAttributeHandler display]
+ -[BLSHGlobalCacheFlipbookOnDisplayWakeAttributeHandler display]
+ -[BLSHGlobalHighLuminanceAlwaysOnAttributeHandler display]
+ -[BLSHGlobalUnrestrictedFramerateAttributeHandler display]
+ -[BLSHInfiniteResourceArbiter claimResource:]
+ -[BLSHInfiniteResourceOwnershipToken dealloc]
+ -[BLSHInfiniteResourceOwnershipToken dealloc].cold.1
+ -[BLSHInfiniteResourceOwnershipToken invalidate]
+ -[BLSHInfiniteResourceOwnershipToken isInvalidated]
+ -[BLSHInfiniteResourceOwnershipToken isOwned]
+ -[BLSHInfiniteResourceOwnershipToken setInvalidated:]
+ -[BLSHLocalAssertionAttributeHandler attributeClasses]
+ -[BLSHLocalAssertionAttributeHandler display]
+ -[BLSHLocalAssertionService queue_registerAttributeHandler:]
+ -[BLSHLocalAssertionService registerAttributeHandler:]
+ -[BLSHLocalHostSceneEnvironment clientNeedsFlipbookStateUpdates]
+ -[BLSHLocalHostSceneEnvironment clientNeedsLowPowerRenderingStateUpdates]
+ -[BLSHLocalHostSceneEnvironment updateToDateSpecifier:sceneContentsUpdated:lowPowerRenderingDisabled:]
+ -[BLSHLocalHostSceneEnvironment updateToDateSpecifier:sceneContentsUpdated:lowPowerRenderingDisabled:].cold.1
+ -[BLSHLocalHostSceneEnvironment updateToDateSpecifier:sceneContentsUpdated:lowPowerRenderingDisabled:].cold.2
+ -[BLSHLocalHostSceneEnvironment updateToDateSpecifier:sceneContentsUpdated:lowPowerRenderingDisabled:].cold.3
+ -[BLSHLocalHostSceneEnvironment updateToDateSpecifier:sceneContentsUpdated:lowPowerRenderingDisabled:].cold.4
+ -[BLSHLocalHostSceneEnvironment updateToDateSpecifier:sceneContentsUpdated:lowPowerRenderingDisabled:].cold.5
+ -[BLSHLocalHostSceneEnvironmentUpdater environmentStateMachine:didUpdateFlipbookVisualState:specifier:]
+ -[BLSHLowPowerRenderingAttributeHandler activateForSceneEnvironment:]
+ -[BLSHLowPowerRenderingAttributeHandler deactivateForSceneEnvironment:]
+ -[BLSHMeasureCommitOnWakeOperation .cxx_destruct]
+ -[BLSHMeasureCommitOnWakeOperation beginMeasurementForTransactionID:withCompletion:]
+ -[BLSHMeasureCommitOnWakeOperation beginMeasurementForTransactionID:withCompletion:].cold.1
+ -[BLSHMeasureCommitOnWakeOperation dealloc]
+ -[BLSHMeasureCommitOnWakeOperation dealloc].cold.1
+ -[BLSHMeasureCommitOnWakeOperation didTimeout]
+ -[BLSHMeasureCommitOnWakeOperation init]
+ -[BLSHMeasureCommitOnWakeOperation invalidate]
+ -[BLSHMeasureCommitOnWakeOperation invalidate].cold.1
+ -[BLSHMeasureCommitOnWakeOperation isCommitPending]
+ -[BLSHMeasureCommitOnWakeOperation performCommitToMeasure]
+ -[BLSHMeasureCommitOnWakeOperation performCommitToMeasure].cold.1
+ -[BLSHMeasureCommitOnWakeOperation performCommitToMeasure].cold.2
+ -[BLSHOSDisplayInterface .cxx_destruct]
+ -[BLSHOSDisplayInterface _didCompleteTransitionToDisplayMode:withError:]
+ -[BLSHOSDisplayInterface abortContextForTimer:]
+ -[BLSHOSDisplayInterface acquireDisplayPowerAssertionForReason:]
+ -[BLSHOSDisplayInterface acquireDisplayPowerAssertionForReason:].cold.1
+ -[BLSHOSDisplayInterface caDisplayPowerState]
+ -[BLSHOSDisplayInterface caDisplayState]
+ -[BLSHOSDisplayInterface caDisplay]
+ -[BLSHOSDisplayInterface cbDisplayMode]
+ -[BLSHOSDisplayInterface cbFlipbookState]
+ -[BLSHOSDisplayInterface clearCAWatchdog]
+ -[BLSHOSDisplayInterface createDisplayPowerResourceHintWithState:]
+ -[BLSHOSDisplayInterface createFlipbook]
+ -[BLSHOSDisplayInterface delegateQueue]
+ -[BLSHOSDisplayInterface didCompleteSwitchToFlipbookState:withError:]
+ -[BLSHOSDisplayInterface didCompleteTransitionToDisplayMode:withError:]
+ -[BLSHOSDisplayInterface didDetectSignificantUserInteraction]
+ -[BLSHOSDisplayInterface displayStateDelegate]
+ -[BLSHOSDisplayInterface display]
+ -[BLSHOSDisplayInterface doesMatchCADisplay:]
+ -[BLSHOSDisplayInterface endSuppressionService]
+ -[BLSHOSDisplayInterface highLuminanceAODsupportedInCB]
+ -[BLSHOSDisplayInterface identifier]
+ -[BLSHOSDisplayInterface initWithCADisplay:platformProvider:osInterfaceProvider:]
+ -[BLSHOSDisplayInterface initWithCADisplay:platformProvider:osInterfaceProvider:].cold.1
+ -[BLSHOSDisplayInterface isCloningDisabled]
+ -[BLSHOSDisplayInterface isFlipbookTransparent]
+ -[BLSHOSDisplayInterface isSuppressionServiceActive]
+ -[BLSHOSDisplayInterface lastSuppressionEvent]
+ -[BLSHOSDisplayInterface loggingName]
+ -[BLSHOSDisplayInterface notifyDelegateDidCompleteSwitchToCBFlipbookState:withError:]
+ -[BLSHOSDisplayInterface notifyDelegateDidCompleteTransitionToCBDisplayMode:withError:]
+ -[BLSHOSDisplayInterface notifyDisplayBlankedIfChangedForCADisplayState:]
+ -[BLSHOSDisplayInterface osInterfaceProvider]
+ -[BLSHOSDisplayInterface referenceId]
+ -[BLSHOSDisplayInterface registerHandlersForService:]
+ -[BLSHOSDisplayInterface registerHandlersForService:].cold.1
+ -[BLSHOSDisplayInterface scheduleOSIPWatchdogWithExplanation:type:]
+ -[BLSHOSDisplayInterface setCATransitionsDelayForTesting:]
+ -[BLSHOSDisplayInterface setCBTransitionsDelayForTesting:]
+ -[BLSHOSDisplayInterface setCloningDisabled:]
+ -[BLSHOSDisplayInterface setDisplayStateDelegate:]
+ -[BLSHOSDisplayInterface setFlipbookTransparent:]
+ -[BLSHOSDisplayInterface setLastSuppressionEvent:]
+ -[BLSHOSDisplayInterface startSuppressionServiceWithHandler:]
+ -[BLSHOSDisplayInterface supportsFlipbookState]
+ -[BLSHOSDisplayInterface surfaceType]
+ -[BLSHOSDisplayInterface switchToFlipbookState:]
+ -[BLSHOSDisplayInterface switchToFlipbookState:].cold.1
+ -[BLSHOSDisplayInterface timeoutForWatchdogType:]
+ -[BLSHOSDisplayInterface transitionToCADisplayState:]
+ -[BLSHOSDisplayInterface transitionToDisplayMode:withDuration:didChangeAlwaysOnBrightnessCurve:]
+ -[BLSHOSDisplayInterface transitionToDisplayMode:withDuration:didChangeAlwaysOnBrightnessCurve:].cold.1
+ -[BLSHPendingBacklightTelemetryEvent .cxx_destruct]
+ -[BLSHPendingBacklightTelemetryEvent backlightState]
+ -[BLSHPendingBacklightTelemetryEvent changeEvent]
+ -[BLSHPendingBacklightTelemetryEvent explanation]
+ -[BLSHPendingBacklightTelemetryEvent initWithBacklightState:sourceEvent:explanation:startTimestamp:changeEvent:]
+ -[BLSHPendingBacklightTelemetryEvent sourceEvent]
+ -[BLSHPendingBacklightTelemetryEvent startTimestamp]
+ -[BLSHPendingEnvironmentUpdate .cxx_destruct]
+ -[BLSHPendingEnvironmentUpdate currentOperation]
+ -[BLSHPendingEnvironmentUpdate description]
+ -[BLSHPendingEnvironmentUpdate environmentUpdateOperation]
+ -[BLSHPendingEnvironmentUpdate flipbookOperation]
+ -[BLSHPendingEnvironmentUpdate initWithFlipbookOperation:environmentUpdateOperation:flipbookFirst:]
+ -[BLSHPendingEnvironmentUpdate isBeforeDisplayBlankingChange]
+ -[BLSHPendingEnvironmentUpdate isCompleted]
+ -[BLSHPendingEnvironmentUpdate isStarted]
+ -[BLSHPendingEnvironmentUpdate setCompleted:]
+ -[BLSHPendingEnvironmentUpdate setStarted:]
+ -[BLSHPendingEnvironmentUpdate shouldBlockTransitionPassIsBeforeDisplayBlankingChange:willUnblank:didUnblank:]
+ -[BLSHPendingEnvironmentUpdate targetDisplayMode]
+ -[BLSHPendingEnvironmentUpdate type]
+ -[BLSHPendingEnvironmentUpdateOperation environmentUpdateOperation]
+ -[BLSHPendingEnvironmentUpdateOperation flipbookOperation]
+ -[BLSHPendingEnvironmentUpdateOperation initWithEvents:withInitialSpecifier:targetDisplayMode:]
+ -[BLSHPendingEnvironmentUpdateOperation isBeforeDisplayBlankingChange]
+ -[BLSHPendingEnvironmentUpdateOperation shouldBlockTransitionPassIsBeforeDisplayBlankingChange:willUnblank:didUnblank:]
+ -[BLSHPendingEnvironmentUpdateOperation targetDisplayMode]
+ -[BLSHPendingFlipbookVisualStateOperation .cxx_destruct]
+ -[BLSHPendingFlipbookVisualStateOperation description]
+ -[BLSHPendingFlipbookVisualStateOperation didUpdateInitialState]
+ -[BLSHPendingFlipbookVisualStateOperation environmentUpdateOperation]
+ -[BLSHPendingFlipbookVisualStateOperation events]
+ -[BLSHPendingFlipbookVisualStateOperation flipbookOperation]
+ -[BLSHPendingFlipbookVisualStateOperation initWithIsFlipbook:initialSpecifier:]
+ -[BLSHPendingFlipbookVisualStateOperation initWithIsFlipbook:initialSpecifier:events:targetDisplayMode:]
+ -[BLSHPendingFlipbookVisualStateOperation initialSpecifier]
+ -[BLSHPendingFlipbookVisualStateOperation isBeforeDisplayBlankingChange]
+ -[BLSHPendingFlipbookVisualStateOperation isCompleted]
+ -[BLSHPendingFlipbookVisualStateOperation isFlipbook]
+ -[BLSHPendingFlipbookVisualStateOperation isStarted]
+ -[BLSHPendingFlipbookVisualStateOperation setCompleted:]
+ -[BLSHPendingFlipbookVisualStateOperation setStarted:]
+ -[BLSHPendingFlipbookVisualStateOperation setUpdatedInitialState:]
+ -[BLSHPendingFlipbookVisualStateOperation shouldBlockTransitionPassIsBeforeDisplayBlankingChange:willUnblank:didUnblank:]
+ -[BLSHPendingFlipbookVisualStateOperation targetDisplayMode]
+ -[BLSHPendingFlipbookVisualStateOperation triggerEvent]
+ -[BLSHPendingFlipbookVisualStateOperation type]
+ -[BLSHPresentationDateSpecifier initWithPresentationDate:specifiers:lowPowerRenderingPresentationTime:sourceFrameType:]
+ -[BLSHPresentationDateSpecifier lowPowerRenderingPresentationTime]
+ -[BLSHPresentationDateSpecifier sourceFrameType]
+ -[BLSHPreventBacklightIdleAttributeHandler display]
+ -[BLSHPseudoFlipbook _stampLowPowerRenderingOnFrame:isLPR:]
+ -[BLSHPseudoFlipbook display]
+ -[BLSHPseudoFlipbook isCompositingWithLowPowerRenderer]
+ -[BLSHPseudoFlipbook lastRenderedFrame].cold.1
+ -[BLSHPseudoFlipbook setCompositingWithLowPowerRenderer:]
+ -[BLSHPseudoFlipbookAttributeHandler display]
+ -[BLSHPseudoFlipbookFrame lowPowerRenderingPresentationTime]
+ -[BLSHPseudoFlipbookFrame lowPowerRendering]
+ -[BLSHPseudoFlipbookFrame setLowPowerRendering:]
+ -[BLSHPseudoFlipbookFrame setLowPowerRenderingPresentationTime:]
+ -[BLSHResourceArbiter .cxx_destruct]
+ -[BLSHResourceArbiter claimResource:]
+ -[BLSHResourceArbiter initWithResourceCount:]
+ -[BLSHResourceArbiter init]
+ -[BLSHResourceArbiter tokenDidInvalidate:]
+ -[BLSHResourceOwnershipToken .cxx_destruct]
+ -[BLSHResourceOwnershipToken arbiter]
+ -[BLSHResourceOwnershipToken dealloc]
+ -[BLSHResourceOwnershipToken dealloc].cold.1
+ -[BLSHResourceOwnershipToken invalidate]
+ -[BLSHResourceOwnershipToken isInvalidated]
+ -[BLSHResourceOwnershipToken isOwned]
+ -[BLSHResourceOwnershipToken nonImmediateAcquireBlock]
+ -[BLSHResourceOwnershipToken setArbiter:]
+ -[BLSHResourceOwnershipToken setInvalidated:]
+ -[BLSHResourceOwnershipToken setNonImmediateAcquireBlock:]
+ -[BLSHResourceOwnershipToken setOwned:]
+ -[BLSHSceneRegistrationHostComponent invalidate]
+ -[BLSHSceneRegistrationHostComponent setScene:]
+ -[BLSHSceneRegistrationStore .cxx_destruct]
+ -[BLSHSceneRegistrationStore init]
+ -[BLSHSceneRegistrationStore registerScene:]
+ -[BLSHSceneRegistrationStore sceneForIdentityToken:]
+ -[BLSHSceneRegistrationStore unregisterScene:]
+ -[BLSHSourcedRenderedFlipbookFrame .cxx_destruct]
+ -[BLSHSourcedRenderedFlipbookFrame aplDimming]
+ -[BLSHSourcedRenderedFlipbookFrame apl]
+ -[BLSHSourcedRenderedFlipbookFrame bls_loggingString]
+ -[BLSHSourcedRenderedFlipbookFrame bls_shortLoggingString]
+ -[BLSHSourcedRenderedFlipbookFrame bls_specifier]
+ -[BLSHSourcedRenderedFlipbookFrame bls_uuid]
+ -[BLSHSourcedRenderedFlipbookFrame description]
+ -[BLSHSourcedRenderedFlipbookFrame frameId]
+ -[BLSHSourcedRenderedFlipbookFrame initWithFrame:sourceFrameType:]
+ -[BLSHSourcedRenderedFlipbookFrame isInverted]
+ -[BLSHSourcedRenderedFlipbookFrame lowPowerRenderingPresentationTime]
+ -[BLSHSourcedRenderedFlipbookFrame lowPowerRendering]
+ -[BLSHSourcedRenderedFlipbookFrame memoryUsage]
+ -[BLSHSourcedRenderedFlipbookFrame presentationTime]
+ -[BLSHSourcedRenderedFlipbookFrame rawSurfaceFrame]
+ -[BLSHSourcedRenderedFlipbookFrame rawSurface]
+ -[BLSHSourcedRenderedFlipbookFrame surface]
+ -[BLSHSystemWakeTelemetry .cxx_destruct]
+ -[BLSHSystemWakeTelemetry dealloc]
+ -[BLSHSystemWakeTelemetry initWithDelegate:]
+ -[BLSHSystemWakeTelemetry init]
+ -[BLSHSystemWakeTelemetry logTelemetryForInvalidation:]
+ -[BLSHSystemWakeTelemetry logTelemetryForRenderSession:]
+ -[BLSHSystemWakeTelemetry logTelemetryForRequestDates:]
+ -[BLSHSystemWakeTelemetry platformDelegate]
+ -[BLSHSystemWakeTelemetry setPlatformDelegate:]
+ -[BLSHSystemWakeTelemetry startObserving]
+ -[BLSHSystemWakeTelemetryMetrics .cxx_destruct]
+ -[BLSHSystemWakeTelemetryMetrics changedSettingsWhileOffCount]
+ -[BLSHSystemWakeTelemetryMetrics confirmedPossibleCount]
+ -[BLSHSystemWakeTelemetryMetrics discardedFramesUpTo2mStale]
+ -[BLSHSystemWakeTelemetryMetrics discardedFramesUpTo3mStale]
+ -[BLSHSystemWakeTelemetryMetrics discardedFramesUpTo4mStale]
+ -[BLSHSystemWakeTelemetryMetrics discardedFramesUpTo5mStale]
+ -[BLSHSystemWakeTelemetryMetrics discardedFramesUpTo6mStale]
+ -[BLSHSystemWakeTelemetryMetrics displayOffCount]
+ -[BLSHSystemWakeTelemetryMetrics displayOnCount]
+ -[BLSHSystemWakeTelemetryMetrics endContinuousSeconds]
+ -[BLSHSystemWakeTelemetryMetrics enteringAOTCount]
+ -[BLSHSystemWakeTelemetryMetrics expiredPossibleCount]
+ -[BLSHSystemWakeTelemetryMetrics flipbookLayoutSeconds]
+ -[BLSHSystemWakeTelemetryMetrics flipbookRenderSeconds]
+ -[BLSHSystemWakeTelemetryMetrics invalidatedFramesUpTo2mStale]
+ -[BLSHSystemWakeTelemetryMetrics invalidatedFramesUpTo3mStale]
+ -[BLSHSystemWakeTelemetryMetrics invalidatedFramesUpTo4mStale]
+ -[BLSHSystemWakeTelemetryMetrics invalidatedFramesUpTo5mStale]
+ -[BLSHSystemWakeTelemetryMetrics invalidatedFramesUpTo6mStale]
+ -[BLSHSystemWakeTelemetryMetrics noTimeSetCount]
+ -[BLSHSystemWakeTelemetryMetrics platformContext]
+ -[BLSHSystemWakeTelemetryMetrics possibleCount]
+ -[BLSHSystemWakeTelemetryMetrics rejectedPossibleCount]
+ -[BLSHSystemWakeTelemetryMetrics renderedFrameCount]
+ -[BLSHSystemWakeTelemetryMetrics renderedPartialMinuteCount]
+ -[BLSHSystemWakeTelemetryMetrics renderedPresentationSeconds]
+ -[BLSHSystemWakeTelemetryMetrics rtcAlarmsCount]
+ -[BLSHSystemWakeTelemetryMetrics secondsDisplayOff]
+ -[BLSHSystemWakeTelemetryMetrics secondsDisplayOn]
+ -[BLSHSystemWakeTelemetryMetrics secondsShowingAOT]
+ -[BLSHSystemWakeTelemetryMetrics serializedPayload]
+ -[BLSHSystemWakeTelemetryMetrics setChangedSettingsWhileOffCount:]
+ -[BLSHSystemWakeTelemetryMetrics setConfirmedPossibleCount:]
+ -[BLSHSystemWakeTelemetryMetrics setDiscardedFramesUpTo2mStale:]
+ -[BLSHSystemWakeTelemetryMetrics setDiscardedFramesUpTo3mStale:]
+ -[BLSHSystemWakeTelemetryMetrics setDiscardedFramesUpTo4mStale:]
+ -[BLSHSystemWakeTelemetryMetrics setDiscardedFramesUpTo5mStale:]
+ -[BLSHSystemWakeTelemetryMetrics setDiscardedFramesUpTo6mStale:]
+ -[BLSHSystemWakeTelemetryMetrics setDisplayOffCount:]
+ -[BLSHSystemWakeTelemetryMetrics setDisplayOnCount:]
+ -[BLSHSystemWakeTelemetryMetrics setEndContinuousSeconds:]
+ -[BLSHSystemWakeTelemetryMetrics setEnteringAOTCount:]
+ -[BLSHSystemWakeTelemetryMetrics setExpiredPossibleCount:]
+ -[BLSHSystemWakeTelemetryMetrics setFlipbookLayoutSeconds:]
+ -[BLSHSystemWakeTelemetryMetrics setFlipbookRenderSeconds:]
+ -[BLSHSystemWakeTelemetryMetrics setInvalidatedFramesUpTo2mStale:]
+ -[BLSHSystemWakeTelemetryMetrics setInvalidatedFramesUpTo3mStale:]
+ -[BLSHSystemWakeTelemetryMetrics setInvalidatedFramesUpTo4mStale:]
+ -[BLSHSystemWakeTelemetryMetrics setInvalidatedFramesUpTo5mStale:]
+ -[BLSHSystemWakeTelemetryMetrics setInvalidatedFramesUpTo6mStale:]
+ -[BLSHSystemWakeTelemetryMetrics setNoTimeSetCount:]
+ -[BLSHSystemWakeTelemetryMetrics setPlatformContext:]
+ -[BLSHSystemWakeTelemetryMetrics setPossibleCount:]
+ -[BLSHSystemWakeTelemetryMetrics setRejectedPossibleCount:]
+ -[BLSHSystemWakeTelemetryMetrics setRenderedFrameCount:]
+ -[BLSHSystemWakeTelemetryMetrics setRenderedPartialMinuteCount:]
+ -[BLSHSystemWakeTelemetryMetrics setRenderedPresentationSeconds:]
+ -[BLSHSystemWakeTelemetryMetrics setRtcAlarmsCount:]
+ -[BLSHSystemWakeTelemetryMetrics setSecondsDisplayOff:]
+ -[BLSHSystemWakeTelemetryMetrics setSecondsDisplayOn:]
+ -[BLSHSystemWakeTelemetryMetrics setSecondsShowingAOT:]
+ -[BLSHSystemWakeTelemetryMetrics setSleepCount:]
+ -[BLSHSystemWakeTelemetryMetrics setSleepOver2mCount:]
+ -[BLSHSystemWakeTelemetryMetrics setSleepOver3mCount:]
+ -[BLSHSystemWakeTelemetryMetrics setSleepOver4mCount:]
+ -[BLSHSystemWakeTelemetryMetrics setSleepOver5mCount:]
+ -[BLSHSystemWakeTelemetryMetrics setSleepOver6mCount:]
+ -[BLSHSystemWakeTelemetryMetrics setSoftwareRequestCount:]
+ -[BLSHSystemWakeTelemetryMetrics setStartContinuousSeconds:]
+ -[BLSHSystemWakeTelemetryMetrics setTotalTimeSeconds:]
+ -[BLSHSystemWakeTelemetryMetrics setWakeCount:]
+ -[BLSHSystemWakeTelemetryMetrics sleepCount]
+ -[BLSHSystemWakeTelemetryMetrics sleepOver2mCount]
+ -[BLSHSystemWakeTelemetryMetrics sleepOver3mCount]
+ -[BLSHSystemWakeTelemetryMetrics sleepOver4mCount]
+ -[BLSHSystemWakeTelemetryMetrics sleepOver5mCount]
+ -[BLSHSystemWakeTelemetryMetrics sleepOver6mCount]
+ -[BLSHSystemWakeTelemetryMetrics softwareRequestCount]
+ -[BLSHSystemWakeTelemetryMetrics startContinuousSeconds]
+ -[BLSHSystemWakeTelemetryMetrics totalTimeSeconds]
+ -[BLSHSystemWakeTelemetryMetrics wakeCount]
+ -[BLSHTransparentFlipbookAttributeHandler display]
+ -[BLSHValidWhenBacklightInactiveAttributeHandler .cxx_destruct]
+ -[BLSHValidWhenBacklightInactiveAttributeHandler display]
+ -[BLSHValidWhenBacklightInactiveAttributeHandler initForService:display:]
+ -[BLSHWatchdogProvider listenForOSStartupComplete]
+ -[BLSHWatchdogProvider makeStartupCheck]
+ -[BLSHWatchdogProvider prepareForStartupCheck]
+ -[BLSHXPCAssertionServiceHost displays]
+ -[BLSHXPCAssertionServiceHost initWithLocalService:peer:osInterfaceProvider:]
+ -[BLSHXPCAssertionServiceHostServer _handleIncomingConnection:]
+ -[BLSHXPCAssertionServiceHostServer _handleIncomingConnection:].cold.1
+ -[BLSHXPCAssertionServiceHostServer initWithLocalAssertionService:osInterfaceProvider:]
+ -[BLSHXPCAssertionServiceHostServer initWithLocalAssertionService:osInterfaceProvider:].cold.1
+ -[BLSHXPCAssertionServiceHostServer initWithLocalAssertionService:osInterfaceProvider:].cold.2
+ -[BLSHXPCBacklightProxyHost initWithLocalBacklightProxy:peer:display:]
+ -[BLSHXPCBacklightProxyHostServer _handleIncomingConnection:]
+ -[BLSHXPCBacklightProxyHostServer _handleIncomingConnection:].cold.1
+ -[BLSHXPCBacklightProxyHostServer _handleIncomingConnection:].cold.2
+ -[BLSHXPCBacklightProxyHostServer init]
+ -[BLSHXPCBacklightProxyHostServer init].cold.1
+ -[BLSHXPCBacklightProxyHostServer init].cold.2
+ -[CAFlipBookFrame(BacklightServicesHost) lowPowerRenderingPresentationTime]
+ -[CAFlipBookFrame(BacklightServicesHost) lowPowerRendering]
+ -[NSDictionary(BLSFlatten) bls_flattenWithSeparator:key:]
+ GCC_except_table146
+ GCC_except_table17
+ GCC_except_table19
+ GCC_except_table29
+ GCC_except_table32
+ GCC_except_table33
+ GCC_except_table35
+ GCC_except_table44
+ GCC_except_table45
+ GCC_except_table46
+ GCC_except_table48
+ GCC_except_table5
+ GCC_except_table69
+ GCC_except_table75
+ GCC_except_table79
+ GCC_except_table88
+ GCC_except_table90
+ _AnalyticsSendEventLazy
+ _BLSClientNeedsFlipbookStateUpdatesForEnvironment
+ _BLSClientNeedsLowPowerRenderingStateUpdatesForEnvironment
+ _BLSHIsTelemetryDisabledViaDefault.onceToken
+ _BLSHIsTelemetryDisabledViaDefault.sDisableTelemetry
+ _BLSHTailspinQueue.onceToken
+ _BLSHTailspinQueue.queue
+ _BLSIsLowPowerRenderingForEnvironment
+ _MaxPowerBLSBacklightDisplayMode
+ _MaxPowerBLSBacklightState
+ _MaxPowerBLSFlipbookState
+ _OBJC_CLASS_$_BKSDisplayService
+ _OBJC_CLASS_$_BLSAssertionDescriptor
+ _OBJC_CLASS_$_BLSDisableLowPowerRenderingAttribute
+ _OBJC_CLASS_$_BLSDisplayAttribute
+ _OBJC_CLASS_$_BLSDisplayReference
+ _OBJC_CLASS_$_BLSHAOTSystemWakeTelemetry
+ _OBJC_CLASS_$_BLSHAggregateBacklightHost
+ _OBJC_CLASS_$_BLSHAggregateHostCachedState
+ _OBJC_CLASS_$_BLSHBacklightEnvironmentSessionProvider
+ _OBJC_CLASS_$_BLSHBacklightEventMetrics
+ _OBJC_CLASS_$_BLSHBacklightWakeTelemetryEvent
+ _OBJC_CLASS_$_BLSHBacklightWakeTelemetryTracker
+ _OBJC_CLASS_$_BLSHCATransactionTelemetryContext
+ _OBJC_CLASS_$_BLSHCoreAnalytics
+ _OBJC_CLASS_$_BLSHDisableLowPowerRenderingAttributeHandler
+ _OBJC_CLASS_$_BLSHDisplayWakeTelemetry
+ _OBJC_CLASS_$_BLSHInfiniteResourceArbiter
+ _OBJC_CLASS_$_BLSHInfiniteResourceOwnershipToken
+ _OBJC_CLASS_$_BLSHLowPowerRenderingAttributeHandler
+ _OBJC_CLASS_$_BLSHMeasureCommitOnWakeOperation
+ _OBJC_CLASS_$_BLSHOSDisplayInterface
+ _OBJC_CLASS_$_BLSHPendingBacklightTelemetryEvent
+ _OBJC_CLASS_$_BLSHPendingEnvironmentUpdate
+ _OBJC_CLASS_$_BLSHPendingFlipbookVisualStateOperation
+ _OBJC_CLASS_$_BLSHResourceArbiter
+ _OBJC_CLASS_$_BLSHResourceOwnershipToken
+ _OBJC_CLASS_$_BLSHSceneRegistrationExtension
+ _OBJC_CLASS_$_BLSHSceneRegistrationHostComponent
+ _OBJC_CLASS_$_BLSHSceneRegistrationStore
+ _OBJC_CLASS_$_BLSHSourcedRenderedFlipbookFrame
+ _OBJC_CLASS_$_BLSHSystemWakeTelemetry
+ _OBJC_CLASS_$_BLSHSystemWakeTelemetryMetrics
+ _OBJC_CLASS_$_BLSLowPowerRenderingAttribute
+ _OBJC_CLASS_$_BSServiceConnectionListenerConfiguration
+ _OBJC_CLASS_$_BSServiceDispatchQueue
+ _OBJC_CLASS_$_CATransaction
+ _OBJC_CLASS_$_FBSSceneComponent
+ _OBJC_CLASS_$_FBSSceneExtension
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_CLASS_$_NSThread
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._accumulatedFlipbookLayoutDuration
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._accumulatedFlipbookRenderDuration
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._accumulatedMetrics
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._accumulatedSecondsDisplayOff
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._accumulatedSecondsDisplayOn
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._accumulatedSecondsShowingAOT
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._backlightOffStartTime
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._backlightOnStartTime
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._blsTelemetryEnabled
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._completedWakeNumber
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._currentMetrics
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._delegateFlags
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._didFinalLog
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._hasPoweredOnTime
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._isAOT
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._isTelemetryEnqueuedAtUtilityQOS
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._lastTelemtryAccumulateTime
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._loggedToTelemtryAccumulateTime
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._powerLogTelemetryIdentifier
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._serviceStarted
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._systemSleepObserver
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._systemWakeMetricsEventKey
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._timer
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._timerQueue
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._wakeNumber
+ _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._willSleepTime
+ _OBJC_IVAR_$_BLSHAggregateBacklightHost._backlightHosts
+ _OBJC_IVAR_$_BLSHAggregateBacklightHost._deviceSupportsAlwaysOn
+ _OBJC_IVAR_$_BLSHAggregateBacklightHost._display
+ _OBJC_IVAR_$_BLSHAggregateBacklightHost._lock
+ _OBJC_IVAR_$_BLSHAggregateBacklightHost._lock_aggregateStateChangeTimestamp
+ _OBJC_IVAR_$_BLSHAggregateBacklightHost._lock_cachedState
+ _OBJC_IVAR_$_BLSHAggregateBacklightHost._lock_cachedStatesByHost
+ _OBJC_IVAR_$_BLSHAggregateBacklightHost._lock_observers
+ _OBJC_IVAR_$_BLSHAggregateHostCachedState._alwaysOnEnabled
+ _OBJC_IVAR_$_BLSHAggregateHostCachedState._backlightState
+ _OBJC_IVAR_$_BLSHAggregateHostCachedState._displayMode
+ _OBJC_IVAR_$_BLSHAggregateHostCachedState._flipbookState
+ _OBJC_IVAR_$_BLSHAggregateHostCachedState._targetDisplayMode
+ _OBJC_IVAR_$_BLSHAggregateHostCachedState._willTransitionBacklightState
+ _OBJC_IVAR_$_BLSHAlwaysOnPresentationEngine._display
+ _OBJC_IVAR_$_BLSHAlwaysOnPresentationEngine._displayLoggingName
+ _OBJC_IVAR_$_BLSHAlwaysOnPresentationEngine._lock_lowPowerRendering
+ _OBJC_IVAR_$_BLSHAlwaysOnPresentationEngine._lock_lowPowerRenderingDisabled
+ _OBJC_IVAR_$_BLSHBacklightDisplayStateMachine._display
+ _OBJC_IVAR_$_BLSHBacklightDisplayStateMachine._displayLoggingName
+ _OBJC_IVAR_$_BLSHBacklightEnvironmentSessionProvider._lock
+ _OBJC_IVAR_$_BLSHBacklightEnvironmentSessionProvider._lock_providersByDisplayId
+ _OBJC_IVAR_$_BLSHBacklightEnvironmentSessionProvider._perDisplayFactory
+ _OBJC_IVAR_$_BLSHBacklightEnvironmentStateMachine._lock_updatingFlipbookVisualState
+ _OBJC_IVAR_$_BLSHBacklightEnvironmentStateMachine._updatingFlipbookIsFlipbook
+ _OBJC_IVAR_$_BLSHBacklightEnvironmentStateMachine._updatingFlipbookSpecifier
+ _OBJC_IVAR_$_BLSHBacklightEventMetrics._abortedEventsCount
+ _OBJC_IVAR_$_BLSHBacklightEventMetrics._allEventsToWakeDurationSeconds
+ _OBJC_IVAR_$_BLSHBacklightEventMetrics._beforeKernelWake
+ _OBJC_IVAR_$_BLSHBacklightEventMetrics._completedEventsCount
+ _OBJC_IVAR_$_BLSHBacklightEventMetrics._compressionsDiff
+ _OBJC_IVAR_$_BLSHBacklightEventMetrics._didCompleteDurationSeconds
+ _OBJC_IVAR_$_BLSHBacklightEventMetrics._didTimeoutSystemActivity
+ _OBJC_IVAR_$_BLSHBacklightEventMetrics._displayIdentifier
+ _OBJC_IVAR_$_BLSHBacklightEventMetrics._durationSeconds
+ _OBJC_IVAR_$_BLSHBacklightEventMetrics._endpoint
+ _OBJC_IVAR_$_BLSHBacklightEventMetrics._eventType
+ _OBJC_IVAR_$_BLSHBacklightEventMetrics._explanation
+ _OBJC_IVAR_$_BLSHBacklightEventMetrics._pageinDiff
+ _OBJC_IVAR_$_BLSHBacklightEventMetrics._performEventCount
+ _OBJC_IVAR_$_BLSHBacklightEventMetrics._platformContext
+ _OBJC_IVAR_$_BLSHBacklightEventMetrics._secondsAfterKernelWake
+ _OBJC_IVAR_$_BLSHBacklightEventMetrics._sourceEvent
+ _OBJC_IVAR_$_BLSHBacklightEventMetrics._systemActivityAcquisitionDetails
+ _OBJC_IVAR_$_BLSHBacklightEventMetrics._systemActivityAcquisitionSeconds
+ _OBJC_IVAR_$_BLSHBacklightEventMetrics._systemActivityAcquisitionSkipped
+ _OBJC_IVAR_$_BLSHBacklightEventMetrics._systemActivityAcquisitionSuccess
+ _OBJC_IVAR_$_BLSHBacklightEventMetrics._timeoutTriggeredBlackFlash
+ _OBJC_IVAR_$_BLSHBacklightEventMetrics._wakeReason
+ _OBJC_IVAR_$_BLSHBacklightEventMetrics._wasInactiveOn
+ _OBJC_IVAR_$_BLSHBacklightFBSceneHostEnvironment._lock_lowPowerRendering
+ _OBJC_IVAR_$_BLSHBacklightFBSceneHostEnvironment._lock_lowPowerRenderingPresentationTime
+ _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._displayInterfaces
+ _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._displayReferences
+ _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._flipbookArbiter
+ _OBJC_IVAR_$_BLSHBacklightService._displayWakeTelemetries
+ _OBJC_IVAR_$_BLSHBacklightService._stateMachines
+ _OBJC_IVAR_$_BLSHBacklightService._transitionStateMachines
+ _OBJC_IVAR_$_BLSHBacklightStateMachine._display
+ _OBJC_IVAR_$_BLSHBacklightStateMachine._displayLoggingName
+ _OBJC_IVAR_$_BLSHBacklightTransitionStateMachine._display
+ _OBJC_IVAR_$_BLSHBacklightTransitionStateMachine._displayLoggingName
+ _OBJC_IVAR_$_BLSHBacklightTransitionStateMachine._flipbookArbiter
+ _OBJC_IVAR_$_BLSHBacklightTransitionStateMachine._lock_flipbookToken
+ _OBJC_IVAR_$_BLSHBacklightTransitionStateMachine._powerResourceHint
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryEvent._abortedEventsCount
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryEvent._allEventsToWakeDurationSeconds
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryEvent._beforeKernelWake
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryEvent._completedEventsCount
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryEvent._compressionsDiff
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryEvent._didCompleteDurationSeconds
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryEvent._didTimeoutSystemActivty
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryEvent._endpoint
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryEvent._pageinDiff
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryEvent._performEventCount
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryEvent._secondsAfterKernelWake
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryEvent._systemActivityAcquisitionDetails
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryEvent._systemActivityAcquisitionSeconds
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryEvent._systemActivityAcquisitionSkipped
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryEvent._systemActivityAcquisitionSuccess
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryEvent._timeoutTriggeredBlackFlash
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryEvent._wakeDurationSeconds
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryEvent._wakeReason
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryEvent._wasInactiveOn
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_abortedEventsCount
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_beforeKernelWake
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_beginMachTime
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_commitOnWakeMeasurementDisabled
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_completedEventsCount
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_completion
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_completionPending
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_didAcquireSystemActivity
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_didBegin
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_didCompleteDurationSeconds
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_didCompleteUpdate
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_didMeasure
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_didTimeout
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_didUnblank
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_hadExistingSystemActivity
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_initialEvent
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_invalidated
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_lastEvent
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_pendingEndTime
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_pendingEndpoint
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_performEventCounter
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_secondsAfterKernelWake
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_systemActivityAcquisitionSeconds
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_systemActivityDetails
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_systemActivityDidTimeout
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_systemActivitySuccess
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_timeoutTriggeredBlackFlash
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_triggerEvent
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_vmStatsBegin
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._lock_vmStatsPendingEnd
+ _OBJC_IVAR_$_BLSHBacklightWakeTelemetryTracker._measureCommitOnWakeOperation
+ _OBJC_IVAR_$_BLSHBaseBacklightEnvironmentSessionProvider._display
+ _OBJC_IVAR_$_BLSHBasePlatformProvider._lock_sessionProviderFactory
+ _OBJC_IVAR_$_BLSHBaseSceneHostEnvironment._lock_lowPowerRendering
+ _OBJC_IVAR_$_BLSHCATransactionTelemetryContext._active
+ _OBJC_IVAR_$_BLSHCATransactionTelemetryContext._beginMachTime
+ _OBJC_IVAR_$_BLSHCATransactionTelemetryContext._elapsedMSActive
+ _OBJC_IVAR_$_BLSHCATransactionTelemetryContext._elapsedSecondsActive
+ _OBJC_IVAR_$_BLSHCATransactionTelemetryContext._generatedSeed
+ _OBJC_IVAR_$_BLSHCATransactionTelemetryContext._hasBegun
+ _OBJC_IVAR_$_BLSHCATransactionTelemetryContext._shouldGenerateSeed
+ _OBJC_IVAR_$_BLSHCATransactionTelemetryContext._stateHandler
+ _OBJC_IVAR_$_BLSHCATransactionTelemetryContext._transactionID
+ _OBJC_IVAR_$_BLSHDisableLowPowerRenderingAttributeHandler._provider
+ _OBJC_IVAR_$_BLSHDisplayWakeTelemetry._analyticsRecorder
+ _OBJC_IVAR_$_BLSHDisplayWakeTelemetry._backlightEventPowerLogIdentifier
+ _OBJC_IVAR_$_BLSHDisplayWakeTelemetry._backlightEventTelemetryEnabled
+ _OBJC_IVAR_$_BLSHDisplayWakeTelemetry._complicationDescriptions
+ _OBJC_IVAR_$_BLSHDisplayWakeTelemetry._delegateFlags
+ _OBJC_IVAR_$_BLSHDisplayWakeTelemetry._displayIdentifier
+ _OBJC_IVAR_$_BLSHDisplayWakeTelemetry._faceDescription
+ _OBJC_IVAR_$_BLSHDisplayWakeTelemetry._lock
+ _OBJC_IVAR_$_BLSHDisplayWakeTelemetry._lock_activeWakeTelemetryTracker
+ _OBJC_IVAR_$_BLSHDisplayWakeTelemetry._lock_commitOnWakeMeasurementDisabled
+ _OBJC_IVAR_$_BLSHDisplayWakeTelemetry._lock_pendingWakeTelemetryTrackers
+ _OBJC_IVAR_$_BLSHDisplayWakeTelemetry._pendingBacklightTelemetryEvent
+ _OBJC_IVAR_$_BLSHDisplayWakeTelemetry._pendingBacklightTelemetryEventLock
+ _OBJC_IVAR_$_BLSHDisplayWakeTelemetry._platformDelegate
+ _OBJC_IVAR_$_BLSHDisplayWakeTelemetry._surfaceType
+ _OBJC_IVAR_$_BLSHDisplayWakeTelemetry._telemetrySource
+ _OBJC_IVAR_$_BLSHEngineRenderFlipbookSession._display
+ _OBJC_IVAR_$_BLSHEnvironmentTransitionStateTarget._hasExplicitFlipbook
+ _OBJC_IVAR_$_BLSHEnvironmentTransitionStateTarget._isFlipbook
+ _OBJC_IVAR_$_BLSHEnvironmentTransitionStateTarget._lowPowerRenderingPresentationTime
+ _OBJC_IVAR_$_BLSHFlipbook._dateToMachTimeCache
+ _OBJC_IVAR_$_BLSHFlipbook._display
+ _OBJC_IVAR_$_BLSHFlipbookPowerSavingProvider._display
+ _OBJC_IVAR_$_BLSHForceActiveAttributeHandler._display
+ _OBJC_IVAR_$_BLSHInfiniteResourceOwnershipToken._invalidated
+ _OBJC_IVAR_$_BLSHMeasureCommitOnWakeOperation._lock
+ _OBJC_IVAR_$_BLSHMeasureCommitOnWakeOperation._lock_caTransaction
+ _OBJC_IVAR_$_BLSHMeasureCommitOnWakeOperation._lock_didBegin
+ _OBJC_IVAR_$_BLSHMeasureCommitOnWakeOperation._lock_didComplete
+ _OBJC_IVAR_$_BLSHMeasureCommitOnWakeOperation._lock_didTimeout
+ _OBJC_IVAR_$_BLSHMeasureCommitOnWakeOperation._lock_invalidated
+ _OBJC_IVAR_$_BLSHMeasureCommitOnWakeOperation._lock_timeoutTimer
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._backlightDimmedFactor
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._caDisplay
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._caTransitionsDelayForTesting
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._cbTransitionsDelayForTesting
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._deviceSupportsAlwaysOn
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._deviceSupportsAlwaysOnFlipbook
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._displayStateClient
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._displayStateClientSupported
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._displayStateControl
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._displayStateDelegate
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._highLuminanceAODsupportedInCB
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._identifier
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._lock
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._lock_CAWatchdogTimer
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._lock_CAWatchdogType
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._lock_CBWatchdogTimer
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._lock_CBWatchdogType
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._lock_caDisplayState
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._lock_cbDisplayMode
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._lock_cbFlipbookState
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._lock_cloningDisabled
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._lock_flipbookTransparent
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._lock_lastSuppressionEvent
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._lock_notifiedCADisplayState
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._lock_suppressionServiceActive
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._loggingName
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._osInterfaceProvider
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._platformProvider
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._referenceId
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._setCBDisplayModeTimer
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._suppressionManager
+ _OBJC_IVAR_$_BLSHOSDisplayInterface._surfaceType
+ _OBJC_IVAR_$_BLSHPendingBacklightTelemetryEvent._backlightState
+ _OBJC_IVAR_$_BLSHPendingBacklightTelemetryEvent._changeEvent
+ _OBJC_IVAR_$_BLSHPendingBacklightTelemetryEvent._explanation
+ _OBJC_IVAR_$_BLSHPendingBacklightTelemetryEvent._sourceEvent
+ _OBJC_IVAR_$_BLSHPendingBacklightTelemetryEvent._startTimestamp
+ _OBJC_IVAR_$_BLSHPendingEnvironmentUpdate._completed
+ _OBJC_IVAR_$_BLSHPendingEnvironmentUpdate._environmentUpdateOperation
+ _OBJC_IVAR_$_BLSHPendingEnvironmentUpdate._flipbookFirst
+ _OBJC_IVAR_$_BLSHPendingEnvironmentUpdate._flipbookOperation
+ _OBJC_IVAR_$_BLSHPendingEnvironmentUpdate._started
+ _OBJC_IVAR_$_BLSHPendingEnvironmentUpdateOperation._targetDisplayMode
+ _OBJC_IVAR_$_BLSHPendingFlipbookVisualStateOperation._completed
+ _OBJC_IVAR_$_BLSHPendingFlipbookVisualStateOperation._events
+ _OBJC_IVAR_$_BLSHPendingFlipbookVisualStateOperation._initialSpecifier
+ _OBJC_IVAR_$_BLSHPendingFlipbookVisualStateOperation._isFlipbook
+ _OBJC_IVAR_$_BLSHPendingFlipbookVisualStateOperation._started
+ _OBJC_IVAR_$_BLSHPendingFlipbookVisualStateOperation._targetDisplayMode
+ _OBJC_IVAR_$_BLSHPendingFlipbookVisualStateOperation._updatedInitialState
+ _OBJC_IVAR_$_BLSHPresentationDateSpecifier._lowPowerRenderingPresentationTime
+ _OBJC_IVAR_$_BLSHPresentationDateSpecifier._sourceFrameType
+ _OBJC_IVAR_$_BLSHPseudoFlipbook._lock_compositingWithLowPowerRenderer
+ _OBJC_IVAR_$_BLSHPseudoFlipbookFrame._lowPowerRendering
+ _OBJC_IVAR_$_BLSHPseudoFlipbookFrame._lowPowerRenderingPresentationTime
+ _OBJC_IVAR_$_BLSHResourceArbiter._lock
+ _OBJC_IVAR_$_BLSHResourceArbiter._lock_currentOwners
+ _OBJC_IVAR_$_BLSHResourceArbiter._lock_pendingTokens
+ _OBJC_IVAR_$_BLSHResourceArbiter._resourceCount
+ _OBJC_IVAR_$_BLSHResourceOwnershipToken._arbiter
+ _OBJC_IVAR_$_BLSHResourceOwnershipToken._invalidated
+ _OBJC_IVAR_$_BLSHResourceOwnershipToken._nonImmediateAcquireBlock
+ _OBJC_IVAR_$_BLSHResourceOwnershipToken._owned
+ _OBJC_IVAR_$_BLSHSceneRegistrationStore._lock
+ _OBJC_IVAR_$_BLSHSceneRegistrationStore._lock_sceneLookup
+ _OBJC_IVAR_$_BLSHService._systemWakeTelemetry
+ _OBJC_IVAR_$_BLSHSourcedRenderedFlipbookFrame._sourceFrameType
+ _OBJC_IVAR_$_BLSHSourcedRenderedFlipbookFrame._wrappedFrame
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._platformDelegate
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._changedSettingsWhileOffCount
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._confirmedPossibleCount
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._discardedFramesUpTo2mStale
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._discardedFramesUpTo3mStale
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._discardedFramesUpTo4mStale
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._discardedFramesUpTo5mStale
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._discardedFramesUpTo6mStale
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._displayOffCount
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._displayOnCount
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._endContinuousSeconds
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._enteringAOTCount
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._expiredPossibleCount
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._flipbookLayoutSeconds
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._flipbookRenderSeconds
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._invalidatedFramesUpTo2mStale
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._invalidatedFramesUpTo3mStale
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._invalidatedFramesUpTo4mStale
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._invalidatedFramesUpTo5mStale
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._invalidatedFramesUpTo6mStale
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._noTimeSetCount
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._platformContext
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._possibleCount
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._rejectedPossibleCount
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._renderedFrameCount
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._renderedPartialMinuteCount
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._renderedPresentationSeconds
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._rtcAlarmsCount
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._secondsDisplayOff
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._secondsDisplayOn
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._secondsShowingAOT
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._sleepCount
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._sleepOver2mCount
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._sleepOver3mCount
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._sleepOver4mCount
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._sleepOver5mCount
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._sleepOver6mCount
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._softwareRequestCount
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._startContinuousSeconds
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._totalTimeSeconds
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetryMetrics._wakeCount
+ _OBJC_IVAR_$_BLSHValidWhenBacklightInactiveAttributeHandler._display
+ _OBJC_IVAR_$_BLSHXPCAssertionServiceHost._osInterfaceProvider
+ _OBJC_IVAR_$_BLSHXPCAssertionServiceHost._remoteToken
+ _OBJC_IVAR_$_BLSHXPCAssertionServiceHostServer._osInterfaceProvider
+ _OBJC_IVAR_$_BLSHXPCBacklightProxyHost._display
+ _OBJC_METACLASS_$_BLSHAOTSystemWakeTelemetry
+ _OBJC_METACLASS_$_BLSHAggregateBacklightHost
+ _OBJC_METACLASS_$_BLSHAggregateHostCachedState
+ _OBJC_METACLASS_$_BLSHBacklightEnvironmentSessionProvider
+ _OBJC_METACLASS_$_BLSHBacklightEventMetrics
+ _OBJC_METACLASS_$_BLSHBacklightWakeTelemetryEvent
+ _OBJC_METACLASS_$_BLSHBacklightWakeTelemetryTracker
+ _OBJC_METACLASS_$_BLSHCATransactionTelemetryContext
+ _OBJC_METACLASS_$_BLSHCoreAnalytics
+ _OBJC_METACLASS_$_BLSHDisableLowPowerRenderingAttributeHandler
+ _OBJC_METACLASS_$_BLSHDisplayWakeTelemetry
+ _OBJC_METACLASS_$_BLSHInfiniteResourceArbiter
+ _OBJC_METACLASS_$_BLSHInfiniteResourceOwnershipToken
+ _OBJC_METACLASS_$_BLSHLowPowerRenderingAttributeHandler
+ _OBJC_METACLASS_$_BLSHMeasureCommitOnWakeOperation
+ _OBJC_METACLASS_$_BLSHOSDisplayInterface
+ _OBJC_METACLASS_$_BLSHPendingBacklightTelemetryEvent
+ _OBJC_METACLASS_$_BLSHPendingEnvironmentUpdate
+ _OBJC_METACLASS_$_BLSHPendingFlipbookVisualStateOperation
+ _OBJC_METACLASS_$_BLSHResourceArbiter
+ _OBJC_METACLASS_$_BLSHResourceOwnershipToken
+ _OBJC_METACLASS_$_BLSHSceneRegistrationExtension
+ _OBJC_METACLASS_$_BLSHSceneRegistrationHostComponent
+ _OBJC_METACLASS_$_BLSHSceneRegistrationStore
+ _OBJC_METACLASS_$_BLSHSourcedRenderedFlipbookFrame
+ _OBJC_METACLASS_$_BLSHSystemWakeTelemetry
+ _OBJC_METACLASS_$_BLSHSystemWakeTelemetryMetrics
+ _OBJC_METACLASS_$_FBSSceneComponent
+ _OBJC_METACLASS_$_FBSSceneExtension
+ _PPSCreateTelemetryIdentifier
+ _PPSSendTelemetry
+ _PowerLevelForBLSBacklightDisplayMode
+ _PowerLevelForBLSBacklightState
+ __MergedGlobals
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSDictionary_$_BLSFlatten
+ __OBJC_$_CATEGORY_NSDictionary_$_BLSFlatten
+ __OBJC_$_CLASS_METHODS_BLSHAggregateBacklightHost
+ __OBJC_$_CLASS_METHODS_BLSHBacklightEnvironmentSessionProvider
+ __OBJC_$_CLASS_METHODS_BLSHCATransactionTelemetryContext
+ __OBJC_$_CLASS_METHODS_BLSHCoreAnalytics
+ __OBJC_$_CLASS_METHODS_BLSHDisableLowPowerRenderingAttributeHandler
+ __OBJC_$_CLASS_METHODS_BLSHLowPowerRenderingAttributeHandler
+ __OBJC_$_CLASS_METHODS_BLSHSceneRegistrationExtension
+ __OBJC_$_CLASS_METHODS_BLSHSceneRegistrationStore
+ __OBJC_$_CLASS_METHODS_BLSHSystemWakeTelemetry
+ __OBJC_$_INSTANCE_METHODS_BLSHAOTSystemWakeTelemetry
+ __OBJC_$_INSTANCE_METHODS_BLSHAggregateBacklightHost
+ __OBJC_$_INSTANCE_METHODS_BLSHAggregateHostCachedState
+ __OBJC_$_INSTANCE_METHODS_BLSHBacklightEnvironmentPresentation(FrontBoard)
+ __OBJC_$_INSTANCE_METHODS_BLSHBacklightEnvironmentSessionProvider
+ __OBJC_$_INSTANCE_METHODS_BLSHBacklightEventMetrics
+ __OBJC_$_INSTANCE_METHODS_BLSHBacklightWakeTelemetryEvent
+ __OBJC_$_INSTANCE_METHODS_BLSHBacklightWakeTelemetryTracker
+ __OBJC_$_INSTANCE_METHODS_BLSHCATransactionTelemetryContext
+ __OBJC_$_INSTANCE_METHODS_BLSHCoreAnalytics
+ __OBJC_$_INSTANCE_METHODS_BLSHDisableLowPowerRenderingAttributeHandler
+ __OBJC_$_INSTANCE_METHODS_BLSHDisplayWakeTelemetry
+ __OBJC_$_INSTANCE_METHODS_BLSHFlipbookFramesHistogram(CoreAnalytics)
+ __OBJC_$_INSTANCE_METHODS_BLSHFlipbookInvalidationTelemetryData(CoreAnalytics)
+ __OBJC_$_INSTANCE_METHODS_BLSHFlipbookRenderSessionTelemetryData(CoreAnalytics)
+ __OBJC_$_INSTANCE_METHODS_BLSHFlipbookRequestDatesTelemetryData(CoreAnalytics)
+ __OBJC_$_INSTANCE_METHODS_BLSHForceActiveAttributeHandler
+ __OBJC_$_INSTANCE_METHODS_BLSHInfiniteResourceArbiter
+ __OBJC_$_INSTANCE_METHODS_BLSHInfiniteResourceOwnershipToken
+ __OBJC_$_INSTANCE_METHODS_BLSHLowPowerRenderingAttributeHandler
+ __OBJC_$_INSTANCE_METHODS_BLSHMeasureCommitOnWakeOperation
+ __OBJC_$_INSTANCE_METHODS_BLSHOSDisplayInterface
+ __OBJC_$_INSTANCE_METHODS_BLSHPendingBacklightTelemetryEvent
+ __OBJC_$_INSTANCE_METHODS_BLSHPendingEnvironmentUpdate
+ __OBJC_$_INSTANCE_METHODS_BLSHPendingFlipbookVisualStateOperation
+ __OBJC_$_INSTANCE_METHODS_BLSHResourceArbiter
+ __OBJC_$_INSTANCE_METHODS_BLSHResourceOwnershipToken
+ __OBJC_$_INSTANCE_METHODS_BLSHSceneRegistrationHostComponent
+ __OBJC_$_INSTANCE_METHODS_BLSHSceneRegistrationStore
+ __OBJC_$_INSTANCE_METHODS_BLSHSourcedRenderedFlipbookFrame
+ __OBJC_$_INSTANCE_METHODS_BLSHSystemWakeTelemetry
+ __OBJC_$_INSTANCE_METHODS_BLSHSystemWakeTelemetryMetrics
+ __OBJC_$_INSTANCE_METHODS_BLSHValidWhenBacklightInactiveAttributeHandler
+ __OBJC_$_INSTANCE_VARIABLES_BLSHAOTSystemWakeTelemetry
+ __OBJC_$_INSTANCE_VARIABLES_BLSHAggregateBacklightHost
+ __OBJC_$_INSTANCE_VARIABLES_BLSHAggregateHostCachedState
+ __OBJC_$_INSTANCE_VARIABLES_BLSHBacklightEnvironmentSessionProvider
+ __OBJC_$_INSTANCE_VARIABLES_BLSHBacklightEventMetrics
+ __OBJC_$_INSTANCE_VARIABLES_BLSHBacklightWakeTelemetryEvent
+ __OBJC_$_INSTANCE_VARIABLES_BLSHBacklightWakeTelemetryTracker
+ __OBJC_$_INSTANCE_VARIABLES_BLSHCATransactionTelemetryContext
+ __OBJC_$_INSTANCE_VARIABLES_BLSHDisableLowPowerRenderingAttributeHandler
+ __OBJC_$_INSTANCE_VARIABLES_BLSHDisplayWakeTelemetry
+ __OBJC_$_INSTANCE_VARIABLES_BLSHForceActiveAttributeHandler
+ __OBJC_$_INSTANCE_VARIABLES_BLSHInfiniteResourceOwnershipToken
+ __OBJC_$_INSTANCE_VARIABLES_BLSHMeasureCommitOnWakeOperation
+ __OBJC_$_INSTANCE_VARIABLES_BLSHOSDisplayInterface
+ __OBJC_$_INSTANCE_VARIABLES_BLSHPendingBacklightTelemetryEvent
+ __OBJC_$_INSTANCE_VARIABLES_BLSHPendingEnvironmentUpdate
+ __OBJC_$_INSTANCE_VARIABLES_BLSHPendingFlipbookVisualStateOperation
+ __OBJC_$_INSTANCE_VARIABLES_BLSHResourceArbiter
+ __OBJC_$_INSTANCE_VARIABLES_BLSHResourceOwnershipToken
+ __OBJC_$_INSTANCE_VARIABLES_BLSHSceneRegistrationStore
+ __OBJC_$_INSTANCE_VARIABLES_BLSHSourcedRenderedFlipbookFrame
+ __OBJC_$_INSTANCE_VARIABLES_BLSHSystemWakeTelemetry
+ __OBJC_$_INSTANCE_VARIABLES_BLSHSystemWakeTelemetryMetrics
+ __OBJC_$_INSTANCE_VARIABLES_BLSHValidWhenBacklightInactiveAttributeHandler
+ __OBJC_$_PROP_LIST_BLSDisplay
+ __OBJC_$_PROP_LIST_BLSDisplaySpecifying
+ __OBJC_$_PROP_LIST_BLSHAOTSystemWakeTelemetry
+ __OBJC_$_PROP_LIST_BLSHAggregateBacklightHost
+ __OBJC_$_PROP_LIST_BLSHAggregateHostCachedState
+ __OBJC_$_PROP_LIST_BLSHBacklightEnvironmentSessionProvider
+ __OBJC_$_PROP_LIST_BLSHBacklightEnvironmentStateMachineDelegate
+ __OBJC_$_PROP_LIST_BLSHBacklightEventMetrics
+ __OBJC_$_PROP_LIST_BLSHBacklightEventMetricsReading
+ __OBJC_$_PROP_LIST_BLSHBacklightService
+ __OBJC_$_PROP_LIST_BLSHBacklightWakeTelemetryEvent
+ __OBJC_$_PROP_LIST_BLSHBacklightWakeTelemetryTracker
+ __OBJC_$_PROP_LIST_BLSHCATransactionTelemetryContext
+ __OBJC_$_PROP_LIST_BLSHDisableCommitOnWakeMeasurementProvider
+ __OBJC_$_PROP_LIST_BLSHDisableLowPowerRenderingProvider
+ __OBJC_$_PROP_LIST_BLSHDisplayWakeTelemetry
+ __OBJC_$_PROP_LIST_BLSHFlipbook.300
+ __OBJC_$_PROP_LIST_BLSHInfiniteResourceArbiter
+ __OBJC_$_PROP_LIST_BLSHInfiniteResourceOwnershipToken
+ __OBJC_$_PROP_LIST_BLSHMeasureCommitOnWakeOperation
+ __OBJC_$_PROP_LIST_BLSHOSDisplayInterface
+ __OBJC_$_PROP_LIST_BLSHOSDisplayInterfaceProviding
+ __OBJC_$_PROP_LIST_BLSHPendingBacklightTelemetryEvent
+ __OBJC_$_PROP_LIST_BLSHPendingEnvironmentUpdate
+ __OBJC_$_PROP_LIST_BLSHPendingFlipbookVisualStateOperation
+ __OBJC_$_PROP_LIST_BLSHPresentationSetting
+ __OBJC_$_PROP_LIST_BLSHResourceArbiter
+ __OBJC_$_PROP_LIST_BLSHResourceOwnershipToken
+ __OBJC_$_PROP_LIST_BLSHResourceOwning
+ __OBJC_$_PROP_LIST_BLSHSourcedRenderedFlipbookFrame
+ __OBJC_$_PROP_LIST_BLSHSystemWakeTelemetry
+ __OBJC_$_PROP_LIST_BLSHSystemWakeTelemetryMetrics
+ __OBJC_$_PROP_LIST_BLSHSystemWakeTelemetryMetricsReading
+ __OBJC_$_PROTOCOL_CLASS_METHODS_BLSHCoreAnalyticsSending
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BLSDisplay
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BLSDisplaySpecifying
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BLSHBacklightEventMetricsReading
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BLSHBacklightHostTelemetryDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BLSHCoreAnalyticsSending
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BLSHDisableCommitOnWakeMeasurementProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BLSHDisableLowPowerRenderingProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BLSHFlipbookTelemetry
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BLSHOSDisplayInterfaceProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BLSHPresentationSetting
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BLSHResourceArbitrating
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BLSHResourceOwning
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BLSHSystemWakeTelemetryMetricsReading
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BLSHAlwaysOnPresentationEngineDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BLSHBacklightEnvironmentSessionProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BLSHBacklightEnvironmentStateMachineDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BLSHBacklightHostTelemetryDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BLSHPendingOperation
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSDisplay
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSDisplaySpecifying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSHBacklightEventMetricsReading
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSHBacklightHostTelemetryDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSHCoreAnalyticsSending
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSHDisableCommitOnWakeMeasurementProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSHDisableLowPowerRenderingProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSHFlipbookTelemetry
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSHOSDisplayInterfaceProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSHPresentationSetting
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSHResourceArbitrating
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSHResourceOwning
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSHSystemWakeTelemetryMetricsReading
+ __OBJC_$_PROTOCOL_REFS_BLSDisplay
+ __OBJC_$_PROTOCOL_REFS_BLSDisplaySpecifying
+ __OBJC_$_PROTOCOL_REFS_BLSHBacklightEventMetricsReading
+ __OBJC_$_PROTOCOL_REFS_BLSHBacklightHostTelemetryDelegate
+ __OBJC_$_PROTOCOL_REFS_BLSHDisableCommitOnWakeMeasurementProvider
+ __OBJC_$_PROTOCOL_REFS_BLSHDisableLowPowerRenderingProvider
+ __OBJC_$_PROTOCOL_REFS_BLSHFlipbookTelemetry
+ __OBJC_$_PROTOCOL_REFS_BLSHOSDisplayInterfaceProviding
+ __OBJC_$_PROTOCOL_REFS_BLSHPresentationSetting
+ __OBJC_$_PROTOCOL_REFS_BLSHResourceArbitrating
+ __OBJC_$_PROTOCOL_REFS_BLSHResourceOwning
+ __OBJC_$_PROTOCOL_REFS_BLSHSystemWakeTelemetryMetricsReading
+ __OBJC_CLASS_PROTOCOLS_$_BLSHAOTSystemWakeTelemetry
+ __OBJC_CLASS_PROTOCOLS_$_BLSHAggregateBacklightHost
+ __OBJC_CLASS_PROTOCOLS_$_BLSHBacklightEnvironmentSessionProvider
+ __OBJC_CLASS_PROTOCOLS_$_BLSHBacklightEventMetrics
+ __OBJC_CLASS_PROTOCOLS_$_BLSHBacklightWakeTelemetryTracker
+ __OBJC_CLASS_PROTOCOLS_$_BLSHCoreAnalytics
+ __OBJC_CLASS_PROTOCOLS_$_BLSHDisplayWakeTelemetry
+ __OBJC_CLASS_PROTOCOLS_$_BLSHInfiniteResourceArbiter
+ __OBJC_CLASS_PROTOCOLS_$_BLSHInfiniteResourceOwnershipToken
+ __OBJC_CLASS_PROTOCOLS_$_BLSHMeasureCommitOnWakeOperation
+ __OBJC_CLASS_PROTOCOLS_$_BLSHOSDisplayInterface
+ __OBJC_CLASS_PROTOCOLS_$_BLSHPendingEnvironmentUpdate
+ __OBJC_CLASS_PROTOCOLS_$_BLSHPendingFlipbookVisualStateOperation
+ __OBJC_CLASS_PROTOCOLS_$_BLSHResourceArbiter
+ __OBJC_CLASS_PROTOCOLS_$_BLSHResourceOwnershipToken
+ __OBJC_CLASS_PROTOCOLS_$_BLSHSourcedRenderedFlipbookFrame
+ __OBJC_CLASS_PROTOCOLS_$_BLSHSystemWakeTelemetry
+ __OBJC_CLASS_PROTOCOLS_$_BLSHSystemWakeTelemetryMetrics
+ __OBJC_CLASS_RO_$_BLSHAOTSystemWakeTelemetry
+ __OBJC_CLASS_RO_$_BLSHAggregateBacklightHost
+ __OBJC_CLASS_RO_$_BLSHAggregateHostCachedState
+ __OBJC_CLASS_RO_$_BLSHBacklightEnvironmentSessionProvider
+ __OBJC_CLASS_RO_$_BLSHBacklightEventMetrics
+ __OBJC_CLASS_RO_$_BLSHBacklightWakeTelemetryEvent
+ __OBJC_CLASS_RO_$_BLSHBacklightWakeTelemetryTracker
+ __OBJC_CLASS_RO_$_BLSHCATransactionTelemetryContext
+ __OBJC_CLASS_RO_$_BLSHCoreAnalytics
+ __OBJC_CLASS_RO_$_BLSHDisableLowPowerRenderingAttributeHandler
+ __OBJC_CLASS_RO_$_BLSHDisplayWakeTelemetry
+ __OBJC_CLASS_RO_$_BLSHInfiniteResourceArbiter
+ __OBJC_CLASS_RO_$_BLSHInfiniteResourceOwnershipToken
+ __OBJC_CLASS_RO_$_BLSHLowPowerRenderingAttributeHandler
+ __OBJC_CLASS_RO_$_BLSHMeasureCommitOnWakeOperation
+ __OBJC_CLASS_RO_$_BLSHOSDisplayInterface
+ __OBJC_CLASS_RO_$_BLSHPendingBacklightTelemetryEvent
+ __OBJC_CLASS_RO_$_BLSHPendingEnvironmentUpdate
+ __OBJC_CLASS_RO_$_BLSHPendingFlipbookVisualStateOperation
+ __OBJC_CLASS_RO_$_BLSHResourceArbiter
+ __OBJC_CLASS_RO_$_BLSHResourceOwnershipToken
+ __OBJC_CLASS_RO_$_BLSHSceneRegistrationExtension
+ __OBJC_CLASS_RO_$_BLSHSceneRegistrationHostComponent
+ __OBJC_CLASS_RO_$_BLSHSceneRegistrationStore
+ __OBJC_CLASS_RO_$_BLSHSourcedRenderedFlipbookFrame
+ __OBJC_CLASS_RO_$_BLSHSystemWakeTelemetry
+ __OBJC_CLASS_RO_$_BLSHSystemWakeTelemetryMetrics
+ __OBJC_LABEL_PROTOCOL_$_BLSDisplay
+ __OBJC_LABEL_PROTOCOL_$_BLSDisplaySpecifying
+ __OBJC_LABEL_PROTOCOL_$_BLSHBacklightEventMetricsReading
+ __OBJC_LABEL_PROTOCOL_$_BLSHBacklightHostTelemetryDelegate
+ __OBJC_LABEL_PROTOCOL_$_BLSHCoreAnalyticsSending
+ __OBJC_LABEL_PROTOCOL_$_BLSHDisableCommitOnWakeMeasurementProvider
+ __OBJC_LABEL_PROTOCOL_$_BLSHDisableLowPowerRenderingProvider
+ __OBJC_LABEL_PROTOCOL_$_BLSHFlipbookTelemetry
+ __OBJC_LABEL_PROTOCOL_$_BLSHOSDisplayInterfaceProviding
+ __OBJC_LABEL_PROTOCOL_$_BLSHPresentationSetting
+ __OBJC_LABEL_PROTOCOL_$_BLSHResourceArbitrating
+ __OBJC_LABEL_PROTOCOL_$_BLSHResourceOwning
+ __OBJC_LABEL_PROTOCOL_$_BLSHSystemWakeTelemetryMetricsReading
+ __OBJC_METACLASS_RO_$_BLSHAOTSystemWakeTelemetry
+ __OBJC_METACLASS_RO_$_BLSHAggregateBacklightHost
+ __OBJC_METACLASS_RO_$_BLSHAggregateHostCachedState
+ __OBJC_METACLASS_RO_$_BLSHBacklightEnvironmentSessionProvider
+ __OBJC_METACLASS_RO_$_BLSHBacklightEventMetrics
+ __OBJC_METACLASS_RO_$_BLSHBacklightWakeTelemetryEvent
+ __OBJC_METACLASS_RO_$_BLSHBacklightWakeTelemetryTracker
+ __OBJC_METACLASS_RO_$_BLSHCATransactionTelemetryContext
+ __OBJC_METACLASS_RO_$_BLSHCoreAnalytics
+ __OBJC_METACLASS_RO_$_BLSHDisableLowPowerRenderingAttributeHandler
+ __OBJC_METACLASS_RO_$_BLSHDisplayWakeTelemetry
+ __OBJC_METACLASS_RO_$_BLSHInfiniteResourceArbiter
+ __OBJC_METACLASS_RO_$_BLSHInfiniteResourceOwnershipToken
+ __OBJC_METACLASS_RO_$_BLSHLowPowerRenderingAttributeHandler
+ __OBJC_METACLASS_RO_$_BLSHMeasureCommitOnWakeOperation
+ __OBJC_METACLASS_RO_$_BLSHOSDisplayInterface
+ __OBJC_METACLASS_RO_$_BLSHPendingBacklightTelemetryEvent
+ __OBJC_METACLASS_RO_$_BLSHPendingEnvironmentUpdate
+ __OBJC_METACLASS_RO_$_BLSHPendingFlipbookVisualStateOperation
+ __OBJC_METACLASS_RO_$_BLSHResourceArbiter
+ __OBJC_METACLASS_RO_$_BLSHResourceOwnershipToken
+ __OBJC_METACLASS_RO_$_BLSHSceneRegistrationExtension
+ __OBJC_METACLASS_RO_$_BLSHSceneRegistrationHostComponent
+ __OBJC_METACLASS_RO_$_BLSHSceneRegistrationStore
+ __OBJC_METACLASS_RO_$_BLSHSourcedRenderedFlipbookFrame
+ __OBJC_METACLASS_RO_$_BLSHSystemWakeTelemetry
+ __OBJC_METACLASS_RO_$_BLSHSystemWakeTelemetryMetrics
+ __OBJC_PROTOCOL_$_BLSDisplay
+ __OBJC_PROTOCOL_$_BLSDisplaySpecifying
+ __OBJC_PROTOCOL_$_BLSHBacklightEventMetricsReading
+ __OBJC_PROTOCOL_$_BLSHBacklightHostTelemetryDelegate
+ __OBJC_PROTOCOL_$_BLSHCoreAnalyticsSending
+ __OBJC_PROTOCOL_$_BLSHDisableCommitOnWakeMeasurementProvider
+ __OBJC_PROTOCOL_$_BLSHDisableLowPowerRenderingProvider
+ __OBJC_PROTOCOL_$_BLSHFlipbookTelemetry
+ __OBJC_PROTOCOL_$_BLSHOSDisplayInterfaceProviding
+ __OBJC_PROTOCOL_$_BLSHPresentationSetting
+ __OBJC_PROTOCOL_$_BLSHResourceArbitrating
+ __OBJC_PROTOCOL_$_BLSHResourceOwning
+ __OBJC_PROTOCOL_$_BLSHSystemWakeTelemetryMetricsReading
+ __OBJC_PROTOCOL_REFERENCE_$_BLSDisplaySpecifying
+ __OBJC_PROTOCOL_REFERENCE_$_BLSHOSDisplayInterfaceProviding
+ ___100-[BLSHBacklightEnvironmentPresentation(FrontBoard) initWithFBScenes:flipbookContext:expirationDate:]_block_invoke
+ ___101-[BLSHBacklightStateMachine backlight:rampingToBrightnessCurve:withDuration:forEvents:abortedEvents:]_block_invoke
+ ___101-[BLSHDisplayWakeTelemetry backlightTelemetrySource:didUnblankToDisplayMode:forEvents:abortedEvents:]_block_invoke
+ ___102-[BLSHBacklightEnvironmentStateMachine onMain_performEvent:withInitialSpecifier:performBacklightRamp:]_block_invoke.198
+ ___102-[BLSHBacklightEnvironmentStateMachine updateFlipbookVisualState:backlightState:withInitialSpecifier:]_block_invoke
+ ___102-[BLSHBacklightTransitionStateMachine environmentStateMachine:didUpdateFlipbookVisualState:specifier:]_block_invoke
+ ___102-[BLSHDisplayWakeTelemetry backlightTelemetrySource:didCompleteUpdateToState:forEvents:abortedEvents:]_block_invoke
+ ___102-[BLSHEngineRenderFlipbookSession initWithDelegate:flipbook:presentation:osInterfaceProvider:display:]_block_invoke
+ ___102-[BLSHLocalHostSceneEnvironment updateToDateSpecifier:sceneContentsUpdated:lowPowerRenderingDisabled:]_block_invoke
+ ___104-[BLSHAOTSystemWakeTelemetry backlight:willUpdateToDisplayMode:fromDisplayMode:forEvents:abortedEvents:]_block_invoke
+ ___104-[BLSHAOTSystemWakeTelemetry backlight:willUpdateToDisplayMode:fromDisplayMode:forEvents:abortedEvents:]_block_invoke_2
+ ___104-[BLSHAggregateBacklightHost backlight:willUpdateToDisplayMode:fromDisplayMode:forEvents:abortedEvents:]_block_invoke
+ ___106-[BLSHAggregateBacklightHost backlight:didUpdateToDisplayMode:fromDisplayMode:activeEvents:abortedEvents:]_block_invoke
+ ___108-[BLSHAlwaysOnPresentationEngine lock_cancelFlipbookFramesForReason:source:didClearDateSpecifiers:wasReset:]_block_invoke.274
+ ___108-[BLSHAlwaysOnPresentationEngine lock_cancelFlipbookFramesForReason:source:didClearDateSpecifiers:wasReset:]_block_invoke.274.cold.1
+ ___108-[BLSHBacklightFBSceneHostEnvironment updateToDateSpecifier:sceneContentsUpdated:lowPowerRenderingDisabled:]_block_invoke
+ ___108-[BLSHBacklightFBSceneHostEnvironment updateToDateSpecifier:sceneContentsUpdated:lowPowerRenderingDisabled:]_block_invoke.106
+ ___108-[BLSHBacklightFBSceneHostEnvironment updateToDateSpecifier:sceneContentsUpdated:lowPowerRenderingDisabled:]_block_invoke.106.cold.1
+ ___112-[BLSHAggregateBacklightHost backlight:didUpdateVisualContentsToBeginTransitionToState:forEvents:abortedEvents:]_block_invoke
+ ___112-[BLSHBacklightDisplayStateMachine display:didCompleteTransitionToCADisplayState:currentState:transitionStatus:]_block_invoke
+ ___112-[BLSHBacklightTransitionStateMachine initForDisplay:platformProvider:osInterfaceProvider:inactiveBudgetPolicy:]_block_invoke
+ ___112-[BLSHBacklightTransitionStateMachine initForDisplay:platformProvider:osInterfaceProvider:inactiveBudgetPolicy:]_block_invoke_2
+ ___113-[BLSHBacklightFBSceneHostEnvironment scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:]_block_invoke.123
+ ___113-[BLSHBacklightFBSceneHostEnvironment scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:]_block_invoke.126
+ ___115-[BLSHBacklightTransitionStateMachine onMainWithLock_updateOperationNeedsFlipbook:isFlipbook:flipbookFirst:events:]_block_invoke
+ ___116-[BLSHAlwaysOnPresentationEngine initForDisplay:delegate:platformProvider:osInterfaceProvider:inactiveBudgetPolicy:]_block_invoke
+ ___118-[BLSHWatchdogProvider _fireWatchdogWithTimer:delegate:timeout:elapsedTime:abortContext:explanation:remainingRetries:]_block_invoke.140
+ ___118-[BLSHWatchdogProvider _fireWatchdogWithTimer:delegate:timeout:elapsedTime:abortContext:explanation:remainingRetries:]_block_invoke.140.cold.1
+ ___118-[BLSHWatchdogProvider _fireWatchdogWithTimer:delegate:timeout:elapsedTime:abortContext:explanation:remainingRetries:]_block_invoke.140.cold.2
+ ___118-[BLSHWatchdogProvider _fireWatchdogWithTimer:delegate:timeout:elapsedTime:abortContext:explanation:remainingRetries:]_block_invoke.140.cold.3
+ ___123-[BLSHBacklightEnvironmentStateMachine checkCompletedOperationsToBacklightState:visualState:transitionState:isBeginUpdate:]_block_invoke.247
+ ___123-[BLSHBacklightTransitionStateMachine onMain_startSubOperation:environmentStateMachine:backlightState:currentPresentation:]_block_invoke
+ ___124-[BLSHAlwaysOnPresentationEngine requestDatesOperation:environment:didProvideSpecifiers:forPresentationInterval:isComplete:]_block_invoke.241
+ ___124-[BLSHAlwaysOnPresentationEngine requestDatesOperation:environment:didProvideSpecifiers:forPresentationInterval:isComplete:]_block_invoke.245
+ ___124-[BLSHAlwaysOnPresentationEngine requestDatesOperation:environment:didProvideSpecifiers:forPresentationInterval:isComplete:]_block_invoke.245.cold.1
+ ___124-[BLSHAlwaysOnPresentationEngine requestDatesOperation:environment:didProvideSpecifiers:forPresentationInterval:isComplete:]_block_invoke.246
+ ___124-[BLSHBacklightFBSceneHostEnvironment requestDateSpecifiersForDateInterval:previousPresentationDate:shouldReset:completion:]_block_invoke.92
+ ___124-[BLSHBacklightFBSceneHostEnvironment requestDateSpecifiersForDateInterval:previousPresentationDate:shouldReset:completion:]_block_invoke.95
+ ___125-[BLSHDisplayWakeTelemetry backlightTelemetrySource:didUpdateVisualContentsToBeginTransitionToState:forEvents:abortedEvents:]_block_invoke
+ ___140-[BLSHEnvironmentTransitionState updateToFlipbookVisualState:backlightState:presentationDate:sceneUpdate:lowPowerRenderingPresentationTime:]_block_invoke
+ ___166-[BLSHEnvironmentTransitionState updateToBacklightState:forEvent:touchTargetable:presentationDate:sceneUpdate:lowPowerRenderingPresentationTime:performBacklightRamp:]_block_invoke
+ ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.68
+ ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.77
+ ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.77.cold.1
+ ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.81
+ ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.81.cold.1
+ ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.85
+ ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.85.cold.1
+ ___29+[BLSHCoreAnalytics workloop]_block_invoke
+ ___31-[BLSHFlipbook logDiagnostics:]_block_invoke
+ ___31-[BLSHFlipbook logDiagnostics:]_block_invoke.cold.1
+ ___34-[BLSHFlipbook hangDetectorFired:]_block_invoke.116
+ ___34-[BLSHFlipbook hangDetectorFired:]_block_invoke.116.cold.1
+ ___34-[BLSHFlipbook hangDetectorFired:]_block_invoke.116.cold.2
+ ___34-[BLSHFlipbook hangDetectorFired:]_block_invoke.93
+ ___38-[BLSHSystemWaker watchdogTimerFired:]_block_invoke.119
+ ___39-[BLSHXPCBacklightProxyHostServer init]_block_invoke
+ ___40-[BLSHWatchdogProvider makeStartupCheck]_block_invoke
+ ___42+[BLSHCoreAnalytics sharedAnalyticsSender]_block_invoke
+ ___42-[BLSHAggregateBacklightHost addObserver:]_block_invoke
+ ___42-[BLSHCATransactionTelemetryContext begin]_block_invoke
+ ___42-[BLSHCATransactionTelemetryContext begin]_block_invoke.7
+ ___42-[BLSHCATransactionTelemetryContext begin]_block_invoke.cold.1
+ ___42-[BLSHCATransactionTelemetryContext begin]_block_invoke.cold.2
+ ___43-[BLSHAggregateHostCachedState description]_block_invoke
+ ___43-[BLSHAggregateHostCachedState description]_block_invoke_2
+ ___43-[BLSHCATransactionTelemetryContext commit]_block_invoke
+ ___43-[BLSHCATransactionTelemetryContext commit]_block_invoke.cold.1
+ ___43-[BLSHWatchdogTester _triggerTestWatchdog:]_block_invoke.65
+ ___43-[BLSHWatchdogTester _triggerTestWatchdog:]_block_invoke.70
+ ___44+[BLSHSceneRegistrationStore sharedInstance]_block_invoke
+ ___44-[BLSHAOTSystemWakeTelemetry startObserving]_block_invoke
+ ___44-[BLSHCATransactionTelemetryContext dealloc]_block_invoke
+ ___46-[BLSHMeasureCommitOnWakeOperation invalidate]_block_invoke
+ ___46-[BLSHWatchdogProvider prepareForStartupCheck]_block_invoke
+ ___49-[BLSHOSDisplayInterface setFlipbookTransparent:]_block_invoke
+ ___50-[BLSHAOTSystemWakeTelemetry logMetricsTimerFired]_block_invoke
+ ___50-[BLSHLocalAssertionService queue_pauseAssertion:]_block_invoke.33
+ ___50-[BLSHWatchdogProvider listenForOSStartupComplete]_block_invoke
+ ___51+[BLSHCoreAnalytics sendEventAsync:payloadBuilder:]_block_invoke
+ ___51+[BLSHCoreAnalytics sendEventAsync:payloadBuilder:]_block_invoke_2
+ ___51-[BLSHDiagnosticsServer _handleIncomingConnection:]_block_invoke
+ ___51-[BLSHDiagnosticsServer _handleIncomingConnection:]_block_invoke.cold.1
+ ___51-[BLSHDiagnosticsServer _handleIncomingConnection:]_block_invoke_2
+ ___51-[BLSHDiagnosticsServer _handleIncomingConnection:]_block_invoke_2.cold.1
+ ___51-[BLSHLocalAssertionService queue_resumeAssertion:]_block_invoke.39
+ ___53-[BLSHBacklightSceneClientSettingsDiffInspector init]_block_invoke_4
+ ___53-[BLSHBacklightSceneClientSettingsDiffInspector init]_block_invoke_5
+ ___53-[BLSHBaseSceneHostEnvironment setLowPowerRendering:]_block_invoke
+ ___53-[BLSHOSDisplayInterface transitionToCADisplayState:]_block_invoke
+ ___53-[BLSHOSDisplayInterface transitionToCADisplayState:]_block_invoke.175
+ ___53-[BLSHOSDisplayInterface transitionToCADisplayState:]_block_invoke.177
+ ___53-[BLSHOSDisplayInterface transitionToCADisplayState:]_block_invoke.177.cold.1
+ ___54-[BLSHLocalAssertionService registerAttributeHandler:]_block_invoke
+ ___56-[BLSHAggregateBacklightHost backlight:performingEvent:]_block_invoke
+ ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke.123
+ ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke.127
+ ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke.130
+ ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke.137
+ ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke_2.131
+ ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke_2.141
+ ___57-[NSDictionary(BLSFlatten) bls_flattenWithSeparator:key:]_block_invoke
+ ___58+[BLSHService startServiceWithPlatformProvider:localOnly:]_block_invoke
+ ___58-[BLSHAOTSystemWakeTelemetry logTelemetryForInvalidation:]_block_invoke
+ ___58-[BLSHMeasureCommitOnWakeOperation performCommitToMeasure]_block_invoke
+ ___59-[BLSHAOTSystemWakeTelemetry logTelemetryForRenderSession:]_block_invoke
+ ___60-[BLSHBacklightFBSceneHostEnvironment setLowPowerRendering:]_block_invoke
+ ___60-[BLSHLocalAssertionService queue_registerAttributeHandler:]_block_invoke
+ ___61-[BLSHBacklightOSInterfaceProvider initWithPlatformProvider:]_block_invoke
+ ___61-[BLSHBacklightOSInterfaceProvider initWithPlatformProvider:]_block_invoke.186
+ ___61-[BLSHBacklightOSInterfaceProvider initWithPlatformProvider:]_block_invoke_2
+ ___61-[BLSHLocalAssertionService queue_cancelAssertion:withError:]_block_invoke.79
+ ___61-[BLSHLocalAssertionService queue_cancelAssertion:withError:]_block_invoke_4
+ ___61-[BLSHOSDisplayInterface startSuppressionServiceWithHandler:]_block_invoke
+ ___61-[BLSHOSDisplayInterface startSuppressionServiceWithHandler:]_block_invoke.cold.1
+ ___61-[BLSHXPCBacklightProxyHostServer _handleIncomingConnection:]_block_invoke
+ ___61-[BLSHXPCBacklightProxyHostServer _handleIncomingConnection:]_block_invoke.cold.1
+ ___61-[BLSHXPCBacklightProxyHostServer _handleIncomingConnection:]_block_invoke_2
+ ___61-[BLSHXPCBacklightProxyHostServer _handleIncomingConnection:]_block_invoke_2.cold.1
+ ___62-[BLSHBacklightWakeTelemetryTracker beginForEvent:completion:]_block_invoke
+ ___63-[BLSHAlwaysOnPresentationEngine setLowPowerRenderingDisabled:]_block_invoke
+ ___63-[BLSHAlwaysOnPresentationEngine setLowPowerRenderingDisabled:]_block_invoke_2
+ ___63-[BLSHXPCAssertionServiceHostServer _handleIncomingConnection:]_block_invoke
+ ___63-[BLSHXPCAssertionServiceHostServer _handleIncomingConnection:]_block_invoke.cold.1
+ ___63-[BLSHXPCAssertionServiceHostServer _handleIncomingConnection:]_block_invoke_2
+ ___63-[BLSHXPCAssertionServiceHostServer _handleIncomingConnection:]_block_invoke_2.cold.1
+ ___64-[BLSHLocalAssertionService queue_restartAssertionTimeoutTimer:]_block_invoke.85
+ ___65-[BLSHAOTSystemWakeTelemetry backlight:didChangeAlwaysOnEnabled:]_block_invoke
+ ___65-[BLSHAggregateBacklightHost backlight:didChangeAlwaysOnEnabled:]_block_invoke
+ ___65-[BLSHLocalHostSceneEnvironmentUpdater subHostedHostEnvironments]_block_invoke.cold.1
+ ___67-[BLSHLocalAssertionService queue_acquireAssertion:skipSleepCheck:]_block_invoke.56
+ ___67-[BLSHLocalAssertionService queue_acquireAssertion:skipSleepCheck:]_block_invoke.64
+ ___67-[BLSHLocalAssertionService queue_acquireAssertion:skipSleepCheck:]_block_invoke_2.69
+ ___67-[BLSHLocalAssertionService queue_acquireAssertion:skipSleepCheck:]_block_invoke_2.69.cold.1
+ ___69-[BLSHBacklightStateMachine systemSleepAction:performWithCompletion:]_block_invoke.218
+ ___69-[BLSHLowPowerRenderingAttributeHandler activateForSceneEnvironment:]_block_invoke
+ ___69-[BLSHLowPowerRenderingAttributeHandler activateForSceneEnvironment:]_block_invoke.cold.1
+ ___70-[BLSHBacklightStateMachine updateSuppressionServiceForActivityState:]_block_invoke.154
+ ___70-[BLSHDisplayWakeTelemetry backlightTelemetrySource:willPerformEvent:]_block_invoke
+ ___70-[BLSHDisplayWakeTelemetry backlightTelemetrySource:willPerformEvent:]_block_invoke.268
+ ___70-[BLSHDisplayWakeTelemetry backlightTelemetrySource:willPerformEvent:]_block_invoke.cold.1
+ ___70-[BLSHDisplayWakeTelemetry backlightTelemetrySource:willPerformEvent:]_block_invoke.cold.2
+ ___70-[BLSHDisplayWakeTelemetry backlightTelemetrySource:willPerformEvent:]_block_invoke.cold.3
+ ___70-[BLSHDisplayWakeTelemetry backlightTelemetrySource:willPerformEvent:]_block_invoke.cold.4
+ ___71-[BLSHLowPowerRenderingAttributeHandler deactivateForSceneEnvironment:]_block_invoke
+ ___71-[BLSHLowPowerRenderingAttributeHandler deactivateForSceneEnvironment:]_block_invoke.cold.1
+ ___71-[BLSHOSDisplayInterface didCompleteTransitionToDisplayMode:withError:]_block_invoke
+ ___71-[BLSHOSDisplayInterface didCompleteTransitionToDisplayMode:withError:]_block_invoke.cold.1
+ ___73-[BLSHBacklightTransitionStateMachine lock_displayModeForBacklightState:]_block_invoke
+ ___75-[BLSHAggregateBacklightHost backlightHost:willTransitionToState:forEvent:]_block_invoke
+ ___75-[BLSHDisplayWakeTelemetry _logAbortedEventsAnalytics:context:targetState:]_block_invoke
+ ___75-[BLSHWatchdogProvider fireWatchdogWithTimer:delegate:timeout:elapsedTime:]_block_invoke
+ ___75-[BLSHWatchdogProvider fireWatchdogWithTimer:delegate:timeout:elapsedTime:]_block_invoke.cold.1
+ ___77-[BLSHAlwaysOnPresentationEngine hostEnvironment:invalidateContentForReason:]_block_invoke.263
+ ___77-[BLSHAlwaysOnPresentationEngine hostEnvironment:invalidateContentForReason:]_block_invoke_2.264
+ ___77-[BLSHEngineRenderFlipbookSession renderFrameSpecifier:timedOutEnvironments:]_block_invoke.662
+ ___77-[BLSHEngineRenderFlipbookSession renderFrameSpecifier:timedOutEnvironments:]_block_invoke.663
+ ___77-[BLSHEngineRenderFlipbookSession renderFrameSpecifier:timedOutEnvironments:]_block_invoke.664
+ ___78-[BLSHAlwaysOnPresentationEngine lock_scheduleUpdateTimerForNextUpdatesStart:]_block_invoke.343
+ ___78-[BLSHBacklightTransitionStateMachine updateDisplayModeAfterClaimingFlipbook:]_block_invoke
+ ___78-[BLSHBaseBacklightEnvironmentSessionProvider setPresentation:withCompletion:]_block_invoke
+ ___80-[BLSHDisplayWakeTelemetry _logBacklightTelemetryEventForPendingEvent:duration:]_block_invoke
+ ___80-[BLSHDisplayWakeTelemetry _logBacklightTelemetryEventForPendingEvent:duration:]_block_invoke_2
+ ___81-[BLSHOSDisplayInterface initWithCADisplay:platformProvider:osInterfaceProvider:]_block_invoke
+ ___84-[BLSHMeasureCommitOnWakeOperation beginMeasurementForTransactionID:withCompletion:]_block_invoke
+ ___84-[BLSHMeasureCommitOnWakeOperation beginMeasurementForTransactionID:withCompletion:]_block_invoke.20
+ ___84-[BLSHMeasureCommitOnWakeOperation beginMeasurementForTransactionID:withCompletion:]_block_invoke.cold.1
+ ___86-[BLSHAlwaysOnPresentationEngine requestDatesOperation:didTimeoutPendingEnvironments:]_block_invoke.247
+ ___87-[BLSHBacklightTransitionStateMachine inactiveEnvironmentSession:updateToPresentation:]_block_invoke.298
+ ___87-[BLSHBacklightTransitionStateMachine inactiveEnvironmentSession:updateToPresentation:]_block_invoke.301
+ ___87-[BLSHBacklightTransitionStateMachine inactiveEnvironmentSession:updateToPresentation:]_block_invoke.306
+ ___87-[BLSHXPCAssertionServiceHostServer initWithLocalAssertionService:osInterfaceProvider:]_block_invoke
+ ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke.149
+ ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke.152
+ ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke.155
+ ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke.169
+ ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke.173
+ ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke.179
+ ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke_2.158
+ ___88-[BLSHFlipbook renderFrameForPresentation:dateSpecifier:onRenderBegin:onRenderComplete:]_block_invoke.169
+ ___89-[BLSHAggregateBacklightHost backlight:didCompleteUpdateToState:forEvents:abortedEvents:]_block_invoke
+ ___89-[BLSHBacklightDisplayStateMachine display:didCompleteSwitchToCBFlipbookState:withError:]_block_invoke
+ ___89-[BLSHLocalHostSceneEnvironmentUpdater updatedEnvironmentWithDelta:backlightSceneUpdate:]_block_invoke.232
+ ___89-[BLSHLocalHostSceneEnvironmentUpdater updatedEnvironmentWithDelta:backlightSceneUpdate:]_block_invoke.232.cold.1
+ ___91-[BLSHBacklightDisplayStateMachine display:didCompleteTransitionToCBDisplayMode:withError:]_block_invoke
+ ___96-[BLSHBacklightStateMachine initForDisplay:platformProvider:eventPerformer:osInterfaceProvider:]_block_invoke
+ ___96-[BLSHBacklightStateMachine initForDisplay:platformProvider:eventPerformer:osInterfaceProvider:]_block_invoke.93
+ ___96-[BLSHBacklightStateMachine initForDisplay:platformProvider:eventPerformer:osInterfaceProvider:]_block_invoke_2
+ ___96-[BLSHOSDisplayInterface transitionToDisplayMode:withDuration:didChangeAlwaysOnBrightnessCurve:]_block_invoke
+ ___97-[BLSHAggregateBacklightHost backlight:didCompleteUpdateToFlipbookState:forEvents:abortedEvents:]_block_invoke
+ ___97-[BLSHBacklightDisplayStateMachine initForDisplay:delegate:platformProvider:osInterfaceProvider:]_block_invoke
+ ___97-[BLSHBacklightDisplayStateMachine transitionToDisplayMode:withDuration:shouldWaitForCompletion:]_block_invoke_2
+ ___BLSHIsTelemetryDisabledViaDefault_block_invoke
+ ___BLSHTailspinQueue_block_invoke
+ ____BLSHShowWatchdogFailureAlert_block_invoke.110
+ ___block_descriptor_106_e8_32s40s48s56s64s72s80bs88bs96bs_e60_"FBSSceneTransitionContext"16?0"FBSMutableSceneSettings"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_117_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_32_e19_B16?0"CADisplay"8l
+ ___block_descriptor_32_e22_B16?0"BLSAttribute"8l
+ ___block_descriptor_32_e40_"BLSDisplayReference"16?0"CADisplay"8l
+ ___block_descriptor_40_e8_32bs_e35_v16?0"<BLSHPresentationSetting>"8ls32l8
+ ___block_descriptor_40_e8_32s_e19_"NSDictionary"8?0ls32l8
+ ___block_descriptor_40_e8_32s_e30_v16?0"<BLSHResourceOwning>"8ls32l8
+ ___block_descriptor_40_e8_32s_e43_"BLSHOSDisplayInterface"16?0"CADisplay"8ls32l8
+ ___block_descriptor_40_e8_32s_e75_B32?0"BLSBacklightChangeEvent"8"BLSHBacklightWakeTelemetryTracker"16^B24ls32l8
+ ___block_descriptor_40_e8_32w_e37_v16?0"BSServiceListenerConnection"8lw32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_41_e40_B16?0"BLSHEnvironmentTransitionState"8l
+ ___block_descriptor_41_e44_B24?0"BLSHEnvironmentTransitionState"8^B16l
+ ___block_descriptor_41_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32r_e45_v24?0"<BLSHAssertionAttributeHandler>"8^B16lu40l8r32l8
+ ___block_descriptor_48_e8_32s40bs_e19_"NSDictionary"8?0ls40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e50_v16?0"<BSServiceListenerConnectionConfiguring>"8ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e65_v16?0"BSServiceListenerConnection<BSServiceConnectionContext>"8ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e11_v24?0q8q16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e19_"NSDictionary"8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_48_e8_32s_e40_v32?0"BLSBacklightChangeEvent"8Q16^B24ls32l8
+ ___block_descriptor_48_e8_32s_e8_v16?0q8ls32l8
+ ___block_descriptor_48_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_49_e8_32s40s_e11_v24?0q8q16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e65_v16?0"BSServiceListenerConnection<BSServiceConnectionContext>"8ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e25_v32?0"NSString"816^B24ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e45_v24?0"<BLSHAssertionAttributeHandler>"8^B16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48w_e45_v24?0"BLSHMeasureCommitOnWakeOperation"8Q16lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e31_16?0"BLSHPresentationEntry"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_57_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e50_v16?0"<BSServiceListenerConnectionConfiguring>"8ls32l8r56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e33_v16?0"FBSMutableSceneSettings"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e45_v24?0"<BLSHAssertionAttributeHandler>"8^B16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e8_v16?0q8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s_e61_v28?0B8"NSError"12"<SWSystemActivityAcquisitionDetails>"20ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s_e11_v24?0q8q16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_65_e8_32s40s48s56s_e45_v24?0"<BLSHAssertionAttributeHandler>"8^B16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40bs48r56w_e31_v16?0"BSContinuousMachTimer"8lw56l8s32l8r48l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e61_v28?0B8"NSError"12"<SWSystemActivityAcquisitionDetails>"20ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32s40s48s56s_e19_"NSDictionary"8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56w_e41_v16?0"BLSHBacklightWakeTelemetryEvent"8lw56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s_e38_v16?0"<BLSHBacklightHostObserving>"8ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s_e19_"NSDictionary"8?0ls32l8s40l8
+ ___block_descriptor_74_e8_32s40s48s56s_e38_v16?0"<BLSHBacklightHostObserving>"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e67_v16?0"<BSTimerScheduleQuerying><BSCancellable><BSInvalidatable>"8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_80_e8_32s40s48s56s64s_e67_v16?0"<BSTimerScheduleQuerying><BSCancellable><BSInvalidatable>"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56bs64r72w_e11_v20?0I8d12lw72l8s32l8r64l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e61_v28?0B8"NSError"12"<SWSystemActivityAcquisitionDetails>"20ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_literal_global.118
+ ___block_literal_global.128
+ ___block_literal_global.136
+ ___block_literal_global.151
+ ___block_literal_global.152
+ ___block_literal_global.155
+ ___block_literal_global.157
+ ___block_literal_global.171
+ ___block_literal_global.172
+ ___block_literal_global.191
+ ___block_literal_global.197
+ ___block_literal_global.204
+ ___block_literal_global.206
+ ___block_literal_global.214
+ ___block_literal_global.243
+ ___block_literal_global.249
+ ___block_literal_global.278
+ ___block_literal_global.297
+ ___block_literal_global.300
+ ___block_literal_global.303
+ ___block_literal_global.305
+ ___block_literal_global.31
+ ___block_literal_global.310
+ ___block_literal_global.34
+ ___block_literal_global.416
+ ___block_literal_global.45
+ ___block_literal_global.51
+ ___block_literal_global.6
+ ___block_literal_global.64
+ ___block_literal_global.644
+ ___block_literal_global.655
+ ___block_literal_global.67
+ ___block_literal_global.78
+ ___block_literal_global.98
+ ___getVMStats_block_invoke
+ __dispatch_source_type_timer
+ __lock_providerByDisplayId
+ __prepareForStartupCheck
+ __workloop
+ _dispatch_block_create_with_qos_class
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_queue_create
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _dispatch_workloop_create
+ _getVMStats
+ _getVMStats._myHost
+ _getVMStats.cold.1
+ _getVMStats.cold.2
+ _getVMStats.onceToken
+ _host_statistics64
+ _listenForOSStartupComplete.onceToken
+ _mach_absolute_time
+ _mach_get_times
+ _mach_host_self
+ _makeStartupCheck.onceToken
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_commonInitWithTelemetrySource:analyticsRecorder:
+ _objc_msgSend$_eventNameForBacklightState:
+ _objc_msgSend$_handleBacklightDidCompleteUpdateToState:updateTime:forEvents:abortedEvents:
+ _objc_msgSend$_handleBacklightNewState:sourceEvent:explanation:startedAtContinuousTime:
+ _objc_msgSend$_handleBacklightNewState:sourceEvent:explanation:startedAtContinuousTime:changeEvent:
+ _objc_msgSend$_handleBacklightNewState:startedAtContinuousTime:event:
+ _objc_msgSend$_handleIncomingConnection:
+ _objc_msgSend$_lock_captureStatsForPendingEndpoint:timestamp:
+ _objc_msgSend$_lock_checkAgainstTriggerEvent:
+ _objc_msgSend$_logAbortedEventsAnalytics:context:targetState:
+ _objc_msgSend$_logBacklightTelemetryEventForPendingEvent:duration:
+ _objc_msgSend$_resetAccumulatedMetrics
+ _objc_msgSend$abortedEventsCount
+ _objc_msgSend$accumulateMetrics:
+ _objc_msgSend$accumulateOffDuration:isAOT:
+ _objc_msgSend$accumulateOnDuration:
+ _objc_msgSend$accumulatedLayoutDuration
+ _objc_msgSend$accumulatedRenderDuration
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$afterFailingToRevertPendingSleep
+ _objc_msgSend$afterSleepOfNonZeroDuration
+ _objc_msgSend$aggregateHostWithBacklightHosts:
+ _objc_msgSend$allEventsToWakeDurationSeconds
+ _objc_msgSend$alwaysOnEnabled
+ _objc_msgSend$alwaysOnPresentationEngine
+ _objc_msgSend$appendString:
+ _objc_msgSend$averageInterval
+ _objc_msgSend$backlight:rampingToBrightnessCurve:withDuration:forEvents:abortedEvents:
+ _objc_msgSend$backlightHostForDisplay:
+ _objc_msgSend$backlightProxyForDisplay:
+ _objc_msgSend$beforeKernelWake
+ _objc_msgSend$begin
+ _objc_msgSend$beginForEvent:completion:
+ _objc_msgSend$beginMeasurementForTransactionID:withCompletion:
+ _objc_msgSend$bls_flattenWithSeparator:key:
+ _objc_msgSend$bls_needsFlipbookStateUpdates
+ _objc_msgSend$bls_needsLowPowerRenderingStateUpdates
+ _objc_msgSend$bls_setLowPowerRenderingPresentationTime:
+ _objc_msgSend$blsh_analyticsEventName
+ _objc_msgSend$blsh_analyticsPayload
+ _objc_msgSend$caDisplay
+ _objc_msgSend$canAcquireForDisplay:
+ _objc_msgSend$changeEvent
+ _objc_msgSend$changedSettingsWhileOffCount
+ _objc_msgSend$checkCompleteForEvent:
+ _objc_msgSend$claimResource:
+ _objc_msgSend$clientNeedsFlipbookStateUpdates
+ _objc_msgSend$clientNeedsLowPowerRenderingStateUpdates
+ _objc_msgSend$commit
+ _objc_msgSend$completeForEvent:
+ _objc_msgSend$completedEventsCount
+ _objc_msgSend$completionDuration
+ _objc_msgSend$compressionsDiff
+ _objc_msgSend$configurationWithDomain:service:
+ _objc_msgSend$configure:
+ _objc_msgSend$confirmedPossibleCount
+ _objc_msgSend$conformsToProtocol:
+ _objc_msgSend$count1to2Min
+ _objc_msgSend$count2to3Min
+ _objc_msgSend$count3to4Min
+ _objc_msgSend$count4to5Min
+ _objc_msgSend$count5to6Min
+ _objc_msgSend$countLessThan1Min
+ _objc_msgSend$countMoreThan6Min
+ _objc_msgSend$createForDisplay:platformProvider:
+ _objc_msgSend$createInactiveEnvironmentSessionForDisplay:
+ _objc_msgSend$createProviderforDisplay:withLocalAssertionService:
+ _objc_msgSend$currentOperation
+ _objc_msgSend$currentState
+ _objc_msgSend$dataWithJSONObject:options:error:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$defaultServiceWithDelegate:
+ _objc_msgSend$didAcquireSystemActivityWithError:isActive:details:forEvent:
+ _objc_msgSend$didClearDateSpecifiers
+ _objc_msgSend$didCompleteDurationSeconds
+ _objc_msgSend$didCompleteUpdateForEvents:abortedEvents:
+ _objc_msgSend$didFailToRender
+ _objc_msgSend$didReset
+ _objc_msgSend$didTimeout
+ _objc_msgSend$didTimeoutSystemActivity
+ _objc_msgSend$didTimeoutSystemActivty
+ _objc_msgSend$didUnblankForEvent:
+ _objc_msgSend$didUpdateVisualContentsToBeginTransitionToActiveOnForEvent:
+ _objc_msgSend$discardedFramesUpTo2mStale
+ _objc_msgSend$discardedFramesUpTo3mStale
+ _objc_msgSend$discardedFramesUpTo4mStale
+ _objc_msgSend$discardedFramesUpTo5mStale
+ _objc_msgSend$discardedFramesUpTo6mStale
+ _objc_msgSend$display
+ _objc_msgSend$display:didCompleteSwitchToCBFlipbookState:withError:
+ _objc_msgSend$display:didCompleteTransitionToCADisplayState:currentState:transitionStatus:
+ _objc_msgSend$display:didCompleteTransitionToCBDisplayMode:withError:
+ _objc_msgSend$displayId
+ _objc_msgSend$displayIdentifier
+ _objc_msgSend$displayInterfaces
+ _objc_msgSend$displayModeWithError:
+ _objc_msgSend$displayOffCount
+ _objc_msgSend$displayOnCount
+ _objc_msgSend$displayReferences
+ _objc_msgSend$displayState:isUpdatingToBrightnessCurve:withDuration:
+ _objc_msgSend$displayType
+ _objc_msgSend$displayWakeTelemetries
+ _objc_msgSend$displays
+ _objc_msgSend$durationSeconds
+ _objc_msgSend$elapsedSecondsActive
+ _objc_msgSend$endContinuousSeconds
+ _objc_msgSend$endpoint
+ _objc_msgSend$enteringAOTCount
+ _objc_msgSend$environmentIdentifiers
+ _objc_msgSend$environmentStateMachine:didUpdateFlipbookVisualState:specifier:
+ _objc_msgSend$environmentUpdateOperation
+ _objc_msgSend$eventType
+ _objc_msgSend$expiredPossibleCount
+ _objc_msgSend$flipbookArbiter
+ _objc_msgSend$flipbookLayoutSeconds
+ _objc_msgSend$flipbookOperation
+ _objc_msgSend$flipbookRenderSeconds
+ _objc_msgSend$generateSeed
+ _objc_msgSend$generatedSeed
+ _objc_msgSend$hadExistingSystemActivityForEvent:
+ _objc_msgSend$hasExplicitFlipbook
+ _objc_msgSend$highLuminanceAODsupported
+ _objc_msgSend$highLuminanceAODsupportedInCB
+ _objc_msgSend$hostEnvironment:clientDidUpdateNeedsFlipbookStateUpdates:
+ _objc_msgSend$hostEnvironment:clientDidUpdateNeedsLowPowerRenderingStateUpdates:
+ _objc_msgSend$hostEnvironment:hostDidSetLowPowerRendering:
+ _objc_msgSend$hostScene
+ _objc_msgSend$incrementPerformEventCounterWithEvent:
+ _objc_msgSend$init
+ _objc_msgSend$initDisplayResourceHintWithSurfaceType:andState:
+ _objc_msgSend$initForDisplay:
+ _objc_msgSend$initForDisplay:delegate:platformProvider:osInterfaceProvider:
+ _objc_msgSend$initForDisplay:delegate:platformProvider:osInterfaceProvider:inactiveBudgetPolicy:
+ _objc_msgSend$initForDisplay:platformProvider:
+ _objc_msgSend$initForDisplay:platformProvider:eventPerformer:osInterfaceProvider:
+ _objc_msgSend$initForDisplay:platformProvider:osInterfaceProvider:inactiveBudgetPolicy:
+ _objc_msgSend$initForService:display:
+ _objc_msgSend$initWithActiveAppearance:updateFidelity:adjustedLuminance:dimmed:flipbook:lowPowerRendering:
+ _objc_msgSend$initWithBacklightHost:
+ _objc_msgSend$initWithBacklightState:displayMode:flipbookState:alwaysOnEnabled:
+ _objc_msgSend$initWithBacklightState:sourceEvent:explanation:startTimestamp:changeEvent:
+ _objc_msgSend$initWithCADisplay:
+ _objc_msgSend$initWithCADisplay:platformProvider:osInterfaceProvider:
+ _objc_msgSend$initWithClientType:configType:
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$initWithDate:fidelity:userObject:lowPowerRenderingPresentationTime:
+ _objc_msgSend$initWithDelegate:flipbook:presentation:osInterfaceProvider:display:
+ _objc_msgSend$initWithDisplayID:
+ _objc_msgSend$initWithDisplayMode:prewarmingDisplayMode:lastSteadyStateDisplayMode:caDisplayState:cbDisplayMode:sleepMonitorAggregateState:hasEnsureFlipbookCurrent:
+ _objc_msgSend$initWithEventID:state:previousState:wasTransitioning:changeRequest:display:
+ _objc_msgSend$initWithEvents:withInitialSpecifier:targetDisplayMode:
+ _objc_msgSend$initWithFBScenes:flipbookContext:expirationDate:
+ _objc_msgSend$initWithFlipbookOperation:environmentUpdateOperation:flipbookFirst:
+ _objc_msgSend$initWithFrame:sourceFrameType:
+ _objc_msgSend$initWithIdentifier:queue:
+ _objc_msgSend$initWithIsFlipbook:initialSpecifier:
+ _objc_msgSend$initWithIsFlipbook:initialSpecifier:events:targetDisplayMode:
+ _objc_msgSend$initWithLocalAssertionService:osInterfaceProvider:
+ _objc_msgSend$initWithLocalBacklightProxy:peer:display:
+ _objc_msgSend$initWithLocalService:peer:osInterfaceProvider:
+ _objc_msgSend$initWithPlatformDelegate:telemetrySource:
+ _objc_msgSend$initWithPlatformDelegate:telemetrySource:analyticsRecorder:
+ _objc_msgSend$initWithPlatformProvider:osInterfaceProvider:inactiveBudgetPolicy:localAssertionService:telemetryPlatformDelegate:localOnly:
+ _objc_msgSend$initWithPresentationDate:fidelity:environment:userObject:lowPowerRenderingPresentationTime:
+ _objc_msgSend$initWithPresentationDate:specifiers:lowPowerRenderingPresentationTime:sourceFrameType:
+ _objc_msgSend$initWithProviderFactory:
+ _objc_msgSend$initWithResourceCount:
+ _objc_msgSend$initWithTarget:visualState:presentationDate:isFlipbook:hasExplicitFlipbook:
+ _objc_msgSend$initWithTransactionID:shouldGenerateSeed:
+ _objc_msgSend$initWithWakeDurationSeconds:wasInactiveOn:endpoint:wakeReason:beforeKernelWake:secondsAfterKernelWake:pageinDiff:compressionsDiff:performEventCount:completedEventsCount:abortedEventsCount:allEventsToWakeDurationSeconds:didCompleteDurationSeconds:systemActivityAcquisitionSeconds:didTimeoutSystemActivty:timeoutTriggerdBlackFlash:systemActivityAcquisitionSuccess:systemActivityAcquisitionDetails:systemActivityAcquisitionSkipped:
+ _objc_msgSend$initiatingContext
+ _objc_msgSend$intervalUntilFirstFrame
+ _objc_msgSend$invalidatedFramesHistogram
+ _objc_msgSend$invalidatedFramesUpTo2mStale
+ _objc_msgSend$invalidatedFramesUpTo3mStale
+ _objc_msgSend$invalidatedFramesUpTo4mStale
+ _objc_msgSend$invalidatedFramesUpTo5mStale
+ _objc_msgSend$invalidatedFramesUpTo6mStale
+ _objc_msgSend$isBeforeDisplayBlankingChange
+ _objc_msgSend$isCloningDisabled
+ _objc_msgSend$isCommitPending
+ _objc_msgSend$isCompositingWithLowPowerRenderer
+ _objc_msgSend$isEqualToVisualStateIgnoringFlipbookAndLowPowerRendering:
+ _objc_msgSend$isFlipbook
+ _objc_msgSend$isLowPowerRendering
+ _objc_msgSend$isLowPowerRenderingDisabled
+ _objc_msgSend$isMainThread
+ _objc_msgSend$isOwned
+ _objc_msgSend$isUpdatedToBacklightState:lowPowerRenderingDisabled:
+ _objc_msgSend$keysOfEntriesPassingTest:
+ _objc_msgSend$listenForOSStartupComplete
+ _objc_msgSend$listenerWithConfiguration:handler:
+ _objc_msgSend$logMetricsTimerFired
+ _objc_msgSend$loggingName
+ _objc_msgSend$longestInterval
+ _objc_msgSend$lowPowerRendering
+ _objc_msgSend$lowPowerRenderingPresentationTime
+ _objc_msgSend$makeStartupCheck
+ _objc_msgSend$mapTableWithKeyOptions:valueOptions:
+ _objc_msgSend$name
+ _objc_msgSend$needsFlipbookStateUpdates
+ _objc_msgSend$needsLowPowerRenderingStateUpdates
+ _objc_msgSend$newVisualStateWithUpdateFidelity:flipbook:lowPowerRendering:
+ _objc_msgSend$noTimeSetCount
+ _objc_msgSend$nonImmediateAcquireBlock
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$observesRampingToBrightnessCurve
+ _objc_msgSend$pageinDiff
+ _objc_msgSend$performCommitToMeasure
+ _objc_msgSend$performEventCount
+ _objc_msgSend$platformContext
+ _objc_msgSend$platformDelegate
+ _objc_msgSend$possibleCount
+ _objc_msgSend$prepareForStartupCheck
+ _objc_msgSend$presentationDuration
+ _objc_msgSend$presentationEngine:didChangeLowPowerRenderingDisabled:
+ _objc_msgSend$providerForDisplay:
+ _objc_msgSend$providersByDisplayId
+ _objc_msgSend$queueWithName:serviceQuality:
+ _objc_msgSend$reasonEnded
+ _objc_msgSend$referenceForAggregateDisplay
+ _objc_msgSend$referenceId
+ _objc_msgSend$referenceIdForCADisplay:
+ _objc_msgSend$registerAttributeHandler:
+ _objc_msgSend$registerBacklightHost:forDisplay:
+ _objc_msgSend$registerHandlerForService:display:
+ _objc_msgSend$registerScene:
+ _objc_msgSend$rejectedPossibleCount
+ _objc_msgSend$remoteToken
+ _objc_msgSend$removeObjectsForKeys:
+ _objc_msgSend$renderedFrameCount
+ _objc_msgSend$renderedPartialMinuteCount
+ _objc_msgSend$renderedPresentationSeconds
+ _objc_msgSend$rtcAlarmsCount
+ _objc_msgSend$sceneForIdentityToken:
+ _objc_msgSend$secondsAfterKernelWake
+ _objc_msgSend$secondsDisplayOff
+ _objc_msgSend$secondsDisplayOn
+ _objc_msgSend$secondsShowingAOT
+ _objc_msgSend$sendEventAsync:payloadBuilder:
+ _objc_msgSend$serialQueueWithQOSClass:label:
+ _objc_msgSend$serializedPayload
+ _objc_msgSend$serverWithLocalAssertionService:osInterfaceProvider:
+ _objc_msgSend$serviceWithPlatformProvider:osInterfaceProvider:inactiveBudgetPolicy:localAssertionService:telemetryPlatformDelegate:localOnly:
+ _objc_msgSend$sessionFramesHistogram
+ _objc_msgSend$setAbortedEventsCount:
+ _objc_msgSend$setAllEventsToWakeDurationSeconds:
+ _objc_msgSend$setAlwaysOnEnabled:
+ _objc_msgSend$setArbiter:
+ _objc_msgSend$setBacklightProxy:forDisplay:
+ _objc_msgSend$setBeforeKernelWake:
+ _objc_msgSend$setChangedSettingsWhileOffCount:
+ _objc_msgSend$setCloningDisabled:
+ _objc_msgSend$setCompletedEventsCount:
+ _objc_msgSend$setCompositingWithLowPowerRenderer:
+ _objc_msgSend$setCompressionsDiff:
+ _objc_msgSend$setConfirmedPossibleCount:
+ _objc_msgSend$setDidCompleteDurationSeconds:
+ _objc_msgSend$setDidTimeoutSystemActivity:
+ _objc_msgSend$setDiscardedFramesUpTo2mStale:
+ _objc_msgSend$setDiscardedFramesUpTo3mStale:
+ _objc_msgSend$setDiscardedFramesUpTo4mStale:
+ _objc_msgSend$setDiscardedFramesUpTo5mStale:
+ _objc_msgSend$setDiscardedFramesUpTo6mStale:
+ _objc_msgSend$setDisplayIdentifier:
+ _objc_msgSend$setDisplayOffCount:
+ _objc_msgSend$setDisplayOnCount:
+ _objc_msgSend$setDisplays:
+ _objc_msgSend$setDurationSeconds:
+ _objc_msgSend$setEndContinuousSeconds:
+ _objc_msgSend$setEndpoint:
+ _objc_msgSend$setEnteringAOTCount:
+ _objc_msgSend$setEventType:
+ _objc_msgSend$setExpiredPossibleCount:
+ _objc_msgSend$setExplanation:
+ _objc_msgSend$setFlipbookLayoutSeconds:
+ _objc_msgSend$setFlipbookRenderSeconds:
+ _objc_msgSend$setFlipbookState:
+ _objc_msgSend$setFlipbookTelemetryDelegate:
+ _objc_msgSend$setHasExplicitFlipbook:
+ _objc_msgSend$setHighLuminanceSupportedByCoreBrightness:
+ _objc_msgSend$setInvalidatedFramesUpTo2mStale:
+ _objc_msgSend$setInvalidatedFramesUpTo3mStale:
+ _objc_msgSend$setInvalidatedFramesUpTo4mStale:
+ _objc_msgSend$setInvalidatedFramesUpTo5mStale:
+ _objc_msgSend$setInvalidatedFramesUpTo6mStale:
+ _objc_msgSend$setIsFlipbook:
+ _objc_msgSend$setLowPowerRendering:
+ _objc_msgSend$setLowPowerRenderingDisabled:
+ _objc_msgSend$setLowPowerRenderingPresentationTime:
+ _objc_msgSend$setNoTimeSetCount:
+ _objc_msgSend$setNonImmediateAcquireBlock:
+ _objc_msgSend$setOwned:
+ _objc_msgSend$setPageinDiff:
+ _objc_msgSend$setPerformEventCount:
+ _objc_msgSend$setPlatformDelegate:
+ _objc_msgSend$setPossibleCount:
+ _objc_msgSend$setPresentation:completion:
+ _objc_msgSend$setPresentationHandler:queue:
+ _objc_msgSend$setQueue:
+ _objc_msgSend$setRejectedPossibleCount:
+ _objc_msgSend$setRenderedFrameCount:
+ _objc_msgSend$setRenderedPartialMinuteCount:
+ _objc_msgSend$setRenderedPresentationSeconds:
+ _objc_msgSend$setRtcAlarmsCount:
+ _objc_msgSend$setSecondsAfterKernelWake:
+ _objc_msgSend$setSecondsDisplayOff:
+ _objc_msgSend$setSecondsDisplayOn:
+ _objc_msgSend$setSecondsShowingAOT:
+ _objc_msgSend$setSleepCount:
+ _objc_msgSend$setSleepOver2mCount:
+ _objc_msgSend$setSleepOver3mCount:
+ _objc_msgSend$setSleepOver4mCount:
+ _objc_msgSend$setSleepOver5mCount:
+ _objc_msgSend$setSleepOver6mCount:
+ _objc_msgSend$setSoftwareRequestCount:
+ _objc_msgSend$setSourceEvent:
+ _objc_msgSend$setStartContinuousSeconds:
+ _objc_msgSend$setSystemActivityAcquisitionDetails:
+ _objc_msgSend$setSystemActivityAcquisitionSeconds:
+ _objc_msgSend$setSystemActivityAcquisitionSkipped:
+ _objc_msgSend$setSystemActivityAcquisitionSuccess:
+ _objc_msgSend$setTargetDisplayMode:
+ _objc_msgSend$setTelemetryDelegate:
+ _objc_msgSend$setTimeoutTriggeredBlackFlash:
+ _objc_msgSend$setTotalTimeSeconds:
+ _objc_msgSend$setWakeCount:
+ _objc_msgSend$setWakeReason:
+ _objc_msgSend$setWasInactiveOn:
+ _objc_msgSend$setWillTransitionBacklightState:
+ _objc_msgSend$sharedAnalyticsSender
+ _objc_msgSend$sharedBacklightForDisplay:
+ _objc_msgSend$sharedService
+ _objc_msgSend$sharedTelemetrySource
+ _objc_msgSend$shortestInterval
+ _objc_msgSend$shouldBlockTransitionPassIsBeforeDisplayBlankingChange:willUnblank:didUnblank:
+ _objc_msgSend$sleepCount
+ _objc_msgSend$sleepOver2mCount
+ _objc_msgSend$sleepOver3mCount
+ _objc_msgSend$sleepOver4mCount
+ _objc_msgSend$sleepOver5mCount
+ _objc_msgSend$sleepOver6mCount
+ _objc_msgSend$softwareRequestCount
+ _objc_msgSend$source
+ _objc_msgSend$sourceFrameType
+ _objc_msgSend$specifierWithPresentationDate:specifiers:lowPowerRenderingPresentationTime:sourceFrameType:
+ _objc_msgSend$startContinuousSeconds
+ _objc_msgSend$startObserving
+ _objc_msgSend$startTimestamp
+ _objc_msgSend$stopObserving
+ _objc_msgSend$stringForEventType:
+ _objc_msgSend$surfaceType
+ _objc_msgSend$systemActivityAcquisitionDetails
+ _objc_msgSend$systemActivityAcquisitionSeconds
+ _objc_msgSend$systemActivityAcquisitionSkipped
+ _objc_msgSend$systemActivityAcquisitionSuccess
+ _objc_msgSend$targetDisplayState
+ _objc_msgSend$telemetryBLSBacklightEventTelemetryEnabled
+ _objc_msgSend$telemetryBLSSystemWakeTelemetryEnabled
+ _objc_msgSend$telemetryContextForBacklightEvent:
+ _objc_msgSend$telemetryContextForSystemWakeMetrics:
+ _objc_msgSend$telemetryContextWithTransactionID:shouldGenerateSeed:
+ _objc_msgSend$telemetryEventKeyForSystemWakeMetrics
+ _objc_msgSend$telemetryLogSystemWakeMetricsToPowerLog:
+ _objc_msgSend$telemetryPowerLogPayloadForBacklightEvent:changeEvent:
+ _objc_msgSend$telemetryServicePlatformDelegate
+ _objc_msgSend$timedOutCount
+ _objc_msgSend$timedOutEnvironmentCount
+ _objc_msgSend$timeoutTriggeredBlackFlash
+ _objc_msgSend$tokenDidInvalidate:
+ _objc_msgSend$totalCount
+ _objc_msgSend$totalPreparationDuration
+ _objc_msgSend$totalTimeSeconds
+ _objc_msgSend$traitsForDisplayUUID:
+ _objc_msgSend$transactionID
+ _objc_msgSend$transitionToDisplayMode:withDuration:didChangeAlwaysOnBrightnessCurve:
+ _objc_msgSend$uniqueId
+ _objc_msgSend$unregisterScene:
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$updateFlipbookVisualState:backlightState:withInitialSpecifier:
+ _objc_msgSend$updateToBacklightState:forEvent:touchTargetable:presentationDate:sceneUpdate:lowPowerRenderingPresentationTime:performBacklightRamp:
+ _objc_msgSend$updateToDateSpecifier:sceneContentsUpdated:lowPowerRenderingDisabled:
+ _objc_msgSend$updateToFlipbookVisualState:backlightState:presentationDate:sceneUpdate:lowPowerRenderingPresentationTime:
+ _objc_msgSend$wakeCount
+ _objc_msgSend$wakeDurationSeconds
+ _objc_msgSend$wakeReason
+ _objc_msgSend$wasInactiveOn
+ _objc_msgSend$wasReset
+ _objc_msgSend$willTransitionBacklightState
+ _objc_msgSend$willUnblankForEvent:
+ _objc_msgSend$workloop
+ _objc_release_x2
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x5
+ _objc_retain_x6
+ _sharedAnalyticsSender.__analyticsSender
+ _sharedAnalyticsSender.onceToken
+ _sharedInstance.onceToken
+ _sharedInstance.result
+ _sw_kernel_wake_mach_continuous_time
+ _sysctlbyname
+ _workloop.onceToken
- +[BLSHBacklightHost checkForWatchdogDidFire:]
- +[BLSHBacklightHost registerSharedBacklightHost:]
- +[BLSHBacklightHost registerSharedBacklightHost:].cold.1
- +[BLSHBacklightHost registerSharedBacklightHost:].cold.2
- +[BLSHBacklightHost registerSharedBacklightHostForTest:]
- +[BLSHBacklightHost sharedBacklightHost].cold.1
- +[BLSHBacklightIdleProvider createSharedProviderWithLocalAssertionService:].cold.1
- +[BLSHBacklightIdleProvider sharedProvider].cold.1
- +[BLSHFlipbook createWithPlatformProvider:]
- +[BLSHXPCAssertionServiceHostServer serverWithLocalAssertionService:]
- +[BLSHXPCAssertionServiceHostServer serverWithLocalAssertionService:].cold.1
- +[BLSHXPCBacklightProxyHostServer serverWithLocalBacklightProxy:]
- +[BLSHXPCBacklightProxyHostServer serverWithLocalBacklightProxy:].cold.1
- -[BLSHAlwaysOnPresentationEngine initWithDelegate:platformProvider:osInterfaceProvider:inactiveBudgetPolicy:]
- -[BLSHAlwaysOnPresentationEngine initWithDelegate:platformProvider:osInterfaceProvider:inactiveBudgetPolicy:].cold.1
- -[BLSHBacklightDisplayStateMachine displayModeForOSInterfaceProvider:]
- -[BLSHBacklightDisplayStateMachine initWithDelegate:platformProvider:osInterfaceProvider:]
- -[BLSHBacklightDisplayStateMachine osInterfaceProvider:didCompleteSwitchToCBFlipbookState:withError:]
- -[BLSHBacklightDisplayStateMachine osInterfaceProvider:didCompleteSwitchToCBFlipbookState:withError:].cold.1
- -[BLSHBacklightDisplayStateMachine osInterfaceProvider:didCompleteTransitionToCADisplayState:currentState:transitionStatus:]
- -[BLSHBacklightDisplayStateMachine osInterfaceProvider:didCompleteTransitionToCBDisplayMode:withError:]
- -[BLSHBacklightDisplayStateMachine osInterfaceProvider:didCompleteTransitionToCBDisplayMode:withError:].cold.1
- -[BLSHBacklightDisplayStateMachine osInterfaceProvider:didCompleteTransitionToCBDisplayMode:withError:].cold.2
- -[BLSHBacklightDisplayStateMachineAbortContext initWithDisplayMode:prewarmingDisplayMode:lastSteadyStateDisplayMode:caDisplayState:cbDisplayMode:showingBlankingWindow:sleepMonitorAggregateState:hasEnsureFlipbookCurrent:]
- -[BLSHBacklightFBSceneHostEnvironment updateToDateSpecifier:sceneContentsUpdated:]
- -[BLSHBacklightOSInterfaceProvider _didCompleteTransitionToDisplayMode:withError:]
- -[BLSHBacklightOSInterfaceProvider abortContextForTimer:]
- -[BLSHBacklightOSInterfaceProvider acquireDisplayPowerAssertionForReason:]
- -[BLSHBacklightOSInterfaceProvider caDisplayPowerState]
- -[BLSHBacklightOSInterfaceProvider caDisplayState]
- -[BLSHBacklightOSInterfaceProvider cbDisplayMode]
- -[BLSHBacklightOSInterfaceProvider cbFlipbookState]
- -[BLSHBacklightOSInterfaceProvider clearCAWatchdog]
- -[BLSHBacklightOSInterfaceProvider createDisplayPowerResourceHintWithState:]
- -[BLSHBacklightOSInterfaceProvider createFlipbook]
- -[BLSHBacklightOSInterfaceProvider delegateQueue]
- -[BLSHBacklightOSInterfaceProvider didCompleteSwitchToFlipbookState:withError:]
- -[BLSHBacklightOSInterfaceProvider didCompleteTransitionToDisplayMode:withError:]
- -[BLSHBacklightOSInterfaceProvider didDetectSignificantUserInteraction]
- -[BLSHBacklightOSInterfaceProvider displayStateDelegate]
- -[BLSHBacklightOSInterfaceProvider endSuppressionService]
- -[BLSHBacklightOSInterfaceProvider identifier]
- -[BLSHBacklightOSInterfaceProvider initWithPlatformProvider:].cold.1
- -[BLSHBacklightOSInterfaceProvider isFlipbookTransparent]
- -[BLSHBacklightOSInterfaceProvider isShowingBlankingWindow]
- -[BLSHBacklightOSInterfaceProvider isSuppressionServiceActive]
- -[BLSHBacklightOSInterfaceProvider lastSuppressionEvent]
- -[BLSHBacklightOSInterfaceProvider notifyDisplayBlankedIfChangedForCADisplayState:]
- -[BLSHBacklightOSInterfaceProvider osInterfaceProvider]
- -[BLSHBacklightOSInterfaceProvider registerHandlersForService:].cold.1
- -[BLSHBacklightOSInterfaceProvider scheduleOSIPWatchdogWithExplanation:type:]
- -[BLSHBacklightOSInterfaceProvider setCATransitionsDelayForTesting:]
- -[BLSHBacklightOSInterfaceProvider setCBTransitionsDelayForTesting:]
- -[BLSHBacklightOSInterfaceProvider setDisplayStateDelegate:]
- -[BLSHBacklightOSInterfaceProvider setFlipbookTransparent:]
- -[BLSHBacklightOSInterfaceProvider setLastSuppressionEvent:]
- -[BLSHBacklightOSInterfaceProvider setShowingBlankingWindow:fadeDuration:]
- -[BLSHBacklightOSInterfaceProvider setSuppressionServiceActive:]
- -[BLSHBacklightOSInterfaceProvider startSuppressionServiceWithHandler:]
- -[BLSHBacklightOSInterfaceProvider supportsFlipbookState]
- -[BLSHBacklightOSInterfaceProvider switchToFlipbookState:]
- -[BLSHBacklightOSInterfaceProvider switchToFlipbookState:].cold.1
- -[BLSHBacklightOSInterfaceProvider timeoutForWatchdogType:]
- -[BLSHBacklightOSInterfaceProvider transitionToCADisplayState:]
- -[BLSHBacklightOSInterfaceProvider transitionToDisplayMode:withDuration:]
- -[BLSHBacklightOSInterfaceProvider transitionToDisplayMode:withDuration:].cold.1
- -[BLSHBacklightService initWithPlatformProvider:osInterfaceProvider:inactiveBudgetPolicy:localAssertionService:localOnly:]
- -[BLSHBacklightStateMachine initWithPlatformProvider:eventPerformer:osInterfaceProvider:]
- -[BLSHBacklightTransitionStateMachine displayState:didUpdateToBrightnessCurve:]
- -[BLSHBacklightTransitionStateMachine initWithPlatformProvider:osInterfaceProvider:inactiveBudgetPolicy:]
- -[BLSHBacklightTransitionStateMachine initWithPlatformProvider:osInterfaceProvider:inactiveBudgetPolicy:].cold.1
- -[BLSHBacklightTransitionStateMachine onMainWithLock_environmentUpdateOperationForEvents:]
- -[BLSHBacklightTransitionStateMachine onMain_performNextStepInTransition].cold.16
- -[BLSHBacklightTransitionStateMachine onMain_performNextStepInTransition].cold.17
- -[BLSHBasePlatformProvider isShowingBlankingWindow]
- -[BLSHBasePlatformProvider showBlankingWindow:withFadeDuration:]
- -[BLSHBaseSceneHostEnvironment updateToDateSpecifier:sceneContentsUpdated:]
- -[BLSHCancelWhenBacklightInactivatesAttributeEntry initForAttribute:fromAssertion:forService:]
- -[BLSHDiagnosticsServer listener:didReceiveConnection:withContext:]
- -[BLSHDiagnosticsServer listener:didReceiveConnection:withContext:].cold.1
- -[BLSHEngineRenderFlipbookSession initWithDelegate:flipbook:presentation:osInterfaceProvider:]
- -[BLSHEnvironmentTransitionState isUpdatedToBacklightState:]
- -[BLSHEnvironmentTransitionState updateToBacklightState:forEvent:touchTargetable:presentationDate:sceneUpdate:performBacklightRamp:]
- -[BLSHFlipbook initWithPlatformProvider:]
- -[BLSHFlipbook initWithPlatformProvider:].cold.1
- -[BLSHFlipbookPowerSavingProvider init]
- -[BLSHLocalAssertionService existingAttributeHandlerForClasses:]
- -[BLSHLocalAssertionService queue_registerAttributeHandler:forAttributeClasses:]
- -[BLSHLocalAssertionService registerAttributeHandler:forAttributeClasses:]
- -[BLSHLocalHostSceneEnvironment updateToDateSpecifier:sceneContentsUpdated:]
- -[BLSHLocalHostSceneEnvironment updateToDateSpecifier:sceneContentsUpdated:].cold.1
- -[BLSHLocalHostSceneEnvironment updateToDateSpecifier:sceneContentsUpdated:].cold.2
- -[BLSHLocalHostSceneEnvironment updateToDateSpecifier:sceneContentsUpdated:].cold.3
- -[BLSHLocalHostSceneEnvironment updateToDateSpecifier:sceneContentsUpdated:].cold.4
- -[BLSHLocalHostSceneEnvironment updateToDateSpecifier:sceneContentsUpdated:].cold.5
- -[BLSHLocalOnlySimplePlatformProvider isShowingBlankingWindow]
- -[BLSHLocalOnlySimplePlatformProvider showBlankingWindow:withFadeDuration:]
- -[BLSHPendingEnvironmentUpdateOperation initWithEvents:withInitialSpecifier:]
- -[BLSHPresentationDateSpecifier initWithPresentationDate:specifiers:]
- -[BLSHXPCAssertionServiceHost initWithLocalService:peer:]
- -[BLSHXPCAssertionServiceHostServer initWithLocalAssertionService:]
- -[BLSHXPCAssertionServiceHostServer initWithLocalAssertionService:].cold.1
- -[BLSHXPCAssertionServiceHostServer initWithLocalAssertionService:].cold.2
- -[BLSHXPCAssertionServiceHostServer listener:didReceiveConnection:withContext:]
- -[BLSHXPCAssertionServiceHostServer listener:didReceiveConnection:withContext:].cold.1
- -[BLSHXPCBacklightProxyHost initWithLocalBacklightProxy:peer:]
- -[BLSHXPCBacklightProxyHostServer initWithLocalBacklightProxy:]
- -[BLSHXPCBacklightProxyHostServer initWithLocalBacklightProxy:].cold.1
- -[BLSHXPCBacklightProxyHostServer initWithLocalBacklightProxy:].cold.2
- -[BLSHXPCBacklightProxyHostServer listener:didReceiveConnection:withContext:]
- -[BLSHXPCBacklightProxyHostServer listener:didReceiveConnection:withContext:].cold.1
- GCC_except_table107
- GCC_except_table129
- GCC_except_table130
- GCC_except_table131
- GCC_except_table138
- GCC_except_table139
- GCC_except_table186
- GCC_except_table187
- GCC_except_table188
- GCC_except_table189
- GCC_except_table26
- GCC_except_table28
- GCC_except_table30
- GCC_except_table37
- GCC_except_table38
- GCC_except_table43
- GCC_except_table54
- GCC_except_table55
- GCC_except_table62
- GCC_except_table70
- GCC_except_table72
- GCC_except_table73
- GCC_except_table76
- GCC_except_table81
- _BKSHIDServicesGetBacklightFactor
- _BSDispatchQueueCreate
- _OBJC_CLASS_$_BSDispatchQueueAttributes
- _OBJC_IVAR_$_BLSHBacklightDisplayStateMachine._powerResourceHint
- _OBJC_IVAR_$_BLSHBacklightDisplayStateMachineAbortContext._showingBlankingWindow
- _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._backlightDimmedFactor
- _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._caTransitionsDelayForTesting
- _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._cbTransitionsDelayForTesting
- _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._displayStateClientSupported
- _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._displayStateDelegate
- _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._lock_CAWatchdogTimer
- _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._lock_CAWatchdogType
- _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._lock_CBWatchdogTimer
- _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._lock_CBWatchdogType
- _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._lock_caDisplayState
- _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._lock_cbDisplayMode
- _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._lock_cbFlipbookState
- _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._lock_lastSuppressionEvent
- _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._lock_notifiedCADisplayState
- _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._lock_suppressionServiceActive
- _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._suppressionManager
- _OBJC_IVAR_$_BLSHBacklightService._stateMachine
- _OBJC_IVAR_$_BLSHBacklightService._transitionStateMachine
- _OBJC_IVAR_$_BLSHXPCAssertionServiceHost._remoteProcessHandle
- _OBJC_IVAR_$_BLSHXPCBacklightProxyHostServer._callbackQueue
- _OBJC_IVAR_$_BLSHXPCBacklightProxyHostServer._localBacklightProxy
- _OUTLINED_FUNCTION_63
- __OBJC_$_INSTANCE_METHODS_BLSHBacklightEnvironmentPresentation
- __OBJC_$_INSTANCE_METHODS_BLSHFlipbookFramesHistogram
- __OBJC_$_INSTANCE_METHODS_BLSHFlipbookInvalidationTelemetryData
- __OBJC_$_INSTANCE_METHODS_BLSHFlipbookRenderSessionTelemetryData
- __OBJC_$_INSTANCE_METHODS_BLSHFlipbookRequestDatesTelemetryData
- __OBJC_$_PROP_LIST_BLSHDiagnosticsServer
- __OBJC_$_PROP_LIST_BLSHFlipbook.197
- __OBJC_$_PROP_LIST_BLSHFlipbookFramesHistogram
- __OBJC_$_PROP_LIST_BLSHFlipbookInvalidationTelemetryData
- __OBJC_$_PROP_LIST_BLSHFlipbookRenderSessionTelemetryData
- __OBJC_$_PROP_LIST_BLSHFlipbookRequestDatesTelemetryData
- __OBJC_$_PROP_LIST_BLSHXPCAssertionServiceHostServer
- __OBJC_$_PROP_LIST_BLSHXPCBacklightProxyHostServer
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSServiceConnectionListenerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_BSServiceConnectionListenerDelegate
- __OBJC_$_PROTOCOL_REFS_BSServiceConnectionListenerDelegate
- __OBJC_CLASS_PROTOCOLS_$_BLSHDiagnosticsServer
- __OBJC_CLASS_PROTOCOLS_$_BLSHXPCAssertionServiceHostServer
- __OBJC_CLASS_PROTOCOLS_$_BLSHXPCBacklightProxyHostServer
- __OBJC_LABEL_PROTOCOL_$_BSServiceConnectionListenerDelegate
- __OBJC_PROTOCOL_$_BSServiceConnectionListenerDelegate
- ___101-[BLSHBacklightDisplayStateMachine osInterfaceProvider:didCompleteSwitchToCBFlipbookState:withError:]_block_invoke
- ___102-[BLSHBacklightEnvironmentStateMachine onMain_performEvent:withInitialSpecifier:performBacklightRamp:]_block_invoke.186
- ___103-[BLSHBacklightDisplayStateMachine osInterfaceProvider:didCompleteTransitionToCBDisplayMode:withError:]_block_invoke
- ___105-[BLSHBacklightTransitionStateMachine initWithPlatformProvider:osInterfaceProvider:inactiveBudgetPolicy:]_block_invoke
- ___105-[BLSHBacklightTransitionStateMachine initWithPlatformProvider:osInterfaceProvider:inactiveBudgetPolicy:]_block_invoke_2
- ___108-[BLSHAlwaysOnPresentationEngine lock_cancelFlipbookFramesForReason:source:didClearDateSpecifiers:wasReset:]_block_invoke.253
- ___108-[BLSHAlwaysOnPresentationEngine lock_cancelFlipbookFramesForReason:source:didClearDateSpecifiers:wasReset:]_block_invoke.253.cold.1
- ___109-[BLSHAlwaysOnPresentationEngine initWithDelegate:platformProvider:osInterfaceProvider:inactiveBudgetPolicy:]_block_invoke
- ___118-[BLSHWatchdogProvider _fireWatchdogWithTimer:delegate:timeout:elapsedTime:abortContext:explanation:remainingRetries:]_block_invoke.137
- ___118-[BLSHWatchdogProvider _fireWatchdogWithTimer:delegate:timeout:elapsedTime:abortContext:explanation:remainingRetries:]_block_invoke.137.cold.1
- ___118-[BLSHWatchdogProvider _fireWatchdogWithTimer:delegate:timeout:elapsedTime:abortContext:explanation:remainingRetries:]_block_invoke.137.cold.2
- ___118-[BLSHWatchdogProvider _fireWatchdogWithTimer:delegate:timeout:elapsedTime:abortContext:explanation:remainingRetries:]_block_invoke.137.cold.3
- ___123-[BLSHBacklightEnvironmentStateMachine checkCompletedOperationsToBacklightState:visualState:transitionState:isBeginUpdate:]_block_invoke.232
- ___124-[BLSHAlwaysOnPresentationEngine requestDatesOperation:environment:didProvideSpecifiers:forPresentationInterval:isComplete:]_block_invoke.222
- ___124-[BLSHAlwaysOnPresentationEngine requestDatesOperation:environment:didProvideSpecifiers:forPresentationInterval:isComplete:]_block_invoke.226
- ___124-[BLSHAlwaysOnPresentationEngine requestDatesOperation:environment:didProvideSpecifiers:forPresentationInterval:isComplete:]_block_invoke.226.cold.1
- ___124-[BLSHAlwaysOnPresentationEngine requestDatesOperation:environment:didProvideSpecifiers:forPresentationInterval:isComplete:]_block_invoke.227
- ___124-[BLSHBacklightDisplayStateMachine osInterfaceProvider:didCompleteTransitionToCADisplayState:currentState:transitionStatus:]_block_invoke
- ___124-[BLSHBacklightFBSceneHostEnvironment requestDateSpecifiersForDateInterval:previousPresentationDate:shouldReset:completion:]_block_invoke.90
- ___124-[BLSHBacklightFBSceneHostEnvironment requestDateSpecifiersForDateInterval:previousPresentationDate:shouldReset:completion:]_block_invoke.93
- ___132-[BLSHEnvironmentTransitionState updateToBacklightState:forEvent:touchTargetable:presentationDate:sceneUpdate:performBacklightRamp:]_block_invoke
- ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.66
- ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.75
- ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.75.cold.1
- ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.79
- ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.79.cold.1
- ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.83
- ___183-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:]_block_invoke.83.cold.1
- ___34-[BLSHFlipbook hangDetectorFired:]_block_invoke.21
- ___38-[BLSHSystemWaker watchdogTimerFired:]_block_invoke.107
- ___43-[BLSHWatchdogTester _triggerTestWatchdog:]_block_invoke.67
- ___43-[BLSHWatchdogTester _triggerTestWatchdog:]_block_invoke.71
- ___49+[BLSHBacklightHost registerSharedBacklightHost:]_block_invoke
- ___50-[BLSHLocalAssertionService queue_pauseAssertion:]_block_invoke.38
- ___51-[BLSHLocalAssertionService queue_resumeAssertion:]_block_invoke.44
- ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke.110
- ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke.114
- ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke.117
- ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke.124
- ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke_2.118
- ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke_2.128
- ___59-[BLSHBacklightOSInterfaceProvider setFlipbookTransparent:]_block_invoke
- ___61-[BLSHDiagnosticsServer initWithFlipbookDiagnosticsProvider:]_block_invoke.cold.1
- ___61-[BLSHLocalAssertionService queue_cancelAssertion:withError:]_block_invoke.77
- ___63-[BLSHBacklightOSInterfaceProvider transitionToCADisplayState:]_block_invoke
- ___63-[BLSHBacklightOSInterfaceProvider transitionToCADisplayState:]_block_invoke.173
- ___63-[BLSHBacklightOSInterfaceProvider transitionToCADisplayState:]_block_invoke.175
- ___63-[BLSHBacklightOSInterfaceProvider transitionToCADisplayState:]_block_invoke.175.cold.1
- ___63-[BLSHXPCBacklightProxyHostServer initWithLocalBacklightProxy:]_block_invoke
- ___63-[BLSHXPCBacklightProxyHostServer initWithLocalBacklightProxy:]_block_invoke.cold.1
- ___64-[BLSHLocalAssertionService existingAttributeHandlerForClasses:]_block_invoke
- ___64-[BLSHLocalAssertionService queue_restartAssertionTimeoutTimer:]_block_invoke.83
- ___67-[BLSHDiagnosticsServer listener:didReceiveConnection:withContext:]_block_invoke
- ___67-[BLSHDiagnosticsServer listener:didReceiveConnection:withContext:]_block_invoke.8
- ___67-[BLSHDiagnosticsServer listener:didReceiveConnection:withContext:]_block_invoke.8.cold.1
- ___67-[BLSHDiagnosticsServer listener:didReceiveConnection:withContext:]_block_invoke.cold.1
- ___67-[BLSHLocalAssertionService queue_acquireAssertion:skipSleepCheck:]_block_invoke.61
- ___67-[BLSHLocalAssertionService queue_acquireAssertion:skipSleepCheck:]_block_invoke.69
- ___67-[BLSHLocalAssertionService queue_acquireAssertion:skipSleepCheck:]_block_invoke.69.cold.1
- ___67-[BLSHXPCAssertionServiceHostServer initWithLocalAssertionService:]_block_invoke
- ___67-[BLSHXPCAssertionServiceHostServer initWithLocalAssertionService:]_block_invoke.cold.1
- ___69-[BLSHBacklightStateMachine systemSleepAction:performWithCompletion:]_block_invoke.201
- ___70-[BLSHBacklightStateMachine updateSuppressionServiceForActivityState:]_block_invoke.141
- ___71-[BLSHBacklightOSInterfaceProvider startSuppressionServiceWithHandler:]_block_invoke
- ___71-[BLSHBacklightOSInterfaceProvider startSuppressionServiceWithHandler:]_block_invoke.cold.1
- ___73-[BLSHBacklightOSInterfaceProvider transitionToDisplayMode:withDuration:]_block_invoke
- ___73-[BLSHBacklightTransitionStateMachine onMain_performNextStepInTransition]_block_invoke.249
- ___74-[BLSHLocalAssertionService registerAttributeHandler:forAttributeClasses:]_block_invoke
- ___76-[BLSHLocalHostSceneEnvironment updateToDateSpecifier:sceneContentsUpdated:]_block_invoke
- ___77-[BLSHAlwaysOnPresentationEngine hostEnvironment:invalidateContentForReason:]_block_invoke.242
- ___77-[BLSHAlwaysOnPresentationEngine hostEnvironment:invalidateContentForReason:]_block_invoke_2.243
- ___77-[BLSHEngineRenderFlipbookSession renderFrameSpecifier:timedOutEnvironments:]_block_invoke.618
- ___77-[BLSHEngineRenderFlipbookSession renderFrameSpecifier:timedOutEnvironments:]_block_invoke.619
- ___77-[BLSHEngineRenderFlipbookSession renderFrameSpecifier:timedOutEnvironments:]_block_invoke.620
- ___77-[BLSHXPCBacklightProxyHostServer listener:didReceiveConnection:withContext:]_block_invoke
- ___77-[BLSHXPCBacklightProxyHostServer listener:didReceiveConnection:withContext:]_block_invoke.8
- ___77-[BLSHXPCBacklightProxyHostServer listener:didReceiveConnection:withContext:]_block_invoke.8.cold.1
- ___77-[BLSHXPCBacklightProxyHostServer listener:didReceiveConnection:withContext:]_block_invoke.cold.1
- ___78-[BLSHAlwaysOnPresentationEngine lock_scheduleUpdateTimerForNextUpdatesStart:]_block_invoke.319
- ___79-[BLSHXPCAssertionServiceHostServer listener:didReceiveConnection:withContext:]_block_invoke
- ___79-[BLSHXPCAssertionServiceHostServer listener:didReceiveConnection:withContext:]_block_invoke.8
- ___79-[BLSHXPCAssertionServiceHostServer listener:didReceiveConnection:withContext:]_block_invoke.8.cold.1
- ___79-[BLSHXPCAssertionServiceHostServer listener:didReceiveConnection:withContext:]_block_invoke.cold.1
- ___80-[BLSHLocalAssertionService queue_registerAttributeHandler:forAttributeClasses:]_block_invoke
- ___81-[BLSHBacklightOSInterfaceProvider didCompleteTransitionToDisplayMode:withError:]_block_invoke
- ___81-[BLSHBacklightOSInterfaceProvider didCompleteTransitionToDisplayMode:withError:]_block_invoke.cold.1
- ___82-[BLSHBacklightFBSceneHostEnvironment updateToDateSpecifier:sceneContentsUpdated:]_block_invoke
- ___82-[BLSHBacklightFBSceneHostEnvironment updateToDateSpecifier:sceneContentsUpdated:]_block_invoke.104
- ___82-[BLSHBacklightFBSceneHostEnvironment updateToDateSpecifier:sceneContentsUpdated:]_block_invoke.104.cold.1
- ___86-[BLSHAlwaysOnPresentationEngine requestDatesOperation:didTimeoutPendingEnvironments:]_block_invoke.228
- ___87-[BLSHBacklightTransitionStateMachine inactiveEnvironmentSession:updateToPresentation:]_block_invoke.269
- ___87-[BLSHBacklightTransitionStateMachine inactiveEnvironmentSession:updateToPresentation:]_block_invoke.272
- ___87-[BLSHBacklightTransitionStateMachine inactiveEnvironmentSession:updateToPresentation:]_block_invoke.277
- ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke.137
- ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke.140
- ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke.143
- ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke.157
- ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke.161
- ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke.167
- ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke_2.146
- ___88-[BLSHFlipbook renderFrameForPresentation:dateSpecifier:onRenderBegin:onRenderComplete:]_block_invoke.76
- ___89-[BLSHBacklightStateMachine initWithPlatformProvider:eventPerformer:osInterfaceProvider:]_block_invoke
- ___89-[BLSHBacklightStateMachine initWithPlatformProvider:eventPerformer:osInterfaceProvider:]_block_invoke.81
- ___89-[BLSHBacklightStateMachine initWithPlatformProvider:eventPerformer:osInterfaceProvider:]_block_invoke_2
- ___89-[BLSHLocalHostSceneEnvironmentUpdater updatedEnvironmentWithDelta:backlightSceneUpdate:]_block_invoke.217
- ___89-[BLSHLocalHostSceneEnvironmentUpdater updatedEnvironmentWithDelta:backlightSceneUpdate:]_block_invoke.217.cold.1
- ___90-[BLSHBacklightDisplayStateMachine initWithDelegate:platformProvider:osInterfaceProvider:]_block_invoke
- ___90-[BLSHBacklightTransitionStateMachine onMainWithLock_environmentUpdateOperationForEvents:]_block_invoke
- ___94-[BLSHEngineRenderFlipbookSession initWithDelegate:flipbook:presentation:osInterfaceProvider:]_block_invoke
- ____BLSHShowWatchdogFailureAlert_block_invoke.111
- ____springboardDidFinishStartup_block_invoke
- ____springboardDidFinishStartup_block_invoke_2
- ___block_descriptor_40_e40_B16?0"BLSHEnvironmentTransitionState"8l
- ___block_descriptor_40_e44_B24?0"BLSHEnvironmentTransitionState"8^B16l
- ___block_descriptor_41_e8_32s_e11_v24?0q8q16ls32l8
- ___block_descriptor_48_e8_32r_e57_v32?0"NSArray"8"<BLSHAssertionAttributeHandler>"16^B24lu40l8r32l8
- ___block_descriptor_48_e8_32s40r_e57_v32?0"NSArray"8"<BLSHAssertionAttributeHandler>"16^B24ls32l8r40l8
- ___block_descriptor_48_e8_32s40s_e50_v16?0"<BSServiceConnectionInternalConfiguring>"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e50_v16?0"<BSServiceConnectionListenerConfiguring>"8ls32l8s40l8
- ___block_descriptor_48_e8_32s_e11_v24?0q8q16ls32l8
- ___block_descriptor_48_e8_32s_e61_v28?0B8"NSError"12"<SWSystemActivityAcquisitionDetails>"20ls32l8
- ___block_descriptor_48_e8_32s_e8_v12?0B8ls32l8
- ___block_descriptor_56_e8_32s40s48r_e57_v16?0"BSServiceConnection<BSServiceConnectionContext>"8ls32l8r48l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e33_v16?0"FBSMutableSceneSettings"8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e57_v32?0"NSArray"8"<BLSHAssertionAttributeHandler>"16^B24ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s_e8_v12?0B8ls32l8
- ___block_descriptor_64_e8_32s40s48s56s_e57_v32?0"NSArray"8"<BLSHAssertionAttributeHandler>"16^B24ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56s_e61_v28?0B8"NSError"12"<SWSystemActivityAcquisitionDetails>"20ls32l8s40l8s48l8s56l8
- ___block_descriptor_65_e8_32s40s48s56s_e57_v32?0"NSArray"8"<BLSHAssertionAttributeHandler>"16^B24ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e60_"FBSSceneTransitionContext"16?0"FBSMutableSceneSettings"8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_72_e8_32s40s48s56s64s_e67_v16?0"<BSTimerScheduleQuerying><BSCancellable><BSInvalidatable>"8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_72_e8_32s40s48s56s_e67_v16?0"<BSTimerScheduleQuerying><BSCancellable><BSInvalidatable>"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64s72s_e61_v28?0B8"NSError"12"<SWSystemActivityAcquisitionDetails>"20ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_98_e8_32s40s48s56s64s72bs80bs88bs_e60_"FBSSceneTransitionContext"16?0"FBSMutableSceneSettings"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_literal_global.116
- ___block_literal_global.119
- ___block_literal_global.123
- ___block_literal_global.139
- ___block_literal_global.142
- ___block_literal_global.145
- ___block_literal_global.146
- ___block_literal_global.148
- ___block_literal_global.149
- ___block_literal_global.162
- ___block_literal_global.185
- ___block_literal_global.186
- ___block_literal_global.189
- ___block_literal_global.194
- ___block_literal_global.224
- ___block_literal_global.234
- ___block_literal_global.257
- ___block_literal_global.268
- ___block_literal_global.271
- ___block_literal_global.274
- ___block_literal_global.276
- ___block_literal_global.286
- ___block_literal_global.32
- ___block_literal_global.37
- ___block_literal_global.43
- ___block_literal_global.49
- ___block_literal_global.612
- ___block_literal_global.70
- ___block_literal_global.96
- __classLock_block_invoke.onceToken
- __sharedBacklightHost
- __springboardDidFinishStartup
- _objc_msgSend$configureConnection:
- _objc_msgSend$createWithPlatformProvider:
- _objc_msgSend$didCompleteTransitionToDisplayMode:withError:
- _objc_msgSend$displayState
- _objc_msgSend$displayStateDelegate
- _objc_msgSend$firstObjectCommonWithArray:
- _objc_msgSend$initWithActiveAppearance:updateFidelity:adjustedLuminance:dimmed:
- _objc_msgSend$initWithClientType:
- _objc_msgSend$initWithDate:fidelity:userObject:
- _objc_msgSend$initWithDelegate:flipbook:presentation:osInterfaceProvider:
- _objc_msgSend$initWithDelegate:platformProvider:osInterfaceProvider:
- _objc_msgSend$initWithDelegate:platformProvider:osInterfaceProvider:inactiveBudgetPolicy:
- _objc_msgSend$initWithDisplayMode:prewarmingDisplayMode:lastSteadyStateDisplayMode:caDisplayState:cbDisplayMode:showingBlankingWindow:sleepMonitorAggregateState:hasEnsureFlipbookCurrent:
- _objc_msgSend$initWithEventID:state:previousState:wasTransitioning:changeRequest:
- _objc_msgSend$initWithEvents:withInitialSpecifier:
- _objc_msgSend$initWithLocalAssertionService:
- _objc_msgSend$initWithLocalBacklightProxy:
- _objc_msgSend$initWithLocalBacklightProxy:peer:
- _objc_msgSend$initWithLocalService:peer:
- _objc_msgSend$initWithPlatformProvider:eventPerformer:osInterfaceProvider:
- _objc_msgSend$initWithPlatformProvider:osInterfaceProvider:inactiveBudgetPolicy:
- _objc_msgSend$initWithPlatformProvider:osInterfaceProvider:inactiveBudgetPolicy:localAssertionService:localOnly:
- _objc_msgSend$initWithPresentationDate:specifiers:
- _objc_msgSend$initWithResourceType:andState:
- _objc_msgSend$initWithTarget:visualState:presentationDate:
- _objc_msgSend$isShowingBlankingWindow
- _objc_msgSend$isUpdatedToBacklightState:
- _objc_msgSend$listenerWithConfigurator:
- _objc_msgSend$mainDisplay
- _objc_msgSend$osInterfaceProvider:didCompleteSwitchToCBFlipbookState:withError:
- _objc_msgSend$osInterfaceProvider:didCompleteTransitionToCADisplayState:currentState:transitionStatus:
- _objc_msgSend$osInterfaceProvider:didCompleteTransitionToCBDisplayMode:withError:
- _objc_msgSend$registerAttributeHandler:forAttributeClasses:
- _objc_msgSend$registerSharedBacklightHost:
- _objc_msgSend$relativePriority
- _objc_msgSend$remoteProcess
- _objc_msgSend$serial
- _objc_msgSend$serverWithLocalAssertionService:
- _objc_msgSend$serverWithLocalBacklightProxy:
- _objc_msgSend$serviceClass
- _objc_msgSend$serviceClass:relativePriority:
- _objc_msgSend$serviceWithPlatformProvider:osInterfaceProvider:inactiveBudgetPolicy:localAssertionService:localOnly:
- _objc_msgSend$setDefaultBacklightProxy:
- _objc_msgSend$setDomain:
- _objc_msgSend$setPresentation:withCompletion:
- _objc_msgSend$setService:
- _objc_msgSend$setServiceQuality:
- _objc_msgSend$setShowingBlankingWindow:fadeDuration:
- _objc_msgSend$setTargetQueue:
- _objc_msgSend$showBlankingWindow:withFadeDuration:
- _objc_msgSend$transitionToDisplayMode:withDuration:
- _objc_msgSend$updateToBacklightState:forEvent:touchTargetable:presentationDate:sceneUpdate:performBacklightRamp:
- _objc_msgSend$updateToDateSpecifier:sceneContentsUpdated:
- _registerSharedBacklightHost:.onceToken
CStrings:
+ "%@ != %@ in %@"
+ "%@ already active, ignoring (currentState %u)"
+ "%@ already inactive, ignoring (currentState %u)"
+ "%@ createInactiveEnvironmentSessionForDisplay: should have been called, not %@"
+ "%@ service not started"
+ "%@-%llx"
+ "%lu"
+ "%p (localHostEnv) updateToVisualState: calling performBacklightSceneUpdate: on delegate for %{public}@ %{public}@ with %{public}@ specifier:%{public}@"
+ "%p (localHostUpdater) created dateSpecifier with lprTime:%llu from scene settings"
+ "%p WakeTelemetry measure on commit timed out for transactionID:%lld"
+ "%p class %@ does not respond to selector setLowPowerRendering:, cannot acquire assertion with BLSLowPowerRenderingAttribute : %@"
+ "%p class %@ does not respond to selector setLowPowerRendering:, cannot deactivate assertion with BLSLowPowerRenderingAttribute : %@"
+ "%p did activate connection:%{public}@"
+ "%p did activate diagnostics connection:%{public}@"
+ "%p did configure connection for display:%{public}@"
+ "%p did configure diagnostics connection"
+ "%p did invalidate connection for interfaceTarget:%{public}@ display:%{public}@"
+ "%p no backlight proxy found for display:%{public}@"
+ "%p server init with listener:%{public}@"
+ "%p updates(%d) (exceeded budget - will coalesce) specifier:%{public}@ nextSpecifier:%{public}@ valid:(%{public}@->%{public}@) gapDuration:%1.3lg env:%{public}@"
+ "%p updates(%d) (exceeded budget - will not coalesce) specifier:%{public}@ nextSpecifier:%{public}@ valid:(%{public}@->%{public}@) gapDuration:%1.3lg env:%{public}@"
+ "%p updates(%d) (will coalesce) specifier:%{public}@ nextSpecifier:%{public}@ valid:(%{public}@->%{public}@) gapDuration:%1.3lg env:%{public}@"
+ "%p updates(%d) (will not coalesce) validSpecifier:%{public}@ specifier:%{public}@ nextSpecifier:%{public}@ valid:(%{public}@->%{public}@) gapDuration:%1.3lg env:%{public}@"
+ "%p will handle connection:%{public}@ for display:%{public}@"
+ "%p:%llu presentationHandler called but invalid displayOnMachTime:%{public}@ displayOnCATime:%lf seedWasPresented:%{BOOL}u (%u >=? %u)"
+ "%p:%llu presentationHandler called displayOnMachTime:%{public}@ displayOnCATime:%lf seedWasPresented:%{BOOL}u (%u >=? %u)"
+ "%p:%llu presentationHandler called early displayOnMachTime:%{public}@ displayOnCATime:%lf seedWasPresented:%{BOOL}u (%u >=? %u)"
+ "%p:%llu presentationHandler called twice displayOnMachTime:%{public}@ displayOnCATime:%lf seedWasPresented:%{BOOL}u (%u >=? %u)"
+ "%p:%llu will perform commit due to invalidation"
+ "%p:%llu will perform commit to measure"
+ "%p:%{public}@ clientDidUpdateNeedsFlipbookStateUpdates:%{BOOL}u"
+ "%p:%{public}@ clientDidUpdateNeedsLowPowerRenderingStateUpdates:%{BOOL}u"
+ "%p:%{public}@ did disable low power rendering"
+ "%p:%{public}@ did re-enable low power rendering"
+ "%p:%{public}@:%{public}@ (%{public}@) did complete %srequest dates operation:%{public}@, interval:%{public}@ specifiers:%{public}@"
+ "%p:%{public}@:%{public}@ (%{public}@) updated %srequest dates operation:%{public}@, interval:%{public}@ specifiers:%{public}@"
+ "%p:%{public}@:%{public}@ (live) hostEnvironment:%{public}@ hostDidSetUnrestrictedFramerateUpdates:%{BOOL}u"
+ "%p:%{public}@:%{public}@ (nil next update) timer already scheduled but %lfs is more than %lfs in the future, will reschedule for %{public}@"
+ "%p:%{public}@:%{public}@ (nil next update) timer already scheduled in %lfs will not reschedule"
+ "%p:%{public}@:%{public}@ (nil next update) timer already scheduled in %lfs will replace with waking timer"
+ "%p:%{public}@:%{public}@ (nil next update) will use 30 seconds from now, nextsUpdateStart:%{public}@"
+ "%p:%{public}@:%{public}@ (suppressed — skipped filling flipbook) sleepActionState:%{public}@ fillState:%{public}@ onStandby:%{BOOL}u"
+ "%p:%{public}@:%{public}@ (waiting for flipbook) sleepActionState:%{public}@ fillState:%{public}@ onStandby:%{BOOL}u"
+ "%p:%{public}@:%{public}@ did create engine with:%{public}@ telemetryDelegate:%{public}@"
+ "%p:%{public}@:%{public}@ did create render session for flipbook memoryUsage:%{public}@(aprox:%{public}@)/%{public}@ updates:%{public}@"
+ "%p:%{public}@:%{public}@ did timeout render dates operation:%{public}@ pendingEnvironments:%{public}@"
+ "%p:%{public}@:%{public}@ ending render session:%p for reason:%{public}@ sleepActionState:%{public}@ fillState:%{public}@ stby:%{BOOL}u sup:%{BOOL}u memoryUsage:%{public}@/%{public}@ %{public}@"
+ "%p:%{public}@:%{public}@ engine starting live from flipbook, will live update to:%{public}@"
+ "%p:%{public}@:%{public}@ flipbook full, will not render more frames memoryUsage:%{public}@/%{public}@ count:%u nextsUpdateStart:%{public}@ updatesCount:%u"
+ "%p:%{public}@:%{public}@ invalidated content will not invalidate flipbook (not in presentation) for source:%{public}@ reason:%{public}@ environment:%{public}@"
+ "%p:%{public}@:%{public}@ live flipbook will not render frames, have scheduled timer:%{public}@"
+ "%p:%{public}@:%{public}@ next update(%{public}@) %lfs from now(%{public}@), will set timer"
+ "%p:%{public}@:%{public}@ no more updates, will not render more frames"
+ "%p:%{public}@:%{public}@ not requesting dates for interval:%{public}@ (no missingIntervals)"
+ "%p:%{public}@:%{public}@ now:%{public}@ is%s in updates:%{public}@"
+ "%p:%{public}@:%{public}@ perform systemSleepAction sleepActionState=%{public}@ fillState:%{public}@ onStandby:%{BOOL}u suppressed:%{BOOL}u"
+ "%p:%{public}@:%{public}@ performing live updates for specifier:%{public}@"
+ "%p:%{public}@:%{public}@ received updates:%{public}@"
+ "%p:%{public}@:%{public}@ request dates timeout will now render frames, waited %.3lfs for operation:%{public}@"
+ "%p:%{public}@:%{public}@ requesting dates for interval:%{public}@ missingIntervals:%{public}@"
+ "%p:%{public}@:%{public}@ requesting updates activeCount:%u lastRenderedFrame:%{public}@"
+ "%p:%{public}@:%{public}@ scheduling timer for %{public}@ nextsUpdateStart:%{public}@"
+ "%p:%{public}@:%{public}@ scheduling waking timer %{public}@ is too soon, using %lf seconds from now:%{public}@ nextsUpdateStart:%{public}@"
+ "%p:%{public}@:%{public}@ scheduling waking timer for %{public}@ nextsUpdateStart:%{public}@"
+ "%p:%{public}@:%{public}@ sleep immenient - do no more work"
+ "%p:%{public}@:%{public}@ suppressed - do no more work"
+ "%p:%{public}@:%{public}@ timer already scheduled in %lfs will not schedule a new timer for %{public}@"
+ "%p:%{public}@:%{public}@ timer too soon (will just dispatch_async) for %{public}@ nextsUpdateStart:%{public}@"
+ "%p:%{public}@:%{public}@ update1HzFromPresentation new1HzFlipbook:%{BOOL}u old1HzFlipbook:%{BOOL}u environment:%{public}@ presentation::%{public}@"
+ "%p:%{public}@:%{public}@ updateLowPowerRenderingFromPresentation newLPR:%{BOOL}u oldLPR:%{BOOL}u disabled:%{BOOL}u presentationLPR:%{BOOL}u presentation:%{public}@"
+ "%p:%{public}@:%{public}@ wait for AP wake before completing notify current"
+ "%p:%{public}@:%{public}@ waiting for last session render frame:%{public}@"
+ "%p:%{public}@:%{public}@ will complete sleep action for reason:%{public}@ subReason:%{public}@ sleepActionState=%{public}@ fillState:%{public}@ onStandby:%{BOOL}u suppressed:%{BOOL}u"
+ "%p:%{public}@:%{public}@ will ignore invalidate flipbook (rendering live) for source:%{public}@ reason:%{public}@ environment:%{public}@"
+ "%p:%{public}@:%{public}@ will not render frames, empty presentation session:%{public}@"
+ "%p:%{public}@:%{public}@ will not render frames, waiting for backoff time:%{public}@ timer:%{public}@"
+ "%p:%{public}@:%{public}@ will not render more frames, waiting to begin previous render:%{public}@"
+ "%p:%{public}@:%{public}@ will notify current, sleeping but have %.2lfs worth of flipbook frames"
+ "%p:%{public}@:%{public}@ will render frame:%{public}@"
+ "%p:%{public}@:%{public}@ will render frames, waiting (enough) %.3lfs for operation:%{public}@ timer:%{public}@"
+ "%p:%{public}@:%{public}@ will use 30 seconds from now, nextsUpdateStart:%{public}@"
+ "%p:%{public}@:%{public}@->%{public}@ %{public}@ sleepActionState=%{public}@ fillState:%{public}@->Awake onStandby:%{BOOL}u suppressed:%{BOOL}u changed:%{BOOL}u shouldNotifyFlipbookCurrent:%{BOOL}u shouldServiceTimer:%{BOOL}u"
+ "%p:%{public}@:%{public}@->%{public}@ did change flipbook render type sleepActionState:%{public}@ fillState:%{public}@ onStandby:%{BOOL}u"
+ "%p:%{public}@:%{public}@->Stopped engine %s (%{public}@) %s:%{public}@"
+ "; "
+ "<%@: %p; transactionID=%llu seed=%u active=%u activeTime:%.3fs>"
+ "@\"BLSDisplayReference\"16@?0@\"CADisplay\"8"
+ "@\"BLSHOSDisplayInterface\"16@?0@\"CADisplay\"8"
+ "@\"NSDictionary\"8@?0"
+ "B16@?0@\"BLSAttribute\"8"
+ "B16@?0@\"CADisplay\"8"
+ "B32@?0@\"BLSBacklightChangeEvent\"8@\"BLSHBacklightWakeTelemetryTracker\"16^B24"
+ "BLS flipbook %@ hang detected – %.4lfs elapsed"
+ "BLSHAggregateBacklightHost.m"
+ "BLSHBacklightEnvironmentSessionProvider.m"
+ "BLSHBacklightService.m"
+ "BLSHBaseBacklightEnvironmentSessionProvider.m"
+ "BLSHCoreAnalyticsWorkLoop"
+ "BLSHDisplayWakeTelemetry.m"
+ "BLSHDisplayWakeTelemetry: backlightEventTelemetryEnabled=%{BOOL}d"
+ "BLSHDisplayWakeTelemetry: backlightEventTelemetryEnabled=%{BOOL}d powerLog=Backlight::BacklightStateChange hasCustomPayload=%{BOOL}d"
+ "BLSHDisplayWakeTelemetry: backlightEventTelemetryEnabled=NO (disabled via disableTelemetry default)"
+ "BLSHDisplayWakeTelemetry: failed to create telemetry identifier for Backlight::BacklightStateChange"
+ "BLSHInfiniteResourceOwnershipToken deallocated without being invalidated - this is a programming error"
+ "BLSHMeasureCommitOnWakeOperation.m"
+ "BLSHMeasureCommitOnWakeOperation:%llu"
+ "BLSHOSDisplayInterface.m"
+ "BLSHResourceArbiter.m"
+ "BLSHResourceOwnershipToken deallocated without being invalidated - this is a programming error"
+ "BLSHSystemWakeTelemetry startObserving with eventKey: %{public}@, powerLog: Backlight::SystemWakeMetrics"
+ "BLSHSystemWakeTelemetry: blsTelemetryEnabled=%{BOOL}d hasDelegate=%{BOOL}d"
+ "BLSHSystemWakeTelemetry: blsTelemetryEnabled=NO (disabled via disableTelemetry default)"
+ "BLSHSystemWakeTelemetry: failed to create telemetry identifier for Backlight::SystemWakeMetrics"
+ "BLSHSystemWakeTelemetry: skipping startObserving (platform opted out via delegate)"
+ "BLSHSystemWakeTelemetry: skipping telemetry emission (disabled)"
+ "BSM:%p:%@ suppressed but suppression service not active"
+ "BSM:%p:%{public}@ (no longer active) unexpected system sleep - isActive:%{BOOL}u activeOnAPAssertion:%{BOOL}u – will not send request:%{public}@ %{public}@"
+ "BSM:%p:%{public}@ (no longer requested) unexpected system sleep - hasSleepActionCompletion:%{BOOL}u %{public}@ - will not send request:%{public}@"
+ "BSM:%p:%{public}@ (no sleep action completion) unexpected system sleep - will not send request:%{public}@ %{public}@"
+ "BSM:%p:%{public}@ (sleep not requested) unexpected system sleep – will not send request:%{public}@ %{public}@"
+ "BSM:%p:%{public}@ (will not sleep - %@) unexpected system sleep - will not send request %{public}@"
+ "BSM:%p:%{public}@ activeOn system activity assertion callback details:%{public}@ event:%{public}@ elapsed:%.4lfs error:%{public}@"
+ "BSM:%p:%{public}@ activeOn system activity assertion timed out (related to rdar://74802930) event:%{public}@ elapsed:%.4lfs"
+ "BSM:%p:%{public}@ didChangeAlwaysOnSetting:%{BOOL}u"
+ "BSM:%p:%{public}@ didCompleteUpdateToState:%{public}@ elapsed:%.4lfs forEvents:%{public}@"
+ "BSM:%p:%{public}@ performEvent system activity assertion callback details:%{public}@ event:%{public}@ elapsed:%.4lfs error:%{public}@"
+ "BSM:%p:%{public}@ sendNewChangeRequest explanation:%{public}@ request:%{public}@"
+ "BSM:%p:%{public}@ setAlwaysOnDisabledByAssertion:%{BOOL}u"
+ "BSM:%p:%{public}@ startup activeOn system activity assertion callback details:%{public}@ elapsed:%.4lfs error:%{public}@"
+ "BSM:%p:%{public}@ startup alwaysOnEnabledByPlatform:%{BOOL}u"
+ "BSM:%p:%{public}@ suppressionEvent explanation:%{public}@ request:%{public}@ event:%{public}@"
+ "BSM:%p:%{public}@ system sleep while acquiring system activity, did not deactivate backlight"
+ "BSM:%p:%{public}@ unexpected system sleep - assertion acquired %{public}@ {elapsedTime:%lf timerInterval:%lf} — dispatching request:%{public}@"
+ "BSM:%p:%{public}@ unexpected system sleep - did deactivate backlight with events:%{public}@"
+ "BSM:%p:%{public}@ unexpected system sleep - will deactivate backlight with request:%{public}@ %{public}@"
+ "BSM:%p:%{public}@ unexpected system sleep - will wait %lfs before sending request:%{public}@"
+ "BSM:%p:%{public}@ will %send suppression service after significant user interaction; activityState:%{public}@"
+ "BSM:%p:%{public}@ will %send suppression service; activityState:%{public}@ unsuppressedTargetBacklightState:%{public}@"
+ "BSM:%p:%{public}@ will %sstart suppression service; activityState:%{public}@ unsuppressedTargetBacklightState:%{public}@"
+ "BSM:%p:%{public}@ will ignore suppressionEvent — arrived after service was deactivated — explanation:%{public}@ event:%{public}@"
+ "BSM:%p:%{public}@ will performRequest with event:%{public}@"
+ "Backlight"
+ "BacklightStateChange"
+ "CADisplayStateControl nil for %@ - %@ - this process needs entitlement: 'com.apple.QuartzCore.display-state'"
+ "DSM:%p:%@ did not have transition, but lastSteadyStateDisplayMode(%@) != targetDisplayMode(%@)"
+ "DSM:%p:%@ did not have transition, but watchdog timer is non-nil: %@"
+ "DSM:%p:%@ transition to displayMode:%@ duration:%lf seqId:%d interrupting previous setDisplayMode:%@ duration:%lf seqId:%d with started at:%@"
+ "DSM:%p:%{public}@ (completed except CB target:%{public}@) waited %lfs for CB callback to cbDisplayMode:%{public}@->%{public}@"
+ "DSM:%p:%{public}@ (likely initialization) core animation completed(%{public}@) switch to display state:%{public}@ currentState:%{public}@"
+ "DSM:%p:%{public}@ (likely initialization) core brightness completed switch to display mode:%{public}@"
+ "DSM:%p:%{public}@ (no prewarm) will start turning on display"
+ "DSM:%p:%{public}@ (pending change flipbook state for %{public}@) still waiting to update CA to %@ (waited %lfs)"
+ "DSM:%p:%{public}@ (pending change flipbook state for %{public}@) waited %lfs for CB callback to cbDisplayMode:%{public}@->%{public}@"
+ "DSM:%p:%{public}@ already have live rendering system activity assertion %{public}@"
+ "DSM:%p:%{public}@ core animation completed transition to display state:%{public}@ (currentState:%{public}@) elapsed:%lfs"
+ "DSM:%p:%{public}@ core animation completed transition to wrong display state:%{public}@ (currentState:%{public}@), waiting for display state:%{public}@ phase:%u elapsed:%lfs"
+ "DSM:%p:%{public}@ core animation completed(%{public}@) transition to matching display state:%{public}@, (currentState:%{public}@), but operation is not started"
+ "DSM:%p:%{public}@ core animation reporting interrupted transition to display state:%{public}@, current display state:%{public}@ – pending transition to display state:%{public}@ phase:%u elapsed:%lfs"
+ "DSM:%p:%{public}@ core animation state transition status:%@ to display state:%{public}@, current display state:%{public}@ – pending transition to display state:%{public}@ phase:%u elapsed:%lfs"
+ "DSM:%p:%{public}@ core brightness completed switch to display mode:%{public}@"
+ "DSM:%p:%{public}@ core brightness completed switch to flipbook state:%{public}@"
+ "DSM:%p:%{public}@ core brightness completed switch to matching display mode:%{public}@, but operation is not started"
+ "DSM:%p:%{public}@ core brightness completed switch to wrong display mode:%{public}@, waiting for display mode:%{public}@ phase:%u"
+ "DSM:%p:%{public}@ core brightness completed switch to wrong flipbook state:%{public}@}, waiting for flipbook state:%{public}@"
+ "DSM:%p:%{public}@ core brightness failed to switch to display mode:%{public}@ error:%{public}@"
+ "DSM:%p:%{public}@ core brightness failed to switch to flipbook state:%{public}@ error:%{public}@"
+ "DSM:%p:%{public}@ didUpdateToMode:%{public}@ seqId:%d but has new transition to:%{public}@ seqId:%d"
+ "DSM:%p:%{public}@ didUpdateToMode:%{public}@ seqId:%d complete"
+ "DSM:%p:%{public}@ dropping live rendering system activity assertion %{public}@"
+ "DSM:%p:%{public}@ flipbook state is transitioning, begin reversing before performing ramp to:%{public}@ cbFlipbookState:%{public}@->%{public}@}"
+ "DSM:%p:%{public}@ flipbook state is transitioning, completing reversing before performing ramp to:%{public}@ cbFlipbookState:%{public}@->%{public}@"
+ "DSM:%p:%{public}@ hadTransition=%{BOOL}u mode:%{public}@ isLiveRendering:%{BOOL}u didReleaseLiveRendering:%{BOOL}u seqId:%d"
+ "DSM:%p:%{public}@ live rendering system activity assertion callback elapsed:%.4lfs details:%{public}@ error:%{public}@"
+ "DSM:%p:%{public}@ performNextStep supportsFlipbookState:%{BOOL}u displayIsOff:%{BOOL}u willUnblank:%{BOOL}u shouldTransitionCBBeforeCA:%{BOOL}u needToTransitionCA:%{BOOL}u hasCBTransition:%{BOOL}u isFlipbookStateTransitioning:%{BOOL}u isTurningOnDisplay:%{BOOL}u didPrewarmDisplayMode:%{BOOL}u isPendingCBDisplayMode:%{BOOL}u"
+ "DSM:%p:%{public}@ preWarmingToMode:%{public}@ fromMode:%{public}@ (waited %lfs)"
+ "DSM:%p:%{public}@ prewarmForDisplayMode:%{public}@->%{public}@%s previousPrewarm:%{public}@ hasAssertion:%{BOOL}u isPrewarmOn:%{BOOL}u requiresModeChange:%{BOOL}u shouldSignalPowerOn:%{BOOL}u shouldCleanup:%{BOOL}u cbDisplayMode:%{public}@"
+ "DSM:%p:%{public}@ ramp to displayMode:%{public}@ withDuration:%fs fullDuration:%fs shouldWaitForCompletion:%{BOOL}u"
+ "DSM:%p:%{public}@ replacing pending ramp to displayMode:%{public}@ withDuration:%fs fullDuration:%fs started at %{public}@ with ramp to displayMode:%{public}@ withDuration:%fs shouldWaitForCompletion:%{BOOL}u"
+ "DSM:%p:%{public}@ replacing pending switch to caDisplayState:%{public}@ from %lfs ago with switch to caDisplayState:%{public}@"
+ "DSM:%p:%{public}@ replacing pending switch to flipbookState:%{public}@ from %lfs ago with switch to flipbookState:%{public}@"
+ "DSM:%p:%{public}@ resumed display mode:%{public}@ did not match current target:%{public}@"
+ "DSM:%p:%{public}@ resumed transition to display mode:%{public}@"
+ "DSM:%p:%{public}@ reversing pending ramp to displayMode:%{public}@ withDuration:%fs fullDuration:%fs started at %{public}@ (%fs elapsed — %f%%) with ramp to displayMode:%{public}@ withDuration:%fs fullDuration:%fs shouldWaitForCompletion:%{BOOL}u"
+ "DSM:%p:%{public}@ setDisplayMode:%{public}@ duration:%lf seqId:%d"
+ "DSM:%p:%{public}@ setDisplayMode:%{public}@ duration:%lf seqId:%d interrupting previous setDisplayMode:%{public}@ duration:%lf seqId:%d with started at:%{public}@%{public}@"
+ "DSM:%p:%{public}@ startup displayMode:%{public}@ caDisplayState:%{public}@ cbDisplayMode:%{public}@"
+ "DSM:%p:%{public}@ waited %lfs for CB callback to cbDisplayMode:%{public}@->%{public}@"
+ "DSM:%p:%{public}@ waited %lfs for CB callback to cbFlipbookState:%{public}@->%{public}@"
+ "DSM:%p:%{public}@ waiting to update CA to %@ (waited %lfs)"
+ "DeviceSupportsAlwaysOnTime"
+ "ESM:%p calling updateFlipbookVisualState on invalidated state machine:%{public}@"
+ "ESM:%p checkFlipbookVisualStateCompletion (rdar://175348594) isBeginUpdate:%{BOOL}u transitionState:%{public}@ notInTrackingSet shouldComplete:%{BOOL}u remaining:%lu"
+ "ESM:%p flipbookVisualStateUpdateCompleted isFlipbook:%{BOOL}u specifier:%{public}@"
+ "ESM:%p updateFlipbookVisualState:%{BOOL}u initialSpecifier:%{public}@ environments:%@ now:%{public}@"
+ "ETS:%p:%{public}@ will update to target:%{public}@ wasUpdating:%{BOOL}u animated:%{BOOL}u hasBacklightRamp:%{BOOL}u event:%{public}@ touchTarget:%{BOOL}u lprTime:%llu"
+ "FBSceneHostEnv:%{public}@ setting lprTime:%llu on scene settings"
+ "Failed to get vm statistics. error %d\n"
+ "HighLuminanceAlwaysOn"
+ "Host Startup"
+ "LPR"
+ "No state machines created - no display interfaces available"
+ "OSDI:%p suppression event error - event:%{public}@ error:%{public}@ reason:%{public}@"
+ "OSDI:%p:%@ (init) transitionToDisplayMode:%@ withDuration:0"
+ "OSDI:%p:%@ cannot change cb display mode to %@, flipbook state:%@ is transitioning"
+ "OSDI:%p:%@ switchToFlipbookState:%@"
+ "OSDI:%p:%@ transitionToCADisplayState:%@"
+ "OSDI:%p:%@ transitionToDisplayMode:%@ withDuration:%fs"
+ "OSDI:%p:%{public}@ %sBacklightFactor:%f WithFadeDuration:%fs"
+ "OSDI:%p:%{public}@ (platformProvider) useAlwaysOnBrightnessCurve:%{BOOL}u withDuration:%fs"
+ "OSDI:%p:%{public}@ brightness is set to off/black but CA display is:%{public}@ will ignore brightness level"
+ "OSDI:%p:%{public}@ completed(%d) setFlipbookTransparent:%{BOOL}u"
+ "OSDI:%p:%{public}@ completion transitionToDisplayState(%{public}@->%{public}@) actual:%{public}@ status:%{public}@"
+ "OSDI:%p:%{public}@ completion transitionToDisplayState(%{public}@->%{public}@) status:%{public}@"
+ "OSDI:%p:%{public}@ could not switchToFlipbookState:%{public}@ error:%{public}@"
+ "OSDI:%p:%{public}@ could not transitionToDisplayMode:%{public}@ during init error:%{public}@"
+ "OSDI:%p:%{public}@ could not transitionToDisplayMode:%{public}@ error:%{public}@"
+ "OSDI:%p:%{public}@ dark boot detected, will set display initial state to off"
+ "OSDI:%p:%{public}@ delayCompletionsForTesting:YES, completing delayed CATransitionToDisplayState:%{public}@"
+ "OSDI:%p:%{public}@ delayCompletionsForTesting:YES, completing delayed didCompleteCBTransitionToDisplayMode"
+ "OSDI:%p:%{public}@ delayCompletionsForTesting:YES, delaying CATransitionToDisplayState:%{public}@ completion by %.2fs"
+ "OSDI:%p:%{public}@ delayCompletionsForTesting:YES, delaying didCompleteCBTransitionToDisplayMode by %.2fs"
+ "OSDI:%p:%{public}@ disableSuppression set to YES - use 'login -f mobile defaults delete com.apple.BacklightServices disableSuppression' to remove"
+ "OSDI:%p:%{public}@ flipbook no longer transparent, will transition to real flipbook"
+ "OSDI:%p:%{public}@ flipbook set transparent, will transition to active"
+ "OSDI:%p:%{public}@ flipbook transparent, will transition to CADisplayStateOn not CADisplayStateFlipBook"
+ "OSDI:%p:%{public}@ got didCompleteSwitchToFlipbookState:%{public}@ error:%@"
+ "OSDI:%p:%{public}@ got didCompleteTransitionToDisplayMode:%{public}@ error:%@"
+ "OSDI:%p:%{public}@ id:%{public}@ startup caDisplayState:%{public}@ cbDisplayMode:%{public}@->%{public}@ alwaysOn:%{BOOL}u flipbook:%{BOOL}u displayStateClient:%{BOOL}u alwaysOnSuppression:%{BOOL}u surfaceType:%d"
+ "OSDI:%p:%{public}@ nil displayTraits for %{public}@"
+ "OSDI:%p:%{public}@ setCATransitionsDelayForTesting:%.02fs"
+ "OSDI:%p:%{public}@ setCBTransitionsDelayForTesting:%.02fs"
+ "OSDI:%p:%{public}@ setCloningDisabled:%{BOOL}u"
+ "OSDI:%p:%{public}@ startup completion(on->off) actual:%{public}@ status:%{public}@"
+ "OSDI:%p:%{public}@ transitionToDisplayMode:%{public}@ withDuration:%fs"
+ "OSDI:%p:%{public}@ unable to read display mode - error:%{public}@ mode(oldCall):%{public}@"
+ "OSDI:%p:%{public}@ unsupported call to switchToFlipbookState:%{public}@"
+ "OSDI:%p:%{public}@ will acquire display power assertion"
+ "OSIP:%p maximumFlipbookCount set to %u - use 'login -f mobile defaults delete com.apple.BacklightServices maximumFlipbookCountOverride' to remove"
+ "Qa"
+ "SystemWakeMetrics"
+ "TSM:%p:%@ transition to backlight state for event:%@"
+ "TSM:%p:%{public}@ %{public}@will performEvent(%llu:%p) %{public}@->%{public}@ %{public}@:%{public}@ %{public}@->%{public}@ %{public}@%{public}@%{public}@\n%{public}@%{public}@"
+ "TSM:%p:%{public}@ (findNextOperation) [_pendingUpdatePresentation isCompleted] so setting to nil: %{public}@"
+ "TSM:%p:%{public}@ (findNextOperation) abandoning ensureFlipbookCurrentOperation %{public}@ because targetDisplayMode=%{public}@"
+ "TSM:%p:%{public}@ (findNextOperation) animating:%{BOOL}u forcedUnanimated:%{BOOL}u pending:%{public}@"
+ "TSM:%p:%{public}@ (findNextOperation) did not stop presentation engine:%{public}@ (displayMode:%{public}@)"
+ "TSM:%p:%{public}@ (findNextOperation) flipbook-off has no specifier — all fallbacks exhausted. currentDisplayMode:%{public}@ targetDisplayMode:%{public}@"
+ "TSM:%p:%{public}@ (findNextOperation) no operation needed isBeforeDisplayBlankingChange:%{BOOL}u hasEvents:%{BOOL}u needsFlipbook:%{BOOL}u"
+ "TSM:%p:%{public}@ (findNextOperation) no updateDisplayMode operation needed"
+ "TSM:%p:%{public}@ (findNextOperation) no updatePresentation operation needed — target:%{public}@ current:%{public}@"
+ "TSM:%p:%{public}@ (findNextOperation) no updateSpecifier needed"
+ "TSM:%p:%{public}@ (findNextOperation) ok to proceed (not to off) and updated to initial state animating:%{BOOL}u forcedUnanimated:%{BOOL}u  pending:%{public}@"
+ "TSM:%p:%{public}@ (findNextOperation) pending presentation update while determining display update, animating:%{BOOL}u forcedUnanimated:%{BOOL}u pending:%{public}@"
+ "TSM:%p:%{public}@ (findNextOperation) replaced pending %{public}@ with %{public}@"
+ "TSM:%p:%{public}@ (findNextOperation) returning existing updatePresentation operation: %{public}@"
+ "TSM:%p:%{public}@ (findNextOperation) started pendingEnvironmentUpdate %{public}@, will skip environment update for -> FlipbookSuppressed events:%{public}@"
+ "TSM:%p:%{public}@ (findNextOperation) still pending:%{public}@"
+ "TSM:%p:%{public}@ (findNextOperation) will discard specifier from presentation engine end:%{public}@ (no events, currentBacklightState:%u)"
+ "TSM:%p:%{public}@ (findNextOperation) will discard specifier from presentation engine end:%{public}@ (not needed for events:%{public}@)"
+ "TSM:%p:%{public}@ (findNextOperation) will start ensure flipbook current operation %{public}@"
+ "TSM:%p:%{public}@ (findNextOperation) will start ensure flipbook current operation %{public}@ and defer %{public}@"
+ "TSM:%p:%{public}@ (findNextOperation) will start:%{public}@"
+ "TSM:%p:%{public}@ (findNextOperation) will start:%{public}@ animating:%{BOOL}u forcedUnanimated:%{BOOL}u "
+ "TSM:%p:%{public}@ (findNextOperation) will update to specifier:%{public}@ prior to display mode:%{public}@->%{public}@"
+ "TSM:%p:%{public}@ (performNextStepInTransition) abandoning ensureFlipbookCurrentOperation %{public}@ because it's obsolete when completing transition"
+ "TSM:%p:%{public}@ (performNextStepInTransition) abandoning pendingEnvironmentUpdate %{public}@ because it's obsolete when completing transition"
+ "TSM:%p:%{public}@ (stopPresentationEngine) abandoning ensureFlipbookCurrentOperation %{public}@ because it's obsolete; displayMode=%{public}@"
+ "TSM:%p:%{public}@ LPR disable state changed disabled:%{BOOL}u"
+ "TSM:%p:%{public}@ abandoning outdated %spending:%{public}@ new:%{public}@"
+ "TSM:%p:%{public}@ already have transition system activity assertion %{public}@"
+ "TSM:%p:%{public}@ cacheFlipbook:YES for %{public}@"
+ "TSM:%p:%{public}@ changed global unrestrictedFramerate:%{BOOL}u targetDisplayMode:%{public}@ previousTarget:%{public}@"
+ "TSM:%p:%{public}@ changed unrestrictedFramerate:%{BOOL}u forEnvironment:%{public}@ but not in presentation"
+ "TSM:%p:%{public}@ changed unrestrictedFramerate:%{BOOL}u forEnvironment:%{public}@ targetDisplayMode:%{public}@ previousTarget:%{public}@"
+ "TSM:%p:%{public}@ claimed flipbook ownership"
+ "TSM:%p:%{public}@ completed ensureFlipbookCurrentOperation %{public}@"
+ "TSM:%p:%{public}@ completed ensureFlipbookCurrentOperation %{public}@, flipbook did update to current with:%{public}@"
+ "TSM:%p:%{public}@ completed pendingEnvironmentUpdate %{public}@"
+ "TSM:%p:%{public}@ completed pendingUpdatePresentation %{public}@"
+ "TSM:%p:%{public}@ completed pendingUpdateToSpecifier %{public}@"
+ "TSM:%p:%{public}@ completed rampOperation:%{public}@ modeMatches:%{BOOL}u lastNotifiedMode:%{public}@"
+ "TSM:%p:%{public}@ completed updateOperation:%{public}@ modeMatches:%{BOOL}u lastNotifiedMode:%{public}@"
+ "TSM:%p:%{public}@ created target:%{public}@"
+ "TSM:%p:%{public}@ createdSession:%p with presentation:%{public}@"
+ "TSM:%p:%{public}@ destroy session:%p with current presentation:%{public}@"
+ "TSM:%p:%{public}@ didAmendSceneSettings: visualState isFlipbook but displayMode is %{public}@ — stripping flipbook, environment:%{public}@ visualState:%{public}@"
+ "TSM:%p:%{public}@ didBeginUpdateToState:%{public}@ matchesPendingEvent:%{BOOL}u pendingEvent:%{public}@ events:%{public}@"
+ "TSM:%p:%{public}@ didUpdateFlipbookVisualState:%{BOOL}u specifier:%{public}@ matchesPending:%{BOOL}u pending:%{public}@"
+ "TSM:%p:%{public}@ didUpdateToMode:%{public}@ fromMode:%{public}@ matchesUpdate:%{BOOL}u matchesRamp:%{BOOL}u matchesTargetDisplayMode:%{BOOL}u shouldNotify:%{BOOL}u update:%{public}@ events:%{public}@"
+ "TSM:%p:%{public}@ didUpdateToPresentation:%{public}@ matchesPendingUpdate:%{BOOL}u targetDisplayMode:%{public}@ pending:%{public}@"
+ "TSM:%p:%{public}@ didUpdateToSpecifier:%{public}@ matchesPendingUpdate:%{BOOL}u pending:%{public}@"
+ "TSM:%p:%{public}@ dropping flipbook ownership ->%{public}@"
+ "TSM:%p:%{public}@ dropping transition system activity assertion %{public}@"
+ "TSM:%p:%{public}@ environmentStateMachine didCompleteUpdateToState:%{public}@ matchesPendingEvent:%{BOOL}u pendingEvent:%{public}@ "
+ "TSM:%p:%{public}@ flipbook already owned, will use live while waiting for ownership"
+ "TSM:%p:%{public}@ flipbook now owned – targetDisplayMode:%{public}@ previousTarget:%{public}@"
+ "TSM:%p:%{public}@ flipbookIsStale=NO ensureCurrent completed"
+ "TSM:%p:%{public}@ flipbookIsStale=YES env:%{public}@ invalidateContentForReason:%{public}@"
+ "TSM:%p:%{public}@ got operation: %{public}@"
+ "TSM:%p:%{public}@ hostDidSetAlwaysOnEnabled:%{BOOL}u forEnvironment:%{public}@ targetDisplayMode:%{public}@ previousTarget:%{public}@"
+ "TSM:%p:%{public}@ hostDidSetLiveUpdating:%{BOOL}u forEnvironment:%{public}@ but not in presentation"
+ "TSM:%p:%{public}@ hostDidSetLiveUpdating:%{BOOL}u forEnvironment:%{public}@ targetDisplayMode:%{public}@ previousTarget:%{public}@"
+ "TSM:%p:%{public}@ new cacheFlipbook:%{BOOL}u"
+ "TSM:%p:%{public}@ new globalCacheFlipbook:%{BOOL}u"
+ "TSM:%p:%{public}@ nil target presentation, will adopt from current state — target:%{public}@ current:%{public}@"
+ "TSM:%p:%{public}@ no operation - currentDisplayMode:%{public}@ shouldStartLiveEngine:%{BOOL}u shouldEndSession:%{BOOL}u finalTriggerEvent:%{public}@ session:%{public}@ cacheFlipbook:%{BOOL}u flipbookIsStale:%{BOOL}u"
+ "TSM:%p:%{public}@ not performing brightness ramp with duration:%.2lfs using operation:%{public}@ because display operation has changed to operation:%{public}@"
+ "TSM:%p:%{public}@ nothing do here since rampOperation has already started:%{public}@"
+ "TSM:%p:%{public}@ onScreenSpecifierForDisplayMode:%{public}@ will use current:%{public}@"
+ "TSM:%p:%{public}@ operation has none type: %{public}@"
+ "TSM:%p:%{public}@ performing brightness ramp with duration:%.2lfs using operation:%{public}@"
+ "TSM:%p:%{public}@ postponing display operation (waiting for system activity acquisition) : %{public}@ safeToUnblank:%{BOOL}u"
+ "TSM:%p:%{public}@ set pending:%{public}@"
+ "TSM:%p:%{public}@ setFlipbookDisabled:%{BOOL}u targetDisplayMode:%{public}@ previousTarget:%{public}@"
+ "TSM:%p:%{public}@ specifier environment:%{public}@ not in presentation:%{public}@ or target:%{public}@"
+ "TSM:%p:%{public}@ started ensureFlipbookCurrent operation %{public}@"
+ "TSM:%p:%{public}@ started environmentUpdate %{public}@ for presentation %{public}@"
+ "TSM:%p:%{public}@ started flipbookVisualState %{public}@"
+ "TSM:%p:%{public}@ started rampOperation %{public}@"
+ "TSM:%p:%{public}@ started setPresentation withTargetState:%{public}@ operation %{public}@"
+ "TSM:%p:%{public}@ started updateDisplayMode pendingOperation %{public}@"
+ "TSM:%p:%{public}@ started updateDisplayMode rampOperation %{public}@"
+ "TSM:%p:%{public}@ started updateToSpecifier operation %{public}@"
+ "TSM:%p:%{public}@ transition system activity assertion callback elapsed:%.4lfs details:%{public}@ error:%{public}@"
+ "TSM:%p:%{public}@ updateToPresentation (redundant) displayMode:%{public}@ previousTarget:%{public}@"
+ "TSM:%p:%{public}@ updateToPresentation by adding:%{public}@ and removing:%{public}@ displayMode:%{public}@ previousTarget:%{public}@"
+ "TSM:%p:%{public}@ updateToPresentation by adding:%{public}@ displayMode:%{public}@ previousTarget:%{public}@"
+ "TSM:%p:%{public}@ updateToPresentation by removing:%{public}@ displayMode:%{public}@ previousTarget:%{public}@"
+ "TSM:%p:%{public}@ updated presentation on invalid session:%{public}@ currentSession:%{public}@ new presentation:%{public}@"
+ "TSM:%p:%{public}@ waiting for composite operation to complete: %{public}@"
+ "TSM:%p:%{public}@ waiting for display ramp operation: %{public}@"
+ "TSM:%p:%{public}@ waiting for operation to complete: %{public}@"
+ "TSM:%p:%{public}@ waiting for prewarmed event:%p toState:%{public}@"
+ "TSM:%p:%{public}@ waiting for prewarmed event:%p toState:%{public}@ {\n%{public}@\n}"
+ "TSM:%p:%{public}@ waiting to perform brightness ramp with duration:%.2lfs using operation:%{public}@"
+ "TSM:%p:%{public}@ will amend scene %{public}@ for backlightState:%{public}@ with visualState:%{public}@ – willBeForeground:%{BOOL}u containsEnv:%{BOOL}u presentation:%{public}@ oldVisualState:%{public}@ oldPresentationDate:%{public}@ settingsVisualState:%{public}@ settingsPresentationDate:%{public}@"
+ "TSM:%p:%{public}@ will not amend scene %{public}@ for backlightState:%{public}@ with settingsVisualState:%{public}@ willBeForeground:%{BOOL}u containsEnv:%{BOOL}u presentation:%{public}@ oldVisualState:%{public}@"
+ "TSM:%p:%{public}@ will resume (if needed) and wait for display operation to complete: %{public}@"
+ "TSM:%p:%{public}@ would have (but will not) amend scene %{public}@ for backlightState:%{public}@ with visualState:%{public}@ – willBeForeground:%{BOOL}u containsEnv:%{BOOL}u presentation:%{public}@ oldVisualState:%{public}@ oldPresentationDate:%{public}@ settingsVisualState:%{public}@ settingsPresentationDate:%{public}@"
+ "TSM:%p:%{public}@: operation is nil (activeEvents:%{public}@). pendEnvUpd=%@, pendPres=%@, pendUpdateToSpec=%@, pendDisplayMode=%@, queued=%@"
+ "Tc"
+ "Tried to begin <CSLBalancedCATransaction %p> off the main thread"
+ "Tried to commit <CSLBalancedCATransaction %p> off the main thread"
+ "Unexpected sub-operation type %ld"
+ "WakeTelemetry ending backlight:%{public}@ source:%{public}@ duration:%llus explanation:%{public}@"
+ "[%d] WakeTelemetry checkCompleteForEvent shouldComplete:%{BOOL}u pending:%{BOOL}u invalidated:%{BOOL}u didTimeout:%{BOOL}u didMeasure:%{BOOL}u measureDisabled:%{BOOL}u didCompleteUpdate:%{BOOL}u didAcquireSystemActivity:%{BOOL}u hadExistingSystemActivity:%{BOOL}u event:%{public}@"
+ "[%d] WakeTelemetry completeForEvent has zero end time – event:%{public}@"
+ "[%d] WakeTelemetry did measure commit – shouldCapture:%{BOOL}u isValidMeasurement:%{BOOL}u pending:%{BOOL}u invalidated:%{BOOL}u event:%{public}@"
+ "[%d] WakeTelemetry didCompleteUpdate – shouldCapture:%{BOOL}u pending:%{BOOL}u didUnblank:%{BOOL}u didMeasure:%{BOOL}u invalidated:%{BOOL}u events:%{public}@"
+ "[%d] WakeTelemetry didUnblank – shouldCapture:%{BOOL}u pending:%{BOOL}u commitPending:%{BOOL}u didMeasure:%{BOOL}u invalidated:%{BOOL}u event:%{public}@"
+ "[%d] WakeTelemetry incrementPerformEventCounterWithEvent:%d forEvent:%{public}@ previousEvent:%{public}@ triggerEvent:%{public}@"
+ "[%d] WakeTelemetry will CA commit to measure for event:%{public}@"
+ "[%d] WakeTelemetry will begin commit measurement for event:%{public}@"
+ "[%d] WakeTelemetry will log wakeTelemetryEvent:%{public}@ for event:%{public}@"
+ "[%d] WakeTelemetry: more than 4 billion compressions: %{public}@"
+ "[%d] WakeTelemetry: more than 4 billion pageins: %{public}@"
+ "[BLSHBacklightIdleProvider providerForDisplay:%@] should not be called before createProviderforDisplay:withLocalAssertionService:"
+ "[NSThread isMainThread]"
+ "[SystemWakeMetrics:%llu] already gathered telemetry"
+ "[SystemWakeMetrics:%llu] secondsDisplayOff:+%.3f=%.3f"
+ "[SystemWakeMetrics:%llu] secondsDisplayOn:+%.3f=%.3f"
+ "[SystemWakeMetrics:%llu] secondsShowingAOT:+%.3f=%.3f"
+ "[SystemWakeMetrics:%llu] unable to query kernel metrics (%d)"
+ "[SystemWakeMetrics:%llu] wakeCount:%u sleepCount:+%u=%u possibleCount:+%u=%u confirmedPossibleCount:+%u=%u rejectedPossibleCount:+%u=%u expiredPossibleCount:+%u=%u noTimeSetCount:+%u=%u rtcAlarmsCount:+%u=%u softwareRequestCount:+%u=%u totalTime:+%llu=%llu [%u,%u,%u,%u,%u]"
+ "[SystemWakeMetrics:%llu] will log\ndisplayOnCount:%u secondsDisplayOn:%.3f\ndisplayOffCount:%u secondsDisplayOff:%.3f\nenteringAOTCount:%u secondsShowingAOT:%.3f\nchangedSettingsWhileOffCount:%u\nwakeCount:%u\nsleepCount:%u\npossibleCount:%u\nconfirmedPossibleCount:%u\nrejectedPossibleCount:%u\nexpiredPossibleCount:%u\nnoTimeSetCount:%u\nrtcAlarmsCount:%u\nsoftwareRequestCount:%u\ntotalTimeSeconds:%.3f\nsleepOver2mCount:%u\nsleepOver3mCount:%u\nsleepOver4mCount:%u\nsleepOver5mCount:%u\nsleepOver6mCount:%u\ninvalidatedFramesUpTo2mStale:%u\ninvalidatedFramesUpTo3mStale:%u\ninvalidatedFramesUpTo4mStale:%u\ninvalidatedFramesUpTo5mStale:%u\ninvalidatedFramesUpTo6mStale:%u\ndiscardedFramesUpTo2mStale:%u\ndiscardedFramesUpTo3mStale:%u\ndiscardedFramesUpTo4mStale:%u\ndiscardedFramesUpTo5mStale:%u\ndiscardedFramesUpTo6mStale:%u\nrenderedFrameCount:%u\nrenderedPartialMinuteCount:%u renderedPresentationSeconds:%llu\nlayoutSeconds:%.3f\nrenderSeconds:%.3f\n"
+ "[SystemWakeMetrics] %{public}@"
+ "_"
+ "aborted"
+ "abortedEvents"
+ "activeDimmed"
+ "activeOn"
+ "afterFailingToRevertPendingSleep"
+ "afterSleepOfNonZeroDuration"
+ "allEventsWake"
+ "allEventsWakeSeconds"
+ "backlightServices.setCBDisplayMode.%@"
+ "beforeKernelWake"
+ "blackFlash"
+ "caTransaction != nil"
+ "cancelled"
+ "changedSettingsWhileOffCount"
+ "checkEntitlementSourceForRequiredEntitlements returned NO but did not provide an error for process:%d descriptor:%@"
+ "com.apple.BacklightServices.AssertionServiceHostServer"
+ "com.apple.BacklightServices.DiagnosticsServer"
+ "com.apple.BacklightServices.XPCProxyHost"
+ "com.apple.backlight.abortedEvents"
+ "com.apple.backlight.activeDimmed"
+ "com.apple.backlight.activeOn"
+ "com.apple.backlight.flipbook.invalidation"
+ "com.apple.backlight.flipbook.render_session"
+ "com.apple.backlight.flipbook.request_dates"
+ "com.apple.backlight.inactiveOn"
+ "com.apple.backlight.off"
+ "com.apple.backlight.systemWakeMetrics"
+ "com.apple.backlight.wakeTelemetry"
+ "com.apple.backlightservices.TailspinRequest"
+ "commitOnGlass"
+ "completeSeconds"
+ "completedEvents"
+ "completion != nil"
+ "compressions"
+ "compressionsDiff"
+ "confirmedPossibleCount"
+ "context:%@ targetState:%@ count:%lu events:%@"
+ "current != nil"
+ "dealloc triggered commit: %@  (currentState %u)"
+ "did commit %@ (currentState %u)"
+ "didSetLowPowerRendering:%u"
+ "didUnblankToDisplayMode"
+ "didUnblankToDisplayMode: %lu events succeeded, %lu events aborted for state:%{public}@"
+ "didUpdateVisualContents"
+ "didUpdateVisualContents: %lu events succeeded, %lu events aborted for state:%{public}@"
+ "disableCancelAllFramesHangPanic"
+ "disableFlipbookHangPanic"
+ "disableTelemetry"
+ "discardedFramesUpTo2mStale"
+ "discardedFramesUpTo3mStale"
+ "discardedFramesUpTo4mStale"
+ "discardedFramesUpTo5mStale"
+ "discardedFramesUpTo6mStale"
+ "display"
+ "displayIdentifier"
+ "displayOffCount"
+ "displayOnCount"
+ "do not call both setSessionProviderFactory: and setSessionProvider: – %@"
+ "durationSeconds"
+ "enableSubhostingForEnvironment called again on %@ which already has a BLSHLocalHostSceneEnvironmentUpdater"
+ "enableSubhostingForEnvironment:%{public}@ sessionProvider:%p existingUpdater:%p(%{public}@)"
+ "endContinuousSeconds"
+ "endMachTime"
+ "endpoint"
+ "enteringAOTCount"
+ "envOp"
+ "event"
+ "event != nil"
+ "eventType"
+ "eventsCount"
+ "executing panic for flipbook %{public}@ hang: %{public}@"
+ "expiredPossibleCount"
+ "flipbook %{public}@ hang: panic enabled by panicOnAllFlipbookHangs default"
+ "flipbook cancelAllFramesWithError hang: panic disabled by user default"
+ "flipbook hang panic attempt failed:%d"
+ "flipbook setPowerSavingEnabled hang: panic disabled by user default"
+ "flipbook token not owned:%@"
+ "flipbookFirst"
+ "flipbookLayoutProfile"
+ "flipbookOp"
+ "flipbookRenderProfile"
+ "histogram_count1to2Min"
+ "histogram_count2to3Min"
+ "histogram_count3to4Min"
+ "histogram_count4to5Min"
+ "histogram_count5to6Min"
+ "histogram_countLessThan1Min"
+ "histogram_countMoreThan6Min"
+ "histogram_intervalUntilFirstFrame"
+ "histogram_presentationDuration"
+ "histogram_totalCount"
+ "hostCachedState != nil"
+ "inactiveOn"
+ "incorrect usage - system shell should set telemetry delegate on specific backlight host, not use the aggregate one"
+ "invalidatedFramesUpTo2mStale"
+ "invalidatedFramesUpTo3mStale"
+ "invalidatedFramesUpTo4mStale"
+ "invalidatedFramesUpTo5mStale"
+ "invalidatedFramesUpTo6mStale"
+ "isFlipbook"
+ "kern.aotmetrics"
+ "lowPowerRendering"
+ "lowPowerRenderingPresentationTime"
+ "lpr"
+ "lprDisabled"
+ "lprTime"
+ "maximumFlipbookCountOverride"
+ "millisecondsDisplayOff"
+ "millisecondsDisplayOn"
+ "millisecondsShowingAOT"
+ "must return non-nil id<BLSHBacklightEnvironmentSessionProviding>"
+ "nil backlightHostForDisplay:%{public}@"
+ "no event"
+ "noTimeSetCount"
+ "none"
+ "off"
+ "on"
+ "onGlass"
+ "pageIns"
+ "pageinDiff"
+ "panicOnAllFlipbookHangs"
+ "performEvents"
+ "performed"
+ "performing dealloc triggered commit for %llu"
+ "possibleCount"
+ "process"
+ "registering scene %{public}@"
+ "rejectedPossibleCount"
+ "renderedFrameCount"
+ "renderedPartialMinuteCount"
+ "renderedPresentationSeconds"
+ "rtcAlarmsCount"
+ "secondsAfterKernelWake"
+ "sending analytics event %@ with payload %@"
+ "sent %{public}@ wakeReason = %{public}@ wakeDurationSeconds = %lf wasInactiveOn = %{BOOL}u beforeKernelWake = %{BOOL}u"
+ "sessionProviderFactory must be non-nil – %@"
+ "should not call twice: [BLSHBacklightIdleProvider createProviderforDisplay:%@ withLocalAssertionService:%p]"
+ "sleepCount"
+ "sleepOver2mCount"
+ "sleepOver3mCount"
+ "sleepOver4mCount"
+ "sleepOver5mCount"
+ "sleepOver6mCount"
+ "softwareRequestCount"
+ "src"
+ "startContinuousSeconds"
+ "startMachTime"
+ "subhosted environment %@ is a BLSHLocalHostSceneEnvironment — another updater's localHostEnv (%@) leaked into this presentation"
+ "surfaceType"
+ "systemActivityAcquisitionSeconds"
+ "systemActivitySeconds"
+ "systemActivitySkipped"
+ "systemActivitySuccess"
+ "systemActivityTimedOut"
+ "systemWakeTelemetry"
+ "thread"
+ "timestampMS"
+ "toCompleteSeconds"
+ "totalTimeMS"
+ "triggerEvent != event, %{public}@ != %{public}@"
+ "triggering panic for flipbook %{public}@ hang after 5s delay: %{public}@"
+ "unblank"
+ "unregistering scene %{public}@"
+ "updateComplete"
+ "userspaceWakeCount"
+ "v16@?0@\"<BLSHPresentationSetting>\"8"
+ "v16@?0@\"<BLSHResourceOwning>\"8"
+ "v16@?0@\"<BSServiceListenerConnectionConfiguring>\"8"
+ "v16@?0@\"BLSHBacklightWakeTelemetryEvent\"8"
+ "v16@?0@\"BSServiceListenerConnection\"8"
+ "v16@?0@\"BSServiceListenerConnection<BSServiceConnectionContext>\"8"
+ "v20@?0I8d12"
+ "v24@?0@\"<BLSHAssertionAttributeHandler>\"8^B16"
+ "v24@?0@\"BLSHMeasureCommitOnWakeOperation\"8Q16"
+ "v32@?0@\"BLSBacklightChangeEvent\"8Q16^B24"
+ "v32@?0@\"NSString\"8@16^B24"
+ "wake"
+ "wakeReason"
+ "wakeSeconds"
+ "wallclockMS"
+ "wasInactiveOn"
+ "will begin %@ (currentState %u)"
+ "\xf0!"
+ "\xf0Q"
+ "\xf0\x91"
+ "\xf0\xf0\xa1"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf1%"
- "\nra"
- "#16@0:8"
- "%p (localHostEnv) updateToVisualState: calling performBacklightSceneUpdate: on delegate for %{public}@ %{public}@ with %{public}@"
- "%p did activate diagnostics peer:%{public}@"
- "%p did activate peer:%{public}@"
- "%p did config"
- "%p did config diagnostics server"
- "%p did configure diagnostics connection:%{public}@"
- "%p updates(%d) (exceeded budget - will coaelsce) specifier:%{public}@ nextSpecifier:%{public}@ valid:(%{public}@->%{public}@) gapDuration:%1.3lg env:%{public}@"
- "%p updates(%d) (exceeded budget - will not coaelsce) specifier:%{public}@ nextSpecifier:%{public}@ valid:(%{public}@->%{public}@) gapDuration:%1.3lg env:%{public}@"
- "%p updates(%d) (will coaelsce) specifier:%{public}@ nextSpecifier:%{public}@ valid:(%{public}@->%{public}@) gapDuration:%1.3lg env:%{public}@"
- "%p updates(%d) (will not coaelsce) validSpecifier:%{public}@ specifier:%{public}@ nextSpecifier:%{public}@ valid:(%{public}@->%{public}@) gapDuration:%1.3lg env:%{public}@"
- "%p:%{public}@ (%{public}@) did complete %srequest dates operation:%{public}@, interval:%{public}@ specifiers:%{public}@"
- "%p:%{public}@ (%{public}@) updated %srequest dates operation:%{public}@, interval:%{public}@ specifiers:%{public}@"
- "%p:%{public}@ (live) hostEnvironment:%{public}@ hostDidSetUnrestrictedFramerateUpdates:%{BOOL}u"
- "%p:%{public}@ (nil next update) timer already scheduled but %lfs is more than %lfs in the future, will reschedule for %{public}@"
- "%p:%{public}@ (nil next update) timer already scheduled in %lfs will not reschedule"
- "%p:%{public}@ (nil next update) timer already scheduled in %lfs will replace with waking timer"
- "%p:%{public}@ (nil next update) will use 30 seconds from now, nextsUpdateStart:%{public}@"
- "%p:%{public}@ (suppressed — skipped filling flipbook) sleepActionState:%{public}@ fillState:%{public}@ onStandby:%{BOOL}u"
- "%p:%{public}@ (waiting for flipbook) sleepActionState:%{public}@ fillState:%{public}@ onStandby:%{BOOL}u"
- "%p:%{public}@ did create engine with:%{public}@ telemetryDelegate:%{public}@"
- "%p:%{public}@ did create render session for flipbook memoryUsage:%{public}@(aprox:%{public}@)/%{public}@ updates:%{public}@"
- "%p:%{public}@ did timeout render dates operation:%{public}@ pendingEnvironments:%{public}@"
- "%p:%{public}@ ending render session:%p for reason:%{public}@ sleepActionState:%{public}@ fillState:%{public}@ stby:%{BOOL}u sup:%{BOOL}u memoryUsage:%{public}@/%{public}@ %{public}@"
- "%p:%{public}@ engine starting live from flipbook, will live update to:%{public}@"
- "%p:%{public}@ flipbook full, will not render more frames memoryUsage:%{public}@/%{public}@ count:%u nextsUpdateStart:%{public}@ updatesCount:%u"
- "%p:%{public}@ invalidated content will not invalidate flipbook (not in presentation) for source:%{public}@ reason:%{public}@ environment:%{public}@"
- "%p:%{public}@ live flipbook will not render frames, have scheduled timer:%{public}@"
- "%p:%{public}@ next update(%{public}@) %lfs from now(%{public}@), will set timer"
- "%p:%{public}@ no more updates, will not render more frames"
- "%p:%{public}@ not requesting dates for interval:%{public}@ (no missingIntervals)"
- "%p:%{public}@ now:%{public}@ is%s in updates:%{public}@"
- "%p:%{public}@ perform systemSleepAction sleepActionState=%{public}@ fillState:%{public}@ onStandby:%{BOOL}u suppressed:%{BOOL}u"
- "%p:%{public}@ performing live updates for specifier:%{public}@"
- "%p:%{public}@ received updates:%{public}@"
- "%p:%{public}@ request dates timeout will now render frames, waited %.3lfs for operation:%{public}@"
- "%p:%{public}@ requesting dates for interval:%{public}@ missingIntervals:%{public}@"
- "%p:%{public}@ requesting updates activeCount:%u lastRenderedFrame:%{public}@"
- "%p:%{public}@ scheduling timer for %{public}@ nextsUpdateStart:%{public}@"
- "%p:%{public}@ scheduling waking timer %{public}@ is too soon, using %lf seconds from now:%{public}@ nextsUpdateStart:%{public}@"
- "%p:%{public}@ scheduling waking timer for %{public}@ nextsUpdateStart:%{public}@"
- "%p:%{public}@ sleep immenient - do no more work"
- "%p:%{public}@ suppressed - do no more work"
- "%p:%{public}@ timer already scheduled in %lfs will not schedule a new timer for %{public}@"
- "%p:%{public}@ timer too soon (will just dispatch_async) for %{public}@ nextsUpdateStart:%{public}@"
- "%p:%{public}@ update1HzFromPresentation new1HzFlipbook:%{BOOL}u old1HzFlipbook:%{BOOL}u environment:%{public}@ presentation::%{public}@"
- "%p:%{public}@ wait for AP wake before completing notify current"
- "%p:%{public}@ waiting for last session render frame:%{public}@"
- "%p:%{public}@ will complete sleep action for reason:%{public}@ subReason:%{public}@ sleepActionState=%{public}@ fillState:%{public}@ onStandby:%{BOOL}u suppressed:%{BOOL}u"
- "%p:%{public}@ will ignore invalidate flipbook (rendering live) for source:%{public}@ reason:%{public}@ environment:%{public}@"
- "%p:%{public}@ will not render frames, empty presentation session:%{public}@"
- "%p:%{public}@ will not render frames, waiting for backoff time:%{public}@ timer:%{public}@"
- "%p:%{public}@ will not render more frames, waiting to begin previous render:%{public}@"
- "%p:%{public}@ will notify current, sleeping but have %.2lfs worth of flipbook frames"
- "%p:%{public}@ will render frame:%{public}@"
- "%p:%{public}@ will render frames, waiting (enough) %.3lfs for operation:%{public}@ timer:%{public}@"
- "%p:%{public}@ will use 30 seconds from now, nextsUpdateStart:%{public}@"
- "%p:%{public}@->%{public}@ %{public}@ sleepActionState=%{public}@ fillState:%{public}@->Awake onStandby:%{BOOL}u suppressed:%{BOOL}u changed:%{BOOL}u shouldNotifyFlipbookCurrent:%{BOOL}u shouldServiceTimer:%{BOOL}u"
- "%p:%{public}@->%{public}@ did change flipbook render type sleepActionState:%{public}@ fillState:%{public}@ onStandby:%{BOOL}u"
- "%p:%{public}@->Stopped engine %s (%{public}@) %s:%{public}@"
- ".cxx_destruct"
- "@"
- "@\"<BLSAssertionService>\""
- "@\"<BLSAssertionServiceResponding>\""
- "@\"<BLSAssertionServiceResponding>\"16@0:8"
- "@\"<BLSBacklightProxy>\""
- "@\"<BLSBacklightSceneEnvironment>\""
- "@\"<BLSBacklightSceneEnvironment_Private>\""
- "@\"<BLSCADisplayPowerAssertion>\""
- "@\"<BLSCADisplayPowerAssertion>\"24@0:8q16"
- "@\"<BLSDisplayPowerResourceHint>\""
- "@\"<BLSDisplayPowerResourceHint>\"24@0:8Q16"
- "@\"<BLSDisplayStateDelegate>\""
- "@\"<BLSDisplayStateDelegate>\"16@0:8"
- "@\"<BLSFlipbookDiagnosticsProviding>\""
- "@\"<BLSHAlwaysFillFlipbookProvider>\""
- "@\"<BLSHAlwaysOnPresentationEngineDelegate>\""
- "@\"<BLSHAssertionAttributeHandlerService>\""
- "@\"<BLSHAssertionAttributeHandlerService>\"16@0:8"
- "@\"<BLSHBacklightDisplayStateMachineDelegate>\""
- "@\"<BLSHBacklightEnvironmentSessionProviding>\""
- "@\"<BLSHBacklightEnvironmentSessionProviding>\"16@0:8"
- "@\"<BLSHBacklightEnvironmentStateMachineDelegate>\""
- "@\"<BLSHBacklightHostObservable><BLSBacklightChangeRequestable>\""
- "@\"<BLSHBacklightHostObserving>\""
- "@\"<BLSHBacklightHostObserving>\"16@0:8"
- "@\"<BLSHBacklightHostTelemetryDelegate>\""
- "@\"<BLSHBacklightHostTelemetryDelegate>\"16@0:8"
- "@\"<BLSHBacklightIdleProviderDelegate>\""
- "@\"<BLSHBacklightInactiveEnvironmentSessionUpdating>\""
- "@\"<BLSHBacklightOSInterfaceProviding>\""
- "@\"<BLSHBacklightPlatformProvider>\""
- "@\"<BLSHBacklightPlatformProvider>\"16@0:8"
- "@\"<BLSHBacklightSceneHostEnvironment>\""
- "@\"<BLSHBacklightSceneHostEnvironment>\"32@0:8@\"<BLSHSceneEnvironmentObserving>\"16@\"<NSObject><NSCopying>\"24"
- "@\"<BLSHBacklightSceneHostEnvironmentObserver>\""
- "@\"<BLSHBacklightStateMachineEventPerforming>\""
- "@\"<BLSHDisableAlwaysOnProvider>\""
- "@\"<BLSHDisableCommitOnWakeMeasurementProvider>\""
- "@\"<BLSHDisableFlipbookProvider>\""
- "@\"<BLSHEngineRenderFlipbookSessionDelegate>\""
- "@\"<BLSHEngineRequestDatesOperationDelegate>\""
- "@\"<BLSHEnvironmentTransitionStateDelegate>\""
- "@\"<BLSHFlipbook>\""
- "@\"<BLSHFlipbook>\"16@0:8"
- "@\"<BLSHFlipbookPowerSavingProviding>\""
- "@\"<BLSHFlipbookTelemetry>\""
- "@\"<BLSHFlipbookTelemetry>\"16@0:8"
- "@\"<BLSHGlobal1HzFlipbookProvider>\""
- "@\"<BLSHGlobalCacheFlipbookOnDisplayWakeProvider>\""
- "@\"<BLSHGlobalHighLuminanceAlwaysOnProvider>\""
- "@\"<BLSHGlobalUnrestrictedFramerateProvider>\""
- "@\"<BLSHInactiveBudgetPolicing>\""
- "@\"<BLSHInactiveBudgetPolicing_Private>\""
- "@\"<BLSHInactiveBudgetPolicing_Private>\"16@0:8"
- "@\"<BLSHIndividualSystemActivityAssertionAggregator>\""
- "@\"<BLSHOSInterfaceProviding>\""
- "@\"<BLSHOSInterfaceProviding>\"16@0:8"
- "@\"<BLSHOSTimerProviding>\""
- "@\"<BLSHOSTimerProviding>\"16@0:8"
- "@\"<BLSHOnSystemSleepActionDelegate>\""
- "@\"<BLSHPreventSystemSleepAsserting>\""
- "@\"<BLSHPreventSystemSleepAsserting>\"24@0:8@\"NSString\"16"
- "@\"<BLSHPseudoFlipbookProvider>\""
- "@\"<BLSHRenderedFlipbookFrame>\""
- "@\"<BLSHRenderedFlipbookFrame>\"16@0:8"
- "@\"<BLSHRenderedFlipbookFrame>\"24@0:8^@16"
- "@\"<BLSHSceneEnvironmentObserving>\""
- "@\"<BLSHServicePlatformProvider>\""
- "@\"<BLSHSystemActivityAsserting>\""
- "@\"<BLSHSystemActivityAsserting>\"32@0:8@\"NSString\"16@?<v@?@\"<SWSystemActivityAssertionConfiguring>\">24"
- "@\"<BLSHSystemSleepMonitoring>\""
- "@\"<BLSHSystemSleepMonitoring>\"16@0:8"
- "@\"<BLSHTransparentFlipbookProvider>\""
- "@\"<BLSHUserIdleProviding>\""
- "@\"<BLSHUserIdleProvidingDelegate>\""
- "@\"<BLSHUserIdleProvidingDelegate>\"16@0:8"
- "@\"<BLSHWatchdogAbortContext>\""
- "@\"<BLSHWatchdogAbortContext>\"24@0:8@\"<BLSHWatchdogTiming>\"16"
- "@\"<BLSHWatchdogDelegate>\""
- "@\"<BLSHWatchdogInvalidatable>\""
- "@\"<BLSHWatchdogInvalidatable>\"40@0:8@\"<BLSHWatchdogDelegate>\"16@\"NSString\"24d32"
- "@\"<BLSHWatchdogProviderDelegate>\""
- "@\"<BLSPresentationDateSpecifying>\"16@0:8"
- "@\"<BLSXPCAssertionServiceClientInterface>\""
- "@\"<BLSXPCBacklightProxyClientInterface>\""
- "@\"<BSInvalidatable>\""
- "@\"<BSInvalidatable>\"32@0:8@\"NSString\"16@?<v@?>24"
- "@\"<BSTimerScheduleQuerying><BSCancellable><BSInvalidatable>\""
- "@\"<BSTimerScheduleQuerying><BSCancellable><BSInvalidatable>\"48@0:8@\"NSString\"16d24d32@?<v@?@\"<BSTimerScheduleQuerying><BSCancellable><BSInvalidatable>\">40"
- "@\"<BSTimerScheduleQuerying><BSInvalidatable>\""
- "@\"<NSObject><NSCopying>\""
- "@\"<SWSystemActivityAcquisitionDetails>\""
- "@\"AWAttentionAwarenessClient\""
- "@\"AWAttentionAwarenessConfiguration\""
- "@\"BLSAlwaysOnDateSpecifier\""
- "@\"BLSAlwaysOnDateSpecifier\"16@0:8"
- "@\"BLSAlwaysOnDateSpecifier\"40@0:8@\"BLSAlwaysOnDateSpecifier\"16@\"BLSAlwaysOnDateSpecifier\"24@\"<BLSHBacklightSceneHostEnvironment>\"32"
- "@\"BLSAlwaysOnDateSpecifier\"40@0:8@\"BLSAlwaysOnDateSpecifier\"16@\"BLSAlwaysOnDateSpecifier\"24q32"
- "@\"BLSAssertion\""
- "@\"BLSAssertionDescriptor\""
- "@\"BLSAssertionDescriptor\"16@0:8"
- "@\"BLSAssertionIdentifier\""
- "@\"BLSAssertionIdentifier\"16@0:8"
- "@\"BLSAssertionIdentifier\"32@0:8@\"BLSAssertionDescriptor\"16o^@24"
- "@\"BLSAttribute\""
- "@\"BLSAttribute\"16@0:8"
- "@\"BLSBacklight\""
- "@\"BLSBacklightChangeEvent\""
- "@\"BLSBacklightSceneUpdate\""
- "@\"BLSBacklightSceneVisualState\""
- "@\"BLSBacklightSceneVisualState\"16@0:8"
- "@\"BLSDiagnosticFlipbookFrame\""
- "@\"BLSDiagnosticFlipbookFrame\"16@0:8"
- "@\"BLSDiagnosticFlipbookFrame\"24@0:8@\"NSUUID\"16"
- "@\"BLSDurationAttribute\""
- "@\"BLSHAggregateProcessAssertion\""
- "@\"BLSHAggregateSystemActivityAssertion\""
- "@\"BLSHAggregatedProcessAssertion\""
- "@\"BLSHAggregatedSystemActivityAssertionFactory\""
- "@\"BLSHAlwaysOnPresentationEngine\""
- "@\"BLSHAssertionService\""
- "@\"BLSHBacklightAggregateState\""
- "@\"BLSHBacklightDisplayStateMachine\""
- "@\"BLSHBacklightEnvironmentPresentation\""
- "@\"BLSHBacklightEnvironmentPresentation\"16@0:8"
- "@\"BLSHBacklightEnvironmentStateMachine\""
- "@\"BLSHBacklightIdleProvider\""
- "@\"BLSHBacklightInactiveEnvironmentSession\""
- "@\"BLSHBacklightInactiveEnvironmentSession\"16@0:8"
- "@\"BLSHBacklightMutableTargetState\""
- "@\"BLSHBacklightOSInterfaceProvider\""
- "@\"BLSHBacklightSceneClientSettingsDiffInspector\""
- "@\"BLSHBacklightService\""
- "@\"BLSHBacklightStateMachine\""
- "@\"BLSHBacklightTransitionStateMachine\""
- "@\"BLSHCriticalAssertProvider\""
- "@\"BLSHCriticalAssertTester\""
- "@\"BLSHDateSpecifierModel\""
- "@\"BLSHDefaultsObserver\""
- "@\"BLSHDiagnosticsServer\""
- "@\"BLSHDurationCalculator\""
- "@\"BLSHEngineEnvironmentObserverHelper\""
- "@\"BLSHEngineRenderFlipbookSession\""
- "@\"BLSHEngineRequestDatesOperation\""
- "@\"BLSHEnsureFlipbookCurrentOperation\""
- "@\"BLSHEnvironmentDatesModel\""
- "@\"BLSHEnvironmentTransitionStateTarget\""
- "@\"BLSHFlipbookContext\""
- "@\"BLSHFlipbookFramesHistogram\""
- "@\"BLSHFlipbookHistory\""
- "@\"BLSHFlipbookPowerSavingProvider\""
- "@\"BLSHFlipbookSpecification\""
- "@\"BLSHFlipbookSpecification\"16@0:8"
- "@\"BLSHFlipbookWatchdog\""
- "@\"BLSHInactiveBudgetBucketEntryCount\""
- "@\"BLSHInactiveProcessMinutesBudget\""
- "@\"BLSHInactiveProcessSecondsBudget\""
- "@\"BLSHInternalTapToRadarDialog\""
- "@\"BLSHLocalAssertionService\""
- "@\"BLSHLocalCountingAssertionAttributeHandler\""
- "@\"BLSHNullInactiveProcessBudget\""
- "@\"BLSHOnSystemSleepAction\""
- "@\"BLSHPendingBacklightRamp\""
- "@\"BLSHPendingEnvironmentUpdateOperation\""
- "@\"BLSHPendingTwoPhaseUpdateDisplayMode\""
- "@\"BLSHPendingUpdateDisplayMode\""
- "@\"BLSHPendingUpdatePresentation\""
- "@\"BLSHPendingUpdateToSpecifier\""
- "@\"BLSHPresentationDateSpecifier\""
- "@\"BLSHPresentationDateSpecifier\"16@0:8"
- "@\"BLSHPresentationUpdates\""
- "@\"BLSHService\""
- "@\"BLSHSuppressionEvent\""
- "@\"BLSHSuppressionEvent\"16@0:8"
- "@\"BLSHTTRWatchdog\""
- "@\"BLSHTTRWatchdogConfiguration\""
- "@\"BLSHTapToRadarDescriptor\""
- "@\"BLSHWatchdogAbortParameters\""
- "@\"BLSHWatchdogProvider\""
- "@\"BLSHWatchdogTester\""
- "@\"BLSHXPCAssertionServiceHostServer\""
- "@\"BLSHXPCBacklightProxyHostServer\""
- "@\"BLSPauseWhenSceneBackgroundAttribute\""
- "@\"BLSSetPresentationOperation\""
- "@\"BLSXPCBacklightProxyObserverMask\""
- "@\"BSAbsoluteMachTimer\""
- "@\"BSContinuousMachTimer\""
- "@\"BSProcessHandle\""
- "@\"BSServiceConnectionListener\""
- "@\"CAContext\""
- "@\"CADisplayStateControl\""
- "@\"CAFlipBook\""
- "@\"CBDisplayStateClient\""
- "@\"CMSuppressionManager\""
- "@\"FBScene\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSArray<__BLSDiagnosticFlipbookFrame__>\"16@0:8"
- "@\"NSDate\""
- "@\"NSDate\"16@0:8"
- "@\"NSDate\"24@0:8d16"
- "@\"NSDateInterval\""
- "@\"NSEnumerator\""
- "@\"NSError\"24@0:8@\"BLSBacklightChangeRequest\"16"
- "@\"NSHashTable\""
- "@\"NSMapTable\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSNumber\"16@0:8"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_queue>\"16@0:8"
- "@\"NSObject<OS_dispatch_workloop>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSSet\""
- "@\"NSSet\"32@0:8@\"FBScene\"16@\"NSSet\"24"
- "@\"NSSet\"32@0:8@\"NSSet\"16@\"FBScene\"24"
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUUID\"16@0:8"
- "@\"NSUserDefaults\""
- "@\"RBSAssertion\""
- "@\"RBSProcessIdentity\""
- "@\"RBSProcessIdentity\"16@0:8"
- "@\"RBSProcessMonitor\""
- "@\"SWSystemSleepMonitorAggregateState\""
- "@120@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8Q16"
- "@24@0:8^@16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8d16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16B24B28"
- "@32@0:8@16Q24"
- "@32@0:8@16o^@24"
- "@32@0:8Q16Q24"
- "@32@0:8d16d24"
- "@32@0:8q16@24"
- "@32@0:8q16q24"
- "@36@0:8B16@20@28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24d32"
- "@40@0:8@16@24q32"
- "@40@0:8@16@?24@?32"
- "@40@0:8@16d24@32"
- "@40@0:8@16q24@32"
- "@40@0:8@16q24Q32"
- "@40@0:8Q16@24@32"
- "@40@0:8Q16Q24Q32"
- "@40@0:8d16@24d32"
- "@40@0:8q16q24@32"
- "@40@0:8q16q24q32"
- "@44@0:8@16@24B32@36"
- "@44@0:8d16d24d32f40"
- "@48@0:8@\"BLSAttribute\"16@\"<BLSAssertionServiceResponding>\"24@\"<BLSHAssertionAttributeHandlerService>\"32@\"<BLSHAssertionAttributeHandler>\"40"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16d24d32@?40"
- "@48@0:8@16q24@32@40"
- "@48@0:8Q16Q24@32Q40"
- "@52@0:8@16@24@32@40B48"
- "@56@0:8@16@24@32@40@48"
- "@56@0:8@16@24B32@36B44@48"
- "@56@0:8@16q24@32@40@48"
- "@64@0:8@16q24@32@40@48@56"
- "@64@0:8Q16d24d32d40d48d56"
- "@64@0:8Q16q24@32@40@48@56"
- "@64@0:8Q16q24@32@?40@48@56"
- "@64@0:8d16@24@32B40B44@48@56"
- "@72@0:8Q16q24d32d40d48d56d64"
- "@72@0:8d16@24d32d40d48d56B64I68"
- "@72@0:8q16q24q32q40q48B56@60B68"
- "@80@0:8Q16q24q32q40q48B56B60B64B68B72f76"
- "@88@0:8@16@24d32d40d48q56@64@72@?80"
- "@88@0:8Q16q24d32d40d48d56d64Q72d80"
- "@88@0:8d16@24@32@40d48d56d64d72B80I84"
- "@?"
- "B"
- "B16@0:8"
- "B20@0:8B16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSDate\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B24@0:8d16"
- "B24@0:8q16"
- "B32@0:8@\"<BLSHBacklightSceneHostEnvironment>\"16@\"FBSMutableSceneSettings\"24"
- "B32@0:8@16@24"
- "B32@0:8@16B24B28"
- "B32@0:8@16o^@24"
- "B32@0:8q16q24"
- "BLSAsserting"
- "BLSAssertionService"
- "BLSAssertionServiceResponding"
- "BLSBacklightChangeRequestable"
- "BLSBacklightProxy"
- "BLSBacklightSceneEnvironmentUpdating"
- "BLSBacklightStateObservable"
- "BLSBacklightStateObserving"
- "BLSDiagnosticsXPCHostInterface"
- "BLSDisplayPowerResourceHint"
- "BLSDisplayStateDelegate"
- "BLSEnvironmentDateSpecifying"
- "BLSFlipbookDiagnosticsProviding"
- "BLSH1HzFlipbookAttributeHandler"
- "BLSHAggregatedProcessAssertion"
- "BLSHAggregatedSystemActivityAssertionFactory"
- "BLSHAlwaysFillFlipbookAttributeHandler"
- "BLSHAlwaysFillFlipbookProvider"
- "BLSHAlwaysOnPresentationEngineDelegate"
- "BLSHAssertionAttributeHandler"
- "BLSHAssertionAttributeHandlerService"
- "BLSHAssertionAttributeTimer"
- "BLSHAssertionPausingSceneObserver"
- "BLSHAssertionProxy"
- "BLSHAssertionService"
- "BLSHAsyncDisplayPowerResourceHint"
- "BLSHBacklightAggregateState"
- "BLSHBacklightDisplayStateMachineAbortContext"
- "BLSHBacklightDisplayStateMachineDelegate"
- "BLSHBacklightEnvironmentPresentation"
- "BLSHBacklightEnvironmentSessionProviding"
- "BLSHBacklightEnvironmentStateMachineAbortPayload"
- "BLSHBacklightEnvironmentStateMachineDelegate"
- "BLSHBacklightFBSceneEnvironmentActionHandler"
- "BLSHBacklightFBSceneHostEnvironment"
- "BLSHBacklightHost"
- "BLSHBacklightHostObservable"
- "BLSHBacklightHostObserving"
- "BLSHBacklightHostObserving.m"
- "BLSHBacklightHostTelemetry"
- "BLSHBacklightHostTelemetrySource"
- "BLSHBacklightIdleProvider"
- "BLSHBacklightInactiveEnvironmentSession"
- "BLSHBacklightInactiveEnvironmentSessionObserving"
- "BLSHBacklightInactiveEnvironmentSessionUpdating"
- "BLSHBacklightMutableTargetState"
- "BLSHBacklightOSInterfaceProvider"
- "BLSHBacklightOSInterfaceProviding"
- "BLSHBacklightOSTimerProvider"
- "BLSHBacklightPlatformProvider"
- "BLSHBacklightPlatformProviderObserver"
- "BLSHBacklightSceneClientSettingsDiffInspector"
- "BLSHBacklightSceneEnvironmentHosting"
- "BLSHBacklightSceneHostEnvironment"
- "BLSHBacklightSceneHostEnvironmentObserver"
- "BLSHBacklightSceneHostEnvironment_Private"
- "BLSHBacklightService"
- "BLSHBacklightStateMachine"
- "BLSHBacklightStateMachineEventPerforming"
- "BLSHBacklightTransitionStateMachineAbortContext"
- "BLSHBacklightTransitionStateMachineState"
- "BLSHBaseBacklightEnvironmentSessionProvider"
- "BLSHBasePlatformProvider"
- "BLSHBaseSceneHostEnvironment"
- "BLSHBegunUpdateOperation"
- "BLSHCacheFlipbookOnDisplayWakeAttributeHandler"
- "BLSHCancelWhenBacklightInactivatesAttributeEntry"
- "BLSHCompletedUpdateOperation"
- "BLSHCountingAssertionAttributeEntry"
- "BLSHCriticalAssertDidFailDetails"
- "BLSHCriticalAssertProvider"
- "BLSHCriticalAssertTester"
- "BLSHDateSpecifierModel"
- "BLSHDateSpecifierModelObserving"
- "BLSHDefaultHandler"
- "BLSHDefaultsObserver"
- "BLSHDiagnosticsHostPeer"
- "BLSHDiagnosticsServer"
- "BLSHDisableAlwaysOnAttributeHandler"
- "BLSHDisableAlwaysOnProvider"
- "BLSHDisableBacklightWatchdogsAttributeHandler"
- "BLSHDisableCommitOnWakeMeasurementAttributeHandler"
- "BLSHDisableFlipbookAttributeHandler"
- "BLSHDisableFlipbookPowerSavingAttribute"
- "BLSHDisableFlipbookPowerSavingAttributeHandler"
- "BLSHDisableFlipbookProvider"
- "BLSHDurationAttributeHandler"
- "BLSHDurationCalculator"
- "BLSHEngineEnvironmentObserverHelper"
- "BLSHEngineRenderFlipbookSessionDelegate"
- "BLSHEngineRequestDatesOperation"
- "BLSHEngineRequestDatesOperationDelegate"
- "BLSHEnsureFlipbookCurrentOperation"
- "BLSHEnvironmentAndSource"
- "BLSHEnvironmentDateInterval"
- "BLSHEnvironmentDateSpecifier"
- "BLSHEnvironmentDatesEnumerator"
- "BLSHEnvironmentDatesModel"
- "BLSHEnvironmentOperation"
- "BLSHEnvironmentPerformEventData"
- "BLSHEnvironmentTransitionState"
- "BLSHEnvironmentTransitionStateDelegate"
- "BLSHEnvironmentTransitionStateTarget"
- "BLSHEnvironmentUpdateData"
- "BLSHFlipbook"
- "BLSHFlipbookContext"
- "BLSHFlipbookFramesHistogram"
- "BLSHFlipbookHistory"
- "BLSHFlipbookHistoryFrame"
- "BLSHFlipbookInvalidationTelemetryData"
- "BLSHFlipbookPowerSavingProvider"
- "BLSHFlipbookPowerSavingProviding"
- "BLSHFlipbookRenderSessionTelemetryData"
- "BLSHFlipbookRequestDatesTelemetryData"
- "BLSHFlipbookSpecification"
- "BLSHFlipbookWatchdog"
- "BLSHForceActiveAttributeEntry"
- "BLSHForceActiveAttributeHandler"
- "BLSHGenericSceneDelegateWithActionHandlers"
- "BLSHGlobal1HzFlipbookAttributeHandler"
- "BLSHGlobal1HzFlipbookProvider"
- "BLSHGlobalCacheFlipbookOnDisplayWakeAttributeHandler"
- "BLSHGlobalCacheFlipbookOnDisplayWakeProvider"
- "BLSHGlobalHighLuminanceAlwaysOnAttributeHandler"
- "BLSHGlobalHighLuminanceAlwaysOnProvider"
- "BLSHGlobalUnrestrictedFramerateAttributeHandler"
- "BLSHGlobalUnrestrictedFramerateProvider"
- "BLSHHighLuminanceAlwaysOnAttributeHandler"
- "BLSHHostEnvironmentAmendSceneSettingsDelegate"
- "BLSHInactiveBudgetBucket"
- "BLSHInactiveBudgetBucketEntryCount"
- "BLSHInactiveBudgetPolicing"
- "BLSHInactiveBudgetPolicing_Private"
- "BLSHInactiveBudgetPolicy"
- "BLSHInactiveProcessBudget"
- "BLSHInactiveProcessBudgeting"
- "BLSHInactiveProcessMinutesBudget"
- "BLSHInactiveProcessSecondsBudget"
- "BLSHIndividualSystemActivityAssertion"
- "BLSHIndividualSystemActivityAssertionAggregator"
- "BLSHInternalTapToRadarDialog"
- "BLSHInternalTapToRadarIgnorer"
- "BLSHInternalTapToRadarManager"
- "BLSHInvalidOnSystemSleepAttributeEntry"
- "BLSHInvalidOnSystemSleepAttributeHandler"
- "BLSHInvalidationTimer"
- "BLSHLocalAssertionAttributeHandler"
- "BLSHLocalAssertionAttributeHandlerEntry"
- "BLSHLocalCountingAssertionAttributeHandler"
- "BLSHLocalCountingSceneAssertionAttributeHandler"
- "BLSHLocalHostSceneEnvironment"
- "BLSHLocalHostSceneEnvironmentUpdater"
- "BLSHLocalHostSceneEnvironmentUpdaterTimelinesCalculator"
- "BLSHLocalOnlyServiceConfiguration"
- "BLSHLocalOnlySimplePlatformProvider"
- "BLSHLongHeldAssertion"
- "BLSHNullBacklightSceneHostEnvironment"
- "BLSHNullInactiveBudgetPolicy"
- "BLSHNullInactiveProcessBudget"
- "BLSHOSInterfaceProviderAbortContext"
- "BLSHOSInterfaceProviding"
- "BLSHOSTimerProviding"
- "BLSHOnSystemSleepAction"
- "BLSHOnSystemSleepActionDelegate"
- "BLSHPauseOnSystemSleepAttributeEntry"
- "BLSHPauseOnSystemSleepAttributeHandler"
- "BLSHPauseWhenSceneBackgroundAttributeHandler"
- "BLSHPendingBacklightRamp"
- "BLSHPendingDirectRampDisplayMode"
- "BLSHPendingEnvironmentUpdateOperation"
- "BLSHPendingOperation"
- "BLSHPendingTwoPhaseUpdateDisplayMode"
- "BLSHPendingUpdateDisplayMode"
- "BLSHPendingUpdateDisplayModeConfiguration"
- "BLSHPendingUpdatePresentation"
- "BLSHPendingUpdateToSpecifier"
- "BLSHPresentationDateSpecifier"
- "BLSHPresentationDifference"
- "BLSHPresentationEntry"
- "BLSHPresentationUpdates"
- "BLSHPreventBacklightIdleAttributeHandler"
- "BLSHPseudoFlipbook"
- "BLSHPseudoFlipbookAttributeHandler"
- "BLSHPseudoFlipbookFrame"
- "BLSHPseudoFlipbookProvider"
- "BLSHRenderedFlipbookFrame"
- "BLSHRequestLiveUpdatingAttributeHandler"
- "BLSHRequestUnrestrictedFramerateAttributeHandler"
- "BLSHSceneEnvironmentObserver"
- "BLSHSceneEnvironmentObserverToken"
- "BLSHSceneEnvironmentObserving"
- "BLSHService"
- "BLSHServicePlatformProvider"
- "BLSHSuppressionEvent"
- "BLSHSystemActivityAsserting"
- "BLSHSystemActivityAssertionConfiguration"
- "BLSHSystemActivityAssertionConfiguring"
- "BLSHSystemWakeWaiter"
- "BLSHTTRWatchdog"
- "BLSHTTRWatchdogConfiguration"
- "BLSHTTRWatchdogDetails"
- "BLSHTailspinLogWriter"
- "BLSHTapToRadarDescriptor"
- "BLSHTapToRadarFiler"
- "BLSHTimeoutTimer"
- "BLSHTransparentFlipbookAttributeHandler"
- "BLSHTransparentFlipbookProvider"
- "BLSHUserIdleProvider"
- "BLSHUserIdleProviding"
- "BLSHUserIdleProvidingDelegate"
- "BLSHValidWhenBacklightInactiveAttributeHandler"
- "BLSHWaitOperation"
- "BLSHWaiterForBacklight"
- "BLSHWaiterForBacklightDisplayMode"
- "BLSHWaiterForBacklightState"
- "BLSHWarningTimer"
- "BLSHWatchdogAbortContext"
- "BLSHWatchdogAbortParameters"
- "BLSHWatchdogDelegate"
- "BLSHWatchdogDidFireDetails"
- "BLSHWatchdogInvalidatable"
- "BLSHWatchdogProvider"
- "BLSHWatchdogProviderDelegate"
- "BLSHWatchdogTester"
- "BLSHWatchdogTesterTimer"
- "BLSHWatchdogTiming"
- "BLSHXPCAssertionServiceHost"
- "BLSHXPCAssertionServiceHostServer"
- "BLSHXPCBacklightProxyHost"
- "BLSHXPCBacklightProxyHostServer"
- "BLSPresentationDateSpecifying"
- "BLSRenderedFlipbookFrame"
- "BLSSceneActionHandler"
- "BLSSceneDelegateWithActionHandlers"
- "BLSSetPresentationOperation"
- "BLSValidWhenBacklightInactiveAttributeEntry"
- "BLSXPCAssertionServiceHostInterface"
- "BLSXPCBacklightProxyHostInterface"
- "BSCancellable"
- "BSInvalidatable"
- "BSLHWatchdogTimer"
- "BSM:%p (no longer active) unexpected system sleep - isActive:%{BOOL}u activeOnAPAssertion:%{BOOL}u – will not send request:%{public}@ %{public}@"
- "BSM:%p (no longer requested) unexpected system sleep - hasSleepActionCompletion:%{BOOL}u %{public}@ - will not send request:%{public}@"
- "BSM:%p (no sleep action completion) unexpected system sleep - will not send request:%{public}@ %{public}@"
- "BSM:%p (sleep not requested) unexpected system sleep – will not send request:%{public}@ %{public}@"
- "BSM:%p (will not sleep - %@) unexpected system sleep - will not send request %{public}@"
- "BSM:%p activeOn system activity assertion callback details:%{public}@ event:%{public}@ elapsed:%.4lfs error:%{public}@"
- "BSM:%p activeOn system activity assertion timed out (related to rdar://74802930) event:%{public}@ elapsed:%.4lfs"
- "BSM:%p didChangeAlwaysOnSetting:%{BOOL}u"
- "BSM:%p didCompleteUpdateToState:%{public}@ elapsed:%.4lfs forEvents:%{public}@"
- "BSM:%p performEvent system activity assertion callback details:%{public}@ event:%{public}@ elapsed:%.4lfs error:%{public}@"
- "BSM:%p sendNewChangeRequest explanation:%{public}@ request:%{public}@"
- "BSM:%p setAlwaysOnDisabledByAssertion:%{BOOL}u"
- "BSM:%p startup activeOn system activity assertion callback details:%{public}@ elapsed:%.4lfs error:%{public}@"
- "BSM:%p startup alwaysOnEnabledByPlatform:%{BOOL}u"
- "BSM:%p suppressed but suppression service not active"
- "BSM:%p suppressionEvent explanation:%{public}@ request:%{public}@ event:%{public}@"
- "BSM:%p system sleep while acquiring system activity, did not deactivate backlight"
- "BSM:%p unexpected system sleep - assertion acquired %{public}@ {elapsedTime:%lf timerInterval:%lf} — dispatching request:%{public}@"
- "BSM:%p unexpected system sleep - did deactivate backlight with events:%{public}@"
- "BSM:%p unexpected system sleep - will deactivate backlight with request:%{public}@ %{public}@"
- "BSM:%p unexpected system sleep - will wait %lfs before sending request:%{public}@"
- "BSM:%p will %send suppression service after significant user interaction; activityState:%{public}@"
- "BSM:%p will %send suppression service; activityState:%{public}@ unsuppressedTargetBacklightState:%{public}@"
- "BSM:%p will %sstart suppression service; activityState:%{public}@ unsuppressedTargetBacklightState:%{public}@"
- "BSM:%p will ignore suppressionEvent — arrived after service was deactivated — explanation:%{public}@ event:%{public}@"
- "BSM:%p will performRequest with event:%{public}@"
- "BSServiceConnectionListenerDelegate"
- "BacklightServicesHost"
- "Black"
- "CADisplayStateControl nil - this process needs entitlement: 'com.apple.QuartzCore.display-state'"
- "CBDisplayStateClientDelegate"
- "DSM:%p (completed except CB target:%{public}@) waited %lfs for CB callback to cbDisplayMode:%{public}@->%{public}@"
- "DSM:%p (likely initialization) core animation completed(%{public}@) switch to display state:%{public}@ currentState:%{public}@"
- "DSM:%p (likely initialization) core brightness completed switch to display mode:%{public}@"
- "DSM:%p (no prewarm) will start turning on display"
- "DSM:%p (pending change flipbook state for %{public}@) still waiting to update CA to %@ (waited %lfs)"
- "DSM:%p (pending change flipbook state for %{public}@) waited %lfs for CB callback to cbDisplayMode:%{public}@->%{public}@"
- "DSM:%p already have live rendering system activity assertion %{public}@"
- "DSM:%p core animation completed transition to display state:%{public}@ (currentState:%{public}@) elapsed:%lfs"
- "DSM:%p core animation completed transition to wrong display state:%{public}@ (currentState:%{public}@), waiting for display state:%{public}@ phase:%u elapsed:%lfs"
- "DSM:%p core animation completed(%{public}@) transition to matching display state:%{public}@, (currentState:%{public}@), but operation is not started"
- "DSM:%p core animation reporting interrupted transition to display state:%{public}@, current display state:%{public}@ – pending transition to display state:%{public}@ phase:%u elapsed:%lfs"
- "DSM:%p core animation state transition status:%@ to display state:%{public}@, current display state:%{public}@ – pending transition to display state:%{public}@ phase:%u elapsed:%lfs"
- "DSM:%p core brightness completed switch to display mode:%{public}@"
- "DSM:%p core brightness completed switch to flipbook state:%{public}@"
- "DSM:%p core brightness completed switch to matching display mode:%{public}@, but operation is not started"
- "DSM:%p core brightness completed switch to wrong display mode:%{public}@, waiting for display mode:%{public}@ phase:%u"
- "DSM:%p core brightness completed switch to wrong flipbook state:%{public}@}, waiting for flipbook state:%{public}@"
- "DSM:%p core brightness failed to switch to display mode:%{public}@ error:%{public}@"
- "DSM:%p core brightness failed to switch to flipbook state:%{public}@ error:%{public}@"
- "DSM:%p did not have transition, but lastSteadyStateDisplayMode(%@) != targetDisplayMode(%@)"
- "DSM:%p did not have transition, but watchdog timer is non-nil: %@"
- "DSM:%p didUpdateToMode:%{public}@ seqId:%d but has new transition to:%{public}@ seqId:%d"
- "DSM:%p didUpdateToMode:%{public}@ seqId:%d complete"
- "DSM:%p dropping live rendering system activity assertion %{public}@"
- "DSM:%p flipbook state is transitioning, begin reversing before performing ramp to:%{public}@ cbFlipbookState:%{public}@->%{public}@}"
- "DSM:%p flipbook state is transitioning, completing reversing before performing ramp to:%{public}@ cbFlipbookState:%{public}@->%{public}@"
- "DSM:%p hadTransition=%{BOOL}u mode:%{public}@ isLiveRendering:%{BOOL}u didReleaseLiveRendering:%{BOOL}u seqId:%d"
- "DSM:%p live rendering system activity assertion callback elapsed:%.4lfs details:%{public}@ error:%{public}@"
- "DSM:%p performNextStep supportsFlipbookState:%{BOOL}u isOffOrBlack:%{BOOL}u willUnblank:%{BOOL}u shouldTransitionCBBeforeCA:%{BOOL}u needToTransitionCA:%{BOOL}u hasCBTransition:%{BOOL}u isFlipbookStateTransitioning:%{BOOL}u isTurningOnDisplay:%{BOOL}u didPrewarmDisplayMode:%{BOOL}u isPendingCBDisplayMode:%{BOOL}u"
- "DSM:%p preWarmingToMode:%{public}@ fromMode:%{public}@ (waited %lfs)"
- "DSM:%p prewarmForDisplayMode:%{public}@->%{public}@%s previousPrewarm:%{public}@ hasAssertion:%{BOOL}u isPrewarmOn:%{BOOL}u requiresModeChange:%{BOOL}u shouldSignalPowerOn:%{BOOL}u shouldCleanup:%{BOOL}u cbDisplayMode:%{public}@"
- "DSM:%p ramp to displayMode:%{public}@ withDuration:%fs fullDuration:%fs shouldWaitForCompletion:%{BOOL}u"
- "DSM:%p replacing pending ramp to displayMode:%{public}@ withDuration:%fs fullDuration:%fs started at %{public}@ with ramp to displayMode:%{public}@ withDuration:%fs shouldWaitForCompletion:%{BOOL}u"
- "DSM:%p replacing pending switch to caDisplayState:%{public}@ from %lfs ago with switch to caDisplayState:%{public}@"
- "DSM:%p replacing pending switch to flipbookState:%{public}@ from %lfs ago with switch to flipbookState:%{public}@"
- "DSM:%p resumed display mode:%{public}@ did not match current target:%{public}@"
- "DSM:%p resumed transition to display mode:%{public}@"
- "DSM:%p reversing pending ramp to displayMode:%{public}@ withDuration:%fs fullDuration:%fs started at %{public}@ (%fs elapsed — %f%%) with ramp to displayMode:%{public}@ withDuration:%fs fullDuration:%fs shouldWaitForCompletion:%{BOOL}u"
- "DSM:%p setDisplayMode:%{public}@ duration:%lf seqId:%d"
- "DSM:%p setDisplayMode:%{public}@ duration:%lf seqId:%d interrupting previous setDisplayMode:%{public}@ duration:%lf seqId:%d with started at:%{public}@%{public}@"
- "DSM:%p transition to displayMode:%@ duration:%lf seqId:%d interrupting previous setDisplayMode:%@ duration:%lf seqId:%d with started at:%@"
- "DSM:%p waited %lfs for CB callback to cbDisplayMode:%{public}@->%{public}@"
- "DSM:%p waited %lfs for CB callback to cbFlipbookState:%{public}@->%{public}@"
- "DSM:%p waiting to update CA to %@ (waited %lfs)"
- "ETS:%p:%{public}@ will update to target:%{public}@ wasUpdating:%{BOOL}u animated:%{BOOL}u hasBacklightRamp:%{BOOL}u event:%{public}@ touchTarget:%{BOOL}u"
- "FBSceneDelegate"
- "FBSceneObserver"
- "I16@0:8"
- "I24@0:8@16"
- "NSCopying"
- "NSObject"
- "OSIP: setCATransitionsDelayForTesting:%.02fs"
- "OSIP: setCBTransitionsDelayForTesting:%.02fs"
- "OSIP:%p %sBacklightFactor:%f WithFadeDuration:%fs"
- "OSIP:%p (platformProvider) useAlwaysOnBrightnessCurve:%{BOOL}u withDuration:%fs"
- "OSIP:%p completed(%d) setFlipbookTransparent:%{BOOL}u"
- "OSIP:%p completion(%{public}@->%{public}@) transitionToDisplayState:%{public}@"
- "OSIP:%p could not switchToFlipbookState:%{public}@ error:%{public}@"
- "OSIP:%p could not transitionToDisplayMode:%{public}@ during init error:%{public}@"
- "OSIP:%p could not transitionToDisplayMode:%{public}@ error:%{public}@"
- "OSIP:%p delayCompletionsForTesting:YES, completing delayed CATransitionToDisplayState:%{public}@"
- "OSIP:%p delayCompletionsForTesting:YES, completing delayed didCompleteCBTransitionToDisplayMode"
- "OSIP:%p delayCompletionsForTesting:YES, delaying CATransitionToDisplayState:%{public}@ completion by %.2fs"
- "OSIP:%p delayCompletionsForTesting:YES, delaying didCompleteCBTransitionToDisplayMode by %.2fs"
- "OSIP:%p disableSuppression set to YES - use 'login -f mobile defaults delete com.apple.BacklightServices disableSuppression' to remove"
- "OSIP:%p flipbook no longer transparent, will transition to real flipbook"
- "OSIP:%p flipbook set transparent, will transition to active"
- "OSIP:%p flipbook transparent, will transition to CADisplayStateOn not CADisplayStateFlipBook"
- "OSIP:%p got didCompleteSwitchToFlipbookState:%{public}@ error:%@"
- "OSIP:%p got didCompleteTransitionToDisplayMode:%{public}@ error:%@"
- "OSIP:%p initWithPlatformProvider: transitionToDisplayMode:%@ withDuration:0"
- "OSIP:%p startup cbDisplayMode:%{public}@ dsao:%{BOOL}u dsaof:%{BOOL}u dscs:%{BOOL}u sup:%{BOOL}u"
- "OSIP:%p suppression event error - event:%{public}@ error:%{public}@ reason:%{public}@"
- "OSIP:%p switchToFlipbookState:%@"
- "OSIP:%p transitionToCADisplayState:%@"
- "OSIP:%p transitionToDisplayMode:%@ withDuration:%fs"
- "OSIP:%p transitionToDisplayMode:%{public}@ withDuration:%fs"
- "OSIP:%p unsupported call to switchToFlipbookState:%{public}@"
- "Q16@0:8"
- "Q24@0:8@16"
- "SWSystemSleepObserver"
- "Subclass"
- "T#,R"
- "T@\"<BLSAssertionServiceResponding>\",R,W,N"
- "T@\"<BLSAssertionServiceResponding>\",R,W,N,V_assertion"
- "T@\"<BLSDisplayStateDelegate>\",&,SsetDisplayStateDelegate:"
- "T@\"<BLSDisplayStateDelegate>\",&,SsetDisplayStateDelegate:,V_displayStateDelegate"
- "T@\"<BLSHAssertionAttributeHandlerService>\",R,W,N"
- "T@\"<BLSHAssertionAttributeHandlerService>\",R,W,N,V_service"
- "T@\"<BLSHBacklightDisplayStateMachineDelegate>\",R,W,N,V_delegate"
- "T@\"<BLSHBacklightEnvironmentSessionProviding>\",&,N"
- "T@\"<BLSHBacklightEnvironmentSessionProviding>\",R,N"
- "T@\"<BLSHBacklightEnvironmentStateMachineDelegate>\",R,W,N,V_lock_delegate"
- "T@\"<BLSHBacklightHostObserving>\",W,N"
- "T@\"<BLSHBacklightHostTelemetryDelegate>\",W"
- "T@\"<BLSHBacklightHostTelemetryDelegate>\",W,V_telemetryDelegate"
- "T@\"<BLSHBacklightIdleProviderDelegate>\",W,N,V_delegate"
- "T@\"<BLSHBacklightInactiveEnvironmentSessionUpdating>\",&,N"
- "T@\"<BLSHBacklightPlatformProvider>\",R,N"
- "T@\"<BLSHBacklightPlatformProvider>\",R,N,V_platformProvider"
- "T@\"<BLSHBacklightSceneHostEnvironment>\",R,N,V_environment"
- "T@\"<BLSHBacklightSceneHostEnvironment>\",R,W,N,V_environment"
- "T@\"<BLSHBacklightStateMachineEventPerforming>\",R,N,V_eventPerformer"
- "T@\"<BLSHFlipbook>\",W,N"
- "T@\"<BLSHFlipbookTelemetry>\",?,R,N"
- "T@\"<BLSHInactiveBudgetPolicing>\",R,N,V_inactiveBudgetPolicy"
- "T@\"<BLSHInactiveBudgetPolicing_Private>\",R,N"
- "T@\"<BLSHInactiveBudgetPolicing_Private>\",R,N,V_inactiveBudgetPolicy"
- "T@\"<BLSHOSInterfaceProviding>\",R,N"
- "T@\"<BLSHOSInterfaceProviding>\",R,N,V_osInterfaceProvider"
- "T@\"<BLSHOSInterfaceProviding>\",W,N,SsetOSInterfaceProvider:,V_osInterfaceProvider"
- "T@\"<BLSHOSTimerProviding>\",R,N"
- "T@\"<BLSHOSTimerProviding>\",R,N,V_osTimerProvider"
- "T@\"<BLSHRenderedFlipbookFrame>\",R,N"
- "T@\"<BLSHRenderedFlipbookFrame>\",R,W,N,V_hostFrame"
- "T@\"<BLSHServicePlatformProvider>\",R,N,V_platformProvider"
- "T@\"<BLSHUserIdleProvidingDelegate>\",W,N"
- "T@\"<BLSHUserIdleProvidingDelegate>\",W,N,V_delegate"
- "T@\"<BLSHWatchdogAbortContext>\",&,N,V_abortContext"
- "T@\"<BLSHWatchdogDelegate>\",W,N,V_delegate"
- "T@\"<BLSPresentationDateSpecifying>\",R,N"
- "T@\"<BLSXPCAssertionServiceClientInterface>\",R,N,V_remoteTarget"
- "T@\"AWAttentionAwarenessClient\",&,N,V_attentionAwarenessClient"
- "T@\"AWAttentionAwarenessConfiguration\",&,N,V_attentionAwarenessConfiguration"
- "T@\"BLSAlwaysOnDateSpecifier\",&,N,V_specifier"
- "T@\"BLSAlwaysOnDateSpecifier\",R,N"
- "T@\"BLSAlwaysOnDateSpecifier\",R,N,V_dateSpecifier"
- "T@\"BLSAssertionDescriptor\",R,N"
- "T@\"BLSAssertionDescriptor\",R,N,V_descriptor"
- "T@\"BLSAssertionIdentifier\",&,N"
- "T@\"BLSAssertionIdentifier\",&,N,V_identifier"
- "T@\"BLSAttribute\",R,W,N"
- "T@\"BLSAttribute\",R,W,N,V_attribute"
- "T@\"BLSBacklightChangeEvent\",R"
- "T@\"BLSBacklightChangeEvent\",R,N,V_activeTransitionEvent"
- "T@\"BLSBacklightChangeEvent\",R,N,V_triggerEvent"
- "T@\"BLSBacklightSceneVisualState\",R"
- "T@\"BLSBacklightSceneVisualState\",R,N,V_visualState"
- "T@\"BLSBacklightSceneVisualState\",R,V_lock_visualState"
- "T@\"BLSDurationAttribute\",R,W,N,V_attribute"
- "T@\"BLSHBacklightDisplayStateMachine\",R,N,V_displayStateMachine"
- "T@\"BLSHBacklightEnvironmentPresentation\",&,N,V_presentation"
- "T@\"BLSHBacklightEnvironmentPresentation\",&,V_presentation"
- "T@\"BLSHBacklightEnvironmentPresentation\",R"
- "T@\"BLSHBacklightEnvironmentPresentation\",R,N"
- "T@\"BLSHBacklightEnvironmentPresentation\",R,N,V_presentation"
- "T@\"BLSHBacklightEnvironmentPresentation\",R,V_presentation"
- "T@\"BLSHBacklightEnvironmentStateMachine\",&,V_presentationSource"
- "T@\"BLSHBacklightFBSceneHostEnvironment\",R"
- "T@\"BLSHBacklightIdleProvider\",R,W,N,V_provider"
- "T@\"BLSHBacklightInactiveEnvironmentSession\",&,N"
- "T@\"BLSHBacklightInactiveEnvironmentSession\",R,N"
- "T@\"BLSHBacklightOSInterfaceProvider\",&"
- "T@\"BLSHDateSpecifierModel\",&,N"
- "T@\"BLSHEnvironmentDateSpecifier\",R,N"
- "T@\"BLSHEnvironmentDatesModel\",R,N,V_sourceModel"
- "T@\"BLSHFlipbookContext\",R,N,V_flipbookContext"
- "T@\"BLSHFlipbookFramesHistogram\",R,N,V_invalidatedFramesHistogram"
- "T@\"BLSHFlipbookFramesHistogram\",R,N,V_sessionFramesHistogram"
- "T@\"BLSHFlipbookSpecification\",?,R,N"
- "T@\"BLSHFlipbookSpecification\",N"
- "T@\"BLSHInactiveBudgetBucketEntryCount\",R,N,V_entryCount"
- "T@\"BLSHInactiveBudgetBucketEntryCount\",R,N,V_invalidatedEntryCount"
- "T@\"BLSHInactiveBudgetBucketEntryCount\",R,N,V_renderedEntryCount"
- "T@\"BLSHLocalAssertionService\",R,N"
- "T@\"BLSHLocalAssertionService\",R,N,V_localAssertionService"
- "T@\"BLSHLocalAssertionService\",R,W,N,V_service"
- "T@\"BLSHPendingBacklightRamp\",R,N,V_pendingBacklightRamp"
- "T@\"BLSHPendingDirectRampDisplayMode\",R,W"
- "T@\"BLSHPendingTwoPhaseUpdateDisplayMode\",&,V_next"
- "T@\"BLSHPendingTwoPhaseUpdateDisplayMode\",W,V_previous"
- "T@\"BLSHPendingUpdateDisplayMode\",&,V_abandonedInProgressOperation"
- "T@\"BLSHPendingUpdateDisplayMode\",&,V_pendingOperation"
- "T@\"BLSHPendingUpdateDisplayMode\",R,W"
- "T@\"BLSHPresentationDateSpecifier\",R,N"
- "T@\"BLSHPresentationDateSpecifier\",R,N,V_bls_specifier"
- "T@\"BLSHPresentationDateSpecifier\",R,V_initialSpecifier"
- "T@\"BLSHPresentationDateSpecifier\",R,V_specifier"
- "T@\"BLSHSuppressionEvent\",R,N"
- "T@\"BLSHTapToRadarDescriptor\",R,N,V_descriptor"
- "T@\"BLSPauseWhenSceneBackgroundAttribute\",R,W,N,V_attribute"
- "T@\"CAContext\",R,N"
- "T@\"CAContext\",R,N,V_caContext"
- "T@\"NSArray\",C,N,V_attachments"
- "T@\"NSArray\",C,N,V_keywordIDs"
- "T@\"NSArray\",R,C,N"
- "T@\"NSArray\",R,C,N,V_presentationEntries"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,N,V_additions"
- "T@\"NSArray\",R,N,V_environmentIdentifiers"
- "T@\"NSArray\",R,N,V_insertions"
- "T@\"NSArray\",R,N,V_memoryUsageHistogram"
- "T@\"NSArray\",R,N,V_presentationTimeHistogram"
- "T@\"NSArray\",R,N,V_removals"
- "T@\"NSArray\",R,N,V_specifiers"
- "T@\"NSArray\",R,V_events"
- "T@\"NSDate\",&,N,V_date"
- "T@\"NSDate\",&,V_timeOfIssue"
- "T@\"NSDate\",C,N,V_timeOfIssue"
- "T@\"NSDate\",R"
- "T@\"NSDate\",R,C,N,V_expirationDate"
- "T@\"NSDate\",R,N"
- "T@\"NSDate\",R,N,V_lastEntryFinalDate"
- "T@\"NSDate\",R,N,V_lastEntryInitialDate"
- "T@\"NSDate\",R,N,V_minuteBoundaryDate"
- "T@\"NSDate\",R,N,V_nextUpdatesStart"
- "T@\"NSDate\",R,N,V_presentationDate"
- "T@\"NSDate\",R,N,V_previousPresentationDate"
- "T@\"NSDate\",R,N,V_startDate"
- "T@\"NSDate\",R,V_lock_presentationDate"
- "T@\"NSDateInterval\",R,N"
- "T@\"NSDateInterval\",R,N,V_dateInterval"
- "T@\"NSDateInterval\",R,N,V_presentationInterval"
- "T@\"NSDateInterval\",R,N,V_requestInterval"
- "T@\"NSEnumerator\",R,N,V_enumerator"
- "T@\"NSMutableDictionary\",&,N,V_attentionLostTimeoutDictionary"
- "T@\"NSObject<OS_dispatch_queue>\",R,N"
- "T@\"NSSet\",R,C,N"
- "T@\"NSSet\",R,N,V_environmentsSet"
- "T@\"NSString\",&"
- "T@\"NSString\",&,V_displayReason"
- "T@\"NSString\",&,V_identifier"
- "T@\"NSString\",&,V_radarDescription"
- "T@\"NSString\",&,V_radarTitle"
- "T@\"NSString\",&,V_timerIdentifier"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_abortReasonString"
- "T@\"NSString\",C,N,V_buildVersion"
- "T@\"NSString\",C,N,V_bundleID"
- "T@\"NSString\",C,N,V_componentName"
- "T@\"NSString\",C,N,V_componentVersion"
- "T@\"NSString\",C,N,V_device"
- "T@\"NSString\",C,N,V_explanation"
- "T@\"NSString\",C,N,V_processName"
- "T@\"NSString\",C,N,V_ttrDisplayReason"
- "T@\"NSString\",C,N,V_ttrPromptHeader"
- "T@\"NSString\",C,N,V_ttrPromptMessage"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_environmentIdentifier"
- "T@\"NSString\",R,C,N,V_explanation"
- "T@\"NSString\",R,C,N,V_identifier"
- "T@\"NSString\",R,C,V_identifier"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_radarDescription"
- "T@\"NSString\",R,N,V_radarTitle"
- "T@\"NSString\",R,N,V_reason"
- "T@\"NSString\",R,N,V_reasonEnded"
- "T@\"NSString\",R,N,V_source"
- "T@\"NSUUID\",R,N"
- "T@\"RBSProcessIdentity\",R"
- "T@\"RBSProcessIdentity\",R,C,N,V_processIdentity"
- "T@\"SWSystemSleepMonitorAggregateState\",&,N,V_sleepMonitorAggregateState"
- "T@,&,N,V_userObject"
- "T@,R,N"
- "T@,R,N,V_environmentSource"
- "TB"
- "TB,?"
- "TB,?,Gis1HzFlipbookForAssertion,Sset1HzFlipbookForAssertion:"
- "TB,?,Gis1HzFlipbookForAssertion,Sset1HzFlipbookForAssertion:,V_lock_1HzFlipbook"
- "TB,?,GisHighLuminanceAlwaysOn"
- "TB,?,GisHighLuminanceAlwaysOn,V_lock_highLuminanceAlwaysOn"
- "TB,?,R,Gis1HzFlipbook"
- "TB,?,R,GisLocal"
- "TB,?,R,N"
- "TB,?,R,N,GisAlwaysOnEnabled"
- "TB,?,R,N,GisTesting"
- "TB,?,R,N,GisUsingAlwaysOnBrightnessCurve"
- "TB,?,V_lock_cacheFlipbookOnDisplayWake"
- "TB,GdidUpdateInitialState,V_updatedInitialState"
- "TB,GhasUnrestrictedFramerateUpdates"
- "TB,GhasUnrestrictedFramerateUpdates,V_lock_unrestrictedFramerateUpdates"
- "TB,GisAlwaysOnEnabledForEnvironment"
- "TB,GisAlwaysOnEnabledForEnvironment,V_lock_alwaysOnEnabledForEnvironment"
- "TB,GisCompleted"
- "TB,GisCompleted,V_completed"
- "TB,GisLiveUpdating"
- "TB,GisLiveUpdating,V_lock_liveUpdating"
- "TB,GisReadyToStart,V_readyToStart"
- "TB,GisStarted"
- "TB,GisStarted,V_started"
- "TB,GisWatchdogEnabled,V_watchdogEnabled"
- "TB,N"
- "TB,N,GhasSleepBeenImminentSinceScheduled"
- "TB,N,GhasSleepBeenImminentSinceScheduled,V_sleepImminentSinceScheduled"
- "TB,N,Gis1HzFlipbook,Sset1HzFlipbook:"
- "TB,N,GisActive"
- "TB,N,GisAlwaysOnDisabledByAssertion"
- "TB,N,GisAlwaysOnSettingEnabled"
- "TB,N,GisAlwaysOnSuppressed"
- "TB,N,GisFlipbookDisabled"
- "TB,N,GisFlipbookTransparent"
- "TB,N,GisGlobal1HzFlipbook"
- "TB,N,GisGlobalHighLuminanceAlwaysOn"
- "TB,N,GisGlobalUnrestrictedFramerate"
- "TB,N,GisHighLuminanceAlwaysOn"
- "TB,N,GisOnStandby"
- "TB,N,GisPowerSavingEnabled"
- "TB,N,GisUsingPseudoFlipbook"
- "TB,N,V_acquireWaitsToAbortSleepImminent"
- "TB,N,V_acquireWaitsToAbortSleepRequested"
- "TB,N,V_debugLogsEnabled"
- "TB,N,V_isPotentialHang"
- "TB,N,V_radarIsUserInitiated"
- "TB,N,V_shouldNotifyOfUnidle"
- "TB,N,V_shouldNotifyOfUnidleChanged"
- "TB,N,V_sleepImminentSinceScheduled"
- "TB,N,V_suppressionSupported"
- "TB,N,V_userInitiated"
- "TB,R"
- "TB,R,GhasUnrestrictedFramerateUpdates"
- "TB,R,GisClientActive"
- "TB,R,GisFullyCompleted"
- "TB,R,GisHighLuminanceAlwaysOn"
- "TB,R,GisLiveUpdating"
- "TB,R,GisStartedButIncomplete"
- "TB,R,N"
- "TB,R,N,GhasBeenRendered,V_rendered"
- "TB,R,N,GhasSleepBeenImminentSinceScheduled"
- "TB,R,N,GhasUserActivityOccured"
- "TB,R,N,GisAcquired"
- "TB,R,N,GisActive"
- "TB,R,N,GisAlwaysOnEnabled"
- "TB,R,N,GisAnimating"
- "TB,R,N,GisComplete"
- "TB,R,N,GisCompleted"
- "TB,R,N,GisFlipbookPowerSavingEnabled"
- "TB,R,N,GisIdle"
- "TB,R,N,GisInvalidated"
- "TB,R,N,GisInverted"
- "TB,R,N,GisInverted,V_inverted"
- "TB,R,N,GisRetainingSurface"
- "TB,R,N,GisSecondsFidelity"
- "TB,R,N,GisSecondsFidelity,V_secondsFidelity"
- "TB,R,N,GisShowingBlankingWindow"
- "TB,R,N,GisSuppressed"
- "TB,R,N,GisSuppressionServiceActive"
- "TB,R,N,GisTransitioning"
- "TB,R,N,GisTransitioningDisplayMode"
- "TB,R,N,GisUpdatingInitialState"
- "TB,R,N,GisUpdatingPresentation"
- "TB,R,N,GisUpdatingState"
- "TB,R,N,GisUpdatingVisualState"
- "TB,R,N,GisUsingPseudoFlipbook"
- "TB,R,N,GwantsSuppression"
- "TB,R,N,GwasSleepImminentWhenScheduled,V_sleepImminentWhenScheduled"
- "TB,R,N,V_containsInvalidation"
- "TB,R,N,V_didClearDateSpecifiers"
- "TB,R,N,V_didFailToRender"
- "TB,R,N,V_didReset"
- "TB,R,N,V_hasChanges"
- "TB,R,N,V_hasEnsureFlipbookCurrent"
- "TB,R,N,V_shouldReset"
- "TB,R,N,V_wantsTransform"
- "TB,R,N,V_wasReset"
- "TB,V_didCompleteAnimation"
- "TB,V_didUpdateInitialState"
- "TB,V_enabledByDefault"
- "TB,V_hangDetected"
- "TB,V_invalidated"
- "TB,V_isAnimatedTransition"
- "TB,V_isNullOperationAllowed"
- "TB,V_shouldFaultOnFailureToAcquire"
- "TB,V_showTTRAlert"
- "TI,?,R,N"
- "TI,R,N"
- "TI,R,N,V_payloadSize"
- "TI,R,N,V_timedOutEnvironmentCount"
- "TQ,N,V_abortTimestamp"
- "TQ,N,V_failureSource"
- "TQ,R"
- "TQ,R,N"
- "TQ,R,N,V_abortReason"
- "TQ,R,N,V_averageMemoryUsage"
- "TQ,R,N,V_designation"
- "TQ,R,N,V_flipbookDiagnosticHistoryFrameLimit"
- "TQ,R,N,V_flipbookDiagnosticHistoryMemoryLimit"
- "TQ,R,N,V_frameId"
- "TQ,R,N,V_machContinuousTimestamp"
- "TQ,R,N,V_medianMemoryUsage"
- "TQ,R,N,V_memoryUsage"
- "TQ,R,N,V_pendingTransitionStateCount"
- "TQ,R,N,V_presentationTime"
- "TQ,R,N,V_reason"
- "TQ,R,N,V_sequenceID"
- "TQ,R,N,V_softMemoryLimit"
- "TQ,R,N,V_startedTime"
- "TQ,R,N,V_timeStamp"
- "TQ,R,N,V_timedOutCount"
- "TQ,R,N,V_totalCount"
- "TQ,R,N,V_type"
- "TSM:%p %{public}@will performEvent(%llu:%p) %{public}@->%{public}@ %{public}@:%{public}@ %{public}@->%{public}@ %{public}@%{public}@%{public}@\n%{public}@%{public}@"
- "TSM:%p (findNextOperation) [_pendingUpdatePresentation isCompleted] so setting to nil: %{public}@"
- "TSM:%p (findNextOperation) abandoning ensureFlipbookCurrentOperation %{public}@ because targetDisplayMode=%{public}@"
- "TSM:%p (findNextOperation) animating:%{BOOL}u forcedUnanimated:%{BOOL}u pending:%{public}@"
- "TSM:%p (findNextOperation) did not stop presentation engine:%{public}@ (displayMode:%{public}@)"
- "TSM:%p (findNextOperation) no environmentPerformUpdate operation needed isBeforeDisplayBlankingChange:%{BOOL}u (queuedEvents:%{public}@})"
- "TSM:%p (findNextOperation) no updateDisplayMode operation needed"
- "TSM:%p (findNextOperation) no updatePresentation operation needed — target:%{public}@ current:%{public}@"
- "TSM:%p (findNextOperation) no updateSpecifier needed"
- "TSM:%p (findNextOperation) ok to proceed (not to off) and updated to initial state animating:%{BOOL}u forcedUnanimated:%{BOOL}u  pending:%{public}@"
- "TSM:%p (findNextOperation) pending presentation update while determining display update, animating:%{BOOL}u forcedUnanimated:%{BOOL}u pending:%{public}@"
- "TSM:%p (findNextOperation) pending:%{public}@"
- "TSM:%p (findNextOperation) replaced pending events:%{public}@ with new events:%{public}@"
- "TSM:%p (findNextOperation) returning existing updatePresentation operation: %{public}@"
- "TSM:%p (findNextOperation) started pendingEnvironmentUpdate %{public}@, will skip environment update for -> FlipbookSuppressed events:%{public}@"
- "TSM:%p (findNextOperation) still pending:%{public}@"
- "TSM:%p (findNextOperation) will discard specifier from presentation engine end:%{public}@ (no events, currentBacklightState:%u)"
- "TSM:%p (findNextOperation) will discard specifier from presentation engine end:%{public}@ (not needed for events:%{public}@)"
- "TSM:%p (findNextOperation) will start ensure flipbook current operation %{public}@"
- "TSM:%p (findNextOperation) will start ensure flipbook current operation %{public}@ and defer %{public}@"
- "TSM:%p (findNextOperation) will start:%{public}@"
- "TSM:%p (findNextOperation) will start:%{public}@ animating:%{BOOL}u forcedUnanimated:%{BOOL}u "
- "TSM:%p (findNextOperation) will update to specifier:%{public}@ prior to display mode:%{public}@->%{public}@"
- "TSM:%p (performNextStepInTransition) abandoning ensureFlipbookCurrentOperation %{public}@ because it's obsolete when completing transition"
- "TSM:%p (performNextStepInTransition) abandoning pendingEnvironmentUpdate %{public}@ because it's obsolete when completing transition"
- "TSM:%p (stopPresentationEngine) abandoning ensureFlipbookCurrentOperation %{public}@ because it's obsolete; displayMode=%{public}@"
- "TSM:%p abandoning outdated %spending:%{public}@ new:%{public}@"
- "TSM:%p already have transition system activity assertion %{public}@"
- "TSM:%p cacheFlipbook:YES for %{public}@"
- "TSM:%p changed global unrestrictedFramerate:%{BOOL}u targetDisplayMode:%{public}@ previousTarget:%{public}@"
- "TSM:%p changed unrestrictedFramerate:%{BOOL}u forEnvironment:%{public}@ but not in presentation"
- "TSM:%p changed unrestrictedFramerate:%{BOOL}u forEnvironment:%{public}@ targetDisplayMode:%{public}@ previousTarget:%{public}@"
- "TSM:%p completed ensureFlipbookCurrentOperation %{public}@"
- "TSM:%p completed ensureFlipbookCurrentOperation %{public}@, flipbook did update to current with:%{public}@"
- "TSM:%p completed pendingEnvironmentUpdate %{public}@"
- "TSM:%p completed pendingUpdatePresentation %{public}@"
- "TSM:%p completed pendingUpdateToSpecifier %{public}@"
- "TSM:%p completed rampOperation:%{public}@ modeMatches:%{BOOL}u lastNotifiedMode:%{public}@"
- "TSM:%p completed updateOperation:%{public}@ modeMatches:%{BOOL}u lastNotifiedMode:%{public}@"
- "TSM:%p created target:%{public}@"
- "TSM:%p createdSession:%p with presentation:%{public}@"
- "TSM:%p destroy session:%p with current presentation:%{public}@"
- "TSM:%p didBeginUpdateToState:%{public}@ matchesPendingEvent:%{BOOL}u pendingEvent:%{public}@ events:%{public}@"
- "TSM:%p didUpdateToMode:%{public}@ fromMode:%{public}@ matchesUpdate:%{BOOL}u matchesRamp:%{BOOL}u matchesTargetDisplayMode:%{BOOL}u shouldNotify:%{BOOL}u update:%{public}@ events:%{public}@"
- "TSM:%p didUpdateToPresentation:%{public}@ matchesPendingUpdate:%{BOOL}u targetDisplayMode:%{public}@ pending:%{public}@"
- "TSM:%p didUpdateToSpecifier:%{public}@ matchesPendingUpdate:%{BOOL}u pending:%{public}@"
- "TSM:%p dropping transition system activity assertion %{public}@"
- "TSM:%p environmentStateMachine didCompleteUpdateToState:%{public}@ matchesPendingEvent:%{BOOL}u pendingEvent:%{public}@ "
- "TSM:%p flipbookIsStale=NO ensureCurrent completed"
- "TSM:%p flipbookIsStale=YES env:%{public}@ invalidateContentForReason:%{public}@"
- "TSM:%p got operation: %{public}@"
- "TSM:%p hostDidSetAlwaysOnEnabled:%{BOOL}u forEnvironment:%{public}@ targetDisplayMode:%{public}@ previousTarget:%{public}@"
- "TSM:%p hostDidSetLiveUpdating:%{BOOL}u forEnvironment:%{public}@ but not in presentation"
- "TSM:%p hostDidSetLiveUpdating:%{BOOL}u forEnvironment:%{public}@ targetDisplayMode:%{public}@ previousTarget:%{public}@"
- "TSM:%p new cacheFlipbook:%{BOOL}u"
- "TSM:%p new globalCacheFlipbook:%{BOOL}u"
- "TSM:%p nil target presentation, will adopt from current state — target:%{public}@ current:%{public}@"
- "TSM:%p no operation - currentDisplayMode:%{public}@ shouldStartLiveEngine:%{BOOL}u shouldEndSession:%{BOOL}u finalTriggerEvent:%{public}@ session:%{public}@ cacheFlipbook:%{BOOL}u flipbookIsStale:%{BOOL}u"
- "TSM:%p not performing brightness ramp with duration:%.2lfs using operation:%{public}@ because display operation has changed to operation:%{public}@"
- "TSM:%p nothing do here since rampOperation has already started:%{public}@"
- "TSM:%p onScreenSpecifierForDisplayMode:%{public}@ will use current:%{public}@"
- "TSM:%p operation has none type: %{public}@"
- "TSM:%p performing brightness ramp with duration:%.2lfs using operation:%{public}@"
- "TSM:%p postponing display operation (waiting for system activity acquisition) : %{public}@ safeToUnblank:%{BOOL}u"
- "TSM:%p set pending:%{public}@"
- "TSM:%p setFlipbookDisabled:%{BOOL}u targetDisplayMode:%{public}@ previousTarget:%{public}@"
- "TSM:%p specifier environment:%{public}@ not in presentation:%{public}@ or target:%{public}@"
- "TSM:%p started ensureFlipbookCurrent operation %{public}@"
- "TSM:%p started environmentUpdate operation %{public}@ for presentation %{public}@"
- "TSM:%p started rampOperation %{public}@"
- "TSM:%p started setPresentation withTargetState:%{public}@ operation %{public}@"
- "TSM:%p started updateDisplayMode pendingOperation %{public}@"
- "TSM:%p started updateDisplayMode rampOperation %{public}@"
- "TSM:%p started updateToSpecifier operation %{public}@"
- "TSM:%p transition system activity assertion callback elapsed:%.4lfs details:%{public}@ error:%{public}@"
- "TSM:%p transition to backlight state for event:%@"
- "TSM:%p updateToPresentation (redundant) displayMode:%{public}@ previousTarget:%{public}@"
- "TSM:%p updateToPresentation by adding:%{public}@ and removing:%{public}@ displayMode:%{public}@ previousTarget:%{public}@"
- "TSM:%p updateToPresentation by adding:%{public}@ displayMode:%{public}@ previousTarget:%{public}@"
- "TSM:%p updateToPresentation by removing:%{public}@ displayMode:%{public}@ previousTarget:%{public}@"
- "TSM:%p updated presentation on invalid session:%{public}@ currentSession:%{public}@ new presentation:%{public}@"
- "TSM:%p waiting for display ramp operation: %{public}@"
- "TSM:%p waiting for operation to complete: %{public}@"
- "TSM:%p waiting for prewarmed event:%p toState:%{public}@"
- "TSM:%p waiting for prewarmed event:%p toState:%{public}@ {\n%{public}@\n}"
- "TSM:%p waiting to perform brightness ramp with duration:%.2lfs using operation:%{public}@"
- "TSM:%p will amend scene %{public}@ for backlightState:%{public}@ with visualState:%{public}@ – willBeForeground:%{BOOL}u containsEnv:%{BOOL}u presentation:%{public}@ oldVisualState:%{public}@ oldPresentationDate:%{public}@ settingsVisualState:%{public}@ settingsPresentationDate:%{public}@"
- "TSM:%p will not amend scene %{public}@ for backlightState:%{public}@ with settingsVisualState:%{public}@ willBeForeground:%{BOOL}u containsEnv:%{BOOL}u presentation:%{public}@ oldVisualState:%{public}@"
- "TSM:%p will resume (if needed) and wait for display operation to complete: %{public}@"
- "TSM:%p would have (but will not) amend scene %{public}@ for backlightState:%{public}@ with visualState:%{public}@ – willBeForeground:%{BOOL}u containsEnv:%{BOOL}u presentation:%{public}@ oldVisualState:%{public}@ oldPresentationDate:%{public}@ settingsVisualState:%{public}@ settingsPresentationDate:%{public}@"
- "TSM:%p: operation is nil (activeEvents:%{public}@). pendEnvUpdate=%@, pendPres=%@, pendUpdateToSpec=%@, pendDisplayMode=%@, queued=%@"
- "T^{__IOSurface=},R,N"
- "Td,?,N,SsetCATransitionsDelayForTesting:"
- "Td,?,N,SsetCBTransitionsDelayForTesting:"
- "Td,?,R,N"
- "Td,?,R,N,V_backlightDimmingDuration"
- "Td,N"
- "Td,R,N"
- "Td,R,N,V_accumulatedLayoutDuration"
- "Td,R,N,V_accumulatedRenderDuration"
- "Td,R,N,V_averageInterval"
- "Td,R,N,V_averagePresentationTimeFromNow"
- "Td,R,N,V_backlightFadeInDuration"
- "Td,R,N,V_backlightFadeOutDuration"
- "Td,R,N,V_coaelscingEpsilon"
- "Td,R,N,V_completionDuration"
- "Td,R,N,V_dimmingDuration"
- "Td,R,N,V_duration"
- "Td,R,N,V_fadeInDuration"
- "Td,R,N,V_fadeOutDuration"
- "Td,R,N,V_framesPerSecond"
- "Td,R,N,V_idleTimeout"
- "Td,R,N,V_intervalUntilFirstFrame"
- "Td,R,N,V_longestInterval"
- "Td,R,N,V_maximumRenderInterval"
- "Td,R,N,V_medianPresentationTimeFromNow"
- "Td,R,N,V_minimumGapDuration"
- "Td,R,N,V_minimumPrepareInterval"
- "Td,R,N,V_presentationDuration"
- "Td,R,N,V_preventedSleepDuration"
- "Td,R,N,V_shortestInterval"
- "Td,R,N,V_surfaceAllocationPoolSize"
- "Td,R,N,V_surfaceOverallocationFactor"
- "Td,R,N,V_timestamp"
- "Td,R,N,V_totalPreparationDuration"
- "Td,R,V_activeDuration"
- "Td,V_duration"
- "Td,V_leeway"
- "Td,V_timeout"
- "Tf,?,R,N"
- "Tf,?,R,N,V_backlightDimmedFactor"
- "Tf,N"
- "Tf,R,N"
- "Tf,R,N,V_averageAPL"
- "Tf,R,N,V_averageAPLDimming"
- "Tf,R,N,V_dimmedFactor"
- "Tf,R,N,V_highestAPL"
- "Tf,R,N,V_highestAPLDimming"
- "Tf,R,N,V_lowestAPL"
- "Tf,R,N,V_lowestAPLDimming"
- "Tf,R,N,V_medianAPL"
- "Tf,R,N,V_medianAPLDimming"
- "Ti,R,N,V_count"
- "Tq,N"
- "Tq,N,V_componentID"
- "Tq,R"
- "Tq,R,N"
- "Tq,R,N,V_backlightState"
- "Tq,R,N,V_eventNewBacklightState"
- "Tq,R,N,V_eventPreviousBacklightState"
- "Tq,R,N,V_frameCapacity"
- "Tq,R,N,V_newBacklightState"
- "Tq,R,N,V_stateMachineOldBacklightState"
- "Tq,R,V_currentDisplayMode"
- "Tq,R,V_rampBeginDisplayMode"
- "Tq,R,V_targetDisplayMode"
- "Tq,V_backlightState"
- "Tq,V_displayMode"
- "Tq,V_targetBacklightState"
- "Tr^v,?,R,N"
- "Tr^v,R,N,V_payload"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "Vv24@0:8@\"<BLSAssertionServiceResponding>\"16"
- "Vv24@0:8@\"BLSAssertionIdentifier\"16"
- "Vv24@0:8@\"NSError\"16"
- "Vv24@0:8@16"
- "Vv32@0:8@\"<BLSAssertionServiceResponding>\"16@\"NSError\"24"
- "Vv32@0:8@\"BLSAssertionIdentifier\"16@\"NSError\"24"
- "Vv32@0:8@\"BLSXPCBacklightProxyObserverMask\"16@?<v@?@\"NSError\">24"
- "Vv32@0:8@16@24"
- "Vv32@0:8@16@?24"
- "[3B]"
- "[8Q]"
- "[BLSHBacklightIdleProvider createSharedProviderWithLocalAssertionService:] should not be called twice"
- "[BLSHBacklightIdleProvider sharedProvider] should not be called before createSharedProviderWithLocalAssertionService:"
- "^{_NSZone=}16@0:8"
- "^{__CFDictionary=}"
- "^{__IOReportSubscriptionCF=}"
- "^{__IOSurface=}16@0:8"
- "^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}24@0:8^{os_state_hints_s=I*II}16"
- "_abandonedInProgressOperation"
- "_abortContext"
- "_abortForWatchdogFire:"
- "_abortReason"
- "_abortReasonString"
- "_abortTimestamp"
- "_abortedEvents"
- "_accumulatedLayoutDuration"
- "_accumulatedRenderDuration"
- "_acquireWaitsToAbortSleepImminent"
- "_acquireWaitsToAbortSleepRequested"
- "_actionHandlers"
- "_active"
- "_activeAssertions"
- "_activeDuration"
- "_activeEvents"
- "_activeTransitionEvent"
- "_additions"
- "_aggregate"
- "_aggregatedAssertionFactory"
- "_alertDidDismiss:"
- "_alertsEnabled"
- "_alwaysOnPresentationEngine"
- "_alwaysOnSupportedByHardware"
- "_assertion"
- "_assertionProxies"
- "_assertionService"
- "_attachments"
- "_attentionAwarenessClient"
- "_attentionAwarenessConfiguration"
- "_attentionLostTimeoutDictionary"
- "_attribute"
- "_attributeHandler"
- "_attributeHandlers"
- "_attributes"
- "_averageAPL"
- "_averageAPLDimming"
- "_averageInterval"
- "_averageMemoryUsage"
- "_averagePresentationTimeFromNow"
- "_backlight"
- "_backlightDimmedFactor"
- "_backlightDimmingDuration"
- "_backlightFadeInDuration"
- "_backlightFadeOutDuration"
- "_backlightHost"
- "_backlightService"
- "_backlightState"
- "_backlightStateChangeTimestamp"
- "_backlightXPCServer"
- "_bls_specifier"
- "_budgetFactory"
- "_budgetProcessIdentity"
- "_budgets"
- "_buildVersion"
- "_bundleID"
- "_caContext"
- "_caDisplayState"
- "_caTransitionsDelayForTesting"
- "_callbackQueue"
- "_cancel"
- "_cbDisplayMode"
- "_cbFlipbookState"
- "_cbTransitionsDelayForTesting"
- "_checkForReadyToAbortAfterWaitingPastFire"
- "_clearIsWaitingForWatchdogCompletion"
- "_clientEnvironment"
- "_clientIsTaskScheduled"
- "_clientPid"
- "_coaelscingEpsilon"
- "_completed"
- "_completedCADisplayState"
- "_completion"
- "_completionDuration"
- "_componentID"
- "_componentName"
- "_componentVersion"
- "_configuration"
- "_containsInvalidation"
- "_count"
- "_countingDictionaryLock"
- "_creationMachTime"
- "_criticalAssertProvider"
- "_criticalAssertTester"
- "_currentDisplayMode"
- "_currentState"
- "_date"
- "_dateInterval"
- "_dateSpecifier"
- "_debugLogsEnabled"
- "_defaults"
- "_defaultsObserver"
- "_delegate"
- "_description"
- "_descriptor"
- "_designation"
- "_detailProviderBlock"
- "_device"
- "_deviceSupportsAlwaysOn"
- "_deviceSupportsAlwaysOnFlipbook"
- "_deviceSupportsAlwaysOnFlipbookWatchdog"
- "_diagnosticsServer"
- "_didBeginUpdateHistory"
- "_didClearDateSpecifiers"
- "_didCompleteAnimation"
- "_didCompleteUpdateHistory"
- "_didFailToRender"
- "_didReset"
- "_didUpdateInitialState"
- "_dimmedFactor"
- "_dimmingDuration"
- "_displayMode"
- "_displayModeSource"
- "_displayReason"
- "_displayStateClient"
- "_displayStateClientSupported"
- "_displayStateControl"
- "_displayStateDelegate"
- "_displayStateMachine"
- "_duration"
- "_enabledByDefault"
- "_encodedPresentationTime"
- "_engine"
- "_ensureFlipbookCurrentOperation"
- "_entitlements"
- "_entries"
- "_entryCount"
- "_enumerator"
- "_environment"
- "_environmentIdentifier"
- "_environmentIdentifiers"
- "_environmentModels"
- "_environmentObserverHelper"
- "_environmentObservers"
- "_environmentSource"
- "_environmentStateMachine"
- "_environmentsSet"
- "_eventNewBacklightState"
- "_eventPerformer"
- "_eventPreviousBacklightState"
- "_events"
- "_expirationDate"
- "_explanation"
- "_fadeInDuration"
- "_fadeOutDuration"
- "_failureSource"
- "_fbScene"
- "_file"
- "_finish:"
- "_fireWatchdogWithTimer:delegate:timeout:elapsedTime:abortContext:explanation:remainingRetries:"
- "_flipbook"
- "_flipbookContext"
- "_flipbookDiagnosticHistoryFrameLimit"
- "_flipbookDiagnosticHistoryMemoryLimit"
- "_flipbookDiagnosticsProvider"
- "_flipbookPowerSavingProvider"
- "_flipbookSpecification"
- "_flipbookSupported"
- "_flipbookTelemetryDelegate"
- "_flipbookTransparent"
- "_flipbookWatchdog"
- "_frameCapacity"
- "_frameId"
- "_frameLimit"
- "_framesPerSecond"
- "_giveUpWaitingForWatchdogCompletionAbortWhileWaitingPastFire:"
- "_globalQueue_initializeDCPStats"
- "_globalQueue_refreshDCPStats:"
- "_gotError"
- "_handlers"
- "_hangDetected"
- "_hangDetectorQueue"
- "_hangDetectorStartTimestamp"
- "_hangDetectorTimer"
- "_hangDetectorWorkloop"
- "_hasChanges"
- "_hasEnsureFlipbookCurrent"
- "_highestAPL"
- "_highestAPLDimming"
- "_hint"
- "_hostFrame"
- "_identifier"
- "_idleTimeout"
- "_ignore"
- "_ignoredDesignations"
- "_inactiveBudgetPolicy"
- "_init"
- "_initTimestamp"
- "_initialSpecifier"
- "_initializing"
- "_insertions"
- "_intervalUntilFirstFrame"
- "_invalidate"
- "_invalidatedEntryCount"
- "_invalidatedFramesHistogram"
- "_invalidationReason"
- "_inverted"
- "_ioReportSubscribedChannels"
- "_ioReportSubscription"
- "_isAnimatedTransition"
- "_isEnvironmentTransitionAnimatedWithPlatformProvider:"
- "_isNullOperationAllowed"
- "_isPotentialHang"
- "_isTransitionForcedUnanimatedWithPlatformProvider:"
- "_key"
- "_keywordIDs"
- "_lastEntryFinalDate"
- "_lastEntryInitialDate"
- "_lastKnown_aodStatsFlipbookMiss"
- "_lastSteadyStateDisplayMode"
- "_lastSteadyStateFlipbookState"
- "_leeway"
- "_liveRenderingTTRWatchdog"
- "_localAssertionService"
- "_localBacklightProxy"
- "_localHostEnvironment"
- "_localService"
- "_lock"
- "_lock_1HzFlipbook"
- "_lock_1HzFlipbookForAssertion"
- "_lock_CAWatchdogTimer"
- "_lock_CAWatchdogType"
- "_lock_CBWatchdogTimer"
- "_lock_CBWatchdogType"
- "_lock_abortedEvents"
- "_lock_accumulatedLayoutDuration"
- "_lock_accumulatedRenderDuration"
- "_lock_accumulatedUnpausedDuration"
- "_lock_acquired"
- "_lock_acquiredAssertion"
- "_lock_acquiredMachContinuousTime"
- "_lock_acquisitionHandler"
- "_lock_active"
- "_lock_activeEvents"
- "_lock_activeFrames"
- "_lock_activeOnAPAwakeAssertion"
- "_lock_activeOnAPAwakeAssertionAcquireTime"
- "_lock_activeOnAPAwakeTimeoutTimer"
- "_lock_activeSession"
- "_lock_activityState"
- "_lock_addSystemActivityAcquisitionHandler:"
- "_lock_addingEnvironmentsCount"
- "_lock_aggregateAssertion"
- "_lock_aggregateAssertions"
- "_lock_aggregated"
- "_lock_aggregator"
- "_lock_alwaysFillFlipbook"
- "_lock_alwaysOnDisabledByAssertion"
- "_lock_alwaysOnEnabledAfterInitialization"
- "_lock_alwaysOnEnabledByPlatform"
- "_lock_alwaysOnEnabledForEnvironment"
- "_lock_alwaysOnEnabledResolved"
- "_lock_alwaysOnSettingEnabled"
- "_lock_alwaysOnSuppressed"
- "_lock_animating"
- "_lock_animationCompletedForOldTarget"
- "_lock_animationCompletedWithNewTarget"
- "_lock_assertion"
- "_lock_averageInterval"
- "_lock_backlightDimmedFactor"
- "_lock_backlightDimmingDuration"
- "_lock_backlightFadeInDuration"
- "_lock_backlightFadeOutDuration"
- "_lock_backlightRampBlock"
- "_lock_backlightState"
- "_lock_beginDate"
- "_lock_beginTime"
- "_lock_begun"
- "_lock_buckets"
- "_lock_caDisplayPowerAssertion"
- "_lock_caDisplayState"
- "_lock_caDisplayStateChangeOperation"
- "_lock_cacheFlipbook"
- "_lock_cacheFlipbookOnDisplayWake"
- "_lock_cachedFlipbookUpdates"
- "_lock_cachedFrameOnGlassNow"
- "_lock_cachedLastCancelledFrame"
- "_lock_cachesFramesOnExit"
- "_lock_canceledMachContinuousTime"
- "_lock_cbDisplayMode"
- "_lock_cbDisplayModeTransitionOperation"
- "_lock_cbFlipbookState"
- "_lock_cbFlipbookStateChangeOperation"
- "_lock_clientActive"
- "_lock_clientAlwaysOnContentIs1hz"
- "_lock_clientHasDelegate"
- "_lock_clientIsTaskScheduled"
- "_lock_clientSupportsAlwaysOn"
- "_lock_complete"
- "_lock_completedCADisplayState"
- "_lock_completedCBDisplayMode"
- "_lock_completedCBFlipbookState"
- "_lock_completion"
- "_lock_count"
- "_lock_delegate"
- "_lock_didCallCompletion"
- "_lock_didDisableFlipbookPowerSavings"
- "_lock_didFailToRender"
- "_lock_didNotifyDisplayModeTransitionStartedButNotCompleted"
- "_lock_didReset"
- "_lock_didStartTransitionToNewState"
- "_lock_didWakeTimestamp"
- "_lock_diffInspector"
- "_lock_displayRampOperation"
- "_lock_durationCalculator"
- "_lock_engineState"
- "_lock_ensureFlipbookCurrentOperation"
- "_lock_entryDictionary"
- "_lock_environmentCount"
- "_lock_environmentIdentifiers"
- "_lock_everPaused"
- "_lock_exemptedSecondsFutureSpecifier"
- "_lock_fillFlipbookState"
- "_lock_fireRetryTimer"
- "_lock_flipbook"
- "_lock_flipbookDisabled"
- "_lock_flipbookIsStale"
- "_lock_flipbookPowerSavingAssertion"
- "_lock_flipbookSpecification"
- "_lock_flipbookTransparent"
- "_lock_forceOverdueAbortTimer"
- "_lock_forcedUnanimated"
- "_lock_frameOnGlassWhenFlipbookCancelled"
- "_lock_frameOnGlassWhenFlipbookLastCancelledAndReset"
- "_lock_frames"
- "_lock_framesDict"
- "_lock_global1HzFlipbook"
- "_lock_globalCacheFlipbook"
- "_lock_globalHighLuminanceAlwaysOn"
- "_lock_globalUnrestrictedFramerate"
- "_lock_highLuminanceAlwaysOn"
- "_lock_idle"
- "_lock_idleProvider"
- "_lock_idleTimeout"
- "_lock_inProgressUpdateTarget"
- "_lock_inactiveEnvSession"
- "_lock_inactiveSession"
- "_lock_incompleteTimelineEntriesForDateInterval"
- "_lock_individualAssertions"
- "_lock_invalidate"
- "_lock_invalidationReason"
- "_lock_invalidationTimer"
- "_lock_isAlwaysOnEnabled"
- "_lock_isPrewarmingDisplayMode"
- "_lock_lastInvalidation"
- "_lock_lastInvalidationTimestamp"
- "_lock_lastLiveSpecifier"
- "_lock_lastNotifiedCompletedDisplayMode"
- "_lock_lastNotifiedTargetDisplayMode"
- "_lock_lastRequestInterval"
- "_lock_lastSteadyStateDisplayMode"
- "_lock_lastSuppressionEvent"
- "_lock_layoutStartTime"
- "_lock_livePowerAssertion"
- "_lock_liveRenderingSystemActivityAssertion"
- "_lock_liveUpdating"
- "_lock_localHostEnvTimelinesComplete"
- "_lock_localTriggerEventForPerformingEvent"
- "_lock_longHeldAssertionHistory"
- "_lock_longestInterval"
- "_lock_modelEnvironments"
- "_lock_nextEventID"
- "_lock_nextSequenceID"
- "_lock_nextTimerID"
- "_lock_nextframeID"
- "_lock_nonInteractiveIdleTimeout"
- "_lock_notifiedCADisplayState"
- "_lock_notifyingObserversWillTransitionToState"
- "_lock_observers"
- "_lock_observingActivatingWithEvent"
- "_lock_observingClient"
- "_lock_observingDeactivatingWithEvent"
- "_lock_observingDidChangeAlwaysOnEnabled"
- "_lock_observingDidCompleteUpdateToState"
- "_lock_observingMask"
- "_lock_observingPerformingEvent"
- "_lock_onStandby"
- "_lock_paused"
- "_lock_pendingEnvironmentUpdate"
- "_lock_pendingEnvironments"
- "_lock_pendingIdleInactiveRequest"
- "_lock_pendingUpdateDisplayMode"
- "_lock_pendingUpdatePresentation"
- "_lock_pendingUpdateToSpecifier"
- "_lock_performEventAPAwakeAssertion"
- "_lock_performEventTargetBacklightState"
- "_lock_performerDelegate"
- "_lock_powerSavingEnabled"
- "_lock_preparingSpecifier"
- "_lock_preparingToRenderSpecifier"
- "_lock_presentation"
- "_lock_presentationDate"
- "_lock_presentationDatesModel"
- "_lock_previousBacklightState"
- "_lock_previousSecondsFutureSpecifier"
- "_lock_previousSecondsRenderedSpecifier"
- "_lock_prewarmingDisplayMode"
- "_lock_prewarmingDisplayMode_startTimestamp"
- "_lock_proceedWithSleepBlock"
- "_lock_queuedEventsToPerform"
- "_lock_rbsAssertion"
- "_lock_reasonsCount"
- "_lock_renderFlipbookSession"
- "_lock_renderFlipbookSessionPowerAssertion"
- "_lock_renderSeed"
- "_lock_renderSessionAssertion"
- "_lock_renderedFrames"
- "_lock_renderingSpecifier"
- "_lock_renderingSpecifier_backoffTime"
- "_lock_requestDateSpecifierFailureCount"
- "_lock_requestDatesOperation"
- "_lock_requestDatesOperationComplete"
- "_lock_requestDatesOperationDidTimeout"
- "_lock_requestingFidelityTarget"
- "_lock_retainedHostFrame"
- "_lock_retryRenderCount"
- "_lock_safeToUnblank"
- "_lock_sceneObservers"
- "_lock_sceneUpdateForPerformingEvent"
- "_lock_sceneWorkspaces"
- "_lock_secondsFidelityAssertion"
- "_lock_sequenceNumber"
- "_lock_service"
- "_lock_serviceNextUpdatesStart"
- "_lock_session"
- "_lock_sessionProvider"
- "_lock_setPresentationCompletion"
- "_lock_setPresentationOperation"
- "_lock_shortestInterval"
- "_lock_shouldInvalidateWhenActivated"
- "_lock_shouldNotifyFlipbookCurrent"
- "_lock_sleepActionCompletion"
- "_lock_sleepImminentSinceScheduled"
- "_lock_sleepRequestedTime"
- "_lock_staleEnvironmentsThatNeedDeferredUpdate"
- "_lock_started"
- "_lock_startedTailspin"
- "_lock_state"
- "_lock_stateIsStale"
- "_lock_stopEngineOnScreenSpecifier"
- "_lock_suppressed"
- "_lock_suppressionServiceActive"
- "_lock_suspended"
- "_lock_systemActivity"
- "_lock_systemActivityAcquisitionDetails"
- "_lock_systemActivityAssertion"
- "_lock_targetBacklightState"
- "_lock_targetIdleBacklightState"
- "_lock_targetState"
- "_lock_timedOut"
- "_lock_timelines"
- "_lock_timelinesCalculators"
- "_lock_timeout"
- "_lock_timeoutTimer"
- "_lock_timer"
- "_lock_transitioningEvent"
- "_lock_unexpectedSleepDebounceTimer"
- "_lock_unpauseMachContinuousTime"
- "_lock_unrestrictedFramerateUpdates"
- "_lock_update1HzFromPresentation:"
- "_lock_updatingDateSpecifierTransitionStates"
- "_lock_updatingToPresentation"
- "_lock_updatingVisualStateTransitionStates"
- "_lock_usePseudoFlipbook"
- "_lock_userActivityOccured"
- "_lock_valid"
- "_lock_validateHostFrame:source:"
- "_lock_visualState"
- "_lock_visualStateMismatchStartTime"
- "_lock_waitStartTimestamp"
- "_lock_waiting"
- "_lock_waitingAbortParams"
- "_lock_waitingForTailspin"
- "_lock_waitingForWatchdogCompletion"
- "_lock_wakeWatchdogTimer"
- "_lock_waking"
- "_lock_watchdogStart"
- "_log"
- "_longestInterval"
- "_lowestAPL"
- "_lowestAPLDimming"
- "_machContinuousTimestamp"
- "_mainQueue_alertFor1hzFlipbookFrameMiss:"
- "_main_callCompletion"
- "_main_waitWithCompletion:"
- "_maximumRenderInterval"
- "_medianAPL"
- "_medianAPLDimming"
- "_medianMemoryUsage"
- "_medianPresentationTimeFromNow"
- "_memoryLimit"
- "_memoryUsage"
- "_memoryUsageHistogram"
- "_minimumGapDuration"
- "_minimumPrepareInterval"
- "_minuteBoundaryDate"
- "_minutesBudget"
- "_newBacklightState"
- "_next"
- "_nextUpdatesStart"
- "_nilSceneIdentifier"
- "_nullBudget"
- "_nullInactiveBudgetPolicy"
- "_observedDefaults"
- "_observer"
- "_observers"
- "_onMain_watchdogTimer"
- "_osInterface"
- "_osInterfaceProvider"
- "_osTimerProvider"
- "_pause"
- "_paused"
- "_pausedAssertions"
- "_payload"
- "_payloadSize"
- "_pendingBacklightRamp"
- "_pendingEnvironmentUpdate"
- "_pendingNotifyBeganUpdatingState"
- "_pendingOperation"
- "_pendingPrewarmedEvent"
- "_pendingTransitionStateCount"
- "_pendingUpdateDisplayMode"
- "_pendingUpdatePresentation"
- "_pendingUpdateToSpecifier"
- "_performEventHistory"
- "_platformProvider"
- "_populatePayload"
- "_powerResourceHint"
- "_predicate"
- "_presentation"
- "_presentationDate"
- "_presentationDuration"
- "_presentationEntries"
- "_presentationInterval"
- "_presentationSource"
- "_presentationTime"
- "_presentationTimeHistogram"
- "_preventedSleepDuration"
- "_previous"
- "_previousPresentationDate"
- "_prewarmingDisplayMode"
- "_processIdentity"
- "_processMonitor"
- "_processName"
- "_provider"
- "_providerDelegate"
- "_queue"
- "_queue_deferredAcquisitionAssertions"
- "_queuedEventsToPerform"
- "_radarDescription"
- "_radarIsUserInitiated"
- "_radarTitle"
- "_rampBeginDisplayMode"
- "_readyToStart"
- "_realInactiveBudgetPolicy"
- "_reason"
- "_reasonEnded"
- "_remoteProcessHandle"
- "_remoteTarget"
- "_removals"
- "_rendered"
- "_renderedEntryCount"
- "_renderedFlipbookHistory"
- "_requestInterval"
- "_reset"
- "_resume"
- "_rootWorkloop"
- "_scene"
- "_sceneIdentityToken"
- "_secondsBudget"
- "_secondsFidelity"
- "_sequenceID"
- "_server"
- "_service"
- "_serviceListener"
- "_sessionFramesHistogram"
- "_sessionProvider"
- "_sessionStartTime"
- "_setCBDisplayModeTimer"
- "_setIdleTimeout:shouldReset:"
- "_setShouldNotifyOfUnidle:"
- "_setupUserDefaults"
- "_sharedBacklightHost == nil"
- "_shortestInterval"
- "_shouldFaultOnFailureToAcquire"
- "_shouldIgnore"
- "_shouldNotifyOfUnidle"
- "_shouldNotifyOfUnidleChanged"
- "_shouldReset"
- "_shouldRunWatchdog"
- "_showTTRAlert"
- "_showingBlankingWindow"
- "_sleepAction"
- "_sleepImminentSinceScheduled"
- "_sleepImminentWhenScheduled"
- "_sleepMonitor"
- "_sleepMonitorAggregateState"
- "_softMemoryLimit"
- "_source"
- "_sourceModel"
- "_specifier"
- "_specifiers"
- "_start"
- "_startDate"
- "_startWritingTailspin"
- "_started"
- "_startedTime"
- "_stateHandler"
- "_stateMachine"
- "_stateMachineOldBacklightState"
- "_subHostedHostEnvironments"
- "_suppressionManager"
- "_suppressionServiceActive"
- "_suppressionSupported"
- "_surfaceAllocationPoolSize"
- "_surfaceOverallocationFactor"
- "_tailspinFilesDirectory"
- "_targetBacklightState"
- "_targetDisplayMode"
- "_targetState"
- "_telemetryDelegate"
- "_test_enabledViaDefaults"
- "_test_forceShowTTRLater"
- "_test_forceShowTTRLater:"
- "_test_forceTryAgainNow"
- "_test_tryAgainState"
- "_testables"
- "_timeOfIssue"
- "_timeReleased"
- "_timeStamp"
- "_timedOutCount"
- "_timedOutEnvironmentCount"
- "_timeout"
- "_timer"
- "_timerIdentifier"
- "_timestamp"
- "_totalCount"
- "_totalPreparationDuration"
- "_touchLockAssertion"
- "_transitionAPAwakeAssertion"
- "_transitionStateMachine"
- "_transitionStates"
- "_triggerEvent"
- "_triggerTestCriticalAssert:"
- "_triggerTestWatchdog:"
- "_ttrDialog"
- "_ttrDisplayReason"
- "_ttrPromptHeader"
- "_ttrPromptMessage"
- "_type"
- "_updatedInitialState"
- "_updater"
- "_updates"
- "_updatingSpecifier"
- "_updatingState"
- "_userInitiated"
- "_userObject"
- "_valid"
- "_visualState"
- "_wantsTransform"
- "_wasReset"
- "_watchdogEnabled"
- "_watchdogFired:"
- "_watchdogProvider"
- "_watchdogProviderDelegate"
- "_watchdogTester"
- "_watchdogTimer"
- "_watchdogType"
- "abandonedInProgressOperation"
- "abortContext"
- "abortContextForTimer:"
- "abortForWatchdog:payload:payloadSize:explanation:"
- "abortReason"
- "abortReasonString"
- "abortTimestamp"
- "acquire"
- "acquireAggregatedAssertion:completion:"
- "acquireAssertion:"
- "acquireAssertionForDescriptor:error:"
- "acquireDisplayPowerAssertionForReason:"
- "acquireIndividualAssertion:handler:"
- "acquireWaitsToAbortSleepImminent"
- "acquireWaitsToAbortSleepRequested"
- "acquireWithCompletion:"
- "acquireWithError:"
- "acquireWithExplanation:observer:attributes:"
- "acquireWithObserver:"
- "acquireWithTimeout:handler:"
- "acquisitionState"
- "actionCompleted"
- "actionWithIdentifier:delegate:"
- "actionWithIdentifier:delegate:osInterfaceProvider:"
- "activate"
- "activate:withEntry:"
- "activateAttributes:fromAssertion:forService:"
- "activateForAttribute:fromAssertion:forService:attributeHandler:"
- "activateForSceneEnvironment:"
- "activateWithFirstEntry:"
- "active"
- "activeSession"
- "activeTransitionEvent"
- "activityMode"
- "addActionHandler:forScene:"
- "addEnvironmentsObserver:"
- "addFutureSpecifier:hasSecondsBudget:allowBeforeStart:"
- "addHandlerForKey:attributes:"
- "addInvalidation:hasSecondsBudget:allowBeforeStart:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:"
- "addObserver:forKeyPath:options:context:"
- "addObserverForName:object:queue:usingBlock:"
- "addRenderedFrameToHistory:"
- "addSceneObserver:forSceneIdentityToken:"
- "adjustedLuminance"
- "aggregateDesiredFidelityForBacklightState:withCompletion:"
- "aggregateState"
- "allFlipbookFrames"
- "allFrames"
- "allObjects"
- "allValues"
- "allowedFidelityAtDate:expectedFidelity:"
- "allowedFidelityAtDate:forEnvironment:expectedFidelity:"
- "alwaysOnContentIs1hz"
- "alwaysOnDisabledByAssertion"
- "alwaysOnEnabledForEnvironment"
- "alwaysOnSession"
- "alwaysOnSettingEnabled"
- "alwaysOnSuppressed"
- "amendSceneSettings:"
- "animationCoalesceThreshold"
- "anyObject"
- "aplDimming"
- "appendArraySection:withName:multilinePrefix:skipIfEmpty:"
- "appendArraySection:withName:multilinePrefix:skipIfEmpty:objectTransformer:"
- "appendArraySection:withName:skipIfEmpty:"
- "appendArraySection:withName:skipIfEmpty:objectTransformer:"
- "appendBodySectionWithName:block:"
- "appendBodySectionWithName:multilinePrefix:block:"
- "appendBodySectionWithName:openDelimiter:closeDelimiter:block:"
- "appendBodySectionWithOpenDelimiter:closeDelimiter:block:"
- "appendBool:"
- "appendBool:counterpart:"
- "appendBool:withName:"
- "appendBool:withName:ifEqualTo:"
- "appendCollection:withName:itemBlock:"
- "appendCustomFormatWithName:block:"
- "appendDictionarySection:withName:skipIfEmpty:"
- "appendDouble:withName:decimalPrecision:"
- "appendFloat:withName:"
- "appendFloat:withName:decimalPrecision:"
- "appendFormat:"
- "appendInt64:"
- "appendInt64:counterpart:"
- "appendInt:withName:"
- "appendInteger:"
- "appendInteger:counterpart:"
- "appendInteger:withName:"
- "appendObject:"
- "appendObject:counterpart:"
- "appendObject:withName:"
- "appendObject:withName:skipIfNil:"
- "appendPointer:"
- "appendPointer:counterpart:"
- "appendPointer:withName:"
- "appendProem:block:"
- "appendRect:withName:"
- "appendString:counterpart:"
- "appendString:withName:"
- "appendString:withName:skipIfEmpty:"
- "appendTimeInterval:withName:decomposeUnits:"
- "appendUInt64:withName:"
- "appendUnsignedInt:withName:"
- "appendUnsignedInteger:"
- "appendUnsignedInteger:withName:"
- "applyRenderedSpecifier:allowBeforeStart:"
- "array"
- "arrayByAddingObjectsFromArray:"
- "arrayForKey:"
- "arrayWithCapacity:"
- "arrayWithObject:"
- "arrayWithObjects:count:"
- "assertion:failedToAcquireWithError:"
- "assertionAcquired:"
- "assertionDidCancel:withError:"
- "assertionPaused:"
- "assertionResumed:"
- "assertionWillCancel:"
- "associatedObject"
- "attachments"
- "attentionAwarenessClient"
- "attentionAwarenessConfiguration"
- "attentionLostTimeoutDictionary"
- "attributeBaseClass"
- "attributeClasses"
- "attributeOfClass:"
- "attributeWithDuration:warningDuration:startPolicy:endPolicy:"
- "attributes"
- "attributesOfClasses:"
- "autorelease"
- "autoupdatingCurrentCalendar"
- "averageAPL"
- "averageAPLDimming"
- "averageMemoryUsage"
- "averagePresentationTimeFromNow"
- "backlight:activatingWithEvent:"
- "backlight:deactivatingWithEvent:"
- "backlight:didBlankToDisplayMode:fromDisplayMode:activeEvents:abortedEvents:"
- "backlight:didChangeAlwaysOnEnabled:"
- "backlight:didCompleteUpdateToFlipbookState:forEvent:"
- "backlight:didCompleteUpdateToFlipbookState:forEvents:abortedEvents:"
- "backlight:didCompleteUpdateToState:forEvent:"
- "backlight:didCompleteUpdateToState:forEvents:abortedEvents:"
- "backlight:didUpdateToDisplayMode:fromDisplayMode:activeEvents:abortedEvents:"
- "backlight:didUpdateVisualContentsToBeginTransitionToState:forEvents:abortedEvents:"
- "backlight:performingEvent:"
- "backlight:willUnblankToDisplayMode:fromDisplayMode:forEvents:abortedEvents:"
- "backlight:willUpdateToDisplayMode:fromDisplayMode:forEvents:abortedEvents:"
- "backlightChangeRequestExplanationIdentifierFromString:"
- "backlightDimmingDuration"
- "backlightDisplayMode"
- "backlightFadeInDuration"
- "backlightFadeOutDuration"
- "backlightHost:willTransitionToState:forEvent:"
- "backlightPlatformProvider"
- "backlightSceneHostEnvironment"
- "backlightServices.setCBDisplayMode"
- "backlightStateChangeTimestamp"
- "backlightStateDescription"
- "backlightTelemetrySource:didAcquireSystemActivityWithError:isActive:details:forEvent:"
- "backlightTelemetrySource:didCompleteUpdateToFlipbookState:forEvent:"
- "backlightTelemetrySource:didCompleteUpdateToFlipbookState:forEvents:abortedEvents:"
- "backlightTelemetrySource:didCompleteUpdateToState:forEvent:"
- "backlightTelemetrySource:didCompleteUpdateToState:forEvents:abortedEvents:"
- "backlightTelemetrySource:didUnblankToDisplayMode:fromDisplayMode:activeEvents:abortedEvents:"
- "backlightTelemetrySource:didUpdateDisplayForState:forEvent:"
- "backlightTelemetrySource:didUpdateDisplayForState:forEvents:abortedEvents:"
- "backlightTelemetrySource:didUpdateVisualContentsToBeginTransitionToState:forEvent:"
- "backlightTelemetrySource:didUpdateVisualContentsToBeginTransitionToState:forEvents:abortedEvents:"
- "backlightTelemetrySource:hadExistingSystemActivityForEvent:"
- "backlightTelemetrySource:willPerformEvent:"
- "backlightTelemetrySource:willTransitionToState:forEvent:"
- "backlightTurnedOnForEvent:"
- "beginDate"
- "beginOperationWithIntervals:shouldReset:"
- "beginSpecialManagementForHostEnvironment:"
- "beginTimestamp"
- "bls_alwaysOnContentIs1hz"
- "bls_appendBoundedCollection:withName:maximumItems:itemBlock:"
- "bls_appendTimeInterval:withName:decomposeUnits:"
- "bls_boundedDescription"
- "bls_boundedDescriptionWithMax:transformer:"
- "bls_boundedDescriptionWithTransformer:"
- "bls_containsDate:withEpsilon:outDelta:"
- "bls_debugLoggingDescriptionForState:"
- "bls_doubleMedian"
- "bls_fileNameString"
- "bls_hasDelegate"
- "bls_hasUnrestrictedFramerateUpdates"
- "bls_initWithBSContinuousMachTime:"
- "bls_initWithMachContinuousTime:"
- "bls_isAlwaysOnEnabledForEnvironment"
- "bls_isDelegateActive"
- "bls_isLiveUpdating"
- "bls_isOnOrAfter:"
- "bls_isOnOrAfter:andOnOrBefore:"
- "bls_isOnOrBefore:"
- "bls_loggingString"
- "bls_loggingStringForState:"
- "bls_machContinuousTime"
- "bls_optsOutOfProcessAssertions"
- "bls_presentationDate"
- "bls_setAlwaysOnEnabledForEnvironment:"
- "bls_setDelegateActive:"
- "bls_setLiveUpdating:"
- "bls_setPresentationDate:"
- "bls_setRenderSeed:"
- "bls_setUnrestrictedFramerateUpdates:"
- "bls_setVisualState:"
- "bls_shortLoggingString"
- "bls_shortLoggingStringForState:"
- "bls_specifier"
- "bls_supportsAlwaysOn"
- "bls_unsignedIntegerMedian"
- "bls_uuid"
- "bls_visualState"
- "boolForKey:"
- "boolValue"
- "bootstrapConfiguration"
- "bs_compactMap:"
- "bs_filter:"
- "bs_map:"
- "bs_mapNoNulls:"
- "bs_reverse"
- "bs_safeNumberForKey:"
- "bs_safeObjectForKey:ofType:"
- "bs_safeStringForKey:"
- "bucketCount"
- "budgetProcessIdentity"
- "build"
- "buildVersion"
- "builder"
- "builderWithObject:"
- "builderWithObject:ofExpectedClass:"
- "bundleID"
- "bundleIdentifier"
- "cStringUsingEncoding:"
- "caContext"
- "caDisplayPowerState"
- "caTransitionsDelayForTesting"
- "cacheFlipbookOnDisplayWake"
- "calculateWithCompletion:"
- "callCompletion"
- "callCompletion:shouldTryAgain:"
- "callCompletionForReason:"
- "callCompletionIfDone"
- "canBePaused"
- "cancel"
- "cancelAllFramesWithError:"
- "cancelAssertion:withError:"
- "cancelWithError:"
- "cannot change cb display mode to %@, flipbook state:%@ is transitioning"
- "cannot register handler for classes:%@ overlaps existing handler for classes:%@"
- "captureFrameOnGlass"
- "cbTransitionsDelayForTesting"
- "changeRequest"
- "chargeRenderedSpecifier:"
- "chargeRenderedSpecifier:expectedFidelity:"
- "chargeSpecifier:withChargeBlock:fitInBucketBlock:exceededBudgetBlock:missedBucketBlock:"
- "checkEntitlementSource:forSingleEntitlement:error:"
- "checkEntitlementSourceForRequiredEntitlements returned NO but did not provide an error for process:%ld:'%@' descriptor:%@"
- "checkEntitlementSourceForRequiredEntitlements:error:"
- "checkForWatchdogDidFire:"
- "class"
- "classLock_aggregateForProcessIdentity:shouldCreate:"
- "clearAllSpecifiers"
- "clearPresentationDate"
- "clearSpecifiersForEnvironment:"
- "clearUserInteraction"
- "clearWatchdogWithExplanation:reason:timeout:elapsedTime:"
- "clientAlwaysOnContentIs1hz"
- "clientDidRequestInvalidationForReason:"
- "clientHasDelegate"
- "clientIdentity"
- "clientPid"
- "clientSettings"
- "clientSupportsAlwaysOn"
- "code"
- "compare:"
- "completeWithDateSpecifiers:"
- "completeWithDesiredFidelity:"
- "componentID"
- "componentName"
- "componentVersion"
- "components:fromDate:"
- "components:fromDate:toDate:options:"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "configurationWithFadeInDuration:fadeOutDuration:"
- "configurationWithFadeInDuration:fadeOutDuration:dimmingDuration:dimmedFactor:"
- "configureConnection:"
- "conformsToProtocol:"
- "constructFrameSpecifiersForTimelines:dateInterval:shouldConstructStartSpecifier:framesPerSecond:previousSpecifier:"
- "containsDate:"
- "containsEnvironment:"
- "containsObject:"
- "containsString:"
- "contextId"
- "copy"
- "copyWithZone:"
- "count1to2Min"
- "count2to3Min"
- "count3to4Min"
- "count4to5Min"
- "count5to6Min"
- "countByEnumeratingWithState:objects:count:"
- "countLessThan1Min"
- "countMoreThan6Min"
- "countSpecifier:hasSecondsBudget:isCoalesceAllowed:"
- "countingTargetForEntry:"
- "createAggregatedSystemActivityAssertionWithIdentifier:configurator:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "createDisplayPowerResourceHintWithState:"
- "createFlipbook"
- "createInactiveEnvironmentSession"
- "createLocalHostEnvironmentForEnvironment:"
- "createPowerAssertionWithIdentifier:"
- "createPowerAssertionWithReason:identifier:"
- "createRBSAssertion"
- "createSharedProviderWithLocalAssertionService:"
- "createStateForEnvironment:delegate:"
- "createSystemActivityAssertionWithIdentifier:configurator:"
- "createWithFrame:"
- "createWithInitialSpecifier:enumerator:dateInterval:environment:sourceModel:"
- "createWithPlatformProvider:"
- "currentContext"
- "currentDisplayMode"
- "d"
- "d16@0:8"
- "d24@0:8@16"
- "d28@0:8@16B24"
- "d32@0:8@16B24B28"
- "date"
- "dateByAddingTimeInterval:"
- "dateInterval"
- "dateSpecifier"
- "dateSpecifierForEnvironment:"
- "dateSpecifierModel:didAddEnvironment:"
- "dateSpecifierModel:didRemoveEnvironment:"
- "dateSpecifiers"
- "dateWithTimeIntervalSinceNow:"
- "dateWithTimeIntervalSinceReferenceDate:"
- "deactivateAttributes:fromAssertion:forService:"
- "deactivateClient"
- "deactivateForSceneEnvironment:"
- "deactivateWithFinalEntry:"
- "dealloc"
- "debugDescription"
- "debugLogsEnabled"
- "decrementDisablePowerSavingUsageCountForReason:"
- "defaultCenter"
- "defaultIsEnvironmentTransitionAnimatedToState:fromPreviousState:"
- "defaultIsTransitionForcedUnanimatedToState:fromPreviousState:"
- "defaultShellMachName"
- "defaultTransitionForcedUnanimatedForSource:"
- "definition"
- "delegateQueue"
- "dequeueAllUpdates"
- "dequeueNextUpdate"
- "deregisterSceneWorkspace:"
- "description"
- "descriptionForObject:"
- "descriptionForTimestamp:"
- "designation"
- "desiredFidelity"
- "desiredFidelityForDateInterval:timelines:withCompletion:"
- "destroyAssertion:"
- "destroyInactiveEnvSession"
- "device"
- "deviceSupportsAlwaysOn"
- "deviceSupportsAlwaysOnFlipbook"
- "deviceSupportsAlwaysOnFlipbookWatchdog"
- "dictionary"
- "dictionaryForKey:"
- "dictionaryWithCapacity:"
- "dictionaryWithObjects:forKeys:count:"
- "did startServer:%{public}@ withLocalBacklightProxy:%{public}@"
- "didAcquireSystemActivityIsActive:error:details:"
- "didBeginUpdateToBacklightState:"
- "didChangeAlwaysOnEnabled:"
- "didCompleteAnimation"
- "didCompleteSwitchToFlipbookState:withError:"
- "didCompleteTransitionToDisplayMode:withError:"
- "didCompleteUpdateToBacklightState:"
- "didCompleteUpdateToState:forEvents:abortedEvents:"
- "didDetectSignificantUserInteraction"
- "didEndInactiveEnvironmentSession:"
- "didFinishDumpingStateForWatchdog:"
- "didUpdateInitialState"
- "didUpdateToPresentation:"
- "differenceFromPresentation:"
- "differenceFromPresentation:forEachRemoval:forEachAddition:"
- "dimmedFactor"
- "dimmingDuration"
- "disablePowerSavingForReason:"
- "disableWatchdogs"
- "dispatchToMainQueueAfterSecondsDelay:identifier:block:"
- "dispatchWithQOSClass:block:"
- "displayReason"
- "displayState"
- "displayState:didUpdateToBrightnessCurve:"
- "displayState:didUpdateToMode:"
- "displayStateDelegate"
- "displayStateMachine"
- "distantFuture"
- "distantPast"
- "domain"
- "domainForMachName:"
- "domainSpecification"
- "domainsContainingServiceIdentifier:"
- "doubleValue"
- "earlierDate:"
- "earlyInitialization"
- "enableAlertsUsingDefaults"
- "enableSubhostingForEnvironment:withSessionProvider:"
- "enableSubhostingForEnvironment:withSessionProvider:osTimerProvider:"
- "enabledByDefault"
- "encodedPresentationTime"
- "endAddingEnvironments"
- "endDate"
- "endSuppressionService"
- "endSuppressionServiceWithExplanation:logBlock:"
- "engineState"
- "ensureAlwaysOnSessionCreated"
- "ensureInactiveEnvSessionCreated"
- "entriesForCountingTarget:"
- "entryClass"
- "entryCount"
- "entryForPresentationTime:withRequestedFidelity:animated:userObject:"
- "entrySpecifierForTimelineIdentifier:"
- "enumerateDateSpecifiersUsingBlock:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "enumerateObjectsWithOptions:usingBlock:"
- "enumerator"
- "environment:performBacklightSceneUpdate:"
- "environment:timelinesForDateInterval:previousSpecifier:completion:"
- "environmentIdentifier"
- "environmentIdentifiers"
- "environmentSource"
- "environmentStateMachine:didBeginUpdateToState:"
- "environmentStateMachine:didCompleteUpdateToState:"
- "environmentStateMachine:didUpdateToPresentation:"
- "environmentStateMachine:didUpdateToSpecifier:"
- "environmentsSet"
- "errorWithDomain:code:userInfo:"
- "eventMask"
- "eventNewBacklightState"
- "eventPerformer"
- "eventPreviousBacklightState"
- "existingBacklightSceneHostEnvironment"
- "f"
- "f16@0:8"
- "fadeInDuration"
- "fadeOutDuration"
- "failureSource"
- "fileRadar:log:completion:"
- "filter:"
- "fireWatchdogWithTimer:delegate:timeout:elapsedTime:"
- "first"
- "firstObject"
- "firstObjectCommonWithArray:"
- "flipBookWithOptions:"
- "flipbook"
- "flipbookContext"
- "flipbookDiagnosticHistoryFrameLimit"
- "flipbookDiagnosticHistoryMemoryLimit"
- "flipbookDisabled"
- "flipbookPowerSavingEnabled"
- "flipbookSpecification"
- "flipbookTelemetryDelegate"
- "formatDuration:"
- "frameAtTime:"
- "frameSpecifier"
- "frameWithUUID:"
- "framesPerSecond"
- "fullyCompleted"
- "genericSurfaceForFrameUUID:reply:name:surfaceFromFrame:"
- "getBacklightState"
- "getFlipbookState"
- "global1HzFlipbook"
- "globalCacheFlipbookOnDisplayWake"
- "globalHighLuminanceAlwaysOn"
- "globalUnrestrictedFramerate"
- "grant"
- "grantUserInitiated"
- "grantWithBackgroundPriority"
- "grantedFidelity"
- "handlerForKey:attributes:"
- "hangDetected"
- "hangDetectorFired:"
- "hasBeenRendered"
- "hasEntitlement:"
- "hasIgnoredDesignations"
- "hasPendingRamp"
- "hasPrefix:"
- "hasSecondsBudgetAtDate:"
- "hasSleepBeenImminentSinceScheduled"
- "hasSleepBeenRequested"
- "hasSuffix:"
- "hasUserActivityOccured"
- "hasVisualStateMistmach"
- "hash"
- "highLuminanceAlwaysOn"
- "highestAPL"
- "highestAPLDimming"
- "hintWithHint:"
- "histogramWithReferenceDate:flipbookFrames:"
- "histogramWithReferenceDate:iteratePresentationDatesBlock:"
- "hostEnvironment:clientDidUpdateAlwaysOnContentIs1hz:"
- "hostEnvironment:clientDidUpdateEnabled:"
- "hostEnvironment:clientDidUpdateSupportsAlwaysOn:"
- "hostEnvironment:didAmendSceneSettings:"
- "hostEnvironment:hostDidSet1HzFlipbook:"
- "hostEnvironment:hostDidSetAlwaysOnEnabledForEnvironment:"
- "hostEnvironment:hostDidSetCacheFlipbookOnDisplayWake:"
- "hostEnvironment:hostDidSetHighLuminanceAlwaysOn:"
- "hostEnvironment:hostDidSetLiveUpdating:"
- "hostEnvironment:hostDidSetUnrestrictedFramerateUpdates:"
- "hostEnvironment:invalidateContentForReason:"
- "hostFrame"
- "hostFrameForUUID:"
- "hour"
- "i16@0:8"
- "identityToken"
- "idle"
- "idleProviderDidIdle:"
- "idleProviderDidUnidle:"
- "ifStillValidPerformAlwaysOnBrightnessRamp:withDuration:"
- "ignoreRadarDesignation:"
- "ignoreWatchdogAborts"
- "inProgressOperation"
- "inactiveBudgetPolicy"
- "inactiveEnvironmentSession:didBeginUpdateToBacklightState:"
- "inactiveEnvironmentSession:didUpdateToPresentation:"
- "inactiveEnvironmentSession:updateToPresentation:"
- "inactiveSession"
- "incrementDisablePowerSavingUsageCountForReason:"
- "indexOfObject:inSortedRange:options:usingComparator:"
- "indexOfObjectWithOptions:passingTest:"
- "indexesOfObjectsPassingTest:"
- "init"
- "initForAttribute:fromAssertion:forService:"
- "initForAttribute:fromAssertion:forService:attributeHandler:"
- "initForEnvironment:visualState:previousVisualState:frameSpecifier:animated:triggerEvent:touchTargetable:isUpdateToDateSpecifier:sceneContentsUpdated:performBacklightRamp:sceneContentsAnimationComplete:"
- "initForService:"
- "initForService:provider:"
- "initWithActiveAppearance:updateFidelity:adjustedLuminance:"
- "initWithActiveAppearance:updateFidelity:adjustedLuminance:dimmed:"
- "initWithBacklightChangeEvent:animated:touchTargetable:isUpdateToDateSpecifier:completion:"
- "initWithBacklightRampBlock:"
- "initWithBacklightSceneEnvironment:"
- "initWithBacklightState:"
- "initWithBacklightState:additions:"
- "initWithBudgetFactory:"
- "initWithCAContext:wantsTransform:inverted:"
- "initWithCapacity:"
- "initWithCapacity:keyOrderingStrategy:"
- "initWithClientPid:hostPid:count:"
- "initWithClientType:"
- "initWithCompletion:"
- "initWithConfiguration:"
- "initWithConfigurator:"
- "initWithCoreMotionEvent:timestamp:"
- "initWithCriticalAssertDidFailDictionary:"
- "initWithCurrentDisplayMode:targetDisplayMode:"
- "initWithCurrentState:targetState:activeEvents:abortedEvents:pendingEnvironmentUpdate:pendingUpdatePresentation:pendingUpdateToSpecifier:pendingUpdateDisplayMode:ensureFlipbookCurrentOperation:queuedEventsToPerform:pendingPrewarmedEvent:environmentStateMachine:sleepMonitorAggregateState:"
- "initWithDate:fidelity:"
- "initWithDate:fidelity:userObject:"
- "initWithDateInterval:previousPresentationDate:shouldReset:completion:"
- "initWithDelegate:"
- "initWithDelegate:abortContext:isPotentialHang:sleepMonitorAggregateState:sleepImminentSinceScheduled:explanation:"
- "initWithDelegate:flipbook:presentation:osInterfaceProvider:"
- "initWithDelegate:platformProvider:osInterfaceProvider:"
- "initWithDelegate:platformProvider:osInterfaceProvider:inactiveBudgetPolicy:"
- "initWithDescriptor:log:"
- "initWithDesignation:radarTitle:radarDescription:"
- "initWithDisplayMode:"
- "initWithDisplayMode:prewarmingDisplayMode:lastSteadyStateDisplayMode:caDisplayState:cbDisplayMode:showingBlankingWindow:sleepMonitorAggregateState:hasEnsureFlipbookCurrent:"
- "initWithDisplayModeSource:"
- "initWithDuration:"
- "initWithEngine:"
- "initWithEnvironment:"
- "initWithEnvironment:environmentSource:"
- "initWithEnvironment:userObject:"
- "initWithEnvironmentIdentifier:newBacklightState:pendingTransitionStateCount:"
- "initWithEnvironments:caContext:expirationDate:"
- "initWithEventID:state:previousState:changeRequest:"
- "initWithEventID:state:previousState:wasTransitioning:changeRequest:"
- "initWithEvents:withInitialSpecifier:"
- "initWithExplanation:"
- "initWithExplanation:attributes:"
- "initWithExplanation:delegate:provider:"
- "initWithExplanation:processIdentity:duration:"
- "initWithExplanation:target:attributes:"
- "initWithFBScene:"
- "initWithFadeInDuration:fadeOutDuration:dimmingDuration:dimmedFactor:"
- "initWithFlipbookDiagnosticsProvider:"
- "initWithFlipbookDiagnosticsProvider:peer:"
- "initWithFrame:"
- "initWithFrameCapacity:framesPerSecond:minimumGapDuration:coaelscingEpsilon:minimumPrepareInterval:maximumRenderInterval:"
- "initWithFrameLimit:memoryLimit:"
- "initWithFutureSpecifier:"
- "initWithHasChanges:insertedEnvironments:removedEnvironments:"
- "initWithHint:"
- "initWithIdentifier:"
- "initWithIdentifier:configurator:"
- "initWithIdentifier:delegate:osInterfaceProvider:"
- "initWithIdentifier:descriptor:remoteTarget:"
- "initWithIdentifier:forReason:invalidationBlock:"
- "initWithIdentifier:osInterfaceProvider:"
- "initWithIdentifier:osTimerProvider:"
- "initWithInactiveBudgetPolicy:"
- "initWithInvalidation:"
- "initWithKey:attributes:"
- "initWithKeyOptions:valueOptions:capacity:"
- "initWithLocalAssertionService:"
- "initWithLocalAssertionService:idleProvider:backlightHost:"
- "initWithLocalBacklightProxy:"
- "initWithLocalBacklightProxy:peer:"
- "initWithLocalService:peer:"
- "initWithNotificationName:"
- "initWithOSInterfaceProvider:"
- "initWithOSInterfaceProvider:localOnly:"
- "initWithOSProvider:configurationProvider:detailProvider:"
- "initWithOSTimerProvider:"
- "initWithObserver:"
- "initWithObserver:sceneIdentityToken:"
- "initWithOptions:capacity:"
- "initWithPlatformProvider:"
- "initWithPlatformProvider:eventPerformer:osInterfaceProvider:"
- "initWithPlatformProvider:localOnly:"
- "initWithPlatformProvider:osInterfaceProvider:inactiveBudgetPolicy:"
- "initWithPlatformProvider:osInterfaceProvider:inactiveBudgetPolicy:localAssertionService:localOnly:"
- "initWithPredicate:"
- "initWithPresentation:"
- "initWithPresentation:backlightState:delegate:inactiveBudgetPolicy:osTimerProvider:"
- "initWithPresentation:backlightState:delegate:inactiveBudgetPolicy:osTimerProvider:platformProvider:"
- "initWithPresentationDate:fidelity:environment:userObject:"
- "initWithPresentationDate:specifiers:"
- "initWithPresentationEntries:caContext:expirationDate:"
- "initWithPresentationEntries:flipbookContext:expirationDate:"
- "initWithPresentationInterval:previousPresentationDate:shouldReset:environment:"
- "initWithPresentationTime:frameId:apl:aplDimming:memoryUsage:rawSurfaceFrameRect:inverted:specifier:uuid:"
- "initWithPresentationTime:frameId:specifier:memoryUsage:"
- "initWithProcessIdentity:"
- "initWithRampBeginDisplayMode:targetDisplayMode:"
- "initWithReason:"
- "initWithRequestInterval:delegate:osTimerProvider:"
- "initWithRequestedActivityState:explanation:timestamp:sourceEvent:sourceEventMetadata:"
- "initWithResourceType:andState:"
- "initWithSequenceID:backlightState:triggerEvent:backlightRampBlock:forIdentifier:previousTarget:"
- "initWithSequenceID:backlightState:visualState:presentationDate:triggerEvent:pendingBacklightRamp:"
- "initWithSessionProvider:localHostEnvironment:osTimerProvider:"
- "initWithSoftMemoryLimit:frameCapacity:framesPerSecond:minimumGapDuration:coaelscingEpsilon:minimumPrepareInterval:maximumRenderInterval:"
- "initWithSoftMemoryLimit:frameCapacity:framesPerSecond:minimumGapDuration:coaelscingEpsilon:minimumPrepareInterval:maximumRenderInterval:surfacePoolSize:surfaceOverallocationFactor:"
- "initWithSpecifier:"
- "initWithStartDate:duration:"
- "initWithStartDate:endDate:"
- "initWithStartDate:updates:nextUpdatesStart:"
- "initWithState:"
- "initWithStateMachineOldBacklightState:eventPreviousBacklightState:eventNewBacklightState:"
- "initWithSuiteName:"
- "initWithSuppressionEvent:"
- "initWithTarget:visualState:presentationDate:"
- "initWithTimestamp:environmentIdentifiers:reasonEnded:sessionFramesHistogram:totalPreparationDuration:accumulatedLayoutDuration:accumulatedRenderDuration:preventedSleepDuration:didFailToRender:timedOutEnvironmentCount:"
- "initWithTimestamp:environmentIdentifiers:shortestInterval:averageInterval:longestInterval:completionDuration:didReset:timedOutCount:"
- "initWithTimestamp:reason:source:didClearDateSpecifiers:wasReset:invalidatedFramesHistogram:environmentIdentifiers:"
- "initWithTotalCount:averagePresentationTimeFromNow:medianPresentationTimeFromNow:presentationTimeHistogram:intervalUntilFirstFrame:presentationDuration:memoryUsage:averageMemoryUsage:medianMemoryUsage:memoryUsageHistogram:lowestAPL:averageAPL:medianAPL:highestAPL:lowestAPLDimming:averageAPLDimming:medianAPLDimming:highestAPLDimming:"
- "initWithTriggerEvent:withInitialSpecifier:"
- "initWithType:reason:"
- "initWithType:reason:timestamp:"
- "initWithWatchdogDidFireDictionary:"
- "initWithWatchdogProviderDelegate:testables:"
- "initWithWatchdogType:cbDisplayMode:cbFlipbookState:caDisplayState:completedCADisplayState:suppressionServiceActive:flipbookTransparent:deviceSupportsAlwaysOn:deviceSupportsAlwaysOnFlipbook:displayStateClientSupported:backlightDimmedFactor:"
- "initWithWithIdentifier:aggregator:"
- "insertObject:atIndex:"
- "insertions"
- "inspectDiff:"
- "inspectDiff:withContext:"
- "install"
- "integerForKey:"
- "interface"
- "intersectionWithDateInterval:"
- "intervalUntilFirstFrame"
- "intervalWithPresentationInterval:previousPresentationDate:shouldReset:environment:"
- "invalidate:"
- "invalidateAggregatedAssertion:"
- "invalidateAllTimelinesForReason:"
- "invalidateAtRequestDate:expectedFidelity:invalidationBlock:"
- "invalidateAtRequestDate:forEnvironment:invalidationBlock:"
- "invalidateContentForReason:"
- "invalidateIndividualAssertion:"
- "invalidateOnGlassFlipbookFrame"
- "invalidateWithError:"
- "invalidatedEntryCount"
- "invalidatedFramesHistogram"
- "is1HzFlipbookForAssertion"
- "isActive"
- "isAlreadyAtDesiredState"
- "isAlwaysOnDisabledByAssertion"
- "isAlwaysOnEnabled"
- "isAlwaysOnEnabledForEnvironment"
- "isAlwaysOnSettingEnabled"
- "isAlwaysOnSuppressed"
- "isAnimated"
- "isAnimatedTransition"
- "isAnimating"
- "isAvailable"
- "isAwakeOrAbortingSleep"
- "isBeforeDate:"
- "isClientActive"
- "isComplete"
- "isCompleted"
- "isCurrentRBSAssertion:"
- "isDelegateActive"
- "isDesiredDisplayMode:"
- "isDesiredState:"
- "isDirectRamp"
- "isEmpty"
- "isEnvironmentTransitionAnimated"
- "isEnvironmentTransitionAnimatedToState:fromPreviousState:"
- "isEqual"
- "isEqual:"
- "isEqualToArray:"
- "isEqualToDate:"
- "isEqualToString:"
- "isEqualToVisualState:presentationDate:"
- "isEssentiallyEqualToVisualState:"
- "isFlipbookDisabled"
- "isFlipbookPowerSavingEnabled"
- "isFlipbookTransparent"
- "isForeground"
- "isFullyCompleted"
- "isGlobal1HzFlipbook"
- "isGlobalHighLuminanceAlwaysOn"
- "isGlobalUnrestrictedFramerate"
- "isHighLuminanceAlwaysOn"
- "isHostProcess"
- "isIdle"
- "isInvalidated"
- "isInverted"
- "isKindOfClass:"
- "isLiveUpdating"
- "isLocal"
- "isMemberOfClass:"
- "isNullOperationAllowed"
- "isObserving"
- "isObservingActivatingWithEvent"
- "isObservingDeactivatingWithEvent"
- "isObservingDidChangeAlwaysOnEnabled"
- "isObservingDidCompleteUpdateToState"
- "isObservingEventsArray"
- "isObservingPerformingEvent"
- "isOnStandby"
- "isOneHzFlipBook"
- "isPotentialHang"
- "isProxy"
- "isRetainingSurface"
- "isRunning"
- "isScheduled"
- "isShowingBlankingWindow"
- "isSleepImminent"
- "isStarted"
- "isStartedButIncomplete"
- "isState:equalToObject:"
- "isSuppressed"
- "isSuppressionServiceActive"
- "isTailspinAvailable"
- "isTouchTargetable"
- "isTransitionForcedUnanimated"
- "isTransitionForcedUnanimatedForSource:"
- "isTransitionForcedUnanimatedToState:fromPreviousState:"
- "isTransitioning"
- "isTransitioningDisplayMode"
- "isTwoPhaseUpdate"
- "isUpdateToDateSpecifier"
- "isUpdatedToBacklightState:"
- "isUpdatingInitialState"
- "isUpdatingPresentation"
- "isUpdatingState"
- "isUpdatingVisualState"
- "isUsingAlwaysOnBrightnessCurve"
- "isUsingPseudoFlipbook"
- "isValid"
- "isValidWithNowDate:"
- "isWaitingwaitingPastFireForCompletionAndTailspin"
- "isWatchdogEnabled"
- "j8/Omm6s1lsmTDFsXjsBfA"
- "keyEnumerator"
- "keywordIDs"
- "last"
- "lastEntryFinalDate"
- "lastEntryInitialDate"
- "lastObject"
- "lastSuppressionEvent"
- "laterDate:"
- "leeway"
- "length"
- "listener:didReceiveConnection:withContext:"
- "listenerWithConfigurator:"
- "local"
- "localAssertionService"
- "localizedDescription"
- "localizedFailureReason"
- "lock_cancelFlipbookFramesForReason:source:didClearDateSpecifiers:wasReset:"
- "lock_completeAllTimelineEntries"
- "lock_delegate"
- "lock_description"
- "lock_displayModeForBacklightState:"
- "lock_setFlipbookPredictiveRenderType"
- "logTelemetryForInvalidation:"
- "logTelemetryForRenderSession:"
- "logTelemetryForRequestDates:"
- "longHeldAssertionWithDescription:activeDuration:timeReleased:"
- "lowestAPL"
- "lowestAPLDimming"
- "machContinuousTimestamp"
- "mach_continuous_time"
- "mainBundle"
- "mainDisplay"
- "mainQueue"
- "main_prepareAndRenderNextFlipbookFrame"
- "markWatchdogDidFire:abortReason:"
- "maskForObservingDidCompleteUpdateToState:observingEventsArray:didChangeAlwaysOnEnabled:activatingWithEvent:deactivatingWithEvent:performingEvent:"
- "medianAPLDimming"
- "medianMemoryUsage"
- "medianPresentationTimeFromNow"
- "memoryUsageHistogram"
- "minimumGapDuration"
- "minusSet:"
- "minute"
- "minuteBoundaryDate"
- "missingAnySpecifiersInDateInterval:forPresentation:"
- "missingIntervalForDateInterval:"
- "missingIntervalsForMinimumInterval:requestInterval:ofPresentation:"
- "model"
- "monitorUsingMainQueue"
- "monitorWithConfiguration:"
- "mutableCopy"
- "nanosecond"
- "newBacklightState"
- "newSpecifierWithMaxFidelity:"
- "newVisualStateWithUpdateFidelity:"
- "nextCount"
- "nextDateAfterDate:matchingComponents:options:"
- "nextObject"
- "nextUpdatesStart"
- "noActivatingMask"
- "noPerformingEventMask"
- "nonInteractiveIdleTimeout"
- "notifyObserversWithBlock:"
- "now"
- "nowObservingWithMask:completion:"
- "null"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithLong:"
- "numberWithLongLong:"
- "numberWithUnsignedInteger:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectEnumerator"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "objectsAtIndexes:"
- "objectsPassingTest:"
- "observeOtherSetting:withBlock:"
- "observeSignificantTimeChangeWithIdentifier:handler:"
- "observeValueForKeyPath:ofObject:change:context:"
- "observerWithObserver:"
- "observesActivation"
- "observesBlankingChanges"
- "observesDeactivation"
- "observesDidUpdateVisualContents"
- "observesPerformingAllEvents"
- "observesUpdateToDisplayMode"
- "onGlassFlipbookFrame"
- "onMain_ensureInactiveEnvSessionCreated"
- "onMain_ensureSessionCreated"
- "onMain_performNextStepInModeTransition"
- "onMain_performNextStepInTransition"
- "onMain_setPresentation:withTargetBacklightState:"
- "oneHzFlipbook"
- "oneHzFlipbookForAssertion"
- "operation"
- "operationForUpdateFromCurrentDisplayMode:toTargetDisplayMode:"
- "operationForUpdateFromCurrentDisplayMode:toTargetDisplayMode:withConfiguration:"
- "osInterfaceProvider"
- "osInterfaceProvider:didCompleteSwitchToCBFlipbookState:withError:"
- "osInterfaceProvider:didCompleteTransitionToCADisplayState:currentState:transitionStatus:"
- "osInterfaceProvider:didCompleteTransitionToCBDisplayMode:withError:"
- "osTimerProvider"
- "panicDelay"
- "panicForWatchdog:withDelay:completion:"
- "pause"
- "pauseAssertion:"
- "pauseOnSystemSleep"
- "payload"
- "payloadSize"
- "peekNextUpdate"
- "pendingBacklightRamp"
- "pendingEventToPerform"
- "pendingOperation"
- "pendingTransitionStateCount"
- "performBacklightRampIfNeededWithDuration:"
- "performBacklightRampIfPendingForReason:"
- "performBacklightRampWithDuration:"
- "performBlockWithSubhostedEnvironments:"
- "performChangeRequest:"
- "performConfigurator:"
- "performDesiredFidelityRequest:"
- "performEvent:"
- "performEvent:withInitialSpecifier:performBacklightRamp:"
- "performFrameSpecifiersRequest:"
- "performFrameSpecifiersRequest:timelines:"
- "performInvalidation"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performUnexpectedSleepRequest:"
- "performWithSubhostedEnvironmentsFromPresentationEntries:block:"
- "performerDelegate"
- "performingEvent:"
- "pid"
- "platformDidDetectSignificantUserInteraction"
- "platformProvider"
- "platformProvider:didChangeAlwaysOnSetting:"
- "platformProviderDidDetectSignificantUserInteraction:"
- "populateEnvironmentStateMachineStruct:"
- "populateEnvironmentStateMachineStruct:machineIsNil:presentation:addingEnvironmentsCount:updatingVisualStateTransitionStates:updatingDateSpecifierTransitionStates:backlightState:previousBacklightState:pendingNotifyBeganUpdatingState:updatingState:updatingPresentation:"
- "populateOperationCompletedMismatchedBacklightStatesStruct:backlightState:targetBacklightState:performEventHistory:didBeginUpdateHistory:didCompleteUpdateHistory:envStateMachineIsNil:envStateMachinePresentation:addingEnvironmentsCount:envStateMachineUpdatingVisualStateTransitionStates:envStateMachineUpdatingDateSpecifierTransitionStates:envStateMachineBacklightState:envStateMachinePreviousBacklightState:envStateMachinePendingNotifyBeganUpdatingState:envStateMachineUpdatingState:envStateMachineUpdatingPresentation:"
- "populatePresentationStruct:withPresentation:"
- "powerSavingEnabled"
- "powerState"
- "predicateMatchingIdentity:"
- "predicateMatchingTarget:"
- "prepareAndRenderFrameSpecifier:"
- "presentWithCompletion:"
- "presentationDatesModel"
- "presentationDuration"
- "presentationEngine:didInvalidateContentForEnvironment:reason:"
- "presentationEngine:didUpdateToCurrentWithSpecifier:"
- "presentationEntryIdentifierFromString:"
- "presentationEntrySupportsAlwaysOn:"
- "presentationInterval"
- "presentationSource"
- "presentationTimeHistogram"
- "preventIdle"
- "preventIdleAndRestartTimerOnInvalidation"
- "preventIdleClearUserInteractionAndRestartTimerOnInvalidation"
- "preventedSleepDuration"
- "previousPresentationDate"
- "previousState"
- "previousVisualState"
- "prewarmEvent:"
- "prewarmForDisplayMode:"
- "processInfo"
- "processName"
- "provider"
- "purgeFlipbook"
- "purgeSpecifiersBefore:"
- "purgeStaleDataForNowDate:"
- "q"
- "q16@0:8"
- "q24@0:8@16"
- "q32@0:8@\"NSDate\"16q24"
- "q32@0:8@16q24"
- "q40@0:8@\"NSDate\"16@\"<BLSHBacklightSceneHostEnvironment>\"24q32"
- "q40@0:8@16@24q32"
- "r^v"
- "r^v16@0:8"
- "radarDescription"
- "radarIsUserInitiated"
- "radarTitle"
- "raise:format:"
- "rampBeginDisplayMode"
- "rampDuration"
- "rampOperation"
- "rawSurface"
- "rawSurfaceForFrameUUID:reply:"
- "reactivateIfPossible"
- "readyToStart"
- "registerAttributeHandler:forAttributeClasses:"
- "registerDefaults:"
- "registerHandlerForService:"
- "registerHandlerForService:provider:"
- "registerHandlersForService:"
- "registerSceneWorkspace:"
- "registerSharedBacklightHost:"
- "registerSharedBacklightHostForTest:"
- "registerSpecifiers:forDateInterval:"
- "registerSpecifiers:forDateInterval:environment:"
- "relativePriority"
- "release"
- "remainingDuration"
- "remoteProcess"
- "removals"
- "removeActionHandler:forScene:"
- "removeAllObjects"
- "removeEnvironmentsObserver:"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObjectsAtIndexes:"
- "removeObjectsInArray:"
- "removeObjectsInRange:"
- "removeObserver:"
- "removeSceneObserver:forSceneIdentityToken:"
- "renderForTime:options:userInfo:onRenderBegin:onRenderComplete:"
- "renderFrameForPresentation:dateSpecifier:onRenderBegin:onRenderComplete:"
- "renderFrameSpecifier:timedOutEnvironments:"
- "renderFramesSession:beganRenderingSpecifier:timedOutEnvironments:"
- "renderFramesSession:didRenderFrame:timedOutEnvironments:"
- "renderFramesSession:failedToRenderSpecifier:error:timedOutEnvironments:"
- "rendered"
- "renderedEntryCount"
- "replaceWithService:"
- "requestDateSpecifiersForDateInterval:previousPresentationDate:shouldReset:completion:"
- "requestDatesOperation:didTimeoutPendingEnvironments:"
- "requestDatesOperation:environment:didProvideSpecifiers:forPresentationInterval:isComplete:"
- "requestTapToRadar:log:completion:"
- "requestTapToRadarNonInteractiveDraft:log:completion:"
- "requestedActivityState"
- "requestedFidelity"
- "requestedFidelityForInactiveContentWithCompletion:"
- "resetAllBudgetsForReason:"
- "resetAllLocalHostBudgetsForReason:"
- "resetBudgetForEnvironment:reason:"
- "resetBudgetForProcess:reason:"
- "resetFutureAndRenderedSpecifiers"
- "resetFutureSpecifiers"
- "resetIgnoredDesignations"
- "resetWatchdogDidFire"
- "respondToActions:forFBScene:"
- "respondsToSelector:"
- "restartAssertionTimeoutTimer:"
- "restartTimer"
- "restartTimerOnInvalidation"
- "resume"
- "resumeAssertion:"
- "resumeDisplayMode:"
- "resumeWithError:"
- "retain"
- "retainCount"
- "retainedMemoryUsage"
- "retainingSurface"
- "runWhenAwakeWithCompletion:"
- "scene:clientDidConnect:"
- "scene:didApplyUpdateWithContext:"
- "scene:didCompleteUpdateWithContext:error:"
- "scene:didPrepareUpdateWithContext:"
- "scene:didReceiveActions:"
- "scene:didUpdateClientSettings:"
- "scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:"
- "scene:didUpdateSettings:"
- "scene:handleActions:"
- "scene:willUpdateSettings:"
- "scene:willUpdateSettings:withTransitionContext:"
- "sceneContentStateDidChange:"
- "sceneContentsAnimationDidComplete"
- "sceneContentsDidUpdate"
- "sceneDidActivate:"
- "sceneDidDeactivate:withContext:"
- "sceneDidDeactivate:withError:"
- "sceneDidInvalidate:"
- "sceneDidInvalidate:environment:"
- "sceneDidInvalidate:withContext:"
- "sceneFromIdentityToken:"
- "sceneIdentityToken"
- "sceneIdentityTokenForEntry:"
- "sceneWillActivate:"
- "sceneWillDeactivate:withContext:"
- "sceneWillDeactivate:withError:"
- "sceneWithIdentityToken:"
- "scheduleWatchdogWithDelegate:explanation:timeout:"
- "scheduleWithFireInterval:leewayInterval:queue:handler:"
- "scheduleWithTimeout:"
- "scheduledTimerWithIdentifier:interval:leewayInterval:handler:"
- "scheduledWakingTimerWithIdentifier:interval:leewayInterval:handler:"
- "second"
- "secondsBucketCount"
- "secondsFidelity"
- "secondsFidelityThreshold"
- "self"
- "serial"
- "serverWithFlipbookDiagnosticsProvider:"
- "serverWithLocalAssertionService:"
- "serverWithLocalBacklightProxy:"
- "service:didAcquireAssertion:"
- "service:didCancelAssertion:withError:"
- "service:didPauseAssertion:"
- "service:didRestartTimeoutTimerForAssertion:"
- "service:didResumeAssertion:"
- "service:failedToAcquireAssertion:withError:"
- "service:willCancelAssertion:"
- "serviceClass"
- "serviceClass:relativePriority:"
- "serviceDidAcquire"
- "serviceDidCancelWithError:"
- "serviceDidPause"
- "serviceDidResume"
- "serviceFailedToAcquireWithError:"
- "serviceInitializing:"
- "serviceQuality"
- "serviceWillCancel"
- "serviceWithOSInterfaceProvider:localOnly:"
- "serviceWithPlatformProvider:osInterfaceProvider:inactiveBudgetPolicy:localAssertionService:localOnly:"
- "session"
- "sessionDidEnd"
- "sessionFramesHistogram"
- "sessionWithPresentation:"
- "set"
- "set1HzFlipbook:"
- "set1HzFlipbookForAssertion:"
- "setAbandonedInProgressOperation:"
- "setAbortContext:"
- "setAbortReasonString:"
- "setAbortTimestamp:"
- "setAcquireWaitsToAbortSleepImminent:"
- "setAcquireWaitsToAbortSleepRequested:"
- "setActions:"
- "setActive:"
- "setAlwaysFillFlipbook:"
- "setAlwaysOnContentIs1hz:"
- "setAlwaysOnDisabledByAssertion:"
- "setAlwaysOnEnabledForEnvironment:"
- "setAlwaysOnSession:"
- "setAlwaysOnSettingEnabled:"
- "setAlwaysOnSuppressed:"
- "setAmendSceneSettingsDelegate:"
- "setAninmationPropertiesWithPlatformProvider:"
- "setArray:"
- "setAttachments:"
- "setAttentionAwarenessClient:"
- "setAttentionAwarenessConfiguration:"
- "setAttentionLostTimeoutDictionary:"
- "setBacklightDimmedFactor:"
- "setBacklightDimmingDuration:"
- "setBacklightFadeInDuration:"
- "setBacklightFadeOutDuration:"
- "setBacklightState:"
- "setBuildVersion:"
- "setBundleID:"
- "setCATransitionsDelayForTesting:"
- "setCBTransitionsDelayForTesting:"
- "setCacheFlipbook:"
- "setCacheFlipbookOnDisplayWake:"
- "setCachesFramesOnExit:"
- "setCommitOnWakeMeasurementDisabled:"
- "setCompleted:"
- "setCompletionDelegate:"
- "setComponentID:"
- "setComponentName:"
- "setComponentVersion:"
- "setConfiguration:shouldReset:error:"
- "setContextId:"
- "setDate:"
- "setDateSpecifier:"
- "setDebugLogsEnabled:"
- "setDefaultBacklightProxy:"
- "setDefaultService:"
- "setDelegate:"
- "setDevice:"
- "setDidCompleteAnimation:"
- "setDidUpdateInitialState:"
- "setDisplayMode:"
- "setDisplayMode:withRampDuration:"
- "setDisplayReason:"
- "setDisplayStateDelegate:"
- "setDomain:"
- "setDuration:"
- "setEnabledByDefault:"
- "setEventHandlerWithQueue:block:"
- "setEventMask:"
- "setExplanation:"
- "setFailureSource:"
- "setFlipbook:"
- "setFlipbookDisabled:"
- "setFlipbookSpecification:"
- "setFlipbookTransparent:"
- "setGlobal1HzFlipbook:"
- "setGlobalCacheFlipbookOnDisplayWake:"
- "setGlobalHighLuminanceAlwaysOn:"
- "setGlobalUnrestrictedFramerate:"
- "setHangDetected:"
- "setHighLuminanceAlwaysOn:"
- "setIdentifier:"
- "setIdleTimeout:"
- "setIdleTimeout:shouldReset:"
- "setIgnoreWatchdogAborts:"
- "setInactiveSession:"
- "setInterface:"
- "setInterfaceTarget:"
- "setInvalidated:"
- "setInvalidationHandler:"
- "setInverted:"
- "setIsAnimatedTransition:"
- "setIsHostProcess:"
- "setIsNullOperationAllowed:"
- "setIsPotentialHang:"
- "setKeywordIDs:"
- "setLeeway:"
- "setLiveUpdating:"
- "setMaximumMemoryUsageForDiagnostics:"
- "setNext:"
- "setNonInteractiveIdleTimeout:"
- "setOSInterfaceProvider:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOnStandby:"
- "setOneHzFlipBook:"
- "setPendingOperation:"
- "setPerformerDelegate:"
- "setPowerSavingEnabled:"
- "setPredicates:"
- "setPresentation:"
- "setPresentation:withCompletion:"
- "setPresentation:withTargetBacklightState:"
- "setPresentationDate:"
- "setPresentationDatesModel:"
- "setPresentationSource:"
- "setPresentationWithFBScenes:flipbookContext:completion:"
- "setPrevious:"
- "setProcessName:"
- "setRadarDescription:"
- "setRadarIsUserInitiated:"
- "setRadarTitle:"
- "setReadyToStart:"
- "setReplacedSceneUpdate:"
- "setRunningBoardAssertionDisabled:"
- "setSafeToUnblank:"
- "setSecond:"
- "setService:"
- "setServiceQuality:"
- "setSessionProvider:"
- "setSharedProvider:"
- "setShouldFaultOnFailureToAcquire:"
- "setShouldNotifyOfUnidle:"
- "setShouldNotifyOfUnidleChanged:"
- "setShowTTRAlert:"
- "setShowingBlankingWindow:fadeDuration:"
- "setSleepImminentAbortReason"
- "setSleepImminentSinceScheduled:"
- "setSleepMonitorAggregateState:"
- "setSpecifier:"
- "setStarted:"
- "setStateDescriptor:"
- "setSuppressionSupported:"
- "setSuspended:"
- "setTargetBacklightState:"
- "setTargetIdleState:"
- "setTargetQueue:"
- "setTelemetryDelegate:"
- "setTimeOfIssue:"
- "setTimeout:"
- "setTimerIdentifier:"
- "setToState:"
- "setTransitionForcedUnanimated:environmentTransitionAnimated:"
- "setTtrDisplayReason:"
- "setTtrPromptHeader:"
- "setTtrPromptMessage:"
- "setUnrestrictedFramerateUpdates:"
- "setUpdateHandler:"
- "setUpdatedInitialState:"
- "setUpdater:"
- "setUsePseudoFlipbook:"
- "setUserInitiated:"
- "setUserObject:"
- "setValue:forKey:"
- "setValues:"
- "setVisualState:presentationDate:"
- "setWaitingwaitingPastFireForCompletionAndTailspin:waitForWatchdogCompletion:"
- "setWantsTransform:"
- "setWatchdogEnabled:"
- "setWithArray:"
- "setWithObject:"
- "settings"
- "setupService"
- "sharedBacklight"
- "sharedBacklightHost"
- "sharedBacklightHost != nil"
- "sharedFormatter"
- "sharedHighPriorityQueue"
- "sharedInstance"
- "sharedProvider"
- "sharedService"
- "sharedSystemActivityFactory"
- "sharedTapToRadarManager"
- "sharedTelemetrySource"
- "shortLoggingString"
- "shouldFaultOnFailureToAcquire"
- "shouldIgnoreDesignation:"
- "shouldNotifyOfUnidle"
- "shouldNotifyOfUnidleChanged"
- "showBlankingWindow:withFadeDuration:"
- "showTTRAlert"
- "showWatchdogDidFireAlert:"
- "showingBlankingWindow"
- "signalUserActivityOccurred"
- "sleepImminentSinceScheduled"
- "sleepImminentWhenScheduled"
- "sleepMonitorAggregateState"
- "sortByInsertionOrder"
- "sortedArrayUsingComparator:"
- "sortedArrayUsingSelector:"
- "sourceModel"
- "specification"
- "specifierCount"
- "specifierForDate:"
- "specifierForPresentationDate:"
- "specifierWithPresentationDate:fidelity:environment:"
- "specifierWithPresentationDate:fidelity:environment:userObject:"
- "specifierWithPresentationDate:specifiers:"
- "specifiers"
- "standardUserDefaults"
- "startDate"
- "startFlipbookAndEnsureCurrent"
- "startLocalOnlyServiceWithConfiguration:"
- "startService"
- "startServiceWithPlatformProvider:"
- "startServiceWithPlatformProvider:localOnly:"
- "startSuppressionServiceWithHandler:"
- "startSuppressionUpdatesToQueue:withHandler:"
- "startWatchdog"
- "startWatchdogTimer"
- "startedButIncomplete"
- "startedTime"
- "stateControl"
- "stateDataWithHints:"
- "stateHash:"
- "stateMachineOldBacklightState"
- "statesForPredicate:withDescriptor:error:"
- "stillTrackingAfterPurgingStaleDataForNowDate:"
- "stopForReason:"
- "stopRetainingSurface"
- "stopService"
- "stopSuppressionUpdates"
- "stopWatchdog"
- "stringByAppendingPathComponent:"
- "stringByAppendingString:"
- "stringFromByteCount:"
- "stringWithFormat:"
- "strongToWeakObjectsMapTable"
- "subHostedHostEnvironments"
- "substringToIndex:"
- "superclass"
- "supported"
- "supportsFlipbookState"
- "suppressForReason:"
- "suppression"
- "suppressionSupported"
- "surface"
- "surfaceForFrameUUID:reply:"
- "suspendForReason:"
- "suspendWithError:"
- "switchToFlipbookState:"
- "switchToFlipbookState:error:"
- "systemSleepAction:performWithCompletion:"
- "systemSleepAction:systemWillWakeForReason:"
- "systemSleepMonitor"
- "systemSleepMonitor:prepareForSleepWithCompletion:"
- "systemSleepMonitor:sleepRequestedWithResult:"
- "systemSleepMonitorDidWakeFromSleep:"
- "systemSleepMonitorSleepRequestAborted:"
- "systemSleepMonitorWillWakeFromSleep:"
- "systemWillWakeForReason:"
- "targetBacklightState"
- "targetDisplayMode"
- "targetIdleState"
- "targetWithPid:"
- "targetWithProcessIdentity:"
- "taskState"
- "telemetryDataWithEndTime:"
- "telemetryDataWithEndTime:reasonEnded:preventedSleepDuration:"
- "telemetryDelegate"
- "testing"
- "timeIntervalFromLastEntryToDate:"
- "timeIntervalSinceDate:"
- "timeIntervalSinceNow"
- "timeIntervalSinceReferenceDate"
- "timeOfIssue"
- "timeRemaining"
- "timeStamp"
- "timelineEntry"
- "timelineWithEntries:identifier:configure:"
- "timelinesForDateInterval:previousPresentationDate:localHostEnvironment:shouldReset:completion:"
- "timeout"
- "timeoutTimerFiredForSpecifier:"
- "timerFired"
- "timerIdentifier"
- "tokenWithObserver:sceneIdentityToken:"
- "totalCount"
- "touchLock"
- "transitionContextClass"
- "transitionState:didBeginUpdateToBacklightState:visualState:"
- "transitionState:didCompleteUpdateToBacklightState:visualState:"
- "transitionState:didUpdateToDateSpecifier:"
- "transitionToCADisplayState:"
- "transitionToDisplayMode:withDuration:"
- "transitionToDisplayMode:withDuration:error:"
- "transitionToDisplayState:withCompletion:"
- "transitioningDisplayMode"
- "triggerEvent"
- "ttrDisplayReason"
- "ttrPromptHeader"
- "ttrPromptMessage"
- "typeForEntry:"
- "uninstall"
- "unionSet:"
- "unrestrictedFramerateUpdates"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "unsignedLongValue"
- "updateAllEnvironmentsInPresentation"
- "updateEnvironment:"
- "updateFidelity"
- "updateForNewValue:"
- "updateOperation"
- "updateRemovedEnvironmentsToActiveOn"
- "updateSettingsWithBlock:"
- "updateSettingsWithTransitionBlock:"
- "updateState:"
- "updateToBacklightState:forEvent:touchTargetable:presentationDate:sceneUpdate:performBacklightRamp:"
- "updateToDateSpecifier:"
- "updateToDateSpecifier:sceneContentsUpdated:"
- "updateToSpecifier:"
- "updateToTarget:touchTargetable:presentationDate:sceneUpdate:requestedFidelity:"
- "updateToVisualState:presentationDateSpecifier:"
- "updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:"
- "updatedEnvironmentWithDelta:backlightSceneUpdate:"
- "updater"
- "updaterDidBeginUpdateToBacklightState:"
- "updaterDidUpdateToPresentation:"
- "updatesAfterSpecifier:coalesceFirstUpdateToNowDate:plusRenderEarlyEpsilon:untilGapOverDuration:coaelscingEpsilon:maximumUpdates:lastValidDate:forPresentation:environmentFilter:"
- "updatingDateSpecifierTransitionStates"
- "updatingInitialState"
- "updatingVisualStateTransitionStates"
- "useAlwaysOnBrightnessCurve"
- "useAlwaysOnBrightnessCurve:withRampDuration:"
- "userActivityOccured"
- "userInfo"
- "userInitiated"
- "uuid"
- "v124@0:8^{?=IiiI[5{?=Ib1iiiQ}]I[5{?=Ib1IiIQ}]I[5{?=Ib1IiIQ}]{?=b1{?=b1b1b1IIIII}I{?=b1Ib1b1b1}{?=b1Ib1b1b1}{?=b1Ib1b1b1}{?=b1Ib1b1b1}I{?=b1Ib1b1b1}{?=b1Ib1b1b1}{?=b1Ib1b1b1}{?=b1Ib1b1b1}iib1b1b1}}16q24q32@40@48@56B64@68i76@80@88q96q104B112B116B120"
- "v16@0:8"
- "v16@?0@\"<BSServiceConnectionInternalConfiguring>\"8"
- "v16@?0@\"<BSServiceConnectionListenerConfiguring>\"8"
- "v16@?0@\"BSServiceConnection<BSServiceConnectionContext>\"8"
- "v20@0:8B16"
- "v20@0:8f16"
- "v24@0:8@\"<BLSAssertionService>\"16"
- "v24@0:8@\"<BLSAssertionServiceResponding>\"16"
- "v24@0:8@\"<BLSBacklightStateObserving>\"16"
- "v24@0:8@\"<BLSDisplayStateDelegate>\"16"
- "v24@0:8@\"<BLSHBacklightHostObserving>\"16"
- "v24@0:8@\"<BLSHBacklightHostTelemetryDelegate>\"16"
- "v24@0:8@\"<BLSHBacklightPlatformProvider>\"16"
- "v24@0:8@\"<BLSHBacklightPlatformProviderObserver>\"16"
- "v24@0:8@\"<BLSHBacklightSceneHostEnvironmentObserver>\"16"
- "v24@0:8@\"<BLSHOSInterfaceProviding>\"16"
- "v24@0:8@\"<BLSHUserIdleProviding>\"16"
- "v24@0:8@\"<BLSHUserIdleProvidingDelegate>\"16"
- "v24@0:8@\"<NSObject>\"16"
- "v24@0:8@\"BLSAssertionIdentifier\"16"
- "v24@0:8@\"BLSBacklightChangeEvent\"16"
- "v24@0:8@\"BLSDesiredFidelityRequest\"16"
- "v24@0:8@\"BLSFrameSpecifiersRequest\"16"
- "v24@0:8@\"BLSHBacklightInactiveEnvironmentSession\"16"
- "v24@0:8@\"BLSHIndividualSystemActivityAssertion\"16"
- "v24@0:8@\"BLSHPresentationDateSpecifier\"16"
- "v24@0:8@\"BLSHService\"16"
- "v24@0:8@\"FBScene\"16"
- "v24@0:8@\"NSDate\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"SWSystemSleepMonitor\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"BLSHSuppressionEvent\">16"
- "v24@0:8@?<v@?q>16"
- "v24@0:8B16B20"
- "v24@0:8Q16"
- "v24@0:8^{?=b1{?=b1b1b1IIIII}I{?=b1Ib1b1b1}{?=b1Ib1b1b1}{?=b1Ib1b1b1}{?=b1Ib1b1b1}I{?=b1Ib1b1b1}{?=b1Ib1b1b1}{?=b1Ib1b1b1}{?=b1Ib1b1b1}iib1b1b1}16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v25@0:8{?=b1b1b1b1b1}16@\"BLSBacklightSceneUpdate\"17"
- "v25@0:8{?=b1b1b1b1b1}16@17"
- "v28@0:8@\"<BLSBacklightStateObservable>\"16B24"
- "v28@0:8@\"<BLSHBacklightPlatformProvider>\"16B24"
- "v28@0:8@\"<BLSHBacklightSceneHostEnvironment>\"16B24"
- "v28@0:8@16B24"
- "v28@0:8B16@20"
- "v28@0:8B16d20"
- "v28@0:8d16B24"
- "v32@0:8@\"<BLSBacklightStateObservable>\"16@\"BLSBacklightChangeEvent\"24"
- "v32@0:8@\"<BLSHBacklightSceneHostEnvironment>\"16@\"NSString\"24"
- "v32@0:8@\"<BLSSceneActionHandler>\"16@\"FBScene\"24"
- "v32@0:8@\"<NSObject><NSCopying>\"16@\"<BLSHBacklightSceneHostEnvironment>\"24"
- "v32@0:8@\"BLSAlwaysOnDateSpecifier\"16@?<v@?>24"
- "v32@0:8@\"BLSAlwaysOnDateSpecifier\"16q24"
- "v32@0:8@\"BLSBacklightSceneVisualState\"16@\"BLSAlwaysOnDateSpecifier\"24"
- "v32@0:8@\"BLSHAlwaysOnPresentationEngine\"16@\"BLSHPresentationDateSpecifier\"24"
- "v32@0:8@\"BLSHBacklightDisplayStateMachine\"16q24"
- "v32@0:8@\"BLSHBacklightEnvironmentStateMachine\"16@\"BLSHBacklightEnvironmentPresentation\"24"
- "v32@0:8@\"BLSHBacklightEnvironmentStateMachine\"16@\"BLSHPresentationDateSpecifier\"24"
- "v32@0:8@\"BLSHBacklightEnvironmentStateMachine\"16q24"
- "v32@0:8@\"BLSHBacklightInactiveEnvironmentSession\"16@\"BLSHBacklightEnvironmentPresentation\"24"
- "v32@0:8@\"BLSHBacklightInactiveEnvironmentSession\"16q24"
- "v32@0:8@\"BLSHDateSpecifierModel\"16@\"<BLSHBacklightSceneHostEnvironment>\"24"
- "v32@0:8@\"BLSHEngineRequestDatesOperation\"16@\"NSArray\"24"
- "v32@0:8@\"BLSHEnvironmentTransitionState\"16@\"BLSAlwaysOnDateSpecifier\"24"
- "v32@0:8@\"BLSHIndividualSystemActivityAssertion\"16@?<v@?B@\"NSError\"@\"<SWSystemActivityAcquisitionDetails>\">24"
- "v32@0:8@\"BLSHOnSystemSleepAction\"16@\"NSString\"24"
- "v32@0:8@\"BLSHOnSystemSleepAction\"16@?<v@?>24"
- "v32@0:8@\"FBScene\"16@\"FBSSceneTransitionContext\"24"
- "v32@0:8@\"FBScene\"16@\"FBSSceneUpdate\"24"
- "v32@0:8@\"FBScene\"16@\"FBSceneClientHandle\"24"
- "v32@0:8@\"FBScene\"16@\"FBSceneUpdateContext\"24"
- "v32@0:8@\"FBScene\"16@\"NSError\"24"
- "v32@0:8@\"FBScene\"16@\"NSSet\"24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"B>24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSObject<OS_xpc_object>\"@\"NSError\">24"
- "v32@0:8@\"RBSProcessIdentity\"16@\"NSString\"24"
- "v32@0:8@\"SWSystemSleepMonitor\"16@?<@\"SWPreventSystemSleepAssertion\"@?B@\"NSString\">24"
- "v32@0:8@\"SWSystemSleepMonitor\"16@?<v@?>24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16q24"
- "v32@0:8^{?=b1b1b1IIIII}16@24"
- "v32@0:8d16@?24"
- "v32@0:8d16@?<v@?B@\"NSError\"@\"<SWSystemActivityAcquisitionDetails>\">24"
- "v32@0:8q16@\"NSError\"24"
- "v32@0:8q16@24"
- "v32@0:8q16@?24"
- "v32@0:8q16d24"
- "v32@?0@\"NSArray\"8@\"<BLSHAssertionAttributeHandler>\"16^B24"
- "v36@0:8B16@20@28"
- "v40@0:8@\"<BLSBacklightStateObservable>\"16q24@\"BLSBacklightChangeEvent\"32"
- "v40@0:8@\"<BLSHBacklightHostObservable>\"16q24@\"BLSBacklightChangeEvent\"32"
- "v40@0:8@\"<BLSHBacklightHostObservable><BLSBacklightChangeRequestable>\"16q24@\"BLSBacklightChangeEvent\"32"
- "v40@0:8@\"<BLSHBacklightOSInterfaceProviding>\"16q24@\"NSError\"32"
- "v40@0:8@\"BLSHAlwaysOnPresentationEngine\"16@\"<BLSHBacklightSceneHostEnvironment>\"24@\"NSString\"32"
- "v40@0:8@\"BLSHEngineRenderFlipbookSession\"16@\"<BLSHRenderedFlipbookFrame>\"24@\"NSArray\"32"
- "v40@0:8@\"BLSHEngineRenderFlipbookSession\"16@\"BLSHPresentationDateSpecifier\"24@\"NSArray\"32"
- "v40@0:8@\"BLSHEnvironmentTransitionState\"16q24@\"BLSBacklightSceneVisualState\"32"
- "v40@0:8@\"BSServiceConnectionListener\"16@\"BSServiceConnection<BSServiceConnectionHost>\"24@\"<BSXPCDecoding>\"32"
- "v40@0:8@\"FBScene\"16@\"FBSMutableSceneSettings\"24@\"FBSSceneTransitionContext\"32"
- "v40@0:8@\"FBScene\"16@\"FBSceneUpdateContext\"24@\"NSError\"32"
- "v40@0:8@\"NSArray\"16@\"<BLSAssertionServiceResponding>\"24@\"<BLSHAssertionAttributeHandlerService>\"32"
- "v40@0:8@\"NSDate\"16@\"<BLSHBacklightSceneHostEnvironment>\"24@?<v@?>32"
- "v40@0:8@\"NSDate\"16q24@?<v@?>32"
- "v40@0:8@\"NSString\"16d24@?<v@?B>32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@?24@?32"
- "v40@0:8@16d24@?32"
- "v40@0:8@16q24@32"
- "v40@0:8@16q24@?32"
- "v40@0:8d16@\"NSString\"24@?<v@?>32"
- "v40@0:8d16@24@?32"
- "v44@0:8@\"NSDateInterval\"16@\"NSDate\"24B32@?<v@?@\"NSDateInterval\"@\"NSArray\">36"
- "v44@0:8@16@24B32@?36"
- "v44@0:8Q16^v24I32@\"NSString\"36"
- "v44@0:8Q16^v24I32@36"
- "v48@0:8@\"<BLSBacklightStateObservable>\"16q24@\"NSArray\"32@\"NSArray\"40"
- "v48@0:8@\"<BLSHBacklightHostObservable>\"16q24@\"NSArray\"32@\"NSArray\"40"
- "v48@0:8@\"<BLSHBacklightOSInterfaceProviding>\"16q24q32q40"
- "v48@0:8@\"BLSHBacklightEnvironmentPresentation\"16@\"BLSHPresentationDateSpecifier\"24@?<v@?>32@?<v@?@\"<BLSHRenderedFlipbookFrame>\"@\"NSError\">40"
- "v48@0:8@\"BLSHEngineRenderFlipbookSession\"16@\"BLSHPresentationDateSpecifier\"24@\"NSError\"32@\"NSArray\"40"
- "v48@0:8@\"FBScene\"16@\"FBSSceneClientSettingsDiff\"24@\"FBSSceneClientSettings\"32@\"FBSSceneTransitionContext\"40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32^v40"
- "v48@0:8@16@24@?32@?40"
- "v48@0:8@16@24d32d40"
- "v48@0:8@16@?24@32@?40"
- "v48@0:8@16Q24d32d40"
- "v48@0:8@16q24@32@40"
- "v48@0:8@16q24q32q40"
- "v52@0:8@\"BLSHEngineRequestDatesOperation\"16@\"<BLSHBacklightSceneHostEnvironment>\"24@\"NSArray\"32@\"NSDateInterval\"40B48"
- "v52@0:8@16@24@32@40B48"
- "v52@0:8@16@24@32B40@?44"
- "v56@0:8@\"<BLSHBacklightHostObservable>\"16q24q32@\"NSArray\"40@\"NSArray\"48"
- "v56@0:8@16q24q32@40@48"
- "v60@0:8q16@24B32@36@44@?52"
- "v72@0:8@\"BLSBacklightSceneVisualState\"16@\"BLSAlwaysOnDateSpecifier\"24B32@\"BLSBacklightChangeEvent\"36B44@?<v@?>48@?<v@?d>56@?<v@?>64"
- "v72@0:8@16@24B32@36B44@?48@?56@?64"
- "v72@0:8@16@24d32d40@48@56Q64"
- "v84@0:8^{?=b1{?=b1b1b1IIIII}I{?=b1Ib1b1b1}{?=b1Ib1b1b1}{?=b1Ib1b1b1}{?=b1Ib1b1b1}I{?=b1Ib1b1b1}{?=b1Ib1b1b1}{?=b1Ib1b1b1}{?=b1Ib1b1b1}iib1b1b1}16B24@28i36@40@48q56q64B72B76B80"
- "validAtDate:"
- "validateAndChargeFutureSpecifier:nextSpecifier:expectedFidelity:"
- "validateAndChargeFutureSpecifier:nextSpecifier:forEnvironment:"
- "valueForKey:"
- "valueForKeyPath:"
- "waitForBacklightDisplayMode:"
- "waitForBacklightDisplayModePassingTest:"
- "waitForBacklightState:"
- "waitForBacklightStatePassingTest:"
- "waitForBlanked"
- "waitForUnblanked"
- "waitWithCompletion:"
- "waiterWithIdentifier:osInterfaceProvider:"
- "waitingPastFireForCompletionAndTailspinAbortParams"
- "wakeWithCompletion:"
- "wakerWithIdentifier:osInterfaceProvider:"
- "wantsPanic"
- "wantsStateUpdateToActiveAfterRemovalFromPresentation"
- "wantsSuppression"
- "wantsWaitPastFireForCompletionAndTailspin"
- "wasSleepImminentWhenScheduled"
- "wasTransitioning"
- "watchdogEnabled"
- "watchdogTimerFired:"
- "willBeginRenderSession:"
- "willCancelAssertion:"
- "willEndRenderSession:"
- "withLock:"
- "writeTailspinForWatchdog:completion:"
- "writeTailspinLogWithCompletion:"
- "zone"
- "{?=\"sequenceNumber\"i\"caDisplayState\"q\"phase\"q\"startTimestamp\"Q}"
- "{?=\"sequenceNumber\"i\"cbDisplayMode\"q\"previousCBDisplayMode\"q\"duration\"d\"fullDuration\"d\"startSeconds\"d\"effectiveStartSeconds\"d\"phase\"q\"shouldWait\"B}"
- "{?=\"sequenceNumber\"i\"cbFlipbookState\"q\"phase\"q\"startTimestamp\"Q}"
- "{?=\"sequenceNumber\"i\"displayMode\"q\"previousDisplayMode\"q\"duration\"d\"startSeconds\"d\"phase\"q}"
- "{?=b1b1b1}24@0:8@16"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "\xf01"
- "\xf0\xf0\x91"
- "\xf1"

```
