## SymptomEvaluator

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator`

```diff

-1848.2.1.0.0
-  __TEXT.__text: 0x24bde0
+1848.42.1.0.0
+  __TEXT.__text: 0x24d774
   __TEXT.__auth_stubs: 0x2600
-  __TEXT.__objc_methlist: 0x16394
-  __TEXT.__cstring: 0x224af
-  __TEXT.__oslogstring: 0x3bbda
+  __TEXT.__objc_methlist: 0x1649c
+  __TEXT.__cstring: 0x227c8
+  __TEXT.__oslogstring: 0x3c046
   __TEXT.__const: 0x738
-  __TEXT.__gcc_except_tab: 0x3298
+  __TEXT.__gcc_except_tab: 0x32ac
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.evaluator_cfg: 0x5f7a
   __TEXT.default_clp: 0x2fe0

   __TEXT.baseband_clp: 0xe950
   __TEXT.bb_MAV_clp: 0xaa40
   __TEXT.modules_clp: 0x1230
-  __TEXT.__unwind_info: 0x6498
+  __TEXT.__unwind_info: 0x64cc
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x1c99
-  __TEXT.__objc_methname: 0x3afc2
-  __TEXT.__objc_methtype: 0x6899
-  __TEXT.__objc_stubs: 0x24ae0
+  __TEXT.__objc_classname: 0x1c9b
+  __TEXT.__objc_methname: 0x3b628
+  __TEXT.__objc_methtype: 0x68a4
+  __TEXT.__objc_stubs: 0x24d20
   __DATA_CONST.__got: 0x6a8
   __DATA_CONST.__const: 0x61a0
   __DATA_CONST.__objc_classlist: 0x850
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x340a0
-  __DATA_CONST.__objc_selrefs: 0xc338
+  __DATA_CONST.__objc_const: 0x34650
+  __DATA_CONST.__objc_selrefs: 0xc398
   __DATA_CONST.__objc_arraydata: 0x798
-  __AUTH_CONST.__cfstring: 0x1b380
+  __AUTH_CONST.__cfstring: 0x1b6e0
   __AUTH_CONST.__objc_const: 0x6f58
   __AUTH_CONST.__const: 0x21f8
   __AUTH_CONST.__objc_arrayobj: 0x198

   __DATA.__objc_protorefs: 0x20
   __DATA.__objc_classrefs: 0xb80
   __DATA.__objc_superrefs: 0x598
-  __DATA.__objc_ivar: 0x2bdc
+  __DATA.__objc_ivar: 0x2c84
   __DATA.__data: 0x1a70
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x378

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libz.1.dylib
-  UUID: B02180DE-6476-356D-89D7-CC896F237025
-  Functions: 10892
-  Symbols:   35255
-  CStrings:  25235
+  UUID: D36CDE19-4A77-32B7-8E91-19FF2992E35C
+  Functions: 10917
+  Symbols:   35366
+  CStrings:  25364
 
Symbols:
+ -[CellOutrankMetrics _dailyOutrankMetricDictionary]
+ -[CellOutrankMetrics _resetDailyTelemetryMetrics]
+ -[CellOutrankMetrics _sendDailyOutrankMetric]
+ -[CellOutrankMetrics _setupDailyTelemetryTimer]
+ -[CellOutrankMetrics _updateStateTransitionMetricsForNewState:oldState:]
+ -[CellOutrankMetrics updateMetricsForState:]
+ -[NWActivityHandler _timestampTwoHourBucketForCurrentTime]
+ -[NWActivityHandler _timestampTwoHourBucketForTime:]
+ -[PowerStateRelay batteryDepthOfDischarge]
+ -[PowerStateRelay batteryRawCurrentCapacity]
+ -[PowerStateRelay batteryRawMaximumCapacity]
+ -[PowerStateRelay setBatteryDepthOfDischarge:]
+ -[PowerStateRelay setBatteryRawCurrentCapacity:]
+ -[PowerStateRelay setBatteryRawMaximumCapacity:]
+ -[SFDeviceReport batteryDepthOfDischarge]
+ -[SFDeviceReport batteryRawCurrentCapacity]
+ -[SFDeviceReport batteryRawMaximumCapacity]
+ -[SFDeviceReport setBatteryDepthOfDischarge:]
+ -[SFDeviceReport setBatteryRawCurrentCapacity:]
+ -[SFDeviceReport setBatteryRawMaximumCapacity:]
+ -[SFDeviceReport setTimestampBucket:]
+ -[SFDeviceReport timestampBucket]
+ GCC_except_table130
+ GCC_except_table56
+ GCC_except_table67
+ GCC_except_table69
+ _OBJC_IVAR_$_CellOutrankMetrics._currentCOSMState
+ _OBJC_IVAR_$_CellOutrankMetrics._dailyTelemetryTimer
+ _OBJC_IVAR_$_CellOutrankMetrics._durationForCellInexpensive
+ _OBJC_IVAR_$_CellOutrankMetrics._durationForCellWRMInexpensive
+ _OBJC_IVAR_$_CellOutrankMetrics._durationInArmedState
+ _OBJC_IVAR_$_CellOutrankMetrics._durationInIdleState
+ _OBJC_IVAR_$_CellOutrankMetrics._durationInOutrankState
+ _OBJC_IVAR_$_CellOutrankMetrics._durationOnSporadicNetwork
+ _OBJC_IVAR_$_CellOutrankMetrics._lastCellInexpensive
+ _OBJC_IVAR_$_CellOutrankMetrics._lastCellWRMInexpensive
+ _OBJC_IVAR_$_CellOutrankMetrics._lastDailyTelemetryTimestamp
+ _OBJC_IVAR_$_CellOutrankMetrics._lastEntryToSporadicNetwork
+ _OBJC_IVAR_$_CellOutrankMetrics._lastTransitionToArmedState
+ _OBJC_IVAR_$_CellOutrankMetrics._lastTransitionToIdleState
+ _OBJC_IVAR_$_CellOutrankMetrics._lastTransitionToOutrankState
+ _OBJC_IVAR_$_CellOutrankMetrics._numTimesCellEligible
+ _OBJC_IVAR_$_CellOutrankMetrics._numTimesCellPrivateNetworkActive
+ _OBJC_IVAR_$_CellOutrankMetrics._numTimesWiFiAndCellEligible
+ _OBJC_IVAR_$_CellOutrankMetrics._numTimesWiFiAndCellEligibleDeviceIneligible
+ _OBJC_IVAR_$_CellOutrankMetrics._numTimesWiFiEligible
+ _OBJC_IVAR_$_CellOutrankMetrics._numberOfArmedToOutrankTransitions
+ _OBJC_IVAR_$_CellOutrankMetrics._numberOfIdleToArmedTransitions
+ _OBJC_IVAR_$_CellOutrankMetrics._numberOfIdleToOutrankTransitions
+ _OBJC_IVAR_$_CellOutrankMetrics._numberOfOutrankToIdleTransitions
+ _OBJC_IVAR_$_CellOutrankMetrics._numberOfTimesInArmedStateForAtLeastFiveSeconds
+ _OBJC_IVAR_$_CellOutrankMetrics._numberOfTimesInOutrankStateForAtLeastFiveSeconds
+ _OBJC_IVAR_$_CellOutrankMetrics._prevCellEligible
+ _OBJC_IVAR_$_CellOutrankMetrics._prevCellInexpensive
+ _OBJC_IVAR_$_CellOutrankMetrics._prevCellPrivateNetworkActive
+ _OBJC_IVAR_$_CellOutrankMetrics._prevCellWRMInexpensive
+ _OBJC_IVAR_$_CellOutrankMetrics._prevDeviceEligible
+ _OBJC_IVAR_$_CellOutrankMetrics._prevWiFiEligible
+ _OBJC_IVAR_$_CellOutrankMetrics._prevWiFiSporadic
+ _OBJC_IVAR_$_CellOutrankMetrics._sporadicIsKnown
+ _OBJC_IVAR_$_CellOutrankMetrics._startedCollectingMetricsFrom
+ _OBJC_IVAR_$_PowerStateRelay._batteryDepthOfDischarge
+ _OBJC_IVAR_$_PowerStateRelay._batteryRawCurrentCapacity
+ _OBJC_IVAR_$_PowerStateRelay._batteryRawMaximumCapacity
+ _OBJC_IVAR_$_SFDeviceReport._batteryDepthOfDischarge
+ _OBJC_IVAR_$_SFDeviceReport._batteryRawCurrentCapacity
+ _OBJC_IVAR_$_SFDeviceReport._batteryRawMaximumCapacity
+ _OBJC_IVAR_$_SFDeviceReport._timestampBucket
+ ___39-[CellOutrankHandler initializeHistory]_block_invoke.656
+ ___39-[CellOutrankHandler initializeHistory]_block_invoke.662
+ ___45-[CellOutrankHandler _completeInitialization]_block_invoke.645
+ ___45-[CellOutrankHandler _completeInitialization]_block_invoke_2.647
+ ___45-[CellOutrankMetrics _sendDailyOutrankMetric]_block_invoke
+ ___47-[CellOutrankMetrics _setupDailyTelemetryTimer]_block_invoke
+ ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.868
+ ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.877
+ ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke_2.880
+ ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke_3.881
+ ___block_literal_global.654
+ ___block_literal_global.866
+ ___block_literal_global.879
+ _objc_msgSend$_dailyOutrankMetricDictionary
+ _objc_msgSend$_resetDailyTelemetryMetrics
+ _objc_msgSend$_sendDailyOutrankMetric
+ _objc_msgSend$_setupDailyTelemetryTimer
+ _objc_msgSend$_timestampTwoHourBucketForCurrentTime
+ _objc_msgSend$_timestampTwoHourBucketForTime:
+ _objc_msgSend$_updateStateTransitionMetricsForNewState:oldState:
+ _objc_msgSend$batteryDepthOfDischarge
+ _objc_msgSend$batteryRawCurrentCapacity
+ _objc_msgSend$batteryRawMaximumCapacity
+ _objc_msgSend$cellEligible
+ _objc_msgSend$cellExpensive
+ _objc_msgSend$cellWRMExpensive
+ _objc_msgSend$deviceEligible
+ _objc_msgSend$setBatteryDepthOfDischarge:
+ _objc_msgSend$setBatteryRawCurrentCapacity:
+ _objc_msgSend$setBatteryRawMaximumCapacity:
+ _objc_msgSend$setTimestampBucket:
+ _objc_msgSend$timestampBucket
+ _objc_msgSend$updateMetricsForState:
+ _objc_msgSend$wifiEligible
+ _objc_msgSend$wifiKnowableSporadic
- GCC_except_table113
- GCC_except_table129
- GCC_except_table54
- GCC_except_table65
- ___39-[CellOutrankHandler initializeHistory]_block_invoke.655
- ___39-[CellOutrankHandler initializeHistory]_block_invoke.661
- ___45-[CellOutrankHandler _completeInitialization]_block_invoke.646
- ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.867
- ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.876
- ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke_2.879
- ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke_3.880
- ___block_literal_global.653
- ___block_literal_global.865
- ___block_literal_global.878
- _objc_msgSend$deltaRxCellularBytes
- _objc_msgSend$deltaRxWiFiBytes
- _objc_msgSend$deltaTxCellularBytes
- _objc_msgSend$deltaTxWiFiBytes
CStrings:
+ "\x06\xf0Q"
+ "<NWDeviceReport:\n\tTimestamp Bucket:\t\t%u\n\tBattery Percentage:\t\t\t%u\n\tBattery Current Capacity:\t\t%u\n\tBattery Maximum Capacity:\t\t%u\n\tBattery Design Capacity:\t\t%u\n\tBattery Absolute Capacity:\t\t%u\n\tBattery Voltage:\t\t\t%u\n\tBattery Time Remaining:\t\t\t%u\n\tBattery Temperature:\t\t\t%u\n\tBattery External Power Is Connected:\t%u\n\tBattery Fully Charged:\t\t\t%u\n\tBattery At Warn Level:\t\t\t%u\n\tBattery At Critical Level:\t\t%u\n\tRNF Enabled:\t\t\t\t%u\n\tDevice Plugged In:\t\t\t%u\n\tDevice Screen On:\t\t\t%u\n\tDevice Screen Brightness:\t\t%u\n\tMotion State:\t\t\t\t%u\n\tDevice Orientation:\t\t\t%u\n\tThermal Pressure:\t\t\t%u\n\tQUIC Experimentally Enabled:\t\t%u\n\tPrivacy Proxy Service Status:\t\t%u\n\tPrivacy Proxy User Tier:\t\t%u\n\tPrivacy Proxy Networks:\t\t%@\n\tPrivacy Proxy Traffic:\t\t%@\n>"
+ "AppleRawCurrentCapacity"
+ "AppleRawMaxCapacity"
+ "C24@0:8d16"
+ "COSM Daily Metrics: Calling AnalyticsSendEventLazy to send Daily COSM Metrics to CA"
+ "COSM Daily Metrics: Cannot send daily telemetry due to nil instance"
+ "COSM Daily Metrics: Error creating daily telemetry timer"
+ "COSM Daily Metrics: Got undefined COSM state %d"
+ "COSM Daily Metrics: Got unexpected COSM state %d"
+ "COSM Daily Metrics: Obtained same state after COSM state transition"
+ "COSM Daily Metrics: Posting metric dictionary %{private}@ to CA"
+ "COSM Daily Metrics: Resetting metrics for next-day collection"
+ "COSM Daily Metrics: Running scheduled daily telemetry collection block"
+ "COSM Daily Metrics: Setting up daily telemetry timer"
+ "COSM Daily Metrics: Skipping daily telemetry collection on nil instance"
+ "COSM Daily Metrics: Updating metrics for state %{private}@"
+ "COSM Daily Metrics: Updating metrics on state transition %d -> %d"
+ "NWACT: Error while parsing input while calculating timestamp bucket"
+ "Power: Failed to create an IONotificationPort"
+ "Power: Failed to get matching IOPMPowerSource"
+ "Power: Successfully registered for IOPMPowerSource interest notification"
+ "Power: battery-percentage %.2f battery-power-connected %d battery-charging %d battery-warn %d battery-critical %d battery-absolute-capacity-mAh %u battery-voltage-mV %u battery-current-capacity-%% %u battery-maximum-capacity-%% %u battery-design-capacity-mAh %u battery-time-remaining %u battery-fully-charged %d battery-temperature %d screen-brightness %u battery-raw-current-capacity %u battery-raw-maximum-capacity %u presentDOD %u"
+ "PresentDOD"
+ "TC,N,V_timestampBucket"
+ "TI,N,V_batteryDepthOfDischarge"
+ "TI,N,V_batteryRawCurrentCapacity"
+ "TI,N,V_batteryRawMaximumCapacity"
+ "TI,V_batteryDepthOfDischarge"
+ "TI,V_batteryRawCurrentCapacity"
+ "TI,V_batteryRawMaximumCapacity"
+ "_batteryDepthOfDischarge"
+ "_batteryRawCurrentCapacity"
+ "_batteryRawMaximumCapacity"
+ "_dailyOutrankMetricDictionary"
+ "_dailyTelemetryTimer"
+ "_durationForCellInexpensive"
+ "_durationForCellWRMInexpensive"
+ "_durationInArmedState"
+ "_durationInIdleState"
+ "_durationInOutrankState"
+ "_durationOnSporadicNetwork"
+ "_lastCellInexpensive"
+ "_lastCellWRMInexpensive"
+ "_lastDailyTelemetryTimestamp"
+ "_lastEntryToSporadicNetwork"
+ "_lastTransitionToArmedState"
+ "_lastTransitionToIdleState"
+ "_lastTransitionToOutrankState"
+ "_numTimesCellEligible"
+ "_numTimesCellPrivateNetworkActive"
+ "_numTimesWiFiAndCellEligible"
+ "_numTimesWiFiAndCellEligibleDeviceIneligible"
+ "_numTimesWiFiEligible"
+ "_numberOfArmedToOutrankTransitions"
+ "_numberOfIdleToArmedTransitions"
+ "_numberOfIdleToOutrankTransitions"
+ "_numberOfOutrankToIdleTransitions"
+ "_numberOfTimesInArmedStateForAtLeastFiveSeconds"
+ "_numberOfTimesInOutrankStateForAtLeastFiveSeconds"
+ "_prevCellEligible"
+ "_prevCellInexpensive"
+ "_prevCellPrivateNetworkActive"
+ "_prevCellWRMInexpensive"
+ "_prevDeviceEligible"
+ "_prevWiFiEligible"
+ "_prevWiFiSporadic"
+ "_resetDailyTelemetryMetrics"
+ "_sendDailyOutrankMetric"
+ "_setupDailyTelemetryTimer"
+ "_sporadicIsKnown"
+ "_startedCollectingMetricsFrom"
+ "_timestampBucket"
+ "_timestampTwoHourBucketForCurrentTime"
+ "_timestampTwoHourBucketForTime:"
+ "_updateStateTransitionMetricsForNewState:oldState:"
+ "batteryDepthOfDischarge"
+ "batteryRawCurrentCapacity"
+ "batteryRawMaximumCapacity"
+ "com.apple.symptoms.CellOutrank.DailyMetrics"
+ "isSporadicKnown"
+ "numTimesCellEligible"
+ "numTimesCellPrivateNetworkActive"
+ "numTimesWiFiAndCellEligible"
+ "numTimesWiFiAndCellEligibleDeviceIneligible"
+ "numTimesWiFiEligible"
+ "numberOfArmedToOutrankTransitions"
+ "numberOfIdleToArmedTransitions"
+ "numberOfIdleToOutrankTransitions"
+ "numberOfOutrankToIdleTransitions"
+ "numberOfTimesInArmedStateForAtLeastFiveSeconds"
+ "numberOfTimesInOutrankStateForAtLeastFiveSeconds"
+ "setBatteryDepthOfDischarge:"
+ "setBatteryRawCurrentCapacity:"
+ "setBatteryRawMaximumCapacity:"
+ "setTimestampBucket:"
+ "timePeriod"
+ "timestampBucket"
+ "totalDurationForCellInexpensive"
+ "totalDurationForCellWRMInexpensive"
+ "totalDurationInArmedState"
+ "totalDurationInIdleState"
+ "totalDurationInOutrankState"
+ "totalDurationOnSporadicNetworks"
+ "updateMetricsForState:"
+ "\xa5"
- "\x06"
- "<NWDeviceReport:\n\tBattery Percentage:\t\t\t%u\n\tBattery Current Capacity:\t\t%u\n\tBattery Maximum Capacity:\t\t%u\n\tBattery Design Capacity:\t\t%u\n\tBattery Absolute Capacity:\t\t%u\n\tBattery Voltage:\t\t\t%u\n\tBattery Time Remaining:\t\t\t%u\n\tBattery Temperature:\t\t\t%u\n\tBattery External Power Is Connected:\t%u\n\tBattery Fully Charged:\t\t\t%u\n\tBattery At Warn Level:\t\t\t%u\n\tBattery At Critical Level:\t\t%u\n\tRNF Enabled:\t\t\t\t%u\n\tDevice Plugged In:\t\t\t%u\n\tDevice Screen On:\t\t\t%u\n\tDevice Screen Brightness:\t\t%u\n\tMotion State:\t\t\t\t%u\n\tDevice Orientation:\t\t\t%u\n\tThermal Pressure:\t\t\t%u\n\tQUIC Experimentally Enabled:\t\t%u\n\tPrivacy Proxy Service Status:\t\t%u\n\tPrivacy Proxy User Tier:\t\t%u\n\tPrivacy Proxy Networks:\t\t%@\n\tPrivacy Proxy Traffic:\t\t%@\n>"
- "Power: battery-percentage %.2f battery-power-connected %d battery-charging %d battery-warn %d battery-critical %d battery-absolute-capacity-mAh %d battery-voltage-mV %d battery-current-capacity-%% %d battery-maximum-capacity-%% %d battery-design-capacity-mAh %d battery-time-remaining %d battery-fully-charged %d battery-temperature %d screen-brightness %u"
- "deltaRxCellularBytes"
- "deltaRxWiFiBytes"
- "deltaTxCellularBytes"
- "deltaTxWiFiBytes"
- "\x95"

```
