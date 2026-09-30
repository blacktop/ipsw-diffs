## WirelessProximity

> `/System/Library/PrivateFrameworks/WirelessProximity.framework/WirelessProximity`

```diff

-193.9.0.0.0
-  __TEXT.__text: 0x31efc
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x29bc
+194.22.1.1.1
+  __TEXT.__text: 0x32864
+  __TEXT.__auth_stubs: 0x550
+  __TEXT.__objc_methlist: 0x29dc
   __TEXT.__const: 0x2f0
-  __TEXT.__cstring: 0x3666
-  __TEXT.__oslogstring: 0x4500
-  __TEXT.__gcc_except_tab: 0x688
-  __TEXT.__unwind_info: 0x1400
-  __TEXT.__objc_classname: 0x1c9
-  __TEXT.__objc_methname: 0x5389
+  __TEXT.__cstring: 0x36d7
+  __TEXT.__oslogstring: 0x452a
+  __TEXT.__gcc_except_tab: 0x638
+  __TEXT.__unwind_info: 0x1440
+  __TEXT.__objc_classname: 0x1ca
+  __TEXT.__objc_methname: 0x540b
   __TEXT.__objc_methtype: 0xe1e
-  __TEXT.__objc_stubs: 0x4440
+  __TEXT.__objc_stubs: 0x4460
   __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x728
+  __DATA_CONST.__const: 0x730
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15e8
+  __DATA_CONST.__objc_selrefs: 0x15f8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xb8
-  __AUTH_CONST.__auth_got: 0x2e8
+  __AUTH_CONST.__auth_got: 0x2b8
   __AUTH_CONST.__const: 0x3440
-  __AUTH_CONST.__cfstring: 0x2ac0
-  __AUTH_CONST.__objc_const: 0x2c98
-  __AUTH_CONST.__objc_intobj: 0x1c8
+  __AUTH_CONST.__cfstring: 0x2b00
+  __AUTH_CONST.__objc_const: 0x2cc8
+  __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x1d4
+  __DATA.__objc_ivar: 0x1d8
   __DATA.__data: 0x2a8
   __DATA_DIRTY.__objc_data: 0x5f0
   __DATA_DIRTY.__bss: 0x20

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C63DDC7C-9C68-3806-AC05-397A829841D4
-  Functions: 1833
-  Symbols:   5388
-  CStrings:  2323
+  UUID: 75417F6C-4E86-348F-946A-5741B2FF1496
+  Functions: 1842
+  Symbols:   5443
+  CStrings:  2333
 
Symbols:
+ -[WPHeySiri startScanning:]
+ -[WPHeySiri startScanning:].cold.1
+ -[WPHeySiri startScanning:].cold.2
+ -[WPScanRequest heySiriElectionEndTimeNsec]
+ -[WPScanRequest setHeySiriElectionEndTimeNsec:]
+ GCC_except_table26
+ GCC_except_table28
+ GCC_except_table37
+ GCC_except_table39
+ _OBJC_IVAR_$_WPScanRequest._heySiriElectionEndTimeNsec
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _WPHeySiriElectionEndTimeNsec
+ ___22-[WPClient connection]_block_invoke.181
+ ___22-[WPClient connection]_block_invoke.181.cold.1
+ ___22-[WPClient connection]_block_invoke.185
+ ___22-[WPClient connection]_block_invoke_2.182
+ ___23-[WPClient addServices]_block_invoke.410
+ ___23-[WPClient addServices]_block_invoke_2.411
+ ___23-[WPClient addServices]_block_invoke_2.411.cold.1
+ ___23-[WPClient addServices]_block_invoke_2.411.cold.2
+ ___23-[WPTransfer startScan]_block_invoke.169
+ ___26-[WPClient enableTestMode]_block_invoke.621
+ ___26-[WPClient enableTestMode]_block_invoke.621.cold.1
+ ___26-[WPClient enableTestMode]_block_invoke.621.cold.2
+ ___26-[WPClient enableTestMode]_block_invoke_2.624
+ ___26-[WPTest sendData:toPeer:]_block_invoke.290
+ ___26-[WPTest sendData:toPeer:]_block_invoke.296
+ ___26-[WPTest sendData:toPeer:]_block_invoke.302
+ ___27-[WPClient disableScanning]_block_invoke.671
+ ___27-[WPClient disableScanning]_block_invoke.671.cold.1
+ ___27-[WPClient disableScanning]_block_invoke.671.cold.2
+ ___27-[WPClient disableScanning]_block_invoke_2.674
+ ___27-[WPClient dumpDaemonState]_block_invoke.663
+ ___27-[WPClient dumpDaemonState]_block_invoke.663.cold.1
+ ___27-[WPClient dumpDaemonState]_block_invoke.663.cold.2
+ ___27-[WPClient dumpDaemonState]_block_invoke_2.666
+ ___27-[WPClient stateDidChange:]_block_invoke.604
+ ___27-[WPHeySiri startScanning:]_block_invoke
+ ___27-[WPHeySiri startScanning:]_block_invoke.185
+ ___27-[WPRanging enableRanging:]_block_invoke.126
+ ___27-[WPTransfer receivedData:]_block_invoke.286
+ ___27-[WPTransfer receivedData:]_block_invoke.292
+ ___27-[WPTransfer receivedData:]_block_invoke.311
+ ___28-[WPClient sendTestRequest:]_block_invoke.679
+ ___28-[WPClient sendTestRequest:]_block_invoke.679.cold.1
+ ___28-[WPClient sendTestRequest:]_block_invoke.679.cold.2
+ ___28-[WPClient sendTestRequest:]_block_invoke_2.682
+ ___28-[WPNearby sendData:toPeer:]_block_invoke.357
+ ___28-[WPNearby sendData:toPeer:]_block_invoke.363
+ ___28-[WPNearby sendData:toPeer:]_block_invoke.367
+ ___29-[WPClient getPowerLogStats:]_block_invoke.653
+ ___29-[WPClient getPowerLogStats:]_block_invoke.653.cold.1
+ ___29-[WPClient getPowerLogStats:]_block_invoke.653.cold.2
+ ___29-[WPClient getPowerLogStats:]_block_invoke.659
+ ___29-[WPClient getPowerLogStats:]_block_invoke_2.656
+ ___29-[WPClient startAdvertising:]_block_invoke.439
+ ___29-[WPNearby deviceDiscovered:]_block_invoke.280
+ ___29-[WPNearby deviceDiscovered:]_block_invoke.285
+ ___29-[WPTest disconnectFromPeer:]_block_invoke.335
+ ___30-[WPClient getAllTrackedZones]_block_invoke.571
+ ___30-[WPClient getAllTrackedZones]_block_invoke.571.cold.1
+ ___30-[WPClient getAllTrackedZones]_block_invoke.571.cold.2
+ ___30-[WPClient getAllTrackedZones]_block_invoke_2.574
+ ___30-[WPClient startTrackingZone:]_block_invoke.547
+ ___30-[WPClient startTrackingZone:]_block_invoke.547.cold.1
+ ___30-[WPClient startTrackingZone:]_block_invoke.547.cold.2
+ ___30-[WPClient startTrackingZone:]_block_invoke_2.550
+ ___30-[WPClient stopTrackingZones:]_block_invoke.555
+ ___30-[WPClient stopTrackingZones:]_block_invoke.555.cold.1
+ ___30-[WPClient stopTrackingZones:]_block_invoke.555.cold.2
+ ___30-[WPClient stopTrackingZones:]_block_invoke_2.558
+ ___30-[WPContinuity connectToPeer:]_block_invoke.276
+ ___30-[WPHeySiri deviceDiscovered:]_block_invoke.228
+ ___31-[WPClient establishConnection]_block_invoke.172
+ ___31-[WPClient overrideAdvTimeout:]_block_invoke.645
+ ___31-[WPClient overrideAdvTimeout:]_block_invoke.645.cold.1
+ ___31-[WPClient overrideAdvTimeout:]_block_invoke.645.cold.2
+ ___31-[WPClient overrideAdvTimeout:]_block_invoke_2.648
+ ___31-[WPNearby disconnectFromPeer:]_block_invoke.405
+ ___31-[WPTransfer deviceDiscovered:]_block_invoke.213
+ ___32-[WPClient enableBubbleTestMode]_block_invoke.629
+ ___32-[WPClient enableBubbleTestMode]_block_invoke.629.cold.1
+ ___32-[WPClient enableBubbleTestMode]_block_invoke.629.cold.2
+ ___32-[WPClient enableBubbleTestMode]_block_invoke_2.632
+ ___32-[WPClient overrideScanTimeout:]_block_invoke.637
+ ___32-[WPClient overrideScanTimeout:]_block_invoke.637.cold.1
+ ___32-[WPClient overrideScanTimeout:]_block_invoke.637.cold.2
+ ___32-[WPClient overrideScanTimeout:]_block_invoke_2.640
+ ___32-[WPClient stopTrackingAllZones]_block_invoke.563
+ ___32-[WPClient stopTrackingAllZones]_block_invoke.563.cold.1
+ ___32-[WPClient stopTrackingAllZones]_block_invoke.563.cold.2
+ ___32-[WPClient stopTrackingAllZones]_block_invoke_2.566
+ ___32-[WPContinuity sendData:toPeer:]_block_invoke.357
+ ___32-[WPContinuity sendData:toPeer:]_block_invoke.363
+ ___32-[WPContinuity sendData:toPeer:]_block_invoke.367
+ ___33-[WPClient checkAllowDuplicates:]_block_invoke.611
+ ___33-[WPClient checkAllowDuplicates:]_block_invoke.611.cold.1
+ ___33-[WPClient checkAllowDuplicates:]_block_invoke.611.cold.2
+ ___33-[WPClient checkAllowDuplicates:]_block_invoke.617
+ ___33-[WPClient checkAllowDuplicates:]_block_invoke_2.614
+ ___33-[WPHomeKit stopScanningForType:]_block_invoke.207
+ ___35-[WPClient initWithQueue:machName:]_block_invoke.157
+ ___35-[WPContinuity disconnectFromPeer:]_block_invoke.331
+ ___36-[WPDeviceScanner deviceDiscovered:]_block_invoke.197
+ ___36-[WPTest connectToPeer:withOptions:]_block_invoke.268
+ ___38-[WPClient connectToPeer:withOptions:]_block_invoke.514
+ ___38-[WPClient connectToPeer:withOptions:]_block_invoke.514.cold.1
+ ___38-[WPClient connectToPeer:withOptions:]_block_invoke.514.cold.2
+ ___38-[WPClient connectToPeer:withOptions:]_block_invoke.527
+ ___38-[WPClient connectToPeer:withOptions:]_block_invoke_2.528
+ ___38-[WPClient connectToPeer:withOptions:]_block_invoke_2.528.cold.1
+ ___38-[WPClient connectToPeer:withOptions:]_block_invoke_2.528.cold.2
+ ___38-[WPNearby connectToPeer:withOptions:]_block_invoke.302
+ ___39-[WPContinuity initWithDelegate:queue:]_block_invoke.149
+ ___39-[WPDeviceScanner anyDiscoveredDevice:]_block_invoke.166
+ ___39-[WPTest disconnectedDevice:withError:]_block_invoke.345
+ ___41-[WPNearby disconnectedDevice:withError:]_block_invoke.413
+ ___42-[WPAWDL initWithDelegate:queue:machName:]_block_invoke.122
+ ___42-[WPClient listenToBandwidthNotifications]_block_invoke.587
+ ___42-[WPClient listenToBandwidthNotifications]_block_invoke.587.cold.1
+ ___42-[WPClient listenToBandwidthNotifications]_block_invoke.587.cold.2
+ ___42-[WPClient listenToBandwidthNotifications]_block_invoke_2.590
+ ___42-[WPHomeKit startCBDiscoveryScan:forType:]_block_invoke.242
+ ___42-[WPHomeKit startCBDiscoveryScan:forType:]_block_invoke.249
+ ___42-[WPHomeKit startCBDiscoveryScan:forType:]_block_invoke.253
+ ___42-[WPHomeKit startCBDiscoveryScan:forType:]_block_invoke.253.cold.1
+ ___42-[WPHomeKit startCBDiscoveryScan:forType:]_block_invoke_2.254
+ ___43-[WPHomeKit startScanningWithData:forType:]_block_invoke.178
+ ___43-[WPHomeKit startScanningWithData:forType:]_block_invoke.188
+ ___43-[WPHomeKit startScanningWithData:forType:]_block_invoke.197
+ ___44-[WPObjectDiscovery initWithDelegate:queue:]_block_invoke.193
+ ___45-[WPClient updateScanningRequest:withUpdate:]_block_invoke.489
+ ___45-[WPContinuity disconnectedDevice:withError:]_block_invoke.339
+ ___45-[WPPairing initWithDelegate:queue:machName:]_block_invoke.151
+ ___45-[WPTest advertisingStoppedOfType:withError:]_block_invoke.196
+ ___45-[WPTest advertisingStoppedOfType:withError:]_block_invoke.201
+ ___46-[WPHeySiri updateScanningRequest:withUpdate:]_block_invoke.199
+ ___46-[WPObjectDiscovery startScanningWithOptions:]_block_invoke.253
+ ___46-[WPZoneTracker enteredZone:manufacturerData:]_block_invoke.168
+ ___46-[WPZoneTracker enteredZone:manufacturerData:]_block_invoke.173
+ ___47-[WPNearby advertisingStoppedOfType:withError:]_block_invoke.236
+ ___48-[WPClient updateAdvertisingRequest:withUpdate:]_block_invoke.451
+ ___49-[WPHeySiri updateAdvertisingRequest:withUpdate:]_block_invoke.180
+ ___51-[WPContinuity advertisingStoppedOfType:withError:]_block_invoke.209
+ ___51-[WPObjectDiscovery startScanningWithMode:Timeout:]_block_invoke.228
+ ___51-[WPTest connectedDevice:withError:shouldDiscover:]_block_invoke.275
+ ___52-[WPMagicSwitch advertisingStoppedOfType:withError:]_block_invoke.195
+ ___53-[WPNearby connectedDevice:withError:shouldDiscover:]_block_invoke.312
+ ___54-[WPTest sentData:toEndpoint:forPeripheral:withError:]_block_invoke.309
+ ___55-[WPClient sendDataToCharacteristic:inService:forPeer:]_block_invoke.539
+ ___55-[WPTransfer connectedDevice:withError:shouldDiscover:]_block_invoke.220
+ ___55-[WPTransfer connectedDevice:withError:shouldDiscover:]_block_invoke.226
+ ___56-[WPNearby sentData:toEndpoint:forPeripheral:withError:]_block_invoke.379
+ ___56-[WPTest central:subscribed:toCharacteristic:inService:]_block_invoke.325
+ ___57-[WPContinuity connectedDevice:withError:shouldDiscover:]_block_invoke.286
+ ___58-[WPHeySiri(Test) startScanningAndAdvertisingWithOptions:]_block_invoke.290
+ ___58-[WPHeySiri(Test) startScanningAndAdvertisingWithOptions:]_block_invoke.300
+ ___58-[WPHeySiri(Test) startScanningAndAdvertisingWithOptions:]_block_invoke.303
+ ___58-[WPNearby central:subscribed:toCharacteristic:inService:]_block_invoke.395
+ ___59-[WPDeviceScanner parseCompanyData:forSize:intoDictionary:]_block_invoke.218
+ ___60-[WPAWDL startConnectionlessAWDLServiceAdvertisingWithData:]_block_invoke.151
+ ___60-[WPTest startAdvertisingOfType:data:priority:mode:options:]_block_invoke.173
+ ___60-[WPTransfer central:subscribed:toCharacteristic:inService:]_block_invoke.349
+ ___61+[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:]_block_invoke.153
+ ___61+[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:]_block_invoke.163
+ ___62-[WPContinuity central:subscribed:toCharacteristic:inService:]_block_invoke.394
+ ___62-[WPNearby startAdvertisingOfType:data:priority:mode:options:]_block_invoke.211
+ ___63-[WPNearby discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.324
+ ___63-[WPNearby discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.330
+ ___65-[WPTest receivedData:forCharacteristic:inService:forPeripheral:]_block_invoke.315
+ ___65-[WPTransfer discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.235
+ ___65-[WPTransfer discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.243
+ ___65-[WPTransfer discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.243.cold.1
+ ___65-[WPTransfer discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.247
+ ___65-[WPTransfer discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.252
+ ___67-[WPContinuity discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.298
+ ___67-[WPContinuity discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.298.cold.1
+ ___67-[WPContinuity discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.302
+ ___67-[WPContinuity discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.307
+ ___67-[WPNearby receivedData:forCharacteristic:inService:forPeripheral:]_block_invoke.385
+ ___69-[WPTransfer receivedData:forCharacteristic:inService:forPeripheral:]_block_invoke.260
+ ___69-[WPTransfer receivedData:forCharacteristic:inService:forPeripheral:]_block_invoke.270
+ ___69-[WPTransfer receivedData:forCharacteristic:inService:forPeripheral:]_block_invoke.276
+ ___71-[WPContinuity receivedData:forCharacteristic:inService:forPeripheral:]_block_invoke.382
+ ___73-[WPNearby sentData:forCharacteristic:inService:forPeripheral:withError:]_block_invoke.374
+ ___75-[WPTransfer sentData:forCharacteristic:inService:forPeripheral:withError:]_block_invoke.325
+ ___77-[WPContinuity sentData:forCharacteristic:inService:forPeripheral:withError:]_block_invoke.374
+ ___80-[WPContinuity startScanningForType:withData:mask:peers:boostedScan:duplicates:]_block_invoke.229
+ ___80-[WPNearby updatedNotificationState:forCharacteristic:inService:withPeripheral:]_block_invoke.338
+ ___80-[WPNearby updatedNotificationState:forCharacteristic:inService:withPeripheral:]_block_invoke.344
+ ___82-[WPTest startScanningForType:data:mask:peers:scanMode:rssi:duplicates:scanCache:]_block_invoke.212
+ ___84-[WPContinuity updatedNotificationState:forCharacteristic:inService:withPeripheral:]_block_invoke.315
+ ___84-[WPContinuity updatedNotificationState:forCharacteristic:inService:withPeripheral:]_block_invoke.321
+ ___96-[WPNearby startScanningForType:data:mask:peers:scanMode:rssi:duplicates:scanCache:useCaseList:]_block_invoke.252
+ ___96-[WPNearby startScanningForType:data:mask:peers:scanMode:rssi:duplicates:scanCache:useCaseList:]_block_invoke.256
+ ___block_literal_global.124
+ ___block_literal_global.125
+ ___block_literal_global.131
+ ___block_literal_global.133
+ ___block_literal_global.144
+ ___block_literal_global.145
+ ___block_literal_global.151
+ ___block_literal_global.155
+ ___block_literal_global.160
+ ___block_literal_global.170
+ ___block_literal_global.175
+ ___block_literal_global.179
+ ___block_literal_global.185
+ ___block_literal_global.198
+ ___block_literal_global.204
+ ___block_literal_global.207
+ ___block_literal_global.213
+ ___block_literal_global.215
+ ___block_literal_global.223
+ ___block_literal_global.238
+ ___block_literal_global.240
+ ___block_literal_global.245
+ ___block_literal_global.247
+ ___block_literal_global.260
+ ___block_literal_global.262
+ ___block_literal_global.270
+ ___block_literal_global.277
+ ___block_literal_global.278
+ ___block_literal_global.283
+ ___block_literal_global.288
+ ___block_literal_global.292
+ ___block_literal_global.300
+ ___block_literal_global.302
+ ___block_literal_global.309
+ ___block_literal_global.316
+ ___block_literal_global.317
+ ___block_literal_global.323
+ ___block_literal_global.327
+ ___block_literal_global.332
+ ___block_literal_global.347
+ ___block_literal_global.349
+ ___block_literal_global.351
+ ___block_literal_global.355
+ ___block_literal_global.359
+ ___block_literal_global.363
+ ___block_literal_global.365
+ ___block_literal_global.367
+ ___block_literal_global.369
+ ___block_literal_global.376
+ ___block_literal_global.389
+ ___block_literal_global.396
+ ___block_literal_global.397
+ ___block_literal_global.402
+ ___block_literal_global.407
+ ___block_literal_global.415
+ ___block_literal_global.416
+ ___block_literal_global.417
+ ___block_literal_global.422
+ ___block_literal_global.424
+ ___block_literal_global.435
+ ___block_literal_global.436
+ ___block_literal_global.441
+ ___block_literal_global.446
+ ___block_literal_global.448
+ ___block_literal_global.453
+ ___block_literal_global.455
+ ___block_literal_global.460
+ ___block_literal_global.465
+ ___block_literal_global.476
+ ___block_literal_global.481
+ ___block_literal_global.486
+ ___block_literal_global.487
+ ___block_literal_global.491
+ ___block_literal_global.493
+ ___block_literal_global.498
+ ___block_literal_global.500
+ ___block_literal_global.505
+ ___block_literal_global.507
+ ___block_literal_global.512
+ ___block_literal_global.519
+ ___block_literal_global.530
+ ___block_literal_global.532
+ ___block_literal_global.534
+ ___block_literal_global.536
+ ___block_literal_global.541
+ ___block_literal_global.552
+ ___block_literal_global.560
+ ___block_literal_global.568
+ ___block_literal_global.576
+ ___block_literal_global.578
+ ___block_literal_global.580
+ ___block_literal_global.582
+ ___block_literal_global.584
+ ___block_literal_global.592
+ ___block_literal_global.606
+ ___block_literal_global.608
+ ___block_literal_global.616
+ ___block_literal_global.626
+ ___block_literal_global.634
+ ___block_literal_global.642
+ ___block_literal_global.650
+ ___block_literal_global.658
+ ___block_literal_global.668
+ ___block_literal_global.676
+ ___block_literal_global.684
+ ___block_literal_global.686
+ ___block_literal_global.834
+ _objc_msgSend$heySiriElectionEndTimeNsec
+ _objc_msgSend$setHeySiriElectionEndTimeNsec:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x28
- -[WPHeySiri startScanning].cold.1
- -[WPHeySiri startScanning].cold.2
- GCC_except_table24
- GCC_except_table27
- GCC_except_table29
- GCC_except_table31
- GCC_except_table36
- GCC_except_table38
- GCC_except_table40
- ___22-[WPClient connection]_block_invoke.178
- ___22-[WPClient connection]_block_invoke.178.cold.1
- ___22-[WPClient connection]_block_invoke.182
- ___22-[WPClient connection]_block_invoke_2.179
- ___23-[WPClient addServices]_block_invoke.407
- ___23-[WPClient addServices]_block_invoke_2.408
- ___23-[WPClient addServices]_block_invoke_2.408.cold.1
- ___23-[WPClient addServices]_block_invoke_2.408.cold.2
- ___23-[WPTransfer startScan]_block_invoke.163
- ___26-[WPClient enableTestMode]_block_invoke.618
- ___26-[WPClient enableTestMode]_block_invoke.618.cold.1
- ___26-[WPClient enableTestMode]_block_invoke.618.cold.2
- ___26-[WPClient enableTestMode]_block_invoke_2.621
- ___26-[WPHeySiri startScanning]_block_invoke
- ___26-[WPHeySiri startScanning]_block_invoke.179
- ___26-[WPTest sendData:toPeer:]_block_invoke.287
- ___26-[WPTest sendData:toPeer:]_block_invoke.293
- ___26-[WPTest sendData:toPeer:]_block_invoke.299
- ___27-[WPClient disableScanning]_block_invoke.668
- ___27-[WPClient disableScanning]_block_invoke.668.cold.1
- ___27-[WPClient disableScanning]_block_invoke.668.cold.2
- ___27-[WPClient disableScanning]_block_invoke_2.671
- ___27-[WPClient dumpDaemonState]_block_invoke.660
- ___27-[WPClient dumpDaemonState]_block_invoke.660.cold.1
- ___27-[WPClient dumpDaemonState]_block_invoke.660.cold.2
- ___27-[WPClient dumpDaemonState]_block_invoke_2.663
- ___27-[WPClient stateDidChange:]_block_invoke.592
- ___27-[WPRanging enableRanging:]_block_invoke.123
- ___27-[WPTransfer receivedData:]_block_invoke.283
- ___27-[WPTransfer receivedData:]_block_invoke.289
- ___27-[WPTransfer receivedData:]_block_invoke.296
- ___28-[WPClient sendTestRequest:]_block_invoke.676
- ___28-[WPClient sendTestRequest:]_block_invoke.676.cold.1
- ___28-[WPClient sendTestRequest:]_block_invoke.676.cold.2
- ___28-[WPClient sendTestRequest:]_block_invoke_2.679
- ___28-[WPNearby sendData:toPeer:]_block_invoke.354
- ___28-[WPNearby sendData:toPeer:]_block_invoke.360
- ___28-[WPNearby sendData:toPeer:]_block_invoke.364
- ___29-[WPClient getPowerLogStats:]_block_invoke.650
- ___29-[WPClient getPowerLogStats:]_block_invoke.650.cold.1
- ___29-[WPClient getPowerLogStats:]_block_invoke.650.cold.2
- ___29-[WPClient getPowerLogStats:]_block_invoke.656
- ___29-[WPClient getPowerLogStats:]_block_invoke_2.653
- ___29-[WPClient startAdvertising:]_block_invoke.436
- ___29-[WPNearby deviceDiscovered:]_block_invoke.277
- ___29-[WPNearby deviceDiscovered:]_block_invoke.282
- ___29-[WPTest disconnectFromPeer:]_block_invoke.332
- ___30-[WPClient getAllTrackedZones]_block_invoke.568
- ___30-[WPClient getAllTrackedZones]_block_invoke.568.cold.1
- ___30-[WPClient getAllTrackedZones]_block_invoke.568.cold.2
- ___30-[WPClient getAllTrackedZones]_block_invoke_2.571
- ___30-[WPClient startTrackingZone:]_block_invoke.544
- ___30-[WPClient startTrackingZone:]_block_invoke.544.cold.1
- ___30-[WPClient startTrackingZone:]_block_invoke.544.cold.2
- ___30-[WPClient startTrackingZone:]_block_invoke_2.547
- ___30-[WPClient stopTrackingZones:]_block_invoke.552
- ___30-[WPClient stopTrackingZones:]_block_invoke.552.cold.1
- ___30-[WPClient stopTrackingZones:]_block_invoke.552.cold.2
- ___30-[WPClient stopTrackingZones:]_block_invoke_2.555
- ___30-[WPContinuity connectToPeer:]_block_invoke.270
- ___30-[WPHeySiri deviceDiscovered:]_block_invoke.222
- ___31-[WPClient establishConnection]_block_invoke.169
- ___31-[WPClient overrideAdvTimeout:]_block_invoke.642
- ___31-[WPClient overrideAdvTimeout:]_block_invoke.642.cold.1
- ___31-[WPClient overrideAdvTimeout:]_block_invoke.642.cold.2
- ___31-[WPClient overrideAdvTimeout:]_block_invoke_2.645
- ___31-[WPNearby disconnectFromPeer:]_block_invoke.402
- ___31-[WPTransfer deviceDiscovered:]_block_invoke.192
- ___32-[WPClient enableBubbleTestMode]_block_invoke.626
- ___32-[WPClient enableBubbleTestMode]_block_invoke.626.cold.1
- ___32-[WPClient enableBubbleTestMode]_block_invoke.626.cold.2
- ___32-[WPClient enableBubbleTestMode]_block_invoke_2.629
- ___32-[WPClient overrideScanTimeout:]_block_invoke.634
- ___32-[WPClient overrideScanTimeout:]_block_invoke.634.cold.1
- ___32-[WPClient overrideScanTimeout:]_block_invoke.634.cold.2
- ___32-[WPClient overrideScanTimeout:]_block_invoke_2.637
- ___32-[WPClient stopTrackingAllZones]_block_invoke.560
- ___32-[WPClient stopTrackingAllZones]_block_invoke.560.cold.1
- ___32-[WPClient stopTrackingAllZones]_block_invoke.560.cold.2
- ___32-[WPClient stopTrackingAllZones]_block_invoke_2.563
- ___32-[WPContinuity sendData:toPeer:]_block_invoke.351
- ___32-[WPContinuity sendData:toPeer:]_block_invoke.360
- ___32-[WPContinuity sendData:toPeer:]_block_invoke.364
- ___33-[WPClient checkAllowDuplicates:]_block_invoke.608
- ___33-[WPClient checkAllowDuplicates:]_block_invoke.608.cold.1
- ___33-[WPClient checkAllowDuplicates:]_block_invoke.608.cold.2
- ___33-[WPClient checkAllowDuplicates:]_block_invoke.614
- ___33-[WPClient checkAllowDuplicates:]_block_invoke_2.611
- ___33-[WPHomeKit stopScanningForType:]_block_invoke.201
- ___35-[WPClient initWithQueue:machName:]_block_invoke.154
- ___35-[WPContinuity disconnectFromPeer:]_block_invoke.328
- ___36-[WPDeviceScanner deviceDiscovered:]_block_invoke.194
- ___36-[WPTest connectToPeer:withOptions:]_block_invoke.262
- ___38-[WPClient connectToPeer:withOptions:]_block_invoke.511
- ___38-[WPClient connectToPeer:withOptions:]_block_invoke.511.cold.1
- ___38-[WPClient connectToPeer:withOptions:]_block_invoke.511.cold.2
- ___38-[WPClient connectToPeer:withOptions:]_block_invoke.524
- ___38-[WPClient connectToPeer:withOptions:]_block_invoke_2.525
- ___38-[WPClient connectToPeer:withOptions:]_block_invoke_2.525.cold.1
- ___38-[WPClient connectToPeer:withOptions:]_block_invoke_2.525.cold.2
- ___38-[WPNearby connectToPeer:withOptions:]_block_invoke.296
- ___39-[WPContinuity initWithDelegate:queue:]_block_invoke.146
- ___39-[WPDeviceScanner anyDiscoveredDevice:]_block_invoke.163
- ___39-[WPTest disconnectedDevice:withError:]_block_invoke.342
- ___41-[WPNearby disconnectedDevice:withError:]_block_invoke.410
- ___42-[WPAWDL initWithDelegate:queue:machName:]_block_invoke.119
- ___42-[WPClient listenToBandwidthNotifications]_block_invoke.584
- ___42-[WPClient listenToBandwidthNotifications]_block_invoke.584.cold.1
- ___42-[WPClient listenToBandwidthNotifications]_block_invoke.584.cold.2
- ___42-[WPClient listenToBandwidthNotifications]_block_invoke_2.587
- ___42-[WPHomeKit startCBDiscoveryScan:forType:]_block_invoke.239
- ___42-[WPHomeKit startCBDiscoveryScan:forType:]_block_invoke.246
- ___42-[WPHomeKit startCBDiscoveryScan:forType:]_block_invoke.250
- ___42-[WPHomeKit startCBDiscoveryScan:forType:]_block_invoke.250.cold.1
- ___42-[WPHomeKit startCBDiscoveryScan:forType:]_block_invoke_2.251
- ___43-[WPHomeKit startScanningWithData:forType:]_block_invoke.175
- ___43-[WPHomeKit startScanningWithData:forType:]_block_invoke.185
- ___43-[WPHomeKit startScanningWithData:forType:]_block_invoke.191
- ___44-[WPObjectDiscovery initWithDelegate:queue:]_block_invoke.190
- ___45-[WPClient updateScanningRequest:withUpdate:]_block_invoke.486
- ___45-[WPContinuity disconnectedDevice:withError:]_block_invoke.336
- ___45-[WPPairing initWithDelegate:queue:machName:]_block_invoke.148
- ___45-[WPTest advertisingStoppedOfType:withError:]_block_invoke.193
- ___45-[WPTest advertisingStoppedOfType:withError:]_block_invoke.198
- ___46-[WPHeySiri updateScanningRequest:withUpdate:]_block_invoke.193
- ___46-[WPObjectDiscovery startScanningWithOptions:]_block_invoke.250
- ___46-[WPZoneTracker enteredZone:manufacturerData:]_block_invoke.165
- ___46-[WPZoneTracker enteredZone:manufacturerData:]_block_invoke.170
- ___47-[WPNearby advertisingStoppedOfType:withError:]_block_invoke.233
- ___48-[WPClient updateAdvertisingRequest:withUpdate:]_block_invoke.448
- ___49-[WPHeySiri updateAdvertisingRequest:withUpdate:]_block_invoke.174
- ___51-[WPContinuity advertisingStoppedOfType:withError:]_block_invoke.206
- ___51-[WPObjectDiscovery startScanningWithMode:Timeout:]_block_invoke.225
- ___51-[WPTest connectedDevice:withError:shouldDiscover:]_block_invoke.272
- ___52-[WPMagicSwitch advertisingStoppedOfType:withError:]_block_invoke.192
- ___53-[WPNearby connectedDevice:withError:shouldDiscover:]_block_invoke.309
- ___54-[WPTest sentData:toEndpoint:forPeripheral:withError:]_block_invoke.306
- ___55-[WPClient sendDataToCharacteristic:inService:forPeer:]_block_invoke.536
- ___55-[WPTransfer connectedDevice:withError:shouldDiscover:]_block_invoke.217
- ___55-[WPTransfer connectedDevice:withError:shouldDiscover:]_block_invoke.223
- ___56-[WPNearby sentData:toEndpoint:forPeripheral:withError:]_block_invoke.376
- ___56-[WPTest central:subscribed:toCharacteristic:inService:]_block_invoke.319
- ___57-[WPContinuity connectedDevice:withError:shouldDiscover:]_block_invoke.283
- ___58-[WPHeySiri(Test) startScanningAndAdvertisingWithOptions:]_block_invoke.284
- ___58-[WPHeySiri(Test) startScanningAndAdvertisingWithOptions:]_block_invoke.288
- ___58-[WPHeySiri(Test) startScanningAndAdvertisingWithOptions:]_block_invoke.291
- ___58-[WPNearby central:subscribed:toCharacteristic:inService:]_block_invoke.389
- ___59-[WPDeviceScanner parseCompanyData:forSize:intoDictionary:]_block_invoke.215
- ___60-[WPAWDL startConnectionlessAWDLServiceAdvertisingWithData:]_block_invoke.148
- ___60-[WPTest startAdvertisingOfType:data:priority:mode:options:]_block_invoke.170
- ___60-[WPTransfer central:subscribed:toCharacteristic:inService:]_block_invoke.331
- ___61+[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:]_block_invoke.141
- ___61+[WPDObjectDiscoveryData objectDiscoveryReportFromAdvReport:]_block_invoke.157
- ___62-[WPContinuity central:subscribed:toCharacteristic:inService:]_block_invoke.388
- ___62-[WPNearby startAdvertisingOfType:data:priority:mode:options:]_block_invoke.208
- ___63-[WPNearby discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.318
- ___63-[WPNearby discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.327
- ___65-[WPTest receivedData:forCharacteristic:inService:forPeripheral:]_block_invoke.312
- ___65-[WPTransfer discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.232
- ___65-[WPTransfer discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.237
- ___65-[WPTransfer discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.240.cold.1
- ___65-[WPTransfer discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.244
- ___65-[WPTransfer discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.249
- ___67-[WPContinuity discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.292
- ___67-[WPContinuity discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.295.cold.1
- ___67-[WPContinuity discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.299
- ___67-[WPContinuity discoveredCharacteristicsAndServices:forPeripheral:]_block_invoke.304
- ___67-[WPNearby receivedData:forCharacteristic:inService:forPeripheral:]_block_invoke.382
- ___69-[WPTransfer receivedData:forCharacteristic:inService:forPeripheral:]_block_invoke.254
- ___69-[WPTransfer receivedData:forCharacteristic:inService:forPeripheral:]_block_invoke.261
- ___69-[WPTransfer receivedData:forCharacteristic:inService:forPeripheral:]_block_invoke.273
- ___71-[WPContinuity receivedData:forCharacteristic:inService:forPeripheral:]_block_invoke.379
- ___73-[WPNearby sentData:forCharacteristic:inService:forPeripheral:withError:]_block_invoke.371
- ___75-[WPTransfer sentData:forCharacteristic:inService:forPeripheral:withError:]_block_invoke.313
- ___77-[WPContinuity sentData:forCharacteristic:inService:forPeripheral:withError:]_block_invoke.371
- ___80-[WPContinuity startScanningForType:withData:mask:peers:boostedScan:duplicates:]_block_invoke.226
- ___80-[WPNearby updatedNotificationState:forCharacteristic:inService:withPeripheral:]_block_invoke.335
- ___80-[WPNearby updatedNotificationState:forCharacteristic:inService:withPeripheral:]_block_invoke.341
- ___82-[WPTest startScanningForType:data:mask:peers:scanMode:rssi:duplicates:scanCache:]_block_invoke.209
- ___84-[WPContinuity updatedNotificationState:forCharacteristic:inService:withPeripheral:]_block_invoke.312
- ___84-[WPContinuity updatedNotificationState:forCharacteristic:inService:withPeripheral:]_block_invoke.318
- ___96-[WPNearby startScanningForType:data:mask:peers:scanMode:rssi:duplicates:scanCache:useCaseList:]_block_invoke.249
- ___96-[WPNearby startScanningForType:data:mask:peers:scanMode:rssi:duplicates:scanCache:useCaseList:]_block_invoke.253
- ___block_literal_global.121
- ___block_literal_global.122
- ___block_literal_global.128
- ___block_literal_global.130
- ___block_literal_global.141
- ___block_literal_global.142
- ___block_literal_global.143
- ___block_literal_global.147
- ___block_literal_global.148
- ___block_literal_global.154
- ___block_literal_global.158
- ___block_literal_global.163
- ___block_literal_global.164
- ___block_literal_global.172
- ___block_literal_global.173
- ___block_literal_global.176
- ___block_literal_global.178
- ___block_literal_global.188
- ___block_literal_global.191
- ___block_literal_global.210
- ___block_literal_global.216
- ___block_literal_global.218
- ___block_literal_global.226
- ___block_literal_global.244
- ___block_literal_global.246
- ___block_literal_global.248
- ___block_literal_global.253
- ___block_literal_global.263
- ___block_literal_global.271
- ___block_literal_global.273
- ___block_literal_global.280
- ___block_literal_global.281
- ___block_literal_global.289
- ___block_literal_global.291
- ___block_literal_global.293
- ___block_literal_global.295
- ___block_literal_global.306
- ___block_literal_global.312
- ___block_literal_global.320
- ___block_literal_global.325
- ___block_literal_global.326
- ___block_literal_global.330
- ___block_literal_global.335
- ___block_literal_global.352
- ___block_literal_global.353
- ___block_literal_global.360
- ___block_literal_global.362
- ___block_literal_global.364
- ___block_literal_global.366
- ___block_literal_global.370
- ___block_literal_global.375
- ___block_literal_global.385
- ___block_literal_global.386
- ___block_literal_global.399
- ___block_literal_global.404
- ___block_literal_global.406
- ___block_literal_global.411
- ___block_literal_global.413
- ___block_literal_global.419
- ___block_literal_global.421
- ___block_literal_global.432
- ___block_literal_global.433
- ___block_literal_global.438
- ___block_literal_global.443
- ___block_literal_global.445
- ___block_literal_global.447
- ___block_literal_global.452
- ___block_literal_global.457
- ___block_literal_global.462
- ___block_literal_global.473
- ___block_literal_global.478
- ___block_literal_global.483
- ___block_literal_global.484
- ___block_literal_global.485
- ___block_literal_global.490
- ___block_literal_global.495
- ___block_literal_global.497
- ___block_literal_global.502
- ___block_literal_global.504
- ___block_literal_global.509
- ___block_literal_global.516
- ___block_literal_global.527
- ___block_literal_global.529
- ___block_literal_global.531
- ___block_literal_global.533
- ___block_literal_global.535
- ___block_literal_global.543
- ___block_literal_global.551
- ___block_literal_global.559
- ___block_literal_global.567
- ___block_literal_global.575
- ___block_literal_global.577
- ___block_literal_global.579
- ___block_literal_global.581
- ___block_literal_global.583
- ___block_literal_global.591
- ___block_literal_global.605
- ___block_literal_global.607
- ___block_literal_global.617
- ___block_literal_global.625
- ___block_literal_global.633
- ___block_literal_global.641
- ___block_literal_global.649
- ___block_literal_global.659
- ___block_literal_global.667
- ___block_literal_global.675
- ___block_literal_global.683
- ___block_literal_global.831
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$startScanning
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x26
- _objc_retain_x27
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
CStrings:
+ "HeySiri start scanning ElectionEndTime:%@"
+ "ProximityServiceAccessorySetup"
+ "T@\"NSNumber\",&,V_heySiriElectionEndTimeNsec"
+ "ThirdPartyAudioSwitching"
+ "WPHeySiriElectionEndTimeNsec"
+ "_heySiriElectionEndTimeNsec"
+ "heySiriElectionEndTimeNsec"
+ "kHeySiriElectionEndTimeNsec"
+ "setHeySiriElectionEndTimeNsec:"
- "%1"

```
