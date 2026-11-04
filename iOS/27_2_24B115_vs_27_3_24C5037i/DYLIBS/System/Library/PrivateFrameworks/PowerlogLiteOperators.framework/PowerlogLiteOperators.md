## PowerlogLiteOperators

> `/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`

```diff

-3486.42.1.0.0
-  __TEXT.__text: 0x4e9554
-  __TEXT.__objc_methlist: 0x2f854
-  __TEXT.__const: 0x2cc0
+3486.60.36.0.0
+  __TEXT.__text: 0x4eb760
+  __TEXT.__objc_methlist: 0x2f954
+  __TEXT.__const: 0x2cf0
   __TEXT.__swift5_typeref: 0x710
   __TEXT.__constg_swiftt: 0x544
   __TEXT.__swift5_reflstr: 0x4de

   __TEXT.__swift5_types: 0x54
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__cstring: 0x60bab
+  __TEXT.__cstring: 0x60e8c
   __TEXT.__swift5_capture: 0x73c
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift_as_entry: 0x64
   __TEXT.__swift_as_ret: 0x6c
   __TEXT.__swift_as_cont: 0xd0
-  __TEXT.__oslogstring: 0x16b24
+  __TEXT.__oslogstring: 0x172dd
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__gcc_except_tab: 0x2d90
+  __TEXT.__gcc_except_tab: 0x2db0
   __TEXT.__ustring: 0x22
-  __TEXT.__unwind_info: 0xb410
+  __TEXT.__unwind_info: 0xb448
   __TEXT.__eh_frame: 0x16f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9740
+  __DATA_CONST.__const: 0x9748
   __DATA_CONST.__objc_classlist: 0xa78
   __DATA_CONST.__objc_nlclslist: 0x268
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14e70
+  __DATA_CONST.__objc_selrefs: 0x14f18
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xb50
-  __DATA_CONST.__objc_arraydata: 0x16da0
-  __DATA_CONST.__got: 0x1b78
-  __AUTH_CONST.__const: 0x2a98
-  __AUTH_CONST.__cfstring: 0x78600
-  __AUTH_CONST.__objc_const: 0x38c70
+  __DATA_CONST.__objc_arraydata: 0x16e00
+  __DATA_CONST.__got: 0x1b88
+  __AUTH_CONST.__const: 0x2ab8
+  __AUTH_CONST.__cfstring: 0x78920
+  __AUTH_CONST.__objc_const: 0x38d90
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x6ea0
-  __AUTH_CONST.__objc_arrayobj: 0x3180
+  __AUTH_CONST.__objc_arrayobj: 0x3198
   __AUTH_CONST.__objc_dictobj: 0x5140
-  __AUTH_CONST.__objc_doubleobj: 0x1320
+  __AUTH_CONST.__objc_doubleobj: 0x1330
   __AUTH_CONST.__auth_got: 0x1960
   __AUTH.__objc_data: 0x2c10
   __AUTH.__data: 0x668
   __DATA.__objc_ivar: 0x1fac
   __DATA.__data: 0x10f8
   __DATA.__common: 0x1f8
-  __DATA_DIRTY.__objc_ivar: 0x1390
+  __DATA_DIRTY.__objc_ivar: 0x13a8
   __DATA_DIRTY.__objc_data: 0x3f58
   __DATA_DIRTY.__data: 0x728
   __DATA_DIRTY.__bss: 0x4798

   - /System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting
   - /System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
+  - /System/Library/PrivateFrameworks/RelevanceServices.framework/RelevanceServices
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SPOwner.framework/SPOwner
   - /System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 19904
-  Symbols:   25910
-  CStrings:  19924
+  Functions: 19930
+  Symbols:   25936
+  CStrings:  19994
 
Symbols:
+ +[PLBLMDebugService shouldRun]
+ +[PLBatteryAgent meetsTLCNotificationConditionsWithChargingState:uisoc:]
+ -[PLBatteryAgent lastFedDetails]
+ -[PLBatteryAgent logFedDetailsToCA:forPort:]
+ -[PLBatteryAgent setLastFedDetails:]
+ -[PLEnergyIssuesService teardownOperatorDependancies]
+ -[PLIOReportMetricsAgent apWakeFiveMinTimer]
+ -[PLIOReportMetricsAgent buildVTHeatMapSet:]
+ -[PLIOReportMetricsAgent logAPWakeFiveMin]
+ -[PLIOReportMetricsAgent sampleChannelsVTHeatMap]
+ -[PLIOReportMetricsAgent setApWakeFiveMinTimer:]
+ -[PLIOReportMetricsAgent setSampleChannelsVTHeatMap:]
+ -[PLIOReportMetricsAgent setVtHeatMapGauges:]
+ -[PLIOReportMetricsAgent setVtHeatMapMetricGroups:]
+ -[PLIOReportMetricsAgent streamVTHeatMapToOSMetrics]
+ -[PLIOReportMetricsAgent vtHeatMapGauges]
+ -[PLIOReportMetricsAgent vtHeatMapMetricGroups]
+ -[PLSiriAgent setSiriRecapGlobalEnabledNotification:]
+ -[PLSiriAgent siriRecapGlobalEnabledNotification]
+ -[PLSiriAgent updateSiriRecapDistribution:]
+ GCC_except_table117
+ GCC_except_table120
+ GCC_except_table139
+ GCC_except_table143
+ GCC_except_table196
+ GCC_except_table266
+ GCC_except_table268
+ GCC_except_table277
+ GCC_except_table284
+ GCC_except_table288
+ GCC_except_table331
+ GCC_except_table334
+ GCC_except_table338
+ GCC_except_table42
+ GCC_except_table65
+ GCC_except_table77
+ GCC_except_table81
+ _OBJC_CLASS_$_RSAudioUnderstandingSettingsManager
+ _RSMindPalaceGlobalEnabledDidChangeNotification
+ ___44-[PLBatteryAgent logFedDetailsToCA:forPort:]_block_invoke
+ ___44-[PLIOReportMetricsAgent buildVTHeatMapSet:]_block_invoke
+ ___52-[PLIOReportMetricsAgent streamVTHeatMapToOSMetrics]_block_invoke
+ ___block_descriptor_80_e8_32s40r48r56r64r72r_e25_i16?0^{__CFDictionary=}8ls32l8r40l8r48l8r56l8r64l8r72l8
- GCC_except_table116
- GCC_except_table138
- GCC_except_table142
- GCC_except_table195
- GCC_except_table265
- GCC_except_table267
- GCC_except_table275
- GCC_except_table281
- GCC_except_table287
- GCC_except_table330
- GCC_except_table333
- GCC_except_table337
- GCC_except_table43
- GCC_except_table61
- GCC_except_table70
- GCC_except_table76
- ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
CStrings:
+ "(none)"
+ "CACHED"
+ "Checking %@ with flags %u"
+ "Could not get eachFlags"
+ "Could not get flags"
+ "ExclavesInferenceProvider"
+ "FedCapabilityData"
+ "FedExtSrcCapProductID"
+ "FedExtSrcCapVendorID"
+ "FedMaxCurrent"
+ "FedMaxPower"
+ "FedMaxVoltage"
+ "FedWPDebugData"
+ "FedWPPolicyData"
+ "INSTANT"
+ "IOReportMetrics: AP Wake 5-minute timer fired"
+ "IOReportMetrics: V-T heat map subscription returned no live channels for %{public}@"
+ "IOReportMetrics: V-T heat map timer armed, interval %{public}d s"
+ "IOReportMetrics: V-T tick got a nil delta"
+ "IOReportMetrics: V-T tick: %{public}d channels, %{public}d buckets, %{public}d non-zero, %{public}lu gauges live, max %{public}@ = %{public}.3f s"
+ "IOReportMetrics: unexpected IOReport format for %@, skipping"
+ "PLBatteryUIAppRecapEnergyUsedKey"
+ "Pushing FedDetails metrics for port %d to CA: %@"
+ "RelevanceServices unavailable, skipping Siri Recap setup"
+ "Siri Recap enabled state: %d"
+ "Siri Recap global enabled changed: %@"
+ "SiriRecap"
+ "Skip %@ with flags %u - not a full AP wake reason"
+ "TLC: Charging State: %d  UISOC: %d  Meets Notification Conditions: %d"
+ "UNUSABLE"
+ "V-T HM"
+ "V-T heat map set has following subscription %{public}@"
+ "WiFi cumulative UNUSABLE: hasLastEntry=%{public}d wifiPowered=%{public}d"
+ "WiFi cumulative dataset=%{public}s (valid=%{public}d hasLastEntry=%{public}d instantTs=%{public}lu cachedTs=%{public}lu lastLoggedTs=%{public}lu)"
+ "WiFi cumulative entry stashed in lastEntryForMetricd, not persisted"
+ "WiFi cumulative entry ts=%{public}@ hasLastEntry=%{public}d metricd=%{public}d"
+ "WiFi power properties not logged from %{public}@: available=NO"
+ "WiFi power properties not logged: no wifi manager/device (manager=%{public}d device=%{public}d)"
+ "WiFi power-off cumulative entry stashed in lastEntryForMetricd, not persisted"
+ "WiFiDeviceClientCopyProperty(POWER_DEBUG_INFO) returned a non-dictionary value: class=%{public}@"
+ "WiFiDeviceClientCopyProperty(POWER_DEBUG_INFO) returned an empty dictionary"
+ "WiFiDeviceClientCopyProperty(POWER_DEBUG_INFO) returned nil, power properties not logged (associated=%{public}d)"
+ "a0-ppt0,ANE V-T HM"
+ "a0-ppt0,DRAM V-T HM"
+ "a0-ppt0,SoC V-T HM"
+ "a1-ppt0,ANE V-T HM"
+ "a1-ppt0,DRAM V-T HM"
+ "a1-ppt0,SoC V-T HM"
+ "alignFastValidSectors"
+ "alignRegularValidSectors"
+ "campo"
+ "com.apple.ExclavesInferenceProvider"
+ "com.apple.campo"
+ "com.apple.conversationd"
+ "com.apple.power.battery.FedDetails"
+ "com.apple.power.camera.property9.activeDuration"
+ "conversationd"
+ "hpBatchDropped"
+ "hpBatchHandoffs"
+ "hpEntriesByRunLen"
+ "hpHotUnits"
+ "hpMulEvictHot"
+ "hpMulInserts"
+ "hpMulLive"
+ "hpOtoInserts"
+ "hpOtoLive"
+ "hpUnits"
+ "hpUnitsByHitAlignFast"
+ "hpUnitsByHitAlignRegular"
+ "logEventBackwardWifiProperties: needModelPower=%{public}d metricd=%{public}d device=%{public}d"
+ "wifi properties: count=%{public}lu hasInstantTs=%{public}d hasCachedTs=%{public}d hasInstantPM=%{public}d hasInstantMPC=%{public}d"
- "No wifi properties"
```
