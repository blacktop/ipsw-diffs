## FindMyDevice

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice`

```diff

-423.5.0.0.0
-  __TEXT.__text: 0x1bc2c
+424.6.0.0.0
+  __TEXT.__text: 0x1c7bc
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_methlist: 0x1908
+  __TEXT.__objc_methlist: 0x1a88
   __TEXT.__const: 0x70
-  __TEXT.__oslogstring: 0x214e
-  __TEXT.__cstring: 0x3afc
+  __TEXT.__oslogstring: 0x2204
+  __TEXT.__cstring: 0x3b4c
   __TEXT.__gcc_except_tab: 0x230
-  __TEXT.__unwind_info: 0x660
-  __TEXT.__objc_classname: 0x56a
-  __TEXT.__objc_methname: 0x41eb
-  __TEXT.__objc_methtype: 0x1023
-  __TEXT.__objc_stubs: 0x2e40
+  __TEXT.__unwind_info: 0x6a8
+  __TEXT.__objc_classname: 0x586
+  __TEXT.__objc_methname: 0x451d
+  __TEXT.__objc_methtype: 0x1094
+  __TEXT.__objc_stubs: 0x3080
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0x1118
-  __DATA_CONST.__objc_classlist: 0x100
+  __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5d70
-  __DATA_CONST.__objc_selrefs: 0xe60
+  __DATA_CONST.__objc_const: 0x6488
+  __DATA_CONST.__objc_selrefs: 0xef8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_classrefs: 0x118
-  __DATA_CONST.__objc_superrefs: 0xe0
-  __AUTH_CONST.__objc_const: 0x1000
-  __AUTH_CONST.__cfstring: 0x3480
+  __DATA_CONST.__objc_classrefs: 0x120
+  __DATA_CONST.__objc_superrefs: 0xe8
+  __AUTH_CONST.__objc_const: 0x1090
+  __AUTH_CONST.__cfstring: 0x3560
   __AUTH_CONST.__const: 0x440
   __AUTH_CONST.__auth_got: 0x240
-  __AUTH.__objc_data: 0x4b0
-  __DATA.__objc_ivar: 0x1a0
+  __AUTH.__objc_data: 0x500
+  __DATA.__objc_ivar: 0x1d0
   __DATA.__data: 0x920
   __DATA.__bss: 0xd0
   __DATA.__common: 0x8

   - /System/Library/PrivateFrameworks/FMCoreLite.framework/FMCoreLite
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 807
-  Symbols:   3292
-  CStrings:  1637
+  Functions: 841
+  Symbols:   3415
+  CStrings:  1694
 
Symbols:
+ +[FMDLocalFindableAccessory supportsSecureCoding]
+ -[FMDFMIPManager didAddLocalFindableAccessory:completion:]
+ -[FMDFMIPManager didRemoveLocalFindableAccessory:completion:]
+ -[FMDLocalFindableAccessory .cxx_destruct]
+ -[FMDLocalFindableAccessory accessoryIdentifier]
+ -[FMDLocalFindableAccessory alternateSerialNumber]
+ -[FMDLocalFindableAccessory baUUID]
+ -[FMDLocalFindableAccessory btAddress]
+ -[FMDLocalFindableAccessory encodeWithCoder:]
+ -[FMDLocalFindableAccessory firmwareVersion]
+ -[FMDLocalFindableAccessory identifier]
+ -[FMDLocalFindableAccessory initWithCoder:]
+ -[FMDLocalFindableAccessory initWithIdentifier:name:connected:]
+ -[FMDLocalFindableAccessory irkData]
+ -[FMDLocalFindableAccessory isConnected]
+ -[FMDLocalFindableAccessory name]
+ -[FMDLocalFindableAccessory productId]
+ -[FMDLocalFindableAccessory serialNumber]
+ -[FMDLocalFindableAccessory setAlternateSerialNumber:]
+ -[FMDLocalFindableAccessory setBaUUID:]
+ -[FMDLocalFindableAccessory setBtAddress:]
+ -[FMDLocalFindableAccessory setConnected:]
+ -[FMDLocalFindableAccessory setFirmwareVersion:]
+ -[FMDLocalFindableAccessory setIdentifier:]
+ -[FMDLocalFindableAccessory setIrkData:]
+ -[FMDLocalFindableAccessory setName:]
+ -[FMDLocalFindableAccessory setProductId:]
+ -[FMDLocalFindableAccessory setSerialNumber:]
+ -[FMDLocalFindableAccessory setVendorId:]
+ -[FMDLocalFindableAccessory vendorId]
+ _OBJC_CLASS_$_FMDLocalFindableAccessory
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_IVAR_$_FMDLocalFindableAccessory._alternateSerialNumber
+ _OBJC_IVAR_$_FMDLocalFindableAccessory._baUUID
+ _OBJC_IVAR_$_FMDLocalFindableAccessory._btAddress
+ _OBJC_IVAR_$_FMDLocalFindableAccessory._connected
+ _OBJC_IVAR_$_FMDLocalFindableAccessory._firmwareVersion
+ _OBJC_IVAR_$_FMDLocalFindableAccessory._identifier
+ _OBJC_IVAR_$_FMDLocalFindableAccessory._irkData
+ _OBJC_IVAR_$_FMDLocalFindableAccessory._name
+ _OBJC_IVAR_$_FMDLocalFindableAccessory._productId
+ _OBJC_IVAR_$_FMDLocalFindableAccessory._serialNumber
+ _OBJC_IVAR_$_FMDLocalFindableAccessory._vendorId
+ _OBJC_IVAR_$_FMDLocalFindableAccessory.accessoryIdentifier
+ _OBJC_METACLASS_$_FMDLocalFindableAccessory
+ __OBJC_$_CLASS_METHODS_FMDLocalFindableAccessory
+ __OBJC_$_CLASS_PROP_LIST_FMDLocalFindableAccessory
+ __OBJC_$_INSTANCE_METHODS_FMDLocalFindableAccessory
+ __OBJC_$_INSTANCE_VARIABLES_FMDLocalFindableAccessory
+ __OBJC_$_PROP_LIST_FMDLocalFindableAccessory
+ __OBJC_CLASS_PROTOCOLS_$_FMDLocalFindableAccessory
+ __OBJC_CLASS_RO_$_FMDLocalFindableAccessory
+ __OBJC_METACLASS_RO_$_FMDLocalFindableAccessory
+ ___58-[FMDFMIPManager didAddLocalFindableAccessory:completion:]_block_invoke
+ ___58-[FMDFMIPManager didAddLocalFindableAccessory:completion:]_block_invoke.cold.1
+ ___61-[FMDFMIPManager didRemoveLocalFindableAccessory:completion:]_block_invoke
+ ___61-[FMDFMIPManager didRemoveLocalFindableAccessory:completion:]_block_invoke.cold.1
+ _objc_msgSend$alternateSerialNumber
+ _objc_msgSend$baUUID
+ _objc_msgSend$btAddress
+ _objc_msgSend$didAddLocalFindableAccessory:completion:
+ _objc_msgSend$didRemoveLocalFindableAccessory:completion:
+ _objc_msgSend$identifier
+ _objc_msgSend$irkData
+ _objc_msgSend$isConnected
+ _objc_msgSend$productId
+ _objc_msgSend$setAlternateSerialNumber:
+ _objc_msgSend$setBaUUID:
+ _objc_msgSend$setBtAddress:
+ _objc_msgSend$setConnected:
+ _objc_msgSend$setIdentifier:
+ _objc_msgSend$setIrkData:
+ _objc_msgSend$setProductId:
+ _objc_msgSend$setVendorId:
+ _objc_msgSend$vendorId
CStrings:
+ "\x1b"
+ "@\"NSObject<FMDIdentifiable>\""
+ "@\"NSUUID\""
+ "@36@0:8@16@24B32"
+ "FMDLocalFindableAccessory"
+ "Framework: didAddLocalFindableAccessory"
+ "Framework: didRemoveLocalFindableAccessory"
+ "T@\"NSData\",C,N,V_irkData"
+ "T@\"NSObject<FMDIdentifiable>\",R,N,VaccessoryIdentifier"
+ "T@\"NSString\",C,N,V_alternateSerialNumber"
+ "T@\"NSString\",C,N,V_btAddress"
+ "T@\"NSString\",C,N,V_firmwareVersion"
+ "T@\"NSString\",C,N,V_name"
+ "T@\"NSString\",C,N,V_productId"
+ "T@\"NSString\",C,N,V_serialNumber"
+ "T@\"NSString\",C,N,V_vendorId"
+ "T@\"NSUUID\",&,N,V_identifier"
+ "T@\"NSUUID\",C,N,V_baUUID"
+ "TB,N,GisConnected,V_connected"
+ "XPC error for didAddLocalFindableAccessory: %li"
+ "XPC error for didRemoveLocalFindableAccessory: %li"
+ "_alternateSerialNumber"
+ "_baUUID"
+ "_btAddress"
+ "_connected"
+ "_identifier"
+ "_irkData"
+ "_productId"
+ "_vendorId"
+ "alternateSerialNumber"
+ "btAddress"
+ "connected"
+ "didAddLocalFindableAccessory:completion:"
+ "didRemoveLocalFindableAccessory:completion:"
+ "identifier"
+ "initWithIdentifier:name:connected:"
+ "irkData"
+ "isConnected"
+ "productId"
+ "setAlternateSerialNumber:"
+ "setBaUUID:"
+ "setBtAddress:"
+ "setConnected:"
+ "setIdentifier:"
+ "setIrkData:"
+ "setProductId:"
+ "setVendorId:"
+ "v32@0:8@\"FMDLocalFindableAccessory\"16@?<v@?@\"NSError\">24"
+ "vendorId"

```
