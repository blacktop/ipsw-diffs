## PowerlogHelperdOperators

> `/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/Versions/A/PowerlogHelperdOperators`

```diff

-3486.0.81.501.3
-  __TEXT.__text: 0x1106b4
-  __TEXT.__objc_methlist: 0xa550
-  __TEXT.__const: 0x4a0
-  __TEXT.__cstring: 0x16695
-  __TEXT.__oslogstring: 0xaeca
-  __TEXT.__gcc_except_tab: 0x1c94
-  __TEXT.__unwind_info: 0x2548
+3486.1.2.0.0
+  __TEXT.__text: 0x112c6c
+  __TEXT.__objc_methlist: 0xa6a0
+  __TEXT.__const: 0x4b0
+  __TEXT.__cstring: 0x1679c
+  __TEXT.__oslogstring: 0xafe7
+  __TEXT.__gcc_except_tab: 0x1cf4
+  __TEXT.__unwind_info: 0x2580
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2228
-  __DATA_CONST.__objc_classlist: 0x228
+  __DATA_CONST.__const: 0x2238
+  __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_nlclslist: 0xb0
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7220
+  __DATA_CONST.__objc_selrefs: 0x7288
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1d0
-  __DATA_CONST.__objc_arraydata: 0x2a98
-  __DATA_CONST.__got: 0xab0
-  __AUTH_CONST.__const: 0x2ba8
-  __AUTH_CONST.__cfstring: 0x206a0
-  __AUTH_CONST.__objc_const: 0xd240
+  __DATA_CONST.__objc_arraydata: 0x2af8
+  __DATA_CONST.__got: 0xac0
+  __AUTH_CONST.__const: 0x2bc8
+  __AUTH_CONST.__cfstring: 0x207a0
+  __AUTH_CONST.__objc_const: 0xd4b8
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x640
-  __AUTH_CONST.__objc_intobj: 0x1410
-  __AUTH_CONST.__objc_dictobj: 0x1e28
+  __AUTH_CONST.__objc_intobj: 0x1428
+  __AUTH_CONST.__objc_dictobj: 0x1e78
   __AUTH_CONST.__objc_arrayobj: 0xc90
-  __AUTH_CONST.__auth_got: 0xb70
-  __AUTH.__objc_data: 0x960
-  __DATA.__objc_ivar: 0xd64
+  __AUTH_CONST.__auth_got: 0xb78
+  __AUTH.__objc_data: 0x9b0
+  __DATA.__objc_ivar: 0xd84
   __DATA.__data: 0x3a0
-  __DATA.__bss: 0xe40
+  __DATA.__bss: 0xe50
   __DATA.__common: 0x74
   __DATA_DIRTY.__objc_data: 0xc30
   __DATA_DIRTY.__bss: 0x2b8

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/_LocationEssentials.framework/Versions/A/_LocationEssentials
   - /System/Library/PrivateFrameworks/AFKUser.framework/Versions/A/AFKUser
+  - /System/Library/PrivateFrameworks/AttentionAwareness.framework/Versions/A/AttentionAwareness
   - /System/Library/PrivateFrameworks/CPMS.framework/Versions/A/CPMS
   - /System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/Versions/A/CloudSubscriptionFeatures
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5255
-  Symbols:   10568
-  CStrings:  5446
+  Functions: 5290
+  Symbols:   10632
+  CStrings:  5461
 
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
+ -[PLPowerMetricMonitorService processWideAgentSetupDone]
+ -[PLPowerMetricMonitorService setProcessWideAgentSetupDone:]
+ -[PLStateMetricsInput locationReducedAccuracySeconds]
+ -[PLStateMetricsInput setLocationReducedAccuracySeconds:]
+ GCC_except_table113
+ GCC_except_table140
+ GCC_except_table143
+ GCC_except_table149
+ GCC_except_table195
+ GCC_except_table202
+ GCC_except_table204
+ GCC_except_table229
+ GCC_except_table233
+ GCC_except_table242
+ GCC_except_table248
+ GCC_except_table252
+ GCC_except_table296
+ GCC_except_table299
+ GCC_except_table303
+ GCC_except_table88
+ OBJC_IVAR_$_KernelTaskMonitorStats._cpu_energy_m
+ OBJC_IVAR_$_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility._criticalDays
+ OBJC_IVAR_$_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility._end
+ OBJC_IVAR_$_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility._responderService
+ OBJC_IVAR_$_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility._start
+ OBJC_IVAR_$_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility._uiLevelEntries
+ OBJC_IVAR_$_PLPowerMetricMonitorService._processWideAgentSetupDone
+ OBJC_IVAR_$_PLStateMetricsInput._locationReducedAccuracySeconds
+ _OBJC_CLASS_$_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility
+ _OBJC_METACLASS_$_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility
+ __OBJC_$_INSTANCE_METHODS_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility
+ __OBJC_$_INSTANCE_VARIABLES_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility
+ __OBJC_$_PROP_LIST_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility
+ __OBJC_CLASS_PROTOCOLS_$_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility
+ __OBJC_CLASS_RO_$_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility
+ __OBJC_METACLASS_RO_$_PLBatteryUIResponseTypeOptimizeBatteryPromptEligibility
+ ___35+[PLUtilities getHardwarePerfKind:]_block_invoke
+ ___56-[PLBatteryAgent logBatteryShutdownToCA:forBatteryPack:]_block_invoke
+ ___84-[PLBatteryAgent logEventPointBatteryShutdownWithRawData:packID:systemShutdownData:]_block_invoke
+ ___84-[PLBatteryAgent logEventPointBatteryShutdownWithRawData:packID:systemShutdownData:]_block_invoke_2
+ ___snprintf_chk
+ _kCLLocationAccuracyReduced
+ _kPLBatteryAgentEventPointNameBatteryShutdownPack0
+ _kPLBatteryAgentStringLastShutdownSystemTimestamp0
+ _kPLBatteryAgentStringLastShutdownSystemTimestampSystem
+ _objc_msgSend$_entryEventBackwardDefinitionAPLStatsWithLogSelector:
+ _objc_msgSend$cleanUp
+ _objc_msgSend$cpu_energy_m
+ _objc_msgSend$criticalDays
+ _objc_msgSend$entryEventPointDefinitionBatteryShutdownPack
+ _objc_msgSend$getHardwarePerfKind:
+ _objc_msgSend$logBatteryShutdownToCA:forBatteryPack:
+ _objc_msgSend$logEventPointBatteryShutdownWithRawData:packID:systemShutdownData:
+ _objc_msgSend$processWideAgentSetupDone
+ _objc_msgSend$setCpu_energy_m:
+ _objc_msgSend$setCriticalDays:
+ _objc_msgSend$setLocationReducedAccuracySeconds:
+ _objc_msgSend$setProcessWideAgentSetupDone:
+ getHardwarePerfKind:.cache
+ getHardwarePerfKind:.cacheOnce
+ logEventPointBatteryShutdownWithRawData:packID:systemShutdownData:.classDebugEnabled
+ logEventPointBatteryShutdownWithRawData:packID:systemShutdownData:.defaultOnce
- -[PLBatteryAgent logBatteryShutdownToCA:]
- GCC_except_table111
- GCC_except_table139
- GCC_except_table142
- GCC_except_table148
- GCC_except_table194
- GCC_except_table203
- GCC_except_table228
- GCC_except_table232
- GCC_except_table240
- GCC_except_table245
- GCC_except_table251
- GCC_except_table294
- GCC_except_table297
- GCC_except_table301
- ___41-[PLBatteryAgent logBatteryShutdownToCA:]_block_invoke
- ___46-[PLBatteryAgent logEventPointBatteryShutdown]_block_invoke
- ___46-[PLBatteryAgent logEventPointBatteryShutdown]_block_invoke_2
- _kPLBatteryAgentStringLastShutdownSystemTimestamp
- _objc_msgSend$logBatteryShutdownToCA:
- logEventPointBatteryShutdown.classDebugEnabled
- logEventPointBatteryShutdown.defaultOnce
CStrings:
+ "-[PLBatteryAgent logEventPointBatteryShutdownWithRawData:packID:systemShutdownData:]"
+ "AppleSmartBatteryPack"
+ "BatteryShutdown: Failed to get AppleSmartBatteryPack data with result=%x"
+ "BatteryShutdown: log entry for pack=%@"
+ "BatteryShutdownPack0"
+ "CPUEnergyM"
+ "Failed to retrieve power sources list handle."
+ "LastShutdownSystemTimestampSystem"
+ "No data in battUI for dormancy eligibility"
+ "Not enough data for dormancy eligibility (need %d days)"
+ "Number of critical days: %d"
+ "ReducedAccuracy"
+ "hw.perflevel%u.name"
+ "locationReducedAccuracySeconds"
+ "optimizeBatteryPromptEligibility"
+ "reducedAccuracy"
+ "reducedAccuracySeconds"
+ "\xbe"
- "-[PLBatteryAgent logEventPointBatteryShutdown]"
- "A"
- "\xae"
```
