## CoreAccessories

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories`

```diff

-1124.2.1.0.0
-  __TEXT.__text: 0x29dd8
+1139.40.1.0.0
+  __TEXT.__text: 0x2a198
   __TEXT.__auth_stubs: 0x710
   __TEXT.__objc_methlist: 0x185c
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x3b58
-  __TEXT.__oslogstring: 0x414b
+  __TEXT.__cstring: 0x3b85
+  __TEXT.__oslogstring: 0x41c5
   __TEXT.__gcc_except_tab: 0xe94
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x910
+  __TEXT.__unwind_info: 0x918
   __TEXT.__objc_classname: 0x25a
   __TEXT.__objc_methname: 0x470f
   __TEXT.__objc_methtype: 0x1609
-  __TEXT.__objc_stubs: 0x2b20
+  __TEXT.__objc_stubs: 0x2dc0
   __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0x1e30
+  __DATA_CONST.__const: 0x1e78
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0xd8
   __AUTH_CONST.__auth_got: 0x398
   __AUTH_CONST.__const: 0xae0
-  __AUTH_CONST.__cfstring: 0x3960
+  __AUTH_CONST.__cfstring: 0x39a0
   __AUTH_CONST.__objc_const: 0x22e0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BB7A0EDE-C292-37AC-AD4B-D20A9C9BC7E6
-  Functions: 760
-  Symbols:   4016
-  CStrings:  2084
+  UUID: A51B25E2-CC81-3423-B791-5ED29404B1A4
+  Functions: 761
+  Symbols:   4046
+  CStrings:  2089
 
Symbols:
+ _ACCUserDefaultsKey_Disable1WayNFCForInductive
+ _ACCUserDefaultsKey_DisableT56Support
+ ___60-[ACCExternalAccessoryProvider updateAccessoryInfo:forUUID:]_block_invoke
+ ___60-[ACCExternalAccessoryProvider updateAccessoryInfo:forUUID:]_block_invoke.cold.1
+ ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.301
+ ___block_literal_global.303
+ _kCFACCUserDefaultsKey_Disable1WayNFCForInductive
+ _kCFACCUserDefaultsKey_DisableT56Support
+ _objc_msgSend$firmwareRevisionActive
+ _objc_msgSend$firmwareRevisionPending
+ _objc_msgSend$hardwareRevision
+ _objc_msgSend$manufacturer
+ _objc_msgSend$model
+ _objc_msgSend$ppid
+ _objc_msgSend$serial
+ _objc_msgSend$setFirmwareRevisionActive:
+ _objc_msgSend$setFirmwareRevisionPending:
+ _objc_msgSend$setFullAccessoryInfo:
+ _objc_msgSend$setHardwareRevision:
+ _objc_msgSend$setIsMFiCharger:
+ _objc_msgSend$setManufacturer:
+ _objc_msgSend$setModel:
+ _objc_msgSend$setName:
+ _objc_msgSend$setPpid:
+ _objc_msgSend$setPrimaryUUID:
+ _objc_msgSend$setProductID:
+ _objc_msgSend$setSerial:
+ _objc_msgSend$setTransportType:
+ _objc_msgSend$setVendorID:
- ___block_literal_global.295
- ___block_literal_global.297
Functions:
~ -[_ACCExternalAccessoryInfo initWithAccessoryInfoDictionary:] : 592 -> 596
~ -[_ACCExternalAccessoryInfo description] : 76 -> 320
~ -[_ACCExternalAccessoryInfo updateAccessoryInfo:] : 572 -> 712
~ -[_ACCExternalAccessoryInfo copyAccessoryInfo] : 224 -> 268
~ -[_ACCExternalAccessoryInfo isEqual:] : 128 -> 164
~ -[_ACCExternalAccessoryInfo hash] : 8 -> 56
~ -[ACCExternalAccessoryProvider updateAccessoryInfo:forUUID:] : 796 -> 900
+ ___60-[ACCExternalAccessoryProvider updateAccessoryInfo:forUUID:]_block_invoke
CStrings:
+ "Disable1WayNFCForInductive"
+ "DisableT56Support"
+ "[#ExternalAccessory] In async to main thread: accessoryd received updateAccessoryInfo for UUID %@ (connection ID: %@), %@"

```
