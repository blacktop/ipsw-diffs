## PowerlogHelperdOperators

> `/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_nlclslist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-3486.0.81.502.4
-  __TEXT.__text: 0x1d96a8
-  __TEXT.__objc_methlist: 0x10928
-  __TEXT.__const: 0x6f0
-  __TEXT.__cstring: 0x26211
-  __TEXT.__oslogstring: 0x14a8b
-  __TEXT.__gcc_except_tab: 0x24e8
+3486.2.4.0.0
+  __TEXT.__text: 0x1dc330
+  __TEXT.__objc_methlist: 0x10ae0
+  __TEXT.__const: 0x700
+  __TEXT.__cstring: 0x2641e
+  __TEXT.__oslogstring: 0x14c39
+  __TEXT.__gcc_except_tab: 0x258c
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x3b30
+  __TEXT.__unwind_info: 0x3b88
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4448
-  __DATA_CONST.__objc_classlist: 0x388
+  __DATA_CONST.__const: 0x4480
+  __DATA_CONST.__objc_classlist: 0x390
   __DATA_CONST.__objc_nlclslist: 0x108
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xac90
+  __DATA_CONST.__objc_selrefs: 0xad78
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x2c8
-  __DATA_CONST.__objc_arraydata: 0x15990
-  __DATA_CONST.__got: 0xf50
-  __AUTH_CONST.__const: 0x1a20
-  __AUTH_CONST.__cfstring: 0x335c0
-  __AUTH_CONST.__objc_const: 0x15ac8
+  __DATA_CONST.__objc_arraydata: 0x159f0
+  __DATA_CONST.__got: 0xf70
+  __AUTH_CONST.__const: 0x1a40
+  __AUTH_CONST.__cfstring: 0x33740
+  __AUTH_CONST.__objc_const: 0x15dd0
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__objc_intobj: 0x2898
-  __AUTH_CONST.__objc_dictobj: 0x3a20
+  __AUTH_CONST.__objc_intobj: 0x28b0
+  __AUTH_CONST.__objc_dictobj: 0x3a70
   __AUTH_CONST.__objc_doubleobj: 0xb90
   __AUTH_CONST.__objc_arrayobj: 0x2e38
   __AUTH_CONST.__auth_got: 0xdf8
-  __AUTH.__objc_data: 0xaf0
-  __DATA.__objc_ivar: 0x15cc
+  __AUTH.__objc_data: 0xb40
+  __DATA.__objc_ivar: 0x15f8
   __DATA.__data: 0x580
-  __DATA.__bss: 0x2098
+  __DATA.__bss: 0x20b8
   __DATA.__common: 0x74
   __DATA_DIRTY.__objc_data: 0x1860
   __DATA_DIRTY.__data: 0x10

   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
   - /System/Library/PrivateFrameworks/ApplePhotonDetectorServices.framework/ApplePhotonDetectorServices
   - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
+  - /System/Library/PrivateFrameworks/AttentionAwareness.framework/AttentionAwareness
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices
   - /System/Library/PrivateFrameworks/CPMS.framework/CPMS

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 8565
-  Symbols:   16015
-  CStrings:  8920
+  Functions: 8612
+  Symbols:   16110
+  CStrings:  8944
 
Symbols:
+ +[PLBatteryAgent entryEventPointDefinitionBatteryShutdownPack]
+ +[PLDisplayAgent _entryEventBackwardDefinitionAPLStatsWithLogSelector:]
+ +[PLUtilities getHardwarePerfKind:]
+ -[KernelTaskMonitorStats cpu_energy_m]
+ -[KernelTaskMonitorStats setCpu_energy_m:]
+ -[PLBatteryAgent logBatteryShutdownToCA:forBatteryPack:]
+ -[PLBatteryAgent logEventPointBatteryShutdownWithRawData:packID:systemShutdownData:]
+ -[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility .cxx_destruct]
+ -[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility cleanUp]
+ -[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility coalesce]
+ -[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility configure:]
+ -[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility criticalDays]
+ -[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility dependencies]
+ -[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility end]
+ -[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility responderService]
+ -[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility result]
+ -[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility run]
+ -[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility setCriticalDays:]
+ -[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility setEnd:]
+ -[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility setResponderService:]
+ -[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility setStart:]
+ -[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility setUiLevelEntries:]
+ -[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility start]
+ -[PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility uiLevelEntries]
+ -[PLContextualizedMetricData reducedAccuracySeconds]
+ -[PLContextualizedMetricData setReducedAccuracySeconds:]
+ -[PLPowerMetricMonitorService processWideAgentSetupDone]
+ -[PLPowerMetricMonitorService setProcessWideAgentSetupDone:]
+ -[PLSpringBoardAgent attentionAwarenessClient]
+ -[PLSpringBoardAgent lastUserEventMediaTime]
+ -[PLSpringBoardAgent setAttentionAwarenessClient:]
+ -[PLSpringBoardAgent setLastUserEventMediaTime:]
+ -[PLSpringBoardAgent startAttentionAwarenessClient]
+ -[PLSpringBoardAgent stopAttentionAwarenessClient]
+ -[PLStateMetricsInput locationReducedAccuracySeconds]
+ -[PLStateMetricsInput setLocationReducedAccuracySeconds:]
+ GCC_except_table119
+ GCC_except_table136
+ GCC_except_table140
+ GCC_except_table158
+ GCC_except_table175
+ GCC_except_table187
+ GCC_except_table193
+ GCC_except_table203
+ GCC_except_table248
+ GCC_except_table257
+ GCC_except_table260
+ GCC_except_table262
+ GCC_except_table271
+ GCC_except_table278
+ GCC_except_table283
+ GCC_except_table325
+ GCC_except_table328
+ GCC_except_table332
+ _OBJC_CLASS_$_AWAttentionAwarenessClient
+ _OBJC_CLASS_$_AWAttentionAwarenessConfiguration
+ _OBJC_CLASS_$_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility
+ _OBJC_IVAR_$_KernelTaskMonitorStats._cpu_energy_m
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility._criticalDays
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility._end
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility._responderService
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility._start
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility._uiLevelEntries
+ _OBJC_IVAR_$_PLContextualizedMetricData._reducedAccuracySeconds
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._processWideAgentSetupDone
+ _OBJC_IVAR_$_PLSpringBoardAgent._attentionAwarenessClient
+ _OBJC_IVAR_$_PLSpringBoardAgent._lastUserEventMediaTime
+ _OBJC_IVAR_$_PLStateMetricsInput._locationReducedAccuracySeconds
+ _OBJC_METACLASS_$_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility
+ __OBJC_$_INSTANCE_METHODS_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility
+ __OBJC_$_INSTANCE_VARIABLES_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility
+ __OBJC_$_PROP_LIST_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility
+ __OBJC_CLASS_PROTOCOLS_$_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility
+ __OBJC_CLASS_RO_$_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility
+ __OBJC_METACLASS_RO_$_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility
+ ___35+[PLUtilities getHardwarePerfKind:]_block_invoke
+ ___51-[PLSpringBoardAgent startAttentionAwarenessClient]_block_invoke
+ ___56-[PLBatteryAgent logBatteryShutdownToCA:forBatteryPack:]_block_invoke
+ ___84-[PLBatteryAgent logEventPointBatteryShutdownWithRawData:packID:systemShutdownData:]_block_invoke
+ ___84-[PLBatteryAgent logEventPointBatteryShutdownWithRawData:packID:systemShutdownData:]_block_invoke_2
+ ___block_descriptor_40_e8_32w_e26_v16?0"AWAttentionEvent"8lw32l8
+ ___snprintf_chk
+ _getHardwarePerfKind:.cache
+ _getHardwarePerfKind:.cacheOnce
+ _kCLLocationAccuracyReduced
+ _kPLBatteryAgentEventPointNameBatteryShutdownPack0
+ _kPLBatteryAgentStringLastShutdownSystemTimestamp0
+ _kPLBatteryAgentStringLastShutdownSystemTimestampSystem
+ _logEventPointBatteryShutdownWithRawData:packID:systemShutdownData:.classDebugEnabled
+ _logEventPointBatteryShutdownWithRawData:packID:systemShutdownData:.defaultOnce
+ _objc_msgSend$_entryEventBackwardDefinitionAPLStatsWithLogSelector:
+ _objc_msgSend$attentionAwarenessClient
+ _objc_msgSend$cleanUp
+ _objc_msgSend$cpu_energy_m
+ _objc_msgSend$criticalDays
+ _objc_msgSend$entryEventPointDefinitionBatteryShutdownPack
+ _objc_msgSend$eventMask
+ _objc_msgSend$getHardwarePerfKind:
+ _objc_msgSend$initWithCumulativeBestAccuracyTimeMeasurement:cumulativeBestAccuracyForNavigationTimeMeasurement:nearestTenMetersAccuracyTimeMeasurement:hundredMetersAccuracyTimeMeasurement:kilometerAccuracyTimeMeasurement:threeKilometerAccuracyTimeMeasurement:reducedAccuracyTimeMeasurement:
+ _objc_msgSend$invalidateWithError:
+ _objc_msgSend$lastUserEventMediaTime
+ _objc_msgSend$locationReducedAccuracySeconds
+ _objc_msgSend$logBatteryShutdownToCA:forBatteryPack:
+ _objc_msgSend$logEventPointBatteryShutdownWithRawData:packID:systemShutdownData:
+ _objc_msgSend$processWideAgentSetupDone
+ _objc_msgSend$reducedAccuracySeconds
+ _objc_msgSend$resumeWithError:
+ _objc_msgSend$setAttentionAwarenessClient:
+ _objc_msgSend$setAttentionLostTimeout:
+ _objc_msgSend$setConfiguration:shouldReset:error:
+ _objc_msgSend$setCpu_energy_m:
+ _objc_msgSend$setCriticalDays:
+ _objc_msgSend$setEventHandlerWithQueue:block:
+ _objc_msgSend$setEventMask:
+ _objc_msgSend$setIdentifier:
+ _objc_msgSend$setLastUserEventMediaTime:
+ _objc_msgSend$setLocationReducedAccuracySeconds:
+ _objc_msgSend$setProcessWideAgentSetupDone:
+ _objc_msgSend$startAttentionAwarenessClient
+ _objc_msgSend$stopAttentionAwarenessClient
+ _startAttentionAwarenessClient.classDebugEnabled
+ _startAttentionAwarenessClient.defaultOnce
- -[PLBatteryAgent logBatteryShutdownToCA:]
- GCC_except_table117
- GCC_except_table135
- GCC_except_table139
- GCC_except_table157
- GCC_except_table174
- GCC_except_table186
- GCC_except_table192
- GCC_except_table247
- GCC_except_table256
- GCC_except_table259
- GCC_except_table261
- GCC_except_table269
- GCC_except_table275
- GCC_except_table281
- GCC_except_table323
- GCC_except_table326
- GCC_except_table330
- _BKSHIDServicesLastUserEventTime
- ___41-[PLBatteryAgent logBatteryShutdownToCA:]_block_invoke
- ___46-[PLBatteryAgent logEventPointBatteryShutdown]_block_invoke
- ___46-[PLBatteryAgent logEventPointBatteryShutdown]_block_invoke_2
- _kPLBatteryAgentStringLastShutdownSystemTimestamp
- _logEventPointBatteryShutdown.classDebugEnabled
- _logEventPointBatteryShutdown.defaultOnce
- _objc_msgSend$initWithCumulativeBestAccuracyTimeMeasurement:cumulativeBestAccuracyForNavigationTimeMeasurement:nearestTenMetersAccuracyTimeMeasurement:hundredMetersAccuracyTimeMeasurement:kilometerAccuracyTimeMeasurement:threeKilometerAccuracyTimeMeasurement:
- _objc_msgSend$logBatteryShutdownToCA:
CStrings:
+ "-[PLBatteryAgent logEventPointBatteryShutdownWithRawData:packID:systemShutdownData:]"
+ "-[PLSpringBoardAgent startAttentionAwarenessClient]"
+ "AppleSmartBatteryPack"
+ "AttentionAwareness unavailable on this image; autolock energy will use fallback timing"
+ "Battery metrics already set up."
+ "BatteryShutdown: Failed to get AppleSmartBatteryPack data with result=%x"
+ "BatteryShutdown: log entry for pack=%@"
+ "BatteryShutdownPack0"
+ "CPUEnergyM"
+ "Failed to configure AttentionAwareness client: %{public}@"
+ "Failed to resume AttentionAwareness client: %{public}@"
+ "Failed to retrieve power sources list handle."
+ "LastShutdownSystemTimestampSystem"
+ "No data in battUI for dormancy eligibility"
+ "Not enough data for dormancy eligibility (need %d days)"
+ "Number of critical days: %d"
+ "PDTP"
+ "ReducedAccuracy"
+ "com.apple.ImagePlaygroundPoster.ImagePlaygroundPosterExtension"
+ "com.apple.powerlog.autolock"
+ "hw.perflevel%u.name"
+ "locationReducedAccuracySeconds"
+ "optimizeBatteryPromptEligibility"
+ "reducedAccuracy"
+ "reducedAccuracySeconds"
+ "v16@?0@\"AWAttentionEvent\"8"
+ "\xbd"
+ "\xf0\xf0Ec"
- "-[PLBatteryAgent logEventPointBatteryShutdown]"
- "A"
- "\xad"
- "\xf0\xf05c"
```
