## PowerlogHelperdOperators

> `/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/Versions/A/PowerlogHelperdOperators`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_nlclslist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-3486.0.46.501.1
-  __TEXT.__text: 0x10dac4
-  __TEXT.__objc_methlist: 0xa3f8
+3486.0.81.501.3
+  __TEXT.__text: 0x1106b4
+  __TEXT.__objc_methlist: 0xa550
   __TEXT.__const: 0x4a0
-  __TEXT.__cstring: 0x1652e
-  __TEXT.__oslogstring: 0xada9
-  __TEXT.__gcc_except_tab: 0x1c3c
-  __TEXT.__unwind_info: 0x24d8
+  __TEXT.__cstring: 0x16695
+  __TEXT.__oslogstring: 0xaeca
+  __TEXT.__gcc_except_tab: 0x1c94
+  __TEXT.__unwind_info: 0x2548
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2208
+  __DATA_CONST.__const: 0x2228
   __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_nlclslist: 0xb0
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7120
+  __DATA_CONST.__objc_selrefs: 0x7220
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_arraydata: 0x2a98
-  __DATA_CONST.__got: 0xaa8
+  __DATA_CONST.__got: 0xab0
   __AUTH_CONST.__const: 0x2ba8
-  __AUTH_CONST.__cfstring: 0x204a0
-  __AUTH_CONST.__objc_const: 0xd0e0
+  __AUTH_CONST.__cfstring: 0x206a0
+  __AUTH_CONST.__objc_const: 0xd240
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x640
   __AUTH_CONST.__objc_intobj: 0x1410

   __AUTH_CONST.__objc_arrayobj: 0xc90
   __AUTH_CONST.__auth_got: 0xb70
   __AUTH.__objc_data: 0x960
-  __DATA.__objc_ivar: 0xd48
+  __DATA.__objc_ivar: 0xd64
   __DATA.__data: 0x3a0
-  __DATA.__bss: 0xe48
+  __DATA.__bss: 0xe40
   __DATA.__common: 0x74
   __DATA_DIRTY.__objc_data: 0xc30
   __DATA_DIRTY.__bss: 0x2b8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5217
-  Symbols:   10505
-  CStrings:  5423
+  Functions: 5255
+  Symbols:   10568
+  CStrings:  5446
 
Symbols:
+ +[PLBatteryAgent entryEventBackwardDefinitionRebalance]
+ +[PLBatteryAgent fusePackCurrentAccumulators:fusedAccumulator:fusedCount:]
+ +[PLUrsaUtilities compareBuildVersion:withBuildVersion:]
+ -[PLBatteryAgent logEventBackwardChargerDataWithRawData:]
+ -[PLBatteryAgent prevRebalanceErrorFlags]
+ -[PLBatteryAgent prevRebalanceNotRebalancingReason]
+ -[PLBatteryAgent setPrevRebalanceErrorFlags:]
+ -[PLBatteryAgent setPrevRebalanceNotRebalancingReason:]
+ -[PLContextualizedMetricData addGlitchWithDuration:scrollDuration:glitchCount:isScrollStart:]
+ -[PLContextualizedMetricData setAnimationHitchTotalAnimationDuration:weightedGlitchRatioSum:]
+ -[PLDisplayAgent modelDisplayPowerFromIOMFB:withRootNodeID:]
+ -[PLDisplayAgent modelDynamicDisplayPowerFromAPL:withRootNodeID:]
+ -[PLPowerMetricMonitorService _primeSystemAgents]
+ -[PLPowerMetricMonitorService _runFullSetup]
+ -[PLPowerMetricMonitorService fullSetupCompleted]
+ -[PLPowerMetricMonitorService isSetUp]
+ -[PLPowerMetricMonitorService setFullSetupCompleted:]
+ -[PLPowerMetricMonitorService setUpForMonitoringWithLiteMode:]
+ -[PLPowerMetricMonitorService upgradeToFullSetup]
+ -[PLProcessNetworkAgent setTransaction:]
+ -[PLProcessNetworkAgent transaction]
+ -[PLStreamingMetricAggregator _bufferAnimationInterval:forBucketKey:]
+ -[PLStreamingMetricAggregator _processBatchForBucketKey:]
+ -[PLStreamingMetricAggregator addAnimationHitchWithBundleID:interval:]
+ -[PLStreamingMetricAggregator addGlitchWithBundleID:timestamp:glitchDurationMs:scrollDurationMs:glitchCount:isScrollStart:]
+ -[PLStreamingMetricAggregator pendingAnimationIntervalsByBucket]
+ -[PLStreamingMetricAggregator processedTotalDurationByBucket]
+ -[PLStreamingMetricAggregator processedWeightedRatioSumByBucket]
+ -[PLStreamingMetricAggregator setPendingAnimationIntervalsByBucket:]
+ -[PLStreamingMetricAggregator setProcessedTotalDurationByBucket:]
+ -[PLStreamingMetricAggregator setProcessedWeightedRatioSumByBucket:]
+ GCC_except_table137
+ GCC_except_table142
+ GCC_except_table148
+ GCC_except_table153
+ GCC_except_table228
+ GCC_except_table232
+ GCC_except_table240
+ GCC_except_table241
+ GCC_except_table246
+ GCC_except_table247
+ GCC_except_table251
+ GCC_except_table294
+ GCC_except_table297
+ GCC_except_table301
+ GCC_except_table90
+ GCC_except_table95
+ OBJC_IVAR_$_PLBatteryAgent._prevRebalanceErrorFlags
+ OBJC_IVAR_$_PLBatteryAgent._prevRebalanceNotRebalancingReason
+ OBJC_IVAR_$_PLPowerMetricMonitorService._fullSetupCompleted
+ OBJC_IVAR_$_PLProcessNetworkAgent._transaction
+ OBJC_IVAR_$_PLStreamingMetricAggregator._pendingAnimationIntervalsByBucket
+ OBJC_IVAR_$_PLStreamingMetricAggregator._processedTotalDurationByBucket
+ OBJC_IVAR_$_PLStreamingMetricAggregator._processedWeightedRatioSumByBucket
+ _OBJC_CLASS_$_SignpostAnimationInterval
+ __49-[PLPowerMetricMonitorService upgradeToFullSetup]_block_invoke
+ ___123-[PLStreamingMetricAggregator addGlitchWithBundleID:timestamp:glitchDurationMs:scrollDurationMs:glitchCount:isScrollStart:]_block_invoke
+ ___123-[PLStreamingMetricAggregator addGlitchWithBundleID:timestamp:glitchDurationMs:scrollDurationMs:glitchCount:isScrollStart:]_block_invoke_2
+ ___38-[PLPowerMetricMonitorService isSetUp]_block_invoke
+ ___44-[PLPowerMetricMonitorService _runFullSetup]_block_invoke
+ ___46-[PLStreamingMetricAggregator finalizeResults]_block_invoke
+ ___49-[PLPowerMetricMonitorService upgradeToFullSetup]_block_invoke
+ ___49-[PLPowerMetricMonitorService upgradeToFullSetup]_block_invoke_2
+ ___62-[PLPowerMetricMonitorService setUpForMonitoringWithLiteMode:]_block_invoke
+ ___62-[PLPowerMetricMonitorService setUpForMonitoringWithLiteMode:]_block_invoke_2
+ ___block_descriptor_57_e36_v16?0"PLContextualizedMetricData"8l
+ _kPLBatteryAgentEventBackwardNameChargerData0
+ _kPLBatteryAgentEventBackwardNameHoldName
+ _kPLBatteryAgentEventBackwardNameIsEoc
+ _kPLBatteryAgentEventBackwardNameSocLimit
+ _objc_msgSend$_bufferAnimationInterval:forBucketKey:
+ _objc_msgSend$_primeSystemAgents
+ _objc_msgSend$_processBatchForBucketKey:
+ _objc_msgSend$_runFullSetup
+ _objc_msgSend$addGlitchWithDuration:scrollDuration:glitchCount:isScrollStart:
+ _objc_msgSend$beginDate
+ _objc_msgSend$entryEventBackwardDefinitionChargerData
+ _objc_msgSend$firstMatchInString:options:range:
+ _objc_msgSend$fullSetupCompleted
+ _objc_msgSend$initOperatorDependanciesSynchronously
+ _objc_msgSend$initWithEntryKey:withDate:capacity:
+ _objc_msgSend$logEventBackwardChargerDataWithRawData:
+ _objc_msgSend$modelDisplayPowerFromIOMFB:withRootNodeID:
+ _objc_msgSend$modelDynamicDisplayPowerFromAPL:withRootNodeID:
+ _objc_msgSend$nonFirstFrameContributedGlitchTimeRatioAdjustedMsPerS
+ _objc_msgSend$setAnimationHitchTotalAnimationDuration:weightedGlitchRatioSum:
+ _objc_msgSend$setFullSetupCompleted:
+ _objc_msgSend$setTransaction:
+ _objc_msgSend$startedSetUp
+ _objc_msgSend$unionOfAnimationIntervals:
+ _parseBuildVersion
- -[PLContextualizedMetricData addGlitchWithDuration:scrollDuration:glitchCount:isScrollStart:glitchRatio:animationDuration:]
- -[PLDisplayAgent modelDisplayPowerFromIOMFB:]
- -[PLDisplayAgent modelDynamicDisplayPowerFromAPL:]
- -[PLPowerMetricMonitorService setUpForMonitoring]
- -[PLStreamingMetricAggregator addGlitchWithBundleID:timestamp:glitchDurationMs:scrollDurationMs:glitchCount:isScrollStart:glitchRatio:animationDuration:]
- GCC_except_table128
- GCC_except_table141
- GCC_except_table144
- GCC_except_table147
- GCC_except_table226
- GCC_except_table230
- GCC_except_table238
- GCC_except_table239
- GCC_except_table243
- GCC_except_table244
- GCC_except_table249
- GCC_except_table292
- GCC_except_table295
- GCC_except_table299
- ___153-[PLStreamingMetricAggregator addGlitchWithBundleID:timestamp:glitchDurationMs:scrollDurationMs:glitchCount:isScrollStart:glitchRatio:animationDuration:]_block_invoke
- ___153-[PLStreamingMetricAggregator addGlitchWithBundleID:timestamp:glitchDurationMs:scrollDurationMs:glitchCount:isScrollStart:glitchRatio:animationDuration:]_block_invoke_2
- ___49-[PLPowerMetricMonitorService setUpForMonitoring]_block_invoke
- ___49-[PLPowerMetricMonitorService setUpForMonitoring]_block_invoke_2
- ___block_descriptor_73_e36_v16?0"PLContextualizedMetricData"8l
- _objc_msgSend$addGlitchWithDuration:scrollDuration:glitchCount:isScrollStart:glitchRatio:animationDuration:
- _objc_msgSend$modelDisplayPowerFromIOMFB:
- _objc_msgSend$modelDynamicDisplayPowerFromAPL:
- setUpForMonitoring.onceToken
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dKRHdU/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLBatteryAgent.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dKRHdU/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLDisplayAgent.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dKRHdU/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLSMCAgent.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dKRHdU/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLCoalitionAgent.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dKRHdU/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLProcessMonitorAgent.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dKRHdU/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLScreenStateAgent.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dKRHdU/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLSleepWakeAgent.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dKRHdU/Sources/PerfPowerServices_Operators/Operators/Services/PLXPCService.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dKRHdU/Sources/PerfPowerServices_Operators/Utilities/PLMetricsFormatterJSON.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dKRHdU/Sources/PerfPowerServices_Operators/Utilities/PLProcessPortMap.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dKRHdU/Sources/PerfPowerServices_Operators/Utilities/PLUtilities.m"
+ "AppleChargerData"
+ "BatteryPackID"
+ "ChargerAccumEfficiencyCount"
+ "ChargerAccumulatedEfficiency"
+ "ChargerData0"
+ "ChargerEfficiency"
+ "ChargerHwIlimBackoffReason"
+ "ChargerIBUS"
+ "ChargerPower"
+ "ChargerVBUS"
+ "Failed to subscribe to IOReport %{public}@ display stats"
+ "Failed to subscribe to IOReport %{public}@ scanout"
+ "Failed to subscribe to IOReport %{public}@ swap"
+ "Invalid build string buildA: %{public}@, buildB: %{public}@"
+ "J"
+ "Lite mode setup complete — agent init skipped"
+ "MULTI_BATTERY: Logging charger entry %@"
+ "Primed IOReport and %lu system agents after full setup upgrade"
+ "Setting up to monitor liteMode=%d"
+ "Upgrading from lite mode to full agent setup"
+ "^([0-9]+)([A-Z]+)([0-9]+)([a-z]*)$"
+ "com.apple.powerlog.pl_process_network_agent"
+ "holds"
+ "isEoc"
+ "promptExpertLoadLatency"
+ "socLimit"
+ "totalExpertsNeedingNANDLoad"
+ "totalExpertsPurgedCount"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.acYFKq/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLBatteryAgent.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.acYFKq/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLDisplayAgent.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.acYFKq/Sources/PerfPowerServices_Operators/Operators/Agents/Hardware/PLSMCAgent.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.acYFKq/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLCoalitionAgent.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.acYFKq/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLProcessMonitorAgent.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.acYFKq/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLScreenStateAgent.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.acYFKq/Sources/PerfPowerServices_Operators/Operators/Agents/Software/PLSleepWakeAgent.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.acYFKq/Sources/PerfPowerServices_Operators/Operators/Services/PLXPCService.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.acYFKq/Sources/PerfPowerServices_Operators/Utilities/PLMetricsFormatterJSON.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.acYFKq/Sources/PerfPowerServices_Operators/Utilities/PLProcessPortMap.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.acYFKq/Sources/PerfPowerServices_Operators/Utilities/PLUtilities.m"
- "Failed to subscribe to IOReport DCP display stats"
- "Failed to subscribe to IOReport DCP scanout"
- "Failed to subscribe to IOReport DCP swap"
- "G"
- "Setting up to monitor"
```
