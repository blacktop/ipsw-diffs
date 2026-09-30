## PerformanceTraceModule

> `/System/Library/ControlCenter/Bundles/PerformanceTraceModule.bundle/PerformanceTraceModule`

```diff

-600.5.3.100.0
-  __TEXT.__text: 0xc90
-  __TEXT.__auth_stubs: 0x1a0
-  __TEXT.__objc_methlist: 0x2c4
-  __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x8e
-  __TEXT.__oslogstring: 0x36
-  __TEXT.__unwind_info: 0xb0
+645.102.0.0.0
+  __TEXT.__text: 0x2c60
+  __TEXT.__auth_stubs: 0x280
+  __TEXT.__objc_methlist: 0x424
+  __TEXT.__const: 0x70
+  __TEXT.__gcc_except_tab: 0x1c
+  __TEXT.__cstring: 0x23a
+  __TEXT.__oslogstring: 0x4cd
+  __TEXT.__unwind_info: 0x120
   __TEXT.__objc_classname: 0x7a
-  __TEXT.__objc_methname: 0x788
-  __TEXT.__objc_methtype: 0x328
-  __TEXT.__objc_stubs: 0x420
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0xa0
+  __TEXT.__objc_methname: 0xe39
+  __TEXT.__objc_methtype: 0x344
+  __TEXT.__objc_stubs: 0x9e0
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x240
+  __DATA_CONST.__objc_selrefs: 0x3d8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xd8
-  __AUTH_CONST.__cfstring: 0x80
-  __AUTH_CONST.__objc_const: 0x4e8
+  __AUTH_CONST.__auth_got: 0x150
+  __AUTH_CONST.__cfstring: 0x240
+  __AUTH_CONST.__objc_const: 0x5a8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x18
+  __DATA.__objc_ivar: 0x24
   __DATA.__data: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/PerformanceTrace.framework/PerformanceTrace
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DE93E6CD-90AD-3B3B-8DAD-BA0D6DE2F55F
-  Functions: 29
-  Symbols:   56
-  CStrings:  136
+  UUID: 8D63C8F1-5898-3DB7-9F99-162A998694EC
+  Functions: 76
+  Symbols:   75
+  CStrings:  258
 
Symbols:
+ _OBJC_CLASS_$_CCUIMenuModuleItem
+ _OBJC_CLASS_$_CCUIMenuModuleViewController
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_PTPassiveTraceConfig
+ _OBJC_CLASS_$_UIView
+ _OBJC_METACLASS_$_CCUIMenuModuleViewController
+ __Unwind_Resume
+ ___objc_personality_v0
+ __os_log_impl
+ _dispatch_get_global_queue
+ _kPTPassiveTracePlanNameLightweightPowerMetrics
+ _kPTPassiveTracePlanNamePassive
+ _kPTTracePlanNameCustom
+ _objc_alloc
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_enumerationMutation
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_release_x24
+ _objc_release_x25
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x8
+ _objc_unsafeClaimAutoreleasedReturnValue
- OBJC_IVAR_$_CCUIPerformanceTraceModuleViewController._performanceTraceSession
- OBJC_IVAR_$_CCUIPerformanceTraceModuleViewController._traceStartScenes
- OBJC_IVAR_$_CCUIPerformanceTraceModuleViewController.state
- _OBJC_CLASS_$_CCUIButtonModuleViewController
- _OBJC_METACLASS_$_CCUIButtonModuleViewController
- _objc_retainBlock
CStrings:
+ "$"
+ "@\"NSString\""
+ "@24@0:8Q16"
+ "B"
+ "B8@?0"
+ "Button tapped (current state is %@ (%lu))"
+ "Button tapped while state was not one of Running or Not Running: %@ (%lu)"
+ "CONTROL_CENTER_STATUS_PERFORMANCE_TRACE_PROCESSING_ERROR"
+ "CONTROL_CENTER_STATUS_PERFORMANCE_TRACE_START_ERROR"
+ "CONTROL_CENTER_STATUS_PERFORMANCE_TRACE_STOP_ERROR"
+ "CONTROL_CENTER_SUBTITLE_PERFORMANCE_TRACE_PROCESSING"
+ "CONTROL_CENTER_SUBTITLE_PERFORMANCE_TRACE_RUNNING"
+ "CONTROL_CENTER_SUBTITLE_PERFORMANCE_TRACE_STARTING"
+ "Collecting passive trace"
+ "Collecting power metrics passive trace"
+ "Completed passive trace collection"
+ "Completed power metrics passive trace collection"
+ "Displaying alert for completed trace"
+ "Error on Performance Trace didComplete: %{public}@"
+ "Error on Performance Trace didStart: %{public}@"
+ "Error on Performance Trace didStop: %{public}@"
+ "Failed to collect passive trace for %{public}@ config: %{public}@"
+ "Failed to create passive trace config: %{public}@"
+ "Failed to start passive trace for %{public}@ config: %{public}@"
+ "Getting FG scene identifiers"
+ "Not Running"
+ "Performance Trace didComplete"
+ "Performance Trace didStart"
+ "Performance Trace didStop"
+ "Preparing to collect passive trace"
+ "Processing"
+ "Requesting alert for completed trace"
+ "Running"
+ "Selected trace plan (%{public}@) does not support stopping recording"
+ "Starting"
+ "Starting power metrics passive trace"
+ "Starting recording with plan %{public}@"
+ "State changed from %{public}@ (%lu) to %{public}@ (%lu)"
+ "Stopping"
+ "Stopping power metrics passive trace"
+ "Stopping recording with plan %{public}@"
+ "T@\"NSArray\",&,N,V_fgSceneIdentifiersAtTraceStart"
+ "T@\"NSArray\",&,N,V_supportedTracePlanNames"
+ "T@\"NSString\",&,N,V_selectedTracePlanName"
+ "T@\"PTTraceSession\",&,N,V_performanceTraceSession"
+ "TB,N,V_selectedTracePlanIsPassive"
+ "TB,N,V_selectedTracePlanIsPassivePowerMetrics"
+ "TQ,N,V_state"
+ "Unknown"
+ "Updating button glyph"
+ "Updating state"
+ "Updating state and nil'ing Performance Trace delegate and session"
+ "User selected plan named %{public}@"
+ "_cleanupSessionAndUpdateState:"
+ "_collectPassiveTrace"
+ "_fgSceneIdentifiersAtTraceStart"
+ "_localizedString:"
+ "_makeTracePlanNameMenuItem:"
+ "_passiveTraceConfig"
+ "_recreateMenu"
+ "_selectedTracePlanIsPassive"
+ "_selectedTracePlanIsPassivePowerMetrics"
+ "_selectedTracePlanName"
+ "_startRecordingPowerMetricsPassiveTrace"
+ "_startRecordingRegularTrace"
+ "_state"
+ "_stopRecordingPowerMetricsPassiveTrace"
+ "_stopRecordingRegularTrace"
+ "_supportedTracePlanNames"
+ "_updateGlyph"
+ "_updatePlanNameConvenienceProperties"
+ "_updateSubtitle:"
+ "addObject:"
+ "applySetting:"
+ "availableTracePlanNames"
+ "bolt.badge.clock"
+ "collectLookbackIntervalWithTraceNamePrefix:triggerUserNotification:errorOut:"
+ "collectThenClearCurrentSettingWithTraceNamePrefix:triggerUserNotification:errorOut:"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "dealloc"
+ "displayNameForState:"
+ "displayNameForTracePlanName:"
+ "fgSceneIdentifiersAtTraceStart"
+ "initWithTitle:identifier:handler:"
+ "isEqualToString:"
+ "isPassiveTracePlanName:"
+ "isPowerMetricsPassiveTracePlanName:"
+ "performWithoutAnimation:"
+ "performanceTraceSession"
+ "selectedTracePlanIsPassive"
+ "selectedTracePlanIsPassivePowerMetrics"
+ "selectedTracePlanName"
+ "setFgSceneIdentifiersAtTraceStart:"
+ "setIndentation:"
+ "setMenuItems:"
+ "setPerformanceTraceSession:"
+ "setSelectedTracePlanIsPassive:"
+ "setSelectedTracePlanIsPassivePowerMetrics:"
+ "setSelectedTracePlanName:"
+ "setSelectedValueText:"
+ "setState:"
+ "setSupportedTracePlanNames:"
+ "setTraceRecordArgs:"
+ "setUserSelectedTracePlanName:"
+ "setValueText:"
+ "sharedConfig:"
+ "square.and.arrow.down.badge.clock"
+ "supportedTracePlanNames"
+ "userSelectedTracePlanName"
+ "userSpecifiedCustomTracePlanArguments"
+ "v20@0:8B16"
+ "v24@0:8Q16"
+ "viewWillAppear:"
+ "willTransitionToExpandedContentMode:"
- "T@\"CCUIContentModuleContext\",&,N,V_contentModuleContext"
- "_traceStartScenes"
- "d16@0:8"
- "displayTraceCompletedAlertWithTraceFileURL failed: %@"
- "preferredExpandedContentHeight"
- "v20@0:8i16"
- "viewDidLoad"

```
