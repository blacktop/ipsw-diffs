## PowerlogHelperdOperators

> `/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`

```diff

-3486.40.98.0.0
-  __TEXT.__text: 0x1e24d4
-  __TEXT.__objc_methlist: 0x11288
+3486.40.112.0.0
+  __TEXT.__text: 0x1e3c5c
+  __TEXT.__objc_methlist: 0x11300
   __TEXT.__const: 0x700
-  __TEXT.__cstring: 0x26afd
-  __TEXT.__oslogstring: 0x15e78
-  __TEXT.__gcc_except_tab: 0x2598
+  __TEXT.__cstring: 0x26c67
+  __TEXT.__oslogstring: 0x15fdd
+  __TEXT.__gcc_except_tab: 0x25a4
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x6088
+  __TEXT.__unwind_info: 0x6098
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x45a8
+  __DATA_CONST.__const: 0x45b8
   __DATA_CONST.__objc_classlist: 0x3a8
   __DATA_CONST.__objc_nlclslist: 0x108
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb270
+  __DATA_CONST.__objc_selrefs: 0xb2d8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x2e0
-  __DATA_CONST.__objc_arraydata: 0x16498
+  __DATA_CONST.__objc_arraydata: 0x16478
   __DATA_CONST.__got: 0xf88
   __AUTH_CONST.__const: 0x1a80
-  __AUTH_CONST.__cfstring: 0x34240
-  __AUTH_CONST.__objc_const: 0x16a40
+  __AUTH_CONST.__cfstring: 0x34380
+  __AUTH_CONST.__objc_const: 0x16b00
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x28e0
   __AUTH_CONST.__objc_dictobj: 0x3b38
-  __AUTH_CONST.__objc_doubleobj: 0xb90
-  __AUTH_CONST.__objc_arrayobj: 0x3048
+  __AUTH_CONST.__objc_doubleobj: 0xba0
+  __AUTH_CONST.__objc_arrayobj: 0x3060
   __AUTH_CONST.__auth_got: 0xe08
   __AUTH.__objc_data: 0xc08
-  __DATA.__objc_ivar: 0x16dc
+  __DATA.__objc_ivar: 0x16ec
   __DATA.__data: 0x580
   __DATA.__common: 0x74
   __DATA_DIRTY.__objc_data: 0x1888

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 8852
-  Symbols:   11974
-  CStrings:  9119
+  Functions: 8864
+  Symbols:   11993
+  CStrings:  9134
 
Symbols:
+ +[PLAppTimeService entryAggregateDefinitionDisplayUsage]
+ +[PLUrsaUtilities diagnosticExtensionIDsForProcess:]
+ -[PLAppTimeService aggregateEntryKeyForDisplayUsage]
+ -[PLAppTimeService setAggregateEntryKeyForDisplayUsage:]
+ -[PLAppTimeService updateScreenOnTimeInDBForBundleId:withTime:withDate:forContext:]
+ -[PLBatteryAgent batteryPackCount]
+ -[PLBatteryAgent setBatteryPackCount:]
+ -[PLSleepWakeAgent kaIDMax]
+ -[PLSleepWakeAgent kaIDMin]
+ -[PLSleepWakeAgent setKaIDMax:]
+ -[PLSleepWakeAgent setKaIDMin:]
+ _OBJC_IVAR_$_PLAppTimeService._aggregateEntryKeyForDisplayUsage
+ _OBJC_IVAR_$_PLBatteryAgent._batteryPackCount
+ _OBJC_IVAR_$_PLSleepWakeAgent._kaIDMax
+ _OBJC_IVAR_$_PLSleepWakeAgent._kaIDMin
+ ___52+[PLUrsaUtilities diagnosticExtensionIDsForProcess:]_block_invoke
+ ___83-[PLAppTimeService updateScreenOnTimeInDBForBundleId:withTime:withDate:forContext:]_block_invoke
+ _diagnosticExtensionIDsForProcess:.mapping
+ _diagnosticExtensionIDsForProcess:.onceToken
+ _kPLAppTimeServiceAggregateNameDisplayID
+ _kPLAppTimeServiceAggregateNameDisplayID_block_invoke.classDebugEnabled
+ _kPLAppTimeServiceAggregateNameDisplayID_block_invoke.defaultOnce
+ _kPLAppTimeServiceAggregateNameDisplayID_block_invoke_2.classDebugEnabled
+ _kPLAppTimeServiceAggregateNameDisplayID_block_invoke_2.defaultOnce
+ _kPLAppTimeServiceAggregateNameDisplayUsage
+ _updateScreenOnTimeInDBForBundleId:withTime:withDate:forContext:.classDebugEnabled
+ _updateScreenOnTimeInDBForBundleId:withTime:withDate:forContext:.defaultOnce
- +[PLUrsaUtilities shouldCollectCPLDiagnosticExtensionForProcess:]
- ___65+[PLUrsaUtilities shouldCollectCPLDiagnosticExtensionForProcess:]_block_invoke
- _kPLAppTimeServiceAggregateNameHasAudioUsage_block_invoke.classDebugEnabled
- _kPLAppTimeServiceAggregateNameHasAudioUsage_block_invoke.defaultOnce
- _kPLAppTimeServiceAggregateNameHasAudioUsage_block_invoke_2.classDebugEnabled
- _kPLAppTimeServiceAggregateNameHasAudioUsage_block_invoke_2.defaultOnce
- _shouldCollectCPLDiagnosticExtensionForProcess:.cplDiagnosticExtensionProcesses
- _shouldCollectCPLDiagnosticExtensionForProcess:.onceToken
CStrings:
+ "-[PLAppTimeService updateScreenOnTimeInDBForBundleId:withTime:withDate:forContext:]"
+ "AccumSystemEffectiveTotalLoad"
+ "AccumSystemEffectiveTotalLoadCount"
+ "AccumulatedBatteryPower"
+ "BatteryPowerAccumulatorCount"
+ "Chunk interval memory: average suspended memory is zero (sampleCount: %ld, peakBytes: %lu)"
+ "DisplayID"
+ "DisplayUsage"
+ "For bundleID '%@' and display ID %@, added foreground %@"
+ "Kernel assertions entry: kaID=%llu, duration=%f, count=%zu"
+ "PLUrsaUtilities: requesting diagnostic extensions %{public}@ for %{public}@"
+ "SystemEffectiveTotalLoad"
+ "adding timeDifference=%f for bundleID=%@ and displayID=%lu"
+ "com.apple.DiagnosticExtensions.IMDiagnosticExtension"
+ "getSignpostMetricsWithStartDate returned launchDurations=%lu extendedLaunchDurations=%lu launchesTimeSeries=%lu bundleIDs(launchDurations)=%@"
+ "imagent"
+ "imdpersistence.imdpersistenceagent"
+ "imdpersistenceagent"
- ",%@"
- "Kernel assertions entry: paID=%llu, duration=%f, count=%zu"
- "PLUrsaUtilities: requesting CPL diagnostic extension for %{public}@"
```
