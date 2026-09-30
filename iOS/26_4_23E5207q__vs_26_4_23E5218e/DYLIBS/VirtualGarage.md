## VirtualGarage

> `/System/Library/PrivateFrameworks/VirtualGarage.framework/VirtualGarage`

```diff

-2391.34.7.17.27
-  __TEXT.__text: 0x2f770
+2391.34.7.17.30
+  __TEXT.__text: 0x31260
   __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_methlist: 0x1eec
-  __TEXT.__const: 0x198
-  __TEXT.__gcc_except_tab: 0x1078
-  __TEXT.__cstring: 0x37ef
-  __TEXT.__oslogstring: 0x4c89
-  __TEXT.__unwind_info: 0x9f0
+  __TEXT.__objc_methlist: 0x1f14
+  __TEXT.__const: 0x1a0
+  __TEXT.__gcc_except_tab: 0x124c
+  __TEXT.__cstring: 0x3b14
+  __TEXT.__oslogstring: 0x4c25
+  __TEXT.__unwind_info: 0xae8
   __TEXT.__objc_classname: 0x3ea
-  __TEXT.__objc_methname: 0x4c37
-  __TEXT.__objc_methtype: 0xbfc
-  __TEXT.__objc_stubs: 0x3c60
+  __TEXT.__objc_methname: 0x4c80
+  __TEXT.__objc_methtype: 0xc1c
+  __TEXT.__objc_stubs: 0x3ce0
   __DATA_CONST.__got: 0x370
-  __DATA_CONST.__const: 0x1148
+  __DATA_CONST.__const: 0x1170
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1338
+  __DATA_CONST.__objc_selrefs: 0x1350
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x48
   __AUTH_CONST.__auth_got: 0x370
   __AUTH_CONST.__const: 0x6a0
   __AUTH_CONST.__cfstring: 0x13e0
-  __AUTH_CONST.__objc_const: 0x3240
+  __AUTH_CONST.__objc_const: 0x3248
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A1C101D7-4080-31CD-A671-C9509477A137
-  Functions: 735
-  Symbols:   2838
-  CStrings:  1847
+  UUID: 1D706551-D832-3332-84AE-2EB99AEBA37F
+  Functions: 752
+  Symbols:   2893
+  CStrings:  1862
 
Symbols:
+ -[VGDataCoordinator vehicleWithIdentifier:]
+ -[VGExternalAccessoryState initWithVehicle:]
+ -[VGVirtualGarage _waitForGarageUpdateIfNecessary:]
+ GCC_except_table242
+ GCC_except_table270
+ GCC_except_table347
+ GCC_except_table383
+ GCC_except_table419
+ GCC_except_table461
+ GCC_except_table475
+ GCC_except_table476
+ GCC_except_table478
+ GCC_except_table479
+ GCC_except_table480
+ GCC_except_table481
+ GCC_except_table482
+ GCC_except_table483
+ GCC_except_table484
+ GCC_except_table488
+ GCC_except_table490
+ GCC_except_table492
+ GCC_except_table496
+ GCC_except_table499
+ GCC_except_table501
+ GCC_except_table503
+ GCC_except_table517
+ GCC_except_table524
+ GCC_except_table525
+ GCC_except_table528
+ GCC_except_table529
+ GCC_except_table531
+ GCC_except_table532
+ GCC_except_table535
+ GCC_except_table536
+ GCC_except_table538
+ GCC_except_table539
+ GCC_except_table540
+ GCC_except_table543
+ GCC_except_table544
+ GCC_except_table606
+ GCC_except_table610
+ GCC_except_table613
+ GCC_except_table618
+ GCC_except_table625
+ GCC_except_table668
+ GCC_except_table672
+ GCC_except_table677
+ GCC_except_table733
+ GCC_except_table738
+ GCC_except_table741
+ GCC_except_table743
+ ___43-[VGDataCoordinator vehicleWithIdentifier:]_block_invoke
+ ___43-[VGVirtualGarage virtualGarageAddVehicle:]_block_invoke
+ ___44-[VGVirtualGarage virtualGarageSaveVehicle:]_block_invoke
+ ___46-[VGVirtualGarage virtualGarageRemoveVehicle:]_block_invoke
+ ___46-[VGVirtualGarage virtualGarageSelectVehicle:]_block_invoke.30
+ ___47-[VGVirtualGarage virtualGarageOnboardVehicle:]_block_invoke
+ ___51-[VGVirtualGarage _waitForGarageUpdateIfNecessary:]_block_invoke
+ ___52-[VGVirtualGarage virtualGarageEndContinuousUpdates]_block_invoke
+ ___53-[VGVirtualGarage virtualGarageForceFetchAllVehicles]_block_invoke
+ ___53-[VGVirtualGarage virtualGarageSetAssumesFullCharge:]_block_invoke
+ ___62-[VGVirtualGarage virtualGarageStartContinuousUpdatesIfNeeded]_block_invoke
+ ___67-[VGVirtualGarage virtualGarageGetListOfUnpairedVehiclesWithReply:]_block_invoke
+ ___73-[VGVirtualGarage virtualGarageSetShouldUsePreferredNetworks:forVehicle:]_block_invoke
+ ___98-[VGVirtualGarage virtualGarageGetLatestStateOfVehicleWithIdentifier:syncAcrossDevices:withReply:]_block_invoke.38
+ ___98-[VGVirtualGarage virtualGarageGetLatestStateOfVehicleWithIdentifier:syncAcrossDevices:withReply:]_block_invoke.47
+ ___98-[VGVirtualGarage virtualGarageGetLatestStateOfVehicleWithIdentifier:syncAcrossDevices:withReply:]_block_invoke.48
+ ___Block_byref_object_copy_.815
+ ___Block_byref_object_dispose_.816
+ ___block_descriptor_41_e8_32w_e5_v8?0lw32l8
+ ___block_literal_global.1223
+ ___block_literal_global.17.344
+ ___block_literal_global.1734
+ ___block_literal_global.1959
+ ___block_literal_global.2097
+ ___block_literal_global.33
+ ___block_literal_global.367
+ ___block_literal_global.457
+ ___block_literal_global.805
+ ___block_literal_global.925
+ _objc_msgSend$_waitForGarageUpdateIfNecessary:
+ _objc_msgSend$displayedBatteryPercentage
+ _objc_msgSend$initWithVehicle:
+ _objc_msgSend$vehicleWithIdentifier:
- GCC_except_table240
- GCC_except_table268
- GCC_except_table344
- GCC_except_table380
- GCC_except_table416
- GCC_except_table458
- GCC_except_table472
- GCC_except_table474
- GCC_except_table477
- GCC_except_table495
- GCC_except_table498
- GCC_except_table504
- GCC_except_table506
- GCC_except_table507
- GCC_except_table508
- GCC_except_table510
- GCC_except_table514
- GCC_except_table518
- GCC_except_table519
- GCC_except_table526
- GCC_except_table589
- GCC_except_table593
- GCC_except_table596
- GCC_except_table601
- GCC_except_table608
- GCC_except_table651
- GCC_except_table655
- GCC_except_table660
- GCC_except_table716
- GCC_except_table721
- GCC_except_table724
- GCC_except_table726
- ___98-[VGVirtualGarage virtualGarageGetLatestStateOfVehicleWithIdentifier:syncAcrossDevices:withReply:]_block_invoke.44
- ___98-[VGVirtualGarage virtualGarageGetLatestStateOfVehicleWithIdentifier:syncAcrossDevices:withReply:]_block_invoke.45
- ___Block_byref_object_copy_.827
- ___Block_byref_object_dispose_.828
- ___block_literal_global.1213
- ___block_literal_global.17.346
- ___block_literal_global.1721
- ___block_literal_global.1938
- ___block_literal_global.2074
- ___block_literal_global.31
- ___block_literal_global.369
- ___block_literal_global.458
- ___block_literal_global.817
- ___block_literal_global.938
CStrings:
+ "-[VGVirtualGarage virtualGarageAddVehicle:]_block_invoke"
+ "-[VGVirtualGarage virtualGarageEndContinuousUpdates]_block_invoke"
+ "-[VGVirtualGarage virtualGarageForceFetchAllVehicles]_block_invoke"
+ "-[VGVirtualGarage virtualGarageGetGarageWithReply:]_block_invoke"
+ "-[VGVirtualGarage virtualGarageGetListOfUnpairedVehiclesWithReply:]_block_invoke"
+ "-[VGVirtualGarage virtualGarageOnboardVehicle:]_block_invoke"
+ "-[VGVirtualGarage virtualGarageRemoveVehicle:]_block_invoke"
+ "-[VGVirtualGarage virtualGarageSaveVehicle:]_block_invoke"
+ "-[VGVirtualGarage virtualGarageSelectVehicle:]_block_invoke"
+ "-[VGVirtualGarage virtualGarageSetAssumesFullCharge:]_block_invoke"
+ "-[VGVirtualGarage virtualGarageSetShouldUsePreferredNetworks:forVehicle:]_block_invoke"
+ "-[VGVirtualGarage virtualGarageStartContinuousUpdatesIfNeeded]_block_invoke"
+ "@\"VGVehicle\"24@0:8@\"NSString\"16"
+ "_waitForGarageUpdateIfNecessary:"
+ "initWithVehicle:"
+ "vehicleWithIdentifier:"
- "Garage hasn't finished loading vehicles from persistor. Once finished, reply block will be executed"

```
