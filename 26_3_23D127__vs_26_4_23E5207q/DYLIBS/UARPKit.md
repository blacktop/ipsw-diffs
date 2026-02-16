## UARPKit

> `/System/Library/PrivateFrameworks/UARPKit.framework/UARPKit`

```diff

-1338.80.37.0.0
-  __TEXT.__text: 0x1a310
-  __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_methlist: 0x10d0
+1345.100.155.0.0
+  __TEXT.__text: 0x1de84
+  __TEXT.__auth_stubs: 0x390
+  __TEXT.__objc_methlist: 0x1200
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x1b34
-  __TEXT.__gcc_except_tab: 0x12a8
-  __TEXT.__oslogstring: 0x586
-  __TEXT.__unwind_info: 0x5e8
-  __TEXT.__objc_classname: 0x19b
-  __TEXT.__objc_methname: 0x3c22
-  __TEXT.__objc_methtype: 0x8fd
-  __TEXT.__objc_stubs: 0x1b40
-  __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0x318
+  __TEXT.__cstring: 0x20d4
+  __TEXT.__gcc_except_tab: 0x1324
+  __TEXT.__oslogstring: 0x7cf
+  __TEXT.__unwind_info: 0x608
+  __TEXT.__objc_classname: 0x1a8
+  __TEXT.__objc_methname: 0x4263
+  __TEXT.__objc_methtype: 0x9b2
+  __TEXT.__objc_stubs: 0x1da0
+  __DATA_CONST.__got: 0xc8
+  __DATA_CONST.__const: 0x368
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbc0
+  __DATA_CONST.__objc_selrefs: 0xcb0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x1e8
+  __AUTH_CONST.__auth_got: 0x1d8
   __AUTH_CONST.__cfstring: 0x320
-  __AUTH_CONST.__objc_const: 0x1430
+  __AUTH_CONST.__objc_const: 0x14e8
   __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x114
+  __DATA.__objc_ivar: 0x120
   __DATA.__data: 0x2a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 07724928-446F-3E3B-9348-A9265F3A285C
-  Functions: 452
-  Symbols:   1438
-  CStrings:  762
+  UUID: F83848D0-63CB-3D41-8054-3CE4091328BB
+  Functions: 502
+  Symbols:   1576
+  CStrings:  830
 
Symbols:
+ -[UARPDevice hostEndpointCopySourceURL:destinationURL:]
+ -[UARPDevice hostEndpointCopySourceURL:destinationURL:].cold.1
+ -[UARPDevice hostEndpointCopySourceURL:destinationURL:].cold.2
+ -[UARPDevice hostEndpointDelegateProvideSandBoxExtension:token:assetURL:appleModelNumber:serialNumber:]
+ -[UARPDevice hostEndpointDelegateProvideSandBoxExtension:token:assetURL:appleModelNumber:serialNumber:].cold.1
+ -[UARPDevice hostEndpointDelegateProvideSandBoxExtension:token:assetURL:appleModelNumber:serialNumber:].cold.2
+ -[UARPDevice hostEndpointDelegateProvideSandBoxExtension:token:assetURL:appleModelNumber:serialNumber:].cold.3
+ -[UARPDevice hostEndpointDelegateProvideSandBoxExtension:token:assetURL:appleModelNumber:serialNumber:].cold.4
+ -[UARPDevice(TapToRadar) tapToRadarAssetsURL]
+ -[UARPDevice(TapToRadar) tapToRadarStart:]
+ -[UARPDevice(TapToRadar) tapToRadarStart:error:]
+ -[UARPDevice(TapToRadar) tapToRadarStart:error:].cold.1
+ -[UARPDevice(TapToRadar) tapToRadarStop:]
+ -[UARPDeviceAsset getIsObservedOnly]
+ -[UARPDeviceAsset initWithUUID:]
+ -[UARPDeviceAsset isObservedOnly]
+ -[UARPDeviceManager endpointControllerDelegateRxDynamicAssetTransferProgress:assetUUID:assetTag:bytesTransferred:totalBytes:]
+ -[UARPDeviceManager endpointControllerDelegateRxDynamicAssetTransferProgress:assetUUID:assetTag:bytesTransferred:totalBytes:].cold.1
+ -[UARPDeviceManager endpointControllerDelegateRxDynamicAssetTransferStatus:assetUUID:assetTag:transferStatus:]
+ -[UARPDeviceManager endpointControllerDelegateTxDynamicAssetTransferProgress:assetUUID:assetTag:bytesTransferred:totalBytes:]
+ -[UARPDeviceManager endpointControllerDelegateTxDynamicAssetTransferProgress:assetUUID:assetTag:bytesTransferred:totalBytes:].cold.1
+ -[UARPDeviceManager endpointControllerDelegateTxDynamicAssetTransferStatus:assetUUID:assetTag:transferStatus:]
+ -[UARPDeviceManager stageFirmwareAsset:deviceEndpoint:tssServerURL:]
+ -[UARPDeviceManager tapToRadarStart:reply:]
+ -[UARPDeviceManager tapToRadarStart:reply:].cold.1
+ -[UARPDeviceManager tapToRadarStop:]
+ GCC_except_table150
+ GCC_except_table164
+ GCC_except_table167
+ GCC_except_table180
+ GCC_except_table185
+ GCC_except_table187
+ GCC_except_table189
+ GCC_except_table192
+ GCC_except_table52
+ _OBJC_IVAR_$_UARPDevice._assetsCollectionURL
+ _OBJC_IVAR_$_UARPDevice._debugTransport
+ _OBJC_IVAR_$_UARPDeviceAsset._isObservedOnly
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_9
+ __OBJC_$_INSTANCE_METHODS_UARPDevice(Private|FeatureSupport|TapToRadar)
+ ___106-[UARPDeviceManager endpointControllerDelegateAssetPayloadDataComplete:assetUUID:payloadTag:payloadIndex:]_block_invoke.cold.1
+ ___110-[UARPDeviceManager endpointControllerDelegateAssetPayloadMetaDataComplete:assetUUID:payloadTag:payloadIndex:]_block_invoke.cold.1
+ ___110-[UARPDeviceManager endpointControllerDelegateRxDynamicAssetTransferStatus:assetUUID:assetTag:transferStatus:]_block_invoke
+ ___110-[UARPDeviceManager endpointControllerDelegateTxDynamicAssetTransferStatus:assetUUID:assetTag:transferStatus:]_block_invoke
+ ___123-[UARPDeviceManager endpointControllerDelegateAssetPayloadData:assetUUID:payloadTag:payloadIndex:payloadOffset:dataLength:]_block_invoke.cold.1
+ ___125-[UARPDeviceManager endpointControllerDelegateRxDynamicAssetTransferProgress:assetUUID:assetTag:bytesTransferred:totalBytes:]_block_invoke
+ ___125-[UARPDeviceManager endpointControllerDelegateTxDynamicAssetTransferProgress:assetUUID:assetTag:bytesTransferred:totalBytes:]_block_invoke
+ ___36-[UARPDeviceManager tapToRadarStop:]_block_invoke
+ ___40-[UARPDevice queryActiveFirmwareVersion]_block_invoke.56
+ ___40-[UARPDevice queryStagedFirmwareVersion]_block_invoke.58
+ ___43-[UARPDeviceManager tapToRadarStart:reply:]_block_invoke
+ ___43-[UARPDeviceManager tapToRadarStart:reply:]_block_invoke_2
+ ___48-[UARPDevice(TapToRadar) tapToRadarStart:error:]_block_invoke
+ ___48-[UARPDevice(TapToRadar) tapToRadarStart:error:]_block_invoke.145
+ ___48-[UARPDevice(TapToRadar) tapToRadarStart:error:]_block_invoke.cold.1
+ ___68-[UARPDeviceManager stageFirmwareAsset:deviceEndpoint:tssServerURL:]_block_invoke
+ ___79-[UARPDeviceManager endpointControllerDelegateAssetOffered:assetUUID:assetTag:]_block_invoke.cold.1
+ ___86-[UARPDeviceManager endpointControllerDelegatePersonalizationStatus:assetUUID:status:]_block_invoke.cold.1
+ ___88-[UARPDeviceManager endpointControllerDelegateAssetMetaDataComplete:assetUUID:assetTag:]_block_invoke.cold.1
+ ___99-[UARPDeviceManager endpointControllerDelegateAssetPayloadReady:assetUUID:payloadTag:payloadIndex:]_block_invoke.cold.1
+ ___block_descriptor_48_e8_32s40s_e18_v16?0"NSString"8ls32l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ _objc_msgSend$URLByAppendingPathComponent:isDirectory:
+ _objc_msgSend$UTF8String
+ _objc_msgSend$copyItemAtURL:toURL:error:
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$endpointControllerTapToRadarStart:reply:
+ _objc_msgSend$endpointControllerTapToRadarStop:
+ _objc_msgSend$fileURLWithPathComponents:
+ _objc_msgSend$hostEndpointCopySourceURL:destinationURL:
+ _objc_msgSend$hostEndpointTapToRadarStart:reply:
+ _objc_msgSend$hostEndpointTapToRadarStop:
+ _objc_msgSend$initWithUUID:
+ _objc_msgSend$isObservedOnly
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$stageFirmwareAsset:deviceEndpoint:tssServerURL:
+ _objc_msgSend$stringByDeletingLastPathComponent
+ _objc_msgSend$uarpDeviceManagerRxDynamicAssetTransferProgress:deviceEndpoint:deviceAsset:deviceAssetTag:bytesTransferred:totalBytes:
+ _objc_msgSend$uarpDeviceManagerRxDynamicAssetTransferStatus:deviceEndpoint:deviceAsset:deviceAssetTag:transferStatus:
+ _objc_msgSend$uarpDeviceManagerTxDynamicAssetTransferProgress:deviceEndpoint:deviceAsset:deviceAssetTag:bytesTransferred:totalBytes:
+ _objc_msgSend$uarpDeviceManagerTxDynamicAssetTransferStatus:deviceEndpoint:deviceAsset:deviceAssetTag:transferStatus:
+ _objc_retainAutoreleasedReturnValue
+ _sandbox_extension_consume
+ _sandbox_extension_release
- -[UARPDeviceManager endpointControllerDelegateAssetTransferProgress:assetUUID:bytesTransferred:totalBytes:].cold.1
- GCC_except_table149
- GCC_except_table152
- GCC_except_table165
- GCC_except_table168
- GCC_except_table179
- GCC_except_table181
- GCC_except_table186
- GCC_except_table27
- GCC_except_table32
- __OBJC_$_INSTANCE_METHODS_UARPDevice(Private|FeatureSupport)
- ___40-[UARPDevice queryActiveFirmwareVersion]_block_invoke.48
- ___40-[UARPDevice queryStagedFirmwareVersion]_block_invoke.50
- ___55-[UARPDeviceManager stageFirmwareAsset:deviceEndpoint:]_block_invoke
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x26
- _objc_retain_x8
CStrings:
+ "%s: %@, Failed to copy contents of %@ to destination file"
+ "%s: %@, assetUUID is %@, bytesTransferred is %lu, totalBytes is %lu"
+ "%s: %@, bytes transferred %lu of total %lu"
+ "%s: Assets Collection URL is nil"
+ "%s: Failed to consume SandBox token"
+ "%s: Failed to copy source URL: %@ to destination URL: %@ with error: %@"
+ "%s: Failed to create directory at path %@ with error: %@"
+ "%s: Failed to remove existing file at destination URL: %@"
+ "%s: Observation Only Asset UUID %@"
+ "%s: Successfully created directory at path %@"
+ "%s: Sucessfully copied source URL: %@ to destination URL: %@"
+ "%s: TapToRadar Start Timestamp is %@"
+ "%s: hostEndpointTapToRadarStart failed with %@"
+ "-[UARPDevice hostEndpointCopySourceURL:destinationURL:]"
+ "-[UARPDevice hostEndpointDelegateProvideSandBoxExtension:token:assetURL:appleModelNumber:serialNumber:]"
+ "-[UARPDevice(TapToRadar) tapToRadarAssetsURL]"
+ "-[UARPDevice(TapToRadar) tapToRadarStart:error:]"
+ "-[UARPDevice(TapToRadar) tapToRadarStart:error:]_block_invoke"
+ "-[UARPDevice(TapToRadar) tapToRadarStop:]"
+ "-[UARPDeviceManager endpointControllerDelegateRxDynamicAssetTransferProgress:assetUUID:assetTag:bytesTransferred:totalBytes:]"
+ "-[UARPDeviceManager endpointControllerDelegateRxDynamicAssetTransferProgress:assetUUID:assetTag:bytesTransferred:totalBytes:]_block_invoke"
+ "-[UARPDeviceManager endpointControllerDelegateRxDynamicAssetTransferStatus:assetUUID:assetTag:transferStatus:]"
+ "-[UARPDeviceManager endpointControllerDelegateRxDynamicAssetTransferStatus:assetUUID:assetTag:transferStatus:]_block_invoke"
+ "-[UARPDeviceManager endpointControllerDelegateTxDynamicAssetTransferProgress:assetUUID:assetTag:bytesTransferred:totalBytes:]"
+ "-[UARPDeviceManager endpointControllerDelegateTxDynamicAssetTransferProgress:assetUUID:assetTag:bytesTransferred:totalBytes:]_block_invoke"
+ "-[UARPDeviceManager endpointControllerDelegateTxDynamicAssetTransferStatus:assetUUID:assetTag:transferStatus:]"
+ "-[UARPDeviceManager endpointControllerDelegateTxDynamicAssetTransferStatus:assetUUID:assetTag:transferStatus:]_block_invoke"
+ "-[UARPDeviceManager tapToRadarStart:reply:]"
+ "-[UARPDeviceManager tapToRadarStop:]"
+ "B24@0:8o^@16"
+ "B32@0:8@16@?24"
+ "B32@0:8@16o^@24"
+ "TB,R,V_isObservedOnly"
+ "TapToRadar"
+ "URLByAppendingPathComponent:isDirectory:"
+ "UTF8String"
+ "_assetsCollectionURL"
+ "_debugTransport"
+ "_isObservedOnly"
+ "copyItemAtURL:toURL:error:"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "endpointControllerDelegateRxDynamicAssetTransferProgress:assetUUID:assetTag:bytesTransferred:totalBytes:"
+ "endpointControllerDelegateRxDynamicAssetTransferStatus:assetUUID:assetTag:transferStatus:"
+ "endpointControllerDelegateTxDynamicAssetTransferProgress:assetUUID:assetTag:bytesTransferred:totalBytes:"
+ "endpointControllerDelegateTxDynamicAssetTransferStatus:assetUUID:assetTag:transferStatus:"
+ "endpointControllerTapToRadarStart:reply:"
+ "endpointControllerTapToRadarStop:"
+ "fileURLWithPathComponents:"
+ "getIsObservedOnly"
+ "hostEndpointCopySourceURL:destinationURL:"
+ "hostEndpointDelegateProvideSandBoxExtension:token:assetURL:appleModelNumber:serialNumber:"
+ "hostEndpointTapToRadarStart:reply:"
+ "hostEndpointTapToRadarStop:"
+ "initWithUUID:"
+ "isObservedOnly"
+ "lastPathComponent"
+ "stageFirmwareAsset:deviceEndpoint:tssServerURL:"
+ "stringByDeletingLastPathComponent"
+ "tapToRadarAssetsURL"
+ "tapToRadarStart:"
+ "tapToRadarStart:error:"
+ "tapToRadarStart:reply:"
+ "tapToRadarStop:"
+ "uarpDeviceManagerRxDynamicAssetTransferProgress:deviceEndpoint:deviceAsset:deviceAssetTag:bytesTransferred:totalBytes:"
+ "uarpDeviceManagerRxDynamicAssetTransferStatus:deviceEndpoint:deviceAsset:deviceAssetTag:transferStatus:"
+ "uarpDeviceManagerTxDynamicAssetTransferProgress:deviceEndpoint:deviceAsset:deviceAssetTag:bytesTransferred:totalBytes:"
+ "uarpDeviceManagerTxDynamicAssetTransferStatus:deviceEndpoint:deviceAsset:deviceAssetTag:transferStatus:"
+ "v56@0:8@\"NSUUID\"16@\"NSString\"24@\"NSURL\"32@\"NSString\"40@\"NSString\"48"
+ "v56@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSString\"32@\"NSNumber\"40@\"NSNumber\"48"
- "%s: %@, assetUUID is %@, bytesTransferred is %@, totalBytes is %@"

```
