## WirelessProximity

> `/System/Library/PrivateFrameworks/WirelessProximity.framework/WirelessProximity`

```diff

-173.2.0.0.0
-  __TEXT.__text: 0x31224
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x241c
+174.16.1.1.2
+  __TEXT.__text: 0x31078
+  __TEXT.__auth_stubs: 0x580
+  __TEXT.__objc_methlist: 0x242c
   __TEXT.__const: 0x238
-  __TEXT.__cstring: 0x3137
-  __TEXT.__oslogstring: 0x44d6
-  __TEXT.__gcc_except_tab: 0x39c
-  __TEXT.__unwind_info: 0xedc
+  __TEXT.__cstring: 0x318b
+  __TEXT.__oslogstring: 0x44dd
+  __TEXT.__gcc_except_tab: 0x398
+  __TEXT.__unwind_info: 0xed8
   __TEXT.__objc_classname: 0x1c9
-  __TEXT.__objc_methname: 0x51e7
+  __TEXT.__objc_methname: 0x51e1
   __TEXT.__objc_methtype: 0xe01
-  __TEXT.__objc_stubs: 0x42e0
+  __TEXT.__objc_stubs: 0x42a0
   __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0x748
+  __DATA_CONST.__const: 0x6f8
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x2b88
-  __DATA_CONST.__objc_selrefs: 0x1500
+  __DATA_CONST.__objc_selrefs: 0x14f8
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x128
+  __DATA_CONST.__objc_superrefs: 0xb8
   __AUTH_CONST.__cfstring: 0x2a60
   __AUTH_CONST.__const: 0x3420
   __AUTH_CONST.__objc_const: 0xa68
   __AUTH_CONST.__objc_intobj: 0x180
-  __AUTH_CONST.__auth_got: 0x2e8
+  __AUTH_CONST.__auth_got: 0x2d0
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x128
-  __DATA.__objc_superrefs: 0xb8
   __DATA.__objc_ivar: 0x1c8
   __DATA.__data: 0x2a8
   __DATA_DIRTY.__objc_data: 0x5f0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7214ADE4-F081-30B8-9ECB-1A1D3A0DCD5C
-  Functions: 1500
-  Symbols:   4594
-  CStrings:  2252
+  UUID: DD9C893D-F204-355B-8DA5-B552D3EE3E2A
+  Functions: 1499
+  Symbols:   4585
+  CStrings:  2258
 
Symbols:
+ -[WPClient dispatchAdvertisement:]
+ -[WPHeySiri updateAdvertisingRequest:withUpdate:].cold.2
+ -[WPHeySiri updateScanningRequest:withUpdate:].cold.2
+ GCC_except_table104
+ GCC_except_table121
+ GCC_except_table126
+ GCC_except_table131
+ GCC_except_table136
+ GCC_except_table141
+ GCC_except_table162
+ GCC_except_table168
+ GCC_except_table173
+ GCC_except_table178
+ GCC_except_table183
+ GCC_except_table188
+ GCC_except_table194
+ GCC_except_table199
+ GCC_except_table204
+ GCC_except_table53
+ GCC_except_table60
+ GCC_except_table80
+ GCC_except_table97
+ ___23-[WPClient addServices]_block_invoke.404
+ ___23-[WPClient addServices]_block_invoke_2.405
+ ___23-[WPClient addServices]_block_invoke_2.405.cold.1
+ ___26-[WPClient enableTestMode]_block_invoke.612
+ ___26-[WPClient enableTestMode]_block_invoke.612.cold.1
+ ___26-[WPClient enableTestMode]_block_invoke_2.615
+ ___26-[WPHeySiri startScanning]_block_invoke.169
+ ___27-[WPClient disableScanning]_block_invoke.662
+ ___27-[WPClient disableScanning]_block_invoke.662.cold.1
+ ___27-[WPClient disableScanning]_block_invoke_2.665
+ ___27-[WPClient dumpDaemonState]_block_invoke.654
+ ___27-[WPClient dumpDaemonState]_block_invoke.654.cold.1
+ ___27-[WPClient dumpDaemonState]_block_invoke_2.657
+ ___27-[WPClient stateDidChange:]_block_invoke.586
+ ___27-[WPClient stateDidChange:]_block_invoke.589
+ ___27-[WPClient stateDidChange:]_block_invoke.592
+ ___28-[WPClient sendTestRequest:]_block_invoke.670
+ ___28-[WPClient sendTestRequest:]_block_invoke.670.cold.1
+ ___28-[WPClient sendTestRequest:]_block_invoke_2.673
+ ___29-[WPClient getPowerLogStats:]_block_invoke.644
+ ___29-[WPClient getPowerLogStats:]_block_invoke.644.cold.1
+ ___29-[WPClient getPowerLogStats:]_block_invoke.650
+ ___29-[WPClient getPowerLogStats:]_block_invoke_2.647
+ ___30-[WPClient getAllTrackedZones]_block_invoke.562
+ ___30-[WPClient getAllTrackedZones]_block_invoke.562.cold.1
+ ___30-[WPClient getAllTrackedZones]_block_invoke_2.565
+ ___30-[WPClient startTrackingZone:]_block_invoke.538
+ ___30-[WPClient startTrackingZone:]_block_invoke.538.cold.1
+ ___30-[WPClient startTrackingZone:]_block_invoke_2.541
+ ___30-[WPClient stopTrackingZones:]_block_invoke.546
+ ___30-[WPClient stopTrackingZones:]_block_invoke.546.cold.1
+ ___30-[WPClient stopTrackingZones:]_block_invoke_2.549
+ ___30-[WPHeySiri deviceDiscovered:]_block_invoke.211
+ ___31-[WPClient overrideAdvTimeout:]_block_invoke.636
+ ___31-[WPClient overrideAdvTimeout:]_block_invoke.636.cold.1
+ ___31-[WPClient overrideAdvTimeout:]_block_invoke_2.639
+ ___32-[WPClient enableBubbleTestMode]_block_invoke.620
+ ___32-[WPClient enableBubbleTestMode]_block_invoke.620.cold.1
+ ___32-[WPClient enableBubbleTestMode]_block_invoke_2.623
+ ___32-[WPClient overrideScanTimeout:]_block_invoke.628
+ ___32-[WPClient overrideScanTimeout:]_block_invoke.628.cold.1
+ ___32-[WPClient overrideScanTimeout:]_block_invoke_2.631
+ ___32-[WPClient stopTrackingAllZones]_block_invoke.554
+ ___32-[WPClient stopTrackingAllZones]_block_invoke.554.cold.1
+ ___32-[WPClient stopTrackingAllZones]_block_invoke_2.557
+ ___33-[WPClient checkAllowDuplicates:]_block_invoke.602
+ ___33-[WPClient checkAllowDuplicates:]_block_invoke.602.cold.1
+ ___33-[WPClient checkAllowDuplicates:]_block_invoke.608
+ ___33-[WPClient checkAllowDuplicates:]_block_invoke_2.605
+ ___34-[WPClient dispatchAdvertisement:]_block_invoke
+ ___34-[WPClient dispatchAdvertisement:]_block_invoke_2
+ ___34-[WPClient dispatchAdvertisement:]_block_invoke_2.cold.1
+ ___34-[WPClient dispatchAdvertisement:]_block_invoke_3
+ ___38-[WPClient connectToPeer:withOptions:]_block_invoke.508
+ ___38-[WPClient connectToPeer:withOptions:]_block_invoke.508.cold.1
+ ___38-[WPClient connectToPeer:withOptions:]_block_invoke.518
+ ___38-[WPClient connectToPeer:withOptions:]_block_invoke_2.519
+ ___38-[WPClient connectToPeer:withOptions:]_block_invoke_2.519.cold.1
+ ___42-[WPClient listenToBandwidthNotifications]_block_invoke.578
+ ___42-[WPClient listenToBandwidthNotifications]_block_invoke.578.cold.1
+ ___42-[WPClient listenToBandwidthNotifications]_block_invoke_2.581
+ ___45-[WPClient updateScanningRequest:withUpdate:]_block_invoke.483
+ ___46-[WPHeySiri updateScanningRequest:withUpdate:]_block_invoke.182
+ ___48-[WPClient updateAdvertisingRequest:withUpdate:]_block_invoke.445
+ ___49-[WPHeySiri updateAdvertisingRequest:withUpdate:]_block_invoke.164
+ ___55-[WPClient sendDataToCharacteristic:inService:forPeer:]_block_invoke.530
+ ___58-[WPHeySiri(Test) startScanningAndAdvertisingWithOptions:]_block_invoke.273
+ ___58-[WPHeySiri(Test) startScanningAndAdvertisingWithOptions:]_block_invoke.283
+ ___58-[WPHeySiri(Test) startScanningAndAdvertisingWithOptions:]_block_invoke.286
+ ___block_literal_global.166
+ ___block_literal_global.275
+ ___block_literal_global.285
+ ___block_literal_global.383
+ ___block_literal_global.403
+ ___block_literal_global.408
+ ___block_literal_global.410
+ ___block_literal_global.416
+ ___block_literal_global.435
+ ___block_literal_global.440
+ ___block_literal_global.442
+ ___block_literal_global.447
+ ___block_literal_global.454
+ ___block_literal_global.462
+ ___block_literal_global.470
+ ___block_literal_global.475
+ ___block_literal_global.480
+ ___block_literal_global.482
+ ___block_literal_global.485
+ ___block_literal_global.487
+ ___block_literal_global.492
+ ___block_literal_global.499
+ ___block_literal_global.506
+ ___block_literal_global.513
+ ___block_literal_global.521
+ ___block_literal_global.523
+ ___block_literal_global.525
+ ___block_literal_global.527
+ ___block_literal_global.529
+ ___block_literal_global.537
+ ___block_literal_global.540
+ ___block_literal_global.543
+ ___block_literal_global.545
+ ___block_literal_global.548
+ ___block_literal_global.551
+ ___block_literal_global.553
+ ___block_literal_global.556
+ ___block_literal_global.559
+ ___block_literal_global.561
+ ___block_literal_global.564
+ ___block_literal_global.567
+ ___block_literal_global.569
+ ___block_literal_global.571
+ ___block_literal_global.575
+ ___block_literal_global.577
+ ___block_literal_global.583
+ ___block_literal_global.585
+ ___block_literal_global.588
+ ___block_literal_global.591
+ ___block_literal_global.599
+ ___block_literal_global.601
+ ___block_literal_global.604
+ ___block_literal_global.607
+ ___block_literal_global.611
+ ___block_literal_global.614
+ ___block_literal_global.617
+ ___block_literal_global.619
+ ___block_literal_global.622
+ ___block_literal_global.625
+ ___block_literal_global.627
+ ___block_literal_global.630
+ ___block_literal_global.633
+ ___block_literal_global.635
+ ___block_literal_global.638
+ ___block_literal_global.641
+ ___block_literal_global.643
+ ___block_literal_global.646
+ ___block_literal_global.649
+ ___block_literal_global.653
+ ___block_literal_global.656
+ ___block_literal_global.659
+ ___block_literal_global.661
+ ___block_literal_global.664
+ ___block_literal_global.667
+ ___block_literal_global.669
+ ___block_literal_global.672
+ ___block_literal_global.675
+ ___block_literal_global.677
+ ___block_literal_global.824
+ _objc_msgSend$dispatchAdvertisement:
- GCC_except_table101
- GCC_except_table120
- GCC_except_table125
- GCC_except_table130
- GCC_except_table135
- GCC_except_table140
- GCC_except_table153
- GCC_except_table166
- GCC_except_table172
- GCC_except_table177
- GCC_except_table182
- GCC_except_table187
- GCC_except_table192
- GCC_except_table198
- GCC_except_table203
- GCC_except_table208
- GCC_except_table57
- GCC_except_table76
- GCC_except_table92
- ___23-[WPClient addServices]_block_invoke.403
- ___23-[WPClient addServices]_block_invoke_2.404
- ___23-[WPClient addServices]_block_invoke_2.404.cold.1
- ___26-[WPClient enableTestMode]_block_invoke.621
- ___26-[WPClient enableTestMode]_block_invoke.621.cold.1
- ___26-[WPClient enableTestMode]_block_invoke_2.624
- ___26-[WPHeySiri startScanning]_block_invoke.166
- ___27-[WPClient disableScanning]_block_invoke.671
- ___27-[WPClient disableScanning]_block_invoke.671.cold.1
- ___27-[WPClient disableScanning]_block_invoke_2.674
- ___27-[WPClient dumpDaemonState]_block_invoke.663
- ___27-[WPClient dumpDaemonState]_block_invoke.663.cold.1
- ___27-[WPClient dumpDaemonState]_block_invoke_2.666
- ___27-[WPClient stateDidChange:]_block_invoke.598
- ___27-[WPClient stateDidChange:]_block_invoke.601
- ___27-[WPClient stateDidChange:]_block_invoke.604
- ___28-[WPClient sendTestRequest:]_block_invoke.679
- ___28-[WPClient sendTestRequest:]_block_invoke.679.cold.1
- ___28-[WPClient sendTestRequest:]_block_invoke_2.682
- ___29-[WPClient getPowerLogStats:]_block_invoke.653
- ___29-[WPClient getPowerLogStats:]_block_invoke.653.cold.1
- ___29-[WPClient getPowerLogStats:]_block_invoke.659
- ___29-[WPClient getPowerLogStats:]_block_invoke_2.656
- ___29-[WPClient startAdvertising:]_block_invoke.427
- ___29-[WPClient startAdvertising:]_block_invoke.430
- ___29-[WPClient startAdvertising:]_block_invoke.440
- ___29-[WPClient startAdvertising:]_block_invoke_2
- ___29-[WPClient startAdvertising:]_block_invoke_2.434
- ___29-[WPClient startAdvertising:]_block_invoke_2.434.cold.1
- ___29-[WPClient startAdvertising:]_block_invoke_2.441
- ___29-[WPClient startAdvertising:]_block_invoke_2.441.cold.1
- ___29-[WPClient startAdvertising:]_block_invoke_3
- ___29-[WPClient startAdvertising:]_block_invoke_3.442
- ___30-[WPClient getAllTrackedZones]_block_invoke.571
- ___30-[WPClient getAllTrackedZones]_block_invoke.571.cold.1
- ___30-[WPClient getAllTrackedZones]_block_invoke_2.574
- ___30-[WPClient startTrackingZone:]_block_invoke.547
- ___30-[WPClient startTrackingZone:]_block_invoke.547.cold.1
- ___30-[WPClient startTrackingZone:]_block_invoke_2.550
- ___30-[WPClient stopTrackingZones:]_block_invoke.555
- ___30-[WPClient stopTrackingZones:]_block_invoke.555.cold.1
- ___30-[WPClient stopTrackingZones:]_block_invoke_2.558
- ___30-[WPHeySiri deviceDiscovered:]_block_invoke.205
- ___31-[WPClient overrideAdvTimeout:]_block_invoke.645
- ___31-[WPClient overrideAdvTimeout:]_block_invoke.645.cold.1
- ___31-[WPClient overrideAdvTimeout:]_block_invoke_2.648
- ___32-[WPClient enableBubbleTestMode]_block_invoke.629
- ___32-[WPClient enableBubbleTestMode]_block_invoke.629.cold.1
- ___32-[WPClient enableBubbleTestMode]_block_invoke_2.632
- ___32-[WPClient overrideScanTimeout:]_block_invoke.637
- ___32-[WPClient overrideScanTimeout:]_block_invoke.637.cold.1
- ___32-[WPClient overrideScanTimeout:]_block_invoke_2.640
- ___32-[WPClient stopTrackingAllZones]_block_invoke.563
- ___32-[WPClient stopTrackingAllZones]_block_invoke.563.cold.1
- ___32-[WPClient stopTrackingAllZones]_block_invoke_2.566
- ___33-[WPClient checkAllowDuplicates:]_block_invoke.611
- ___33-[WPClient checkAllowDuplicates:]_block_invoke.611.cold.1
- ___33-[WPClient checkAllowDuplicates:]_block_invoke.617
- ___33-[WPClient checkAllowDuplicates:]_block_invoke_2.614
- ___38-[WPClient connectToPeer:withOptions:]_block_invoke.517
- ___38-[WPClient connectToPeer:withOptions:]_block_invoke.517.cold.1
- ___38-[WPClient connectToPeer:withOptions:]_block_invoke.527
- ___38-[WPClient connectToPeer:withOptions:]_block_invoke_2.528
- ___38-[WPClient connectToPeer:withOptions:]_block_invoke_2.528.cold.1
- ___42-[WPClient listenToBandwidthNotifications]_block_invoke.587
- ___42-[WPClient listenToBandwidthNotifications]_block_invoke.587.cold.1
- ___42-[WPClient listenToBandwidthNotifications]_block_invoke_2.590
- ___45-[WPClient updateScanningRequest:withUpdate:]_block_invoke.492
- ___48-[WPClient updateAdvertisingRequest:withUpdate:]_block_invoke.454
- ___55-[WPClient sendDataToCharacteristic:inService:forPeer:]_block_invoke.539
- ___58-[WPHeySiri(Test) startScanningAndAdvertisingWithOptions:]_block_invoke.267
- ___58-[WPHeySiri(Test) startScanningAndAdvertisingWithOptions:]_block_invoke.271
- ___58-[WPHeySiri(Test) startScanningAndAdvertisingWithOptions:]_block_invoke.274
- ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_literal_global.402
- ___block_literal_global.407
- ___block_literal_global.422
- ___block_literal_global.432
- ___block_literal_global.439
- ___block_literal_global.451
- ___block_literal_global.453
- ___block_literal_global.456
- ___block_literal_global.458
- ___block_literal_global.463
- ___block_literal_global.471
- ___block_literal_global.479
- ___block_literal_global.484
- ___block_literal_global.489
- ___block_literal_global.491
- ___block_literal_global.496
- ___block_literal_global.503
- ___block_literal_global.508
- ___block_literal_global.510
- ___block_literal_global.515
- ___block_literal_global.522
- ___block_literal_global.530
- ___block_literal_global.534
- ___block_literal_global.536
- ___block_literal_global.538
- ___block_literal_global.541
- ___block_literal_global.546
- ___block_literal_global.549
- ___block_literal_global.552
- ___block_literal_global.554
- ___block_literal_global.557
- ___block_literal_global.560
- ___block_literal_global.562
- ___block_literal_global.565
- ___block_literal_global.568
- ___block_literal_global.570
- ___block_literal_global.576
- ___block_literal_global.578
- ___block_literal_global.582
- ___block_literal_global.584
- ___block_literal_global.586
- ___block_literal_global.589
- ___block_literal_global.592
- ___block_literal_global.600
- ___block_literal_global.603
- ___block_literal_global.606
- ___block_literal_global.608
- ___block_literal_global.610
- ___block_literal_global.613
- ___block_literal_global.616
- ___block_literal_global.620
- ___block_literal_global.623
- ___block_literal_global.626
- ___block_literal_global.628
- ___block_literal_global.631
- ___block_literal_global.634
- ___block_literal_global.636
- ___block_literal_global.639
- ___block_literal_global.642
- ___block_literal_global.644
- ___block_literal_global.647
- ___block_literal_global.650
- ___block_literal_global.652
- ___block_literal_global.655
- ___block_literal_global.658
- ___block_literal_global.662
- ___block_literal_global.665
- ___block_literal_global.668
- ___block_literal_global.670
- ___block_literal_global.673
- ___block_literal_global.676
- ___block_literal_global.678
- ___block_literal_global.681
- ___block_literal_global.684
- ___block_literal_global.686
- ___block_literal_global.832
- _dispatch_sync
- _objc_msgSend$advertisingStartedOfTypeAt:
- _objc_msgSend$startAdvertising:reply:
- _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
- _objc_retainBlock
- _objc_retain_x9
CStrings:
+ "FindNearbyPencil"
+ "HeySiri advertising updateTime set to %.2f"
+ "HeySiri scan updateTime set to %.2f, current scan: %d"
+ "SafetyAlerts"
+ "SharingVisionProDiscovery"
+ "SharingVisionProStateChange"
+ "T@\"NSString\",?,R,C"
+ "dispatchAdvertisement:"
- "WPClient queueing up HeySiri start advertising synchronously onto daemon deliver queue %@"
- "synchronousRemoteObjectProxyWithErrorHandler:"

```
