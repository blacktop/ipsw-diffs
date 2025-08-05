## UARPKit

> `/System/Library/PrivateFrameworks/UARPKit.framework/UARPKit`

```diff

-1338.0.62.0.1
-  __TEXT.__text: 0x15cbc
-  __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_methlist: 0x1010
+1338.0.72.0.0
+  __TEXT.__text: 0x1a104
+  __TEXT.__auth_stubs: 0x3b0
+  __TEXT.__objc_methlist: 0x10d0
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x14f2
-  __TEXT.__gcc_except_tab: 0x910
-  __TEXT.__oslogstring: 0x3db
-  __TEXT.__unwind_info: 0x5f8
-  __TEXT.__objc_classname: 0x18b
-  __TEXT.__objc_methname: 0x39bc
-  __TEXT.__objc_methtype: 0x8f2
-  __TEXT.__objc_stubs: 0x1a80
+  __TEXT.__cstring: 0x1b34
+  __TEXT.__gcc_except_tab: 0x12a8
+  __TEXT.__oslogstring: 0x54b
+  __TEXT.__unwind_info: 0x5e0
+  __TEXT.__objc_classname: 0x19b
+  __TEXT.__objc_methname: 0x3c22
+  __TEXT.__objc_methtype: 0x8fd
+  __TEXT.__objc_stubs: 0x1b00
   __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0x2f0
+  __DATA_CONST.__const: 0x318
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb40
+  __DATA_CONST.__objc_selrefs: 0xbc0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x1d8
+  __AUTH_CONST.__auth_got: 0x1e8
   __AUTH_CONST.__cfstring: 0x320
-  __AUTH_CONST.__objc_const: 0x1350
+  __AUTH_CONST.__objc_const: 0x1430
   __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x104
+  __DATA.__objc_ivar: 0x114
   __DATA.__data: 0x2a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CFE77774-4E5A-3BDB-8B41-14A9C6D9DC1F
-  Functions: 434
-  Symbols:   1389
-  CStrings:  710
+  UUID: 1E4E88E9-0BB1-30F7-AE2D-1E11B754A8B8
+  Functions: 449
+  Symbols:   1430
+  CStrings:  761
 
Symbols:
+ -[UARPDevice setSupportsChargingChimeDebounce:]
+ -[UARPDevice setSupportsHeySiri:]
+ -[UARPDevice setSupportsJustSiri:]
+ -[UARPDevice setSupportsVoiceAssist:]
+ -[UARPDevice supportsChargingChimeDebounce]
+ -[UARPDevice supportsHeySiri]
+ -[UARPDevice supportsJustSiri]
+ -[UARPDevice supportsVoiceAssist]
+ -[UARPDevice(FeatureSupport) deviceSupportsChargingChimeDebounce]
+ -[UARPDevice(FeatureSupport) deviceSupportsHeySiri]
+ -[UARPDevice(FeatureSupport) deviceSupportsJustSiri]
+ -[UARPDevice(FeatureSupport) deviceSupportsVoiceAssist]
+ _OBJC_IVAR_$_UARPDevice._supportsChargingChimeDebounce
+ _OBJC_IVAR_$_UARPDevice._supportsHeySiri
+ _OBJC_IVAR_$_UARPDevice._supportsJustSiri
+ _OBJC_IVAR_$_UARPDevice._supportsVoiceAssist
+ _OUTLINED_FUNCTION_7
+ __OBJC_$_INSTANCE_METHODS_UARPDevice(Private|FeatureSupport)
+ ___40-[UARPDevice queryActiveFirmwareVersion]_block_invoke.48
+ ___40-[UARPDevice queryActiveFirmwareVersion]_block_invoke.cold.1
+ ___40-[UARPDevice queryStagedFirmwareVersion]_block_invoke.50
+ ___40-[UARPDevice queryStagedFirmwareVersion]_block_invoke.cold.1
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8ls32l8r40l8
+ _objc_msgSend$hostEndpointSupportsChargingChimeDebounce:
+ _objc_msgSend$hostEndpointSupportsHeySiri:
+ _objc_msgSend$hostEndpointSupportsJustSiri:
+ _objc_msgSend$hostEndpointSupportsVoiceAssist:
+ _objc_release_x9
+ _objc_retain_x1
- __OBJC_$_INSTANCE_METHODS_UARPDevice(Private)
- ___40-[UARPDevice queryActiveFirmwareVersion]_block_invoke_2
- ___40-[UARPDevice queryStagedFirmwareVersion]_block_invoke_2
CStrings:
+ "%s: Out of band component index %@ on endpoint index %@ for device %@, which has %lu components"
+ "%s: Out of band endpoint index %@ for device %@, which has %lu endpoints"
+ "%s: Unknown Asset UUID %@"
+ "%s: Unknown Endpoint UUID %@"
+ "%s: active firmware version is %@"
+ "%s: hostEndpointQueryFirmwareVersion failed with %@"
+ "%s: hostEndpointQueryStagedFirmwareVersion failed with %@"
+ "-[UARPDevice queryActiveFirmwareVersion]_block_invoke"
+ "-[UARPDevice queryStagedFirmwareVersion]_block_invoke"
+ "-[UARPDevice(FeatureSupport) deviceSupportsChargingChimeDebounce]"
+ "-[UARPDevice(FeatureSupport) deviceSupportsHeySiri]"
+ "-[UARPDevice(FeatureSupport) deviceSupportsJustSiri]"
+ "-[UARPDevice(FeatureSupport) deviceSupportsVoiceAssist]"
+ "-[UARPDeviceManager endpointControllerDelegateAppliedStagedAssets:layer3Flags:]_block_invoke"
+ "-[UARPDeviceManager endpointControllerDelegateAssetMetaDataComplete:assetUUID:assetTag:]_block_invoke"
+ "-[UARPDeviceManager endpointControllerDelegateAssetOffered:assetUUID:assetTag:]_block_invoke"
+ "-[UARPDeviceManager endpointControllerDelegateAssetPayloadData:assetUUID:payloadTag:payloadIndex:payloadOffset:dataLength:]_block_invoke"
+ "-[UARPDeviceManager endpointControllerDelegateAssetPayloadDataComplete:assetUUID:payloadTag:payloadIndex:]_block_invoke"
+ "-[UARPDeviceManager endpointControllerDelegateAssetPayloadMetaDataComplete:assetUUID:payloadTag:payloadIndex:]_block_invoke"
+ "-[UARPDeviceManager endpointControllerDelegateAssetPayloadReady:assetUUID:payloadTag:payloadIndex:]_block_invoke"
+ "-[UARPDeviceManager endpointControllerDelegateAssetTransferProgress:assetUUID:bytesTransferred:totalBytes:]_block_invoke"
+ "-[UARPDeviceManager endpointControllerDelegateAssetTransferStatus:assetUUID:transferStatus:]_block_invoke"
+ "-[UARPDeviceManager endpointControllerDelegateEndpointUnavailable:]_block_invoke"
+ "-[UARPDeviceManager endpointControllerDelegatePersonalizationStatus:assetUUID:status:]_block_invoke"
+ "-[UARPDeviceManager endpointControllerDelegateRescindedAssets:]_block_invoke"
+ "FeatureSupport"
+ "TB,V_supportsChargingChimeDebounce"
+ "TB,V_supportsHeySiri"
+ "TB,V_supportsJustSiri"
+ "TB,V_supportsVoiceAssist"
+ "_supportsChargingChimeDebounce"
+ "_supportsHeySiri"
+ "_supportsJustSiri"
+ "_supportsVoiceAssist"
+ "deviceSupportsChargingChimeDebounce"
+ "deviceSupportsHeySiri"
+ "deviceSupportsJustSiri"
+ "deviceSupportsVoiceAssist"
+ "hostEndpointSupportsChargingChimeDebounce:"
+ "hostEndpointSupportsHeySiri:"
+ "hostEndpointSupportsJustSiri:"
+ "hostEndpointSupportsVoiceAssist:"
+ "setSupportsChargingChimeDebounce:"
+ "setSupportsHeySiri:"
+ "setSupportsJustSiri:"
+ "setSupportsVoiceAssist:"
+ "supportsChargingChimeDebounce"
+ "supportsHeySiri"
+ "supportsJustSiri"
+ "supportsVoiceAssist"
+ "v20@0:8B16"

```
