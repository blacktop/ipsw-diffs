## CoreAccessories

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories`

```diff

-898.2.3.0.0
-  __TEXT.__text: 0x2f304
+898.42.3.0.0
+  __TEXT.__text: 0x2f428
   __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__objc_methlist: 0xf2c
+  __TEXT.__objc_methlist: 0xf6c
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x375a
+  __TEXT.__cstring: 0x37dc
   __TEXT.__oslogstring: 0x3a62
   __TEXT.__gcc_except_tab: 0x618
   __TEXT.__ustring: 0xa
   __TEXT.__unwind_info: 0x874
   __TEXT.__objc_classname: 0x258
-  __TEXT.__objc_methname: 0x401d
-  __TEXT.__objc_methtype: 0x13fc
-  __TEXT.__objc_stubs: 0x2800
+  __TEXT.__objc_methname: 0x40ab
+  __TEXT.__objc_methtype: 0x1408
+  __TEXT.__objc_stubs: 0x2820
   __DATA_CONST.__got: 0x38
-  __DATA_CONST.__const: 0x1c10
+  __DATA_CONST.__const: 0x1c90
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2a60
-  __DATA_CONST.__objc_selrefs: 0xcf0
+  __DATA_CONST.__objc_const: 0x2ac0
+  __DATA_CONST.__objc_selrefs: 0xd18
   __DATA_CONST.__objc_arraydata: 0xd8
-  __AUTH_CONST.__cfstring: 0x35e0
+  __AUTH_CONST.__cfstring: 0x36e0
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x370
   __DATA.__objc_protorefs: 0x50
   __DATA.__objc_classrefs: 0x100
   __DATA.__objc_superrefs: 0x48
-  __DATA.__objc_ivar: 0xc0
+  __DATA.__objc_ivar: 0xc8
   __DATA.__data: 0x740
   __DATA.__bss: 0xe0
-  __DATA_DIRTY.__const: 0xa40
+  __DATA_DIRTY.__const: 0x9c0
   __DATA_DIRTY.__objc_const: 0x510
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__data: 0x138

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EAE85B4E-6F0A-3BC0-9A09-4846720540E5
-  Functions: 1130
-  Symbols:   3691
-  CStrings:  1932
+  UUID: E3EC49A9-17B8-30E6-A643-3D8833CD148D
+  Functions: 1135
+  Symbols:   3720
+  CStrings:  1958
 
Symbols:
+ -[ACCTransportPlugin connectedThroughAdapter:]
+ -[_ACCExternalAccessoryInfo productID]
+ -[_ACCExternalAccessoryInfo setProductID:]
+ -[_ACCExternalAccessoryInfo setVendorID:]
+ -[_ACCExternalAccessoryInfo vendorID]
+ GCC_except_table35
+ _OBJC_IVAR_$__ACCExternalAccessoryInfo._productID
+ _OBJC_IVAR_$__ACCExternalAccessoryInfo._vendorID
+ ___107-[ACCExternalAccessoryProvider createExternalAccessorySessionForProtocol:accessoryUUID:withEASessionReply:]_block_invoke.221
+ ___107-[ACCExternalAccessoryProvider createExternalAccessorySessionForProtocol:accessoryUUID:withEASessionReply:]_block_invoke.221.cold.1
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.194
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.194.cold.1
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.195
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.195.cold.1
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.195.cold.2
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.197
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.197.cold.1
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.197.cold.2
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.200
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.200.cold.1
+ ___51-[ACCExternalAccessoryProvider currentVehicleInfo:]_block_invoke.241
+ ___51-[ACCExternalAccessoryProvider currentVehicleInfo:]_block_invoke.241.cold.1
+ ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.216
+ ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.216.cold.1
+ ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.216.cold.2
+ ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.216.cold.3
+ ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.217
+ ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.217.cold.1
+ ___99-[ACCExternalAccessoryProvider sendOutgoingExternalAccessoryData:forEASessionIdentifier:withReply:]_block_invoke.231
+ ___99-[ACCExternalAccessoryProvider sendOutgoingExternalAccessoryData:forEASessionIdentifier:withReply:]_block_invoke.231.cold.1
+ ___block_literal_global.220
+ ___block_literal_global.224
+ ___block_literal_global.226
+ ___block_literal_global.228
+ _kACCExternalAccessoryProductIDKey
+ _kACCExternalAccessoryVendorIDKey
+ _kACCInfo_ProductID
+ _kACCInfo_VendorID
+ _kACCProperties_Connection_AdapterPID
+ _kACCProperties_Connection_AdapterVID
+ _kACCProperties_Connection_IsAdapter
+ _kACCProperties_Connection_ManagerParent
+ _kCFACCExternalAccessoryProductIDKey
+ _kCFACCExternalAccessoryVendorIDKey
+ _kCFACCInfo_ProductID
+ _kCFACCInfo_VendorID
+ _kCFACCProperties_Connection_AdapterPID
+ _kCFACCProperties_Connection_AdapterVID
+ _kCFACCProperties_Connection_IsAdapter
+ _kCFACCProperties_Connection_ManagerParent
+ _objc_msgSend$connectedThroughAdapter:
- GCC_except_table28
- GCC_except_table31
- ___107-[ACCExternalAccessoryProvider createExternalAccessorySessionForProtocol:accessoryUUID:withEASessionReply:]_block_invoke.210
- ___107-[ACCExternalAccessoryProvider createExternalAccessorySessionForProtocol:accessoryUUID:withEASessionReply:]_block_invoke.210.cold.1
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.183
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.183.cold.1
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.184
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.184.cold.1
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.184.cold.2
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.186
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.186.cold.1
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.186.cold.2
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.189
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.189.cold.1
- ___51-[ACCExternalAccessoryProvider currentVehicleInfo:]_block_invoke.230
- ___51-[ACCExternalAccessoryProvider currentVehicleInfo:]_block_invoke.230.cold.1
- ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.205
- ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.205.cold.1
- ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.205.cold.2
- ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.205.cold.3
- ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.206
- ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.206.cold.1
- ___99-[ACCExternalAccessoryProvider sendOutgoingExternalAccessoryData:forEASessionIdentifier:withReply:]_block_invoke.220
- ___99-[ACCExternalAccessoryProvider sendOutgoingExternalAccessoryData:forEASessionIdentifier:withReply:]_block_invoke.220.cold.1
- ___block_literal_global.188
- ___block_literal_global.219
- ___block_literal_global.229
CStrings:
+ "\f"
+ "@\"NSNumber\""
+ "ACCExternalAccessoryProductIDKey"
+ "ACCExternalAccessoryVendorIDKey"
+ "AdapterPID"
+ "AdapterVID"
+ "IsAdapter"
+ "ManagerParent"
+ "ProductID"
+ "T@\"NSNumber\",&,V_productID"
+ "T@\"NSNumber\",&,V_vendorID"
+ "VendorID"
+ "_productID"
+ "_vendorID"
+ "connectedThroughAdapter:"
+ "productID"
+ "setProductID:"
+ "setVendorID:"
+ "vendorID"
- "\n"

```
