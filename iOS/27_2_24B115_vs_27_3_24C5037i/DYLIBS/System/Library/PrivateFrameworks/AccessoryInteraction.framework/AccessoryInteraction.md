## AccessoryInteraction

> `/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`

```diff

-33.0.0.0.0
-  __TEXT.__text: 0x90878
-  __TEXT.__objc_methlist: 0x7010
-  __TEXT.__const: 0x9f0
+39.0.0.0.0
+  __TEXT.__text: 0x93594
+  __TEXT.__objc_methlist: 0x72d0
+  __TEXT.__const: 0xd60
   __TEXT.__oslogstring: 0x2a906
-  __TEXT.__cstring: 0x73d7
+  __TEXT.__cstring: 0x7427
   __TEXT.__gcc_except_tab: 0x104
-  __TEXT.__swift5_typeref: 0x3de
-  __TEXT.__swift5_fieldmd: 0x2c0
-  __TEXT.__constg_swiftt: 0x59c
-  __TEXT.__swift5_reflstr: 0x2a5
-  __TEXT.__swift5_capture: 0x140
-  __TEXT.__swift5_proto: 0xc
-  __TEXT.__swift5_types: 0x3c
-  __TEXT.__unwind_info: 0x1f10
+  __TEXT.__swift5_typeref: 0x67c
+  __TEXT.__swift5_reflstr: 0x3a5
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__swift5_fieldmd: 0x458
+  __TEXT.__constg_swiftt: 0x808
+  __TEXT.__swift5_capture: 0x150
+  __TEXT.__swift5_protos: 0x10
+  __TEXT.__swift5_proto: 0x1c
+  __TEXT.__swift5_types: 0x58
+  __TEXT.__unwind_info: 0x20c0
   __TEXT.__eh_frame: 0x198
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1220
-  __DATA_CONST.__objc_classlist: 0x218
+  __DATA_CONST.__const: 0x1230
+  __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0xc0
+  __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x44a8
-  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_selrefs: 0x44f8
+  __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0x58
-  __DATA_CONST.__got: 0x768
-  __AUTH_CONST.__const: 0xbf8
+  __DATA_CONST.__got: 0x7a0
+  __AUTH_CONST.__const: 0xe80
   __AUTH_CONST.__cfstring: 0x7d20
-  __AUTH_CONST.__objc_const: 0xbc38
+  __AUTH_CONST.__objc_const: 0xc5f8
   __AUTH_CONST.__objc_intobj: 0x390
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0xb08
-  __AUTH.__objc_data: 0x888
-  __AUTH.__data: 0xb8
+  __AUTH_CONST.__auth_got: 0xb88
+  __AUTH.__objc_data: 0x9f0
+  __AUTH.__data: 0x288
   __DATA.__objc_ivar: 0x700
-  __DATA.__data: 0x9a0
+  __DATA.__data: 0xb30
   __DATA_DIRTY.__objc_data: 0x1478
-  __DATA_DIRTY.__data: 0x308
+  __DATA_DIRTY.__data: 0x2e8
   __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2645
-  Symbols:   3713
-  CStrings:  2700
+  Functions: 2765
+  Symbols:   3810
+  CStrings:  2702
 
Symbols:
+ +[ANCentralManagerNullableShim startConnectionEventCounterOnCentralManager:forPeripheral:]
+ +[ANCentralManagerNullableShim stopConnectionEventCounterOnCentralManager:forPeripheral:]
+ +[ANDeviceManager retrievePeripheralFromCentralManager:material:isFindMyNetwork:]
+ +[ANDeviceManagerPeripheralRetriever retrievePeripheralFromCentralManager:material:isFindMyNetwork:]
+ +[ANMetricManager(RedactedSerialNumber) hashedSerialNumber:]
+ +[ANMetricManager(RedactedSerialNumber) productId:]
+ +[ANMetricManager(RedactedSerialNumber) redactedProductId:vendorId:]
+ -[ANDeviceManager initWithQueue:meDeviceMonitor:systemUtils:maintenance:zoneMonitor:metricManager:platform:settings:centralManager:beaconManager:]
+ -[ANDeviceManager simpleBeaconForUUID:]
+ -[ANMetricManager submitHardwareFaultsMetrics:serialNumber:isSharedWithUser:isMeDevice:firmwareVersion:productId:vendorId:]
+ -[ANService beginServiceWithScannerClient:zoneMonitor:commuteMetricManager:keyReconciler:]
+ GCC_except_table117
+ _OBJC_CLASS_$_ANCentralManagerNullableShim
+ _OBJC_CLASS_$_ANDeviceManagerPeripheralRetriever
+ _OBJC_CLASS_$_CBPeripheral
+ _OBJC_CLASS_$__TtC20AccessoryInteraction16ANCentralManager
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_ANService._centralManager
+ _OBJC_METACLASS_$_ANCentralManagerNullableShim
+ _OBJC_METACLASS_$_ANDeviceManagerPeripheralRetriever
+ _OBJC_METACLASS_$__TtC20AccessoryInteraction16ANCentralManager
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __DATA__TtC20AccessoryInteraction16ANCentralManager
+ __DATA__TtCO20AccessoryInteraction15ANCompanionLink7Request
+ __DATA__TtCO20AccessoryInteraction15ANCompanionLink7Session
+ __IVARS__TtC20AccessoryInteraction10ANThrottle
+ __IVARS__TtC20AccessoryInteraction16ANCentralManager
+ __IVARS__TtCO20AccessoryInteraction15ANCompanionLink7Request
+ __IVARS__TtCO20AccessoryInteraction15ANCompanionLink7Session
+ __METACLASS_DATA__TtC20AccessoryInteraction16ANCentralManager
+ __METACLASS_DATA__TtCO20AccessoryInteraction15ANCompanionLink7Request
+ __METACLASS_DATA__TtCO20AccessoryInteraction15ANCompanionLink7Session
+ __OBJC_$_CLASS_METHODS_ANCentralManagerNullableShim
+ __OBJC_$_CLASS_METHODS_ANDeviceManager
+ __OBJC_$_CLASS_METHODS_ANDeviceManagerPeripheralRetriever
+ __OBJC_$_CLASS_METHODS_ANMetricManager(RedactedSerialNumber)
+ __OBJC_$_INSTANCE_METHODS__TtC20AccessoryInteraction16ANCentralManager(AccessoryInteraction)
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ANSimpleBeaconProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__TtP20AccessoryInteraction24ANCentralManagerDelegate_
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ANSimpleBeaconProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES__TtP20AccessoryInteraction24ANCentralManagerDelegate_
+ __OBJC_CLASS_PROTOCOLS_$__TtC20AccessoryInteraction16ANCentralManager(AccessoryInteraction)
+ __OBJC_CLASS_RO_$_ANCentralManagerNullableShim
+ __OBJC_CLASS_RO_$_ANDeviceManagerPeripheralRetriever
+ __OBJC_LABEL_PROTOCOL_$_ANSimpleBeaconProvider
+ __OBJC_LABEL_PROTOCOL_$__TtP20AccessoryInteraction24ANCentralManagerDelegate_
+ __OBJC_METACLASS_RO_$_ANCentralManagerNullableShim
+ __OBJC_METACLASS_RO_$_ANDeviceManagerPeripheralRetriever
+ __OBJC_PROTOCOL_$_ANSimpleBeaconProvider
+ __OBJC_PROTOCOL_$__TtP20AccessoryInteraction24ANCentralManagerDelegate_
+ __PROPERTIES__TtC20AccessoryInteraction16ANCentralManager
+ __PROTOCOL_INSTANCE_METHODS__TtP20AccessoryInteraction24ANCentralManagerDelegate_
+ __PROTOCOL_METHOD_TYPES__TtP20AccessoryInteraction24ANCentralManagerDelegate_
+ __PROTOCOL__TtP20AccessoryInteraction24ANCentralManagerDelegate_
+ ___146-[ANDeviceManager initWithQueue:meDeviceMonitor:systemUtils:maintenance:zoneMonitor:metricManager:platform:settings:centralManager:beaconManager:]_block_invoke
+ ___146-[ANDeviceManager initWithQueue:meDeviceMonitor:systemUtils:maintenance:zoneMonitor:metricManager:platform:settings:centralManager:beaconManager:]_block_invoke_2
+ ___146-[ANDeviceManager initWithQueue:meDeviceMonitor:systemUtils:maintenance:zoneMonitor:metricManager:platform:settings:centralManager:beaconManager:]_block_invoke_3
+ ___146-[ANDeviceManager initWithQueue:meDeviceMonitor:systemUtils:maintenance:zoneMonitor:metricManager:platform:settings:centralManager:beaconManager:]_block_invoke_4
+ ___146-[ANDeviceManager initWithQueue:meDeviceMonitor:systemUtils:maintenance:zoneMonitor:metricManager:platform:settings:centralManager:beaconManager:]_block_invoke_5
+ ___90-[ANService beginServiceWithScannerClient:zoneMonitor:commuteMetricManager:keyReconciler:]_block_invoke
+ ___90-[ANService beginServiceWithScannerClient:zoneMonitor:commuteMetricManager:keyReconciler:]_block_invoke_2
+ ___swift_instantiateGenericMetadata
+ ___swift_memcpy16_8
+ ___swift_memcpy48_8
+ ___unnamed_1
+ _associated conformance 20AccessoryInteraction15ANCompanionLinkO7SessionC5StateOSHAASQ
+ _associated conformance 20AccessoryInteraction16ANCentralManagerCAA0cD8ProtocolAA10PeripheralAaDP_AA012ANPeripheralE0
+ _flat unique 20AccessoryInteraction24ANCentralManagerDelegate_p
+ _free
+ _get_enum_tag_for_layout_string 20AccessoryInteraction15ANCompanionLinkO7RequestC5State33_70D752575E908BC19625D1A5BE5475BDLLO
+ _objc_retain_x28
+ _swift_allocateGenericClassMetadata
+ _swift_coroFrameAlloc
+ _swift_deallocClassInstance
+ _swift_getGenericMetadata
+ _swift_initClassMetadata2
+ _swift_release_x1
+ _swift_retain_x19
+ _swift_unknownObjectWeakAssign
+ _symbolic $s20AccessoryInteraction15ANCompanionLinkO9TransportP
+ _symbolic $s20AccessoryInteraction20ANPeripheralProtocolP
+ _symbolic $s20AccessoryInteraction21ANPeripheralRetrieverP
+ _symbolic $s20AccessoryInteraction24ANCentralManagerDelegateP
+ _symbolic $s20AccessoryInteraction24ANCentralManagerProtocolP
+ _symbolic 10Peripheral_____Qz 20AccessoryInteraction21ANPeripheralRetrieverP
+ _symbolic 10Peripheral_____Qz 20AccessoryInteraction24ANCentralManagerProtocolP
+ _symbolic SDy__________G s5UInt8V 20AccessoryInteraction15ANCompanionLinkO7RequestC
+ _symbolic SDyxSdG
+ _symbolic SSSg12serialNumber_SS15firmwareVersionSi9productIdSi06vendorF0t
+ _symbolic SS_ypt
+ _symbolic So12CBPeripheralC
+ _symbolic So16CBCentralManagerC
+ _symbolic So7NSErrorCSgIeyBy_
+ _symbolic _____ 10Foundation4DataV
+ _symbolic _____ 20AccessoryInteraction10ANThrottleC
+ _symbolic _____ 20AccessoryInteraction15ANCompanionLinkO
+ _symbolic _____ 20AccessoryInteraction15ANCompanionLinkO7RequestC
+ _symbolic _____ 20AccessoryInteraction15ANCompanionLinkO7RequestC5State33_70D752575E908BC19625D1A5BE5475BDLLO
+ _symbolic _____ 20AccessoryInteraction15ANCompanionLinkO7SessionC
+ _symbolic _____ 20AccessoryInteraction15ANCompanionLinkO7SessionC5StateO
+ _symbolic _____ 20AccessoryInteraction16ANCentralManagerC
+ _symbolic _____ s5UInt8V
+ _symbolic ______pSgXw 20AccessoryInteraction24ANCentralManagerDelegateP
+ _symbolic _____ySS_yptG s23_ContiguousArrayStorageC
+ _symbolic _____y_____ypG s18_DictionaryStorageC s11AnyHashableV
+ _symbolic x
+ _symbolic y______pc 20AccessoryInteraction15ANCompanionLinkO9TransportP
+ _symbolic y_____y___________pGc10onResponse_t s6ResultOsRi_zRi0_zrlE 10Foundation4DataV s5ErrorP
+ _symbolic y_____y___________pGcSg s6ResultOsRi_zRi0_zrlE 10Foundation4DataV s5ErrorP
+ _symbolic y_____yyt______pGc s6ResultOsRi_zRi0_zrlE s5ErrorP
+ _type_layout_string 20AccessoryInteraction15ANCompanionLinkO7RequestC5State33_70D752575E908BC19625D1A5BE5475BDLLO
- -[ANDeviceManager initWithQueue:meDeviceMonitor:systemUtils:maintenance:zoneMonitor:metricManager:platform:settings:]
- -[ANMetricManager submitHardwareFaultsMetrics:serialNumber:isSharedWithUser:isMeDevice:firmwareVersion:]
- GCC_except_table116
- _OBJC_IVAR_$_ANService._keyReconciler
- __OBJC_$_CLASS_METHODS_ANMetricManager
- ___117-[ANDeviceManager initWithQueue:meDeviceMonitor:systemUtils:maintenance:zoneMonitor:metricManager:platform:settings:]_block_invoke
- ___117-[ANDeviceManager initWithQueue:meDeviceMonitor:systemUtils:maintenance:zoneMonitor:metricManager:platform:settings:]_block_invoke_2
- ___117-[ANDeviceManager initWithQueue:meDeviceMonitor:systemUtils:maintenance:zoneMonitor:metricManager:platform:settings:]_block_invoke_3
- ___117-[ANDeviceManager initWithQueue:meDeviceMonitor:systemUtils:maintenance:zoneMonitor:metricManager:platform:settings:]_block_invoke_4
- ___117-[ANDeviceManager initWithQueue:meDeviceMonitor:systemUtils:maintenance:zoneMonitor:metricManager:platform:settings:]_block_invoke_5
- ___76-[ANService beginServiceWithScannerClient:zoneMonitor:commuteMetricManager:]_block_invoke
- ___76-[ANService beginServiceWithScannerClient:zoneMonitor:commuteMetricManager:]_block_invoke_2
- ___swift_memcpy32_8
- _symbolic SS12serialNumber_SS15firmwareVersiont
CStrings:
+ "AccessoryInteraction.ANCentralManager"
+ "ProximityServiceThirdPartyHomeSetup"
+ "faults"
- "5612"
```
