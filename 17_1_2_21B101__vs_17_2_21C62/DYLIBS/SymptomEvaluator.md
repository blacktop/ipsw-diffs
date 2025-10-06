## SymptomEvaluator

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator`

```diff

-1848.42.1.0.0
-  __TEXT.__text: 0x24d774
-  __TEXT.__auth_stubs: 0x2600
-  __TEXT.__objc_methlist: 0x1649c
-  __TEXT.__cstring: 0x227c8
-  __TEXT.__oslogstring: 0x3c046
+1848.60.8.0.0
+  __TEXT.__text: 0x24e2b4
+  __TEXT.__auth_stubs: 0x2610
+  __TEXT.__objc_methlist: 0x1658c
+  __TEXT.__cstring: 0x229f6
+  __TEXT.__oslogstring: 0x3c230
   __TEXT.__const: 0x738
-  __TEXT.__gcc_except_tab: 0x32ac
+  __TEXT.__gcc_except_tab: 0x3308
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.evaluator_cfg: 0x5f7a
   __TEXT.default_clp: 0x2fe0

   __TEXT.baseband_clp: 0xe950
   __TEXT.bb_MAV_clp: 0xaa40
   __TEXT.modules_clp: 0x1230
-  __TEXT.__unwind_info: 0x64cc
+  __TEXT.__unwind_info: 0x6510
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x1c9b
-  __TEXT.__objc_methname: 0x3b628
+  __TEXT.__objc_methname: 0x3b86c
   __TEXT.__objc_methtype: 0x68a4
-  __TEXT.__objc_stubs: 0x24d20
+  __TEXT.__objc_stubs: 0x24f00
   __DATA_CONST.__got: 0x6a8
-  __DATA_CONST.__const: 0x61a0
+  __DATA_CONST.__const: 0x61c8
   __DATA_CONST.__objc_classlist: 0x850
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x34650
-  __DATA_CONST.__objc_selrefs: 0xc398
-  __DATA_CONST.__objc_arraydata: 0x798
-  __AUTH_CONST.__cfstring: 0x1b6e0
+  __DATA_CONST.__objc_const: 0x34bf8
+  __DATA_CONST.__objc_selrefs: 0xc428
+  __DATA_CONST.__objc_arraydata: 0x7d8
+  __AUTH_CONST.__cfstring: 0x1b8c0
   __AUTH_CONST.__objc_const: 0x6f58
   __AUTH_CONST.__const: 0x21f8
   __AUTH_CONST.__objc_arrayobj: 0x198
-  __AUTH_CONST.__objc_dictobj: 0x870
+  __AUTH_CONST.__objc_dictobj: 0x8c0
   __AUTH_CONST.__objc_intobj: 0x660
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_floatobj: 0x30
-  __AUTH_CONST.__auth_got: 0x1318
+  __AUTH_CONST.__auth_got: 0x1320
   __AUTH.__objc_data: 0x15e0
   __DATA.__objc_protorefs: 0x20
   __DATA.__objc_classrefs: 0xb80
   __DATA.__objc_superrefs: 0x598
-  __DATA.__objc_ivar: 0x2c84
+  __DATA.__objc_ivar: 0x2ca4
   __DATA.__data: 0x1a70
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x378

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D36CDE19-4A77-32B7-8E91-19FF2992E35C
-  Functions: 10917
-  Symbols:   35366
-  CStrings:  25364
+  UUID: 56742706-7080-3F44-B4FA-8D022888D3D7
+  Functions: 10938
+  Symbols:   35442
+  CStrings:  25426
 
Symbols:
+ -[COSMStateSummary setWifiAlwaysOutrank:]
+ -[COSMStateSummary setWifiNeverOutrank:]
+ -[COSMStateSummary setWifiPublicEligible:]
+ -[COSMStateSummary wifiAlwaysOutrank]
+ -[COSMStateSummary wifiNeverOutrank]
+ -[COSMStateSummary wifiPublicEligible]
+ -[CellOutrankHandler carrierBundleSISWiFiOutrankPolicyChangedForSubscription:]
+ -[CellOutrankHandlerSTM wifiPublicEligiblePred]
+ -[CoreTelephonyShim carrierBundleChange:]
+ -[CoreTelephonyShim getCurrentSISWiFiHotSpotOutrankPolicy]
+ -[CoreTelephonyShim wifiHotSpotOutrankPolicyStringFor:]
+ -[MiscStateRelay setWifiAlwaysOutrank:]
+ -[MiscStateRelay setWifiNeverOutrank:]
+ -[MiscStateRelay wifiAlwaysOutrank]
+ -[MiscStateRelay wifiNeverOutrank]
+ -[NWActivityHandler _isDBSizeWithinThreshold]
+ -[NWActivityHandler dbWriteStateToString:]
+ -[NWActivityHandler enableDBWrites]
+ -[NWActivityHandler handleDBEvent:]
+ -[NWActivityHandler writesToDBAllowed]
+ GCC_except_table107
+ GCC_except_table121
+ GCC_except_table135
+ GCC_except_table75
+ GCC_except_table84
+ GCC_except_table85
+ GCC_except_table94
+ _CTShimSubscriptionWiFiEnableMmWaveSisOutrank
+ _OBJC_IVAR_$_COSMStateSummary._wifiAlwaysOutrank
+ _OBJC_IVAR_$_COSMStateSummary._wifiNeverOutrank
+ _OBJC_IVAR_$_CellOutrankHandler._ctShim
+ _OBJC_IVAR_$_MiscStateRelay._wifiAlwaysOutrank
+ _OBJC_IVAR_$_MiscStateRelay._wifiNeverOutrank
+ _OBJC_IVAR_$_NWActivityHandler._dbWriteState
+ _OBJC_IVAR_$_NWActivityHandler._metricsDataWritesBudget
+ _OBJC_IVAR_$_NWActivityHelper._numberOfFragmentsInDB
+ _WiFiNetworkGetOriginator
+ ___113-[NetworkAnalyticsEngine performQueryOnEntity:fetchRequestProperties:pred:sort:actions:service:connection:reply:]_block_invoke.1256
+ ___31-[CoreTelephonyShim commonInit]_block_invoke.131
+ ___35-[NWActivityHandler enableDBWrites]_block_invoke
+ ___39-[CellOutrankHandler initializeHistory]_block_invoke.682
+ ___39-[CellOutrankHandler initializeHistory]_block_invoke.688
+ ___39-[CoreTelephonyShim _updateSubscribers]_block_invoke.256
+ ___39-[CoreTelephonyShim _updateSubscribers]_block_invoke.258
+ ___43-[NetworkAnalyticsEngine _armDOASuspector:]_block_invoke.1204
+ ___45-[CellOutrankHandler _completeInitialization]_block_invoke.650
+ ___45-[CellOutrankHandler _completeInitialization]_block_invoke.651
+ ___45-[CellOutrankHandler _completeInitialization]_block_invoke.658
+ ___45-[CellOutrankHandler _completeInitialization]_block_invoke.668
+ ___45-[CellOutrankHandler _completeInitialization]_block_invoke.670
+ ___45-[CellOutrankHandler _completeInitialization]_block_invoke.671
+ ___45-[CellOutrankHandler _completeInitialization]_block_invoke_2.673
+ ___45-[CoreTelephonyShim carrierSettingsDidChange]_block_invoke.249
+ ___45-[CoreTelephonyShim carrierSettingsDidChange]_block_invoke.251
+ ___45-[CoreTelephonyShim carrierSettingsDidChange]_block_invoke.252
+ ___45-[CoreTelephonyShim carrierSettingsDidChange]_block_invoke.253
+ ___51-[CoreTelephonyShim registerForCTDumpNotifications]_block_invoke.279
+ ___51-[NetworkAnalyticsEngine _idleExitTransactionCheck]_block_invoke.1203
+ ___53-[CoreTelephonyShim unregisterForCTDumpNotifications]_block_invoke.280
+ ___53-[NetworkAnalyticsEngine didReceiveProtocolSnapshot:]_block_invoke.1007
+ ___54-[NetworkAnalyticsEngine _armFatalSuspector:isActive:]_block_invoke.1214
+ ___55-[NetworkAnalyticsEngine _layer2MetricsOn:queue:reply:]_block_invoke.1264
+ ___57-[CoreTelephonyShim _deliverRNFSettingAvailable:enabled:]_block_invoke.178
+ ___57-[NetworkAnalyticsEngine _awdCaptureIn:replyQueue:reply:]_block_invoke.1362
+ ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.888
+ ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.896
+ ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.902
+ ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.904
+ ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.908
+ ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke_2.889
+ ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke_2.906
+ ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke_3.891
+ ___59-[WiFiShim observeValueForKeyPath:ofObject:change:context:]_block_invoke.44
+ ___60-[CoreTelephonyShim _registerForCoreTelephonyNotifications:]_block_invoke.176
+ ___61-[NetworkAnalyticsEngine _performNetAttachmentQueryOn:reply:]_block_invoke.1260
+ ___61-[NetworkAnalyticsEngine wifiShim_L2NewMetrics:forInterface:]_block_invoke.1048
+ ___62-[NetworkAnalyticsEngine _awdCaptureInstant:replyQueue:reply:]_block_invoke.1359
+ ___63-[CoreTelephonyShim _unregisterFromCoreTelephonyNotifications:]_block_invoke.177
+ ___66-[NetworkAnalyticsEngine _registerForSIMStatusChangeNotification:]_block_invoke.917
+ ___68-[CoreTelephonyShim _dispatchCellInfoResult:error:queue:completion:]_block_invoke.264
+ ___69-[CellOutrankHandler observeValueForKeyPath:ofObject:change:context:]_block_invoke.630
+ ___69-[CellOutrankHandler observeValueForKeyPath:ofObject:change:context:]_block_invoke.632
+ ___69-[CellOutrankHandler observeValueForKeyPath:ofObject:change:context:]_block_invoke_2.631
+ ___69-[CellOutrankHandler observeValueForKeyPath:ofObject:change:context:]_block_invoke_2.633
+ ___76-[CoreTelephonyShim _deliverSignalStrengthChanged:cellularRSRP:cellularSNR:]_block_invoke.183
+ ___76-[NetworkAnalyticsEngine _usageToLOICorrelationFor:scopedToLOI:queue:reply:]_block_invoke.1274
+ ___78-[NetworkAnalyticsEngine _estimatedTransferTimeOn:forPayloadInfo:queue:reply:]_block_invoke.1265
+ ___78-[NetworkAnalyticsEngine _estimatedTransferTimeOn:forPayloadInfo:queue:reply:]_block_invoke_2.1266
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1135
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1145
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1149
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1156
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1164
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1177
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1181
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke_2.1168
+ ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke_2.1182
+ ___block_literal_global.1023
+ ___block_literal_global.1081
+ ___block_literal_global.1170
+ ___block_literal_global.1255
+ ___block_literal_global.1262
+ ___block_literal_global.1276
+ ___block_literal_global.1352
+ ___block_literal_global.159
+ ___block_literal_global.273
+ ___block_literal_global.314
+ ___block_literal_global.680
+ ___block_literal_global.912
+ ___block_literal_global.914
+ ___block_literal_global.916
+ __unnamed_array_storage.269
+ __unnamed_array_storage.270
+ __unnamed_array_storage.276
+ __unnamed_array_storage.277
+ __unnamed_array_storage.307
+ __unnamed_array_storage.308
+ __unnamed_array_storage.314
+ __unnamed_array_storage.315
+ __unnamed_array_storage.324
+ __unnamed_array_storage.325
+ __unnamed_array_storage.332
+ __unnamed_array_storage.344
+ __unnamed_array_storage.345
+ __unnamed_array_storage.354
+ __unnamed_array_storage.355
+ __unnamed_array_storage.364
+ __unnamed_array_storage.365
+ __unnamed_array_storage.381
+ __unnamed_array_storage.382
+ __unnamed_array_storage.392
+ __unnamed_array_storage.393
+ __unnamed_array_storage.399
+ __unnamed_array_storage.400
+ __unnamed_array_storage.403
+ __unnamed_array_storage.404
+ __unnamed_array_storage.617
+ __unnamed_array_storage.618
+ _kWiFiShimIsCarrierBundle
+ _objc_msgSend$_isDBSizeWithinThreshold
+ _objc_msgSend$carrierBundleSISWiFiOutrankPolicyChangedForSubscription:
+ _objc_msgSend$currentDBSizeInBytes
+ _objc_msgSend$dbWriteStateToString:
+ _objc_msgSend$enableDBWrites
+ _objc_msgSend$fileSystemSizeInBytes
+ _objc_msgSend$getCurrentSISWiFiHotSpotOutrankPolicy
+ _objc_msgSend$handleDBEvent:
+ _objc_msgSend$setWifiAlwaysOutrank:
+ _objc_msgSend$setWifiNeverOutrank:
+ _objc_msgSend$wifiAlwaysOutrank
+ _objc_msgSend$wifiHotSpotOutrankPolicyStringFor:
+ _objc_msgSend$wifiNeverOutrank
+ _objc_msgSend$wifiPublicEligiblePred
+ _objc_msgSend$writesToDBAllowed
- GCC_except_table104
- GCC_except_table130
- GCC_except_table71
- GCC_except_table77
- ___113-[NetworkAnalyticsEngine performQueryOnEntity:fetchRequestProperties:pred:sort:actions:service:connection:reply:]_block_invoke.1255
- ___31-[CoreTelephonyShim commonInit]_block_invoke.128
- ___39-[CellOutrankHandler initializeHistory]_block_invoke.656
- ___39-[CellOutrankHandler initializeHistory]_block_invoke.662
- ___39-[CoreTelephonyShim _updateSubscribers]_block_invoke.242
- ___39-[CoreTelephonyShim _updateSubscribers]_block_invoke.244
- ___43-[NetworkAnalyticsEngine _armDOASuspector:]_block_invoke.1203
- ___45-[CellOutrankHandler _completeInitialization]_block_invoke.624
- ___45-[CellOutrankHandler _completeInitialization]_block_invoke.625
- ___45-[CellOutrankHandler _completeInitialization]_block_invoke.632
- ___45-[CellOutrankHandler _completeInitialization]_block_invoke.642
- ___45-[CellOutrankHandler _completeInitialization]_block_invoke.644
- ___45-[CellOutrankHandler _completeInitialization]_block_invoke.645
- ___45-[CellOutrankHandler _completeInitialization]_block_invoke_2.647
- ___45-[CoreTelephonyShim carrierSettingsDidChange]_block_invoke.235
- ___45-[CoreTelephonyShim carrierSettingsDidChange]_block_invoke.237
- ___45-[CoreTelephonyShim carrierSettingsDidChange]_block_invoke.238
- ___45-[CoreTelephonyShim carrierSettingsDidChange]_block_invoke.239
- ___51-[CoreTelephonyShim registerForCTDumpNotifications]_block_invoke.265
- ___51-[NetworkAnalyticsEngine _idleExitTransactionCheck]_block_invoke.1202
- ___53-[CoreTelephonyShim unregisterForCTDumpNotifications]_block_invoke.266
- ___53-[NetworkAnalyticsEngine didReceiveProtocolSnapshot:]_block_invoke.1006
- ___54-[NetworkAnalyticsEngine _armFatalSuspector:isActive:]_block_invoke.1212
- ___55-[NetworkAnalyticsEngine _layer2MetricsOn:queue:reply:]_block_invoke.1262
- ___57-[CoreTelephonyShim _deliverRNFSettingAvailable:enabled:]_block_invoke.175
- ___57-[NetworkAnalyticsEngine _awdCaptureIn:replyQueue:reply:]_block_invoke.1361
- ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.887
- ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.895
- ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.900
- ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.903
- ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke.907
- ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke_2.888
- ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke_2.905
- ___57-[NetworkAnalyticsEngine initWithWorkspace:params:queue:]_block_invoke_3.890
- ___59-[WiFiShim observeValueForKeyPath:ofObject:change:context:]_block_invoke.41
- ___60-[CoreTelephonyShim _registerForCoreTelephonyNotifications:]_block_invoke.173
- ___61-[NetworkAnalyticsEngine _performNetAttachmentQueryOn:reply:]_block_invoke.1259
- ___61-[NetworkAnalyticsEngine wifiShim_L2NewMetrics:forInterface:]_block_invoke.1047
- ___62-[NetworkAnalyticsEngine _awdCaptureInstant:replyQueue:reply:]_block_invoke.1358
- ___63-[CoreTelephonyShim _unregisterFromCoreTelephonyNotifications:]_block_invoke.174
- ___66-[NetworkAnalyticsEngine _registerForSIMStatusChangeNotification:]_block_invoke.916
- ___68-[CoreTelephonyShim _dispatchCellInfoResult:error:queue:completion:]_block_invoke.250
- ___69-[CellOutrankHandler observeValueForKeyPath:ofObject:change:context:]_block_invoke.605
- ___69-[CellOutrankHandler observeValueForKeyPath:ofObject:change:context:]_block_invoke.607
- ___69-[CellOutrankHandler observeValueForKeyPath:ofObject:change:context:]_block_invoke_2.606
- ___69-[CellOutrankHandler observeValueForKeyPath:ofObject:change:context:]_block_invoke_2.608
- ___76-[CoreTelephonyShim _deliverSignalStrengthChanged:cellularRSRP:cellularSNR:]_block_invoke.180
- ___76-[NetworkAnalyticsEngine _usageToLOICorrelationFor:scopedToLOI:queue:reply:]_block_invoke.1273
- ___78-[NetworkAnalyticsEngine _estimatedTransferTimeOn:forPayloadInfo:queue:reply:]_block_invoke.1264
- ___78-[NetworkAnalyticsEngine _estimatedTransferTimeOn:forPayloadInfo:queue:reply:]_block_invoke_2.1265
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1134
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1144
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1148
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1155
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1163
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1176
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke.1180
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke_2.1167
- ___80-[NetworkAnalyticsEngine startRNFTestWithConnection:options:scenarioName:reply:]_block_invoke_2.1181
- ___block_literal_global.1022
- ___block_literal_global.1080
- ___block_literal_global.1169
- ___block_literal_global.1254
- ___block_literal_global.1261
- ___block_literal_global.1275
- ___block_literal_global.1351
- ___block_literal_global.153
- ___block_literal_global.259
- ___block_literal_global.302
- ___block_literal_global.654
- ___block_literal_global.911
- ___block_literal_global.913
- ___block_literal_global.915
- __unnamed_array_storage.272
- __unnamed_array_storage.273
- __unnamed_array_storage.279
- __unnamed_array_storage.280
- __unnamed_array_storage.310
- __unnamed_array_storage.311
- __unnamed_array_storage.317
- __unnamed_array_storage.318
- __unnamed_array_storage.330
- __unnamed_array_storage.340
- __unnamed_array_storage.341
- __unnamed_array_storage.350
- __unnamed_array_storage.351
- __unnamed_array_storage.357
- __unnamed_array_storage.358
- __unnamed_array_storage.367
- __unnamed_array_storage.368
- __unnamed_array_storage.378
- __unnamed_array_storage.379
- __unnamed_array_storage.389
- __unnamed_array_storage.390
- __unnamed_array_storage.595
- __unnamed_array_storage.596
CStrings:
+ "\x0211\x14\x19"
+ "\x13\x1d1R\xf0!\x11\x86!"
+ " wifiAlwaysOutrank"
+ " wifiNeverOutrank"
+ "((wifiActive == YES) AND ((wifiPrimary == YES) OR (wifiGoodSecurity == NO)) AND (wifiManuallyJoined == NO) AND ((wifiSporadic == YES) OR (cellPrivateNetworkActive == YES) OR ((wifiAlwaysOutrank == YES) AND (cellWRMExpensive == NO))) AND ((LOIUseAuthorized == NO) OR ((homeLocationIsKnown == YES) AND (wifiHome == NO))) AND (wifiPublicEligible == YES))"
+ "(forcedOutrankEligible == YES) OR ((armedEligible == YES) AND ((wifiGoodSecurity == NO) OR  (cellPrivateNetworkActive == YES) OR  (wifiLowDataMode == YES) OR  (coremediaDownloadActive == YES) OR  (captivityFrictionEligible == YES) OR  (wifiAmbientFrictionEligible == YES) OR  (wifiTputAdvice == YES) OR  (userInitiatedFrictionEligible == YES) OR  (trialWaiveOutrankReason == YES) OR  ((wifiNeverOutrank == NO) AND (wifiAlwaysOutrank == YES) AND (cellWRMExpensive == NO))) )"
+ "(wifiNeverOutrank == NO) AND (((wifiAlwaysOutrank == YES) AND (cellWRMExpensive == NO)) OR ((wifiPublic == NO) OR ((wifiHotspot20 == NO) AND (wifiManaged == NO))))"
+ "Always Outrank"
+ "COSM: updateForAssociation %d active %d sporadic %d (known:%d spor:%d 1st:%d) goodsecurity %d man join %d (m:%d d:%d) public %d prof-base %d hspot20 %d carrier %d (always %d never %d) "
+ "COSMStateSummary: trial %d force-profile %d forceSPI %d damp %d cell act %d const %d exp %d wexp %d pri %d wrm %d pbad %d prvnwact %d wifi act %d const %d exp %d goodsec %d pri %d dnsout %d pdnsout %d public %d hotspot20 %d managed %d always %d never %d sporadic %d known %d m-join %d flow-bad %d pbad %d tput-adv %d (lrg:%d/hi:%d) wrm %d home (auth:%d/known:%d)d/l act %d hyst %d end %d LPM %d notDark %d unlock %d thermal %d rnf act %d ev exp %d certs %d dstall %d istall %d mstall %d ssidchg %d regret %d wifitputend %d prvnwoutrank %d secno %lld"
+ "CTShim: carrierBundleChange, context slotID (%ld) does not match with currentSubscriberSlotID (%ld)"
+ "CTShim: wifiHotSpotOutrankPolicy is now %@, was %@"
+ "Carrier Bundle without Profile"
+ "EnableMmWaveSisOutrank"
+ "NWACT: Current DB State: Check DB size. Received Event: Check DB size."
+ "NWACT: Current DB State: Not ready. Received Event: Initialize."
+ "NWACT: Current DB State: Ready. Received Event: Wrote metric to disk."
+ "NWACT: Current DB size = %llu, DB size threshold = %llu"
+ "NWACT: Current DB state: %@, writes throttled."
+ "NWACT: DB size checked, over threshold."
+ "NWACT: DB size checked, under threshold."
+ "NWACT: Successfully saved metric with activity UUIDS: %@ and type: %d, writes budget remaining: %llu"
+ "NWACT: Unexpected NWActivityDBEvent received."
+ "NWActivityDBWriteStateCheckFileSize"
+ "NWActivityDBWriteStateInvalid"
+ "NWActivityDBWriteStateNotReady"
+ "NWActivityDBWriteStateReady"
+ "Never Outrank"
+ "No Advice"
+ "TB,N,V_wifiAlwaysOutrank"
+ "TB,N,V_wifiNeverOutrank"
+ "WiFiAlwaysOutrank"
+ "WiFiNeverOutrank"
+ "_ctShim"
+ "_dbWriteState"
+ "_isDBSizeWithinThreshold"
+ "_metricsDataWritesBudget"
+ "_numberOfFragmentsInDB"
+ "_wifiAlwaysOutrank"
+ "_wifiNeverOutrank"
+ "carrierBundleChange:"
+ "carrierBundleSISWiFiOutrankPolicyChangedForSubscription:"
+ "currentDBSizeInBytes"
+ "dbWriteStateToString:"
+ "enableDBWrites"
+ "fileSystemSizeInBytes"
+ "getCurrentSISWiFiHotSpotOutrankPolicy"
+ "handleDBEvent:"
+ "isCarrierBundle"
+ "setWifiAlwaysOutrank:"
+ "setWifiNeverOutrank:"
+ "setWifiPublicEligible:"
+ "wifiAlwaysOutrank"
+ "wifiHotSpotOutrankPolicyStringFor:"
+ "wifiNeverOutrank"
+ "wifiPublicEligible"
+ "wifiPublicEligiblePred"
+ "writesToDBAllowed"
- "\x021\x11\x14\x19"
- "\x13\x1c1R\xf0!\x11\x86!"
- "((wifiActive == YES) AND ((wifiPrimary == YES) OR (wifiGoodSecurity == NO)) AND (wifiManuallyJoined == NO) AND ((wifiSporadic == YES) OR (cellPrivateNetworkActive == YES)) AND ((LOIUseAuthorized == NO) OR ((homeLocationIsKnown == YES) AND (wifiHome == NO))) AND ((wifiPublic == NO) OR ((wifiPublic == YES) AND (wifiHotspot20 == NO) AND (wifiManaged == NO))))"
- "(forcedOutrankEligible == YES) OR ((armedEligible == YES) AND ((wifiGoodSecurity == NO) OR  (cellPrivateNetworkActive == YES) OR  (wifiLowDataMode == YES) OR  (coremediaDownloadActive == YES) OR  (captivityFrictionEligible == YES) OR  (wifiAmbientFrictionEligible == YES) OR  (wifiTputAdvice == YES) OR  (userInitiatedFrictionEligible == YES) OR  (trialWaiveOutrankReason == YES) ))"
- "COSM: updateForAssociation %d active %d sporadic %d (known:%d spor:%d 1st:%d) public %d goodsecurity %d man join %d (m:%d d:%d) prof-base %d hspot20 %d"
- "COSMStateSummary: trial %d force-profile %d forceSPI %d damp %d cell act %d const %d exp %d wexp %d pri %d wrm %d pbad %d prvnwact %d wifi act %d const %d exp %d goodsec %d pri %d dnsout %d pdnsout %d public %d hotspot20 %d managed %d sporadic %d known %d m-join %d flow-bad %d pbad %d tput-adv %d (lrg:%d/hi:%d) wrm %d home (auth:%d/known:%d)d/l act %d hyst %d end %d LPM %d notDark %d unlock %d thermal %d rnf act %d ev exp %d certs %d dstall %d istall %d mstall %d ssidchg %d regret %d wifitputend %d prvnwoutrank %d secno %lld"
- "Deleted %ld old activities"
- "Deleting old activity %@"
- "Failed to delete expired metrics, error: %@"
- "Failed to fetch context when garbage collecting metrics, skipping"
- "LINK_CHANGED_NETWORK"
- "NWACT: Successfully saved metric with activity UUIDS:%@ and type:%d"
- "ObsoleteDeviceInMotion"
- "ObsoleteTCPProgressHints"

```
