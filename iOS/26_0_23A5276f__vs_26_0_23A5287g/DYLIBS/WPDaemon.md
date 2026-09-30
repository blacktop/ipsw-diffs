## WPDaemon

> `/System/Library/PrivateFrameworks/WPDaemon.framework/WPDaemon`

```diff

-190.43.0.0.0
+190.45.1.0.0
   __TEXT.__text: 0x5de7c
   __TEXT.__auth_stubs: 0x8d0
   __TEXT.__objc_methlist: 0x4294
-  __TEXT.__cstring: 0x4495
+  __TEXT.__cstring: 0x44a7
   __TEXT.__const: 0x218
-  __TEXT.__oslogstring: 0xa8a9
+  __TEXT.__oslogstring: 0xa8ab
   __TEXT.__gcc_except_tab: 0x16dc
-  __TEXT.__unwind_info: 0x1e60
+  __TEXT.__unwind_info: 0x1e68
   __TEXT.__objc_classname: 0x37a
   __TEXT.__objc_methname: 0x9f2c
   __TEXT.__objc_methtype: 0x1680

   __DATA_CONST.__objc_selrefs: 0x26d8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xd0
-  __DATA_CONST.__objc_arraydata: 0x2b8
+  __DATA_CONST.__objc_arraydata: 0x2c0
   __AUTH_CONST.__auth_got: 0x478
   __AUTH_CONST.__const: 0x6920
-  __AUTH_CONST.__cfstring: 0x33c0
+  __AUTH_CONST.__cfstring: 0x33e0
   __AUTH_CONST.__objc_const: 0x8498
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F59E38C5-EEC1-3F55-BD36-35422EFE83D9
+  UUID: 09742775-1F26-3047-9ED7-447FBEB167DD
   Functions: 3402
   Symbols:   10028
-  CStrings:  4002
+  CStrings:  4004
 
Symbols:
+ ___20-[WPDClient destroy]_block_invoke.588
+ ___26-[WPDClient destroy_async]_block_invoke.594
+ ___26-[WPDClient stopScanning:]_block_invoke.757
+ ___27-[WPDClient tickleMachPort]_block_invoke.571
+ ___28-[WPDClient setupConnection]_block_invoke.579
+ ___28-[WPDClient setupConnection]_block_invoke.579.cold.1
+ ___28-[WPDClient setupConnection]_block_invoke_2.580
+ ___29-[WPDClient sendTestRequest:]_block_invoke.990
+ ___29-[WPDClient stopAdvertising:]_block_invoke.655
+ ___30+[WPDClient generateStateDump]_block_invoke.468
+ ___30-[WPDClient discoveredDevice:]_block_invoke.685
+ ___30-[WPDClient startAdvertising:]_block_invoke.612
+ ___31-[WPDClient createdConnection:]_block_invoke.878
+ ___31-[WPDClient discoveredDevices:]_block_invoke.689
+ ___32-[WPDClient disconnectFromPeer:]_block_invoke.854
+ ___32-[WPDClient stopScanning_async:]_block_invoke.769
+ ___33-[WPDClient anyDiscoveredDevice:]_block_invoke.692
+ ___33-[WPDClient enableRanging:reply:]_block_invoke.943
+ ___33-[WPDClient startScanning_async:]_block_invoke.702
+ ___33-[WPDClient startScanning_async:]_block_invoke.708
+ ___33-[WPDClient startScanning_async:]_block_invoke.714
+ ___33-[WPDClient startScanning_async:]_block_invoke.720
+ ___33-[WPDClient startScanning_async:]_block_invoke.738.cold.1
+ ___33-[WPDClient startScanning_async:]_block_invoke.738.cold.2
+ ___33-[WPDClient startScanning_async:]_block_invoke.744
+ ___33-[WPDClient startScanning_async:]_block_invoke.744.cold.1
+ ___33-[WPDClient startScanning_async:]_block_invoke.744.cold.2
+ ___33-[WPDClient startScanning_async:]_block_invoke.744.cold.3
+ ___33-[WPDClient startScanning_async:]_block_invoke.751
+ ___33-[WPDClient startScanning_async:]_block_invoke_2.745
+ ___34-[WPDClient verifyApprovedUseCase]_block_invoke.463
+ ___35-[WPDClient stopAdvertising_async:]_block_invoke.664
+ ___36-[WPDClient disconnectedPeer:error:]_block_invoke.859
+ ___36-[WPDClient disconnectedPeer:error:]_block_invoke.865
+ ___36-[WPDClient startAdvertising_async:]_block_invoke.615
+ ___36-[WPDClient startAdvertising_async:]_block_invoke.625.cold.1
+ ___36-[WPDClient startAdvertising_async:]_block_invoke.625.cold.2
+ ___36-[WPDClient startAdvertising_async:]_block_invoke.631
+ ___36-[WPDClient startAdvertising_async:]_block_invoke.631.cold.1
+ ___36-[WPDClient startAdvertising_async:]_block_invoke.631.cold.2
+ ___36-[WPDClient startAdvertising_async:]_block_invoke.631.cold.3
+ ___36-[WPDClient startAdvertising_async:]_block_invoke.638
+ ___36-[WPDClient startAdvertising_async:]_block_invoke.642
+ ___36-[WPDClient startAdvertising_async:]_block_invoke.650
+ ___36-[WPDClient startAdvertising_async:]_block_invoke_2.632
+ ___39-[WPDClient connectToPeer:withOptions:]_block_invoke.818
+ ___39-[WPDClient connectedDeviceOverLEPipe:]_block_invoke.840
+ ___40-[WPDClient startScanning:withDispatch:]_block_invoke.696
+ ___42-[WPDClient initWithXPCConnection:server:]_block_invoke.484
+ ___42-[WPDClient initWithXPCConnection:server:]_block_invoke.490
+ ___42-[WPDClient initWithXPCConnection:server:]_block_invoke.490.cold.1
+ ___42-[WPDClient initWithXPCConnection:server:]_block_invoke.490.cold.2
+ ___45-[WPDClient clearDuplicateFilterCache_async:]_block_invoke.783
+ ___48-[WPDClient advertisingStoppedOfType:withError:]_block_invoke.675
+ ___48-[WPDClient notifyClientStateChange:Restricted:]_block_invoke.680
+ ___54-[WPDClient connectedDevice:withError:shouldDiscover:]_block_invoke.832
+ ___56-[WPDClient sendDataToCharacteristic:inService:forPeer:]_block_invoke.922
+ ___59-[WPDClient central:subscribed:toCharacteristic:inService:]_block_invoke.901
+ ___62-[WPDClient discoverCharacteristicsAndServices:forPeripheral:]_block_invoke.909
+ ___65-[WPDClient registerWithDaemon:forProcess:machName:holdVouchers:]_block_invoke.522
+ ___65-[WPDClient shouldSubscribe:toPeer:withCharacteristic:inService:]_block_invoke.885
+ ___81-[WPDClient updatedNotificationState:forCharacteristic:inService:withPeripheral:]_block_invoke.890
+ ___block_literal_global.470
+ ___block_literal_global.481
+ ___block_literal_global.497
+ ___block_literal_global.521
+ ___block_literal_global.597
+ ___block_literal_global.599
+ ___block_literal_global.609
+ ___block_literal_global.617
+ ___block_literal_global.630
+ ___block_literal_global.640
+ ___block_literal_global.644
+ ___block_literal_global.666
+ ___block_literal_global.670
+ ___block_literal_global.672
+ ___block_literal_global.677
+ ___block_literal_global.687
+ ___block_literal_global.698
+ ___block_literal_global.771
+ ___block_literal_global.787
+ ___block_literal_global.789
+ ___block_literal_global.791
+ ___block_literal_global.793
+ ___block_literal_global.799
+ ___block_literal_global.801
+ ___block_literal_global.823
+ ___block_literal_global.834
+ ___block_literal_global.842
+ ___block_literal_global.856
+ ___block_literal_global.861
+ ___block_literal_global.867
+ ___block_literal_global.869
+ ___block_literal_global.880
+ ___block_literal_global.882
+ ___block_literal_global.887
+ ___block_literal_global.892
+ ___block_literal_global.903
+ ___block_literal_global.911
+ ___block_literal_global.913
+ ___block_literal_global.924
+ ___block_literal_global.929
+ ___block_literal_global.931
+ ___block_literal_global.933
+ ___block_literal_global.935
+ ___block_literal_global.937
+ ___block_literal_global.945
+ ___block_literal_global.950
+ ___block_literal_global.955
+ ___block_literal_global.959
+ ___block_literal_global.961
+ ___block_literal_global.969
+ ___block_literal_global.971
+ ___block_literal_global.976
+ ___block_literal_global.978
+ ___block_literal_global.980
+ ___block_literal_global.982
+ ___block_literal_global.984
+ ___block_literal_global.992
+ ___block_literal_global.994
- ___20-[WPDClient destroy]_block_invoke.582
- ___26-[WPDClient destroy_async]_block_invoke.588
- ___26-[WPDClient stopScanning:]_block_invoke.754
- ___27-[WPDClient tickleMachPort]_block_invoke.568
- ___28-[WPDClient setupConnection]_block_invoke.576
- ___28-[WPDClient setupConnection]_block_invoke.576.cold.1
- ___28-[WPDClient setupConnection]_block_invoke_2.577
- ___29-[WPDClient sendTestRequest:]_block_invoke.984
- ___29-[WPDClient stopAdvertising:]_block_invoke.652
- ___30+[WPDClient generateStateDump]_block_invoke.465
- ___30-[WPDClient discoveredDevice:]_block_invoke.682
- ___30-[WPDClient startAdvertising:]_block_invoke.609
- ___31-[WPDClient createdConnection:]_block_invoke.869
- ___31-[WPDClient discoveredDevices:]_block_invoke.686
- ___32-[WPDClient disconnectFromPeer:]_block_invoke.842
- ___32-[WPDClient stopScanning_async:]_block_invoke.757
- ___33-[WPDClient anyDiscoveredDevice:]_block_invoke.689
- ___33-[WPDClient enableRanging:reply:]_block_invoke.940
- ___33-[WPDClient startScanning_async:]_block_invoke.699
- ___33-[WPDClient startScanning_async:]_block_invoke.705
- ___33-[WPDClient startScanning_async:]_block_invoke.711
- ___33-[WPDClient startScanning_async:]_block_invoke.717
- ___33-[WPDClient startScanning_async:]_block_invoke.723
- ___33-[WPDClient startScanning_async:]_block_invoke.735.cold.1
- ___33-[WPDClient startScanning_async:]_block_invoke.735.cold.2
- ___33-[WPDClient startScanning_async:]_block_invoke.741.cold.1
- ___33-[WPDClient startScanning_async:]_block_invoke.741.cold.2
- ___33-[WPDClient startScanning_async:]_block_invoke.741.cold.3
- ___33-[WPDClient startScanning_async:]_block_invoke.745
- ___33-[WPDClient startScanning_async:]_block_invoke_2.742
- ___34-[WPDClient verifyApprovedUseCase]_block_invoke.457
- ___35-[WPDClient stopAdvertising_async:]_block_invoke.655
- ___36-[WPDClient disconnectedPeer:error:]_block_invoke.856
- ___36-[WPDClient disconnectedPeer:error:]_block_invoke.862
- ___36-[WPDClient startAdvertising_async:]_block_invoke.612
- ___36-[WPDClient startAdvertising_async:]_block_invoke.616
- ___36-[WPDClient startAdvertising_async:]_block_invoke.622.cold.1
- ___36-[WPDClient startAdvertising_async:]_block_invoke.622.cold.2
- ___36-[WPDClient startAdvertising_async:]_block_invoke.628.cold.1
- ___36-[WPDClient startAdvertising_async:]_block_invoke.628.cold.2
- ___36-[WPDClient startAdvertising_async:]_block_invoke.628.cold.3
- ___36-[WPDClient startAdvertising_async:]_block_invoke.632
- ___36-[WPDClient startAdvertising_async:]_block_invoke.639
- ___36-[WPDClient startAdvertising_async:]_block_invoke.647
- ___36-[WPDClient startAdvertising_async:]_block_invoke_2.629
- ___39-[WPDClient connectToPeer:withOptions:]_block_invoke.803
- ___39-[WPDClient connectedDeviceOverLEPipe:]_block_invoke.834
- ___40-[WPDClient startScanning:withDispatch:]_block_invoke.693
- ___42-[WPDClient initWithXPCConnection:server:]_block_invoke.481
- ___42-[WPDClient initWithXPCConnection:server:]_block_invoke.487
- ___42-[WPDClient initWithXPCConnection:server:]_block_invoke.487.cold.1
- ___42-[WPDClient initWithXPCConnection:server:]_block_invoke.487.cold.2
- ___45-[WPDClient clearDuplicateFilterCache_async:]_block_invoke.771
- ___48-[WPDClient advertisingStoppedOfType:withError:]_block_invoke.672
- ___48-[WPDClient notifyClientStateChange:Restricted:]_block_invoke.677
- ___54-[WPDClient connectedDevice:withError:shouldDiscover:]_block_invoke.823
- ___56-[WPDClient sendDataToCharacteristic:inService:forPeer:]_block_invoke.913
- ___59-[WPDClient central:subscribed:toCharacteristic:inService:]_block_invoke.892
- ___62-[WPDClient discoverCharacteristicsAndServices:forPeripheral:]_block_invoke.906
- ___65-[WPDClient registerWithDaemon:forProcess:machName:holdVouchers:]_block_invoke.513
- ___65-[WPDClient shouldSubscribe:toPeer:withCharacteristic:inService:]_block_invoke.882
- ___81-[WPDClient updatedNotificationState:forCharacteristic:inService:withPeripheral:]_block_invoke.887
- ___block_literal_global.464
- ___block_literal_global.478
- ___block_literal_global.483
- ___block_literal_global.499
- ___block_literal_global.572
- ___block_literal_global.594
- ___block_literal_global.596
- ___block_literal_global.606
- ___block_literal_global.608
- ___block_literal_global.618
- ___block_literal_global.631
- ___block_literal_global.651
- ___block_literal_global.665
- ___block_literal_global.667
- ___block_literal_global.669
- ___block_literal_global.681
- ___block_literal_global.692
- ___block_literal_global.701
- ___block_literal_global.707
- ___block_literal_global.744
- ___block_literal_global.770
- ___block_literal_global.784
- ___block_literal_global.786
- ___block_literal_global.790
- ___block_literal_global.794
- ___block_literal_global.796
- ___block_literal_global.798
- ___block_literal_global.805
- ___block_literal_global.822
- ___block_literal_global.833
- ___block_literal_global.841
- ___block_literal_global.864
- ___block_literal_global.866
- ___block_literal_global.868
- ___block_literal_global.879
- ___block_literal_global.881
- ___block_literal_global.886
- ___block_literal_global.891
- ___block_literal_global.905
- ___block_literal_global.910
- ___block_literal_global.912
- ___block_literal_global.926
- ___block_literal_global.928
- ___block_literal_global.930
- ___block_literal_global.932
- ___block_literal_global.934
- ___block_literal_global.942
- ___block_literal_global.947
- ___block_literal_global.952
- ___block_literal_global.956
- ___block_literal_global.958
- ___block_literal_global.966
- ___block_literal_global.968
- ___block_literal_global.973
- ___block_literal_global.975
- ___block_literal_global.977
- ___block_literal_global.979
- ___block_literal_global.981
- ___block_literal_global.983
- ___block_literal_global.991
CStrings:
+ "WPDaemon iOS 26.0 (23A5287c) (WirelessProximity-190.45.1) (Release) built on 2025-06-30 23:13:35"
+ "com.apple.Setup"
- "WPDaemon iOS 26.0 (23A5275s) (WirelessProximity-190.43) (Release) built on 2025-06-14 08:58:18"

```
