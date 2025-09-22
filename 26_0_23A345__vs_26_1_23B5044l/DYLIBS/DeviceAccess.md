## DeviceAccess

> `/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess`

```diff

-320.40.0.0.0
-  __TEXT.__text: 0x2775c
+321.4.1.0.0
+  __TEXT.__text: 0x29970
   __TEXT.__auth_stubs: 0xe30
-  __TEXT.__objc_methlist: 0x24a4
-  __TEXT.__cstring: 0x51f7
+  __TEXT.__objc_methlist: 0x265c
+  __TEXT.__cstring: 0x53c7
   __TEXT.__gcc_except_tab: 0x75c
   __TEXT.__const: 0x24a
   __TEXT.__swift5_typeref: 0x119

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x940
-  __TEXT.__objc_classname: 0x362
-  __TEXT.__objc_methname: 0x518c
-  __TEXT.__objc_methtype: 0x790
-  __TEXT.__objc_stubs: 0x2ae0
-  __DATA_CONST.__got: 0x2b8
-  __DATA_CONST.__const: 0x890
-  __DATA_CONST.__objc_classlist: 0x108
+  __TEXT.__unwind_info: 0x9a8
+  __TEXT.__objc_classname: 0x382
+  __TEXT.__objc_methname: 0x561f
+  __TEXT.__objc_methtype: 0x7b9
+  __TEXT.__objc_stubs: 0x2be0
+  __DATA_CONST.__got: 0x300
+  __DATA_CONST.__const: 0x928
+  __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12a8
+  __DATA_CONST.__objc_selrefs: 0x1368
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0xd0
+  __DATA_CONST.__objc_superrefs: 0xd8
   __AUTH_CONST.__auth_got: 0x728
-  __AUTH_CONST.__const: 0x438
-  __AUTH_CONST.__cfstring: 0x2100
-  __AUTH_CONST.__objc_const: 0x4340
+  __AUTH_CONST.__const: 0x458
+  __AUTH_CONST.__cfstring: 0x2180
+  __AUTH_CONST.__objc_const: 0x45b0
   __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x3c0
+  __AUTH.__objc_data: 0x320
+  __DATA.__objc_ivar: 0x3e0
   __DATA.__data: 0x738
   __DATA.__bss: 0x140
   __DATA_DIRTY.__objc_data: 0x780

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C986323E-E6E5-301C-A12A-9DCDAEB7304E
-  Functions: 1134
-  Symbols:   3479
-  CStrings:  2181
+  UUID: A8A43C52-ED06-39E6-86FD-3819657F4F15
+  Functions: 1178
+  Symbols:   3612
+  CStrings:  2241
 
Symbols:
+ +[DADeviceAccessoryServiceInfo supportsSecureCoding]
+ +[DASession setDeviceAccessoryServiceInfo:device:session:error:]
+ -[DADevice accessoryServicesInternalMap]
+ -[DADevice accessoryServicesMap]
+ -[DADevice bluetoothAdvertisementData]
+ -[DADevice bluetoothRSSI]
+ -[DADevice connectionStatus]
+ -[DADevice decodeXPCAdvData:]
+ -[DADevice encodeXPCAdvData:]
+ -[DADevice setAccessoryServicesInternalMap:]
+ -[DADevice setBluetoothAdvertisementData:]
+ -[DADevice setBluetoothRSSI:]
+ -[DADevice setConnectionStatus:]
+ -[DADeviceAccessoryServiceInfo .cxx_destruct]
+ -[DADeviceAccessoryServiceInfo associatedBundleID]
+ -[DADeviceAccessoryServiceInfo associatedDeviceID]
+ -[DADeviceAccessoryServiceInfo authorizationLevel]
+ -[DADeviceAccessoryServiceInfo copyWithZone:]
+ -[DADeviceAccessoryServiceInfo descriptionWithLevel:]
+ -[DADeviceAccessoryServiceInfo description]
+ -[DADeviceAccessoryServiceInfo encodeWithCoder:]
+ -[DADeviceAccessoryServiceInfo encodeWithXPCObject:]
+ -[DADeviceAccessoryServiceInfo hash]
+ -[DADeviceAccessoryServiceInfo initWithCoder:]
+ -[DADeviceAccessoryServiceInfo initWithCoder:].cold.1
+ -[DADeviceAccessoryServiceInfo initWithName:authorizationLevel:bundleID:deviceID:]
+ -[DADeviceAccessoryServiceInfo initWithPersistentDictionaryRepresentation:deviceID:error:]
+ -[DADeviceAccessoryServiceInfo initWithPersistentDictionaryRepresentation:deviceID:error:].cold.1
+ -[DADeviceAccessoryServiceInfo initWithXPCObject:error:]
+ -[DADeviceAccessoryServiceInfo isEqual:]
+ -[DADeviceAccessoryServiceInfo name]
+ -[DADeviceAccessoryServiceInfo persistentDictionaryRepresentation]
+ -[DADeviceAccessoryServiceInfo setAuthorizationLevel:]
+ -[DASession launchInteractionWithDevice:flags:reason:completionHandler:]
+ -[DASession requestPermissionForDevice:services:completionHandler:]
+ -[DASession setDeviceAccessoryServiceInfo:device:completionHandler:]
+ GCC_except_table17
+ GCC_except_table3
+ GCC_except_table45
+ GCC_except_table49
+ GCC_except_table69
+ _CBAdvertisementDataIsConnectable
+ _CBAdvertisementDataLocalNameKey
+ _CBAdvertisementDataManufacturerDataKey
+ _CBAdvertisementDataOverflowServiceUUIDsKey
+ _CBAdvertisementDataServiceDataKey
+ _CBAdvertisementDataServiceUUIDsKey
+ _CBAdvertisementDataSolicitedServiceUUIDsKey
+ _CBAdvertisementDataTxPowerLevelKey
+ _DADeviceConnectedStatusToString
+ _DADeviceInteractionTypeToString
+ _OBJC_CLASS_$_DADeviceAccessoryServiceInfo
+ _OBJC_IVAR_$_DADevice._accessoryServicesInternalMap
+ _OBJC_IVAR_$_DADevice._bluetoothAdvertisementData
+ _OBJC_IVAR_$_DADevice._bluetoothRSSI
+ _OBJC_IVAR_$_DADevice._connectionStatus
+ _OBJC_IVAR_$_DADeviceAccessoryServiceInfo._associatedBundleID
+ _OBJC_IVAR_$_DADeviceAccessoryServiceInfo._associatedDeviceID
+ _OBJC_IVAR_$_DADeviceAccessoryServiceInfo._authorizationLevel
+ _OBJC_IVAR_$_DADeviceAccessoryServiceInfo._name
+ _OBJC_METACLASS_$_DADeviceAccessoryServiceInfo
+ __OBJC_$_CLASS_METHODS_DADeviceAccessoryServiceInfo
+ __OBJC_$_CLASS_PROP_LIST_DADeviceAccessoryServiceInfo
+ __OBJC_$_INSTANCE_METHODS_DADeviceAccessoryServiceInfo
+ __OBJC_$_INSTANCE_VARIABLES_DADeviceAccessoryServiceInfo
+ __OBJC_$_PROP_LIST_DADeviceAccessoryServiceInfo
+ __OBJC_CLASS_PROTOCOLS_$_DADeviceAccessoryServiceInfo
+ __OBJC_CLASS_RO_$_DADeviceAccessoryServiceInfo
+ __OBJC_METACLASS_RO_$_DADeviceAccessoryServiceInfo
+ ___29-[DADevice decodeXPCAdvData:]_block_invoke
+ ___29-[DADevice encodeXPCAdvData:]_block_invoke
+ ___33-[DADevice descriptionWithLevel:]_block_invoke_3
+ ___64+[DASession setDeviceAccessoryServiceInfo:device:session:error:]_block_invoke
+ ___67-[DASession requestPermissionForDevice:services:completionHandler:]_block_invoke
+ ___68-[DASession setDeviceAccessoryServiceInfo:device:completionHandler:]_block_invoke
+ ___68-[DASession setDeviceAccessoryServiceInfo:device:completionHandler:]_block_invoke.cold.1
+ ___68-[DASession setDeviceAccessoryServiceInfo:device:completionHandler:]_block_invoke_2
+ ___68-[DASession setDeviceAccessoryServiceInfo:device:completionHandler:]_block_invoke_2.cold.1
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32s_e31_v32?0"CBUUID"8"NSData"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e33_v32?0"NSString"8"NSData"16^B24ls32l8
+ ___block_descriptor_52_e8_32r40r_e55_v32?0"NSString"8"DADeviceAccessoryServiceInfo"16^B24lr32l8r40l8
+ ___block_literal_global.117
+ ___block_literal_global.128
+ ___block_literal_global.69
+ ___block_literal_global.72
+ ___block_literal_global.85
+ ___block_literal_global.94
+ _approvedCoreBluetoothADVKeysNested
+ _objc_msgSend$UUIDWithString:
+ _objc_msgSend$associatedBundleID
+ _objc_msgSend$associatedDeviceID
+ _objc_msgSend$authorizationLevel
+ _objc_msgSend$cStringUsingEncoding:
+ _objc_msgSend$decodeXPCAdvData:
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$encodeXPCAdvData:
+ _objc_msgSend$runMigrationWithDiscovery:fromPostOnboarding:
- +[DASession getDevicesWithFlags:session:error:].cold.1
- -[DADevice initWithXPCObject:error:].cold.2
- GCC_except_table16
- GCC_except_table35
- GCC_except_table44
- GCC_except_table61
- ___block_literal_global.110
- ___block_literal_global.121
- ___block_literal_global.62
- ___block_literal_global.78
- ___block_literal_global.87
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreImage_$_DeviceAccess
- _objc_msgSend$runMigrationWithDiscovery:
CStrings:
+ "+[DASession setDeviceAccessoryServiceInfo:device:session:error:]"
+ "-[DASession setDeviceAccessoryServiceInfo:device:completionHandler:]_block_invoke_2"
+ "@48@0:8@16Q24@32@40"
+ "DADeviceAccessoryServiceInfo"
+ "DASession-SetAccessoryServiceInfo"
+ "Extended-Runtime"
+ "SASi"
+ "T@\"NSDictionary\",C,N,V_bluetoothAdvertisementData"
+ "T@\"NSMutableDictionary\",&,N,V_accessoryServicesInternalMap"
+ "T@\"NSNumber\",C,N,V_bluetoothRSSI"
+ "T@\"NSString\",R,C,N,V_associatedBundleID"
+ "T@\"NSString\",R,C,N,V_associatedDeviceID"
+ "T@\"NSString\",R,C,N,V_name"
+ "TQ,N,V_authorizationLevel"
+ "TQ,N,V_connectionStatus"
+ "UUIDWithString:"
+ "_accessoryServicesInternalMap"
+ "_associatedBundleID"
+ "_associatedDeviceID"
+ "_authorizationLevel"
+ "_bluetoothAdvertisementData"
+ "_bluetoothRSSI"
+ "_connectionStatus"
+ "accessoryServicesInternalMap"
+ "accessoryServicesMap"
+ "associatedBundleID"
+ "associatedDeviceID"
+ "auL"
+ "authorizationLevel"
+ "bluetoothAdvertisementData"
+ "bluetoothRSSI"
+ "btAdv"
+ "btRs"
+ "cStringUsingEncoding:"
+ "connectionStatus"
+ "dAsI"
+ "decodeXPCAdvData:"
+ "dictionaryWithDictionary:"
+ "encodeXPCAdvData:"
+ "initWithName:authorizationLevel:bundleID:deviceID:"
+ "initWithPersistentDictionaryRepresentation:deviceID:error:"
+ "launchInteractionWithDevice:flags:reason:completionHandler:"
+ "requestPermissionForDevice:services:completionHandler:"
+ "runMigrationWithDiscovery:fromPostOnboarding:"
+ "setAccessoryServicesInternalMap:"
+ "setAuthorizationLevel:"
+ "setBluetoothAdvertisementData:"
+ "setBluetoothRSSI:"
+ "setConnectionStatus:"
+ "setDeviceAccessoryServiceInfo completed: %@, %@"
+ "setDeviceAccessoryServiceInfo start: %@, device %@"
+ "setDeviceAccessoryServiceInfo:device:completionHandler:"
+ "setDeviceAccessoryServiceInfo:device:session:error:"
+ "v32@?0@\"CBUUID\"8@\"NSData\"16^B24"
+ "v32@?0@\"NSString\"8@\"DADeviceAccessoryServiceInfo\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSData\"16^B24"
+ "v48@0:8@16q24@32@?40"
- "T@\"NSDictionary\",R,N"
- "runMigrationWithDiscovery:"

```
