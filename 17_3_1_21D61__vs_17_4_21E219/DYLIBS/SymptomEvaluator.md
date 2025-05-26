## SymptomEvaluator

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator`

```diff

-1848.80.6.0.0
-  __TEXT.__text: 0x24e484
-  __TEXT.__auth_stubs: 0x2630
-  __TEXT.__objc_methlist: 0x1658c
-  __TEXT.__cstring: 0x22a1e
-  __TEXT.__oslogstring: 0x3c260
+1871.100.22.0.0
+  __TEXT.__text: 0x253c20
+  __TEXT.__auth_stubs: 0x2670
+  __TEXT.__objc_methlist: 0x166fc
+  __TEXT.__cstring: 0x22f58
   __TEXT.__const: 0x738
-  __TEXT.__gcc_except_tab: 0x3308
+  __TEXT.__gcc_except_tab: 0x3398
+  __TEXT.__oslogstring: 0x3daa6
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.evaluator_cfg: 0x5fbe
+  __TEXT.evaluator_cfg: 0x63e1
   __TEXT.default_clp: 0x2fe0
   __TEXT.symptoms_clp: 0x5f90
   __TEXT.network_clp: 0x4b40
   __TEXT.baseband_clp: 0xe950
   __TEXT.bb_MAV_clp: 0xaa40
   __TEXT.modules_clp: 0x1230
-  __TEXT.__unwind_info: 0x6518
+  __TEXT.__unwind_info: 0x65f8
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x1c9b
-  __TEXT.__objc_methname: 0x3b86c
-  __TEXT.__objc_methtype: 0x68a4
-  __TEXT.__objc_stubs: 0x24f00
+  __TEXT.__objc_classname: 0x1cad
+  __TEXT.__objc_methname: 0x3bc22
+  __TEXT.__objc_methtype: 0x68e0
+  __TEXT.__objc_stubs: 0x25080
   __DATA_CONST.__got: 0x6a8
-  __DATA_CONST.__const: 0x61c8
-  __DATA_CONST.__objc_classlist: 0x850
+  __DATA_CONST.__const: 0x6270
+  __DATA_CONST.__objc_classlist: 0x858
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x34bf8
-  __DATA_CONST.__objc_selrefs: 0xc428
+  __DATA_CONST.__objc_const: 0x34f50
+  __DATA_CONST.__objc_selrefs: 0xc4e0
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0xb80
+  __DATA_CONST.__objc_superrefs: 0x5a0
   __DATA_CONST.__objc_arraydata: 0x7d8
-  __AUTH_CONST.__cfstring: 0x1b8c0
-  __AUTH_CONST.__objc_const: 0x6f58
-  __AUTH_CONST.__const: 0x2218
+  __AUTH_CONST.__cfstring: 0x1bd40
+  __AUTH_CONST.__objc_const: 0x6fa0
+  __AUTH_CONST.__const: 0x23a0
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0x8c0
-  __AUTH_CONST.__objc_intobj: 0x660
+  __AUTH_CONST.__objc_intobj: 0x648
   __AUTH_CONST.__auth_ptr: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_floatobj: 0x30
-  __AUTH_CONST.__auth_got: 0x1330
-  __AUTH.__objc_data: 0x15e0
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0xb80
-  __DATA.__objc_superrefs: 0x598
-  __DATA.__objc_ivar: 0x2ca4
-  __DATA.__data: 0x1a70
+  __AUTH_CONST.__auth_got: 0x1350
+  __AUTH.__objc_data: 0x1540
+  __DATA.__objc_ivar: 0x2cdc
+  __DATA.__data: 0x1b10
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x388
+  __DATA.__bss: 0x3a0
   __DATA.__common: 0xc0
-  __DATA_DIRTY.__objc_data: 0x3d40
+  __DATA_DIRTY.__objc_data: 0x3e30
   __DATA_DIRTY.__data: 0xb4
-  __DATA_DIRTY.__bss: 0x1380
+  __DATA_DIRTY.__bss: 0x1398
   __DATA_DIRTY.__common: 0x180
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 10940
-  Symbols:   35451
-  CStrings:  21902
+  Functions: 11041
+  Symbols:   35720
+  CStrings:  22119
 
Symbols:
+ -[CAUsageDeltaTracker dealloc]
+ -[CAUsageDeltaTracker initForNetworkType:rootCause:startValue:]
+ -[CAUsageDeltaTracker recordFlowCount:]
+ -[CAUsageDeltaTracker recordUsageValue:]
+ -[CellFallbackMetric .cxx_destruct]
+ -[CellFallbackMetric _interestingTrigger]
+ -[CellFallbackMetric addCellIngressTriggers:]
+ -[CellFallbackMetric addWifiIngressTriggers:]
+ -[CellFallbackMetric adviceHeldForSecs]
+ -[CellFallbackMetric comingFromState]
+ -[CellFallbackMetric description]
+ -[CellFallbackMetric egressMotionState]
+ -[CellFallbackMetric egressTriggerInterfaceType]
+ -[CellFallbackMetric egressTrigger]
+ -[CellFallbackMetric ingressMotionState]
+ -[CellFallbackMetric ingressTriggerInterfaceType]
+ -[CellFallbackMetric ingressTrigger]
+ -[CellFallbackMetric initCellFallbackMetricWithLevel:policy:state:]
+ -[CellFallbackMetric postMetric]
+ -[CellFallbackMetric setAdviceHeldForSecs:]
+ -[CellFallbackMetric setComingFromState:]
+ -[CellFallbackMetric setEgressMotionState:]
+ -[CellFallbackMetric setEgressTrigger:]
+ -[CellFallbackMetric setEgressTriggerInterfaceType:]
+ -[CellFallbackMetric setIngressMotionState:]
+ -[CellFallbackMetric setIngressTrigger:]
+ -[CellFallbackMetric setIngressTriggerInterfaceType:]
+ -[CellularStateRelay networkSlicingStates]
+ -[CellularStateRelay setNetworkSlicingStateAtIndex:to:]
+ -[CoreTelephonyShim _deliverNetworkSlicingActiveChangedTo:forSliceIndex:]
+ -[CoreTelephonyShim connectionStateChanged:connection:dataConnectionStatusInfo:]
+ -[CoreTelephonyShim getConnectionType:activeForContext:]
+ -[CoreTelephonyShim getNetworkSlicingStates]
+ -[CoreTelephonyShim sendNetworkSlicingStatesToDelegate]
+ -[NWNetworkOfInterest _thinCopy]
+ -[NetworkAnalyticsEngine networkSlicingActiveChangedTo:forSliceIndex:]
+ -[NetworkAnalyticsStateRelay populateCellFallbackPropertiesOnCAMetric:]
+ -[SFL2Report cellularSliceActive]
+ -[SFL2Report setCellularSliceActive:]
+ -[State caMetric]
+ -[State setCaMetric:]
+ GCC_except_table111
+ GCC_except_table122
+ GCC_except_table125
+ GCC_except_table142
+ GCC_except_table149
+ GCC_except_table150
+ GCC_except_table158
+ GCC_except_table176
+ GCC_except_table191
+ GCC_except_table206
+ GCC_except_table208
+ GCC_except_table213
+ GCC_except_table232
+ GCC_except_table293
+ GCC_except_table343
+ GCC_except_table380
+ GCC_except_table387
+ GCC_except_table388
+ GCC_except_table389
+ GCC_except_table390
+ GCC_except_table415
+ GCC_except_table416
+ GCC_except_table417
+ GCC_except_table418
+ GCC_except_table42
+ GCC_except_table425
+ GCC_except_table426
+ GCC_except_table44
+ GCC_except_table470
+ GCC_except_table50
+ GCC_except_table509
+ GCC_except_table523
+ GCC_except_table534
+ GCC_except_table57
+ GCC_except_table77
+ GCC_except_table97
+ _CALaunchSequenceEventIdentifier
+ _CALaunchSequenceEvent_IsFirstUnlock
+ _CALaunchSequenceInterval_DispatchLaunchSequence
+ _CALaunchSequenceInterval_DispatchXPCCheckpoint
+ _CALaunchSequenceInterval_InitializeFlowEngine
+ _CALaunchSequenceInterval_InitializeNOIEngine
+ _CALaunchSequenceInterval_InitializeNetworkEngine
+ _CALaunchSequenceInterval_InitializePersistence
+ _CALaunchSequenceInterval_InitializeWorkspace
+ _CALaunchSequenceInterval_ProcessedFirstUnlock
+ _CALaunchSequenceInterval_TotalLaunchToXPC
+ _CAPreLaunchEvent_IsFirstUnlock
+ _CAPrelaunchEventIdentifier
+ _CAPrelaunchInterval_FirstUnlockCheck
+ _CAPrelaunchInterval_LaunchpadInitialization
+ _CAPrelaunchInterval_TotalPrelaunchToUnlockCheck
+ _CAPrelaunchInterval_XPCListenerInitialization
+ _OBJC_CLASS_$_CAUsageDeltaTracker
+ _OBJC_CLASS_$_CellFallbackMetric
+ _OBJC_IVAR_$_CAUsageDeltaTracker._flowCount
+ _OBJC_IVAR_$_CAUsageDeltaTracker._lastValue
+ _OBJC_IVAR_$_CAUsageDeltaTracker._netType
+ _OBJC_IVAR_$_CAUsageDeltaTracker._rootCause
+ _OBJC_IVAR_$_CAUsageDeltaTracker._startValue
+ _OBJC_IVAR_$_CellFallbackMetric._advice
+ _OBJC_IVAR_$_CellFallbackMetric._adviceHeldForSecs
+ _OBJC_IVAR_$_CellFallbackMetric._cellIngressTriggers
+ _OBJC_IVAR_$_CellFallbackMetric._comingFromState
+ _OBJC_IVAR_$_CellFallbackMetric._egressMotionState
+ _OBJC_IVAR_$_CellFallbackMetric._egressTrigger
+ _OBJC_IVAR_$_CellFallbackMetric._egressTriggerInterfaceType
+ _OBJC_IVAR_$_CellFallbackMetric._ingressMotionState
+ _OBJC_IVAR_$_CellFallbackMetric._ingressTrigger
+ _OBJC_IVAR_$_CellFallbackMetric._ingressTriggerInterfaceType
+ _OBJC_IVAR_$_CellFallbackMetric._policy
+ _OBJC_IVAR_$_CellFallbackMetric._state
+ _OBJC_IVAR_$_CellFallbackMetric._wifiIngressTriggers
+ _OBJC_IVAR_$_CellularStateRelay._networkSlicingStates
+ _OBJC_IVAR_$_SFL2Report._cellularSliceActive
+ _OBJC_IVAR_$_State._caMetric
+ _OBJC_METACLASS_$_CAUsageDeltaTracker
+ _OBJC_METACLASS_$_CellFallbackMetric
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _SPReportKQWorkLoopExhaustion_FatalPort
+ __OBJC_$_INSTANCE_METHODS_CAUsageDeltaTracker
+ __OBJC_$_INSTANCE_METHODS_CellFallbackMetric
+ __OBJC_$_INSTANCE_VARIABLES_CAUsageDeltaTracker
+ __OBJC_$_INSTANCE_VARIABLES_CellFallbackMetric
+ __OBJC_$_PROP_LIST_CellFallbackMetric
+ __OBJC_CLASS_RO_$_CAUsageDeltaTracker
+ __OBJC_CLASS_RO_$_CellFallbackMetric
+ __OBJC_METACLASS_RO_$_CAUsageDeltaTracker
+ __OBJC_METACLASS_RO_$_CellFallbackMetric
+ __Xkqworkloops_violation
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__119__map_value_compareIKPKcNS_12__value_typeIS3_S3_EEN12_GLOBAL__N_112CmpByContentELb1EEclB8ue170006ERKS5_RS3_
+ __ZNKSt3__119__map_value_compareIKPKcNS_12__value_typeIS3_S3_EEN12_GLOBAL__N_112CmpByContentELb1EEclB8ue170006ERS3_RKS5_
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ue170006ILi0EEEPKc
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZNSt3__127__tree_balance_after_insertB8ue170006IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ ___105-[FlowAnalyticsEngine performThresholdingOn:forKey:andValue:connection:createdBlock:hitBlock:errorBlock:]_block_invoke.876
+ ___110-[FlowAnalyticsEngine performQueryOnEntity:fetchRequestProperties:pred:sort:actions:service:connection:reply:]_block_invoke.873
+ ___110-[FlowAnalyticsEngine performQueryOnEntity:fetchRequestProperties:pred:sort:actions:service:connection:reply:]_block_invoke_2.875
+ ___113-[NetworkAnalyticsEngine performQueryOnEntity:fetchRequestProperties:pred:sort:actions:service:connection:reply:]_block_invoke.1265
+ ___23-[ServiceImpl shutdown]_block_invoke.174
+ ___27-[CellFallbackHandler init]_block_invoke.207
+ ___27-[CellFallbackHandler init]_block_invoke.213
+ ___27-[CellFallbackHandler init]_block_invoke.214
+ ___27-[CellFallbackHandler init]_block_invoke.215
+ ___27-[CellFallbackHandler init]_block_invoke.219
+ ___27-[CellFallbackHandler init]_block_invoke_2.208
+ ___27-[CellFallbackHandler init]_block_invoke_2.220
+ ___27-[CellFallbackHandler init]_block_invoke_3.209
+ ___30-[CAUsageDeltaTracker dealloc]_block_invoke
+ ___32-[CellFallbackMetric postMetric]_block_invoke
+ ___33-[CellFallbackHandler _dumpState]_block_invoke.338
+ ___34-[InterfaceTypeTracker _dumpState]_block_invoke_2
+ ___37-[ServiceImpl abortRNFTestWithReply:]_block_invoke.171
+ ___39-[CoreTelephonyShim _updateSubscribers]_block_invoke.259
+ ___39-[CoreTelephonyShim _updateSubscribers]_block_invoke.261
+ ___39-[FlowAnalyticsEngine _handleSnapshot:]_block_invoke.303
+ ___40-[CellFallbackHandler _peekIntoCellPlan]_block_invoke.370
+ ___40-[CellFallbackHandler _peekIntoCellPlan]_block_invoke.371
+ ___40-[FlowAnalyticsEngine _pruneFlowHistory]_block_invoke.825
+ ___40-[ServiceImpl clientTransactionsRelease]_block_invoke.173
+ ___41-[FlowAnalyticsEngine _flowFetchForName:]_block_invoke.814
+ ___43-[NetworkAnalyticsEngine _armDOASuspector:]_block_invoke.1213
+ ___44-[NWActivityHandler setUpBatteryAccumulator]_block_invoke_14
+ ___45-[ArbitratorExpertSystemHandler noteSymptom:]_block_invoke_6
+ ___45-[CoreTelephonyShim carrierSettingsDidChange]_block_invoke.254
+ ___45-[CoreTelephonyShim carrierSettingsDidChange]_block_invoke.255
+ ___45-[CoreTelephonyShim carrierSettingsDidChange]_block_invoke.256
+ ___45-[NetworkAnalyticsEngine _processCTCellInfo:]_block_invoke.817
+ ___45-[ServiceImpl _serviceReadyCheckPointRelease]_block_invoke
+ ___46-[CellFallbackHandler _completeInitialization]_block_invoke.249
+ ___46-[CellFallbackHandler _completeInitialization]_block_invoke.251
+ ___46-[CellFallbackHandler _completeInitialization]_block_invoke.252
+ ___46-[CellFallbackHandler _completeInitialization]_block_invoke.254
+ ___46-[CellFallbackHandler _completeInitialization]_block_invoke.255
+ ___46-[CellFallbackHandler _completeInitialization]_block_invoke.257
+ ___46-[CellFallbackHandler _completeInitialization]_block_invoke.258
+ ___46-[CellFallbackHandler _completeInitialization]_block_invoke.259
+ ___46-[CellFallbackHandler _completeInitialization]_block_invoke_2.261
+ ___47-[CellFallbackHandler _updateCellFallbackState]_block_invoke.467
+ ___47-[CellFallbackHandler _updateCellFallbackState]_block_invoke.472
+ ___48-[FlowAnalyticsEngine _saveAndUnloadSelectState]_block_invoke.331
+ ___48-[NWActivityHelper _getNWActivitySummaryReport:]_block_invoke.452
+ ___49-[NOIAnalyticsEngine _bottomUpNOIEvent:withInfo:]_block_invoke.90
+ ___49-[NOIAnalyticsEngine _bottomUpNOIEvent:withInfo:]_block_invoke.93
+ ___51-[CoreTelephonyShim registerForCTDumpNotifications]_block_invoke.281
+ ___51-[NetworkAnalyticsEngine _idleExitTransactionCheck]_block_invoke.1212
+ ___52-[CellFallbackHandler _canUseApps:replyQueue:reply:]_block_invoke.454
+ ___52-[CellFallbackHandler _canUseApps:replyQueue:reply:]_block_invoke.456
+ ___53-[CoreTelephonyShim unregisterForCTDumpNotifications]_block_invoke.282
+ ___53-[NetworkAnalyticsEngine didReceiveProtocolSnapshot:]_block_invoke.1016
+ ___54-[FlowAnalyticsEngine _summaryAppDomainUsageBy:reply:]_block_invoke.753
+ ___54-[NetworkAnalyticsEngine _armFatalSuspector:isActive:]_block_invoke.1222
+ ___54-[NetworkAnalyticsEngine _armFatalSuspector:isActive:]_block_invoke.1223
+ ___55-[FlowAnalyticsEngine _newCoreMediaAssetDownloadEvent:]_block_invoke.375
+ ___55-[NetworkAnalyticsEngine _layer2MetricsOn:queue:reply:]_block_invoke.1272
+ ___55-[NetworkAnalyticsEngine _layer2MetricsOn:queue:reply:]_block_invoke.1273
+ ___57-[NetworkAnalyticsEngine _awdCaptureIn:replyQueue:reply:]_block_invoke.1371
+ ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.886
+ ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.897
+ ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.905
+ ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.910
+ ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.911
+ ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.913
+ ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.917
+ ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke_2.898
+ ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke_2.915
+ ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke_3.890
+ ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke_3.900
+ ___58+[FlowAnalyticsEngine identifierForUUID:replyQueue:reply:]_block_invoke.586
+ ___58-[ServiceImpl startRNFTestWithOptions:scenarioName:reply:]_block_invoke.168
+ ___60+[AppTracker endTrafficClassFlowSnapshot:periodUsecs:reply:]_block_invoke.320
+ ___60-[FlowAnalyticsEngine _recentUsageForApps:replyQueue:reply:]_block_invoke.585
+ ___61-[NetworkAnalyticsEngine _performNetAttachmentQueryOn:reply:]_block_invoke.1269
+ ___61-[NetworkAnalyticsEngine wifiShim_L2NewMetrics:forInterface:]_block_invoke.1057
+ ___62-[NetworkAnalyticsEngine _awdCaptureInstant:replyQueue:reply:]_block_invoke.1368
+ ___63-[NetworkAnalyticsEngine _getAuditableLoadedLQMOn:queue:reply:]_block_invoke.795
+ ___66-[NetworkAnalyticsEngine _registerForSIMStatusChangeNotification:]_block_invoke.926
+ ___68-[CoreTelephonyShim _dispatchCellInfoResult:error:queue:completion:]_block_invoke.266
+ ___70-[CellFallbackHandler generateInfoForId:context:uuid:completionBlock:]_block_invoke.525
+ ___70-[CellFallbackHandler observeValueForKeyPath:ofObject:change:context:]_block_invoke.349
+ ___70-[CellFallbackHandler observeValueForKeyPath:ofObject:change:context:]_block_invoke.351
+ ___70-[CellFallbackHandler observeValueForKeyPath:ofObject:change:context:]_block_invoke.352
+ ___70-[FlowAnalyticsEngine observeValueForKeyPath:ofObject:change:context:]_block_invoke.193
+ ___70-[FlowAnalyticsEngine observeValueForKeyPath:ofObject:change:context:]_block_invoke.197
+ ___70-[NetworkAnalyticsEngine networkSlicingActiveChangedTo:forSliceIndex:]_block_invoke
+ ___74-[ArbitratorExpertSystemHandler scheduleABCNotificationForCarrierSeedUser]_block_invoke.256
+ ___74-[CellFallbackHandler _trackCellUsageAfterTriggerDisconnectWithNewSeries:]_block_invoke.480
+ ___76-[NetworkAnalyticsEngine _usageToLOICorrelationFor:scopedToLOI:queue:reply:]_block_invoke.1283
+ ___78-[NetworkAnalyticsEngine _estimatedTransferTimeOn:forPayloadInfo:queue:reply:]_block_invoke.1274
+ ___78-[NetworkAnalyticsEngine _estimatedTransferTimeOn:forPayloadInfo:queue:reply:]_block_invoke_2.1275
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1144
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1154
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1158
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1165
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1173
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1186
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1190
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke_2.1177
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke_2.1191
+ ___82-[FlowAnalyticsEngine getNetworkBitmapsWithNames:startTime:endTime:options:reply:]_block_invoke_2
+ ___82-[FlowAnalyticsEngine getNetworkBitmapsWithNames:startTime:endTime:options:reply:]_block_invoke_3
+ ___88-[ArbitratorExpertSystemHandler triggerABCSnapshotWithSignature:events:uuid:parameters:]_block_invoke.220
+ ___92-[CellFallbackHandler _idempotentInitializationFromIdleWithCellRelay:wifiRelay:motionRelay:]_block_invoke.278
+ ___92-[CellFallbackHandler _idempotentInitializationFromIdleWithCellRelay:wifiRelay:motionRelay:]_block_invoke.279
+ ___92-[CellFallbackHandler _idempotentInitializationFromIdleWithCellRelay:wifiRelay:motionRelay:]_block_invoke.281
+ ___92-[CellFallbackHandler _idempotentInitializationFromIdleWithCellRelay:wifiRelay:motionRelay:]_block_invoke.283
+ ___92-[CellFallbackHandler _idempotentInitializationFromIdleWithCellRelay:wifiRelay:motionRelay:]_block_invoke.284
+ ___92-[CellFallbackHandler _idempotentInitializationFromIdleWithCellRelay:wifiRelay:motionRelay:]_block_invoke.285
+ ___92-[CellFallbackHandler _idempotentInitializationFromIdleWithCellRelay:wifiRelay:motionRelay:]_block_invoke.286
+ ___92-[NetworkAnalyticsEngine _setupCoreTelephonyAndBasebandNotificationsOnElevatedPriorityQueue]_block_invoke
+ ___Block_byref_object_copy_.871
+ ___Block_byref_object_dispose_.872
+ ___block_descriptor_40_e8_32r_e27_v32?0"AppTracker"8Q16^B24lr32l8
+ ___block_descriptor_41_e5_v8?0l
+ ___block_descriptor_41_e8_32r_e5_v8?0lr32l8
+ ___block_literal_global.1032
+ ___block_literal_global.1090
+ ___block_literal_global.1179
+ ___block_literal_global.1264
+ ___block_literal_global.1271
+ ___block_literal_global.1285
+ ___block_literal_global.133
+ ___block_literal_global.1361
+ ___block_literal_global.170
+ ___block_literal_global.179
+ ___block_literal_global.195
+ ___block_literal_global.218
+ ___block_literal_global.222
+ ___block_literal_global.275
+ ___block_literal_global.322
+ ___block_literal_global.324
+ ___block_literal_global.341
+ ___block_literal_global.347
+ ___block_literal_global.407
+ ___block_literal_global.463
+ ___block_literal_global.466
+ ___block_literal_global.50
+ ___block_literal_global.52
+ ___block_literal_global.55
+ ___block_literal_global.581
+ ___block_literal_global.583
+ ___block_literal_global.62
+ ___block_literal_global.664
+ ___block_literal_global.67
+ ___block_literal_global.70
+ ___block_literal_global.789
+ ___block_literal_global.830
+ ___block_literal_global.839
+ ___block_literal_global.875
+ ___block_literal_global.888
+ ___block_literal_global.921
+ ___block_literal_global.923
+ ___block_literal_global.925
+ ___cell_server_connection_callback_block_invoke.731
+ ___cell_server_connection_callback_block_invoke.732
+ ___cell_server_connection_callback_block_invoke.736
+ ___config_callback_block_invoke.757
+ ___config_callback_block_invoke.758
+ ___config_callback_block_invoke.759
+ ___destroyMeasurementType_block_invoke
+ ___destroyMeasurementType_block_invoke.53
+ ___destroyMeasurementType_block_invoke.53.cold.1
+ ___destroyMeasurementType_block_invoke.cold.1
+ ___getMeasurement_block_invoke
+ ___getMeasurement_block_invoke.56
+ ___initializeActivityMeasurements_block_invoke
+ ___measureLaunchXPCHandle_block_invoke
+ ___setMeasurement_block_invoke
+ ___setMeasurement_block_invoke.57
+ ___setMeasurement_block_invoke.57.cold.1
+ ___setMeasurement_block_invoke.cold.1
+ ___submitMeasurementsToCA_block_invoke
+ ___submitMeasurementsToCA_block_invoke.61
+ ___submitMeasurementsToCA_block_invoke.65
+ ___submitMeasurementsToCA_block_invoke.68
+ __launchSequenceActivityMeasurements
+ __os_log_debug_impl
+ __os_log_error_impl
+ __prelaunchActivityMeasurements
+ __unnamed_array_storage.444
+ __unnamed_array_storage.455
+ __unnamed_array_storage.548
+ __unnamed_array_storage.625
+ __unnamed_array_storage.642
+ __unnamed_array_storage.672
+ __unnamed_array_storage.755
+ __unnamed_array_storage.779
+ __unnamed_array_storage.791
+ __unnamed_array_storage.792
+ _allocateMeasurementType
+ _allocateMeasurementType.cold.1
+ _allocateMeasurementType.cold.2
+ _allocateMeasurementType.cold.3
+ _allocateMeasurementType.cold.4
+ _allocateMeasurementType.cold.5
+ _allocateMeasurementType.cold.6
+ _allocateMeasurementType.cold.7
+ _allocateMeasurementType.cold.8
+ _allocateMeasurementType.cold.9
+ _analyticsDictionaryForLaunchSequence
+ _analyticsDictionaryForLaunchSequence.cold.1
+ _analyticsDictionaryForLaunchSequence.cold.2
+ _analyticsDictionaryForPrelaunchSequence
+ _analyticsDictionaryForPrelaunchSequence.cold.1
+ _analyticsDictionaryForPrelaunchSequence.cold.2
+ _clock_gettime_nsec_np
+ _destroyAllMeasurementTypes
+ _destroyMeasurementType
+ _destroyMeasurementType.cold.1
+ _getMeasurement
+ _getMeasurement.cold.1
+ _initializeActivityMeasurements
+ _initializeActivityMeasurements.cold.1
+ _initializeActivityMeasurements.initToken
+ _kNWStatsParameterMappingUseNEHelper
+ _kNetDiagOptPcapBufferSize
+ _kResourceNotifyEventKQWorkloopsExhaustionTrigger
+ _launchseq_lock
+ _logLaunchSequenceEventTimeline
+ _markMeasurement
+ _measureLaunchXPCHandle
+ _measureLaunchXPCHandle.launchXPCHandle
+ _measureLaunchXPCHandle.launchXPCToken
+ _microsecondsFromMachAbsoluteTime
+ _millisecondsFromBaselineMachAbsoluteTime
+ _millisecondsFromBaselineNanosecondTime
+ _millisecondsFromMachAbsoluteTime
+ _objc_msgSend$_deliverNetworkSlicingActiveChangedTo:forSliceIndex:
+ _objc_msgSend$_interestingTrigger
+ _objc_msgSend$_processSymptomsdNoDefaultRoute:symptomName:
+ _objc_msgSend$_thinCopy
+ _objc_msgSend$caMetric
+ _objc_msgSend$cellularSliceActive
+ _objc_msgSend$getConnectionState:connectionType:error:
+ _objc_msgSend$getConnectionType:activeForContext:
+ _objc_msgSend$getNetworkSlicingStates
+ _objc_msgSend$initCellFallbackMetricWithLevel:policy:state:
+ _objc_msgSend$initWithSet:copyItems:
+ _objc_msgSend$isSubFlow
+ _objc_msgSend$networkSlicingActiveChangedTo:forSliceIndex:
+ _objc_msgSend$networkSlicingStates
+ _objc_msgSend$populateCellFallbackPropertiesOnCAMetric:
+ _objc_msgSend$postMetric
+ _objc_msgSend$sendNetworkSlicingStatesToDelegate
+ _objc_msgSend$setCaMetric:
+ _objc_msgSend$setCellularSliceActive:
+ _objc_msgSend$setEgressMotionState:
+ _objc_msgSend$setEgressTriggerInterfaceType:
+ _objc_msgSend$setIngressMotionState:
+ _objc_msgSend$setIngressTriggerInterfaceType:
+ _objc_msgSend$setNetworkSlicingStateAtIndex:to:
+ _prelaunch_lock
+ _receive_kqworkloops_violation
+ _setMeasurement
+ _sf_synchronize
+ _submitAllMeasurementsToCA
+ _submitMeasurementsToCA
- +[CellFallbackHandler awdWifiAssistPolicyForRNFPolicy:]
- +[State createAndInitializeAWDMetricForStateWithLevel:activationIdentifier:policy:andSignature:]
- -[AWDUsageDeltaTracker dealloc]
- -[AWDUsageDeltaTracker initForNetworkType:rootCause:startValue:]
- -[AWDUsageDeltaTracker recordFlowCount:]
- -[AWDUsageDeltaTracker recordUsageValue:]
- -[AnalyticsLaunchpad launchSequence]
- -[CellFallbackHandler _motionToAwdCode]
- -[State awdMetric]
- -[State setAwdMetric:]
- -[SymptomExpertSystemHandler _processSymptomsdMbufPeak:symptomName:]
- GCC_except_table107
- GCC_except_table121
- GCC_except_table151
- GCC_except_table156
- GCC_except_table167
- GCC_except_table177
- GCC_except_table185
- GCC_except_table203
- GCC_except_table207
- GCC_except_table209
- GCC_except_table210
- GCC_except_table220
- GCC_except_table229
- GCC_except_table288
- GCC_except_table337
- GCC_except_table374
- GCC_except_table377
- GCC_except_table381
- GCC_except_table382
- GCC_except_table384
- GCC_except_table405
- GCC_except_table409
- GCC_except_table410
- GCC_except_table412
- GCC_except_table419
- GCC_except_table420
- GCC_except_table464
- GCC_except_table503
- GCC_except_table517
- GCC_except_table528
- GCC_except_table56
- GCC_except_table67
- GCC_except_table73
- GCC_except_table74
- GCC_except_table98
- _OBJC_CLASS_$_AWDUsageDeltaTracker
- _OBJC_IVAR_$_AWDUsageDeltaTracker.flowCount
- _OBJC_IVAR_$_AWDUsageDeltaTracker.lastValue
- _OBJC_IVAR_$_AWDUsageDeltaTracker.netType
- _OBJC_IVAR_$_AWDUsageDeltaTracker.rootCause
- _OBJC_IVAR_$_AWDUsageDeltaTracker.startValue
- _OBJC_IVAR_$_CellFallbackHandler.awdAgent
- _OBJC_IVAR_$_State._awdMetric
- _OBJC_METACLASS_$_AWDUsageDeltaTracker
- __OBJC_$_INSTANCE_METHODS_AWDUsageDeltaTracker
- __OBJC_$_INSTANCE_VARIABLES_AWDUsageDeltaTracker
- __OBJC_CLASS_RO_$_AWDUsageDeltaTracker
- __OBJC_METACLASS_RO_$_AWDUsageDeltaTracker
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__119__map_value_compareIKPKcNS_12__value_typeIS3_S3_EEN12_GLOBAL__N_112CmpByContentELb1EEclB7v160006ERKS5_RS3_
- __ZNKSt3__119__map_value_compareIKPKcNS_12__value_typeIS3_S3_EEN12_GLOBAL__N_112CmpByContentELb1EEclB7v160006ERS3_RKS5_
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B7v160006IDnEEPKc
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZNSt3__127__tree_balance_after_insertB7v160006IPNS_16__tree_node_baseIPvEEEEvT_S5_
- ___105-[FlowAnalyticsEngine performThresholdingOn:forKey:andValue:connection:createdBlock:hitBlock:errorBlock:]_block_invoke.874
- ___110-[FlowAnalyticsEngine performQueryOnEntity:fetchRequestProperties:pred:sort:actions:service:connection:reply:]_block_invoke.871
- ___110-[FlowAnalyticsEngine performQueryOnEntity:fetchRequestProperties:pred:sort:actions:service:connection:reply:]_block_invoke_2.873
- ___113-[NetworkAnalyticsEngine performQueryOnEntity:fetchRequestProperties:pred:sort:actions:service:connection:reply:]_block_invoke.1256
- ___23-[ServiceImpl shutdown]_block_invoke.172
- ___27-[CellFallbackHandler init]_block_invoke.195
- ___27-[CellFallbackHandler init]_block_invoke.201
- ___27-[CellFallbackHandler init]_block_invoke.202
- ___27-[CellFallbackHandler init]_block_invoke.203
- ___27-[CellFallbackHandler init]_block_invoke.208
- ___27-[CellFallbackHandler init]_block_invoke_2.196
- ___27-[CellFallbackHandler init]_block_invoke_2.209
- ___27-[CellFallbackHandler init]_block_invoke_3.197
- ___33-[CellFallbackHandler _dumpState]_block_invoke.326
- ___37-[ServiceImpl abortRNFTestWithReply:]_block_invoke.169
- ___39-[CoreTelephonyShim _updateSubscribers]_block_invoke.256
- ___39-[CoreTelephonyShim _updateSubscribers]_block_invoke.258
- ___39-[FlowAnalyticsEngine _handleSnapshot:]_block_invoke.305
- ___40-[CellFallbackHandler _peekIntoCellPlan]_block_invoke.359
- ___40-[CellFallbackHandler _peekIntoCellPlan]_block_invoke.360
- ___40-[FlowAnalyticsEngine _pruneFlowHistory]_block_invoke.821
- ___40-[ServiceImpl clientTransactionsRelease]_block_invoke.171
- ___41-[FlowAnalyticsEngine _flowFetchForName:]_block_invoke.810
- ___43-[NetworkAnalyticsEngine _armDOASuspector:]_block_invoke.1204
- ___45-[CoreTelephonyShim carrierSettingsDidChange]_block_invoke.249
- ___45-[CoreTelephonyShim carrierSettingsDidChange]_block_invoke.251
- ___45-[CoreTelephonyShim carrierSettingsDidChange]_block_invoke.253
- ___45-[NetworkAnalyticsEngine _processCTCellInfo:]_block_invoke.809
- ___46-[CellFallbackHandler _completeInitialization]_block_invoke.233
- ___46-[CellFallbackHandler _completeInitialization]_block_invoke.236
- ___46-[CellFallbackHandler _completeInitialization]_block_invoke.238
- ___46-[CellFallbackHandler _completeInitialization]_block_invoke.240
- ___46-[CellFallbackHandler _completeInitialization]_block_invoke.241
- ___46-[CellFallbackHandler _completeInitialization]_block_invoke.243
- ___46-[CellFallbackHandler _completeInitialization]_block_invoke.246
- ___46-[CellFallbackHandler _completeInitialization]_block_invoke.248
- ___46-[CellFallbackHandler _completeInitialization]_block_invoke_2.250
- ___47-[CellFallbackHandler _updateCellFallbackState]_block_invoke.456
- ___47-[CellFallbackHandler _updateCellFallbackState]_block_invoke.461
- ___48-[FlowAnalyticsEngine _saveAndUnloadSelectState]_block_invoke.327
- ___48-[NWActivityHelper _getNWActivitySummaryReport:]_block_invoke.446
- ___49-[NOIAnalyticsEngine _bottomUpNOIEvent:withInfo:]_block_invoke.91
- ___49-[NOIAnalyticsEngine _bottomUpNOIEvent:withInfo:]_block_invoke.95
- ___51-[CoreTelephonyShim registerForCTDumpNotifications]_block_invoke.279
- ___51-[NetworkAnalyticsEngine _idleExitTransactionCheck]_block_invoke.1203
- ___52-[CellFallbackHandler _canUseApps:replyQueue:reply:]_block_invoke.443
- ___52-[CellFallbackHandler _canUseApps:replyQueue:reply:]_block_invoke.445
- ___53-[CoreTelephonyShim unregisterForCTDumpNotifications]_block_invoke.280
- ___53-[NetworkAnalyticsEngine didReceiveProtocolSnapshot:]_block_invoke.1007
- ___54-[FlowAnalyticsEngine _summaryAppDomainUsageBy:reply:]_block_invoke.749
- ___54-[NetworkAnalyticsEngine _armFatalSuspector:isActive:]_block_invoke.1213
- ___54-[NetworkAnalyticsEngine _armFatalSuspector:isActive:]_block_invoke.1214
- ___55-[FlowAnalyticsEngine _newCoreMediaAssetDownloadEvent:]_block_invoke.371
- ___55-[NetworkAnalyticsEngine _layer2MetricsOn:queue:reply:]_block_invoke.1263
- ___55-[NetworkAnalyticsEngine _layer2MetricsOn:queue:reply:]_block_invoke.1264
- ___57-[NetworkAnalyticsEngine _awdCaptureIn:replyQueue:reply:]_block_invoke.1362
- ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.868
- ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.888
- ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.896
- ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.901
- ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.902
- ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.904
- ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.908
- ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke_2.880
- ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke_2.906
- ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke_3.881
- ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke_3.891
- ___58+[FlowAnalyticsEngine identifierForUUID:replyQueue:reply:]_block_invoke.585
- ___58-[ServiceImpl startRNFTestWithOptions:scenarioName:reply:]_block_invoke.166
- ___60+[AppTracker endTrafficClassFlowSnapshot:periodUsecs:reply:]_block_invoke.315
- ___60-[FlowAnalyticsEngine _recentUsageForApps:replyQueue:reply:]_block_invoke.584
- ___61-[NetworkAnalyticsEngine _performNetAttachmentQueryOn:reply:]_block_invoke.1260
- ___61-[NetworkAnalyticsEngine wifiShim_L2NewMetrics:forInterface:]_block_invoke.1048
- ___62-[NetworkAnalyticsEngine _awdCaptureInstant:replyQueue:reply:]_block_invoke.1359
- ___63-[NetworkAnalyticsEngine _getAuditableLoadedLQMOn:queue:reply:]_block_invoke.787
- ___66-[NetworkAnalyticsEngine _registerForSIMStatusChangeNotification:]_block_invoke.917
- ___68-[CoreTelephonyShim _dispatchCellInfoResult:error:queue:completion:]_block_invoke.264
- ___70-[CellFallbackHandler generateInfoForId:context:uuid:completionBlock:]_block_invoke.516
- ___70-[CellFallbackHandler observeValueForKeyPath:ofObject:change:context:]_block_invoke.337
- ___70-[CellFallbackHandler observeValueForKeyPath:ofObject:change:context:]_block_invoke.339
- ___70-[CellFallbackHandler observeValueForKeyPath:ofObject:change:context:]_block_invoke.340
- ___70-[FlowAnalyticsEngine observeValueForKeyPath:ofObject:change:context:]_block_invoke.196
- ___70-[FlowAnalyticsEngine observeValueForKeyPath:ofObject:change:context:]_block_invoke.200
- ___74-[ArbitratorExpertSystemHandler scheduleABCNotificationForCarrierSeedUser]_block_invoke.247
- ___74-[CellFallbackHandler _trackCellUsageAfterTriggerDisconnectWithNewSeries:]_block_invoke.469
- ___76-[NetworkAnalyticsEngine _usageToLOICorrelationFor:scopedToLOI:queue:reply:]_block_invoke.1274
- ___78-[NetworkAnalyticsEngine _estimatedTransferTimeOn:forPayloadInfo:queue:reply:]_block_invoke.1265
- ___78-[NetworkAnalyticsEngine _estimatedTransferTimeOn:forPayloadInfo:queue:reply:]_block_invoke_2.1266
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1135
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1145
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1149
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1156
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1164
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1177
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1181
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke_2.1168
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke_2.1182
- ___82-[FlowAnalyticsEngine getNetworkBitmapsWithNames:startTime:endTime:options:reply:]_block_invoke.832
- ___82-[FlowAnalyticsEngine getNetworkBitmapsWithNames:startTime:endTime:options:reply:]_block_invoke.833
- ___88-[ArbitratorExpertSystemHandler triggerABCSnapshotWithSignature:events:uuid:parameters:]_block_invoke.211
- ___92-[CellFallbackHandler _idempotentInitializationFromIdleWithCellRelay:wifiRelay:motionRelay:]_block_invoke.267
- ___92-[CellFallbackHandler _idempotentInitializationFromIdleWithCellRelay:wifiRelay:motionRelay:]_block_invoke.268
- ___92-[CellFallbackHandler _idempotentInitializationFromIdleWithCellRelay:wifiRelay:motionRelay:]_block_invoke.269
- ___92-[CellFallbackHandler _idempotentInitializationFromIdleWithCellRelay:wifiRelay:motionRelay:]_block_invoke.271
- ___92-[CellFallbackHandler _idempotentInitializationFromIdleWithCellRelay:wifiRelay:motionRelay:]_block_invoke.272
- ___92-[CellFallbackHandler _idempotentInitializationFromIdleWithCellRelay:wifiRelay:motionRelay:]_block_invoke.273
- ___92-[CellFallbackHandler _idempotentInitializationFromIdleWithCellRelay:wifiRelay:motionRelay:]_block_invoke.274
- ___Block_byref_object_copy_.869
- ___Block_byref_object_dispose_.870
- ___block_literal_global.1023
- ___block_literal_global.1081
- ___block_literal_global.109
- ___block_literal_global.1170
- ___block_literal_global.1255
- ___block_literal_global.1262
- ___block_literal_global.1276
- ___block_literal_global.1352
- ___block_literal_global.157
- ___block_literal_global.165
- ___block_literal_global.168
- ___block_literal_global.190
- ___block_literal_global.213
- ___block_literal_global.273
- ___block_literal_global.314
- ___block_literal_global.317
- ___block_literal_global.335
- ___block_literal_global.452
- ___block_literal_global.465
- ___block_literal_global.580
- ___block_literal_global.582
- ___block_literal_global.663
- ___block_literal_global.785
- ___block_literal_global.826
- ___block_literal_global.831
- ___block_literal_global.866
- ___block_literal_global.879
- ___block_literal_global.912
- ___block_literal_global.914
- ___block_literal_global.916
- ___cell_server_connection_callback_block_invoke.721
- ___cell_server_connection_callback_block_invoke.722
- ___cell_server_connection_callback_block_invoke.728
- ___config_callback_block_invoke.749
- ___config_callback_block_invoke.750
- ___config_callback_block_invoke.751
- __unnamed_array_storage.440
- __unnamed_array_storage.454
- __unnamed_array_storage.547
- __unnamed_array_storage.624
- __unnamed_array_storage.641
- __unnamed_array_storage.670
- __unnamed_array_storage.747
- __unnamed_array_storage.775
- __unnamed_array_storage.787
- __unnamed_array_storage.788
- _kNWStatsParameterMappingUseNEHelperForSet
- _objc_msgSend$_motionToAwdCode
- _objc_msgSend$_processSymptomsdMbufPeak:symptomName:
- _objc_msgSend$awdWifiAssistPolicyForRNFPolicy:
- _objc_msgSend$createAndInitializeAWDMetricForStateWithLevel:activationIdentifier:policy:andSignature:
- _objc_msgSend$digest
- _objc_msgSend$launchSequence
- _objc_msgSend$setEgressMobilityCode:
- _objc_msgSend$setFlowsImpactedCount:
- _objc_msgSend$setIngressMobilityCode:
- _objc_msgSend$setIngressTriggerSignatures:
- _objc_msgSend$setUsageAttributedTo:
- _objc_msgSend$setUsageBytes:
- _synchronize
CStrings:
+ "\x01a\x13"
+ "\b\x11\x12\x81\x14\x11'\x11#"
+ "\t\t\tCFSM error while exiting %@, metric instance can not be nil"
+ "\t\t\tCFSM error while posting metrics to CA after exiting %@"
+ "\t\tCFSM error while exiting %@, metric instance can not be nil"
+ "\t\tCFSM error while posting metrics to CA after exiting %@"
+ "  Begin persistence initialization: %llums"
+ "  Begin workspace initialization: %llums"
+ "  End persistence initialization: %llums"
+ "  End workspace initialization: %llums"
+ "  First-unlock check: %llums"
+ "  Flow Engine allocate: %llums"
+ "  Flow Engine initialized: %llums"
+ "  Generating report for kqworkloop exhaustion"
+ "  Handled unlock checkpoint: %llums"
+ "  IsFirstUnlock: %{BOOL}d"
+ "  Launchpad initialization: %llums"
+ "  NOI Engine allocate: %llums"
+ "  NOI Engine initialized: %llums"
+ "  Network Engine allocate: %llums"
+ "  Network Engine initialized: %llums"
+ "  XPC checkpoint ready: %llums"
+ "  XPCListener initialization: %llums"
+ "%016llX "
+ "(viaNEHelper)"
+ "+ First unlock processing interval: %llums"
+ "+ First-unlock check interval: %llums"
+ "+ Flow Engine initialization interval: %llums"
+ "+ Launch sequence dispatch interval: %llums"
+ "+ Launchpad initialization interval: %llums"
+ "+ NOIEngine initialization interval: %llums"
+ "+ Network Engine initialization interval: %llums"
+ "+ Persistence initialization interval: %llums"
+ "+ Total Launch sequence (first unlock) interval: %llums"
+ "+ Total Launch sequence (unlocked) interval: %llums"
+ "+ Total Prelaunch sequence interval: %llums"
+ "+ Workspace initialization interval: %llums"
+ "+ XPC checkpoint dispatch interval: %llums"
+ "+ XPCListener initialization interval: %llums"
+ "3rd Party obfuscated Drop reported to analytics for %{private}@ cause %lu detail %{private}@"
+ "<NWL2Report:\n\tCellular LQM:\t\t\t%d\n\tCellular Known Good:\t\t%s\n\tCellular Radio Technology:\t%d\n\tCellular MNC:\t\t\t%d\n\tCellular MCC:\t\t\t%d\n\tCellular UARFCN:\t\t%d\n\tCellular PID:\t\t\t%d\n\tCellular Band Info:\t\t%d\n\tCellular Cell Type:\t\t%@\n\tCellular Bandwidth:\t\t%d\n\tCellular TAC:\t\t\t%d\n\tCellular Bars:\t\t\t%d\n\tCellular RSRP:\t\t\t%d\n\tCellular SNR:\t\t\t%f\n\tCellular Slice Active:\t%s\n\tCellular Band:\t\t\t%u\n\tCellular Mode:\t\t%u\n\tCellular Dual SIM Status:\t%d\n\tCellular Secondary MNC:\t\t%d\n\tCellular Secondary MCC:\t\t%d\n\tCellular Outranks Wi-Fi:\t\t%d\n\tCellular Outrank Primary Reason:\t\t%d\n\tCellular Outrank Reason Flags:\t\t%llu\n\tWi-Fi LQM:\t\t\t%d\n\tWi-Fi RSSI:\t\t\t%d\n\tWi-Fi Known Good:\t\t%s\n\tWi-Fi Radio Technology:\t\t%d\n\tWi-Fi Is Hotspot:\t\t%s\n\tWi-Fi Is Apple Personal Hotspot:\t\t%s\n\tInterface Queue Stats:\t\t%@\n>"
+ "== LaunchSequence Event Timeline =="
+ "== Prelaunch Event Timeline =="
+ "> getMeasurement : _launchSequenceActivityMeasurements is NULL"
+ "> getMeasurement : _prelaunchActivityMeasurements is NULL"
+ "> setMeasurement : _launchSequenceActivityMeasurements is NULL %p"
+ "> setMeasurement : _prelaunchActivityMeasurements is NULL %p"
+ "@\"CAUsageDeltaTracker\""
+ "@\"CellFallbackMetric\""
+ "@32@0:8C16i20Q24"
+ "@40@0:8q16Q24@32"
+ "Allocated storage %p"
+ "Allocating FlowAnalyticsEngine"
+ "Allocating NOIAnalyticsEngine"
+ "Allocating NetworkAnalyticsEngine"
+ "Allocating measurements storage for LaunchSequence"
+ "Allocating measurements storage for PrelaunchSequence"
+ "AnalyticsLaunchPadInitialize"
+ "AnalyticsPortalInitializeXPC"
+ "B28@0:8i16@20"
+ "CAUsageDeltaTracker"
+ "CFSM Metric: About to post %{private}@ to CA"
+ "CFSM TriggerDisconnect logs, record dispose: %p, failed to post to CA"
+ "CFSM TriggerDisconnect logs, record dispose: %p, final balance: %llu, flow count: %llu, will post to CA"
+ "CFSM TriggerDisconnect logs, record dispose: %p, successfully posted to CA"
+ "CTShim: connectionStateChanged, context slotID (%ld) does not match with currentSubscriberSlotID (%ld)"
+ "CellFallbackMetric"
+ "Data Usage for %@%@ on flow %llu - WiFi in/out: %@/%@, WiFi delta_in/delta_out: %lld/%lld, Cell in/out: %@/%@, Cell delta_in/delta_out: %lld/%lld, RNF: %d, subscriber tag: %@"
+ "Deallocating measurements storage for LaunchSequence"
+ "Deallocating measurements storage for PrelaunchSequence"
+ "Delivering new network slicing active value to delegates"
+ "DispatchLaunchSequence_Interval"
+ "DispatchXPCCheckpoint_Interval"
+ "First unlock processing complete - semaphore released"
+ "First unlock processing interval: %llums"
+ "First-unlock check: %llums"
+ "FirstUnlockCheck"
+ "FirstUnlockCheck_Interval"
+ "FirstUnlockNotification"
+ "Flow Engine initialization interval: %llums"
+ "FlowAnalyticsEngine completed initialization"
+ "FlowAnalyticsEngineAllocated"
+ "FlowAnalyticsEngineInitialized"
+ "Immediately after allocating the first workspace"
+ "Immediately after called into configureInstance"
+ "Immediately after called into launchSequence"
+ "Immediately after called into main"
+ "Immediately after called into setListeningPort:%s queue:%s"
+ "Immediately after completing persistence initialization and health checks"
+ "Immediately before allocating the first workspace"
+ "Immediately before calling MKBDeviceUnlockedSinceBoot()"
+ "Immediately before performing persistence initialization"
+ "InitializeFlowEngine_Interval"
+ "InitializeNOIEngine_Interval"
+ "InitializeNetworkEngine_Interval"
+ "InitializePersistence_Interval"
+ "InitializeWorkspace_Interval"
+ "Initialized _networkSlicingStates to %@"
+ "IsFirstUnlock"
+ "IsFirstUnlock: %{BOOL}d"
+ "KQWORKLOOP_EXHAUSTION"
+ "Launch sequence complete, ready to signal XPC checkpoint semaphore"
+ "Launch sequence complete, ready to signal XPC checkpoint semaphore enableTelemetry=YES "
+ "Launch sequence dispatch interval: %llums"
+ "LaunchSequenceDict: %@"
+ "LaunchSequenceInterval"
+ "LaunchSequenceStart"
+ "Launchpad initialization: %llums"
+ "LaunchpadInitialization_Interval"
+ "LightWeightTimer with scale factor %f timer expiry slot %lld index %lld current slot %lld bitmask 0x%llx\n"
+ "Measurements storage for LaunchSequence already allocated"
+ "Measurements storage for PrelaunchSequence already allocated"
+ "NOIAnalyticsEngine completed initialization"
+ "NOIAnalyticsEngineAllocated"
+ "NOIAnalyticsEngineInitialized"
+ "NOIEngine initialization interval: %llums"
+ "Network Engine initialization interval: %llums"
+ "Network slicing states changed to %@"
+ "NetworkAnalyticsEngine completed initialization"
+ "NetworkAnalyticsEngineAllocated"
+ "NetworkAnalyticsEngineInitialized"
+ "No LaunchSequence measurements available to submit to CoreAnalytics"
+ "No PrelaunchSequence measurements available to submit to CoreAnalytics"
+ "Persistence initialization interval: %llums"
+ "PersistenceInitializationBegin"
+ "PersistenceInitializationEnd"
+ "Populating CoreAnalytics metrics for LaunchSequence measurements"
+ "Populating CoreAnalytics metrics for PrelaunchSequence measurements"
+ "Prelaunch sequence complete, ready to call MKBDeviceUnlockedSinceBoot()"
+ "PrelaunchSequenceDict: %@"
+ "PrelaunchSequenceInterval"
+ "ProcessLaunch"
+ "ProcessedFirstUnlock_Interval"
+ "Ready to submit CoreAnalytics metrics for LaunchSequence measurements"
+ "Ready to submit CoreAnalytics metrics for PrelaunchSequence measurements"
+ "Received %skqworkloops exhaustion trigger:\n  %s[%d] allocated %lld kqworkloops violating a limit of %lld kqworkloops"
+ "Received a callback for connection state change. Connection %d active: %{BOOL}d"
+ "Received com.apple.mobile.keybagd.first_unlock notification"
+ "Received network slicing active changed notification, new status for slice %lu: %{BOOL}d"
+ "Received request to change network slicing state at invalid index %lu"
+ "ResourceNotifyTriggerKQWorkloopsExhaustion"
+ "SYMPTOM_FLOW_COUNT_NOT_MONOTONIC"
+ "T@\"CellFallbackMetric\",&,N,V_caMetric"
+ "T@\"NSArray\",R"
+ "T@\"NSString\",?,R,C"
+ "TB,N,V_cellularSliceActive"
+ "TC,N,V_egressTriggerInterfaceType"
+ "TC,N,V_ingressTriggerInterfaceType"
+ "TI,N,V_egressMotionState"
+ "TI,N,V_egressTrigger"
+ "TI,N,V_ingressMotionState"
+ "TI,N,V_ingressTrigger"
+ "Td,N,V_adviceHeldForSecs"
+ "Total launch sequence (first unlock) interval: %llums"
+ "Total launch sequence (unlocked) interval: %llums"
+ "Total prelaunch sequence (first unlock) interval: %llums"
+ "Total prelaunch sequence (unlocked) interval: %llums"
+ "TotalLaunchToXPC_Interval"
+ "TotalPrelaunchToUnlockCheck_Interval"
+ "Unlock check complete - device already unlocked"
+ "UnlockCheckComplete"
+ "Updating networkSlicingStates after delegate registration"
+ "Workspace initialization interval: %llums"
+ "WorkspaceInitializeBegin"
+ "WorkspaceInitializeEnd"
+ "XPC checkpoint dispatch interval: %llums"
+ "XPC checkpoint released, ready for servicing"
+ "XPCCheckpointReady"
+ "XPCListener initialization: %llums"
+ "XPCListenerInitialization_Interval"
+ "[Bitmap] flow id %llu, %@: current bitmaps stored after adding new bitmap: %@"
+ "[Bitmap] flow id %llu, %@: current bitmaps stored before adding new bitmap: %@"
+ "[Bitmap] flow id %llu, %@: the activity bitmap to add with start time %llu is smaller than existing startTime %llu."
+ "[Bitmap] flow id %llu, %@: the activity bitmap to add with start time %llu will replace all previous bitmaps with startTime %llu"
+ "_caMetric"
+ "_cellularSliceActive"
+ "_deliverNetworkSlicingActiveChangedTo:forSliceIndex:"
+ "_egressMotionState"
+ "_egressTriggerInterfaceType"
+ "_flowCount"
+ "_ingressMotionState"
+ "_ingressTriggerInterfaceType"
+ "_interestingTrigger"
+ "_lastValue"
+ "_launchSequenceActivityMeasurements : %p"
+ "_netType"
+ "_networkSlicingStates"
+ "_prelaunchActivityMeasurements : %p"
+ "_rootCause"
+ "_startValue"
+ "_thinCopy"
+ "a_l2Report_cellularSliceActive"
+ "allocateMeasurementType : %d"
+ "analyticsDictionaryForLaunchSequence : _launchSequenceActivityMeasurements:%p baseline:%llu"
+ "analyticsDictionaryForPrelaunchSequence : _prelaunchActivityMeasurements:%p baseline:%llu"
+ "baseline is zero: %llu"
+ "caMetric"
+ "cellularSliceActive"
+ "com.apple.apr.3pp"
+ "com.apple.symptoms.WiFiAssist.StateTransition"
+ "com.apple.symptoms.WiFiAssist.TriggerDisconnect"
+ "com.apple.symptoms.measurements.LaunchSequenceEvents"
+ "com.apple.symptoms.measurements.PrelaunchEvents"
+ "com.apple.symptoms.resource_notify.kqworkloops_exhaustion_trigger"
+ "destroyMeasurementType: %d"
+ "durationInState"
+ "e_l2Report_cellularSliceActive"
+ "egressMotionState"
+ "egressTriggerInterfaceType"
+ "getConnectionState failed error: %@, context: %{private}@"
+ "getConnectionState:connectionType:error:"
+ "getConnectionType for type %d, isActive: %{BOOL}d"
+ "getConnectionType:activeForContext:"
+ "getMeasurement : type:%d event:%d"
+ "getNetworkSlicingStates"
+ "ingressMotionState"
+ "ingressTriggerInterfaceType"
+ "initCellFallbackMetricWithLevel:policy:state:"
+ "initWithSet:copyItems:"
+ "initializeActivityMeasurements"
+ "interestingIngressTrigger"
+ "isSubFlow"
+ "kqworkloop Exhaustion"
+ "measure.launch_xpc"
+ "networkSlicingActiveChangedTo:forSliceIndex:"
+ "networkSlicingStates"
+ "numberOfImpactedFlows"
+ "pcapbuffersize"
+ "populateCellFallbackPropertiesOnCAMetric:"
+ "postMetric"
+ "sendNetworkSlicingStatesToDelegate"
+ "setCaMetric:"
+ "setCellularSliceActive:"
+ "setEgressMotionState:"
+ "setEgressTriggerInterfaceType:"
+ "setIngressMotionState:"
+ "setIngressTriggerInterfaceType:"
+ "setMeasurement : type:%d event:%d value:%llu"
+ "setNetworkSlicingStateAtIndex:to:"
+ "skip typical flow processing for subflow %lld"
+ "state %@ advice %ld durationInState %.2f policy %lu motionState (%d/%d) previousState %d trigger (%u/%u) triggerInterfaceType (%d/%d) wifiIngressTriggers %@ interestingTrigger %u"
+ "v28@0:8B16Q20"
+ "v28@0:8Q16B24"
+ "v32@?0@\"AppTracker\"8Q16^B24"
- "\b\x11\x12\x11q\x14\x11'\x11#"
- "%#016llx "
- "%p (voided)"
- "<NWL2Report:\n\tCellular LQM:\t\t\t%d\n\tCellular Known Good:\t\t%s\n\tCellular Radio Technology:\t%d\n\tCellular MNC:\t\t\t%d\n\tCellular MCC:\t\t\t%d\n\tCellular UARFCN:\t\t%d\n\tCellular PID:\t\t\t%d\n\tCellular Band Info:\t\t%d\n\tCellular Cell Type:\t\t%@\n\tCellular Bandwidth:\t\t%d\n\tCellular TAC:\t\t\t%d\n\tCellular Bars:\t\t\t%d\n\tCellular RSRP:\t\t\t%d\n\tCellular SNR:\t\t\t%f\n\tCellular Band:\t\t\t%u\n\tCellular Mode:\t\t%u\n\tCellular Dual SIM Status:\t%d\n\tCellular Secondary MNC:\t\t%d\n\tCellular Secondary MCC:\t\t%d\n\tCellular Outranks Wi-Fi:\t\t%d\n\tCellular Outrank Primary Reason:\t\t%d\n\tCellular Outrank Reason Flags:\t\t%llu\n\tWi-Fi LQM:\t\t\t%d\n\tWi-Fi RSSI:\t\t\t%d\n\tWi-Fi Known Good:\t\t%s\n\tWi-Fi Radio Technology:\t\t%d\n\tWi-Fi Is Hotspot:\t\t%s\n\tWi-Fi Is Apple Personal Hotspot:\t\t%s\n\tInterface Queue Stats:\t\t%@\n>"
- "@\"AWDUsageDeltaTracker\""
- "@32@0:8i16i20Q24"
- "@36@0:8i16I20i24@28"
- "AWDUsageDeltaTracker"
- "ApparentTimeHandler dispatchAfterDelay delegate %p"
- "CFSM TriggerDisconnect logs, record dispose: %p, final balance: %llu, flow count: %llu, will post to AWD"
- "Data Usage for %@ on flow %llu - WiFi in/out: %@/%@, WiFi delta_in/delta_out: %lld/%lld, Cell in/out: %@/%@, Cell delta_in/delta_out: %lld/%lld, RNF: %d, subscriber tag: %@"
- "LightWeightTimer with scale factor %f timer expiry slot %lld index %lld current slot %lld bitmap 0x%llx\n"
- "[Bitmap] flow %llu, %@: adding bitmap part1: %#016llx, part2: %#016llx, startTime %llu, interface %u"
- "[Bitmap] flow %llu, %@: current bitmaps stored after adding new bitmap: %@"
- "[Bitmap] flow %llu, %@: current bitmaps stored before adding new bitmap: %@"
- "[Bitmap] flow %llu, %@: the activity bitmap to add with start time %llu is smaller than existing startTime %llu."
- "[Bitmap] flow %llu, %@: the activity bitmap to add with start time %llu will replace all previous bitmaps with startTime %llu"
- "[Bitmap] polling complete, success %d"
- "[Bitmap] polling start"
- "_motionToAwdCode"
- "_processSymptomsdMbufPeak:symptomName:"
- "a\x13"
- "awdAgent"
- "awdWifiAssistPolicyForRNFPolicy:"
- "createAndInitializeAWDMetricForStateWithLevel:activationIdentifier:policy:andSignature:"
- "flowCount"
- "kernel"
- "lastValue"
- "launchSequence"
- "malloc failed to create a new journal record of type %d"
- "netType"
- "startValue"

```
