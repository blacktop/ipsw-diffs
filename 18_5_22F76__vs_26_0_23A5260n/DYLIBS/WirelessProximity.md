## WirelessProximity

> `/System/Library/PrivateFrameworks/WirelessProximity.framework/WirelessProximity`

```diff

-185.7.0.0.0
-  __TEXT.__text: 0x319f4
-  __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_methlist: 0x2994
+190.40.1.2.0
+  __TEXT.__text: 0x31ed4
+  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__objc_methlist: 0x29bc
   __TEXT.__const: 0x2f0
-  __TEXT.__cstring: 0x3370
+  __TEXT.__cstring: 0x3666
   __TEXT.__oslogstring: 0x4500
-  __TEXT.__gcc_except_tab: 0x684
-  __TEXT.__unwind_info: 0x13e0
+  __TEXT.__gcc_except_tab: 0x688
+  __TEXT.__unwind_info: 0x1410
   __TEXT.__objc_classname: 0x1c9
-  __TEXT.__objc_methname: 0x52b0
-  __TEXT.__objc_methtype: 0xe01
-  __TEXT.__objc_stubs: 0x43a0
+  __TEXT.__objc_methname: 0x5389
+  __TEXT.__objc_methtype: 0xe1e
+  __TEXT.__objc_stubs: 0x4440
   __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x700
+  __DATA_CONST.__const: 0x728
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15c0
+  __DATA_CONST.__objc_selrefs: 0x15e8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xb8
-  __AUTH_CONST.__auth_got: 0x2d8
+  __AUTH_CONST.__auth_got: 0x2e8
   __AUTH_CONST.__const: 0x3440
-  __AUTH_CONST.__cfstring: 0x2aa0
-  __AUTH_CONST.__objc_const: 0x2c60
-  __AUTH_CONST.__objc_intobj: 0x198
+  __AUTH_CONST.__cfstring: 0x2ac0
+  __AUTH_CONST.__objc_const: 0x2c98
+  __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x1d0
+  __DATA.__objc_ivar: 0x1d4
   __DATA.__data: 0x2a8
   __DATA_DIRTY.__objc_data: 0x5f0
   __DATA_DIRTY.__bss: 0x20

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8B8DC179-F254-36CD-9A59-023AB117A577
-  Functions: 1827
-  Symbols:   5383
-  CStrings:  2287
+  UUID: 7057A89D-7729-358F-94C9-FBCC8B5CE261
+  Functions: 1833
+  Symbols:   5388
+  CStrings:  2323
 
Symbols:
+ -[WPAdvertisingRequest advertisingRandomData]
+ -[WPAdvertisingRequest setAdvertisingRandomData:]
+ -[WPClient handleStartScanningError:ofType:]
+ -[WPClient handleStartScanningError:ofType:].cold.1
+ -[WPClient handleStartScanningError:ofType:].cold.2
+ GCC_except_table100
+ GCC_except_table107
+ GCC_except_table111
+ GCC_except_table115
+ GCC_except_table119
+ GCC_except_table124
+ GCC_except_table129
+ GCC_except_table134
+ GCC_except_table139
+ GCC_except_table144
+ GCC_except_table148
+ GCC_except_table152
+ GCC_except_table165
+ GCC_except_table171
+ GCC_except_table176
+ GCC_except_table181
+ GCC_except_table186
+ GCC_except_table191
+ GCC_except_table197
+ GCC_except_table202
+ GCC_except_table207
+ GCC_except_table66
+ GCC_except_table71
+ GCC_except_table75
+ GCC_except_table83
+ GCC_except_table87
+ GCC_except_table91
+ _OBJC_IVAR_$_WPAdvertisingRequest._advertisingRandomData
+ ___23-[WPClient addServices]_block_invoke.407
+ ___23-[WPClient addServices]_block_invoke_2.408
+ ___23-[WPClient addServices]_block_invoke_2.408.cold.1
+ ___23-[WPClient addServices]_block_invoke_2.408.cold.2
+ ___26-[WPClient enableTestMode]_block_invoke.616
+ ___26-[WPClient enableTestMode]_block_invoke.616.cold.1
+ ___26-[WPClient enableTestMode]_block_invoke.616.cold.2
+ ___26-[WPClient enableTestMode]_block_invoke_2.619
+ ___26-[WPClient startScanning:]_block_invoke_4
+ ___27-[WPClient disableScanning]_block_invoke.666
+ ___27-[WPClient disableScanning]_block_invoke.666.cold.1
+ ___27-[WPClient disableScanning]_block_invoke.666.cold.2
+ ___27-[WPClient disableScanning]_block_invoke_2.669
+ ___27-[WPClient dumpDaemonState]_block_invoke.658
+ ___27-[WPClient dumpDaemonState]_block_invoke.658.cold.1
+ ___27-[WPClient dumpDaemonState]_block_invoke.658.cold.2
+ ___27-[WPClient dumpDaemonState]_block_invoke_2.661
+ ___27-[WPClient stateDidChange:]_block_invoke.590
+ ___27-[WPClient stateDidChange:]_block_invoke.593
+ ___27-[WPClient stateDidChange:]_block_invoke.596
+ ___27-[WPClient stateDidChange:]_block_invoke.599
+ ___28-[WPClient sendTestRequest:]_block_invoke.674
+ ___28-[WPClient sendTestRequest:]_block_invoke.674.cold.1
+ ___28-[WPClient sendTestRequest:]_block_invoke.674.cold.2
+ ___28-[WPClient sendTestRequest:]_block_invoke_2.677
+ ___29-[WPClient getPowerLogStats:]_block_invoke.648
+ ___29-[WPClient getPowerLogStats:]_block_invoke.648.cold.1
+ ___29-[WPClient getPowerLogStats:]_block_invoke.648.cold.2
+ ___29-[WPClient getPowerLogStats:]_block_invoke.654
+ ___29-[WPClient getPowerLogStats:]_block_invoke_2.651
+ ___29-[WPClient startAdvertising:]_block_invoke.436
+ ___30-[WPClient getAllTrackedZones]_block_invoke.566
+ ___30-[WPClient getAllTrackedZones]_block_invoke.566.cold.1
+ ___30-[WPClient getAllTrackedZones]_block_invoke.566.cold.2
+ ___30-[WPClient getAllTrackedZones]_block_invoke_2.569
+ ___30-[WPClient startTrackingZone:]_block_invoke.542
+ ___30-[WPClient startTrackingZone:]_block_invoke.542.cold.1
+ ___30-[WPClient startTrackingZone:]_block_invoke.542.cold.2
+ ___30-[WPClient startTrackingZone:]_block_invoke_2.545
+ ___30-[WPClient stopTrackingZones:]_block_invoke.550
+ ___30-[WPClient stopTrackingZones:]_block_invoke.550.cold.1
+ ___30-[WPClient stopTrackingZones:]_block_invoke.550.cold.2
+ ___30-[WPClient stopTrackingZones:]_block_invoke_2.553
+ ___31-[WPClient overrideAdvTimeout:]_block_invoke.640
+ ___31-[WPClient overrideAdvTimeout:]_block_invoke.640.cold.1
+ ___31-[WPClient overrideAdvTimeout:]_block_invoke.640.cold.2
+ ___31-[WPClient overrideAdvTimeout:]_block_invoke_2.643
+ ___32-[WPClient enableBubbleTestMode]_block_invoke.624
+ ___32-[WPClient enableBubbleTestMode]_block_invoke.624.cold.1
+ ___32-[WPClient enableBubbleTestMode]_block_invoke.624.cold.2
+ ___32-[WPClient enableBubbleTestMode]_block_invoke_2.627
+ ___32-[WPClient overrideScanTimeout:]_block_invoke.632
+ ___32-[WPClient overrideScanTimeout:]_block_invoke.632.cold.1
+ ___32-[WPClient overrideScanTimeout:]_block_invoke.632.cold.2
+ ___32-[WPClient overrideScanTimeout:]_block_invoke_2.635
+ ___32-[WPClient stopTrackingAllZones]_block_invoke.558
+ ___32-[WPClient stopTrackingAllZones]_block_invoke.558.cold.1
+ ___32-[WPClient stopTrackingAllZones]_block_invoke.558.cold.2
+ ___32-[WPClient stopTrackingAllZones]_block_invoke_2.561
+ ___33-[WPClient checkAllowDuplicates:]_block_invoke.606
+ ___33-[WPClient checkAllowDuplicates:]_block_invoke.606.cold.1
+ ___33-[WPClient checkAllowDuplicates:]_block_invoke.606.cold.2
+ ___33-[WPClient checkAllowDuplicates:]_block_invoke.612
+ ___33-[WPClient checkAllowDuplicates:]_block_invoke_2.609
+ ___38-[WPClient connectToPeer:withOptions:]_block_invoke.511
+ ___38-[WPClient connectToPeer:withOptions:]_block_invoke.511.cold.1
+ ___38-[WPClient connectToPeer:withOptions:]_block_invoke.511.cold.2
+ ___38-[WPClient connectToPeer:withOptions:]_block_invoke.522
+ ___38-[WPClient connectToPeer:withOptions:]_block_invoke_2.523
+ ___38-[WPClient connectToPeer:withOptions:]_block_invoke_2.523.cold.1
+ ___38-[WPClient connectToPeer:withOptions:]_block_invoke_2.523.cold.2
+ ___42-[WPClient listenToBandwidthNotifications]_block_invoke.582
+ ___42-[WPClient listenToBandwidthNotifications]_block_invoke.582.cold.1
+ ___42-[WPClient listenToBandwidthNotifications]_block_invoke.582.cold.2
+ ___42-[WPClient listenToBandwidthNotifications]_block_invoke_2.585
+ ___44-[WPClient handleStartScanningError:ofType:]_block_invoke
+ ___45-[WPClient updateScanningRequest:withUpdate:]_block_invoke.486
+ ___48-[WPClient updateAdvertisingRequest:withUpdate:]_block_invoke.448
+ ___55-[WPClient sendDataToCharacteristic:inService:forPeer:]_block_invoke.534
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_literal_global.386
+ ___block_literal_global.406
+ ___block_literal_global.411
+ ___block_literal_global.413
+ ___block_literal_global.419
+ ___block_literal_global.432
+ ___block_literal_global.438
+ ___block_literal_global.443
+ ___block_literal_global.445
+ ___block_literal_global.450
+ ___block_literal_global.452
+ ___block_literal_global.457
+ ___block_literal_global.473
+ ___block_literal_global.478
+ ___block_literal_global.483
+ ___block_literal_global.488
+ ___block_literal_global.490
+ ___block_literal_global.495
+ ___block_literal_global.497
+ ___block_literal_global.502
+ ___block_literal_global.504
+ ___block_literal_global.509
+ ___block_literal_global.516
+ ___block_literal_global.531
+ ___block_literal_global.533
+ ___block_literal_global.536
+ ___block_literal_global.541
+ ___block_literal_global.544
+ ___block_literal_global.547
+ ___block_literal_global.549
+ ___block_literal_global.552
+ ___block_literal_global.555
+ ___block_literal_global.557
+ ___block_literal_global.560
+ ___block_literal_global.563
+ ___block_literal_global.565
+ ___block_literal_global.568
+ ___block_literal_global.579
+ ___block_literal_global.581
+ ___block_literal_global.584
+ ___block_literal_global.587
+ ___block_literal_global.589
+ ___block_literal_global.592
+ ___block_literal_global.595
+ ___block_literal_global.598
+ ___block_literal_global.603
+ ___block_literal_global.605
+ ___block_literal_global.608
+ ___block_literal_global.615
+ ___block_literal_global.618
+ ___block_literal_global.621
+ ___block_literal_global.623
+ ___block_literal_global.626
+ ___block_literal_global.629
+ ___block_literal_global.631
+ ___block_literal_global.634
+ ___block_literal_global.637
+ ___block_literal_global.639
+ ___block_literal_global.642
+ ___block_literal_global.645
+ ___block_literal_global.647
+ ___block_literal_global.650
+ ___block_literal_global.657
+ ___block_literal_global.660
+ ___block_literal_global.663
+ ___block_literal_global.665
+ ___block_literal_global.668
+ ___block_literal_global.671
+ ___block_literal_global.673
+ ___block_literal_global.676
+ ___block_literal_global.679
+ ___block_literal_global.681
+ ___block_literal_global.829
+ _dispatch_sync
+ _objc_msgSend$advertisingRandomData
+ _objc_msgSend$handleStartScanningError:ofType:
+ _objc_msgSend$setAdvertisingRandomData:
+ _objc_msgSend$startScanning:withDispatch:
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_retain_x9
- GCC_except_table104
- GCC_except_table108
- GCC_except_table112
- GCC_except_table116
- GCC_except_table121
- GCC_except_table126
- GCC_except_table131
- GCC_except_table136
- GCC_except_table141
- GCC_except_table145
- GCC_except_table149
- GCC_except_table162
- GCC_except_table168
- GCC_except_table173
- GCC_except_table178
- GCC_except_table183
- GCC_except_table188
- GCC_except_table194
- GCC_except_table199
- GCC_except_table204
- GCC_except_table64
- GCC_except_table68
- GCC_except_table72
- GCC_except_table80
- GCC_except_table84
- GCC_except_table88
- GCC_except_table97
- ___23-[WPClient addServices]_block_invoke.404
- ___23-[WPClient addServices]_block_invoke_2.405
- ___23-[WPClient addServices]_block_invoke_2.405.cold.1
- ___23-[WPClient addServices]_block_invoke_2.405.cold.2
- ___26-[WPClient enableTestMode]_block_invoke.612
- ___26-[WPClient enableTestMode]_block_invoke.612.cold.1
- ___26-[WPClient enableTestMode]_block_invoke.612.cold.2
- ___26-[WPClient enableTestMode]_block_invoke_2.615
- ___26-[WPClient startScanning:]_block_invoke_2.cold.1
- ___26-[WPClient startScanning:]_block_invoke_2.cold.2
- ___27-[WPClient disableScanning]_block_invoke.662
- ___27-[WPClient disableScanning]_block_invoke.662.cold.1
- ___27-[WPClient disableScanning]_block_invoke.662.cold.2
- ___27-[WPClient disableScanning]_block_invoke_2.665
- ___27-[WPClient dumpDaemonState]_block_invoke.654
- ___27-[WPClient dumpDaemonState]_block_invoke.654.cold.1
- ___27-[WPClient dumpDaemonState]_block_invoke.654.cold.2
- ___27-[WPClient dumpDaemonState]_block_invoke_2.657
- ___27-[WPClient stateDidChange:]_block_invoke.586
- ___27-[WPClient stateDidChange:]_block_invoke.589
- ___27-[WPClient stateDidChange:]_block_invoke.592
- ___27-[WPClient stateDidChange:]_block_invoke.595
- ___28-[WPClient sendTestRequest:]_block_invoke.670
- ___28-[WPClient sendTestRequest:]_block_invoke.670.cold.1
- ___28-[WPClient sendTestRequest:]_block_invoke.670.cold.2
- ___28-[WPClient sendTestRequest:]_block_invoke_2.673
- ___29-[WPClient getPowerLogStats:]_block_invoke.644
- ___29-[WPClient getPowerLogStats:]_block_invoke.644.cold.1
- ___29-[WPClient getPowerLogStats:]_block_invoke.644.cold.2
- ___29-[WPClient getPowerLogStats:]_block_invoke.650
- ___29-[WPClient getPowerLogStats:]_block_invoke_2.647
- ___29-[WPClient startAdvertising:]_block_invoke.433
- ___30-[WPClient getAllTrackedZones]_block_invoke.562
- ___30-[WPClient getAllTrackedZones]_block_invoke.562.cold.1
- ___30-[WPClient getAllTrackedZones]_block_invoke.562.cold.2
- ___30-[WPClient getAllTrackedZones]_block_invoke_2.565
- ___30-[WPClient startTrackingZone:]_block_invoke.538
- ___30-[WPClient startTrackingZone:]_block_invoke.538.cold.1
- ___30-[WPClient startTrackingZone:]_block_invoke.538.cold.2
- ___30-[WPClient startTrackingZone:]_block_invoke_2.541
- ___30-[WPClient stopTrackingZones:]_block_invoke.546
- ___30-[WPClient stopTrackingZones:]_block_invoke.546.cold.1
- ___30-[WPClient stopTrackingZones:]_block_invoke.546.cold.2
- ___30-[WPClient stopTrackingZones:]_block_invoke_2.549
- ___31-[WPClient overrideAdvTimeout:]_block_invoke.636
- ___31-[WPClient overrideAdvTimeout:]_block_invoke.636.cold.1
- ___31-[WPClient overrideAdvTimeout:]_block_invoke.636.cold.2
- ___31-[WPClient overrideAdvTimeout:]_block_invoke_2.639
- ___32-[WPClient enableBubbleTestMode]_block_invoke.620
- ___32-[WPClient enableBubbleTestMode]_block_invoke.620.cold.1
- ___32-[WPClient enableBubbleTestMode]_block_invoke.620.cold.2
- ___32-[WPClient enableBubbleTestMode]_block_invoke_2.623
- ___32-[WPClient overrideScanTimeout:]_block_invoke.628
- ___32-[WPClient overrideScanTimeout:]_block_invoke.628.cold.1
- ___32-[WPClient overrideScanTimeout:]_block_invoke.628.cold.2
- ___32-[WPClient overrideScanTimeout:]_block_invoke_2.631
- ___32-[WPClient stopTrackingAllZones]_block_invoke.554
- ___32-[WPClient stopTrackingAllZones]_block_invoke.554.cold.1
- ___32-[WPClient stopTrackingAllZones]_block_invoke.554.cold.2
- ___32-[WPClient stopTrackingAllZones]_block_invoke_2.557
- ___33-[WPClient checkAllowDuplicates:]_block_invoke.602
- ___33-[WPClient checkAllowDuplicates:]_block_invoke.602.cold.1
- ___33-[WPClient checkAllowDuplicates:]_block_invoke.602.cold.2
- ___33-[WPClient checkAllowDuplicates:]_block_invoke.608
- ___33-[WPClient checkAllowDuplicates:]_block_invoke_2.605
- ___38-[WPClient connectToPeer:withOptions:]_block_invoke.508
- ___38-[WPClient connectToPeer:withOptions:]_block_invoke.508.cold.1
- ___38-[WPClient connectToPeer:withOptions:]_block_invoke.508.cold.2
- ___38-[WPClient connectToPeer:withOptions:]_block_invoke.518
- ___38-[WPClient connectToPeer:withOptions:]_block_invoke_2.519
- ___38-[WPClient connectToPeer:withOptions:]_block_invoke_2.519.cold.1
- ___38-[WPClient connectToPeer:withOptions:]_block_invoke_2.519.cold.2
- ___42-[WPClient listenToBandwidthNotifications]_block_invoke.578
- ___42-[WPClient listenToBandwidthNotifications]_block_invoke.578.cold.1
- ___42-[WPClient listenToBandwidthNotifications]_block_invoke.578.cold.2
- ___42-[WPClient listenToBandwidthNotifications]_block_invoke_2.581
- ___45-[WPClient updateScanningRequest:withUpdate:]_block_invoke.483
- ___48-[WPClient updateAdvertisingRequest:withUpdate:]_block_invoke.445
- ___55-[WPClient sendDataToCharacteristic:inService:forPeer:]_block_invoke.530
- ___block_literal_global.383
- ___block_literal_global.403
- ___block_literal_global.408
- ___block_literal_global.410
- ___block_literal_global.416
- ___block_literal_global.429
- ___block_literal_global.435
- ___block_literal_global.440
- ___block_literal_global.442
- ___block_literal_global.444
- ___block_literal_global.449
- ___block_literal_global.454
- ___block_literal_global.470
- ___block_literal_global.475
- ___block_literal_global.480
- ___block_literal_global.482
- ___block_literal_global.487
- ___block_literal_global.492
- ___block_literal_global.494
- ___block_literal_global.499
- ___block_literal_global.501
- ___block_literal_global.506
- ___block_literal_global.513
- ___block_literal_global.521
- ___block_literal_global.523
- ___block_literal_global.532
- ___block_literal_global.537
- ___block_literal_global.540
- ___block_literal_global.543
- ___block_literal_global.545
- ___block_literal_global.548
- ___block_literal_global.551
- ___block_literal_global.553
- ___block_literal_global.556
- ___block_literal_global.559
- ___block_literal_global.561
- ___block_literal_global.564
- ___block_literal_global.567
- ___block_literal_global.569
- ___block_literal_global.580
- ___block_literal_global.583
- ___block_literal_global.585
- ___block_literal_global.588
- ___block_literal_global.591
- ___block_literal_global.594
- ___block_literal_global.597
- ___block_literal_global.599
- ___block_literal_global.604
- ___block_literal_global.607
- ___block_literal_global.614
- ___block_literal_global.617
- ___block_literal_global.619
- ___block_literal_global.622
- ___block_literal_global.625
- ___block_literal_global.627
- ___block_literal_global.630
- ___block_literal_global.633
- ___block_literal_global.635
- ___block_literal_global.638
- ___block_literal_global.641
- ___block_literal_global.643
- ___block_literal_global.646
- ___block_literal_global.649
- ___block_literal_global.656
- ___block_literal_global.659
- ___block_literal_global.661
- ___block_literal_global.664
- ___block_literal_global.667
- ___block_literal_global.669
- ___block_literal_global.672
- ___block_literal_global.675
- ___block_literal_global.677
- ___block_literal_global.824
CStrings:
+ "DOD"
+ "DOS"
+ "FindMyPair"
+ "FindMyTemporaryAggressiveLegacyExtendedRange"
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
+ "NearbyFaceTime"
+ "NearbyFaceTimeData"
+ "ProximityServiceDeviceSetup"
+ "SOSBeaconActivateAdvA"
+ "SOSBeaconActivateAdvB"
+ "SOSBeaconActivateScan"
+ "SOSBeaconPartA"
+ "SOSBeaconPartB"
+ "SOSBeaconPrecisionFindRequest"
+ "SOSBeaconPrecisionFindResponse"
+ "SOSBeaconScan"
+ "SharingHomePodSetup"
+ "T@\"NSData\",&,N,V_advertisingRandomData"
+ "WPClient can't reach bluetoothd to discover services and characteristics for peer %@. ERROR: %@"
+ "WPClient can't reach bluetoothd to subscribe characteristic for peer %@. ERROR: %@"
+ "_advertisingRandomData"
+ "advertising request of type %ld, priority %ld, UseFG %ld (%.2f ms), data %@, connectable %d, addr change %d, options %@, advertisementRequestedAt %llu, randomData %@"
+ "advertisingRandomData"
+ "handleStartScanningError:ofType:"
+ "kAdvertisingRandomData"
+ "setAdvertisingRandomData:"
+ "startScanning:withDispatch:"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "v28@0:8@\"WPScanRequest\"16B24"
- "WPClient can't reach bluetoothd to discover services and charactertistcs for peer %@. ERROR: %@"
- "WPClient can't reach bluetoothd to subscribe charactertistc for peer %@. ERROR: %@"
- "advertising request of type %ld, priority %ld, UseFG %ld (%.2f ms), data %@, connectable %d, addr change %d, options %@, advertisementRequestedAt %llu"

```
