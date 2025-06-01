## SymptomEvaluator

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator`

```diff

-1871.100.22.0.0
-  __TEXT.__text: 0x253c20
+1871.120.6.0.0
+  __TEXT.__text: 0x253e74
   __TEXT.__auth_stubs: 0x2670
   __TEXT.__objc_methlist: 0x166fc
-  __TEXT.__cstring: 0x22f58
+  __TEXT.__cstring: 0x22f88
   __TEXT.__const: 0x738
   __TEXT.__gcc_except_tab: 0x3398
-  __TEXT.__oslogstring: 0x3daa6
+  __TEXT.__oslogstring: 0x3db8f
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.evaluator_cfg: 0x63e1
   __TEXT.default_clp: 0x2fe0

   __TEXT.baseband_clp: 0xe950
   __TEXT.bb_MAV_clp: 0xaa40
   __TEXT.modules_clp: 0x1230
-  __TEXT.__unwind_info: 0x65f8
+  __TEXT.__unwind_info: 0x664c
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x1cad
   __TEXT.__objc_methname: 0x3bc22

   __DATA_CONST.__objc_classrefs: 0xb80
   __DATA_CONST.__objc_superrefs: 0x5a0
   __DATA_CONST.__objc_arraydata: 0x7d8
-  __AUTH_CONST.__cfstring: 0x1bd40
+  __AUTH_CONST.__cfstring: 0x1bda0
   __AUTH_CONST.__objc_const: 0x6fa0
   __AUTH_CONST.__const: 0x23a0
   __AUTH_CONST.__objc_arrayobj: 0x198

   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__auth_got: 0x1350
-  __AUTH.__objc_data: 0x1540
+  __AUTH.__objc_data: 0x14a0
   __DATA.__objc_ivar: 0x2cdc
-  __DATA.__data: 0x1b10
+  __DATA.__data: 0x1b20
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x3a0
-  __DATA.__common: 0xc0
-  __DATA_DIRTY.__objc_data: 0x3e30
+  __DATA.__bss: 0x328
+  __DATA.__common: 0xa8
+  __DATA_DIRTY.__objc_data: 0x3ed0
   __DATA_DIRTY.__data: 0xb4
-  __DATA_DIRTY.__bss: 0x1398
-  __DATA_DIRTY.__common: 0x180
+  __DATA_DIRTY.__bss: 0x1418
+  __DATA_DIRTY.__common: 0x198
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 8C65E30C-45C2-32AA-AE49-609029D69190
+  UUID: 1C66B473-797F-35A3-87A1-8A31C0DBB276
   Functions: 11041
-  Symbols:   35720
-  CStrings:  25681
+  Symbols:   35721
+  CStrings:  25691
 
Symbols:
+ ___105-[FlowAnalyticsEngine performThresholdingOn:forKey:andValue:connection:createdBlock:hitBlock:errorBlock:]_block_invoke.879
+ ___110-[FlowAnalyticsEngine performQueryOnEntity:fetchRequestProperties:pred:sort:actions:service:connection:reply:]_block_invoke.876
+ ___110-[FlowAnalyticsEngine performQueryOnEntity:fetchRequestProperties:pred:sort:actions:service:connection:reply:]_block_invoke_2.878
+ ___39-[FlowAnalyticsEngine _handleSnapshot:]_block_invoke.306
+ ___40-[FlowAnalyticsEngine _pruneFlowHistory]_block_invoke.828
+ ___41-[FlowAnalyticsEngine _flowFetchForName:]_block_invoke.817
+ ___48-[FlowAnalyticsEngine _saveAndUnloadSelectState]_block_invoke.334
+ ___48-[NWActivityHelper _getNWActivitySummaryReport:]_block_invoke.461
+ ___54-[FlowAnalyticsEngine _summaryAppDomainUsageBy:reply:]_block_invoke.756
+ ___55-[FlowAnalyticsEngine _newCoreMediaAssetDownloadEvent:]_block_invoke.378
+ ___58+[FlowAnalyticsEngine identifierForUUID:replyQueue:reply:]_block_invoke.589
+ ___60-[FlowAnalyticsEngine _recentUsageForApps:replyQueue:reply:]_block_invoke.588
+ ___70-[FlowAnalyticsEngine observeValueForKeyPath:ofObject:change:context:]_block_invoke.196
+ ___70-[FlowAnalyticsEngine observeValueForKeyPath:ofObject:change:context:]_block_invoke.200
+ ___Block_byref_object_copy_.874
+ ___Block_byref_object_dispose_.875
+ ___block_literal_global.410
+ ___block_literal_global.469
+ ___block_literal_global.584
+ ___block_literal_global.586
+ ___block_literal_global.667
+ ___block_literal_global.792
+ ___block_literal_global.833
+ __unnamed_array_storage.447
+ __unnamed_array_storage.458
+ __unnamed_array_storage.551
+ __unnamed_array_storage.628
+ __unnamed_array_storage.645
+ __unnamed_array_storage.674
+ __unnamed_array_storage.675
+ __unnamed_array_storage.754
+ __unnamed_array_storage.758
+ __unnamed_array_storage.782
+ __unnamed_array_storage.794
+ __unnamed_array_storage.795
+ _kNWStatsParameterMappingUseNEHelperForSet
+ _kNetDiagUDPSockets
- ___105-[FlowAnalyticsEngine performThresholdingOn:forKey:andValue:connection:createdBlock:hitBlock:errorBlock:]_block_invoke.876
- ___110-[FlowAnalyticsEngine performQueryOnEntity:fetchRequestProperties:pred:sort:actions:service:connection:reply:]_block_invoke.873
- ___110-[FlowAnalyticsEngine performQueryOnEntity:fetchRequestProperties:pred:sort:actions:service:connection:reply:]_block_invoke_2.875
- ___39-[FlowAnalyticsEngine _handleSnapshot:]_block_invoke.303
- ___40-[FlowAnalyticsEngine _pruneFlowHistory]_block_invoke.825
- ___41-[FlowAnalyticsEngine _flowFetchForName:]_block_invoke.814
- ___48-[FlowAnalyticsEngine _saveAndUnloadSelectState]_block_invoke.331
- ___48-[NWActivityHelper _getNWActivitySummaryReport:]_block_invoke.452
- ___54-[FlowAnalyticsEngine _summaryAppDomainUsageBy:reply:]_block_invoke.753
- ___55-[FlowAnalyticsEngine _newCoreMediaAssetDownloadEvent:]_block_invoke.375
- ___58+[FlowAnalyticsEngine identifierForUUID:replyQueue:reply:]_block_invoke.586
- ___60-[FlowAnalyticsEngine _recentUsageForApps:replyQueue:reply:]_block_invoke.585
- ___70-[FlowAnalyticsEngine observeValueForKeyPath:ofObject:change:context:]_block_invoke.193
- ___70-[FlowAnalyticsEngine observeValueForKeyPath:ofObject:change:context:]_block_invoke.197
- ___Block_byref_object_copy_.871
- ___Block_byref_object_dispose_.872
- ___block_literal_global.407
- ___block_literal_global.466
- ___block_literal_global.581
- ___block_literal_global.583
- ___block_literal_global.664
- ___block_literal_global.789
- ___block_literal_global.830
- __unnamed_array_storage.444
- __unnamed_array_storage.455
- __unnamed_array_storage.548
- __unnamed_array_storage.625
- __unnamed_array_storage.642
- __unnamed_array_storage.671
- __unnamed_array_storage.672
- __unnamed_array_storage.751
- __unnamed_array_storage.755
- __unnamed_array_storage.779
- __unnamed_array_storage.791
- __unnamed_array_storage.792
- _kNWStatsParameterMappingUseNEHelper
CStrings:
+ "FlowSnapshot: %{private}@, already processed domain info"
+ "FlowSnapshot: %{private}@, waiting to process domain info until flow closing with nil fuuid"
+ "FlowSnapshot: %{private}@, will process domain info for flow closing with nil fuuid"
+ "a_l2Report_cellularOutrankPrimaryReason"
+ "a_l2Report_cellularOutranksWifi"
+ "eWiFiLQM"
+ "e_completionReason"
+ "e_l2Report_cellularOutrankPrimaryReason"
+ "e_l2Report_cellularOutranksWifi"
+ "e_l2Report_wifiLqm"
+ "udpsockets"
- "a_l2Report_cellular_outrank_primary_reason"
- "a_l2Report_cellular_outranks_wifi"
- "e_l2Report_cellular_outrank_primary_reason"
- "e_l2Report_cellular_outranks_wifi"

```
