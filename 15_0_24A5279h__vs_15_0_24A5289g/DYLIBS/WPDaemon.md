## WPDaemon

> `/System/Library/PrivateFrameworks/WPDaemon.framework/Versions/A/WPDaemon`

```diff

-180.51.4.0.0
-  __TEXT.__text: 0x57fd0
+180.53.2.0.0
+  __TEXT.__text: 0x57e60
   __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_methlist: 0x3544
+  __TEXT.__objc_methlist: 0x3514
   __TEXT.__cstring: 0x3bd2
   __TEXT.__const: 0x1c8
-  __TEXT.__oslogstring: 0x957b
-  __TEXT.__gcc_except_tab: 0x14ec
+  __TEXT.__oslogstring: 0x9537
+  __TEXT.__gcc_except_tab: 0x14e0
   __TEXT.__unwind_info: 0x1558
   __TEXT.__objc_classname: 0x35c
-  __TEXT.__objc_methname: 0x92f2
+  __TEXT.__objc_methname: 0x9280
   __TEXT.__objc_methtype: 0x15b6
-  __TEXT.__objc_stubs: 0x73a0
+  __TEXT.__objc_stubs: 0x7380
   __DATA_CONST.__got: 0x418
   __DATA_CONST.__const: 0x280
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2338
+  __DATA_CONST.__objc_selrefs: 0x2318
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x2b8
   __AUTH_CONST.__auth_got: 0x340
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x6cb0
+  __AUTH_CONST.__const: 0x6c70
   __AUTH_CONST.__cfstring: 0x3160
-  __AUTH_CONST.__objc_const: 0x8fa8
+  __AUTH_CONST.__objc_const: 0x8f48
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x4b0
+  __DATA.__objc_ivar: 0x4a8
   __DATA.__data: 0x5a0
   __DATA.__bss: 0x7c
   __DATA_DIRTY.__objc_data: 0x730

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2376
-  Symbols:   5239
+  Functions: 2370
+  Symbols:   5228
   CStrings:  593
 
Symbols:
+ GCC_except_table105
+ GCC_except_table179
+ GCC_except_table67
+ GCC_except_table87
+ GCC_except_table89
+ __24-[WPDScanManager update]_block_invoke.382
+ __31-[WPDScanManager updateScanner]_block_invoke.396
+ __31-[WPDZoneManager updateScanner]_block_invoke.230
+ __32-[WPDZoneManager exitTimerFired]_block_invoke.241
+ __32-[WPDZoneManager startExitTimer]_block_invoke.233
+ __33-[WPDScanManager updateScanRules]_block_invoke.262
+ __33-[WPDScanManager updateScanRules]_block_invoke.279
+ __33-[WPDScanManager updateScanRules]_block_invoke.285
+ __33-[WPDScanManager updateScanRules]_block_invoke.292
+ __33-[WPDScanManager updateScanRules]_block_invoke.296
+ __33-[WPDScanManager updateScanRules]_block_invoke.300
+ __33-[WPDScanManager updateScanRules]_block_invoke_2.301
+ __33-[WPDScanManager updateScanRules]_block_invoke_3.302
+ __42-[WPDScanManager clearExistingConnections]_block_invoke.375
+ __44-[WPDZoneManager unregisterZones:forClient:]_block_invoke.273
+ __49-[WPDScanManager scanOptionsChanged:ForRequests:]_block_invoke.318
+ __49-[WPDScanManager startTrackingPeripheral:ofType:]_block_invoke.496
+ __51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.454
+ __51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.460
+ __51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.472
+ __51-[WPDZoneManager addZoneTrackingRequest:forClient:]_block_invoke.261
+ __51-[WPDZoneManager addZoneTrackingRequest:forClient:]_block_invoke.268
+ __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.543
+ __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.546.cold.1
+ __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.571
+ __54-[WPDScanManager clearDuplicateFilterCache:forClient:]_block_invoke.362
+ __54-[WPDScanManager logScanTypes:method:window:interval:]_block_invoke.357
+ __55-[WPDScanManager removePeripheralConnection:forClient:]_block_invoke.583
+ __56-[WPDScanManager centralManager:didFailToScanWithError:]_block_invoke.443
+ __57-[WPDScanManager logScanRequests:method:window:interval:]_block_invoke.351
+ __57-[WPDScanManager removeAllPeerTrackingRequestsForClient:]_block_invoke.488
+ __57-[WPDZoneManager addSingleZoneTrackingRequest:forClient:]_block_invoke.248
+ __57-[WPDZoneManager addSingleZoneTrackingRequest:forClient:]_block_invoke.252
+ __57-[WPDZoneManager unregisterZonesForClient:updateScanner:]_block_invoke.284
+ __59-[WPDScanManager centralManager:didFindPeripheral:forType:]_block_invoke.512
+ __59-[WPDScanManager centralManager:didLosePeripheral:forType:]_block_invoke.507
+ __61-[WPDScanManager connectToPeripheral:fromClient:withOptions:]_block_invoke.515
+ __61-[WPDScanManager connectToPeripheral:fromClient:withOptions:]_block_invoke.522
+ __61-[WPDScanManager connectToPeripheral:fromClient:withOptions:]_block_invoke.528
+ __66-[WPDScanManager centralManager:didFailToConnectPeripheral:error:]_block_invoke.578
+ __74-[WPDScanManager removePeerTrackingRequest:checkZonesAvailable:forClient:]_block_invoke.477
+ __74-[WPDScanManager removePeerTrackingRequest:checkZonesAvailable:forClient:]_block_invoke.483
+ __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.401
+ __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.411
+ __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.425
+ __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.425.cold.1
+ __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.429
+ __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.435
+ __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke_2.426
+ __83-[WPDScanManager disconnectFromPeripheral:withSubscribedCharacteristics:forClient:]_block_invoke.533
+ __block_literal_global.283
+ __block_literal_global.294
+ __block_literal_global.320
+ __block_literal_global.353
+ __block_literal_global.359
+ __block_literal_global.372
+ __block_literal_global.395
+ __block_literal_global.400
+ __block_literal_global.428
+ __block_literal_global.442
+ __block_literal_global.447
+ __block_literal_global.449
+ __block_literal_global.462
+ __block_literal_global.504
+ __block_literal_global.506
+ __block_literal_global.524
+ __block_literal_global.532
+ __block_literal_global.542
- -[WPDaemonServer gazeChangeToken]
- -[WPDaemonServer onHead]
- -[WPDaemonServer setGazeChangeToken:]
- -[WPDaemonServer setOnHead:]
- GCC_except_table106
- GCC_except_table180
- GCC_except_table281
- GCC_except_table86
- GCC_except_table90
- OBJC_IVAR_$_WPDaemonServer._gazeChangeToken
- OBJC_IVAR_$_WPDaemonServer._onHead
- __24-[WPDScanManager update]_block_invoke.394
- __31-[WPDScanManager updateScanner]_block_invoke.399
- __31-[WPDZoneManager updateScanner]_block_invoke.229
- __31-[WPDZoneManager updateScanner]_block_invoke.233
- __32-[WPDZoneManager exitTimerFired]_block_invoke.244
- __32-[WPDZoneManager startExitTimer]_block_invoke.239
- __33-[WPDScanManager updateScanRules]_block_invoke.261
- __33-[WPDScanManager updateScanRules]_block_invoke.277
- __33-[WPDScanManager updateScanRules]_block_invoke.282
- __33-[WPDScanManager updateScanRules]_block_invoke.291
- __33-[WPDScanManager updateScanRules]_block_invoke.298
- __33-[WPDScanManager updateScanRules]_block_invoke.302
- __33-[WPDScanManager updateScanRules]_block_invoke.303
- __33-[WPDScanManager updateScanRules]_block_invoke_2.304
- __33-[WPDScanManager updateScanRules]_block_invoke_3.305
- __42-[WPDScanManager clearExistingConnections]_block_invoke.378
- __44-[WPDZoneManager unregisterZones:forClient:]_block_invoke.282
- __49-[WPDScanManager scanOptionsChanged:ForRequests:]_block_invoke.336
- __49-[WPDScanManager startTrackingPeripheral:ofType:]_block_invoke.499
- __51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.457
- __51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.469
- __51-[WPDScanManager addPeerTrackingRequest:forClient:]_block_invoke.475
- __51-[WPDZoneManager addZoneTrackingRequest:forClient:]_block_invoke.264
- __51-[WPDZoneManager addZoneTrackingRequest:forClient:]_block_invoke.271
- __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.549.cold.1
- __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.570
- __54-[WPDScanManager centralManager:didConnectPeripheral:]_block_invoke.574
- __54-[WPDScanManager clearDuplicateFilterCache:forClient:]_block_invoke.368
- __54-[WPDScanManager logScanTypes:method:window:interval:]_block_invoke.360
- __55-[WPDScanManager removePeripheralConnection:forClient:]_block_invoke.589
- __56-[WPDScanManager centralManager:didFailToScanWithError:]_block_invoke.446
- __57-[WPDScanManager logScanRequests:method:window:interval:]_block_invoke.354
- __57-[WPDScanManager removeAllPeerTrackingRequestsForClient:]_block_invoke.491
- __57-[WPDZoneManager addSingleZoneTrackingRequest:forClient:]_block_invoke.251
- __57-[WPDZoneManager addSingleZoneTrackingRequest:forClient:]_block_invoke.255
- __57-[WPDZoneManager unregisterZonesForClient:updateScanner:]_block_invoke.296
- __59-[WPDScanManager centralManager:didFindPeripheral:forType:]_block_invoke.515
- __59-[WPDScanManager centralManager:didLosePeripheral:forType:]_block_invoke.510
- __61-[WPDScanManager connectToPeripheral:fromClient:withOptions:]_block_invoke.521
- __61-[WPDScanManager connectToPeripheral:fromClient:withOptions:]_block_invoke.525
- __61-[WPDScanManager connectToPeripheral:fromClient:withOptions:]_block_invoke.531
- __66-[WPDScanManager centralManager:didFailToConnectPeripheral:error:]_block_invoke.581
- __74-[WPDScanManager removePeerTrackingRequest:checkZonesAvailable:forClient:]_block_invoke.480
- __74-[WPDScanManager removePeerTrackingRequest:checkZonesAvailable:forClient:]_block_invoke.486
- __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.407
- __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.417
- __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.428
- __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.428.cold.1
- __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.432
- __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke.438
- __78-[WPDScanManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:]_block_invoke_2.429
- __83-[WPDScanManager disconnectFromPeripheral:withSubscribedCharacteristics:forClient:]_block_invoke.539
- __block_literal_global.246
- __block_literal_global.279
- __block_literal_global.301
- __block_literal_global.307
- __block_literal_global.356
- __block_literal_global.362
- __block_literal_global.373
- __block_literal_global.375
- __block_literal_global.380
- __block_literal_global.396
- __block_literal_global.434
- __block_literal_global.448
- __block_literal_global.450
- __block_literal_global.452
- __block_literal_global.477
- __block_literal_global.482
- __block_literal_global.488
- __block_literal_global.501
- __block_literal_global.507
- __block_literal_global.520
- __block_literal_global.527
- __block_literal_global.533
- __block_literal_global.541
- __block_literal_global.572
- __block_literal_global.583
- __block_literal_global.591
- _objc_msgSend$onHead
CStrings:
+ "WPDaemon macOS 15.0 (24A5287a) (WirelessProximity-180.53.2) (Release) built on 2024-06-28 22:25:32"
- "WPDaemon macOS 15.0 (24A5276a) (WirelessProximity-180.51.4) (Release) built on 2024-06-15 00:27:36"

```
