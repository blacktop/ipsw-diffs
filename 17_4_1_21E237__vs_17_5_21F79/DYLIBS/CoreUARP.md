## CoreUARP

> `/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP`

```diff

-975.100.86.0.1
-  __TEXT.__text: 0x65fb4
+975.120.15.0.0
+  __TEXT.__text: 0x66320
   __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_methlist: 0x6004
+  __TEXT.__objc_methlist: 0x600c
   __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0x54cc
-  __TEXT.__oslogstring: 0x3c85
+  __TEXT.__cstring: 0x553c
+  __TEXT.__oslogstring: 0x3d55
   __TEXT.__gcc_except_tab: 0x62c
   __TEXT.__dlopen_cstrs: 0xa4
-  __TEXT.__unwind_info: 0x1d04
+  __TEXT.__unwind_info: 0x1ccc
   __TEXT.__objc_classname: 0xcca
-  __TEXT.__objc_methname: 0xbf98
-  __TEXT.__objc_methtype: 0x388a
-  __TEXT.__objc_stubs: 0x7de0
+  __TEXT.__objc_methname: 0xc034
+  __TEXT.__objc_methtype: 0x38f8
+  __TEXT.__objc_stubs: 0x7e00
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x1bb0
   __DATA_CONST.__objc_classlist: 0x360

   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x8d60
-  __DATA_CONST.__objc_selrefs: 0x28f0
+  __DATA_CONST.__objc_selrefs: 0x2900
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x3b8
   __DATA_CONST.__objc_superrefs: 0x350

   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__objc_intobj: 0xbe8
   __AUTH_CONST.__auth_got: 0x448
-  __AUTH.__objc_data: 0x19f0
+  __AUTH.__objc_data: 0x1950
   __DATA.__objc_ivar: 0x8cc
   __DATA.__data: 0x2c3
   __DATA.__bss: 0x1a08
-  __DATA_DIRTY.__objc_data: 0x7d0
+  __DATA_DIRTY.__objc_data: 0x870
   __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: B3FF580D-8758-312F-8E8B-B97AD2CB7BE0
-  Functions: 3022
-  Symbols:   9115
-  CStrings:  4460
+  UUID: 96B6ABA8-2E1D-3365-878E-0880DB01F9C7
+  Functions: 3027
+  Symbols:   9126
+  CStrings:  4468
 
Symbols:
+ -[UARPController getBatchedSupportedAccessories:assetLocationType:]
+ -[UARPController getSupportedAccessoriesInternal:assetID:batchRequest:]
+ -[UARPController supportedAccessories:forProductGroup:isComplete:]
+ -[UARPControllerXPC getSupportedAccessories:assetID:batchRequest:]
+ -[UARPControllerXPC getSupportedAccessories:forProductGroup:]
+ -[UARPControllerXPC getSupportedAccessories:forProductGroup:].cold.1
+ -[UARPControllerXPC getSupportedAccessories:forProductGroup:].cold.2
+ _OUTLINED_FUNCTION_17
+ _UARPPlatformControllerOfferFirmwareAsset.cold.4
+ ___34-[UARPControllerXPC xpcConnection]_block_invoke.113
+ ___46-[UARPControllerXPC getAssetIDForAccessoryID:]_block_invoke.133
+ ___48-[UARPControllerXPC getAttestationCertificates:]_block_invoke.139
+ ___56-[UARPControllerXPC getSandboxExtensionTokenForAssetID:]_block_invoke.141
+ ___60-[UARPControllerXPC getSupplementalAssetNameForAccessoryID:]_block_invoke.135
+ ___61-[UARPControllerXPC getSupportedAccessories:forProductGroup:]_block_invoke
+ ___61-[UARPControllerXPC getSupportedAccessories:forProductGroup:]_block_invoke.137
+ ___66-[UARPController supportedAccessories:forProductGroup:isComplete:]_block_invoke
+ ___66-[UARPController supportedAccessories:forProductGroup:isComplete:]_block_invoke.cold.1
+ ___66-[UARPControllerXPC getSupportedAccessories:assetID:batchRequest:]_block_invoke
+ ___66-[UARPControllerXPC getSupportedAccessories:assetID:batchRequest:]_block_invoke_2
+ ___71-[UARPController getSupportedAccessoriesInternal:assetID:batchRequest:]_block_invoke
+ ___71-[UARPController getSupportedAccessoriesInternal:assetID:batchRequest:]_block_invoke.cold.1
+ ___block_descriptor_48_e8_32r40r_e18_v20?0"NSSet"8B16lr32l8r40l8
+ _objc_msgSend$getSupportedAccessories:assetID:batchRequest:
+ _objc_msgSend$getSupportedAccessories:assetID:batchRequest:reply:
+ _objc_msgSend$getSupportedAccessories:forProductGroup:
+ _objc_msgSend$getSupportedAccessoriesInternal:assetID:batchRequest:
+ _objc_msgSend$supportedAccessories:forProductGroup:isComplete:
- -[UARPController getSupportedAccessoriesInternal:assetID:]
- -[UARPController supportedAccessories:forProductGroup:]
- -[UARPControllerXPC getSupportedAccessories:]
- -[UARPControllerXPC getSupportedAccessories:].cold.1
- -[UARPControllerXPC getSupportedAccessories:assetID:]
- ___34-[UARPControllerXPC xpcConnection]_block_invoke.112
- ___45-[UARPControllerXPC getSupportedAccessories:]_block_invoke
- ___45-[UARPControllerXPC getSupportedAccessories:]_block_invoke.136
- ___46-[UARPControllerXPC getAssetIDForAccessoryID:]_block_invoke.132
- ___48-[UARPControllerXPC getAttestationCertificates:]_block_invoke.138
- ___53-[UARPControllerXPC getSupportedAccessories:assetID:]_block_invoke
- ___53-[UARPControllerXPC getSupportedAccessories:assetID:]_block_invoke_2
- ___55-[UARPController supportedAccessories:forProductGroup:]_block_invoke
- ___55-[UARPController supportedAccessories:forProductGroup:]_block_invoke_2
- ___56-[UARPControllerXPC getSandboxExtensionTokenForAssetID:]_block_invoke.140
- ___58-[UARPController getSupportedAccessoriesInternal:assetID:]_block_invoke
- ___58-[UARPController getSupportedAccessoriesInternal:assetID:]_block_invoke.cold.1
- ___60-[UARPControllerXPC getSupplementalAssetNameForAccessoryID:]_block_invoke.134
- ___block_descriptor_40_e8_32r_e15_v16?0"NSSet"8lr32l8
- _objc_msgSend$getSupportedAccessories:
- _objc_msgSend$getSupportedAccessories:assetID:
- _objc_msgSend$getSupportedAccessories:assetID:reply:
- _objc_msgSend$getSupportedAccessoriesInternal:assetID:
CStrings:
+ "%s: Caller provided nil parameter set"
+ "%s: Firmware already in flight. Do not offet asset %@ to endpoint %@"
+ "%{public}s: Delegate doesn't implement a supportedAccessories:forProductGroup:(isComplete:) callback"
+ "-[UARPController getSupportedAccessoriesInternal:assetID:batchRequest:]_block_invoke"
+ "-[UARPController supportedAccessories:forProductGroup:isComplete:]_block_invoke"
+ "-[UARPControllerXPC getSupportedAccessories:forProductGroup:]"
+ "B32@0:8@\"NSMutableSet\"16@\"NSString\"24"
+ "B36@0:8@\"NSString\"16@\"UARPAssetID\"24B32"
+ "DawnF"
+ "getBatchedSupportedAccessories:assetLocationType:"
+ "getSupportedAccessories:assetID:batchRequest:"
+ "getSupportedAccessories:assetID:batchRequest:reply:"
+ "getSupportedAccessories:forProductGroup:"
+ "getSupportedAccessoriesInternal:assetID:batchRequest:"
+ "supportedAccessories:forProductGroup:isComplete:"
+ "v20@?0@\"NSSet\"8B16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSSet\"B>24"
+ "v44@0:8@\"NSString\"16@\"UARPAssetID\"24B32@?<v@?@\"NSError\">36"
- "-[UARPController getSupportedAccessoriesInternal:assetID:]_block_invoke"
- "-[UARPControllerXPC getSupportedAccessories:]"
- "@\"NSSet\"24@0:8@\"NSString\"16"
- "DawnE"
- "getSupportedAccessories:"
- "getSupportedAccessories:assetID:"
- "getSupportedAccessories:assetID:reply:"
- "getSupportedAccessoriesInternal:assetID:"
- "v16@?0@\"NSSet\"8"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSSet\">24"

```
