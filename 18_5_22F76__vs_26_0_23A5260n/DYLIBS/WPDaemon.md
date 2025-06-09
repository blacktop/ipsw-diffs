## WPDaemon

> `/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon`

```diff

-185.7.0.0.0
-  __TEXT.__text: 0x5b0f8
+190.40.1.2.0
+  __TEXT.__text: 0x5de7c
   __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_methlist: 0x41bc
-  __TEXT.__cstring: 0x3fbf
+  __TEXT.__objc_methlist: 0x4294
+  __TEXT.__cstring: 0x4499
   __TEXT.__const: 0x218
-  __TEXT.__oslogstring: 0xa5f4
-  __TEXT.__gcc_except_tab: 0x169c
-  __TEXT.__unwind_info: 0x1d88
-  __TEXT.__objc_classname: 0x377
-  __TEXT.__objc_methname: 0x9a08
-  __TEXT.__objc_methtype: 0x162d
-  __TEXT.__objc_stubs: 0x7b40
-  __DATA_CONST.__got: 0x470
-  __DATA_CONST.__const: 0x1100
+  __TEXT.__oslogstring: 0xa8ad
+  __TEXT.__gcc_except_tab: 0x16dc
+  __TEXT.__unwind_info: 0x1e60
+  __TEXT.__objc_classname: 0x37a
+  __TEXT.__objc_methname: 0x9f2c
+  __TEXT.__objc_methtype: 0x1680
+  __TEXT.__objc_stubs: 0x7f20
+  __DATA_CONST.__got: 0x488
+  __DATA_CONST.__const: 0x1260
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x25c0
+  __DATA_CONST.__objc_selrefs: 0x26d8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x2b8
   __AUTH_CONST.__auth_got: 0x478
-  __AUTH_CONST.__const: 0x6680
-  __AUTH_CONST.__cfstring: 0x33a0
-  __AUTH_CONST.__objc_const: 0x82c0
-  __AUTH_CONST.__objc_intobj: 0x108
+  __AUTH_CONST.__const: 0x6920
+  __AUTH_CONST.__cfstring: 0x33c0
+  __AUTH_CONST.__objc_const: 0x8498
+  __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x4f8
+  __DATA.__objc_ivar: 0x51c
   __DATA.__data: 0x600
   __DATA.__bss: 0x4
   __DATA_DIRTY.__objc_data: 0x820

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4AB3532C-99C6-359B-B9DF-B7B39A0CC0A8
-  Functions: 3328
-  Symbols:   9825
-  CStrings:  3893
+  UUID: 9E48E532-3F8B-37C1-A031-DD3EDF8CBC9F
+  Functions: 3402
+  Symbols:   10028
+  CStrings:  4002
 
Symbols:
+ -[WPAdvertisingRequest advertisingRandomData]
+ -[WPAdvertisingRequest setAdvertisingRandomData:]
+ -[WPDAdvertisingData advDataPerType]
+ -[WPDAdvertisingManager advertisingRulesCBStackAdvertiser]
+ -[WPDAdvertisingManager advertisingRulesCBStackAdvertiser].cold.1
+ -[WPDAdvertisingManager advertisingRulesCBStackAdvertiser].cold.2
+ -[WPDAdvertisingManager advertisingRulesCBStackAdvertiser].cold.3
+ -[WPDAdvertisingManager advertisingRulesCBStackAdvertiser].cold.4
+ -[WPDAdvertisingManager advertisingRules].cold.6
+ -[WPDAdvertisingManager advertisingRules].cold.7
+ -[WPDAdvertisingManager isAdvPermittedDuringHeySiriForType:]
+ -[WPDAdvertisingManager setWPDaemonAdvDataFrom:]
+ -[WPDAdvertisingManager setWPDaemonAdvDataFromWPAdvertisingRequest:]
+ -[WPDAdvertisingManager setupStackAdvertiser:]
+ -[WPDAdvertisingManager updateAdvertiser].cold.10
+ -[WPDAdvertisingManager updateAdvertiser].cold.6
+ -[WPDAdvertisingManager updateAdvertiser].cold.7
+ -[WPDAdvertisingManager updateAdvertiser].cold.8
+ -[WPDAdvertisingManager updateAdvertiser].cold.9
+ -[WPDClient copyWithZone:]
+ -[WPDClient startScanning:withDispatch:]
+ -[WPDClient startScanning:withDispatch:].cold.1
+ -[WPDClient startScanning:withDispatch:].cold.2
+ -[WPDaemonServer initWithCBStackAdaptor:]
+ -[WPDaemonServer initWithCBStackAdaptor:].cold.1
+ -[WPDaemonServer initWithCBStackAdaptor:].cold.2
+ -[WPDaemonServer initWithCBStackAdaptor:].cold.3
+ -[WPDaemonServer initWithCBStackAdaptor:].cold.4
+ -[WPDaemonServer initWithCBStackAdaptor:].cold.5
+ -[WPDaemonServer initWithCBStackAdaptor:].cold.6
+ -[WPDaemonServer initWithCBStackAdaptor:].cold.7
+ -[WPDaemonServer screenDimmedChangeNotifyToken]
+ -[WPDaemonServer screenDisplayChangedNotifyToken]
+ -[WPDaemonServer screenUndimmedChangeNotifyToken]
+ -[WPDaemonServer setScreenDimmedChangeNotifyToken:]
+ -[WPDaemonServer setScreenDisplayChangedNotifyToken:]
+ -[WPDaemonServer setScreenUndimmedChangeNotifyToken:]
+ -[WPDaemonServer stackAdaptor]
+ GCC_except_table102
+ GCC_except_table107
+ GCC_except_table114
+ GCC_except_table117
+ GCC_except_table118
+ GCC_except_table128
+ GCC_except_table135
+ GCC_except_table144
+ GCC_except_table172
+ GCC_except_table237
+ GCC_except_table241
+ GCC_except_table27
+ GCC_except_table271
+ GCC_except_table383
+ GCC_except_table401
+ GCC_except_table408
+ GCC_except_table415
+ GCC_except_table442
+ GCC_except_table445
+ GCC_except_table451
+ GCC_except_table458
+ GCC_except_table488
+ GCC_except_table571
+ GCC_except_table62
+ GCC_except_table67
+ GCC_except_table76
+ _CBCentralManagerScanOptionReport127dBm
+ _CBCentralManagerScanOptionReport27dBm
+ _OBJC_CLASS_$_CBWPDaemonAdvertisingData
+ _OBJC_IVAR_$_WPAdvertisingRequest._advertisingRandomData
+ _OBJC_IVAR_$_WPDAdvertisingData._advDataPerType
+ _OBJC_IVAR_$_WPDAdvertisingManager._advStackAdaptor
+ _OBJC_IVAR_$_WPDAdvertisingManager._clientStackAdvertisers
+ _OBJC_IVAR_$_WPDAdvertisingManager._heySiriAdvEnabled
+ _OBJC_IVAR_$_WPDaemonServer._screenDimmedChangeNotifyToken
+ _OBJC_IVAR_$_WPDaemonServer._screenDisplayChangedNotifyToken
+ _OBJC_IVAR_$_WPDaemonServer._screenUndimmedChangeNotifyToken
+ _OBJC_IVAR_$_WPDaemonServer._stackAdaptor
+ ___28-[WPDaemonServer addClient:]_block_invoke.241
+ ___28-[WPDaemonServer addClient:]_block_invoke.244
+ ___29-[WPDaemonServer initClients]_block_invoke.219
+ ___29-[WPDaemonServer updateState]_block_invoke.229
+ ___29-[WPDaemonServer updateState]_block_invoke.232
+ ___30-[WPDaemonServer initManagers]_block_invoke.207
+ ___30-[WPDaemonServer initManagers]_block_invoke.207.cold.1
+ ___30-[WPDaemonServer initManagers]_block_invoke.207.cold.2
+ ___31-[WPDAdvertisingManager update]_block_invoke.463
+ ___31-[WPDAdvertisingManager update]_block_invoke.466
+ ___31-[WPDAdvertisingManager update]_block_invoke.469
+ ___31-[WPDaemonServer removeClient:]_block_invoke.249
+ ___31-[WPDaemonServer removeClient:]_block_invoke.252
+ ___31-[WPDaemonServer removeClient:]_block_invoke.255
+ ___31-[WPDaemonServer removeClient:]_block_invoke.258
+ ___32-[WPDaemonServer enableRanging:]_block_invoke.268
+ ___35-[WPDaemonServer generateStateDump]_block_invoke.354
+ ___35-[WPDaemonServer generateStateDump]_block_invoke.357
+ ___35-[WPDaemonServer generateStateDump]_block_invoke.360
+ ___35-[WPDaemonServer generateStateDump]_block_invoke.364
+ ___35-[WPDaemonServer generateStateDump]_block_invoke.369
+ ___35-[WPDaemonServer generateStateDump]_block_invoke.372
+ ___35-[WPDaemonServer generateStateDump]_block_invoke.375
+ ___35-[WPDaemonServer generateStateDump]_block_invoke.378
+ ___35-[WPDaemonServer getClientForUUID:]_block_invoke.226
+ ___38-[WPDaemonServer dumpDaemonStateAsync]_block_invoke.385
+ ___40-[WPDClient startScanning:withDispatch:]_block_invoke
+ ___40-[WPDClient startScanning:withDispatch:]_block_invoke.693
+ ___41-[WPDAdvertisingManager advertisingRules]_block_invoke.408
+ ___41-[WPDAdvertisingManager advertisingRules]_block_invoke.411
+ ___41-[WPDAdvertisingManager advertisingRules]_block_invoke.423
+ ___41-[WPDAdvertisingManager advertisingRules]_block_invoke.427
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.341
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.344
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.350
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.353
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.359
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.362
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.365
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.367
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.373
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.373.cold.1
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.373.cold.2
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.377
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.381
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.381.cold.1
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.381.cold.2
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.385
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.389
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.389.cold.1
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.394
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke_2
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke_2.356
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke_2.374
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke_2.382
+ ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke_2.390
+ ___41-[WPDaemonServer initWithCBStackAdaptor:]_block_invoke
+ ___41-[WPDaemonServer initWithCBStackAdaptor:]_block_invoke.175
+ ___41-[WPDaemonServer initWithCBStackAdaptor:]_block_invoke.185
+ ___41-[WPDaemonServer initWithCBStackAdaptor:]_block_invoke.185.cold.1
+ ___41-[WPDaemonServer initWithCBStackAdaptor:]_block_invoke.185.cold.2
+ ___41-[WPDaemonServer initWithCBStackAdaptor:]_block_invoke.190
+ ___41-[WPDaemonServer initWithCBStackAdaptor:]_block_invoke.194
+ ___41-[WPDaemonServer initWithCBStackAdaptor:]_block_invoke_2
+ ___44-[WPDAdvertisingData addAdvertisingRequest:]_block_invoke.126
+ ___45-[WPDAdvertisingManager heySiriAdvertActive:]_block_invoke.452
+ ___46-[WPDAdvertisingManager setupStackAdvertiser:]_block_invoke
+ ___46-[WPDAdvertisingManager setupStackAdvertiser:]_block_invoke_2
+ ___46-[WPDAdvertisingManager setupStackAdvertiser:]_block_invoke_3
+ ___46-[WPDAdvertisingManager setupStackAdvertiser:]_block_invoke_4
+ ___46-[WPDAdvertisingManager setupStackAdvertiser:]_block_invoke_5
+ ___48-[WPDAdvertisingManager removeServiceForClient:]_block_invoke.296
+ ___49-[WPDAdvertisingManager enableRanging:forClient:]_block_invoke.306
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.281
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.286
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.286.cold.1
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.286.cold.2
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.290
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.295
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.295.cold.1
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.301
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.301.cold.1
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.301.cold.2
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.301.cold.3
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.309
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.313
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.313.cold.1
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.319
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.328
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.331
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.336
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.336.cold.1
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.336.cold.2
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.340
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.344
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.287
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.302
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.314
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.322
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.322.cold.1
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.332
+ ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.337
+ ___54-[WPDAdvertisingManager heySiriAdvertActiveAllDevices]_block_invoke.457
+ ___57-[WPDAdvertisingManager addAdvertisingRequest:forClient:]_block_invoke.318
+ ___58-[WPDAdvertisingManager advertisingRulesCBStackAdvertiser]_block_invoke
+ ___58-[WPDAdvertisingManager advertisingRulesCBStackAdvertiser]_block_invoke.432
+ ___58-[WPDAdvertisingManager advertisingRulesCBStackAdvertiser]_block_invoke.435
+ ___58-[WPDAdvertisingManager advertisingRulesCBStackAdvertiser]_block_invoke.438
+ ___63-[WPDAdvertisingManager peripheralManager:didAddService:error:]_block_invoke.301
+ ___64-[WPDAdvertisingManager addCharacteristic:forService:forClient:]_block_invoke.269
+ ___64-[WPDAdvertisingManager addCharacteristic:forService:forClient:]_block_invoke.279
+ ___64-[WPDAdvertisingManager addCharacteristic:forService:forClient:]_block_invoke.282
+ ___64-[WPDAdvertisingManager addCharacteristic:forService:forClient:]_block_invoke.288
+ ___64-[WPDAdvertisingManager addCharacteristic:forService:forClient:]_block_invoke.291
+ ___67-[WPDAdvertisingManager peripheralManager:didReceiveWriteRequests:]_block_invoke.544
+ ___67-[WPDAdvertisingManager peripheralManager:didReceiveWriteRequests:]_block_invoke.547
+ ___68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke.474
+ ___68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke.477
+ ___68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke.480
+ ___68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke.480.cold.1
+ ___68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke.483
+ ___68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke_2.484
+ ___68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke_2.484.cold.1
+ ___69-[WPDAdvertisingManager peripheralManagerIsReadyToUpdateSubscribers:]_block_invoke.552
+ ___71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.489
+ ___71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.492
+ ___71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.496
+ ___71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.499
+ ___71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.503
+ ___71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke_2.500
+ ___73-[WPDAdvertisingManager removeAdvertisingRequest:forClient:shouldUpdate:]_block_invoke.326
+ ___73-[WPDAdvertisingManager removeAdvertisingRequest:forClient:shouldUpdate:]_block_invoke.326.cold.1
+ ___78-[WPDAdvertisingManager addressChangeNotificationNeeded:advertiserTypeString:]_block_invoke.558
+ ___79-[WPDAdvertisingManager addCharacteristic:Properties:Permissions:Service:Name:]_block_invoke.256
+ ___79-[WPDAdvertisingManager addCharacteristic:Properties:Permissions:Service:Name:]_block_invoke.262
+ ___80-[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:]_block_invoke.510
+ ___80-[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:]_block_invoke.513
+ ___80-[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:]_block_invoke.516
+ ___80-[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:]_block_invoke.520
+ ___80-[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:]_block_invoke.523
+ ___84-[WPDAdvertisingManager peripheralManager:central:didUnsubscribeFromCharacteristic:]_block_invoke.528
+ ___84-[WPDAdvertisingManager peripheralManager:central:didUnsubscribeFromCharacteristic:]_block_invoke.531
+ ___84-[WPDAdvertisingManager peripheralManager:central:didUnsubscribeFromCharacteristic:]_block_invoke.534
+ ___84-[WPDAdvertisingManager peripheralManager:central:didUnsubscribeFromCharacteristic:]_block_invoke.537
+ ___block_descriptor_32_e54_v32?0"NSNumber"8"CBStackBLEAdvertiserBTStack"16^B24l
+ ___block_descriptor_40_e8_32s_e15_v32?08Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e29_"CBPeripheralManager"12?0C8ls32l8
+ ___block_descriptor_40_e8_32s_e35_v32?0"NSNumber"8"NSNumber"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e54_v32?0"NSNumber"8"CBStackBLEAdvertiserBTStack"16^B24ls32l8
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0"NSError"8C16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e29_v32?0"NSDictionary"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e52_v32?0"NSNumber"8"CBWPDaemonAdvertisingData"16^B24ls32l8s40l8
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_literal_global.225
+ ___block_literal_global.267
+ ___block_literal_global.300
+ ___block_literal_global.307
+ ___block_literal_global.311
+ ___block_literal_global.314
+ ___block_literal_global.339
+ ___block_literal_global.342
+ ___block_literal_global.364
+ ___block_literal_global.366
+ ___block_literal_global.376
+ ___block_literal_global.379
+ ___block_literal_global.382
+ ___block_literal_global.396
+ ___block_literal_global.410
+ ___block_literal_global.413
+ ___block_literal_global.426
+ ___block_literal_global.431
+ ___block_literal_global.434
+ ___block_literal_global.437
+ ___block_literal_global.440
+ ___block_literal_global.465
+ ___block_literal_global.488
+ ___block_literal_global.491
+ ___block_literal_global.495
+ ___block_literal_global.512
+ ___block_literal_global.536
+ ___block_literal_global.539
+ ___block_literal_global.541
+ ___block_literal_global.551
+ ___block_literal_global.557
+ ___block_literal_global.560
+ ___block_literal_global.583
+ ___validateNearbyInfoV2RandomDataAdvertisement_block_invoke
+ ___validateShortPayloadAirPlaySourceRequest_block_invoke
+ _initWithCBStackAdaptor:.onceDToken
+ _objc_msgSend$activate
+ _objc_msgSend$advDataPerType
+ _objc_msgSend$advInstanceType
+ _objc_msgSend$advertisingRandomData
+ _objc_msgSend$advertisingRulesCBStackAdvertiser
+ _objc_msgSend$bleAdvertiserClass
+ _objc_msgSend$heySiriAdvertActiveAllDevices
+ _objc_msgSend$isAdvPermittedDuringHeySiriForType:
+ _objc_msgSend$mfgData
+ _objc_msgSend$peripheralManager:didStopAdvertisingWithError:
+ _objc_msgSend$peripheralManagerDidStartAdvertising:error:
+ _objc_msgSend$replaceObjectAtIndex:withObject:
+ _objc_msgSend$setAdvDataPerType:
+ _objc_msgSend$setAdvInstanceType:
+ _objc_msgSend$setAdvInterval:
+ _objc_msgSend$setAdvStartedHandler:
+ _objc_msgSend$setAdvStoppedHandler:
+ _objc_msgSend$setAdvertisingRandomData:
+ _objc_msgSend$setDispatchQueue:
+ _objc_msgSend$setEnableAdvertisingWithPowerAssertion:
+ _objc_msgSend$setEnableObjectLocatorResponseOnAdvertisingInstance:
+ _objc_msgSend$setListOfClients:
+ _objc_msgSend$setMfgData:
+ _objc_msgSend$setWPDaemonAdvDataFrom:
+ _objc_msgSend$setWPDaemonAdvDataFromWPAdvertisingRequest:
+ _objc_msgSend$setWiProxUpdateTimestamp:
+ _objc_msgSend$setWpDaemonData:
+ _objc_msgSend$setupStackAdvertiser:
+ _objc_msgSend$stackAdaptor
+ _objc_msgSend$startScanning:withDispatch:
+ _objc_msgSend$wpDaemonData
- -[WPDClient startScanning:].cold.1
- -[WPDClient startScanning:].cold.2
- -[WPDaemonServer init]
- -[WPDaemonServer init].cold.1
- -[WPDaemonServer init].cold.2
- -[WPDaemonServer init].cold.3
- -[WPDaemonServer init].cold.4
- -[WPDaemonServer init].cold.5
- -[WPDaemonServer init].cold.6
- -[WPDaemonServer init].cold.7
- GCC_except_table101
- GCC_except_table106
- GCC_except_table109
- GCC_except_table113
- GCC_except_table126
- GCC_except_table133
- GCC_except_table142
- GCC_except_table170
- GCC_except_table235
- GCC_except_table239
- GCC_except_table26
- GCC_except_table269
- GCC_except_table381
- GCC_except_table397
- GCC_except_table406
- GCC_except_table413
- GCC_except_table434
- GCC_except_table443
- GCC_except_table449
- GCC_except_table456
- GCC_except_table486
- GCC_except_table565
- GCC_except_table58
- GCC_except_table61
- GCC_except_table66
- GCC_except_table78
- ___22-[WPDaemonServer init]_block_invoke
- ___22-[WPDaemonServer init]_block_invoke.175
- ___22-[WPDaemonServer init]_block_invoke.181
- ___22-[WPDaemonServer init]_block_invoke.181.cold.1
- ___22-[WPDaemonServer init]_block_invoke.181.cold.2
- ___22-[WPDaemonServer init]_block_invoke.186
- ___22-[WPDaemonServer init]_block_invoke.190
- ___22-[WPDaemonServer init]_block_invoke_2
- ___27-[WPDClient startScanning:]_block_invoke
- ___27-[WPDClient startScanning:]_block_invoke.693
- ___28-[WPDaemonServer addClient:]_block_invoke.237
- ___28-[WPDaemonServer addClient:]_block_invoke.240
- ___29-[WPDaemonServer initClients]_block_invoke.215
- ___29-[WPDaemonServer updateState]_block_invoke.225
- ___29-[WPDaemonServer updateState]_block_invoke.228
- ___30-[WPDaemonServer initManagers]_block_invoke.203
- ___30-[WPDaemonServer initManagers]_block_invoke.203.cold.1
- ___30-[WPDaemonServer initManagers]_block_invoke.203.cold.2
- ___31-[WPDAdvertisingManager update]_block_invoke.404
- ___31-[WPDAdvertisingManager update]_block_invoke.407
- ___31-[WPDAdvertisingManager update]_block_invoke.410
- ___31-[WPDaemonServer removeClient:]_block_invoke.245
- ___31-[WPDaemonServer removeClient:]_block_invoke.248
- ___31-[WPDaemonServer removeClient:]_block_invoke.251
- ___31-[WPDaemonServer removeClient:]_block_invoke.254
- ___32-[WPDaemonServer enableRanging:]_block_invoke.264
- ___35-[WPDaemonServer generateStateDump]_block_invoke.328
- ___35-[WPDaemonServer generateStateDump]_block_invoke.331
- ___35-[WPDaemonServer generateStateDump]_block_invoke.334
- ___35-[WPDaemonServer generateStateDump]_block_invoke.338
- ___35-[WPDaemonServer generateStateDump]_block_invoke.343
- ___35-[WPDaemonServer generateStateDump]_block_invoke.346
- ___35-[WPDaemonServer generateStateDump]_block_invoke.349
- ___35-[WPDaemonServer generateStateDump]_block_invoke.352
- ___35-[WPDaemonServer getClientForUUID:]_block_invoke.222
- ___38-[WPDaemonServer dumpDaemonStateAsync]_block_invoke.359
- ___41-[WPDAdvertisingManager advertisingRules]_block_invoke.360
- ___41-[WPDAdvertisingManager advertisingRules]_block_invoke.363
- ___41-[WPDAdvertisingManager advertisingRules]_block_invoke.375
- ___41-[WPDAdvertisingManager advertisingRules]_block_invoke.379
- ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.336
- ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.339
- ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.342
- ___41-[WPDAdvertisingManager updateAdvertiser]_block_invoke.345
- ___44-[WPDAdvertisingData addAdvertisingRequest:]_block_invoke.125
- ___45-[WPDAdvertisingManager heySiriAdvertActive:]_block_invoke.393
- ___48-[WPDAdvertisingManager removeServiceForClient:]_block_invoke.294
- ___49-[WPDAdvertisingManager enableRanging:forClient:]_block_invoke.304
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.276
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.283
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.287
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.287.cold.1
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.293
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.302
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.310
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.310.cold.1
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.310.cold.2
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.314
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.318
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke.cold.3
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.288
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.296.cold.1
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.306
- ___53-[WPDaemonServer registerForSpringboardNotifications]_block_invoke_2.311
- ___54-[WPDAdvertisingManager heySiriAdvertActiveAllDevices]_block_invoke.398
- ___57-[WPDAdvertisingManager addAdvertisingRequest:forClient:]_block_invoke.316
- ___63-[WPDAdvertisingManager peripheralManager:didAddService:error:]_block_invoke.299
- ___64-[WPDAdvertisingManager addCharacteristic:forService:forClient:]_block_invoke.267
- ___64-[WPDAdvertisingManager addCharacteristic:forService:forClient:]_block_invoke.277
- ___64-[WPDAdvertisingManager addCharacteristic:forService:forClient:]_block_invoke.280
- ___64-[WPDAdvertisingManager addCharacteristic:forService:forClient:]_block_invoke.286
- ___64-[WPDAdvertisingManager addCharacteristic:forService:forClient:]_block_invoke.289
- ___67-[WPDAdvertisingManager peripheralManager:didReceiveWriteRequests:]_block_invoke.485
- ___67-[WPDAdvertisingManager peripheralManager:didReceiveWriteRequests:]_block_invoke.488
- ___68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke.415
- ___68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke.418
- ___68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke.421
- ___68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke.421.cold.1
- ___68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke.424
- ___68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke_2.425
- ___68-[WPDAdvertisingManager peripheralManagerDidStartAdvertising:error:]_block_invoke_2.425.cold.1
- ___69-[WPDAdvertisingManager peripheralManagerIsReadyToUpdateSubscribers:]_block_invoke.493
- ___71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.430
- ___71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.433
- ___71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.437
- ___71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.440
- ___71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke.444
- ___71-[WPDAdvertisingManager peripheralManager:didStopAdvertisingWithError:]_block_invoke_2.441
- ___73-[WPDAdvertisingManager removeAdvertisingRequest:forClient:shouldUpdate:]_block_invoke.324
- ___73-[WPDAdvertisingManager removeAdvertisingRequest:forClient:shouldUpdate:]_block_invoke.324.cold.1
- ___78-[WPDAdvertisingManager addressChangeNotificationNeeded:advertiserTypeString:]_block_invoke.499
- ___79-[WPDAdvertisingManager addCharacteristic:Properties:Permissions:Service:Name:]_block_invoke.254
- ___79-[WPDAdvertisingManager addCharacteristic:Properties:Permissions:Service:Name:]_block_invoke.260
- ___80-[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:]_block_invoke.451
- ___80-[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:]_block_invoke.454
- ___80-[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:]_block_invoke.457
- ___80-[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:]_block_invoke.461
- ___80-[WPDAdvertisingManager peripheralManager:central:didSubscribeToCharacteristic:]_block_invoke.464
- ___84-[WPDAdvertisingManager peripheralManager:central:didUnsubscribeFromCharacteristic:]_block_invoke.469
- ___84-[WPDAdvertisingManager peripheralManager:central:didUnsubscribeFromCharacteristic:]_block_invoke.472
- ___84-[WPDAdvertisingManager peripheralManager:central:didUnsubscribeFromCharacteristic:]_block_invoke.475
- ___84-[WPDAdvertisingManager peripheralManager:central:didUnsubscribeFromCharacteristic:]_block_invoke.478
- ___block_literal_global.188
- ___block_literal_global.242
- ___block_literal_global.253
- ___block_literal_global.256
- ___block_literal_global.263
- ___block_literal_global.291
- ___block_literal_global.313
- ___block_literal_global.333
- ___block_literal_global.335
- ___block_literal_global.336
- ___block_literal_global.345
- ___block_literal_global.351
- ___block_literal_global.354
- ___block_literal_global.365
- ___block_literal_global.400
- ___block_literal_global.412
- ___block_literal_global.420
- ___block_literal_global.423
- ___block_literal_global.436
- ___block_literal_global.450
- ___block_literal_global.463
- ___block_literal_global.466
- ___block_literal_global.480
- ___block_literal_global.484
- ___block_literal_global.501
- ___block_literal_global.503
- ___block_literal_global.524
- _init.onceDToken
CStrings:
+ "#"
+ "@\"<CBStackAdaptor>\""
+ "@\"CBPeripheralManager\"12@?0C8"
+ "AdvertisingRulesCBStackAdvertiser - advertising rules: %@"
+ "AirPlaySource old: %@, new: %@"
+ "BluetoothFeatures"
+ "DOD"
+ "DOS"
+ "FindMyPair"
+ "FindMyTemporaryAggressiveLegacyExtendedRange"
+ "IOHIDEvent_AlwaysOnDisplay"
+ "InternalTestAdvWithHigherPower"
+ "InternalTestAdvWithHigherPowerServiceDataConnectable"
+ "InternalTestAdvWithHigherPowerServiceDataNonConnectable"
+ "InternalTestAdvWithHigherPowerServiceDataS2"
+ "InternalTestAdvWithHigherPowerServiceDataS8"
+ "InternalTestDiscoveryScanCodedPHY"
+ "InternalTestDiscoveryScanWithMRC"
+ "InternalTestScanLowDutyCycleMCOnly"
+ "InternalTestUUIDScanWithMinRSSI"
+ "InternalTestUUIDScanWithMinRSSIMediumLow"
+ "MoveAdvConsolidation"
+ "NearbyFaceTime"
+ "NearbyFaceTimeData"
+ "NearbyInfoV2 rd: %@, payload: %@, valid: %d"
+ "ProximityServiceDeviceSetup"
+ "Requesting to start advertising for client type %{public}@ with %{public}@"
+ "Requesting to stop advertising for client type %{public}@"
+ "SOSBeaconActivateAdvA"
+ "SOSBeaconActivateAdvB"
+ "SOSBeaconActivateScan"
+ "SOSBeaconPartA"
+ "SOSBeaconPartB"
+ "SOSBeaconPrecisionFindRequest"
+ "SOSBeaconPrecisionFindResponse"
+ "SOSBeaconScan"
+ "Screen already dimmed - SpringBoard"
+ "Screen already undimmed - SpringBoard"
+ "Screen dimmed - SpringBoard"
+ "Screen state - %s - IOHIDEvent"
+ "Screen undimmed - SpringBoard"
+ "SharingHomePodSetup"
+ "Stop all advertisings internally"
+ "T@\"<CBStackAdaptor>\",R,N,V_stackAdaptor"
+ "T@\"NSData\",&,N,V_advertisingRandomData"
+ "T@\"NSMutableDictionary\",R,V_advDataPerType"
+ "Ti,N,V_screenDimmedChangeNotifyToken"
+ "Ti,N,V_screenDisplayChangedNotifyToken"
+ "Ti,N,V_screenUndimmedChangeNotifyToken"
+ "WPDaemon iOS 26.0 (23A5260g) (WirelessProximity-190.40.1.2) (Release) built on 2025-05-30 20:32:25"
+ "WiproxDaemonDirect"
+ "[3@\"CBStackBLEAdvertiserBTStack\"]"
+ "_advDataPerType"
+ "_advStackAdaptor"
+ "_advertisingRandomData"
+ "_clientStackAdvertisers"
+ "_heySiriAdvEnabled"
+ "_screenDimmedChangeNotifyToken"
+ "_screenDisplayChangedNotifyToken"
+ "_screenUndimmedChangeNotifyToken"
+ "_stackAdaptor"
+ "advDataPerType"
+ "advInstanceType"
+ "advertising request of type %ld, priority %ld, UseFG %ld (%.2f ms), data %@, connectable %d, addr change %d, options %@, advertisementRequestedAt %llu, randomData %@"
+ "advertisingRandomData"
+ "advertisingRulesCBStackAdvertiser"
+ "bleAdvertiserClass"
+ "com.apple.iokit.hid.displayStatus"
+ "com.apple.springboardservices.eventobserver.internalSBSEventObserverEventDimmed"
+ "com.apple.springboardservices.eventobserver.internalSBSEventObserverEventUndimmed"
+ "initWithCBStackAdaptor:"
+ "isAdvPermittedDuringHeySiriForType:"
+ "kAdvertisingRandomData"
+ "mfgData"
+ "replaceObjectAtIndex:withObject:"
+ "screenDimmedChangeNotifyToken"
+ "screenDisplayChangedNotifyToken"
+ "screenUndimmedChangeNotifyToken"
+ "setAdvDataPerType:"
+ "setAdvInstanceType:"
+ "setAdvInterval:"
+ "setAdvStartedHandler:"
+ "setAdvStoppedHandler:"
+ "setAdvertisingRandomData:"
+ "setDispatchQueue:"
+ "setEnableAdvertisingWithPowerAssertion:"
+ "setEnableObjectLocatorResponseOnAdvertisingInstance:"
+ "setListOfClients:"
+ "setMfgData:"
+ "setScreenDimmedChangeNotifyToken:"
+ "setScreenDisplayChangedNotifyToken:"
+ "setScreenUndimmedChangeNotifyToken:"
+ "setWPDaemonAdvDataFrom:"
+ "setWPDaemonAdvDataFromWPAdvertisingRequest:"
+ "setWiProxUpdateTimestamp:"
+ "setWpDaemonData:"
+ "setupStackAdvertiser:"
+ "stackAdaptor"
+ "startScanning:withDispatch:"
+ "v20@?0@\"NSError\"8C16"
+ "v28@0:8@\"WPScanRequest\"16B24"
+ "v32@?0@\"NSNumber\"8@\"CBStackBLEAdvertiserBTStack\"16^B24"
+ "v32@?0@\"NSNumber\"8@\"CBWPDaemonAdvertisingData\"16^B24"
+ "v32@?0@\"NSNumber\"8@\"NSNumber\"16^B24"
+ "wpDaemonData"
+ "wpDaemonData advInstance %d has data, stop advertising"
+ "wpDaemonData advInstance %d has no data, stop advertising"
+ "wpDaemonData advInstance %d has same data, skip updating"
+ "wpDaemonData advInstance %d request updating mfg data %@"
- "WPDaemon iOS 18.5 (22F65) (WirelessProximity-185.7) (Release) built on 2025-04-22 20:30:13"
- "advertising request of type %ld, priority %ld, UseFG %ld (%.2f ms), data %@, connectable %d, addr change %d, options %@, advertisementRequestedAt %llu"

```
