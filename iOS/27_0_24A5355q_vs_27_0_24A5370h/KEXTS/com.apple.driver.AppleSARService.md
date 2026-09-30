## com.apple.driver.AppleSARService

> `com.apple.driver.AppleSARService`

```diff

-1563.0.0.0.0
-  __TEXT.__os_log: 0x2224b sha256:672689030c8cde5fd4e181d86b07ffcde44077eca2d4ed1d94cb5359cc4cec72
-  __TEXT.__const: 0x1646 sha256:b836ca06f0e7829e6d520d1ed753da2b66d0b406856a963f34ec230cafdd7266
-  __TEXT.__cstring: 0x1c9c9 sha256:f462e7128c8f3a6c68e81adce05adaaa4844805efaedb4272c729f0a96ccdab6
-  __TEXT_EXEC.__text: 0xe7f6c sha256:491bd6caa666850ddfceab892f0984fca4efdcbda24e2ac6a7ff5ad831577dc4
-  __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x133 sha256:cbee610b219dafa1c7016fb625cd31580b81284f6db7ec6c48d2fe6e5feed222
+1570.0.0.0.0
+  __TEXT.__os_log: 0x233e6 sha256:35aa9b33c6248bcc42d4123e58109d722f7a4ea842f2ab258b8710ecc6b0bcff
+  __TEXT.__const: 0x1246 sha256:8a42d5a5709325cb67de50e706531ebd7a6b28acc061015d42807a19f113c4c4
+  __TEXT.__cstring: 0x1dfd6 sha256:0ec8f9b4320562dfb7c3c1716b71b9c02dff296e9fb9a6cce1534a6911eefe42
+  __TEXT_EXEC.__text: 0xef6c4 sha256:004d9159f4e4ff63e9ee95dfbb3c123f7bf93e139f5bb8d466f6031124755550
+  __TEXT_EXEC.__auth_stubs: 0x730 sha256:f001c65804c78f53ae678246a803281fdb53ea69ff84f29a8b70ae0e0ff40464
+  __DATA.__data: 0x133 sha256:dc3e90fce352dfa1c40d6bb2f118f87ef0c5f0aa72adb6d3ddbadc6873087b9c
   __DATA.__common: 0x11b8 sha256:f50095b91cf5b6d3c17ab95301c6d8d4fbb3f0c53e5c6f6b1cc502b0868519fe
   __DATA.__bss: 0xa8 sha256:e3c2af35d1dfc500e16f826a071cc311bf55003a3de77de7ea3376c6b6fa2857
-  __DATA_CONST.__mod_init_func: 0xe8 sha256:011581e04ad6ea10dfcf03e91a216097a4bf2817472fe39065b3d5811beeb057
-  __DATA_CONST.__mod_term_func: 0xf0 sha256:e346069c0afc2cb389d6257f5754bec23f7236dc7a8fa29568a36a5f569e157e
-  __DATA_CONST.__const: 0xd340 sha256:8eb7e37a3ca2d1799823b295d5d8cd28ec89994b2e58fc0d451dd04dc6bec44f
-  __DATA_CONST.__kalloc_type: 0xcd80 sha256:cd682c9762e56a231c21639b81afce1e3aa827f4412c5f4d27c2786ca11fe574
-  __DATA_CONST.__kalloc_var: 0x280 sha256:dee7caf8aecf41ba4ac6332efc1a65673124c34fafb84d232cc2185fcbab685c
-  __DATA_CONST.__auth_got: 0x390 sha256:9d4d11ee1a86507718f4ec8df035204d85152bae19f1b541551d643cec6142f0
-  __DATA_CONST.__got: 0xd0 sha256:8002c98c3a2e7a7ac5423b6c954742e452416d27a5892c228afb915d970ca452
-  __DATA_CONST.__auth_ptr: 0x18 sha256:c7502cd24624f9858eb55fe99f56ec98a5c349274a244ed53f193b86770a7306
-  UUID: FF97450F-4905-306F-8312-C43EE85888BA
-  Functions: 1776
+  __DATA_CONST.__mod_init_func: 0xe8 sha256:52ca8939a2aff49cab0ced1f9385add349deef90d9d251ac96aa24ec68487f57
+  __DATA_CONST.__mod_term_func: 0xf0 sha256:e59dbb37aa42860a064d63efdff1b3b72a3626f857ff4797bfa053cccc9a02bb
+  __DATA_CONST.__const: 0xd6d0 sha256:339acf15e3777668c7b3f1cac26cbfdab96c831f0f50ea874ad12b3cdc4c0765
+  __DATA_CONST.__kalloc_type: 0xcf80 sha256:6d315d839c8fc5ae1e9e0eb3f3ddd1493416e9b674c072db87800712b67c9a94
+  __DATA_CONST.__kalloc_var: 0x280 sha256:1a16c4fe41bd096ec0ad643d53965c1dd7143ac80ae81e4302ce361b440c09bf
+  __DATA_CONST.__auth_got: 0x398 sha256:eea2da04cb9afb3edd0b7fce07745212557290abdc924a459e5a131145c66f4d
+  __DATA_CONST.__got: 0xd0 sha256:312951217e19cd5ef2b966cd72373a794ca16c2bc1d17a214655acd6e8d0fed4
+  __DATA_CONST.__auth_ptr: 0x18 sha256:0f40a65db3a6cc8623f5e92d4e85647fa4f005eac5941ef78d806d4f69e5fbf9
+  UUID: 6C4AA3F2-1EB1-30E2-AA9E-C4A075270494
+  Functions: 1814
   Symbols:   0
-  CStrings:  3340
+  CStrings:  3520
 
CStrings:
+ "#D: %s::%s:%d: Budget has been overridden. No need to assign a budget"
+ "#D: %s::%s:%d: CoreAnalytics service not available for HSAR metric"
+ "#D: %s::%s:%d: Dequeued Tx indication: %u (remaining: %u)"
+ "#D: %s::%s:%d: Enqueued Tx indication: %u (queue depth: %u)"
+ "#D: %s::%s:%d: HSAR Metric: all %u fields populated, dict count=%u, sending event"
+ "#D: %s::%s:%d: HSAR Metric: enum/state fields done, OBD=%u, BT_conn=%d, Cell_on=%d, WiFi_pwr=%d"
+ "#D: %s::%s:%d: HSAR Metric: state change field done (hasStateChanged=%d), gathering per-cluster data"
+ "#D: %s::%s:%d: Notified clients about TX state (async): %u\n"
+ "#D: %s::%s:%d: Required data not ready for HSAR metric"
+ "#D: %s::%s:%d: Tx state (%s) is remained as same as before"
+ "#D: %s::%s:%d: Updating Use Case Detection"
+ "#D: %s::%s:%d: Uplink Constraint Condition (%s) is remained as same as before"
+ "#T: %s::%s:%d: Non Colocated Antenna for cellular: %u, Number of SAR Cluster: %u, SAR Selection: %u, SAR Request Type: %s, Stewie: %u"
+ "#T: %s::%s:%d: [%s %u] 2-second next budget: %u, Previous budget: %u, Assigning budget: %u, The residual: %u"
+ "%s::%s:%d: AppleHSARMultipleRadio: Invalid mmW frequency %u GHz, clamping to %u GHz\n"
+ "%s::%s:%d: Cannot report HSAR error to userland"
+ "%s::%s:%d: Cellular Regulatory Time Average Mode is now DISABLED; Not updating regulatory time averaging for cellular"
+ "%s::%s:%d: Cellular SAR Limit = %s (index: %u, SAR Boost: %s, OBD selection: %u (original: %u), region: %u)"
+ "%s::%s:%d: Cellular TAS disabled: stopping SAR Report Monitor"
+ "%s::%s:%d: Checking Connectivity SAR Report: Monitor Started: %llu (ms), Now: %llu (ms), Monitor Diff: %llu (sec), Reports Received: %u, Expected: %llu"
+ "%s::%s:%d: Connectivity Budget Scaling Factor: %u"
+ "%s::%s:%d: Connectivity SAR Report Monitor has started. Stopping the service before starting"
+ "%s::%s:%d: Connectivity SAR Report Monitor timer expired"
+ "%s::%s:%d: Connectivity SAR Report seq mismatch! Received: %u, Expected: %u"
+ "%s::%s:%d: Connectivity TAS disabled: stopping Connectivity SAR Report Monitor"
+ "%s::%s:%d: Failed to allocate CA event for HSAR metric"
+ "%s::%s:%d: Failed to call use case detection override callback: (ret: 0x%x)"
+ "%s::%s:%d: Failed to create Connectivity SAR Report Monitor"
+ "%s::%s:%d: Failed to create OSSerialize for payload size cal"
+ "%s::%s:%d: Failed to create Tx indication event source"
+ "%s::%s:%d: Failed to reset fConnectivityBudgetScalingFactor"
+ "%s::%s:%d: HSAR Error: %s (subsystem: %u)"
+ "%s::%s:%d: HSAR Metric CA event sent successfully (%u fields)"
+ "%s::%s:%d: HSAR Metric payload serialized: ret=%u, length=%lu bytes (%u fields)"
+ "%s::%s:%d: Instance of Regulatory Info (%p), or instance of AR Buffer (%p) is not ready"
+ "%s::%s:%d: Issue found on the connectivity SAR report: received %u reports, expected %llu in %llu seconds"
+ "%s::%s:%d: No issue on the SAR report (modem not yet reporting)"
+ "%s::%s:%d: No issue on the connectivity SAR report"
+ "%s::%s:%d: No need to run Antenna Cluster Config when it is overridden"
+ "%s::%s:%d: Non-colocated mode is disabled. Minimum budget: %u"
+ "%s::%s:%d: Non-colocated mode is disabled. Using total SAR Consumed value: %u (before clamping: %u)"
+ "%s::%s:%d: One of instances is not ready: fCentralSAR (%p) fCentralSARInstantValues (%p) fCellularSAR (%p) fConnectivitySAR (%p) fCellularSARReport (%p) fCellularMPEReport (%p) currentARBuffer (%p) fAntennaClusterConfig (%p) fUWBSAR (%p) fCellularSARBudget (%p)"
+ "%s::%s:%d: One of instances is not ready: fConnectivitySAR (%p) kConnectivitySARLimitTable (%p) fRegulatoryLimit (%p) fARBuffer (%p) fWiFiStateManager (%p) fBTStateManager (%p) fSARSelectionState (%p) fCentralSAR (%p) fRegulatoryInfo (%p)"
+ "%s::%s:%d: One of instances is not ready: fRegulatoryInfo (%p) fAntennaClusterConfig (%p) fRegulatoryLimit (%p)"
+ "%s::%s:%d: Overridden consumption[%u] is adjusted: %u from %u"
+ "%s::%s:%d: Routing Use Case Detection override to HSAR: status: %u value: %u"
+ "%s::%s:%d: Simulation: %u, Budget overridng: %u, Operation mode: %s, HSAR enabled: %u -> Not to send a budget to Connectivity"
+ "%s::%s:%d: Skipping connectivity SAR report check during sleep"
+ "%s::%s:%d: Starting Connectivity SAR Report Monitor"
+ "%s::%s:%d: Stopped Connectivity SAR Report Monitor"
+ "%s::%s:%d: TAS disabled: stopping SAR Report Monitor"
+ "%s::%s:%d: TX update to %s"
+ "%s::%s:%d: Trying to do an action due to 0 connectivity SAR budget for cluster %u"
+ "%s::%s:%d: Trying to trigger logdump due to connectivity SAR report error"
+ "%s::%s:%d: Tx indication event source not set up"
+ "%s::%s:%d: Tx indication queue full — dropping oldest entry (txOn: %u)"
+ "%s::%s:%d: Updated OBD State from %u to %u"
+ "%s::%s:%d: Updated minimum mmW frequency: %u GHz"
+ "%s::%s:%d: Use Case Detection: %u (Override: %u)"
+ "%s::%s:%d: Use case detection overridden — ignoring live modem value: %u"
+ "%s::%s:%d: Use case detection override applied to regulatory bitmask: %u"
+ "%s::%s:%d: Use case detection override: status=%u value=%u"
+ "%s::%s:%d: WARNING: The Budget-Max (%u) is less than Budget-Min-Future (%u). So, the Budget-Margin (%u) is zero"
+ "%s::%s:%d: [Regulatory Limit] Mode: %s, SAR Limit: %s, MPE Agency Limit: %s, MPE Radio Limit: %s, TER Limit: %s, SAR SPLSR: %s, SAR Total Limit: %s, Non Colocated Antenna Enabled: %s, SAR External Limit: %s, MPE External: %s, OBD: %u"
+ "%s::%s:%d: [SAR/MPE/Connectivity Regulatory Averaging Duration] Cellular Mode: %s, SAR: %u seconds, MPE: %u seconds, Connectivity Mode: %s, Connectivity: %u seconds, UWB: %u seconds"
+ "%s::%s:%d: [Static Connectivity] Connectivity SAR Budget = %u (index: %u, OBD selection: %u (original: %u), region: %u)"
+ "%s::%s:%d: fConnectivityBudgetScalingFactor is NULL"
+ "%s::%s:%d: fUseCaseDetection instance is NULL!"
+ "%s::%s:%d: null input"
+ "-10..0 from Min"
+ "0-100mm Closer"
+ "0-100mm Further"
+ "0..+10 from Max"
+ "1211111212221212111111121121121121121121121121121121121121121122112112112112112112112112112112112112112112112112112112112112112112212112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211222222221121121121122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221222221121111221121121121121121121121122122121122122112122221122"
+ "121111121222121212111121121121121121121121121122121111211211212"
+ "12111112122212121211112112112112112112112112112212111121121121221"
+ "<-10 from Min"
+ ">+10 from Max"
+ ">100mm Closer"
+ ">100mm Further"
+ "Face Down"
+ "Face Up"
+ "OBD_State"
+ "Within Range"
+ "antennaClusterFromInterface_block_invoke"
+ "bt_sar_budget_cluster1"
+ "bt_sar_budget_cluster2"
+ "bt_sar_utilization_cluster1"
+ "bt_sar_utilization_cluster2"
+ "bt_ter_average_cluster1"
+ "bt_ter_average_cluster2"
+ "budgetScalingFactor"
+ "budgetScalingFactor_block_invoke"
+ "cellularBudgetAssignmentGated"
+ "cellular_connected"
+ "cellular_hp_tx"
+ "cellular_mmW_tx"
+ "cellular_mpe_budget_cluster1"
+ "cellular_mpe_consumed_cluster1"
+ "cellular_mpe_utilization_cluster1"
+ "cellular_sar_budget_cluster1"
+ "cellular_sar_budget_cluster2"
+ "cellular_sar_consumed_cluster1"
+ "cellular_sar_consumed_cluster2"
+ "cellular_sar_utilization_cluster1"
+ "cellular_sar_utilization_cluster2"
+ "cellular_ter_average_cluster1"
+ "cellular_ter_average_cluster2"
+ "cellular_ter_mpe_average_cluster1"
+ "cellular_ter_sar_average_cluster1"
+ "cellular_ter_sar_average_cluster2"
+ "checkConnectivitySARReportGated"
+ "com.apple.Telephony.HSAR"
+ "connectivity_sar_budget_cluster1"
+ "connectivity_sar_budget_cluster2"
+ "connectivity_sar_utilization_cluster1"
+ "connectivity_sar_utilization_cluster2"
+ "enqueueTxIndicationGated"
+ "hasStateChangedInAveragingWindow"
+ "kMax"
+ "overrideUseCaseDetection"
+ "overrideUseCaseDetection_block_invoke"
+ "overrideUseCaseDetection_block_invoke_2"
+ "radio_subsystem"
+ "sendCAEventHSARMetric"
+ "sendTxIndicationGated"
+ "setUseCaseDetectionOverride_block_invoke"
+ "startConnectivitySARReportMonitorGated"
+ "startConnectivitySARReportMonitorGated_block_invoke"
+ "static IOReturn AppleSARServiceUserClient::extBudgetScalingFactor(AppleSARService *, void *, IOExternalMethodArguments *)"
+ "static IOReturn AppleSARServiceUserClient::extoverrideUseCaseDetection(AppleSARService *, void *, IOExternalMethodArguments *)"
+ "stopConnectivitySARReportMonitorGated"
+ "total_ter_average_cluster1"
+ "total_ter_average_cluster2"
+ "total_ter_budget_cluster1"
+ "total_ter_budget_cluster2"
+ "total_ter_consumed_cluster1"
+ "total_ter_consumed_cluster2"
+ "total_ter_utilization_cluster1"
+ "total_ter_utilization_cluster2"
+ "updateConnectivityRegInfoInternalGated"
+ "updateTxIndicator_block_invoke"
+ "updateUseCaseDetectionGated"
+ "updateUseCaseDetectionOverrideGated"
+ "uwb_power"
+ "wifi_p2p"
+ "wifi_sar_budget_cluster1"
+ "wifi_sar_budget_cluster2"
+ "wifi_sar_utilization_cluster1"
+ "wifi_sar_utilization_cluster2"
+ "wifi_ter_average_cluster1"
+ "wifi_ter_average_cluster2"
+ "|MIC"
- "#D: %s::%s:%d: Tx state (%s) is reamined as same as before"
- "#D: %s::%s:%d: Uplink Constraint Condition (%s) is reamined as same as before"
- "#T: %s::%s:%d: Non Colocated Antenna: %u, Number of SAR Cluster: %u, SAR Selection: %s, SAR Request Type: %s, Stewie: %u"
- "#T: %s::%s:%d: [%s] 2-second next budget: %u, Previous budget: %u, Assigning budget: %u, The residual: %u"
- "%s::%s:%d: %s: max: %u, min future: %u, margin: %u"
- "%s::%s:%d: Checking SAR Report: Monitor Started: %llu (sec), Now: %llu (sec), Monitor Diff: %llu (sec), 1st SAR Report: %llu (sec), last SAR Report: %llu (sec), SAR Report Diff: %llu (sec)"
- "%s::%s:%d: Failed to send RF occlusion control signal during baseband initialization: 0x%x"
- "%s::%s:%d: Not sending HSAR error to a userclient yet"
- "%s::%s:%d: One of instances is not ready: fCentralSAR (%p) fCentralSARInstantValues (%p) fCellularSAR (%p) fConnectivitySAR (%p) fCellularSARReport (%p) fCellularMPEReport (%p) currentARBuffer (%p) fAntennaClusterConfig (%p) fUWBSAR (%p)"
- "%s::%s:%d: One of instances is not ready: fConnectivitySAR (%p), kConnectivitySARLimitTable (%p), fARBuffer (%p), fWiFiStateManager (%p), fBTStateManager (%p), fSARSelectionState (%p)"
- "%s::%s:%d: One of instances is not ready: fConnectivitySAR (%p), kConnectivitySARLimitTable (%p), fWiFiStateManager (%p), fBTStateManager (%p), fSARSelectionState (%p)"
- "%s::%s:%d: Regulatory Time Average Mode is now DISABLED, and WiFi and BT powers are off; Not updating regulatory time averaging"
- "%s::%s:%d: Simulation: %u, Budget overridng: %u, Operation mode: %s, HSAR enabled: %u, WiFi Power: %u, BT Power: %u -> Not to send a budget to Connectivity"
- "%s::%s:%d: The first SAR reported timestamp is zero when Tx is off. So, reset the value to the SAR report timestamp"
- "%s::%s:%d: Trying to trigger logdump due to SAR report error"
- "%s::%s:%d: Tx is off. Not running SAR RF Sensing logic"
- "%s::%s:%d: [Regulatory Limit] Mode: %s, SAR Limit: %s, MPE Limit: %s, TER Limit: %s, SAR SPLSR: %s, SAR Total Limit: %s, Non Colocated Antenna Enabled: %s, SAR External Limit: %s, MPE External: %s"
- "%s::%s:%d: [SAR/MPE/Connectivity Regulatory Averaging Duration] Mode: %s, SAR: %u seconds, MPE: %u seconds, Connectivity: %u seconds"
- "%s::%s:%d: [Static Connectivity] Connectivity SAR Budget = %u (index: %u, OBD: %u, region: %u)"
- "1211111212221212111111121121121121121121121121121121121121122112112112112112112112112112112112112112112112112112112112112112112212112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211222222221121121121122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221222221121111221121121121121121121121122122121122112"
- "1211111212221212121111211211211211211211211211221211211211212"
- "121111121222121212111121121121121121121121121122121121121121221"
- "sendingOutTxIndication"

```
