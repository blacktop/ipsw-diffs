## BacklightServicesHost

> `/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`

```diff

-4.5.3.0.0
-  __TEXT.__text: 0x8617c
-  __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_methlist: 0x798c
+5.0.55.0.0
+  __TEXT.__text: 0x88a40
+  __TEXT.__auth_stubs: 0xb10
+  __TEXT.__objc_methlist: 0x7bcc
   __TEXT.__const: 0x3b8
-  __TEXT.__gcc_except_tab: 0x10b0
-  __TEXT.__cstring: 0x66f0
-  __TEXT.__oslogstring: 0xf51b
-  __TEXT.__ustring: 0x2fe
-  __TEXT.__unwind_info: 0x21a0
-  __TEXT.__objc_classname: 0x1fc5
-  __TEXT.__objc_methname: 0x11518
-  __TEXT.__objc_methtype: 0x42c5
-  __TEXT.__objc_stubs: 0x9f40
-  __DATA_CONST.__got: 0x768
-  __DATA_CONST.__const: 0x2500
-  __DATA_CONST.__objc_classlist: 0x550
+  __TEXT.__gcc_except_tab: 0x1090
+  __TEXT.__cstring: 0x69db
+  __TEXT.__oslogstring: 0xfac8
+  __TEXT.__ustring: 0x328
+  __TEXT.__unwind_info: 0x21d8
+  __TEXT.__objc_classname: 0x2004
+  __TEXT.__objc_methname: 0x11d05
+  __TEXT.__objc_methtype: 0x43e9
+  __TEXT.__objc_stubs: 0xa2a0
+  __DATA_CONST.__got: 0x758
+  __DATA_CONST.__const: 0x25c8
+  __DATA_CONST.__objc_classlist: 0x560
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x2a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3090
-  __DATA_CONST.__objc_superrefs: 0x458
+  __DATA_CONST.__objc_selrefs: 0x31a0
+  __DATA_CONST.__objc_superrefs: 0x460
   __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__auth_got: 0x560
-  __AUTH_CONST.__const: 0xb40
-  __AUTH_CONST.__cfstring: 0x6300
-  __AUTH_CONST.__objc_const: 0x138c8
+  __AUTH_CONST.__auth_got: 0x598
+  __AUTH_CONST.__const: 0xba0
+  __AUTH_CONST.__cfstring: 0x6520
+  __AUTH_CONST.__objc_const: 0x13d38
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0xe20
+  __AUTH.__objc_data: 0xf00
+  __DATA.__objc_ivar: 0xe60
   __DATA.__data: 0x1f80
-  __DATA.__bss: 0x90
-  __DATA_DIRTY.__objc_data: 0x3430
+  __DATA.__bss: 0x98
+  __DATA_DIRTY.__objc_data: 0x26c0
   __DATA_DIRTY.__bss: 0xf8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
-  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore

   - /System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
+  - /System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest
   - /System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport

   - /System/Library/PrivateFrameworks/PowerExperience.framework/PowerExperience
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SystemWake.framework/SystemWake
+  - /usr/lib/libIOReport.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 2C3A07AE-6B67-3D59-9DCD-B04E367FC936
-  Functions: 3275
-  Symbols:   11480
-  CStrings:  5744
+  UUID: D68A212A-F9C3-3343-93FA-1B06360139D7
+  Functions: 3355
+  Symbols:   11635
+  CStrings:  5851
 
Symbols:
+ +[BLSBacklightChangeEvent(BacklightServicesHost) defaultIsEnvironmentTransitionAnimatedToState:fromPreviousState:]
+ +[BLSBacklightChangeEvent(BacklightServicesHost) defaultIsTransitionForcedUnanimatedToState:fromPreviousState:]
+ +[BLSBacklightChangeEvent(BacklightServicesHost) defaultTransitionForcedUnanimatedForSource:]
+ +[BLSHPendingUpdateDisplayMode operationForUpdateFromCurrentDisplayMode:toTargetDisplayMode:withConfiguration:]
+ +[BLSHPendingUpdateDisplayMode operationForUpdateFromCurrentDisplayMode:toTargetDisplayMode:withConfiguration:].cold.1
+ +[BLSHPendingUpdateDisplayMode operationForUpdateFromCurrentDisplayMode:toTargetDisplayMode:withConfiguration:].cold.2
+ -[BLSBacklightChangeEvent(BacklightServicesHost) _isEnvironmentTransitionAnimatedWithPlatformProvider:]
+ -[BLSBacklightChangeEvent(BacklightServicesHost) _isTransitionForcedUnanimatedWithPlatformProvider:]
+ -[BLSBacklightChangeEvent(BacklightServicesHost) setAninmationPropertiesWithPlatformProvider:]
+ -[BLSHAlwaysOnPresentationEngine renderFramesSession:beganRenderingSpecifier:timedOutEnvironments:]
+ -[BLSHBacklightEnvironmentStateMachine initWithPresentation:backlightState:delegate:inactiveBudgetPolicy:osTimerProvider:platformProvider:]
+ -[BLSHBacklightEnvironmentStateMachine initWithPresentation:backlightState:delegate:inactiveBudgetPolicy:osTimerProvider:platformProvider:].cold.1
+ -[BLSHBacklightFBSceneHostEnvironment clientAlwaysOnContentIs1hz]
+ -[BLSHBacklightFBSceneHostEnvironment is1HzFlipbookForAssertion]
+ -[BLSHBacklightFBSceneHostEnvironment set1HzFlipbookForAssertion:]
+ -[BLSHBacklightFBSceneHostEnvironment update1HzFlipbookForSettingChange]
+ -[BLSHBacklightFBSceneHostEnvironment updateHost1HzFlipbook]
+ -[BLSHBacklightIdleProvider setTargetIdleState:]
+ -[BLSHBacklightIdleProvider setTargetIdleState:].cold.1
+ -[BLSHBacklightIdleProvider targetIdleState]
+ -[BLSHBacklightInactiveEnvironmentSession hostEnvironment:clientDidUpdateAlwaysOnContentIs1hz:]
+ -[BLSHBacklightOSInterfaceProvider deviceSupportsAlwaysOnFlipbookWatchdog]
+ -[BLSHBacklightTransitionStateMachine isDisplayModeTransitionAnimatedToMode:fromMode:]
+ -[BLSHBaseSceneHostEnvironment clientAlwaysOnContentIs1hz]
+ -[BLSHBaseSceneHostEnvironment is1HzFlipbookForAssertion]
+ -[BLSHBaseSceneHostEnvironment set1HzFlipbookForAssertion:]
+ -[BLSHCriticalAssertDidFailDetails failureSource]
+ -[BLSHCriticalAssertDidFailDetails radarIsUserInitiated]
+ -[BLSHCriticalAssertDidFailDetails setFailureSource:]
+ -[BLSHCriticalAssertDidFailDetails setRadarIsUserInitiated:]
+ -[BLSHDisableFlipbookPowerSavingAttribute description]
+ -[BLSHDisableFlipbookPowerSavingAttribute hash]
+ -[BLSHDisableFlipbookPowerSavingAttribute isEqual:]
+ -[BLSHFlipbook flushLogBuffers:]
+ -[BLSHFlipbook hangDetectorFired:]
+ -[BLSHFlipbook hangDetectorFor:block:]
+ -[BLSHFlipbook hangDetectorFor:block:].cold.1
+ -[BLSHFlipbook hangDetectorFor:block:].cold.2
+ -[BLSHFlipbook logDiagnostics:]
+ -[BLSHFlipbook renderFrameForPresentation:dateSpecifier:onRenderBegin:onRenderComplete:]
+ -[BLSHFlipbook renderFrameForPresentation:dateSpecifier:onRenderBegin:onRenderComplete:].cold.1
+ -[BLSHFlipbookSpecification initWithSoftMemoryLimit:frameCapacity:framesPerSecond:minimumGapDuration:coaelscingEpsilon:minimumPrepareInterval:maximumRenderInterval:surfacePoolSize:surfaceOverallocationFactor:]
+ -[BLSHFlipbookSpecification surfaceAllocationPoolSize]
+ -[BLSHFlipbookSpecification surfaceOverallocationFactor]
+ -[BLSHFlipbookWatchdog .cxx_destruct]
+ -[BLSHFlipbookWatchdog _globalQueue_initializeDCPStats]
+ -[BLSHFlipbookWatchdog _globalQueue_initializeDCPStats].cold.1
+ -[BLSHFlipbookWatchdog _globalQueue_initializeDCPStats].cold.2
+ -[BLSHFlipbookWatchdog _globalQueue_initializeDCPStats].cold.3
+ -[BLSHFlipbookWatchdog _globalQueue_refreshDCPStats:]
+ -[BLSHFlipbookWatchdog _mainQueue_alertFor1hzFlipbookFrameMiss:]
+ -[BLSHFlipbookWatchdog _mainQueue_alertFor1hzFlipbookFrameMiss:].cold.1
+ -[BLSHFlipbookWatchdog dealloc]
+ -[BLSHFlipbookWatchdog enableAlertsUsingDefaults]
+ -[BLSHFlipbookWatchdog initWithOSInterfaceProvider:]
+ -[BLSHFlipbookWatchdog systemSleepMonitorDidWakeFromSleep:]
+ -[BLSHInternalTapToRadarManager requestTapToRadarNonInteractiveDraft:log:completion:]
+ -[BLSHLocalHostSceneEnvironment clientAlwaysOnContentIs1hz]
+ -[BLSHLocalHostSceneEnvironmentUpdater _lock_update1HzFromPresentation:]
+ -[BLSHLocalHostSceneEnvironmentUpdater hostEnvironment:hostDidSet1HzFlipbook:]
+ -[BLSHOSInterfaceProviderAbortContext initWithWatchdogType:cbDisplayMode:cbFlipbookState:caDisplayState:completedCADisplayState:suppressionServiceActive:flipbookTransparent:deviceSupportsAlwaysOn:deviceSupportsAlwaysOnFlipbook:displayStateClientSupported:backlightDimmedFactor:]
+ -[BLSHPendingUpdateDisplayModeConfiguration .cxx_destruct]
+ -[BLSHPendingUpdateDisplayModeConfiguration abandonedInProgressOperation]
+ -[BLSHPendingUpdateDisplayModeConfiguration isAnimatedTranistion]
+ -[BLSHPendingUpdateDisplayModeConfiguration isNullOperationAllowed]
+ -[BLSHPendingUpdateDisplayModeConfiguration pendingOperation]
+ -[BLSHPendingUpdateDisplayModeConfiguration setAbandonedInProgressOperation:]
+ -[BLSHPendingUpdateDisplayModeConfiguration setIsAnimatedTranistion:]
+ -[BLSHPendingUpdateDisplayModeConfiguration setIsNullOperationAllowed:]
+ -[BLSHPendingUpdateDisplayModeConfiguration setPendingOperation:]
+ -[BLSHPseudoFlipbook renderFrameForPresentation:dateSpecifier:onRenderBegin:onRenderComplete:]
+ -[BLSHTapToRadarDescriptor setUserInitiated:]
+ -[BLSHTapToRadarDescriptor userInitiated]
+ GCC_except_table138
+ GCC_except_table139
+ GCC_except_table147
+ GCC_except_table186
+ GCC_except_table187
+ GCC_except_table188
+ GCC_except_table189
+ GCC_except_table30
+ GCC_except_table38
+ GCC_except_table43
+ GCC_except_table65
+ GCC_except_table73
+ GCC_except_table81
+ GCC_except_table83
+ GCC_except_table9
+ _AnalyticsSendEvent
+ _BLSHCheckForCriticalAssertFailureAndPrompt.cold.5
+ _CAFlipBookErrorDomain
+ _CFRelease
+ _DRTailspinRequest
+ _DefaultIsEnvironmentTransitionAnimated
+ _DefaultIsTransitionForcedUnanimated
+ _DefaultIsTransitionForcedUnanimatedForSource
+ _IOReportChannelGetChannelName
+ _IOReportCopyChannelsInGroup
+ _IOReportCreateSamples
+ _IOReportCreateSubscription
+ _IOReportIterate
+ _IOReportSimpleGetIntegerValue
+ _OBJC_CLASS_$_BLSHFlipbookWatchdog
+ _OBJC_CLASS_$_BLSHPendingUpdateDisplayModeConfiguration
+ _OBJC_IVAR_$_BLSHAlwaysOnPresentationEngine._flipbookWatchdog
+ _OBJC_IVAR_$_BLSHAlwaysOnPresentationEngine._lock_preparingToRenderSpecifier
+ _OBJC_IVAR_$_BLSHBacklightEnvironmentStateMachine._platformProvider
+ _OBJC_IVAR_$_BLSHBacklightFBSceneHostEnvironment._lock_1HzFlipbookForAssertion
+ _OBJC_IVAR_$_BLSHBacklightIdleProvider._lock_targetIdleBacklightState
+ _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._deviceSupportsAlwaysOnFlipbookWatchdog
+ _OBJC_IVAR_$_BLSHCriticalAssertDidFailDetails._failureSource
+ _OBJC_IVAR_$_BLSHCriticalAssertDidFailDetails._radarIsUserInitiated
+ _OBJC_IVAR_$_BLSHFlipbookSpecification._surfaceAllocationPoolSize
+ _OBJC_IVAR_$_BLSHFlipbookSpecification._surfaceOverallocationFactor
+ _OBJC_IVAR_$_BLSHFlipbookWatchdog._alertsEnabled
+ _OBJC_IVAR_$_BLSHFlipbookWatchdog._ioReportSubscribedChannels
+ _OBJC_IVAR_$_BLSHFlipbookWatchdog._ioReportSubscription
+ _OBJC_IVAR_$_BLSHFlipbookWatchdog._lastKnown_aodStatsFlipbookMiss
+ _OBJC_IVAR_$_BLSHFlipbookWatchdog._osInterfaceProvider
+ _OBJC_IVAR_$_BLSHFlipbookWatchdog._sleepMonitor
+ _OBJC_IVAR_$_BLSHPendingUpdateDisplayModeConfiguration._abandonedInProgressOperation
+ _OBJC_IVAR_$_BLSHPendingUpdateDisplayModeConfiguration._isAnimatedTranistion
+ _OBJC_IVAR_$_BLSHPendingUpdateDisplayModeConfiguration._isNullOperationAllowed
+ _OBJC_IVAR_$_BLSHPendingUpdateDisplayModeConfiguration._pendingOperation
+ _OBJC_IVAR_$_BLSHTapToRadarDescriptor._userInitiated
+ _OBJC_METACLASS_$_BLSHFlipbookWatchdog
+ _OBJC_METACLASS_$_BLSHPendingUpdateDisplayModeConfiguration
+ __BLSHDescriptorForDetails
+ __BLSHRequestNonInteractiveTTRDraft
+ __BLSHShowFlipbook1hzMissAlert
+ __OBJC_$_CATEGORY_CLASS_METHODS_BLSBacklightChangeEvent_$_BacklightServicesHost
+ __OBJC_$_INSTANCE_METHODS_BLSHFlipbookWatchdog
+ __OBJC_$_INSTANCE_METHODS_BLSHPendingUpdateDisplayModeConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_BLSHFlipbookWatchdog
+ __OBJC_$_INSTANCE_VARIABLES_BLSHPendingUpdateDisplayModeConfiguration
+ __OBJC_$_PROP_LIST_BLSHFlipbook.197
+ __OBJC_$_PROP_LIST_BLSHFlipbookWatchdog
+ __OBJC_$_PROP_LIST_BLSHPendingUpdateDisplayModeConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_BLSHFlipbookWatchdog
+ __OBJC_CLASS_RO_$_BLSHFlipbookWatchdog
+ __OBJC_CLASS_RO_$_BLSHPendingUpdateDisplayModeConfiguration
+ __OBJC_METACLASS_RO_$_BLSHFlipbookWatchdog
+ __OBJC_METACLASS_RO_$_BLSHPendingUpdateDisplayModeConfiguration
+ ___102-[BLSHBacklightEnvironmentStateMachine transitionState:didCompleteUpdateToBacklightState:visualState:]_block_invoke.198
+ ___108-[BLSHAlwaysOnPresentationEngine lock_cancelFlipbookFramesForReason:source:didClearDateSpecifiers:wasReset:]_block_invoke.250
+ ___108-[BLSHAlwaysOnPresentationEngine lock_cancelFlipbookFramesForReason:source:didClearDateSpecifiers:wasReset:]_block_invoke.250.cold.1
+ ___111+[BLSHPendingUpdateDisplayMode operationForUpdateFromCurrentDisplayMode:toTargetDisplayMode:withConfiguration:]_block_invoke
+ ___113-[BLSHBacklightFBSceneHostEnvironment scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:]_block_invoke_3
+ ___124-[BLSHAlwaysOnPresentationEngine requestDatesOperation:environment:didProvideSpecifiers:forPresentationInterval:isComplete:]_block_invoke.219
+ ___124-[BLSHAlwaysOnPresentationEngine requestDatesOperation:environment:didProvideSpecifiers:forPresentationInterval:isComplete:]_block_invoke.223
+ ___124-[BLSHAlwaysOnPresentationEngine requestDatesOperation:environment:didProvideSpecifiers:forPresentationInterval:isComplete:]_block_invoke.223.cold.1
+ ___124-[BLSHAlwaysOnPresentationEngine requestDatesOperation:environment:didProvideSpecifiers:forPresentationInterval:isComplete:]_block_invoke.224
+ ___139-[BLSHBacklightEnvironmentStateMachine initWithPresentation:backlightState:delegate:inactiveBudgetPolicy:osTimerProvider:platformProvider:]_block_invoke
+ ___34-[BLSHFlipbook hangDetectorFired:]_block_invoke
+ ___34-[BLSHFlipbook hangDetectorFired:]_block_invoke.21
+ ___34-[BLSHFlipbook hangDetectorFired:]_block_invoke_2
+ ___34-[BLSHFlipbook hangDetectorFired:]_block_invoke_3
+ ___34-[BLSHFlipbook hangDetectorFired:]_block_invoke_4
+ ___34-[BLSHFlipbook hangDetectorFired:]_block_invoke_5
+ ___38-[BLSHFlipbook hangDetectorFor:block:]_block_invoke
+ ___38-[BLSHSystemWaker watchdogTimerFired:]_block_invoke.104
+ ___50-[BLSHAlwaysOnPresentationEngine debugDescription]_block_invoke_10
+ ___52-[BLSHFlipbookWatchdog initWithOSInterfaceProvider:]_block_invoke
+ ___53-[BLSHBacklightSceneClientSettingsDiffInspector init]_block_invoke_3
+ ___53-[BLSHFlipbookWatchdog _globalQueue_refreshDCPStats:]_block_invoke
+ ___53-[BLSHFlipbookWatchdog _globalQueue_refreshDCPStats:]_block_invoke_2
+ ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke.107
+ ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke.111
+ ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke.114
+ ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke.121
+ ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke_2.115
+ ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke_2.125
+ ___59-[BLSHBaseSceneHostEnvironment set1HzFlipbookForAssertion:]_block_invoke
+ ___59-[BLSHFlipbookWatchdog systemSleepMonitorDidWakeFromSleep:]_block_invoke
+ ___60-[BLSHBacklightFBSceneHostEnvironment updateHost1HzFlipbook]_block_invoke
+ ___63-[BLSHBacklightOSInterfaceProvider transitionToCADisplayState:]_block_invoke.170
+ ___63-[BLSHBacklightOSInterfaceProvider transitionToCADisplayState:]_block_invoke.172
+ ___63-[BLSHBacklightOSInterfaceProvider transitionToCADisplayState:]_block_invoke.172.cold.1
+ ___69-[BLSHBacklightStateMachine systemSleepAction:performWithCompletion:]_block_invoke.198
+ ___70-[BLSHBacklightStateMachine updateSuppressionServiceForActivityState:]_block_invoke.138
+ ___73-[BLSHBacklightTransitionStateMachine onMain_performNextStepInTransition]_block_invoke.246
+ ___77-[BLSHAlwaysOnPresentationEngine hostEnvironment:invalidateContentForReason:]_block_invoke.239
+ ___77-[BLSHAlwaysOnPresentationEngine hostEnvironment:invalidateContentForReason:]_block_invoke_2.240
+ ___77-[BLSHEngineRenderFlipbookSession renderFrameSpecifier:timedOutEnvironments:]_block_invoke.615
+ ___77-[BLSHEngineRenderFlipbookSession renderFrameSpecifier:timedOutEnvironments:]_block_invoke.616
+ ___77-[BLSHEngineRenderFlipbookSession renderFrameSpecifier:timedOutEnvironments:]_block_invoke.617
+ ___77-[BLSHEngineRenderFlipbookSession renderFrameSpecifier:timedOutEnvironments:]_block_invoke_2
+ ___78-[BLSHAlwaysOnPresentationEngine lock_scheduleUpdateTimerForNextUpdatesStart:]_block_invoke.316
+ ___85-[BLSHInternalTapToRadarManager requestTapToRadarNonInteractiveDraft:log:completion:]_block_invoke
+ ___85-[BLSHInternalTapToRadarManager requestTapToRadarNonInteractiveDraft:log:completion:]_block_invoke_2
+ ___85-[BLSHInternalTapToRadarManager requestTapToRadarNonInteractiveDraft:log:completion:]_block_invoke_2.cold.1
+ ___86-[BLSHAlwaysOnPresentationEngine requestDatesOperation:didTimeoutPendingEnvironments:]_block_invoke.225
+ ___87-[BLSHBacklightTransitionStateMachine inactiveEnvironmentSession:updateToPresentation:]_block_invoke.266
+ ___87-[BLSHBacklightTransitionStateMachine inactiveEnvironmentSession:updateToPresentation:]_block_invoke.269
+ ___87-[BLSHBacklightTransitionStateMachine inactiveEnvironmentSession:updateToPresentation:]_block_invoke.274
+ ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke.134
+ ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke.137
+ ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke.140
+ ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke.154
+ ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke_2.143
+ ___88-[BLSHFlipbook renderFrameForPresentation:dateSpecifier:onRenderBegin:onRenderComplete:]_block_invoke
+ ___88-[BLSHFlipbook renderFrameForPresentation:dateSpecifier:onRenderBegin:onRenderComplete:]_block_invoke.76
+ ___88-[BLSHFlipbook renderFrameForPresentation:dateSpecifier:onRenderBegin:onRenderComplete:]_block_invoke_2
+ ___88-[BLSHFlipbook renderFrameForPresentation:dateSpecifier:onRenderBegin:onRenderComplete:]_block_invoke_3
+ ___88-[BLSHFlipbook renderFrameForPresentation:dateSpecifier:onRenderBegin:onRenderComplete:]_block_invoke_3.cold.1
+ ___89-[BLSHBacklightStateMachine initWithPlatformProvider:eventPerformer:osInterfaceProvider:]_block_invoke.78
+ ___89-[BLSHLocalHostSceneEnvironmentUpdater updatedEnvironmentWithDelta:backlightSceneUpdate:]_block_invoke.214
+ ___89-[BLSHLocalHostSceneEnvironmentUpdater updatedEnvironmentWithDelta:backlightSceneUpdate:]_block_invoke.214.cold.1
+ ___95-[BLSHBacklightInactiveEnvironmentSession hostEnvironment:clientDidUpdateAlwaysOnContentIs1hz:]_block_invoke
+ ___99-[BLSHAlwaysOnPresentationEngine renderFramesSession:beganRenderingSpecifier:timedOutEnvironments:]_block_invoke
+ ____BLSHRequestNonInteractiveTTRDraft_block_invoke
+ ____BLSHShowFlipbook1hzMissAlert_block_invoke
+ ____BLSHShowFlipbook1hzMissAlert_block_invoke.69
+ ____BLSHShowFlipbook1hzMissAlert_block_invoke.cold.1
+ ____BLSHShowFlipbook1hzMissAlert_block_invoke_2
+ ___aodStatsFlipbookMissValueForTTRAlert
+ ___block_descriptor_40_e8_32r_e25_i16?0^{__CFDictionary=}8lr32l8
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e29_v16?0"BSAbsoluteMachTimer"8lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs_e37_v24?0"CAFlipBookFrame"8"NSError"16ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48bs56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.113
+ ___block_literal_global.119
+ ___block_literal_global.120
+ ___block_literal_global.129
+ ___block_literal_global.136
+ ___block_literal_global.139
+ ___block_literal_global.143
+ ___block_literal_global.145
+ ___block_literal_global.157
+ ___block_literal_global.174
+ ___block_literal_global.178
+ ___block_literal_global.183
+ ___block_literal_global.191
+ ___block_literal_global.197
+ ___block_literal_global.200
+ ___block_literal_global.221
+ ___block_literal_global.254
+ ___block_literal_global.265
+ ___block_literal_global.268
+ ___block_literal_global.271
+ ___block_literal_global.273
+ ___block_literal_global.283
+ ___block_literal_global.4
+ ___block_literal_global.609
+ __bls1hzFlipbookWatchdogLockStatusDidChange
+ __bls1hzFlipbookWatchdogLockStatusDidChange.cold.1
+ _kCAFlipBookMaximumPoolMemory
+ _kCAFlipBookOverAllocationFactor
+ _objc_msgSend$_globalQueue_initializeDCPStats
+ _objc_msgSend$_globalQueue_refreshDCPStats:
+ _objc_msgSend$_isEnvironmentTransitionAnimatedWithPlatformProvider:
+ _objc_msgSend$_isTransitionForcedUnanimatedWithPlatformProvider:
+ _objc_msgSend$_lock_update1HzFromPresentation:
+ _objc_msgSend$_mainQueue_alertFor1hzFlipbookFrameMiss:
+ _objc_msgSend$abandonedInProgressOperation
+ _objc_msgSend$alwaysOnContentIs1hz
+ _objc_msgSend$appendUnsignedInteger:
+ _objc_msgSend$bls_alwaysOnContentIs1hz
+ _objc_msgSend$bs_safeNumberForKey:
+ _objc_msgSend$clientAlwaysOnContentIs1hz
+ _objc_msgSend$deviceSupportsAlwaysOnFlipbookWatchdog
+ _objc_msgSend$enableAlertsUsingDefaults
+ _objc_msgSend$hostEnvironment:clientDidUpdateAlwaysOnContentIs1hz:
+ _objc_msgSend$initWithPresentation:backlightState:delegate:inactiveBudgetPolicy:osTimerProvider:platformProvider:
+ _objc_msgSend$initWithSoftMemoryLimit:frameCapacity:framesPerSecond:minimumGapDuration:coaelscingEpsilon:minimumPrepareInterval:maximumRenderInterval:surfacePoolSize:surfaceOverallocationFactor:
+ _objc_msgSend$initWithWatchdogType:cbDisplayMode:cbFlipbookState:caDisplayState:completedCADisplayState:suppressionServiceActive:flipbookTransparent:deviceSupportsAlwaysOn:deviceSupportsAlwaysOnFlipbook:displayStateClientSupported:backlightDimmedFactor:
+ _objc_msgSend$is1HzFlipbookForAssertion
+ _objc_msgSend$isAnimatedTranistion
+ _objc_msgSend$isEnvironmentTransitionAnimatedToState:fromPreviousState:
+ _objc_msgSend$isNullOperationAllowed
+ _objc_msgSend$isTransitionForcedUnanimatedForSource:
+ _objc_msgSend$isTransitionForcedUnanimatedToState:fromPreviousState:
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$operationForUpdateFromCurrentDisplayMode:toTargetDisplayMode:withConfiguration:
+ _objc_msgSend$pendingOperation
+ _objc_msgSend$radarIsUserInitiated
+ _objc_msgSend$renderForTime:options:userInfo:onRenderBegin:onRenderComplete:
+ _objc_msgSend$renderFrameForPresentation:dateSpecifier:onRenderBegin:onRenderComplete:
+ _objc_msgSend$renderFramesSession:beganRenderingSpecifier:timedOutEnvironments:
+ _objc_msgSend$requestTapToRadarNonInteractiveDraft:log:completion:
+ _objc_msgSend$set1HzFlipbookForAssertion:
+ _objc_msgSend$setAlwaysOnContentIs1hz:
+ _objc_msgSend$setAninmationPropertiesWithPlatformProvider:
+ _objc_msgSend$setIsAnimatedTranistion:
+ _objc_msgSend$setIsNullOperationAllowed:
+ _objc_msgSend$setPendingOperation:
+ _objc_msgSend$setTransitionForcedUnanimated:environmentTransitionAnimated:
+ _objc_msgSend$setUserInitiated:
+ _objc_msgSend$surfaceAllocationPoolSize
+ _objc_msgSend$surfaceOverallocationFactor
- +[BLSHBacklightOSInterfaceProvider sysctlKernSpecialMode]
- +[BLSHBacklightOSInterfaceProvider sysctlKernSpecialMode].cold.1
- +[BLSHBacklightOSInterfaceProvider sysctlKernSpecialMode].cold.2
- +[BLSHPendingUpdateDisplayMode operationForUpdateFromCurrentDisplayMode:toTargetDisplayMode:withPendingOperation:abandonedInProgressOperation:isNullOperationAllowed:]
- +[BLSHPendingUpdateDisplayMode operationForUpdateFromCurrentDisplayMode:toTargetDisplayMode:withPendingOperation:abandonedInProgressOperation:isNullOperationAllowed:].cold.1
- +[BLSHPendingUpdateDisplayMode operationForUpdateFromCurrentDisplayMode:toTargetDisplayMode:withPendingOperation:abandonedInProgressOperation:isNullOperationAllowed:].cold.2
- -[BLSBacklightChangeEvent(BacklightServicesHost) isAlwaysOnTransition]
- -[BLSBacklightChangeEvent(BacklightServicesHost) isEnvironmentTransitionAnimated]
- -[BLSBacklightChangeEvent(BacklightServicesHost) isTransitionForcedUnanimated]
- -[BLSHBacklightEnvironmentStateMachine initWithPresentation:backlightState:delegate:inactiveBudgetPolicy:osTimerProvider:].cold.1
- -[BLSHBacklightFBSceneHostEnvironment set1HzFlipbook:]
- -[BLSHBacklightFBSceneHostEnvironment set1HzFlipbook:].cold.1
- -[BLSHBacklightOSInterfaceProvider isKernelAlwaysOnMode]
- -[BLSHBacklightOSInterfaceProvider setKernelAlwaysOnMode:]
- -[BLSHBacklightOSInterfaceProvider setKernelAlwaysOnMode:].cold.1
- -[BLSHBacklightTransitionStateMachine onMain_ensureSessionCreated].cold.2
- -[BLSHBaseSceneHostEnvironment set1HzFlipbook:]
- -[BLSHFlipbook flushLogBuffers]
- -[BLSHFlipbook hangDetector:]
- -[BLSHFlipbook hangDetector:].cold.1
- -[BLSHFlipbook hangDetectorFired]
- -[BLSHFlipbook renderFrameForPresentation:dateSpecifier:completion:]
- -[BLSHFlipbook renderFrameForPresentation:dateSpecifier:completion:].cold.1
- -[BLSHOSInterfaceProviderAbortContext initWithWatchdogType:cbDisplayMode:cbFlipbookState:caDisplayState:completedCADisplayState:suppressionServiceActive:flipbookTransparent:deviceSupportsAlwaysOn:deviceSupportsAlwaysOnFlipbook:kernelSpecialMode:displayStateClientSupported:backlightDimmedFactor:]
- -[BLSHPseudoFlipbook renderFrameForPresentation:dateSpecifier:completion:]
- -[BLSHTapToRadarDescriptor classification]
- -[BLSHTapToRadarDescriptor reproducibility]
- -[BLSHTapToRadarDescriptor setClassification:]
- -[BLSHTapToRadarDescriptor setReproducibility:]
- -[BLSHTapToRadarDescriptor toURL]
- GCC_except_table135
- GCC_except_table136
- GCC_except_table146
- GCC_except_table17
- GCC_except_table181
- GCC_except_table182
- GCC_except_table183
- GCC_except_table184
- GCC_except_table19
- GCC_except_table29
- GCC_except_table33
- GCC_except_table40
- GCC_except_table41
- GCC_except_table61
- GCC_except_table69
- GCC_except_table75
- GCC_except_table78
- GCC_except_table80
- _OBJC_CLASS_$_LSApplicationWorkspace
- _OBJC_CLASS_$_NSURLComponents
- _OBJC_CLASS_$_NSURLQueryItem
- _OBJC_IVAR_$_BLSHBacklightFBSceneHostEnvironment._lock_1HzFlipbook
- _OBJC_IVAR_$_BLSHBacklightOSInterfaceProvider._lock_kernelSpecialMode
- _OBJC_IVAR_$_BLSHOSInterfaceProviderAbortContext._kernelSpecialMode
- _OBJC_IVAR_$_BLSHTapToRadarDescriptor._classification
- _OBJC_IVAR_$_BLSHTapToRadarDescriptor._reproducibility
- __OBJC_$_PROP_LIST_BLSBacklightChangeEvent_$_BacklightServicesHost
- __OBJC_$_PROP_LIST_BLSHFlipbook.138
- ___102-[BLSHBacklightEnvironmentStateMachine transitionState:didCompleteUpdateToBacklightState:visualState:]_block_invoke.183
- ___108-[BLSHAlwaysOnPresentationEngine lock_cancelFlipbookFramesForReason:source:didClearDateSpecifiers:wasReset:]_block_invoke.231
- ___108-[BLSHAlwaysOnPresentationEngine lock_cancelFlipbookFramesForReason:source:didClearDateSpecifiers:wasReset:]_block_invoke.231.cold.1
- ___122-[BLSHBacklightEnvironmentStateMachine initWithPresentation:backlightState:delegate:inactiveBudgetPolicy:osTimerProvider:]_block_invoke
- ___124-[BLSHAlwaysOnPresentationEngine requestDatesOperation:environment:didProvideSpecifiers:forPresentationInterval:isComplete:]_block_invoke.200
- ___124-[BLSHAlwaysOnPresentationEngine requestDatesOperation:environment:didProvideSpecifiers:forPresentationInterval:isComplete:]_block_invoke.204
- ___124-[BLSHAlwaysOnPresentationEngine requestDatesOperation:environment:didProvideSpecifiers:forPresentationInterval:isComplete:]_block_invoke.204.cold.1
- ___124-[BLSHAlwaysOnPresentationEngine requestDatesOperation:environment:didProvideSpecifiers:forPresentationInterval:isComplete:]_block_invoke.205
- ___166+[BLSHPendingUpdateDisplayMode operationForUpdateFromCurrentDisplayMode:toTargetDisplayMode:withPendingOperation:abandonedInProgressOperation:isNullOperationAllowed:]_block_invoke
- ___29-[BLSHFlipbook hangDetector:]_block_invoke
- ___33-[BLSHFlipbook hangDetectorFired]_block_invoke
- ___33-[BLSHFlipbook hangDetectorFired]_block_invoke.21
- ___33-[BLSHFlipbook hangDetectorFired]_block_invoke_2
- ___33-[BLSHFlipbook hangDetectorFired]_block_invoke_3
- ___33-[BLSHFlipbook hangDetectorFired]_block_invoke_4
- ___33-[BLSHFlipbook hangDetectorFired]_block_invoke_5
- ___38-[BLSHSystemWaker watchdogTimerFired:]_block_invoke.89
- ___47-[BLSHBaseSceneHostEnvironment set1HzFlipbook:]_block_invoke
- ___48+[BLSHTapToRadarFiler fileRadar:log:completion:]_block_invoke
- ___48+[BLSHTapToRadarFiler fileRadar:log:completion:]_block_invoke.cold.1
- ___54-[BLSHBacklightFBSceneHostEnvironment set1HzFlipbook:]_block_invoke
- ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke.106
- ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke.92
- ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke.96
- ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke.99
- ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke_2.100
- ___57-[BLSHBacklightStateMachine onMain_performChangeRequest:]_block_invoke_2.110
- ___63-[BLSHBacklightOSInterfaceProvider transitionToCADisplayState:]_block_invoke.157
- ___63-[BLSHBacklightOSInterfaceProvider transitionToCADisplayState:]_block_invoke.159
- ___63-[BLSHBacklightOSInterfaceProvider transitionToCADisplayState:]_block_invoke.159.cold.1
- ___68-[BLSHFlipbook renderFrameForPresentation:dateSpecifier:completion:]_block_invoke
- ___68-[BLSHFlipbook renderFrameForPresentation:dateSpecifier:completion:]_block_invoke_2
- ___69-[BLSHBacklightStateMachine systemSleepAction:performWithCompletion:]_block_invoke.183
- ___70-[BLSHBacklightStateMachine updateSuppressionServiceForActivityState:]_block_invoke.123
- ___73-[BLSHBacklightTransitionStateMachine onMain_performNextStepInTransition]_block_invoke.226
- ___77-[BLSHAlwaysOnPresentationEngine hostEnvironment:invalidateContentForReason:]_block_invoke.220
- ___77-[BLSHAlwaysOnPresentationEngine hostEnvironment:invalidateContentForReason:]_block_invoke_2.221
- ___77-[BLSHEngineRenderFlipbookSession renderFrameSpecifier:timedOutEnvironments:]_block_invoke.593
- ___77-[BLSHEngineRenderFlipbookSession renderFrameSpecifier:timedOutEnvironments:]_block_invoke.594
- ___78-[BLSHAlwaysOnPresentationEngine lock_scheduleUpdateTimerForNextUpdatesStart:]_block_invoke.297
- ___86-[BLSHAlwaysOnPresentationEngine requestDatesOperation:didTimeoutPendingEnvironments:]_block_invoke.206
- ___87-[BLSHBacklightTransitionStateMachine inactiveEnvironmentSession:updateToPresentation:]_block_invoke.246
- ___87-[BLSHBacklightTransitionStateMachine inactiveEnvironmentSession:updateToPresentation:]_block_invoke.249
- ___87-[BLSHBacklightTransitionStateMachine inactiveEnvironmentSession:updateToPresentation:]_block_invoke.254
- ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke.119
- ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke.122
- ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke.125
- ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke.139
- ___88-[BLSHBacklightEnvironmentStateMachine onMain_setPresentation:withTargetBacklightState:]_block_invoke_2.128
- ___89-[BLSHBacklightStateMachine initWithPlatformProvider:eventPerformer:osInterfaceProvider:]_block_invoke.63
- ___89-[BLSHLocalHostSceneEnvironmentUpdater updatedEnvironmentWithDelta:backlightSceneUpdate:]_block_invoke.199
- ___89-[BLSHLocalHostSceneEnvironmentUpdater updatedEnvironmentWithDelta:backlightSceneUpdate:]_block_invoke.199.cold.1
- ___NSDictionary0__struct
- ___block_descriptor_72_e8_32s40s48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
- ___block_literal_global.105
- ___block_literal_global.107
- ___block_literal_global.121
- ___block_literal_global.124
- ___block_literal_global.127
- ___block_literal_global.128
- ___block_literal_global.130
- ___block_literal_global.144
- ___block_literal_global.163
- ___block_literal_global.168
- ___block_literal_global.176
- ___block_literal_global.182
- ___block_literal_global.185
- ___block_literal_global.202
- ___block_literal_global.235
- ___block_literal_global.245
- ___block_literal_global.248
- ___block_literal_global.251
- ___block_literal_global.253
- ___block_literal_global.264
- ___block_literal_global.584
- ___kCFBooleanTrue
- __os_feature_enabled_impl
- _objc_msgSend$URL
- _objc_msgSend$componentsWithString:
- _objc_msgSend$defaultWorkspace
- _objc_msgSend$initWithPresentation:backlightState:delegate:inactiveBudgetPolicy:osTimerProvider:
- _objc_msgSend$initWithSoftMemoryLimit:frameCapacity:framesPerSecond:minimumGapDuration:coaelscingEpsilon:minimumPrepareInterval:maximumRenderInterval:
- _objc_msgSend$initWithWatchdogType:cbDisplayMode:cbFlipbookState:caDisplayState:completedCADisplayState:suppressionServiceActive:flipbookTransparent:deviceSupportsAlwaysOn:deviceSupportsAlwaysOnFlipbook:kernelSpecialMode:displayStateClientSupported:backlightDimmedFactor:
- _objc_msgSend$isKernelAlwaysOnMode
- _objc_msgSend$openURL:withOptions:error:
- _objc_msgSend$operationForUpdateFromCurrentDisplayMode:toTargetDisplayMode:withPendingOperation:abandonedInProgressOperation:isNullOperationAllowed:
- _objc_msgSend$queryItemWithName:value:
- _objc_msgSend$renderForTime:options:userInfo:error:
- _objc_msgSend$renderFrameForPresentation:dateSpecifier:completion:
- _objc_msgSend$setKernelAlwaysOnMode:
- _objc_msgSend$setQueryItems:
- _objc_msgSend$toURL
- _sysctlbyname
CStrings:
+ "%@ alert: BacklightServices 1hz flipbook missed frames detected %@ debug logs at %@ on %@.\nPlease file a radar against BacklightServices | All with a sysdiagnose."
+ "%@%@ - 1hz Flipbook DCP Missed Frames Detected"
+ "%p %{public}@ hang detector ending for source: %@"
+ "%p %{public}@ hang detector starting for source: %@"
+ "%p -[CAFlipBook renderForTime:options:userInfo:onRenderBegin:onRenderComplete:] took %.5fs to render frame:%{public}@ error:%{public}@"
+ "%p -[CAFlipBook renderForTime:options:userInfo:onRenderBegin:onRenderComplete:] took %.5fs until renderBegun"
+ "%p -[CAFlipBook renderForTime:options:userInfo:onRenderBegin:onRenderComplete:] took %.5fs. Renderserver may be blocked"
+ "%p created %{public}@, specification: %{public}@"
+ "%p updates(%d) (complete) after:%{public}@ coalesceTo:%{public}@ gapDuration:%1.3lg epsilon:%.3lf max:%ld upTo:%{public}@ pres:%p filtered:%{BOOL}u result:%{public}@ startingAtDate:%{public}@ pres:%{public}@"
+ "%p:%{public}@ did create render session for flipbook memoryUsage:%{public}@(aprox:%{public}@)/%{public}@ updates:%{public}@"
+ "%p:%{public}@ ending render session:%p for reason:%{public}@ sleepActionState:%{public}@ fillState:%{public}@ stby:%{BOOL}u sup:%{BOOL}u memoryUsage:%{public}@/%{public}@ %{public}@"
+ "%p:%{public}@ set1HzFlipbookForAssertion:%{BOOL}u client1Hz::%{BOOL}u didChange:%{BOOL}u is1HzFlipbookDidChange:%{BOOL}u"
+ "%p:%{public}@ waiting for last session render frame:%{public}@"
+ "%p:%{public}@ will not render more frames, waiting to begin previous render:%{public}@"
+ "%p:update1HzFromPresentation new1HzFlipbook:%{BOOL}u old1HzFlipbook:%{BOOL}u environment:%{public}@ presentation::%{public}@"
+ "1hz Flipbook frame miss detected from DCP stats. New miss count = %lld, delta = %lld"
+ "1hz_frame_miss_"
+ "<skip>"
+ "@\"<BLSHSystemSleepMonitoring>\""
+ "@\"BLSHFlipbookWatchdog\""
+ "@40@0:8q16q24@32"
+ "@64@0:8@16q24@32@40@48@56"
+ "@80@0:8Q16q24q32q40q48B56B60B64B68B72f76"
+ "@88@0:8Q16q24d32d40d48d56d64Q72d80"
+ "B32@0:8q16q24"
+ "BLSFlipbookHang"
+ "BLSH Critical Assert did fail at %{public}@ on build %{public}@: %{public}@ userIntiated: %{public}d"
+ "BLSHCriticalAssertDidFailSource"
+ "BLSHCriticalAssertDidFailUserInitiated"
+ "BLSHFlipbookWatchdog"
+ "BLSHPendingUpdateDisplayModeConfiguration"
+ "C"
+ "CoreAnimation [CAFlipbook %@] hang detected –\u00a0%.4lfs elapsed - will flush buffers"
+ "CoreAnimation flipbook hang detected from : %@"
+ "DCP"
+ "Error when trying to get aod channels: %{public}@"
+ "Error when trying to get aod stats subscription: %{public}@"
+ "Failed to generate tailspin for flipbook hang: %@"
+ "Flipbook 1hz frame miss detected from DCP in %@"
+ "IOReport shows that the DCP is reporting %lld missed 1hz flipbook frames on this device."
+ "Problem creating non-interactive radar draft: %@"
+ "Radar is not user initiated, requesting a draft immediately."
+ "T@\"BLSHPendingUpdateDisplayMode\",&,V_abandonedInProgressOperation"
+ "T@\"BLSHPendingUpdateDisplayMode\",&,V_pendingOperation"
+ "T@\"NSArray\",C,N,V_attachments"
+ "T@\"NSArray\",C,N,V_keywordIDs"
+ "TB,?,Gis1HzFlipbookForAssertion,Sset1HzFlipbookForAssertion:"
+ "TB,?,Gis1HzFlipbookForAssertion,Sset1HzFlipbookForAssertion:,V_lock_1HzFlipbook"
+ "TB,?,R,Gis1HzFlipbook"
+ "TB,N,V_radarIsUserInitiated"
+ "TB,N,V_userInitiated"
+ "TB,V_isAnimatedTranistion"
+ "TB,V_isNullOperationAllowed"
+ "TQ,N,V_failureSource"
+ "Td,R,N,V_surfaceAllocationPoolSize"
+ "Td,R,N,V_surfaceOverallocationFactor"
+ "Tq,N"
+ "Unable to subscribe to IOReport AOD metrics, Flipbook 1hz validation will not be available."
+ "^{__CFDictionary=}"
+ "^{__IOReportSubscriptionCF=}"
+ "_abandonedInProgressOperation"
+ "_alertsEnabled"
+ "_bls1hzFlipbookWatchdogLockStatusDidChange: will stop listening for kMobileKeyBagLockStatusNotificationID and check for stored failed watchdog details"
+ "_deviceSupportsAlwaysOnFlipbookWatchdog"
+ "_failureSource"
+ "_flipbookWatchdog"
+ "_globalQueue_initializeDCPStats"
+ "_globalQueue_refreshDCPStats:"
+ "_ioReportSubscribedChannels"
+ "_ioReportSubscription"
+ "_isAnimatedTranistion"
+ "_isEnvironmentTransitionAnimatedWithPlatformProvider:"
+ "_isNullOperationAllowed"
+ "_isTransitionForcedUnanimatedWithPlatformProvider:"
+ "_lastKnown_aodStatsFlipbookMiss"
+ "_lock_1HzFlipbookForAssertion"
+ "_lock_preparingToRenderSpecifier"
+ "_lock_targetIdleBacklightState"
+ "_lock_update1HzFromPresentation:"
+ "_mainQueue_alertFor1hzFlipbookFrameMiss:"
+ "_pendingOperation"
+ "_radarIsUserInitiated"
+ "_sleepMonitor"
+ "_surfaceAllocationPoolSize"
+ "_surfaceOverallocationFactor"
+ "_userInitiated"
+ "abandonedInProgressOperation"
+ "alwaysOnContentIs1hz"
+ "aod stats"
+ "appendUnsignedInteger:"
+ "bls_alwaysOnContentIs1hz"
+ "blsh_1hz_flipbook_watchdog_enabled"
+ "bs_safeNumberForKey:"
+ "cancelAllFramesWithError"
+ "clientAlwaysOnContentIs1hz"
+ "com.apple.backlightservices"
+ "com.apple.backlightservices.flipbook.missedframes"
+ "defaultIsEnvironmentTransitionAnimatedToState:fromPreviousState:"
+ "defaultIsTransitionForcedUnanimatedToState:fromPreviousState:"
+ "defaultTransitionForcedUnanimatedForSource:"
+ "deviceSupportsAlwaysOnFlipbookWatchdog"
+ "enableAlertsUsingDefaults"
+ "failureSource"
+ "hangDetectorFired:"
+ "hostEnvironment:clientDidUpdateAlwaysOnContentIs1hz:"
+ "i16@?0^{__CFDictionary=}8"
+ "initWithPresentation:backlightState:delegate:inactiveBudgetPolicy:osTimerProvider:platformProvider:"
+ "initWithSoftMemoryLimit:frameCapacity:framesPerSecond:minimumGapDuration:coaelscingEpsilon:minimumPrepareInterval:maximumRenderInterval:surfacePoolSize:surfaceOverallocationFactor:"
+ "initWithWatchdogType:cbDisplayMode:cbFlipbookState:caDisplayState:completedCADisplayState:suppressionServiceActive:flipbookTransparent:deviceSupportsAlwaysOn:deviceSupportsAlwaysOnFlipbook:displayStateClientSupported:backlightDimmedFactor:"
+ "is1HzFlipbookForAssertion"
+ "isAnimatedTranistion"
+ "isEnvironmentTransitionAnimatedToState:fromPreviousState:"
+ "isNullOperationAllowed"
+ "isTransitionForcedUnanimatedForSource:"
+ "isTransitionForcedUnanimatedToState:fromPreviousState:"
+ "missedFrames"
+ "numberWithLongLong:"
+ "oneHzFlipbookForAssertion"
+ "operationForUpdateFromCurrentDisplayMode:toTargetDisplayMode:withConfiguration:"
+ "pendingOperation"
+ "preparingToRender"
+ "radarIsUserInitiated"
+ "reasonCode"
+ "renderForTime"
+ "renderForTime:options:userInfo:onRenderBegin:onRenderComplete:"
+ "renderFrame:setContext"
+ "renderFrameForPresentation:dateSpecifier:onRenderBegin:onRenderComplete:"
+ "renderFramesSession:beganRenderingSpecifier:timedOutEnvironments:"
+ "rendering"
+ "requestTapToRadarNonInteractiveDraft:log:completion:"
+ "set1HzFlipbook"
+ "set1HzFlipbookForAssertion:"
+ "setAbandonedInProgressOperation:"
+ "setAlwaysOnContentIs1hz:"
+ "setAninmationPropertiesWithPlatformProvider:"
+ "setCachesFramesOnExit"
+ "setFailureSource:"
+ "setIsAnimatedTranistion:"
+ "setIsNullOperationAllowed:"
+ "setPendingOperation:"
+ "setPowerSavingEnabled"
+ "setRadarIsUserInitiated:"
+ "setTargetIdleState targetIdleState:%@ changed=%{BOOL}u"
+ "setTargetIdleState:"
+ "setTransitionForcedUnanimated:environmentTransitionAnimated:"
+ "setUserInitiated:"
+ "surfaceAllocationPoolSize"
+ "surfaceOverallocationFactor"
+ "targetIdleState"
+ "userInitiated"
+ "v24@?0@\"CAFlipBookFrame\"8@\"NSError\"16"
+ "v40@0:8@\"BLSHEngineRenderFlipbookSession\"16@\"BLSHPresentationDateSpecifier\"24@\"NSArray\"32"
+ "v48@0:8@\"BLSHBacklightEnvironmentPresentation\"16@\"BLSHPresentationDateSpecifier\"24@?<v@?>32@?<v@?@\"<BLSHRenderedFlipbookFrame>\"@\"NSError\">40"
+ "v48@0:8@16@24@?32@?40"
+ "{?=b1b1b1}24@0:8@16"
+ "\x91"
+ "\xf01"
- "%ld"
- "%p -[CAFlipBook renderForTime:options:userInfo:error:] took %.5fs. Likely dupe of rdar://78634442"
- "%p:%{public}@ ending render session:%p for reason:%{public}@ sleepActionState:%{public}@ fillState:%{public}@ stby:%{BOOL}u sup:%{BOOL}u %{public}@"
- "%p:%{public}@ set1HzFlipbook:%{BOOL}u didChange:%{BOOL}u"
- "%p:%{public}@ will not render more frames, waiting for previous render:%{public}@"
- "@52@0:8q16q24@32@40B48"
- "@84@0:8Q16q24q32q40q48B56B60B64B68B72B76f80"
- "Attachments"
- "BLSH Critical Assert did fail at %{public}@ on build %{public}@: %{public}@"
- "BundleID"
- "Classification"
- "ComponentID"
- "ComponentName"
- "ComponentVersion"
- "Description"
- "Kernel always on mode disabled by disable_kernel_only_wakes feature flag"
- "KeywordIDs"
- "OSIP:%p failed to get kernel aotMode status:%d"
- "OSIP:%p failed to set kernel aotMode:%x status:%d"
- "OSIP:%p get kernel aotMode:%x"
- "OSIP:%p set kernel aotMode:%x"
- "Reproducibility"
- "Serious Bug"
- "Sometimes"
- "T@\"NSString\",C,N,V_attachments"
- "T@\"NSString\",C,N,V_classification"
- "T@\"NSString\",C,N,V_keywordIDs"
- "T@\"NSString\",C,N,V_reproducibility"
- "TB,?,Gis1HzFlipbook,Sset1HzFlipbook:"
- "TB,?,Gis1HzFlipbook,Sset1HzFlipbook:,V_lock_1HzFlipbook"
- "TB,N,GisKernelAlwaysOnMode"
- "TB,R,N,GisAlwaysOnTransition"
- "TB,R,N,GisEnvironmentTransitionAnimated"
- "TB,R,N,GisTransitionForcedUnanimated"
- "Title"
- "URL"
- "_classification"
- "_kernelSpecialMode"
- "_lock_kernelSpecialMode"
- "_reproducibility"
- "alwaysOnTransition"
- "classification"
- "com.apple.coreanimation.flipbook"
- "componentsWithString:"
- "could not file Tap-To-Radar %@ %@"
- "defaultWorkspace"
- "disable_kernel_only_wakes"
- "environmentTransitionAnimated"
- "filed Tap-To-Radar %@"
- "flipbook hang detected –\u00a0%.4lfs elapsed - will flush buffers"
- "hangDetectorFired"
- "initWithWatchdogType:cbDisplayMode:cbFlipbookState:caDisplayState:completedCADisplayState:suppressionServiceActive:flipbookTransparent:deviceSupportsAlwaysOn:deviceSupportsAlwaysOnFlipbook:kernelSpecialMode:displayStateClientSupported:backlightDimmedFactor:"
- "isAlwaysOnTransition"
- "isKernelAlwaysOnMode"
- "kern.aotmode"
- "kernelAlwaysOnMode"
- "kernelSpecialMode"
- "openURL:withOptions:error:"
- "operationForUpdateFromCurrentDisplayMode:toTargetDisplayMode:withPendingOperation:abandonedInProgressOperation:isNullOperationAllowed:"
- "queryItemWithName:value:"
- "renderForTime:options:userInfo:error:"
- "renderFrameForPresentation:dateSpecifier:completion:"
- "renderingSpecifier"
- "reproducibility"
- "setClassification:"
- "setKernelAlwaysOnMode:"
- "setQueryItems:"
- "setReproducibility:"
- "tap-to-radar://new"
- "toURL"
- "transitionForcedUnanimated"
- "v40@0:8@\"BLSHBacklightEnvironmentPresentation\"16@\"BLSHPresentationDateSpecifier\"24@?<v@?@\"<BLSHRenderedFlipbookFrame>\"@\"NSError\">32"
- "{?=b1b1}24@0:8@16"
- "\x81"
- "\xf0!"

```
