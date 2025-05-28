## SEService

> `/System/Library/PrivateFrameworks/SEService.framework/SEService`

```diff

-41.7.0.0.0
-  __TEXT.__text: 0x5d668
-  __TEXT.__auth_stubs: 0x13a0
-  __TEXT.__objc_methlist: 0x1e68
+42.10.0.0.0
+  __TEXT.__text: 0x5dd6c
+  __TEXT.__auth_stubs: 0x13b0
+  __TEXT.__objc_methlist: 0x1eb0
   __TEXT.__const: 0x27e0
-  __TEXT.__gcc_except_tab: 0x1330
-  __TEXT.__cstring: 0x3fe0
+  __TEXT.__gcc_except_tab: 0x1384
+  __TEXT.__cstring: 0x40e0
   __TEXT.__oslogstring: 0x6a8
   __TEXT.__swift5_typeref: 0x93c
   __TEXT.__swift5_reflstr: 0x3ca

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x148
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1fc0
+  __TEXT.__unwind_info: 0x1fd0
   __TEXT.__eh_frame: 0x23b8
   __TEXT.__objc_classname: 0x491
-  __TEXT.__objc_methname: 0x5ecc
-  __TEXT.__objc_methtype: 0x21aa
-  __TEXT.__objc_stubs: 0x32e0
+  __TEXT.__objc_methname: 0x6088
+  __TEXT.__objc_methtype: 0x220d
+  __TEXT.__objc_stubs: 0x3360
   __DATA_CONST.__got: 0x218
-  __DATA_CONST.__const: 0x9c8
+  __DATA_CONST.__const: 0x9e0
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4598
-  __DATA_CONST.__objc_selrefs: 0x1298
+  __DATA_CONST.__objc_const: 0x4648
+  __DATA_CONST.__objc_selrefs: 0x12d0
   __DATA_CONST.__objc_arraydata: 0x58
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__cfstring: 0x2c00
+  __AUTH_CONST.__cfstring: 0x2d20
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__const: 0x11b0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_ptr: 0x50
-  __AUTH_CONST.__auth_got: 0x9e0
+  __AUTH_CONST.__auth_got: 0x9e8
   __AUTH.__objc_data: 0x0
   __DATA.__objc_protorefs: 0x78
   __DATA.__objc_classrefs: 0x1f8
   __DATA.__objc_superrefs: 0xb0
-  __DATA.__objc_ivar: 0x294
+  __DATA.__objc_ivar: 0x2a0
   __DATA.__objc_data: 0xc8
   __DATA.__data: 0x1540
   __DATA.__bss: 0x30b0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2117
-  Symbols:   3504
-  CStrings:  1778
+  Functions: 2125
+  Symbols:   3527
+  CStrings:  1801
 
Symbols:
+ -[SEEndPoint additionalAttestationsDict]
+ -[SEEndPoint setAdditionalAttestationsDict:]
+ -[SEEndPoint setSlotIdentifier:]
+ -[SEEndPoint setVehicleSupportedVersionsData:]
+ -[SEEndPoint slotIdentifier]
+ -[SEEndPoint vehicleSupportedVersionsData]
+ GCC_except_table110
+ GCC_except_table119
+ GCC_except_table28
+ GCC_except_table33
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table60
+ GCC_except_table66
+ GCC_except_table67
+ GCC_except_table74
+ GCC_except_table77
+ GCC_except_table80
+ _OBJC_IVAR_$_SEEndPoint._additionalAttestationsDict
+ _OBJC_IVAR_$_SEEndPoint._slotIdentifier
+ _OBJC_IVAR_$_SEEndPoint._vehicleSupportedVersionsData
+ _SESEndPointCreateForLyonWithSession
+ ___SESEndPointCreateForLyonWithSession_block_invoke
+ ___block_literal_global.519
+ ___block_literal_global.525
+ __unnamed_array_storage.609
+ _objc_msgSend$additionalAttestationsDict
+ _objc_msgSend$createLyonEndpointWithProxy:readerGroupIdentifier:readerPublicKey:privateMailboxSize:reply:
+ _objc_msgSend$slotIdentifier
+ _objc_msgSend$vehicleSupportedVersionsData
- GCC_except_table115
- GCC_except_table29
- GCC_except_table34
- GCC_except_table58
- GCC_except_table64
- GCC_except_table65
- GCC_except_table68
- GCC_except_table75
- GCC_except_table78
- GCC_except_table82
- ___block_literal_global.516
- ___block_literal_global.522
- __unnamed_array_storage.603
CStrings:
+ "\tadditionalAttestationsDict : %lu\n"
+ "\tslotIdentifier length : %ld,\n"
+ "\tvehicleSupportedVersionsData : %@,\n"
+ "\x1f\x0f\x0f\a"
+ "1.2.840.113635.100.6.65.34"
+ "A0000008580103"
+ "T@\"NSData\",C,V_slotIdentifier"
+ "T@\"NSData\",C,V_vehicleSupportedVersionsData"
+ "T@\"NSDictionary\",C,V_additionalAttestationsDict"
+ "Vv56@0:8@\"<SEProxyInterface>\"16@\"NSData\"24@\"NSData\"32@\"NSNumber\"40@?<v@?@\"SEEndPoint\"@\"NSError\">48"
+ "_additionalAttestationsDict"
+ "_slotIdentifier"
+ "_vehicleSupportedVersionsData"
+ "additionalAttestationsDict"
+ "createLyonEndpointWithProxy:readerGroupIdentifier:readerPublicKey:privateMailboxSize:reply:"
+ "setAdditionalAttestationsDict:"
+ "setSlotIdentifier:"
+ "setVehicleSupportedVersionsData:"
+ "slotIdentifier"
+ "vehicleSupportedVersionsData"
+ "vehicleSupportedVersionsData.asHexString"
- "\x1f\x0f\x0f\x04"

```
