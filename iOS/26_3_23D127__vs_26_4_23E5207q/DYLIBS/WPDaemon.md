## WPDaemon

> `/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon`

```diff

-193.9.0.0.0
-  __TEXT.__text: 0x5de7c
-  __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_methlist: 0x4294
-  __TEXT.__cstring: 0x44a2
+194.22.1.1.1
+  __TEXT.__text: 0x5f8b8
+  __TEXT.__auth_stubs: 0x880
+  __TEXT.__objc_methlist: 0x42a4
+  __TEXT.__cstring: 0x44ff
   __TEXT.__const: 0x218
-  __TEXT.__oslogstring: 0xa8a6
-  __TEXT.__gcc_except_tab: 0x16dc
-  __TEXT.__unwind_info: 0x1e68
-  __TEXT.__objc_classname: 0x37a
-  __TEXT.__objc_methname: 0x9f2c
+  __TEXT.__oslogstring: 0xa889
+  __TEXT.__gcc_except_tab: 0x1548
+  __TEXT.__unwind_info: 0x1ee0
+  __TEXT.__objc_classname: 0x37b
+  __TEXT.__objc_methname: 0x9fba
   __TEXT.__objc_methtype: 0x1680
-  __TEXT.__objc_stubs: 0x7f20
-  __DATA_CONST.__got: 0x488
+  __TEXT.__objc_stubs: 0x7f60
+  __DATA_CONST.__got: 0x490
   __DATA_CONST.__const: 0x1260
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x26d8
+  __DATA_CONST.__objc_selrefs: 0x26e8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x2c0
-  __AUTH_CONST.__auth_got: 0x478
-  __AUTH_CONST.__const: 0x6920
-  __AUTH_CONST.__cfstring: 0x33e0
-  __AUTH_CONST.__objc_const: 0x8498
-  __AUTH_CONST.__objc_intobj: 0x150
+  __AUTH_CONST.__auth_got: 0x450
+  __AUTH_CONST.__const: 0x6900
+  __AUTH_CONST.__cfstring: 0x3400
+  __AUTH_CONST.__objc_const: 0x84c8
+  __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x51c
+  __DATA.__objc_ivar: 0x520
   __DATA.__data: 0x600
   __DATA.__bss: 0x4
   __DATA_DIRTY.__objc_data: 0x820

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CBEC99A4-2405-339C-9134-EC8286BCA63F
-  Functions: 3402
-  Symbols:   10028
-  CStrings:  4004
+  UUID: 914D0803-CF16-3825-8A1B-6836B19D8FB3
+  Functions: 3412
+  Symbols:   10104
+  CStrings:  4010
 
Symbols:
+ -[WPScanRequest heySiriElectionEndTimeNsec]
+ -[WPScanRequest setHeySiriElectionEndTimeNsec:]
+ GCC_except_table164
+ GCC_except_table352
+ _CBCentralManagerScanOptionHeySiriElectionEndTimeNsec
+ _OBJC_IVAR_$_WPScanRequest._heySiriElectionEndTimeNsec
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ ___20-[WPDClient destroy]_block_invoke.591
+ ___24+[WPDManager initialize]_block_invoke.123
+ ___24-[WPDConnection dealloc]_block_invoke.125
+ ___24-[WPDPipeManager update]_block_invoke.773
+ ___24-[WPDScanManager update]_block_invoke.400
+ ___24-[WPDScanManager update]_block_invoke.403
+ ___24-[WPDScanManager update]_block_invoke.406
+ ___24-[WPDScanManager update]_block_invoke.409
+ ___24-[WPDZoneManager update]_block_invoke.172
+ ___26-[WPDClient destroy_async]_block_invoke.597
+ ___26-[WPDClient stopScanning:]_block_invoke.760
+ ___27-[WPDClient tickleMachPort]_block_invoke.574
+ ___28-[WPDClient setupConnection]_block_invoke.582
+ ___28-[WPDClient setupConnection]_block_invoke.582.cold.1
+ ___28-[WPDClient setupConnection]_block_invoke_2.583
+ ___28-[WPDaemonServer addClient:]_block_invoke.247
+ ___29-[WPDClient sendTestRequest:]_block_invoke.993
+ ___29-[WPDClient stopAdvertising:]_block_invoke.658
+ ___29-[WPDaemonServer initClients]_block_invoke.222
+ ___29-[WPDaemonServer updateState]_block_invoke.235
+ ___30+[WPDClient generateStateDump]_block_invoke.471
+ ___30-[WPDClient discoveredDevice:]_block_invoke.688
+ ___30-[WPDClient startAdvertising:]_block_invoke.615
+ ___30-[WPDaemonServer initManagers]_block_invoke.210
+ ___30-[WPDaemonServer initManagers]_block_invoke.210.cold.1
+ ___30-[WPDaemonServer initManagers]_block_invoke.210.cold.2
+ ___31-[WPDAdvertisingManager update]_block_invoke.472
+ ___31-[WPDClient createdConnection:]_block_invoke.881
+ ___31-[WPDClient discoveredDevices:]_block_invoke.692
+ ___31-[WPDScanManager updateScanner]_block_invoke.414
+ ___31-[WPDZoneManager updateScanner]_block_invoke.233
+ ___31-[WPDZoneManager updateScanner]_block_invoke.237
+ ___31-[WPDaemonServer removeClient:]_block_invoke.261
+ ___32-[WPDClient disconnectFromPeer:]_block_invoke.857
+ ___32-[WPDClient stopScanning_async:]_block_invoke.772
+ ___32-[WPDStatsManager reportPLStats]_block_invoke.213
+ ___32-[WPDZoneManager exitTimerFired]_block_invoke.247
+ ___32-[WPDZoneManager exitTimerFired]_block_invoke.247.cold.1
+ ___32-[WPDZoneManager startExitTimer]_block_invoke.242
+ ___32-[WPDaemonServer enableRanging:]_block_invoke.271
+ ___33-[WPDClient anyDiscoveredDevice:]_block_invoke.695
+ ___33-[WPDClient enableRanging:reply:]_block_invoke.946
+ ___33-[WPDClient startScanning_async:]_block_invoke.705
+ ___33-[WPDClient startScanning_async:]_block_invoke.711
+ ___33-[WPDClient startScanning_async:]_block_invoke.717
+ ___33-[WPDClient startScanning_async:]_block_invoke.723
+ ___33-[WPDClient startScanning_async:]_block_invoke.741.cold.1
+ ___33-[WPDClient startScanning_async:]_block_invoke.741.cold.2
+ ___33-[WPDClient startScanning_async:]_block_invoke.747
+ ___33-[WPDClient startScanning_async:]_block_invoke.747.cold.1
+ ___33-[WPDClient startScanning_async:]_block_invoke.747.cold.2
+ ___33-[WPDClient startScanning_async:]_block_invoke.747.cold.3
+ ___33-[WPDClient startScanning_async:]_block_invoke.754
+ ___33-[WPDClient startScanning_async:]_block_invoke_2.748
+ ___33-[WPDPipeManager channelHasData:]_block_invoke.824
+ ___33-[WPDPipeManager channelHasData:]_block_invoke.828
+ ___33-[WPDPipeManager channelHasData:]_block_invoke_2.825
+ ___33-[WPDScanManager updateScanRules]_block_invoke.293
+ ___33-[WPDScanManager updateScanRules]_block_invoke.297
+ ___33-[WPDScanManager updateScanRules]_block_invoke.314
+ ___33-[WPDScanManager updateScanRules]_block_invoke.321
+ ___33-[WPDScanManager updateScanRules]_block_invoke.324
+ ___33-[WPDScanManager updateScanRules]_block_invoke_2.318
+ ___33-[WPDScanManager updateScanRules]_block_invoke_2.327
+ ___33-[WPDScanManager updateScanRules]_block_invoke_3.328
+ ___33-[WPDScanManager updateScanRules]_block_invoke_4.329
+ ___34-[WPDClient verifyApprovedUseCase]_block_invoke.466
+ ___34-[WPDConnection sendDataToCentral]_block_invoke.245
+ ___34-[WPDPipeManager sendChannelData:]_block_invoke.813
+ ___35-[WPDClient stopAdvertising_async:]_block_invoke.667
+ ___35-[WPDObjectDiscoveryManager update]_block_invoke.178
+ ___35-[WPDScanManager addSpyScanClient:]_block_invoke.173
+ ___35-[WPDaemonServer generateStateDump]_block_invoke.363
+ ___35-[WPDaemonServer generateStateDump]_block_invoke.367
+ ___35-[WPDaemonServer generateStateDump]_block_invoke.381
+ ___35-[WPDaemonServer getClientForUUID:]_block_invoke.229
+ ___36-[WPDClient disconnectedPeer:error:]_block_invoke.862
+ ___36-[WPDClient disconnectedPeer:error:]_block_invoke.868
+ ___36-[WPDClient startAdvertising_async:]_block_invoke.618
+ ___36-[WPDClient startAdvertising_async:]_block_invoke.628.cold.1
+ ___36-[WPDClient startAdvertising_async:]_block_invoke.628.cold.2
+ ___36-[WPDClient startAdvertising_async:]_block_invoke.634
+ ___36-[WPDClient startAdvertising_async:]_block_invoke.634.cold.1
+ ___36-[WPDClient startAdvertising_async:]_block_invoke.634.cold.2
+ ___36-[WPDClient startAdvertising_async:]_block_invoke.634.cold.3
+ ___36-[WPDClient startAdvertising_async:]_block_invoke.641
+ ___36-[WPDClient startAdvertising_async:]_block_invoke.645
+ ___36-[WPDClient startAdvertising_async:]_block_invoke.653
+ ___36-[WPDClient startAdvertising_async:]_block_invoke_2.635
+ ___36-[WPDPipeManager sendAck:errorCode:]_block_invoke.703
+ ___36-[WPDScanManager heySiriScanActive:]_block_invoke.253
+ ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.220
+ ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.220.cold.1
+ ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.220.cold.2
+ ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.220.cold.3
+ ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.224
+ ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.228
+ ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.228.cold.1
+ ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.233
+ ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.233.cold.1
+ ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.233.cold.2
+ ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.233.cold.3
+ ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.237
+ ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.248
+ ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke_2.221
+ ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke_2.229
+ ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke_2.234
+ ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke_2.241
+ ___36-[WPDaemonServer SetupSignalHandler]_block_invoke.164
+ ___37-[WPDConnection sendDataToPeripheral]_block_invoke.265
+ ___37-[WPDPipeManager pipeInfo:forClient:]_block_invoke.498
+ ___37-[WPDPipeManager stream:handleEvent:]_block_invoke.559
+ ___37-[WPDPipeManager stream:handleEvent:]_block_invoke.569
+ ___37-[WPDPipeManager stream:handleEvent:]_block_invoke_2.560
+ ___38-[WPDScanManager removeSpyScanClient:]_block_invoke.178
+ ___38-[WPDaemonServer dumpDaemonStateAsync]_block_invoke.388
+ ___39-[WPDClient connectToPeer:withOptions:]_block_invoke.821
+ ___39-[WPDClient connectedDeviceOverLEPipe:]_block_invoke.843
+ ___39-[WPDPendingCompletions addCompletion:]_block_invoke.129
+ ___39-[WPDPipeManager writeDataToPipe:pipe:]_block_invoke.747
+ ___40-[WPDAdvertisingManager initWithServer:]_block_invoke.198
+ ___40-[WPDAdvertisingManager initWithServer:]_block_invoke.204
+ ___40-[WPDClient startScanning:withDispatch:]_block_invoke.699
+ ___40-[WPDScanManager assertCBDiscoveryScan:]_block_invoke.233
+ ___40-[WPDScanManager assertCBDiscoveryScan:]_block_invoke.240
+ ___40-[WPDSearchPartyAgent generateStateDump]_block_invoke.211
+ ___41-[WPDAdvertisingManager advertisingRules]_block_invoke.414
+ ___41-[WPDAdvertisingManager advertisingRules]_block_invoke.426
+ ___41-[WPDAdvertisingManager advertisingRules]_block_invoke.430
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.347
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.356
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.368
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.370
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.376
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.376.cold.1
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.376.cold.2
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.380
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.384
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.384.cold.1
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.384.cold.2
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.388
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.392
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.392.cold.1
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.397
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke_2.359
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke_2.377
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke_2.385
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke_2.393
+ ___41-[WPDState updateWithManager:Completion:]_block_invoke.131
+ ___41-[WPDState updateWithManager:Completion:]_block_invoke.136
+ ___41-[WPDaemonServer initWithCBStackAdaptor:]_block_invoke.178
+ ___41-[WPDaemonServer initWithCBStackAdaptor:]_block_invoke.188
+ ___41-[WPDaemonServer initWithCBStackAdaptor:]_block_invoke.188.cold.1
+ ___41-[WPDaemonServer initWithCBStackAdaptor:]_block_invoke.188.cold.2
+ ___41-[WPDaemonServer initWithCBStackAdaptor:]_block_invoke.193
+ ___41-[WPDaemonServer initWithCBStackAdaptor:]_block_invoke.197
+ ___42-[PipeDataTransfer generateSequenceNumber]_block_invoke.146
+ ___42-[WPDClient initWithXPCConnection:server:]_block_invoke.487
+ ___42-[WPDClient initWithXPCConnection:server:]_block_invoke.493
+ ___42-[WPDClient initWithXPCConnection:server:]_block_invoke.493.cold.1
+ ___42-[WPDClient initWithXPCConnection:server:]_block_invoke.493.cold.2
+ ___42-[WPDObjectDiscoveryManager updateScanner]_block_invoke.384
+ ___42-[WPDScanManager clearExistingConnections]_block_invoke.393
+ ___43-[WPDScanManager addScanRequest:forClient:]_block_invoke.203
+ ___43-[WPDScanManager addScanRequest:forClient:]_block_invoke.209
+ ___44-[WPDAdvertisingData addAdvertisingRequest:]_block_invoke.129
+ ___44-[WPDObjectDiscoveryClient sendTestRequest:]_block_invoke.262
+ ___44-[WPDObjectDiscoveryClient startSPBeaconing]_block_invoke.206
+ ___44-[WPDObjectDiscoveryClient stopAdvertising:]_block_invoke.242
+ ___44-[WPDObjectDiscoveryClient stopAdvertising:]_block_invoke.251
+ ___44-[WPDObjectDiscoveryManager updateScanRules]_block_invoke.362
+ ___44-[WPDObjectDiscoveryManager updateScanRules]_block_invoke.368
+ ___44-[WPDPendingCompletions completeID:success:]_block_invoke.140
+ ___44-[WPDPipeManager receivedAck:data:dataSize:]_block_invoke.662
+ ___44-[WPDPipeManager receivedAck:data:dataSize:]_block_invoke.668
+ ___44-[WPDPipeManager receivedAck:data:dataSize:]_block_invoke.675
+ ___44-[WPDPipeManager receivedAck:data:dataSize:]_block_invoke_2.669
+ ___44-[WPDSearchPartyAgent updateTestBeaconKeys:]_block_invoke.283
+ ___44-[WPDZoneManager unregisterZones:forClient:]_block_invoke.283
+ ___45-[WPDAdvertisingManager heySiriAdvertActive:]_block_invoke.455
+ ___45-[WPDClient clearDuplicateFilterCache_async:]_block_invoke.786
+ ___45-[WPDObjectDiscoveryClient generateStateDump]_block_invoke.168
+ ___45-[WPDObjectDiscoveryClient startAdvertising:]_block_invoke.215
+ ___45-[WPDObjectDiscoveryClient startAdvertising:]_block_invoke.222
+ ___45-[WPDObjectDiscoveryClient startAdvertising:]_block_invoke.234
+ ___45-[WPDObjectDiscoveryClient updateSPBeaconing]_block_invoke.200
+ ___45-[WPDObjectDiscoveryManager addScanStopTimer]_block_invoke.428
+ ___45-[WPDObjectDiscoveryManager addScanStopTimer]_block_invoke.428.cold.1
+ ___45-[WPDPipeManager invalidatePipeInfo:forPeer:]_block_invoke.844
+ ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.431
+ ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.436
+ ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.440
+ ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.446
+ ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.450
+ ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.457
+ ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.461
+ ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.465
+ ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.472
+ ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke_2.454
+ ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke_2.458
+ ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke_2.462
+ ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke_2.469
+ ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke_2.473
+ ___45-[WPDPipeManager sendRemainingData:wpClient:]_block_invoke.726
+ ___45-[WPDScanManager reconcileScanRule:withRule:]_block_invoke.258
+ ___45-[WPDScanManager reconcileScanRule:withRule:]_block_invoke.258.cold.1
+ ___45-[WPDScanManager reconcileScanRule:withRule:]_block_invoke.258.cold.2
+ ___45-[WPDScanManager reconcileScanRule:withRule:]_block_invoke.263
+ ___45-[WPDSearchPartyAgent rollKeysWithRequestID:]_block_invoke.253.cold.1
+ ___45-[WPDSearchPartyAgent rollKeysWithRequestID:]_block_invoke.253.cold.2
+ ___45-[WPDSearchPartyAgent rollKeysWithRequestID:]_block_invoke.253.cold.3
+ ___45-[WPDSearchPartyAgent rollKeysWithRequestID:]_block_invoke.253.cold.4
+ ___45-[WPDSearchPartyAgent rollKeysWithRequestID:]_block_invoke.256
+ ___45-[WPDSearchPartyAgent rollKeysWithRequestID:]_block_invoke.269
+ ___46+[WPDSearchPartyAgent spBeaconKeyFromTestKey:]_block_invoke.307
+ ___46-[WPDConnection peripheral:didModifyServices:]_block_invoke.199
+ ___46-[WPDPipeManager receivedError:data:dataSize:]_block_invoke.683
+ ___46-[WPDPipeManager receivedError:data:dataSize:]_block_invoke.692
+ ___46-[WPDScanManager removeScanRequest:forClient:]_block_invoke.220
+ ___47-[WPDPipeManager unregisterEndpoint:forClient:]_block_invoke.423
+ ___48-[WPDAdvertisingManager removeServiceForClient:]_block_invoke.299
+ ___48-[WPDClient advertisingStoppedOfType:withError:]_block_invoke.678
+ ___48-[WPDClient notifyClientStateChange:Restricted:]_block_invoke.683
+ ___48-[WPDConnection peripheral:didDiscoverServices:]_block_invoke.155
+ ___48-[WPDConnection peripheral:didDiscoverServices:]_block_invoke.162
+ ___48-[WPDConnection peripheral:didDiscoverServices:]_block_invoke.162.cold.1
+ ___48-[WPDConnection peripheral:didDiscoverServices:]_block_invoke.162.cold.2
+ ___48-[WPDConnection peripheral:didDiscoverServices:]_block_invoke_2.163
+ ___48-[WPDObjectDiscoveryClient updateSPNearbyTokens]_block_invoke.191
+ ___48-[WPDObjectDiscoveryManager cancelScanStopTimer]_block_invoke.423
+ ___48-[WPDObjectDiscoveryManager updateNearbyTokens:]_block_invoke.307
+ ___48-[WPDObjectDiscoveryManager updateNearbyTokens:]_block_invoke.325
+ ___48-[WPDPipeManager receivedPayload:data:dataSize:]_block_invoke.632
+ ___48-[WPDPipeManager receivedPayload:data:dataSize:]_block_invoke.632.cold.1
+ ___48-[WPDPipeManager receivedPayload:data:dataSize:]_block_invoke.642
+ ___48-[WPDPipeManager receivedPayload:data:dataSize:]_block_invoke_2.633
+ ___49-[WPDAdvertisingManager enableRanging:forClient:]_block_invoke.309
+ ___49-[WPDScanManager scanOptionsChanged:ForRequests:]_block_invoke.343
+ ___49-[WPDScanManager scanOptionsChanged:ForRequests:]_block_invoke.346
+ ___49-[WPDScanManager scanOptionsChanged:ForRequests:]_block_invoke.349
+ ___49-[WPDScanManager scanOptionsChanged:ForRequests:]_block_invoke.352
+ ___49-[WPDScanManager scanOptionsChanged:ForRequests:]_block_invoke.355
+ ___50-[WPDObjectDiscoveryManager advertOptionsChanged:]_block_invoke.186
+ ___50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.197.cold.1
+ ___50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.197.cold.2
+ ___50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.197.cold.3
+ ___50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.197.cold.4
+ ___50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.197.cold.5
+ ___50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.197.cold.6
+ ___50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.197.cold.7
+ ___50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.197.cold.8
+ ___50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.197.cold.9
+ ___50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.209
+ ___51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.466
+ ___51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.472
+ ___51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.475
+ ___51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.478
+ ___51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.484
+ ___51-[WPDZoneManager addZoneTrackingRequest:forClient:]_block_invoke.265
+ ___51-[WPDZoneManager addZoneTrackingRequest:forClient:]_block_invoke.272
+ ___52-[WPDPipeManager receivedVersionInfo:data:dataSize:]_block_invoke.594
+ ___53-[WPDPipeManager scalablePipeManager:pipeDidConnect:]_block_invoke.782
+ ___53-[WPDPipeManager scalablePipeManager:pipeDidConnect:]_block_invoke.782.cold.1
+ ___53-[WPDPipeManager scalablePipeManager:pipeDidConnect:]_block_invoke.782.cold.2
+ ___53-[WPDPipeManager scalablePipeManager:pipeDidConnect:]_block_invoke.792
+ ___53-[WPDPipeManager scalablePipeManager:pipeDidConnect:]_block_invoke.796
+ ___53-[WPDPipeManager scalablePipeManager:pipeDidConnect:]_block_invoke_2.793
+ ___53-[WPDScanManager removeConflictingRequest:forClient:]_block_invoke.183
+ ___53-[WPDScanManager removeConflictingRequest:forClient:]_block_invoke.191
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.284
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.289
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.289.cold.1
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.289.cold.2
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.293
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.298
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.298.cold.1
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.304
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.304.cold.1
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.304.cold.2
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.304.cold.3
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.308
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.312
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.316
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.316.cold.1
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.322
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.334
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.339
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.339.cold.1
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.339.cold.2
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.343
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.347
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.290
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.299
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.305
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.317
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.325
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.325.cold.1
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.335
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.340
+ ___54-[WPDAdvertisingManager heySiriAdvertActiveAllDevices]_block_invoke.460
+ ___54-[WPDClient connectedDevice:withError:shouldDiscover:]_block_invoke.835
+ ___54-[WPDObjectDiscoveryManager addScanRequest:forClient:]_block_invoke.398
+ ___54-[WPDObjectDiscoveryManager addScanRequest:forClient:]_block_invoke.410
+ ___54-[WPDObjectDiscoveryManager updateClientsWithReports:]_block_invoke.270.cold.1
+ ___54-[WPDObjectDiscoveryManager updateClientsWithReports:]_block_invoke.270.cold.2
+ ___54-[WPDObjectDiscoveryManager updateClientsWithReports:]_block_invoke.270.cold.3
+ ___54-[WPDObjectDiscoveryManager updateClientsWithReports:]_block_invoke.270.cold.4
+ ___54-[WPDObjectDiscoveryManager updateClientsWithReports:]_block_invoke.282
+ ___54-[WPDObjectDiscoveryManager updateClientsWithReports:]_block_invoke.282.cold.1
+ ___54-[WPDObjectDiscoveryManager updateClientsWithReports:]_block_invoke.282.cold.2
+ ___54-[WPDObjectDiscoveryManager updateClientsWithReports:]_block_invoke.282.cold.3
+ ___54-[WPDObjectDiscoveryManager updateClientsWithReports:]_block_invoke.286
+ ___54-[WPDObjectDiscoveryManager updateClientsWithReports:]_block_invoke_2.283
+ ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.539
+ ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.542
+ ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.542.cold.1
+ ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.542.cold.10
+ ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.542.cold.2
+ ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.542.cold.3
+ ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.542.cold.4
+ ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.542.cold.5
+ ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.542.cold.6
+ ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.542.cold.7
+ ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.542.cold.8
+ ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.542.cold.9
+ ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.545
+ ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.548
+ ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.551
+ ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.554
+ ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.557
+ ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.560
+ ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.563
+ ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.567
+ ___54-[WPDScanManager clearDuplicateFilterCache:forClient:]_block_invoke.380
+ ___54-[WPDScanManager clearDuplicateFilterCache:forClient:]_block_invoke.383
+ ___55-[WPDPipeManager handleIncomingPipeData:data:dataSize:]_block_invoke.583
+ ___55-[WPDScanManager removePeripheralConnection:forClient:]_block_invoke.577
+ ___55-[WPDScanManager removePeripheralConnection:forClient:]_block_invoke.577.cold.1
+ ___55-[WPDScanManager removePeripheralConnection:forClient:]_block_invoke.577.cold.2
+ ___55-[WPDScanManager removePeripheralConnection:forClient:]_block_invoke.580
+ ___56-[WPDClient sendDataToCharacteristic:inService:forPeer:]_block_invoke.925
+ ___56-[WPDObjectDiscoveryManager changedScanOptions:Clients:]_block_invoke.330
+ ___56-[WPDScanManager centralManager:didFailToScanWithError:]_block_invoke.455
+ ___57-[WPDAdvertisingManager addAdvertisingRequest:forClient:]_block_invoke.321
+ ___57-[WPDObjectDiscoveryClient initWithXPCConnection:server:]_block_invoke.155
+ ___57-[WPDObjectDiscoveryClient initWithXPCConnection:server:]_block_invoke.155.cold.1
+ ___57-[WPDObjectDiscoveryClient initWithXPCConnection:server:]_block_invoke.155.cold.2
+ ___57-[WPDObjectDiscoveryClient initWithXPCConnection:server:]_block_invoke.159
+ ___57-[WPDObjectDiscoveryClient initWithXPCConnection:server:]_block_invoke_2.156
+ ___57-[WPDObjectDiscoveryManager removeScanRequestsForClient:]_block_invoke.418
+ ___57-[WPDScanManager removeAllPeerTrackingRequestsForClient:]_block_invoke.500
+ ___57-[WPDZoneManager addSingleZoneTrackingRequest:forClient:]_block_invoke.252
+ ___57-[WPDZoneManager addSingleZoneTrackingRequest:forClient:]_block_invoke.256
+ ___57-[WPDZoneManager unregisterZonesForClient:updateScanner:]_block_invoke.291.cold.1
+ ___57-[WPDZoneManager unregisterZonesForClient:updateScanner:]_block_invoke.297
+ ___58-[WPDAdvertisingManager advertisingRulesCBStackAdvertiser]_block_invoke.441
+ ___59-[WPDClient central:subscribed:toCharacteristic:inService:]_block_invoke.904
+ ___59-[WPDPipeManager setConnectionInitiator:forPeer:forClient:]_block_invoke.483
+ ___59-[WPDPipeManager setConnectionInitiator:forPeer:forClient:]_block_invoke.493
+ ___59-[WPDScanManager centralManager:didFindPeripheral:forType:]_block_invoke.509
+ ___59-[WPDScanManager centralManager:didLosePeripheral:forType:]_block_invoke.506
+ ___60-[WPDConnection sendDataToCharacteristic:inService:forPeer:]_block_invoke.224
+ ___60-[WPDConnection sendDataToCharacteristic:inService:forPeer:]_block_invoke.230
+ ___61+[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:]_block_invoke.153
+ ___61+[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:]_block_invoke.163
+ ___61-[WPDScanManager connectToPeripheral:fromClient:withOptions:]_block_invoke.512
+ ___61-[WPDScanManager connectToPeripheral:fromClient:withOptions:]_block_invoke.515
+ ___61-[WPDScanManager connectToPeripheral:fromClient:withOptions:]_block_invoke.524
+ ___62-[WPDClient discoverCharacteristicsAndServices:forPeripheral:]_block_invoke.912
+ ___62-[WPDPipeManager scalablePipeManager:pipeDidDisconnect:error:]_block_invoke.836
+ ___63-[WPDAdvertisingManager peripheralManager:didAddService:error:]_block_invoke.304
+ ___63-[WPDObjectDiscoveryManager updateAdvertisingOptionsWithError:]_block_invoke.193
+ ___63-[WPDObjectDiscoveryManager updateAdvertisingOptionsWithError:]_block_invoke.202
+ ___64-[WPDAdvertisingManager addCharacteristic:forService:forClient:]_block_invoke.272
+ ___64-[WPDAdvertisingManager addCharacteristic:forService:forClient:]_block_invoke.285
+ ___64-[WPDAdvertisingManager addCharacteristic:forService:forClient:]_block_invoke.294
+ ___65-[WPDClient registerWithDaemon:forProcess:machName:holdVouchers:]_block_invoke.525
+ ___65-[WPDClient shouldSubscribe:toPeer:withCharacteristic:inService:]_block_invoke.888
+ ___65-[WPDConnection peripheral:didWriteValueForCharacteristic:error:]_block_invoke.273
+ ___66-[WPDConnection peripheral:didUpdateValueForCharacteristic:error:]_block_invoke.188
+ ___66-[WPDPipeManager setPipeClientConnectionStatus:forPeer:forClient:]_block_invoke.478
+ ___66-[WPDScanManager centralManager:didFailToConnectPeripheral:error:]_block_invoke.572
+ ___67-[WPDAdvertisingManager peripheralManager:didReceiveWriteRequests:]_block_invoke.550
+ ___67-[WPDConnection getCharacteristicWithUUID:inService:forPeripheral:]_block_invoke.281
+ ___67-[WPDConnection getCharacteristicWithUUID:inService:forPeripheral:]_block_invoke_2.282
+ ___67-[WPDObjectDiscoveryClient notifyClientObjectDiscoveryStateChange:]_block_invoke.256
+ ___67-[WPDObjectDiscoveryManager centralManager:didFailToScanWithError:]_block_invoke.299.cold.1
+ ___67-[WPDObjectDiscoveryManager centralManager:didFailToScanWithError:]_block_invoke.299.cold.2
+ ___67-[WPDObjectDiscoveryManager centralManager:didFailToScanWithError:]_block_invoke.302
+ ___68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke.483.cold.1
+ ___68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke.486
+ ___68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke_2.487
+ ___68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke_2.487.cold.1
+ ___69-[WPDAdvertisingManager peripheralManagerIsReadyToUpdateSubscribers:]_block_invoke.555
+ ___71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.495
+ ___71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.502
+ ___71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.506
+ ___71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke_2.503
+ ___71-[WPDConnection peripheral:didDiscoverCharacteristicsForService:error:]_block_invoke.168
+ ___72-[WPDObjectDiscoveryManager peripheralManagerDidStartAdvertising:error:]_block_invoke.236
+ ___73-[WPDAdvertisingManager removeAdvertisingRequest:forClient:shouldUpdate:]_block_invoke.329
+ ___73-[WPDAdvertisingManager removeAdvertisingRequest:forClient:shouldUpdate:]_block_invoke.329.cold.1
+ ___74-[WPDPipeManager registerEndpoint:requireAck:requireEncryption:forClient:]_block_invoke.408
+ ___74-[WPDPipeManager registerEndpoint:requireAck:requireEncryption:forClient:]_block_invoke.415
+ ___74-[WPDScanManager removePeerTrackingRequest:checkZonesAvailable:forClient:]_block_invoke.489
+ ___74-[WPDScanManager removePeerTrackingRequest:checkZonesAvailable:forClient:]_block_invoke.495
+ ___75-[WPDObjectDiscoveryManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.244
+ ___76+[WPDManager initializeAdvDenylist:AdvAllowlist:ScanDenylist:ScanAllowlist:]_block_invoke.180
+ ___77-[WPDObjectDiscoveryManager updateReports:Peripheral:AdvertisementData:RSSI:]_block_invoke.261
+ ___77-[WPDObjectDiscoveryManager updateReports:Peripheral:AdvertisementData:RSSI:]_block_invoke.266
+ ___78-[WPDAdvertisingManager addressChangeNotificationNeeded:advertiserTypeString:]_block_invoke.561
+ ___78-[WPDConnection peripheral:didUpdateNotificationStateForCharacteristic:error:]_block_invoke.183
+ ___78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.419
+ ___78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.422
+ ___78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.429
+ ___78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.429.cold.1
+ ___78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.432
+ ___78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.442
+ ___78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.442.cold.1
+ ___78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.442.cold.2
+ ___78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.447
+ ___78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke_2.443
+ ___78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.177
+ ___78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.184
+ ___78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.184.cold.1
+ ___78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.184.cold.2
+ ___78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.184.cold.3
+ ___78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.184.cold.4
+ ___78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.184.cold.5
+ ___78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.191
+ ___79-[WPDAdvertisingManager addCharacteristic:Properties:Permissions:Service:Name:]_block_invoke.259
+ ___79-[WPDAdvertisingManager addCharacteristic:Properties:Permissions:Service:Name:]_block_invoke.265
+ ___80-[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:]_block_invoke.519
+ ___80-[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:]_block_invoke.526
+ ___81-[WPDClient updatedNotificationState:forCharacteristic:inService:withPeripheral:]_block_invoke.893
+ ___83-[WPDScanManager disconnectFromPeripheral:withSubscribedCharacteristics:forClient:]_block_invoke.529
+ ___83-[WPDScanManager disconnectFromPeripheral:withSubscribedCharacteristics:forClient:]_block_invoke.532
+ ___84-[WPDAdvertisingManager peripheralManager:central:didUnsubscribeFromCharacteristic:]_block_invoke.540
+ ____getCombinedAllowlist_block_invoke.362
+ ___block_descriptor_72_e8_32s40r48r56r64r_e30_v32?0"WPScanRequest"8Q16^B24ls32l8r40l8r48l8r56l8r64l8
+ ___block_literal_global.131
+ ___block_literal_global.138
+ ___block_literal_global.142
+ ___block_literal_global.148
+ ___block_literal_global.150
+ ___block_literal_global.154
+ ___block_literal_global.161
+ ___block_literal_global.166
+ ___block_literal_global.170
+ ___block_literal_global.175
+ ___block_literal_global.186
+ ___block_literal_global.188
+ ___block_literal_global.200
+ ___block_literal_global.215
+ ___block_literal_global.242
+ ___block_literal_global.253
+ ___block_literal_global.263
+ ___block_literal_global.291
+ ___block_literal_global.299
+ ___block_literal_global.310
+ ___block_literal_global.313
+ ___block_literal_global.317
+ ___block_literal_global.323
+ ___block_literal_global.325
+ ___block_literal_global.332
+ ___block_literal_global.333
+ ___block_literal_global.345
+ ___block_literal_global.351
+ ___block_literal_global.354
+ ___block_literal_global.357
+ ___block_literal_global.365
+ ___block_literal_global.369
+ ___block_literal_global.388
+ ___block_literal_global.390
+ ___block_literal_global.394
+ ___block_literal_global.399
+ ___block_literal_global.400
+ ___block_literal_global.402
+ ___block_literal_global.405
+ ___block_literal_global.408
+ ___block_literal_global.412
+ ___block_literal_global.418
+ ___block_literal_global.420
+ ___block_literal_global.421
+ ___block_literal_global.425
+ ___block_literal_global.430
+ ___block_literal_global.438
+ ___block_literal_global.442
+ ___block_literal_global.446
+ ___block_literal_global.449
+ ___block_literal_global.452
+ ___block_literal_global.464
+ ___block_literal_global.475
+ ___block_literal_global.480
+ ___block_literal_global.484
+ ___block_literal_global.499
+ ___block_literal_global.500
+ ___block_literal_global.501
+ ___block_literal_global.503
+ ___block_literal_global.505
+ ___block_literal_global.508
+ ___block_literal_global.511
+ ___block_literal_global.514
+ ___block_literal_global.520
+ ___block_literal_global.524
+ ___block_literal_global.526
+ ___block_literal_global.538
+ ___block_literal_global.542
+ ___block_literal_global.544
+ ___block_literal_global.547
+ ___block_literal_global.550
+ ___block_literal_global.553
+ ___block_literal_global.554
+ ___block_literal_global.556
+ ___block_literal_global.563
+ ___block_literal_global.569
+ ___block_literal_global.571
+ ___block_literal_global.574
+ ___block_literal_global.585
+ ___block_literal_global.586
+ ___block_literal_global.596
+ ___block_literal_global.600
+ ___block_literal_global.602
+ ___block_literal_global.612
+ ___block_literal_global.620
+ ___block_literal_global.631
+ ___block_literal_global.633
+ ___block_literal_global.647
+ ___block_literal_global.661
+ ___block_literal_global.667
+ ___block_literal_global.669
+ ___block_literal_global.673
+ ___block_literal_global.675
+ ___block_literal_global.680
+ ___block_literal_global.685
+ ___block_literal_global.690
+ ___block_literal_global.694
+ ___block_literal_global.701
+ ___block_literal_global.705
+ ___block_literal_global.707
+ ___block_literal_global.709
+ ___block_literal_global.711
+ ___block_literal_global.749
+ ___block_literal_global.775
+ ___block_literal_global.777
+ ___block_literal_global.784
+ ___block_literal_global.790
+ ___block_literal_global.794
+ ___block_literal_global.796
+ ___block_literal_global.798
+ ___block_literal_global.802
+ ___block_literal_global.804
+ ___block_literal_global.815
+ ___block_literal_global.826
+ ___block_literal_global.830
+ ___block_literal_global.838
+ ___block_literal_global.845
+ ___block_literal_global.846
+ ___block_literal_global.859
+ ___block_literal_global.864
+ ___block_literal_global.870
+ ___block_literal_global.872
+ ___block_literal_global.883
+ ___block_literal_global.885
+ ___block_literal_global.890
+ ___block_literal_global.895
+ ___block_literal_global.906
+ ___block_literal_global.914
+ ___block_literal_global.916
+ ___block_literal_global.927
+ ___block_literal_global.932
+ ___block_literal_global.934
+ ___block_literal_global.936
+ ___block_literal_global.938
+ ___block_literal_global.940
+ ___block_literal_global.948
+ ___block_literal_global.953
+ ___block_literal_global.958
+ ___block_literal_global.962
+ ___block_literal_global.964
+ ___block_literal_global.972
+ ___block_literal_global.974
+ ___block_literal_global.979
+ ___block_literal_global.981
+ ___block_literal_global.983
+ ___block_literal_global.985
+ ___block_literal_global.987
+ ___block_literal_global.995
+ ___block_literal_global.997
+ _objc_msgSend$heySiriElectionEndTimeNsec
+ _objc_msgSend$setHeySiriElectionEndTimeNsec:
+ _objc_msgSend$unsignedLongLongValue
- -[WPDScanManager shallStop]
- -[WPDScanManager shallStop].cold.1
- -[WPDScanManager shallStop].cold.2
- GCC_except_table166
- GCC_except_table356
- ___20-[WPDClient destroy]_block_invoke.585
- ___24+[WPDManager initialize]_block_invoke.117
- ___24-[WPDConnection dealloc]_block_invoke.119
- ___24-[WPDPipeManager update]_block_invoke.770
- ___24-[WPDScanManager update]_block_invoke.396
- ___24-[WPDScanManager update]_block_invoke.399
- ___24-[WPDScanManager update]_block_invoke.402
- ___24-[WPDScanManager update]_block_invoke.405
- ___24-[WPDZoneManager update]_block_invoke.166
- ___26-[WPDClient destroy_async]_block_invoke.591
- ___26-[WPDClient stopScanning:]_block_invoke.757
- ___27-[WPDClient tickleMachPort]_block_invoke.571
- ___27-[WPDScanManager shallStop]_block_invoke
- ___28-[WPDClient setupConnection]_block_invoke.579
- ___28-[WPDClient setupConnection]_block_invoke.579.cold.1
- ___28-[WPDClient setupConnection]_block_invoke_2.580
- ___28-[WPDaemonServer addClient:]_block_invoke.241
- ___29-[WPDClient sendTestRequest:]_block_invoke.987
- ___29-[WPDClient stopAdvertising:]_block_invoke.655
- ___29-[WPDaemonServer initClients]_block_invoke.219
- ___29-[WPDaemonServer updateState]_block_invoke.229
- ___30+[WPDClient generateStateDump]_block_invoke.468
- ___30-[WPDClient discoveredDevice:]_block_invoke.685
- ___30-[WPDClient startAdvertising:]_block_invoke.612
- ___30-[WPDaemonServer initManagers]_block_invoke.207
- ___30-[WPDaemonServer initManagers]_block_invoke.207.cold.1
- ___30-[WPDaemonServer initManagers]_block_invoke.207.cold.2
- ___31-[WPDAdvertisingManager update]_block_invoke.463
- ___31-[WPDClient createdConnection:]_block_invoke.872
- ___31-[WPDClient discoveredDevices:]_block_invoke.689
- ___31-[WPDScanManager updateScanner]_block_invoke.412
- ___31-[WPDZoneManager updateScanner]_block_invoke.221
- ___31-[WPDZoneManager updateScanner]_block_invoke.234
- ___31-[WPDaemonServer removeClient:]_block_invoke.249
- ___32-[WPDClient disconnectFromPeer:]_block_invoke.845
- ___32-[WPDClient stopScanning_async:]_block_invoke.760
- ___32-[WPDStatsManager reportPLStats]_block_invoke.207
- ___32-[WPDZoneManager exitTimerFired]_block_invoke.244
- ___32-[WPDZoneManager exitTimerFired]_block_invoke.244.cold.1
- ___32-[WPDZoneManager startExitTimer]_block_invoke.239
- ___32-[WPDaemonServer enableRanging:]_block_invoke.268
- ___33-[WPDClient anyDiscoveredDevice:]_block_invoke.692
- ___33-[WPDClient enableRanging:reply:]_block_invoke.943
- ___33-[WPDClient startScanning_async:]_block_invoke.702
- ___33-[WPDClient startScanning_async:]_block_invoke.708
- ___33-[WPDClient startScanning_async:]_block_invoke.714
- ___33-[WPDClient startScanning_async:]_block_invoke.720
- ___33-[WPDClient startScanning_async:]_block_invoke.726
- ___33-[WPDClient startScanning_async:]_block_invoke.738.cold.1
- ___33-[WPDClient startScanning_async:]_block_invoke.738.cold.2
- ___33-[WPDClient startScanning_async:]_block_invoke.744.cold.1
- ___33-[WPDClient startScanning_async:]_block_invoke.744.cold.2
- ___33-[WPDClient startScanning_async:]_block_invoke.744.cold.3
- ___33-[WPDClient startScanning_async:]_block_invoke.748
- ___33-[WPDClient startScanning_async:]_block_invoke_2.745
- ___33-[WPDPipeManager channelHasData:]_block_invoke.815
- ___33-[WPDPipeManager channelHasData:]_block_invoke.825
- ___33-[WPDPipeManager channelHasData:]_block_invoke_2.822
- ___33-[WPDScanManager updateScanRules]_block_invoke.266
- ___33-[WPDScanManager updateScanRules]_block_invoke.294
- ___33-[WPDScanManager updateScanRules]_block_invoke.300
- ___33-[WPDScanManager updateScanRules]_block_invoke.313
- ___33-[WPDScanManager updateScanRules]_block_invoke.320
- ___33-[WPDScanManager updateScanRules]_block_invoke_2.314
- ___33-[WPDScanManager updateScanRules]_block_invoke_2.323
- ___33-[WPDScanManager updateScanRules]_block_invoke_3.324
- ___33-[WPDScanManager updateScanRules]_block_invoke_4.325
- ___34-[WPDClient verifyApprovedUseCase]_block_invoke.460
- ___34-[WPDConnection sendDataToCentral]_block_invoke.233
- ___34-[WPDPipeManager sendChannelData:]_block_invoke.798
- ___35-[WPDClient stopAdvertising_async:]_block_invoke.658
- ___35-[WPDObjectDiscoveryManager update]_block_invoke.169
- ___35-[WPDScanManager addSpyScanClient:]_block_invoke.170
- ___35-[WPDaemonServer generateStateDump]_block_invoke.354
- ___35-[WPDaemonServer generateStateDump]_block_invoke.364
- ___35-[WPDaemonServer generateStateDump]_block_invoke.369
- ___35-[WPDaemonServer getClientForUUID:]_block_invoke.226
- ___36-[WPDClient disconnectedPeer:error:]_block_invoke.859
- ___36-[WPDClient disconnectedPeer:error:]_block_invoke.865
- ___36-[WPDClient startAdvertising_async:]_block_invoke.615
- ___36-[WPDClient startAdvertising_async:]_block_invoke.619
- ___36-[WPDClient startAdvertising_async:]_block_invoke.625.cold.1
- ___36-[WPDClient startAdvertising_async:]_block_invoke.625.cold.2
- ___36-[WPDClient startAdvertising_async:]_block_invoke.631.cold.1
- ___36-[WPDClient startAdvertising_async:]_block_invoke.631.cold.2
- ___36-[WPDClient startAdvertising_async:]_block_invoke.631.cold.3
- ___36-[WPDClient startAdvertising_async:]_block_invoke.635
- ___36-[WPDClient startAdvertising_async:]_block_invoke.642
- ___36-[WPDClient startAdvertising_async:]_block_invoke.650
- ___36-[WPDClient startAdvertising_async:]_block_invoke_2.632
- ___36-[WPDPipeManager sendAck:errorCode:]_block_invoke.697
- ___36-[WPDScanManager heySiriScanActive:]_block_invoke.250
- ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.217
- ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.217.cold.1
- ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.217.cold.2
- ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.217.cold.3
- ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.221
- ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.225
- ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.225.cold.1
- ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.230
- ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.230.cold.1
- ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.230.cold.2
- ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.230.cold.3
- ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.234
- ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke.242
- ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke_2.218
- ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke_2.226
- ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke_2.231
- ___36-[WPDSearchPartyAgent initSPObjects]_block_invoke_2.238
- ___36-[WPDaemonServer SetupSignalHandler]_block_invoke.161
- ___37-[WPDConnection sendDataToPeripheral]_block_invoke.253
- ___37-[WPDPipeManager pipeInfo:forClient:]_block_invoke.495
- ___37-[WPDPipeManager stream:handleEvent:]_block_invoke.520
- ___37-[WPDPipeManager stream:handleEvent:]_block_invoke.560
- ___37-[WPDPipeManager stream:handleEvent:]_block_invoke_2.557
- ___38-[WPDScanManager removeSpyScanClient:]_block_invoke.175
- ___38-[WPDaemonServer dumpDaemonStateAsync]_block_invoke.385
- ___39-[WPDClient connectToPeer:withOptions:]_block_invoke.806
- ___39-[WPDClient connectedDeviceOverLEPipe:]_block_invoke.837
- ___39-[WPDPendingCompletions addCompletion:]_block_invoke.126
- ___39-[WPDPipeManager writeDataToPipe:pipe:]_block_invoke.726
- ___40-[WPDAdvertisingManager initWithServer:]_block_invoke.195
- ___40-[WPDAdvertisingManager initWithServer:]_block_invoke.201
- ___40-[WPDClient startScanning:withDispatch:]_block_invoke.696
- ___40-[WPDScanManager assertCBDiscoveryScan:]_block_invoke.227
- ___40-[WPDScanManager assertCBDiscoveryScan:]_block_invoke.234
- ___40-[WPDSearchPartyAgent generateStateDump]_block_invoke.187
- ___41-[WPDAdvertisingManager advertisingRules]_block_invoke.408
- ___41-[WPDAdvertisingManager advertisingRules]_block_invoke.423
- ___41-[WPDAdvertisingManager advertisingRules]_block_invoke.427
- ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.341
- ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.350
- ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.359
- ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.367
- ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.373
- ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.373.cold.1
- ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.373.cold.2
- ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.377
- ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.381
- ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.381.cold.1
- ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.381.cold.2
- ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.385
- ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.389
- ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.389.cold.1
- ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.394
- ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke_2.356
- ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke_2.374
- ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke_2.382
- ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke_2.390
- ___41-[WPDState updateWithManager:Completion:]_block_invoke.128
- ___41-[WPDState updateWithManager:Completion:]_block_invoke.133
- ___41-[WPDaemonServer initWithCBStackAdaptor:]_block_invoke.175
- ___41-[WPDaemonServer initWithCBStackAdaptor:]_block_invoke.185
- ___41-[WPDaemonServer initWithCBStackAdaptor:]_block_invoke.185.cold.1
- ___41-[WPDaemonServer initWithCBStackAdaptor:]_block_invoke.185.cold.2
- ___41-[WPDaemonServer initWithCBStackAdaptor:]_block_invoke.190
- ___41-[WPDaemonServer initWithCBStackAdaptor:]_block_invoke.194
- ___42-[PipeDataTransfer generateSequenceNumber]_block_invoke.143
- ___42-[WPDClient initWithXPCConnection:server:]_block_invoke.484
- ___42-[WPDClient initWithXPCConnection:server:]_block_invoke.490
- ___42-[WPDClient initWithXPCConnection:server:]_block_invoke.490.cold.1
- ___42-[WPDClient initWithXPCConnection:server:]_block_invoke.490.cold.2
- ___42-[WPDObjectDiscoveryManager updateScanner]_block_invoke.372
- ___42-[WPDScanManager clearExistingConnections]_block_invoke.389
- ___43-[WPDScanManager addScanRequest:forClient:]_block_invoke.197
- ___43-[WPDScanManager addScanRequest:forClient:]_block_invoke.206
- ___44-[WPDAdvertisingData addAdvertisingRequest:]_block_invoke.126
- ___44-[WPDObjectDiscoveryClient sendTestRequest:]_block_invoke.256
- ___44-[WPDObjectDiscoveryClient startSPBeaconing]_block_invoke.203
- ___44-[WPDObjectDiscoveryClient stopAdvertising:]_block_invoke.236
- ___44-[WPDObjectDiscoveryClient stopAdvertising:]_block_invoke.245
- ___44-[WPDObjectDiscoveryManager updateScanRules]_block_invoke.332
- ___44-[WPDObjectDiscoveryManager updateScanRules]_block_invoke.365
- ___44-[WPDPendingCompletions completeID:success:]_block_invoke.131
- ___44-[WPDPipeManager receivedAck:data:dataSize:]_block_invoke.644
- ___44-[WPDPipeManager receivedAck:data:dataSize:]_block_invoke.665
- ___44-[WPDPipeManager receivedAck:data:dataSize:]_block_invoke.669
- ___44-[WPDPipeManager receivedAck:data:dataSize:]_block_invoke_2.666
- ___44-[WPDSearchPartyAgent updateTestBeaconKeys:]_block_invoke.280
- ___44-[WPDZoneManager unregisterZones:forClient:]_block_invoke.274
- ___45-[WPDAdvertisingManager heySiriAdvertActive:]_block_invoke.452
- ___45-[WPDClient clearDuplicateFilterCache_async:]_block_invoke.774
- ___45-[WPDObjectDiscoveryClient generateStateDump]_block_invoke.165
- ___45-[WPDObjectDiscoveryClient startAdvertising:]_block_invoke.212
- ___45-[WPDObjectDiscoveryClient startAdvertising:]_block_invoke.219
- ___45-[WPDObjectDiscoveryClient startAdvertising:]_block_invoke.225
- ___45-[WPDObjectDiscoveryClient updateSPBeaconing]_block_invoke.197
- ___45-[WPDObjectDiscoveryManager addScanStopTimer]_block_invoke.425
- ___45-[WPDObjectDiscoveryManager addScanStopTimer]_block_invoke.425.cold.1
- ___45-[WPDPipeManager invalidatePipeInfo:forPeer:]_block_invoke.838
- ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.425
- ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.433
- ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.437
- ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.443
- ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.447
- ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.454
- ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.458
- ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.462
- ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke.469
- ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke_2.451
- ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke_2.455
- ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke_2.459
- ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke_2.466
- ___45-[WPDPipeManager sendData:forPeer:forClient:]_block_invoke_2.470
- ___45-[WPDPipeManager sendRemainingData:wpClient:]_block_invoke.711
- ___45-[WPDScanManager reconcileScanRule:withRule:]_block_invoke.255
- ___45-[WPDScanManager reconcileScanRule:withRule:]_block_invoke.255.cold.1
- ___45-[WPDScanManager reconcileScanRule:withRule:]_block_invoke.255.cold.2
- ___45-[WPDScanManager reconcileScanRule:withRule:]_block_invoke.260
- ___45-[WPDSearchPartyAgent rollKeysWithRequestID:]_block_invoke.250
- ___45-[WPDSearchPartyAgent rollKeysWithRequestID:]_block_invoke.250.cold.1
- ___45-[WPDSearchPartyAgent rollKeysWithRequestID:]_block_invoke.250.cold.2
- ___45-[WPDSearchPartyAgent rollKeysWithRequestID:]_block_invoke.250.cold.3
- ___45-[WPDSearchPartyAgent rollKeysWithRequestID:]_block_invoke.250.cold.4
- ___45-[WPDSearchPartyAgent rollKeysWithRequestID:]_block_invoke.257
- ___46+[WPDSearchPartyAgent spBeaconKeyFromTestKey:]_block_invoke.304
- ___46-[WPDConnection peripheral:didModifyServices:]_block_invoke.190
- ___46-[WPDPipeManager receivedError:data:dataSize:]_block_invoke.677
- ___46-[WPDPipeManager receivedError:data:dataSize:]_block_invoke.686
- ___46-[WPDScanManager removeScanRequest:forClient:]_block_invoke.214
- ___47-[WPDPipeManager unregisterEndpoint:forClient:]_block_invoke.417
- ___48-[WPDAdvertisingManager removeServiceForClient:]_block_invoke.296
- ___48-[WPDClient advertisingStoppedOfType:withError:]_block_invoke.675
- ___48-[WPDClient notifyClientStateChange:Restricted:]_block_invoke.680
- ___48-[WPDConnection peripheral:didDiscoverServices:]_block_invoke.152
- ___48-[WPDConnection peripheral:didDiscoverServices:]_block_invoke.159
- ___48-[WPDConnection peripheral:didDiscoverServices:]_block_invoke.159.cold.1
- ___48-[WPDConnection peripheral:didDiscoverServices:]_block_invoke.159.cold.2
- ___48-[WPDConnection peripheral:didDiscoverServices:]_block_invoke_2.160
- ___48-[WPDObjectDiscoveryClient updateSPNearbyTokens]_block_invoke.179
- ___48-[WPDObjectDiscoveryManager cancelScanStopTimer]_block_invoke.420
- ___48-[WPDObjectDiscoveryManager updateNearbyTokens:]_block_invoke.304
- ___48-[WPDObjectDiscoveryManager updateNearbyTokens:]_block_invoke.313
- ___48-[WPDPipeManager receivedPayload:data:dataSize:]_block_invoke.596
- ___48-[WPDPipeManager receivedPayload:data:dataSize:]_block_invoke.629.cold.1
- ___48-[WPDPipeManager receivedPayload:data:dataSize:]_block_invoke.633
- ___48-[WPDPipeManager receivedPayload:data:dataSize:]_block_invoke_2.630
- ___49-[WPDAdvertisingManager enableRanging:forClient:]_block_invoke.306
- ___49-[WPDScanManager scanOptionsChanged:ForRequests:]_block_invoke.339
- ___49-[WPDScanManager scanOptionsChanged:ForRequests:]_block_invoke.342
- ___49-[WPDScanManager scanOptionsChanged:ForRequests:]_block_invoke.345
- ___49-[WPDScanManager scanOptionsChanged:ForRequests:]_block_invoke.348
- ___49-[WPDScanManager scanOptionsChanged:ForRequests:]_block_invoke.351
- ___50-[WPDObjectDiscoveryManager advertOptionsChanged:]_block_invoke.180
- ___50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.194
- ___50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.194.cold.1
- ___50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.194.cold.2
- ___50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.194.cold.3
- ___50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.194.cold.4
- ___50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.194.cold.5
- ___50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.194.cold.6
- ___50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.194.cold.7
- ___50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.194.cold.8
- ___50-[WPDZoneManager centralManager:didLoseZone:mask:]_block_invoke.194.cold.9
- ___51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.465
- ___51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.471
- ___51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.474
- ___51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.477
- ___51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.483
- ___51-[WPDZoneManager addZoneTrackingRequest:forClient:]_block_invoke.262
- ___51-[WPDZoneManager addZoneTrackingRequest:forClient:]_block_invoke.269
- ___52-[WPDPipeManager receivedVersionInfo:data:dataSize:]_block_invoke.585
- ___53-[WPDPipeManager scalablePipeManager:pipeDidConnect:]_block_invoke.779
- ___53-[WPDPipeManager scalablePipeManager:pipeDidConnect:]_block_invoke.779.cold.1
- ___53-[WPDPipeManager scalablePipeManager:pipeDidConnect:]_block_invoke.779.cold.2
- ___53-[WPDPipeManager scalablePipeManager:pipeDidConnect:]_block_invoke.783
- ___53-[WPDPipeManager scalablePipeManager:pipeDidConnect:]_block_invoke.793
- ___53-[WPDPipeManager scalablePipeManager:pipeDidConnect:]_block_invoke_2.790
- ___53-[WPDScanManager removeConflictingRequest:forClient:]_block_invoke.180
- ___53-[WPDScanManager removeConflictingRequest:forClient:]_block_invoke.185
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.281
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.286
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.286.cold.1
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.286.cold.2
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.290
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.295
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.295.cold.1
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.301
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.301.cold.1
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.301.cold.2
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.301.cold.3
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.305
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.309
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.313
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.313.cold.1
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.319
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.328
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.336
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.336.cold.1
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.336.cold.2
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.340
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.344
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.287
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.296
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.302
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.314
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.322
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.322.cold.1
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.332
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.337
- ___54-[WPDAdvertisingManager heySiriAdvertActiveAllDevices]_block_invoke.457
- ___54-[WPDClient connectedDevice:withError:shouldDiscover:]_block_invoke.826
- ___54-[WPDObjectDiscoveryManager addScanRequest:forClient:]_block_invoke.395
- ___54-[WPDObjectDiscoveryManager addScanRequest:forClient:]_block_invoke.401
- ___54-[WPDObjectDiscoveryManager updateClientsWithReports:]_block_invoke.267
- ___54-[WPDObjectDiscoveryManager updateClientsWithReports:]_block_invoke.267.cold.1
- ___54-[WPDObjectDiscoveryManager updateClientsWithReports:]_block_invoke.267.cold.2
- ___54-[WPDObjectDiscoveryManager updateClientsWithReports:]_block_invoke.267.cold.3
- ___54-[WPDObjectDiscoveryManager updateClientsWithReports:]_block_invoke.267.cold.4
- ___54-[WPDObjectDiscoveryManager updateClientsWithReports:]_block_invoke.279.cold.1
- ___54-[WPDObjectDiscoveryManager updateClientsWithReports:]_block_invoke.279.cold.2
- ___54-[WPDObjectDiscoveryManager updateClientsWithReports:]_block_invoke.279.cold.3
- ___54-[WPDObjectDiscoveryManager updateClientsWithReports:]_block_invoke.283
- ___54-[WPDObjectDiscoveryManager updateClientsWithReports:]_block_invoke_2.280
- ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.538
- ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.541
- ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.541.cold.1
- ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.541.cold.10
- ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.541.cold.2
- ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.541.cold.3
- ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.541.cold.4
- ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.541.cold.5
- ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.541.cold.6
- ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.541.cold.7
- ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.541.cold.8
- ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.541.cold.9
- ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.544
- ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.547
- ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.550
- ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.553
- ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.556
- ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.559
- ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.562
- ___54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.566
- ___54-[WPDScanManager clearDuplicateFilterCache:forClient:]_block_invoke.376
- ___54-[WPDScanManager clearDuplicateFilterCache:forClient:]_block_invoke.379
- ___55-[WPDPipeManager handleIncomingPipeData:data:dataSize:]_block_invoke.571
- ___55-[WPDScanManager removePeripheralConnection:forClient:]_block_invoke.576
- ___55-[WPDScanManager removePeripheralConnection:forClient:]_block_invoke.576.cold.1
- ___55-[WPDScanManager removePeripheralConnection:forClient:]_block_invoke.576.cold.2
- ___55-[WPDScanManager removePeripheralConnection:forClient:]_block_invoke.579
- ___56-[WPDClient sendDataToCharacteristic:inService:forPeer:]_block_invoke.916
- ___56-[WPDObjectDiscoveryManager changedScanOptions:Clients:]_block_invoke.327
- ___56-[WPDScanManager centralManager:didFailToScanWithError:]_block_invoke.454
- ___57-[WPDAdvertisingManager addAdvertisingRequest:forClient:]_block_invoke.318
- ___57-[WPDObjectDiscoveryClient initWithXPCConnection:server:]_block_invoke.152
- ___57-[WPDObjectDiscoveryClient initWithXPCConnection:server:]_block_invoke.152.cold.1
- ___57-[WPDObjectDiscoveryClient initWithXPCConnection:server:]_block_invoke.152.cold.2
- ___57-[WPDObjectDiscoveryClient initWithXPCConnection:server:]_block_invoke.156
- ___57-[WPDObjectDiscoveryClient initWithXPCConnection:server:]_block_invoke_2.153
- ___57-[WPDObjectDiscoveryManager removeScanRequestsForClient:]_block_invoke.412
- ___57-[WPDScanManager removeAllPeerTrackingRequestsForClient:]_block_invoke.499
- ___57-[WPDZoneManager addSingleZoneTrackingRequest:forClient:]_block_invoke.249
- ___57-[WPDZoneManager addSingleZoneTrackingRequest:forClient:]_block_invoke.253
- ___57-[WPDZoneManager unregisterZonesForClient:updateScanner:]_block_invoke.285
- ___57-[WPDZoneManager unregisterZonesForClient:updateScanner:]_block_invoke.288.cold.1
- ___58-[WPDAdvertisingManager advertisingRulesCBStackAdvertiser]_block_invoke.432
- ___59-[WPDClient central:subscribed:toCharacteristic:inService:]_block_invoke.895
- ___59-[WPDPipeManager setConnectionInitiator:forPeer:forClient:]_block_invoke.480
- ___59-[WPDPipeManager setConnectionInitiator:forPeer:forClient:]_block_invoke.484
- ___59-[WPDScanManager centralManager:didFindPeripheral:forType:]_block_invoke.508
- ___59-[WPDScanManager centralManager:didLosePeripheral:forType:]_block_invoke.505
- ___60-[WPDConnection sendDataToCharacteristic:inService:forPeer:]_block_invoke.215
- ___60-[WPDConnection sendDataToCharacteristic:inService:forPeer:]_block_invoke.227
- ___61+[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:]_block_invoke.141
- ___61+[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:]_block_invoke.157
- ___61-[WPDScanManager connectToPeripheral:fromClient:withOptions:]_block_invoke.511
- ___61-[WPDScanManager connectToPeripheral:fromClient:withOptions:]_block_invoke.514
- ___61-[WPDScanManager connectToPeripheral:fromClient:withOptions:]_block_invoke.523
- ___62-[WPDClient discoverCharacteristicsAndServices:forPeripheral:]_block_invoke.909
- ___62-[WPDPipeManager scalablePipeManager:pipeDidDisconnect:error:]_block_invoke.830
- ___63-[WPDAdvertisingManager peripheralManager:didAddService:error:]_block_invoke.301
- ___63-[WPDObjectDiscoveryManager updateAdvertisingOptionsWithError:]_block_invoke.190
- ___63-[WPDObjectDiscoveryManager updateAdvertisingOptionsWithError:]_block_invoke.199
- ___64-[WPDAdvertisingManager addCharacteristic:forService:forClient:]_block_invoke.269
- ___64-[WPDAdvertisingManager addCharacteristic:forService:forClient:]_block_invoke.279
- ___64-[WPDAdvertisingManager addCharacteristic:forService:forClient:]_block_invoke.288
- ___65-[WPDClient registerWithDaemon:forProcess:machName:holdVouchers:]_block_invoke.516
- ___65-[WPDClient shouldSubscribe:toPeer:withCharacteristic:inService:]_block_invoke.885
- ___65-[WPDConnection peripheral:didWriteValueForCharacteristic:error:]_block_invoke.267
- ___66-[WPDConnection peripheral:didUpdateValueForCharacteristic:error:]_block_invoke.185
- ___66-[WPDPipeManager setPipeClientConnectionStatus:forPeer:forClient:]_block_invoke.475
- ___66-[WPDScanManager centralManager:didFailToConnectPeripheral:error:]_block_invoke.571
- ___67-[WPDAdvertisingManager peripheralManager:didReceiveWriteRequests:]_block_invoke.544
- ___67-[WPDConnection getCharacteristicWithUUID:inService:forPeripheral:]_block_invoke.275
- ___67-[WPDConnection getCharacteristicWithUUID:inService:forPeripheral:]_block_invoke_2.279
- ___67-[WPDObjectDiscoveryClient notifyClientObjectDiscoveryStateChange:]_block_invoke.253
- ___67-[WPDObjectDiscoveryManager centralManager:didFailToScanWithError:]_block_invoke.293
- ___67-[WPDObjectDiscoveryManager centralManager:didFailToScanWithError:]_block_invoke.296.cold.1
- ___67-[WPDObjectDiscoveryManager centralManager:didFailToScanWithError:]_block_invoke.296.cold.2
- ___68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke.474
- ___68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke.480.cold.1
- ___68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke_2.484
- ___68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke_2.484.cold.1
- ___69-[WPDAdvertisingManager peripheralManagerIsReadyToUpdateSubscribers:]_block_invoke.552
- ___71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.489
- ___71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.496
- ___71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.503
- ___71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke_2.500
- ___71-[WPDConnection peripheral:didDiscoverCharacteristicsForService:error:]_block_invoke.165
- ___72-[WPDObjectDiscoveryManager peripheralManagerDidStartAdvertising:error:]_block_invoke.227
- ___73-[WPDAdvertisingManager removeAdvertisingRequest:forClient:shouldUpdate:]_block_invoke.326
- ___73-[WPDAdvertisingManager removeAdvertisingRequest:forClient:shouldUpdate:]_block_invoke.326.cold.1
- ___74-[WPDPipeManager registerEndpoint:requireAck:requireEncryption:forClient:]_block_invoke.402
- ___74-[WPDPipeManager registerEndpoint:requireAck:requireEncryption:forClient:]_block_invoke.412
- ___74-[WPDScanManager removePeerTrackingRequest:checkZonesAvailable:forClient:]_block_invoke.488
- ___74-[WPDScanManager removePeerTrackingRequest:checkZonesAvailable:forClient:]_block_invoke.494
- ___75-[WPDObjectDiscoveryManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.238
- ___76+[WPDManager initializeAdvDenylist:AdvAllowlist:ScanDenylist:ScanAllowlist:]_block_invoke.177
- ___77-[WPDObjectDiscoveryManager updateReports:Peripheral:AdvertisementData:RSSI:]_block_invoke.255
- ___77-[WPDObjectDiscoveryManager updateReports:Peripheral:AdvertisementData:RSSI:]_block_invoke.263
- ___78-[WPDAdvertisingManager addressChangeNotificationNeeded:advertiserTypeString:]_block_invoke.558
- ___78-[WPDConnection peripheral:didUpdateNotificationStateForCharacteristic:error:]_block_invoke.180
- ___78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.417
- ___78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.420
- ___78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.427
- ___78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.427.cold.1
- ___78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.430
- ___78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.441
- ___78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.441.cold.1
- ___78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.441.cold.2
- ___78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.446
- ___78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke_2.442
- ___78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.174
- ___78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.178
- ___78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.181.cold.1
- ___78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.181.cold.2
- ___78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.181.cold.3
- ___78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.181.cold.4
- ___78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.181.cold.5
- ___78-[WPDZoneManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.185
- ___79-[WPDAdvertisingManager addCharacteristic:Properties:Permissions:Service:Name:]_block_invoke.256
- ___79-[WPDAdvertisingManager addCharacteristic:Properties:Permissions:Service:Name:]_block_invoke.262
- ___80-[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:]_block_invoke.510
- ___80-[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:]_block_invoke.520
- ___81-[WPDClient updatedNotificationState:forCharacteristic:inService:withPeripheral:]_block_invoke.890
- ___83-[WPDScanManager disconnectFromPeripheral:withSubscribedCharacteristics:forClient:]_block_invoke.528
- ___83-[WPDScanManager disconnectFromPeripheral:withSubscribedCharacteristics:forClient:]_block_invoke.531
- ___84-[WPDAdvertisingManager peripheralManager:central:didUnsubscribeFromCharacteristic:]_block_invoke.528
- ____getCombinedAllowlist_block_invoke.356
- ___block_descriptor_64_e8_32s40r48r56r_e30_v32?0"WPScanRequest"8Q16^B24ls32l8r40l8r48l8r56l8
- ___block_literal_global.118
- ___block_literal_global.119
- ___block_literal_global.135
- ___block_literal_global.137
- ___block_literal_global.145
- ___block_literal_global.147
- ___block_literal_global.151
- ___block_literal_global.153
- ___block_literal_global.160
- ___block_literal_global.164
- ___block_literal_global.169
- ___block_literal_global.173
- ___block_literal_global.178
- ___block_literal_global.189
- ___block_literal_global.194
- ___block_literal_global.206
- ___block_literal_global.221
- ___block_literal_global.248
- ___block_literal_global.259
- ___block_literal_global.266
- ___block_literal_global.300
- ___block_literal_global.302
- ___block_literal_global.312
- ___block_literal_global.315
- ___block_literal_global.322
- ___block_literal_global.330
- ___block_literal_global.338
- ___block_literal_global.339
- ___block_literal_global.341
- ___block_literal_global.344
- ___block_literal_global.347
- ___block_literal_global.353
- ___block_literal_global.356
- ___block_literal_global.366
- ___block_literal_global.371
- ___block_literal_global.373
- ___block_literal_global.375
- ___block_literal_global.376
- ___block_literal_global.378
- ___block_literal_global.381
- ___block_literal_global.384
- ___block_literal_global.389
- ___block_literal_global.391
- ___block_literal_global.396
- ___block_literal_global.397
- ___block_literal_global.398
- ___block_literal_global.401
- ___block_literal_global.403
- ___block_literal_global.426
- ___block_literal_global.439
- ___block_literal_global.444
- ___block_literal_global.451
- ___block_literal_global.453
- ___block_literal_global.458
- ___block_literal_global.467
- ___block_literal_global.472
- ___block_literal_global.481
- ___block_literal_global.487
- ___block_literal_global.490
- ___block_literal_global.496
- ___block_literal_global.502
- ___block_literal_global.504
- ___block_literal_global.507
- ___block_literal_global.509
- ___block_literal_global.510
- ___block_literal_global.513
- ___block_literal_global.519
- ___block_literal_global.527
- ___block_literal_global.535
- ___block_literal_global.551
- ___block_literal_global.557
- ___block_literal_global.561
- ___block_literal_global.564
- ___block_literal_global.570
- ___block_literal_global.575
- ___block_literal_global.583
- ___block_literal_global.584
- ___block_literal_global.595
- ___block_literal_global.597
- ___block_literal_global.599
- ___block_literal_global.609
- ___block_literal_global.611
- ___block_literal_global.621
- ___block_literal_global.632
- ___block_literal_global.634
- ___block_literal_global.654
- ___block_literal_global.664
- ___block_literal_global.668
- ___block_literal_global.670
- ___block_literal_global.672
- ___block_literal_global.676
- ___block_literal_global.684
- ___block_literal_global.688
- ___block_literal_global.695
- ___block_literal_global.696
- ___block_literal_global.704
- ___block_literal_global.706
- ___block_literal_global.708
- ___block_literal_global.710
- ___block_literal_global.747
- ___block_literal_global.769
- ___block_literal_global.773
- ___block_literal_global.778
- ___block_literal_global.787
- ___block_literal_global.789
- ___block_literal_global.793
- ___block_literal_global.797
- ___block_literal_global.799
- ___block_literal_global.801
- ___block_literal_global.808
- ___block_literal_global.824
- ___block_literal_global.825
- ___block_literal_global.829
- ___block_literal_global.836
- ___block_literal_global.844
- ___block_literal_global.855
- ___block_literal_global.867
- ___block_literal_global.869
- ___block_literal_global.871
- ___block_literal_global.882
- ___block_literal_global.884
- ___block_literal_global.889
- ___block_literal_global.894
- ___block_literal_global.908
- ___block_literal_global.913
- ___block_literal_global.915
- ___block_literal_global.929
- ___block_literal_global.931
- ___block_literal_global.933
- ___block_literal_global.935
- ___block_literal_global.937
- ___block_literal_global.945
- ___block_literal_global.950
- ___block_literal_global.955
- ___block_literal_global.959
- ___block_literal_global.961
- ___block_literal_global.969
- ___block_literal_global.971
- ___block_literal_global.976
- ___block_literal_global.978
- ___block_literal_global.980
- ___block_literal_global.982
- ___block_literal_global.984
- ___block_literal_global.986
- ___block_literal_global.994
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$shallStop
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x9
CStrings:
+ "ProximityServiceAccessorySetup"
+ "T@\"NSNumber\",&,V_heySiriElectionEndTimeNsec"
+ "ThirdPartyAudioSwitching"
+ "WPDaemon iOS 26.4 (23E5207i) (WirelessProximity-194.22.1.1.1) (Release) built on 2026-02-05 21:41:24"
+ "_heySiriElectionEndTimeNsec"
+ "heySiriElectionEndTimeNsec"
+ "kHeySiriElectionEndTimeNsec"
+ "setHeySiriElectionEndTimeNsec:"
+ "unsignedLongLongValue"
- "%1"
- "WPDScanManager shall call stopScan:%d"
- "WPDaemon iOS 26.3 (23D118) (WirelessProximity-193.9) (Release) built on 2026-01-26 23:09:16"
- "shallStop"

```
