## BacklightServicesHost

> `/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`

### Sections with Same Size but Changed Content

- `__TEXT.__ustring`

```diff

-6.1.3.0.0
-  __TEXT.__text: 0x98d90
-  __TEXT.__objc_methlist: 0x9de4
+6.1.4.0.0
+  __TEXT.__text: 0x997f0
+  __TEXT.__objc_methlist: 0x9dec
   __TEXT.__const: 0x488
-  __TEXT.__gcc_except_tab: 0xf10
-  __TEXT.__cstring: 0x7eaf
-  __TEXT.__oslogstring: 0x12edb
+  __TEXT.__gcc_except_tab: 0xee0
+  __TEXT.__cstring: 0x7ef1
+  __TEXT.__oslogstring: 0x13056
   __TEXT.__ustring: 0x570
-  __TEXT.__unwind_info: 0x35c8
+  __TEXT.__unwind_info: 0x3608
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2e08
-  __DATA_CONST.__objc_classlist: 0x640
+  __DATA_CONST.__const: 0x2de0
+  __DATA_CONST.__objc_classlist: 0x638
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x318
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3c28
+  __DATA_CONST.__objc_selrefs: 0x3c68
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x518
   __DATA_CONST.__objc_arraydata: 0x78
-  __DATA_CONST.__got: 0x840
-  __AUTH_CONST.__const: 0xd40
-  __AUTH_CONST.__cfstring: 0x7d00
-  __AUTH_CONST.__objc_const: 0x19498
+  __DATA_CONST.__got: 0x848
+  __AUTH_CONST.__const: 0xd60
+  __AUTH_CONST.__cfstring: 0x7d40
+  __AUTH_CONST.__objc_const: 0x19478
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x130c
+  __DATA.__objc_ivar: 0x1318
   __DATA.__data: 0x2520
-  __DATA_DIRTY.__objc_data: 0x3de0
+  __DATA_DIRTY.__objc_data: 0x3d90
   __DATA_DIRTY.__bss: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 4235
-  Symbols:   7498
-  CStrings:  2001
+  Functions: 4247
+  Symbols:   7501
+  CStrings:  2009
 
Symbols:
+ +[BLSHTelemetryService sharedTelemetryService]
+ -[BLSHAggregateBacklightHost _addObserver:forBacklight:]
+ -[BLSHAggregateBacklightHost addObserver:forBacklight:]
+ -[BLSHAggregateBacklightHost backlightForObserver:]
+ -[BLSHBacklightStateMachine _addObserver:forBacklight:]
+ -[BLSHBacklightStateMachine addObserver:forBacklight:]
+ -[BLSHBacklightStateMachine backlightForObserver:]
+ -[BLSHDisplayWakeTelemetry _commonInitWithTelemetrySource:telemetryService:]
+ -[BLSHDisplayWakeTelemetry initWithPlatformDelegate:telemetrySource:telemetryService:]
+ -[BLSHFlipbook resolveHangAsAbortForSource:description:]
+ -[BLSHFlipbook resolveHangAsPanicForSource:explanation:]
+ -[BLSHSystemWakeTelemetry _commonInitWithBacklightHost:osInterfaceProvider:telemetryService:]
+ -[BLSHSystemWakeTelemetry _resetAccumulatedMetrics]
+ -[BLSHSystemWakeTelemetry _scheduleMetricsTimer]
+ -[BLSHSystemWakeTelemetry accumulateMetrics:]
+ -[BLSHSystemWakeTelemetry accumulateOffDuration:isAOT:]
+ -[BLSHSystemWakeTelemetry accumulateOnDuration:]
+ -[BLSHSystemWakeTelemetry backlight:didChangeAlwaysOnEnabled:]
+ -[BLSHSystemWakeTelemetry backlight:didUpdateToDisplayMode:fromDisplayMode:activeEvents:abortedEvents:]
+ -[BLSHSystemWakeTelemetry backlight:willUpdateToDisplayMode:fromDisplayMode:forEvents:abortedEvents:]
+ -[BLSHSystemWakeTelemetry gatherTelemetryForWakeNumber:]
+ -[BLSHSystemWakeTelemetry initWithPlatformDelegate:backlightHost:osInterfaceProvider:telemetryService:]
+ -[BLSHSystemWakeTelemetry logMetricsTimerFired]
+ -[BLSHSystemWakeTelemetry observesUpdateToDisplayMode]
+ -[BLSHSystemWakeTelemetry stopObserving]
+ -[BLSHTelemetryService .cxx_destruct]
+ -[BLSHTelemetryService _powerLogIdentifierForSubsystem:category:]
+ -[BLSHTelemetryService init]
+ -[BLSHTelemetryService sendAnalyticsEvent:payloadBuilder:]
+ -[BLSHTelemetryService sendPowerLogTelemetryWithSubsystem:category:payload:]
+ GCC_except_table26
+ GCC_except_table28
+ GCC_except_table30
+ GCC_except_table36
+ GCC_except_table42
+ GCC_except_table51
+ _BLSHTelemetryServiceWorkloop.onceToken
+ _BLSHTelemetryServiceWorkloop.workloop
+ _OBJC_CLASS_$_BLSBacklightProxyObservation
+ _OBJC_CLASS_$_BLSHTelemetryService
+ _OBJC_CLASS_$_NSValue
+ _OBJC_IVAR_$_BLSHDisplayWakeTelemetry._telemetryService
+ _OBJC_IVAR_$_BLSHFlipbook._hangResolved
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._accumulatedFlipbookLayoutDuration
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._accumulatedFlipbookRenderDuration
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._accumulatedMetrics
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._accumulatedSecondsDisplayOff
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._accumulatedSecondsDisplayOn
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._accumulatedSecondsShowingAOT
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._backlightHost
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._backlightOffStartTime
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._backlightOnStartTime
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._blsTelemetryEnabled
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._completedWakeNumber
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._currentMetrics
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._delegateFlags
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._didFinalLog
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._hasPoweredOnTime
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._isAOT
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._isTelemetryEnqueuedAtUtilityQOS
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._lastTelemtryAccumulateTime
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._loggedToTelemtryAccumulateTime
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._osInterfaceProvider
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._serviceStarted
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._systemSleepObserver
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._systemWakeMetricsEventKey
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._telemetryService
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._timer
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._wakeNumber
+ _OBJC_IVAR_$_BLSHSystemWakeTelemetry._willSleepTime
+ _OBJC_IVAR_$_BLSHTelemetryService._lock
+ _OBJC_IVAR_$_BLSHTelemetryService._lock_powerLogIdentifiersByKey
+ _OBJC_METACLASS_$_BLSHTelemetryService
+ __OBJC_$_CLASS_METHODS_BLSHTelemetryService
+ __OBJC_$_INSTANCE_METHODS_BLSHTelemetryService
+ __OBJC_$_INSTANCE_VARIABLES_BLSHTelemetryService
+ __OBJC_$_PROP_LIST_BLSHTelemetryService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BLSBacklightProxy
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BLSHTelemetryServiceSending
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSBacklightProxy
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSHTelemetryServiceSending
+ __OBJC_$_PROTOCOL_REFS_BLSHTelemetryServiceSending
+ __OBJC_CLASS_PROTOCOLS_$_BLSHTelemetryService
+ __OBJC_CLASS_RO_$_BLSHTelemetryService
+ __OBJC_LABEL_PROTOCOL_$_BLSHTelemetryServiceSending
+ __OBJC_METACLASS_RO_$_BLSHTelemetryService
+ __OBJC_PROTOCOL_$_BLSHTelemetryServiceSending
+ ___103-[BLSHSystemWakeTelemetry backlight:didUpdateToDisplayMode:fromDisplayMode:activeEvents:abortedEvents:]_block_invoke
+ ___34-[BLSHFlipbook hangDetectorFired:]_block_invoke_6
+ ___34-[BLSHFlipbook hangDetectorFired:]_block_invoke_7
+ ___46+[BLSHTelemetryService sharedTelemetryService]_block_invoke
+ ___47-[BLSHSystemWakeTelemetry logMetricsTimerFired]_block_invoke
+ ___48-[BLSHSystemWakeTelemetry _scheduleMetricsTimer]_block_invoke
+ ___55-[BLSHBacklightStateMachine _addObserver:forBacklight:]_block_invoke
+ ___55-[BLSHSystemWakeTelemetry logTelemetryForInvalidation:]_block_invoke
+ ___55-[BLSHSystemWakeTelemetry logTelemetryForRequestDates:]_block_invoke
+ ___56-[BLSHAggregateBacklightHost _addObserver:forBacklight:]_block_invoke
+ ___56-[BLSHSystemWakeTelemetry logTelemetryForRenderSession:]_block_invoke
+ ___58-[BLSHTelemetryService sendAnalyticsEvent:payloadBuilder:]_block_invoke
+ ___58-[BLSHTelemetryService sendAnalyticsEvent:payloadBuilder:]_block_invoke_2
+ ___62-[BLSHSystemWakeTelemetry backlight:didChangeAlwaysOnEnabled:]_block_invoke
+ ___BLSHTelemetryServiceWorkloop_block_invoke
+ ___block_descriptor_109_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_65_e8_32w_e5_v8?0lw32l8
+ _sharedTelemetryService.onceToken
+ _sharedTelemetryService.shared
- +[BLSHCoreAnalytics sendEventAsync:payloadBuilder:]
- +[BLSHCoreAnalytics sharedAnalyticsSender]
- +[BLSHCoreAnalytics workloop]
- -[BLSHAOTSystemWakeTelemetry .cxx_destruct]
- -[BLSHAOTSystemWakeTelemetry _resetAccumulatedMetrics]
- -[BLSHAOTSystemWakeTelemetry accumulateMetrics:]
- -[BLSHAOTSystemWakeTelemetry accumulateOffDuration:isAOT:]
- -[BLSHAOTSystemWakeTelemetry accumulateOnDuration:]
- -[BLSHAOTSystemWakeTelemetry backlight:didChangeAlwaysOnEnabled:]
- -[BLSHAOTSystemWakeTelemetry backlight:didUpdateToDisplayMode:fromDisplayMode:activeEvents:abortedEvents:]
- -[BLSHAOTSystemWakeTelemetry backlight:willUpdateToDisplayMode:fromDisplayMode:forEvents:abortedEvents:]
- -[BLSHAOTSystemWakeTelemetry dealloc]
- -[BLSHAOTSystemWakeTelemetry gatherTelemetryForWakeNumber:]
- -[BLSHAOTSystemWakeTelemetry logMetricsTimerFired]
- -[BLSHAOTSystemWakeTelemetry logTelemetryForInvalidation:]
- -[BLSHAOTSystemWakeTelemetry logTelemetryForRenderSession:]
- -[BLSHAOTSystemWakeTelemetry logTelemetryForRequestDates:]
- -[BLSHAOTSystemWakeTelemetry observesUpdateToDisplayMode]
- -[BLSHAOTSystemWakeTelemetry startObserving]
- -[BLSHAOTSystemWakeTelemetry stopObserving]
- -[BLSHCoreAnalytics sendEventAsync:payloadBuilder:]
- -[BLSHDisplayWakeTelemetry _commonInitWithTelemetrySource:analyticsRecorder:]
- -[BLSHDisplayWakeTelemetry initWithPlatformDelegate:telemetrySource:analyticsRecorder:]
- GCC_except_table23
- GCC_except_table25
- GCC_except_table27
- GCC_except_table39
- GCC_except_table48
- _OBJC_CLASS_$_BLSHAOTSystemWakeTelemetry
- _OBJC_CLASS_$_BLSHCoreAnalytics
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._accumulatedFlipbookLayoutDuration
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._accumulatedFlipbookRenderDuration
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._accumulatedMetrics
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._accumulatedSecondsDisplayOff
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._accumulatedSecondsDisplayOn
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._accumulatedSecondsShowingAOT
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._backlightOffStartTime
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._backlightOnStartTime
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._blsTelemetryEnabled
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._completedWakeNumber
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._currentMetrics
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._delegateFlags
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._didFinalLog
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._hasPoweredOnTime
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._isAOT
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._isTelemetryEnqueuedAtUtilityQOS
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._lastTelemtryAccumulateTime
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._loggedToTelemtryAccumulateTime
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._powerLogTelemetryIdentifier
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._serviceStarted
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._systemSleepObserver
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._systemWakeMetricsEventKey
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._timer
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._timerQueue
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._wakeNumber
- _OBJC_IVAR_$_BLSHAOTSystemWakeTelemetry._willSleepTime
- _OBJC_IVAR_$_BLSHDisplayWakeTelemetry._analyticsRecorder
- _OBJC_IVAR_$_BLSHDisplayWakeTelemetry._backlightEventPowerLogIdentifier
- _OBJC_METACLASS_$_BLSHAOTSystemWakeTelemetry
- _OBJC_METACLASS_$_BLSHCoreAnalytics
- __OBJC_$_CLASS_METHODS_BLSHCoreAnalytics
- __OBJC_$_INSTANCE_METHODS_BLSHAOTSystemWakeTelemetry
- __OBJC_$_INSTANCE_METHODS_BLSHCoreAnalytics
- __OBJC_$_INSTANCE_VARIABLES_BLSHAOTSystemWakeTelemetry
- __OBJC_$_PROP_LIST_BLSHAOTSystemWakeTelemetry
- __OBJC_$_PROTOCOL_CLASS_METHODS_BLSHCoreAnalyticsSending
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BLSHCoreAnalyticsSending
- __OBJC_$_PROTOCOL_METHOD_TYPES_BLSHCoreAnalyticsSending
- __OBJC_CLASS_PROTOCOLS_$_BLSHAOTSystemWakeTelemetry
- __OBJC_CLASS_PROTOCOLS_$_BLSHCoreAnalytics
- __OBJC_CLASS_RO_$_BLSHAOTSystemWakeTelemetry
- __OBJC_CLASS_RO_$_BLSHCoreAnalytics
- __OBJC_LABEL_PROTOCOL_$_BLSHCoreAnalyticsSending
- __OBJC_METACLASS_RO_$_BLSHAOTSystemWakeTelemetry
- __OBJC_METACLASS_RO_$_BLSHCoreAnalytics
- __OBJC_PROTOCOL_$_BLSHCoreAnalyticsSending
- ___104-[BLSHAOTSystemWakeTelemetry backlight:willUpdateToDisplayMode:fromDisplayMode:forEvents:abortedEvents:]_block_invoke
- ___104-[BLSHAOTSystemWakeTelemetry backlight:willUpdateToDisplayMode:fromDisplayMode:forEvents:abortedEvents:]_block_invoke_2
- ___29+[BLSHCoreAnalytics workloop]_block_invoke
- ___41-[BLSHBacklightStateMachine addObserver:]_block_invoke
- ___42+[BLSHCoreAnalytics sharedAnalyticsSender]_block_invoke
- ___42-[BLSHAggregateBacklightHost addObserver:]_block_invoke
- ___44-[BLSHAOTSystemWakeTelemetry startObserving]_block_invoke
- ___50-[BLSHAOTSystemWakeTelemetry logMetricsTimerFired]_block_invoke
- ___51+[BLSHCoreAnalytics sendEventAsync:payloadBuilder:]_block_invoke
- ___51+[BLSHCoreAnalytics sendEventAsync:payloadBuilder:]_block_invoke_2
- ___58-[BLSHAOTSystemWakeTelemetry logTelemetryForInvalidation:]_block_invoke
- ___59-[BLSHAOTSystemWakeTelemetry logTelemetryForRenderSession:]_block_invoke
- ___65-[BLSHAOTSystemWakeTelemetry backlight:didChangeAlwaysOnEnabled:]_block_invoke
- ___block_descriptor_109_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
- ___block_descriptor_48_e8_32w_e5_v8?0lw32l8
- __dispatch_source_type_timer
- __workloop
- _dispatch_source_cancel
- _dispatch_source_create
- _dispatch_source_set_event_handler
- _dispatch_source_set_timer
- _objc_release_x2
- _objc_release_x4
- _sharedAnalyticsSender.__analyticsSender
- _sharedAnalyticsSender.onceToken
- _workloop.onceToken
CStrings:
+ "%@"
+ "%@::%@"
+ "BLSHSystemWakeTelemetry startObserving with eventKey: %{public}@"
+ "BLSHTelemetryService: failed to create telemetry identifier for %{public}@"
+ "BLSHTelemetryServiceWorkLoop"
+ "CoreAnimation [CAFlipbook %@] hang detected – %.4lfs elapsed"
+ "[SystemWakeMetrics:%llu] didUpdateToDisplayMode:%{public}@ from:%{public}@ isActive:%{BOOL}u wasActive:%{BOOL}u isAOT:%{BOOL}u -> %{public}s"
+ "[SystemWakeMetrics:%llu] willUpdateToDisplayMode:%{public}@ from:%{public}@ events:%{public}@ (not accounted -- see didUpdateToDisplayMode:)"
+ "accounting edge"
+ "flipbook %{public}@ hang already resolved (main thread recovered); not panicking"
+ "flipbook %{public}@ hang already resolved; main thread recovered too late to abort"
+ "flipbook hang panic attempt failed:%d – re-arming abort"
+ "ignoring (no active/inactive change)"
+ "main thread recovered from flipbook %{public}@ hang; aborting: %{public}@"
- "BLSHCoreAnalyticsWorkLoop"
- "BLSHDisplayWakeTelemetry: failed to create telemetry identifier for Backlight::BacklightStateChange"
- "BLSHSystemWakeTelemetry startObserving with eventKey: %{public}@, powerLog: Backlight::SystemWakeMetrics"
- "BLSHSystemWakeTelemetry: failed to create telemetry identifier for Backlight::SystemWakeMetrics"
- "CoreAnimation [CAFlipbook %@] hang detected –\u00a0%.4lfs elapsed"
- "flipbook hang panic attempt failed:%d"
```
