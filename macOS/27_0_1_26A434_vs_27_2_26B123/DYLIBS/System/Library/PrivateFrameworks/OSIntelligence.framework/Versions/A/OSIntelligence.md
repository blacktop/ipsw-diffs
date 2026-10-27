## OSIntelligence

> `/System/Library/PrivateFrameworks/OSIntelligence.framework/Versions/A/OSIntelligence`

```diff

-286.0.0.0.0
-  __TEXT.__text: 0x19830
-  __TEXT.__objc_methlist: 0x2220
-  __TEXT.__const: 0x188
-  __TEXT.__cstring: 0x17e7
-  __TEXT.__oslogstring: 0x2024
-  __TEXT.__gcc_except_tab: 0x660
-  __TEXT.__unwind_info: 0xa40
+288.40.7.0.0
+  __TEXT.__text: 0x1c268
+  __TEXT.__objc_methlist: 0x24a8
+  __TEXT.__const: 0x1a0
+  __TEXT.__cstring: 0x1b7f
+  __TEXT.__oslogstring: 0x2357
+  __TEXT.__gcc_except_tab: 0x6a0
+  __TEXT.__unwind_info: 0xb08
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x198
+  __DATA_CONST.__const: 0x1e8
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1190
+  __DATA_CONST.__objc_selrefs: 0x1358
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xa8
-  __DATA_CONST.__got: 0x1a8
-  __AUTH_CONST.__const: 0xfe0
-  __AUTH_CONST.__cfstring: 0x1480
-  __AUTH_CONST.__objc_const: 0x3048
-  __AUTH_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__got: 0x1b0
+  __AUTH_CONST.__const: 0x1090
+  __AUTH_CONST.__cfstring: 0x18a0
+  __AUTH_CONST.__objc_const: 0x3378
+  __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x1dc
+  __DATA.__objc_ivar: 0x220
   __DATA.__data: 0x4e0
-  __DATA.__bss: 0x8
+  __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x730
   __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 930
-  Symbols:   1807
-  CStrings:  382
+  Functions: 1016
+  Symbols:   1947
+  CStrings:  443
 
Symbols:
+ +[_OSIBLMAnalyticsHandler allNotificationAnalyticsKeys]
+ +[_OSIBLMAnalyticsHandler analyticsKeyForNotificationDecision:]
+ -[_OSIBLMAnalyticsHandler historicalNotificationDataForDate:]
+ -[_OSIBLMAnalyticsHandler recordNotificationDecision:]
+ -[_OSIBLMAnalyticsHandler windowedNotificationSumsEndingDate:days:suffix:]
+ -[_OSIBLManager analyticsHandler]
+ -[_OSIBLManager earlyThermalNotifyToken]
+ -[_OSIBLManager forwardFeatureGateToPerformanceControl:]
+ -[_OSIBLManager forwardThermalGateToPerformanceControl]
+ -[_OSIBLManager isIBLMEnabledUnsynchronized]
+ -[_OSIBLManager isLowPowerModeActive]
+ -[_OSIBLManager isThermalMitigationEnabledByDefaults]
+ -[_OSIBLManager isThermallyElevated]
+ -[_OSIBLManager lowPowerModeNotificationHandler]
+ -[_OSIBLManager lpmNotifyToken]
+ -[_OSIBLManager registerForConsoleModeChanges]
+ -[_OSIBLManager registerForLowPowerModeChanges]
+ -[_OSIBLManager setAnalyticsHandler:]
+ -[_OSIBLManager setEarlyThermalNotifyToken:]
+ -[_OSIBLManager setIsLowPowerModeActive:]
+ -[_OSIBLManager setIsThermallyElevated:]
+ -[_OSIBLManager setLpmNotifyToken:]
+ -[_OSIBLManager setThermalPressureNotifyToken:]
+ -[_OSIBLManager setTrialThermalMitigationEnabled:]
+ -[_OSIBLManager thermalPressureNotifyToken]
+ -[_OSIBLManager trialThermalMitigationEnabled]
+ -[_OSICLPCInterface batteryLifeChallenged]
+ -[_OSICLPCInterface clpcMitigationsEnabled]
+ -[_OSICLPCInterface consoleModeActive]
+ -[_OSICLPCInterface featureEnabled]
+ -[_OSICLPCInterface lastPushedState]
+ -[_OSICLPCInterface lowPowerModeActive]
+ -[_OSICLPCInterface reconcile]
+ -[_OSICLPCInterface resolveAndActuate:]
+ -[_OSICLPCInterface setBatteryLifeChallenged:]
+ -[_OSICLPCInterface setClpcMitigationsEnabled:]
+ -[_OSICLPCInterface setConsoleModeActive:]
+ -[_OSICLPCInterface setFeatureEnabled:]
+ -[_OSICLPCInterface setLastPushedState:]
+ -[_OSICLPCInterface setLowPowerModeActive:]
+ -[_OSICLPCInterface setTestOverride:]
+ -[_OSICLPCInterface setThermalMitigationsEnabled:]
+ -[_OSICLPCInterface setThermallyChallenged:]
+ -[_OSICLPCInterface setViewfinderActive:]
+ -[_OSICLPCInterface shouldEngage]
+ -[_OSICLPCInterface stateDescription]
+ -[_OSICLPCInterface testOverride]
+ -[_OSICLPCInterface thermalMitigationsEnabled]
+ -[_OSICLPCInterface thermallyChallenged]
+ -[_OSICLPCInterface updateCLPCMitigationsEnabled:]
+ -[_OSICLPCInterface updateFeatureEnabled:]
+ -[_OSICLPCInterface updateSource:engaged:]
+ -[_OSICLPCInterface updateSuppressor:active:]
+ -[_OSICLPCInterface updateTestOverride:]
+ -[_OSICLPCInterface updateThermalMitigationsEnabled:]
+ -[_OSICLPCInterface viewfinderActive]
+ GCC_except_table46
+ OBJC_IVAR_$__OSIBLManager._analyticsHandler
+ OBJC_IVAR_$__OSIBLManager._earlyThermalNotifyToken
+ OBJC_IVAR_$__OSIBLManager._isLowPowerModeActive
+ OBJC_IVAR_$__OSIBLManager._isThermallyElevated
+ OBJC_IVAR_$__OSIBLManager._lpmNotifyToken
+ OBJC_IVAR_$__OSIBLManager._thermalPressureNotifyToken
+ OBJC_IVAR_$__OSIBLManager._trialThermalMitigationEnabled
+ OBJC_IVAR_$__OSICLPCInterface._batteryLifeChallenged
+ OBJC_IVAR_$__OSICLPCInterface._clpcMitigationsEnabled
+ OBJC_IVAR_$__OSICLPCInterface._consoleModeActive
+ OBJC_IVAR_$__OSICLPCInterface._featureEnabled
+ OBJC_IVAR_$__OSICLPCInterface._lastPushedState
+ OBJC_IVAR_$__OSICLPCInterface._lowPowerModeActive
+ OBJC_IVAR_$__OSICLPCInterface._testOverride
+ OBJC_IVAR_$__OSICLPCInterface._thermalMitigationsEnabled
+ OBJC_IVAR_$__OSICLPCInterface._thermallyChallenged
+ OBJC_IVAR_$__OSICLPCInterface._viewfinderActive
+ __42-[_OSICLPCInterface updateSource:engaged:]_block_invoke
+ __45-[_OSICLPCInterface updateSuppressor:active:]_block_invoke
+ __46-[_OSIBLManager registerForConsoleModeChanges]_block_invoke
+ __47-[_OSIBLManager registerForLowPowerModeChanges]_block_invoke
+ ___25-[_OSICLPCInterface stop]_block_invoke
+ ___30-[_OSICLPCInterface reconcile]_block_invoke
+ ___32-[_OSIBLManager handleCallback:]_block_invoke_2
+ ___37-[_OSICLPCInterface stateDescription]_block_invoke
+ ___40-[_OSICLPCInterface updateTestOverride:]_block_invoke
+ ___42-[_OSICLPCInterface updateFeatureEnabled:]_block_invoke
+ ___42-[_OSICLPCInterface updateSource:engaged:]_block_invoke
+ ___45-[_OSICLPCInterface updateSuppressor:active:]_block_invoke
+ ___46-[_OSIBLManager registerForConsoleModeChanges]_block_invoke
+ ___47-[_OSIBLManager registerForLowPowerModeChanges]_block_invoke
+ ___50-[_OSICLPCInterface updateCLPCMitigationsEnabled:]_block_invoke
+ ___53-[_OSICLPCInterface updateThermalMitigationsEnabled:]_block_invoke
+ ___54-[_OSIBLMAnalyticsHandler recordNotificationDecision:]_block_invoke
+ ___55+[_OSIBLMAnalyticsHandler allNotificationAnalyticsKeys]_block_invoke
+ ___61-[_OSIBLMAnalyticsHandler historicalNotificationDataForDate:]_block_invoke
+ ___74-[_OSIBLMAnalyticsHandler windowedNotificationSumsEndingDate:days:suffix:]_block_invoke
+ ___NSDictionary0__struct
+ ___block_descriptor_48_e8_32s40s_e5_v8?0l
+ ___block_descriptor_49_e8_32s_e5_v8?0l
+ ___block_descriptor_64_e8_32s40s48s56s_e39_v32?0"NSString"8"NSDictionary"16^B24l
+ ___copy_helper_block_e8_32s40s
+ _dispatch_assert_queue$V2
+ _objc_msgSend$allNotificationAnalyticsKeys
+ _objc_msgSend$analyticsKeyForNotificationDecision:
+ _objc_msgSend$batteryLifeChallenged
+ _objc_msgSend$clpcMitigationsEnabled
+ _objc_msgSend$consoleModeActive
+ _objc_msgSend$featureEnabled
+ _objc_msgSend$forwardFeatureGateToPerformanceControl:
+ _objc_msgSend$forwardThermalGateToPerformanceControl
+ _objc_msgSend$historicalNotificationDataForDate:
+ _objc_msgSend$isIBLMEnabledUnsynchronized
+ _objc_msgSend$isThermalMitigationEnabledByDefaults
+ _objc_msgSend$lastPushedState
+ _objc_msgSend$lowPowerModeActive
+ _objc_msgSend$lowPowerModeNotificationHandler
+ _objc_msgSend$mitigationOption
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$resolveAndActuate:
+ _objc_msgSend$setBatteryLifeChallenged:
+ _objc_msgSend$setClpcMitigationsEnabled:
+ _objc_msgSend$setConsoleModeActive:
+ _objc_msgSend$setFeatureEnabled:
+ _objc_msgSend$setLastPushedState:
+ _objc_msgSend$setLowPowerModeActive:
+ _objc_msgSend$setTestOverride:
+ _objc_msgSend$setThermalMitigationsEnabled:
+ _objc_msgSend$setThermallyChallenged:
+ _objc_msgSend$setViewfinderActive:
+ _objc_msgSend$shouldEngage
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$testOverride
+ _objc_msgSend$thermalMitigationsEnabled
+ _objc_msgSend$thermallyChallenged
+ _objc_msgSend$updateCLPCMitigationsEnabled:
+ _objc_msgSend$updateFeatureEnabled:
+ _objc_msgSend$updateSource:engaged:
+ _objc_msgSend$updateSuppressor:active:
+ _objc_msgSend$updateTestOverride:
+ _objc_msgSend$updateThermalMitigationsEnabled:
+ _objc_msgSend$viewfinderActive
+ _objc_msgSend$windowedNotificationSumsEndingDate:days:suffix:
+ allNotificationAnalyticsKeys.keys
+ allNotificationAnalyticsKeys.onceToken
- -[_OSICLPCInterface updatePerformanceControlWithMitigation:]
- _objc_msgSend$updatePerformanceControlWithMitigation:
CStrings:
+ "$"
+ "CLPCInterface"
+ "Failed to register for console mode changes"
+ "Failed to register for low power mode changes"
+ "IBLMNotificationDecision"
+ "IBLM_ThermalMitigationEnabled"
+ "Last30Days"
+ "Last7Days"
+ "Low Power Mode is now %{public}s"
+ "NotificationDecision"
+ "Perf mitigation Trial gate is now %{public}s"
+ "Perf mitigation feature gate is now %{public}s"
+ "Perf mitigation source %ld is now %{public}s"
+ "Perf mitigation suppressor %ld is now %{public}s"
+ "Perf mitigation test override cleared"
+ "Perf mitigation test override forcing %{public}s"
+ "Perf mitigation thermal Trial gate is now %{public}s"
+ "Reconciling perf mitigation state with CLPC"
+ "Recorded notification decision %{public}@ for %@ (now %ld)"
+ "Thermal perf mitigation gate: trial %{public}d, defaults %{public}d -> %{public}d"
+ "Unknown perf mitigation source %ld"
+ "Unknown perf mitigation suppressor %ld"
+ "Unsupported notification decision for analytics %ld"
+ "\\\"c"
+ "active"
+ "batteryLifeChallenged"
+ "clear"
+ "closed"
+ "clpcMitigationsEnabled"
+ "com.apple.osintelligence.clpcinterface"
+ "com.apple.osintelligence.iblm.recordNotificationDecision"
+ "com.apple.system.lowpowermode"
+ "consoleModeActive"
+ "disengaged"
+ "engaged"
+ "featureEnabled"
+ "historicalIBLMNotificationCounts"
+ "lowPowerModeActive"
+ "mitigationOption"
+ "never pushed"
+ "none"
+ "notificationEvaluationCount"
+ "notificationSuppressedByBackstop"
+ "notificationSuppressedByCooldown"
+ "notificationSuppressedByDisabled"
+ "notificationSuppressedByInsufficientData"
+ "notificationSuppressedByNotUnusual"
+ "notificationSuppressedBySlotOutOfRange"
+ "notificationSuppressedByStartHour"
+ "notify_get_state() for low power mode failed with error %u"
+ "off"
+ "on"
+ "onboardingNotificationCount"
+ "open"
+ "shouldEngage"
+ "testOverride"
+ "thermalMitigationEnabled"
+ "thermalMitigationsEnabled"
+ "thermalSupported"
+ "thermallyChallenged"
+ "unusualDrainNotificationCount"
+ "viewfinderActive"
- ";\"c"
```
