## SymptomEvaluator

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator`

```diff

-2144.0.0.0.0
-  __TEXT.__text: 0x278c78
-  __TEXT.__auth_stubs: 0x2c70
-  __TEXT.__objc_methlist: 0x17748
-  __TEXT.__cstring: 0x25146
-  __TEXT.__const: 0xec0
-  __TEXT.__oslogstring: 0x42eef
+2150.0.0.502.1
+  __TEXT.__text: 0x2791fc
+  __TEXT.__auth_stubs: 0x2c80
+  __TEXT.__objc_methlist: 0x17768
+  __TEXT.__cstring: 0x25156
+  __TEXT.__const: 0xed8
+  __TEXT.__oslogstring: 0x42eff
   __TEXT.__gcc_except_tab: 0x53a0
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__swift5_typeref: 0x304
-  __TEXT.__swift5_capture: 0x33c
+  __TEXT.__swift5_capture: 0x37c
   __TEXT.__constg_swiftt: 0xe8
   __TEXT.__swift5_reflstr: 0x105
   __TEXT.__swift5_fieldmd: 0xd0
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_mpenum: 0x20
   __TEXT.__swift5_types: 0x10
-  __TEXT.__swift_as_entry: 0x38
-  __TEXT.__swift_as_ret: 0x5c
+  __TEXT.__swift_as_entry: 0x3c
+  __TEXT.__swift_as_ret: 0x60
   __TEXT.evaluator_cfg: 0x647c
   __TEXT.default_clp: 0x2fe0
   __TEXT.symptoms_clp: 0x5f90

   __TEXT.bb_MAV_clp: 0x89e0
   __TEXT.bb_INT_clp: 0x6930
   __TEXT.modules_clp: 0x16e0
-  __TEXT.__unwind_info: 0x69f8
-  __TEXT.__eh_frame: 0x670
+  __TEXT.__unwind_info: 0x6a18
+  __TEXT.__eh_frame: 0x698
   __TEXT.__objc_classname: 0x1d5b
-  __TEXT.__objc_methname: 0x3c67a
-  __TEXT.__objc_methtype: 0x6c58
-  __TEXT.__objc_stubs: 0x25980
-  __DATA_CONST.__got: 0xf80
-  __DATA_CONST.__const: 0x66e8
+  __TEXT.__objc_methname: 0x3c6bf
+  __TEXT.__objc_methtype: 0x6c5b
+  __TEXT.__objc_stubs: 0x259a0
+  __DATA_CONST.__got: 0xf88
+  __DATA_CONST.__const: 0x66f0
   __DATA_CONST.__objc_classlist: 0x860
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xca48
+  __DATA_CONST.__objc_selrefs: 0xca50
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x588
   __DATA_CONST.__objc_arraydata: 0x850
-  __AUTH_CONST.__auth_got: 0x1650
-  __AUTH_CONST.__const: 0x2b98
-  __AUTH_CONST.__cfstring: 0x1cea0
-  __AUTH_CONST.__objc_const: 0x3c0c0
+  __AUTH_CONST.__auth_got: 0x1658
+  __AUTH_CONST.__const: 0x2c10
+  __AUTH_CONST.__cfstring: 0x1cec0
+  __AUTH_CONST.__objc_const: 0x3c108
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x910
   __AUTH_CONST.__objc_intobj: 0x798

   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH.__objc_data: 0x15b0
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x2d34
+  __DATA.__objc_ivar: 0x2d38
   __DATA.__data: 0x1dc0
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0xff0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: E85D587B-167F-3FC0-B822-439B5775364D
-  Functions: 11291
-  Symbols:   36444
-  CStrings:  26567
+  UUID: D2B02FCC-D626-38A6-BD40-F85B3610DF6C
+  Functions: 11301
+  Symbols:   36453
+  CStrings:  26572
 
Symbols:
+ -[ServiceImpl cleanupNDFDeviceRecordsWithReply:]
+ -[TCPProgressProbe fetchMetricsForFlowsAged:metrics:includeQUICFlows:resultBlock:]
+ _OBJC_IVAR_$_CellFallbackHandler.wifiEpochObserver
+ ___113-[NetworkAnalyticsEngine performQueryOnEntity:fetchRequestProperties:pred:sort:actions:service:connection:reply:]_block_invoke.815
+ ___114-[ProxyAnalytics donateBiomeEventForEdgeSelectionWithPrefix:interfaceType:radioType:radioBand:latitude:longitude:]_block_invoke.84
+ ___23-[ServiceImpl shutdown]_block_invoke.220
+ ___27-[CellFallbackHandler init]_block_invoke.217
+ ___27-[CellFallbackHandler init]_block_invoke.225
+ ___27-[CellFallbackHandler init]_block_invoke.229
+ ___27-[CellFallbackHandler init]_block_invoke_2.218
+ ___27-[CellFallbackHandler init]_block_invoke_2.230
+ ___27-[CellFallbackHandler init]_block_invoke_3.219
+ ___27-[CellFallbackHandler init]_block_invoke_4
+ ___33-[CellFallbackHandler _dumpState]_block_invoke.369
+ ___37-[ServiceImpl abortRNFTestWithReply:]_block_invoke.217
+ ___40-[CellFallbackHandler _peekIntoCellPlan]_block_invoke.406
+ ___40-[ServiceImpl clientTransactionsRelease]_block_invoke.219
+ ___40-[ServiceImpl getOption:inScopes:reply:]_block_invoke.200
+ ___40-[ServiceImpl setOption:inScopes:reply:]_block_invoke.196
+ ___40-[ServiceImpl setOption:inScopes:reply:]_block_invoke.198
+ ___43-[NetworkAnalyticsEngine _armDOASuspector:]_block_invoke.763
+ ___45-[NetworkAnalyticsEngine _processCTCellInfo:]_block_invoke.329
+ ___46-[CellFallbackHandler _completeInitialization]_block_invoke.254
+ ___46-[CellFallbackHandler _completeInitialization]_block_invoke.257
+ ___46-[CellFallbackHandler _completeInitialization]_block_invoke.259
+ ___46-[CellFallbackHandler _completeInitialization]_block_invoke.262
+ ___46-[CellFallbackHandler _completeInitialization]_block_invoke.265
+ ___46-[CellFallbackHandler _completeInitialization]_block_invoke.269
+ ___46-[CellFallbackHandler _completeInitialization]_block_invoke_2.271
+ ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke.405
+ ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke.417
+ ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke.424
+ ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke.434
+ ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke.442
+ ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke.447
+ ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke.449
+ ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke.453
+ ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke_2.425
+ ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke_2.435
+ ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke_2.451
+ ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke_3.426
+ ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke_3.437
+ ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke_4.427
+ ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke_5.428
+ ___47-[CellFallbackHandler _updateCellFallbackState]_block_invoke.502
+ ___47-[CellFallbackHandler _updateCellFallbackState]_block_invoke.507
+ ___48-[ServiceImpl initWithQueue:noiEngine:isHelper:]_block_invoke.178
+ ___48-[ServiceImpl initWithQueue:noiEngine:isHelper:]_block_invoke.180
+ ___48-[ServiceImpl initWithQueue:noiEngine:isHelper:]_block_invoke.182
+ ___48-[ServiceImpl initWithQueue:noiEngine:isHelper:]_block_invoke_2.183
+ ___49-[ServiceImpl waitForOSLogErrorSymptomWithReply:]_block_invoke.221
+ ___51-[NetworkAnalyticsEngine _idleExitTransactionCheck]_block_invoke.762
+ ___51-[ProxyAnalytics performPersistentStoreHealthCheck]_block_invoke.104
+ ___51-[ProxyAnalytics trainModelAndScore:lastScoreDate:]_block_invoke.76
+ ___52-[CellFallbackHandler _canUseApps:replyQueue:reply:]_block_invoke.489
+ ___52-[CellFallbackHandler _canUseApps:replyQueue:reply:]_block_invoke.491
+ ___52-[ServiceImpl createSnapshotFor:pred:actions:reply:]_block_invoke.195
+ ___53-[NetworkAnalyticsEngine didReceiveProtocolSnapshot:]_block_invoke.550
+ ___54-[NetworkAnalyticsEngine _armFatalSuspector:isActive:]_block_invoke.772
+ ___54-[NetworkAnalyticsEngine _armFatalSuspector:isActive:]_block_invoke.773
+ ___54-[ServiceImpl getPreferCellOverWiFiWithOptions:reply:]_block_invoke.225
+ ___54-[ServiceImpl setPreferCellOverWiFiWithOptions:reply:]_block_invoke.226
+ ___55-[NetworkAnalyticsEngine _layer2MetricsOn:queue:reply:]_block_invoke.822
+ ___55-[NetworkAnalyticsEngine _layer2MetricsOn:queue:reply:]_block_invoke.823
+ ___57-[NetworkAnalyticsEngine _awdCaptureIn:replyQueue:reply:]_block_invoke.925
+ ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.389
+ ___58-[ServiceImpl startRNFTestWithOptions:scenarioName:reply:]_block_invoke.214
+ ___61-[NetworkAnalyticsEngine _performNetAttachmentQueryOn:reply:]_block_invoke.819
+ ___61-[NetworkAnalyticsEngine wifiShim_L2NewMetrics:forInterface:]_block_invoke.595
+ ___62-[NetworkAnalyticsEngine _awdCaptureInstant:replyQueue:reply:]_block_invoke.922
+ ___63-[NetworkAnalyticsEngine _getAuditableLoadedLQMOn:queue:reply:]_block_invoke.281
+ ___66-[NetworkAnalyticsEngine _registerForSIMStatusChangeNotification:]_block_invoke.461
+ ___70-[CellFallbackHandler generateInfoForId:context:uuid:completionBlock:]_block_invoke.566
+ ___70-[CellFallbackHandler observeValueForKeyPath:ofObject:change:context:]_block_invoke.384
+ ___70-[CellFallbackHandler observeValueForKeyPath:ofObject:change:context:]_block_invoke.387
+ ___74-[CellFallbackHandler _trackCellUsageAfterTriggerDisconnectWithNewSeries:]_block_invoke.515
+ ___76-[NetworkAnalyticsEngine _usageToLOICorrelationFor:scopedToLOI:queue:reply:]_block_invoke.833
+ ___78-[NetworkAnalyticsEngine _estimatedTransferTimeOn:forPayloadInfo:queue:reply:]_block_invoke.824
+ ___78-[NetworkAnalyticsEngine _estimatedTransferTimeOn:forPayloadInfo:queue:reply:]_block_invoke_2.825
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.689
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.699
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.703
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.710
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.718
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.734
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.738
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke_2.725
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke_2.739
+ ___83-[ServiceImpl performQueryOnEntity:fetchRequestProperties:pred:sort:actions:reply:]_block_invoke.194
+ ___92-[CellFallbackHandler _idempotentInitializationFromIdleWithCellRelay:wifiRelay:motionRelay:]_block_invoke.298
+ ___92-[CellFallbackHandler _idempotentInitializationFromIdleWithCellRelay:wifiRelay:motionRelay:]_block_invoke.300
+ ___92-[CellFallbackHandler _idempotentInitializationFromIdleWithCellRelay:wifiRelay:motionRelay:]_block_invoke.307
+ ___block_literal_global.154
+ ___block_literal_global.169
+ ___block_literal_global.205
+ ___block_literal_global.213
+ ___block_literal_global.216
+ ___block_literal_global.309
+ ___block_literal_global.351
+ ___block_literal_global.360
+ ___block_literal_global.372
+ ___block_literal_global.383
+ ___block_literal_global.419
+ ___block_literal_global.423
+ ___block_literal_global.458
+ ___block_literal_global.460
+ ___block_literal_global.498
+ ___block_literal_global.630
+ ___block_literal_global.727
+ ___block_literal_global.814
+ ___block_literal_global.821
+ ___block_literal_global.88
+ ___block_literal_global.915
+ ___block_literal_global.92
+ ___block_literal_global.96
+ ___cell_server_connection_callback_block_invoke.175
+ ___cell_server_connection_callback_block_invoke.177
+ ___cell_server_connection_callback_block_invoke.183
+ ___config_callback_block_invoke.206
+ ___config_callback_block_invoke.207
+ ___config_callback_block_invoke.208
+ _kNotificationRoaming
+ _objc_msgSend$cleanupNDFDeviceRecordsWithReply:
+ _objc_msgSend$fetchMetricsForFlowsAged:metrics:includeQUICFlows:resultBlock:
+ _objectdestroy.150Tm
+ _objectdestroy.27Tm
+ _objectdestroy.35Tm
- -[TCPProgressProbe fetchMetricsForFlowsAged:metrics:resultBlock:]
- GCC_except_table121
- ___113-[NetworkAnalyticsEngine performQueryOnEntity:fetchRequestProperties:pred:sort:actions:service:connection:reply:]_block_invoke.812
- ___114-[ProxyAnalytics donateBiomeEventForEdgeSelectionWithPrefix:interfaceType:radioType:radioBand:latitude:longitude:]_block_invoke.83
- ___23-[ServiceImpl shutdown]_block_invoke.219
- ___27-[CellFallbackHandler init]_block_invoke.222
- ___27-[CellFallbackHandler init]_block_invoke.228
- ___27-[CellFallbackHandler init]_block_invoke_2.217
- ___27-[CellFallbackHandler init]_block_invoke_2.229
- ___27-[CellFallbackHandler init]_block_invoke_3.218
- ___33-[CellFallbackHandler _dumpState]_block_invoke.368
- ___37-[ServiceImpl abortRNFTestWithReply:]_block_invoke.216
- ___40-[CellFallbackHandler _peekIntoCellPlan]_block_invoke.404
- ___40-[ServiceImpl clientTransactionsRelease]_block_invoke.218
- ___40-[ServiceImpl getOption:inScopes:reply:]_block_invoke.198
- ___40-[ServiceImpl setOption:inScopes:reply:]_block_invoke.195
- ___40-[ServiceImpl setOption:inScopes:reply:]_block_invoke.197
- ___43-[NetworkAnalyticsEngine _armDOASuspector:]_block_invoke.760
- ___45-[NetworkAnalyticsEngine _processCTCellInfo:]_block_invoke.326
- ___46-[CellFallbackHandler _completeInitialization]_block_invoke.253
- ___46-[CellFallbackHandler _completeInitialization]_block_invoke.256
- ___46-[CellFallbackHandler _completeInitialization]_block_invoke.258
- ___46-[CellFallbackHandler _completeInitialization]_block_invoke.260
- ___46-[CellFallbackHandler _completeInitialization]_block_invoke.263
- ___46-[CellFallbackHandler _completeInitialization]_block_invoke.266
- ___46-[CellFallbackHandler _completeInitialization]_block_invoke_2.270
- ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke.402
- ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke.414
- ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke.421
- ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke.431
- ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke.439
- ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke.444
- ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke.446
- ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke.450
- ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke_2.422
- ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke_2.432
- ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke_2.448
- ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke_3.423
- ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke_3.434
- ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke_4.424
- ___46-[NetworkAnalyticsEngine _initializeInternals]_block_invoke_5.425
- ___47-[CellFallbackHandler _updateCellFallbackState]_block_invoke.501
- ___47-[CellFallbackHandler _updateCellFallbackState]_block_invoke.506
- ___48-[ServiceImpl initWithQueue:noiEngine:isHelper:]_block_invoke.177
- ___48-[ServiceImpl initWithQueue:noiEngine:isHelper:]_block_invoke.179
- ___48-[ServiceImpl initWithQueue:noiEngine:isHelper:]_block_invoke.181
- ___48-[ServiceImpl initWithQueue:noiEngine:isHelper:]_block_invoke_2.182
- ___49-[ServiceImpl waitForOSLogErrorSymptomWithReply:]_block_invoke.220
- ___51-[NetworkAnalyticsEngine _idleExitTransactionCheck]_block_invoke.759
- ___51-[ProxyAnalytics performPersistentStoreHealthCheck]_block_invoke.103
- ___51-[ProxyAnalytics trainModelAndScore:lastScoreDate:]_block_invoke.75
- ___52-[CellFallbackHandler _canUseApps:replyQueue:reply:]_block_invoke.488
- ___52-[CellFallbackHandler _canUseApps:replyQueue:reply:]_block_invoke.490
- ___52-[ServiceImpl createSnapshotFor:pred:actions:reply:]_block_invoke.194
- ___53-[NetworkAnalyticsEngine didReceiveProtocolSnapshot:]_block_invoke.547
- ___54-[NetworkAnalyticsEngine _armFatalSuspector:isActive:]_block_invoke.769
- ___54-[NetworkAnalyticsEngine _armFatalSuspector:isActive:]_block_invoke.770
- ___54-[ServiceImpl getPreferCellOverWiFiWithOptions:reply:]_block_invoke.224
- ___54-[ServiceImpl setPreferCellOverWiFiWithOptions:reply:]_block_invoke.225
- ___55-[NetworkAnalyticsEngine _layer2MetricsOn:queue:reply:]_block_invoke.819
- ___55-[NetworkAnalyticsEngine _layer2MetricsOn:queue:reply:]_block_invoke.820
- ___57-[NetworkAnalyticsEngine _awdCaptureIn:replyQueue:reply:]_block_invoke.922
- ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.386
- ___58-[ServiceImpl startRNFTestWithOptions:scenarioName:reply:]_block_invoke.213
- ___61-[NetworkAnalyticsEngine _performNetAttachmentQueryOn:reply:]_block_invoke.816
- ___61-[NetworkAnalyticsEngine wifiShim_L2NewMetrics:forInterface:]_block_invoke.592
- ___62-[NetworkAnalyticsEngine _awdCaptureInstant:replyQueue:reply:]_block_invoke.919
- ___63-[NetworkAnalyticsEngine _getAuditableLoadedLQMOn:queue:reply:]_block_invoke.278
- ___66-[NetworkAnalyticsEngine _registerForSIMStatusChangeNotification:]_block_invoke.458
- ___70-[CellFallbackHandler generateInfoForId:context:uuid:completionBlock:]_block_invoke.565
- ___70-[CellFallbackHandler observeValueForKeyPath:ofObject:change:context:]_block_invoke.383
- ___70-[CellFallbackHandler observeValueForKeyPath:ofObject:change:context:]_block_invoke.385
- ___74-[CellFallbackHandler _trackCellUsageAfterTriggerDisconnectWithNewSeries:]_block_invoke.514
- ___76-[NetworkAnalyticsEngine _usageToLOICorrelationFor:scopedToLOI:queue:reply:]_block_invoke.830
- ___78-[NetworkAnalyticsEngine _estimatedTransferTimeOn:forPayloadInfo:queue:reply:]_block_invoke.821
- ___78-[NetworkAnalyticsEngine _estimatedTransferTimeOn:forPayloadInfo:queue:reply:]_block_invoke_2.822
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.686
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.696
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.700
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.707
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.715
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.731
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.735
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke_2.722
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke_2.736
- ___83-[ServiceImpl performQueryOnEntity:fetchRequestProperties:pred:sort:actions:reply:]_block_invoke.193
- ___92-[CellFallbackHandler _idempotentInitializationFromIdleWithCellRelay:wifiRelay:motionRelay:]_block_invoke.296
- ___92-[CellFallbackHandler _idempotentInitializationFromIdleWithCellRelay:wifiRelay:motionRelay:]_block_invoke.299
- ___92-[CellFallbackHandler _idempotentInitializationFromIdleWithCellRelay:wifiRelay:motionRelay:]_block_invoke.301
- ___block_literal_global.204
- ___block_literal_global.212
- ___block_literal_global.215
- ___block_literal_global.308
- ___block_literal_global.348
- ___block_literal_global.359
- ___block_literal_global.371
- ___block_literal_global.382
- ___block_literal_global.400
- ___block_literal_global.416
- ___block_literal_global.420
- ___block_literal_global.452
- ___block_literal_global.457
- ___block_literal_global.497
- ___block_literal_global.627
- ___block_literal_global.724
- ___block_literal_global.811
- ___block_literal_global.82
- ___block_literal_global.87
- ___block_literal_global.91
- ___block_literal_global.912
- ___block_literal_global.95
- ___cell_server_connection_callback_block_invoke.172
- ___cell_server_connection_callback_block_invoke.174
- ___cell_server_connection_callback_block_invoke.180
- ___config_callback_block_invoke.202
- ___config_callback_block_invoke.203
- ___config_callback_block_invoke.204
- _objc_msgSend$fetchMetricsForFlowsAged:metrics:resultBlock:
- _objectdestroy.137Tm
- _objectdestroy.15Tm
- _objectdestroy.31Tm
CStrings:
+ "(en|pdp_ip|ipsec|utun)[^/]+"
+ "CFSM WiFi roaming event"
+ "Roaming"
+ "cleanupNDFDeviceRecordsWithReply:"
+ "fetchMetricsForFlowsAged:metrics:includeQUICFlows:resultBlock:"
+ "v44@0:8d16^{nstat_progress_indicators=IIIIIIQQQQQQQQQ}24B32@?36"
+ "wifiEpochObserver"
- "(en|pdp_ip|ipsec)[^/]+"
- "fetchMetricsForFlowsAged:metrics:resultBlock:"
- "v40@0:8d16^{nstat_progress_indicators=IIIIIIQQQQQQQQQ}24@?32"

```
