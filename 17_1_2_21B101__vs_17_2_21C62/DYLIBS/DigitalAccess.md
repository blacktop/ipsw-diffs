## DigitalAccess

> `/System/Library/PrivateFrameworks/DigitalAccess.framework/DigitalAccess`

```diff

-41.7.0.0.0
-  __TEXT.__text: 0x1729c
-  __TEXT.__auth_stubs: 0x590
+42.10.0.0.0
+  __TEXT.__text: 0x16d78
+  __TEXT.__auth_stubs: 0x5a0
   __TEXT.__objc_methlist: 0xf74
   __TEXT.__const: 0x538
-  __TEXT.__cstring: 0x539a
+  __TEXT.__cstring: 0x529c
   __TEXT.__oslogstring: 0xb
-  __TEXT.__gcc_except_tab: 0x620
-  __TEXT.__unwind_info: 0x7c0
+  __TEXT.__gcc_except_tab: 0x5f0
+  __TEXT.__unwind_info: 0x7b4
   __TEXT.__objc_classname: 0x3cd
-  __TEXT.__objc_methname: 0x340a
-  __TEXT.__objc_methtype: 0x11fb
-  __TEXT.__objc_stubs: 0x1cc0
+  __TEXT.__objc_methname: 0x3466
+  __TEXT.__objc_methtype: 0x11bb
+  __TEXT.__objc_stubs: 0x1ca0
   __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0xd60
+  __DATA_CONST.__const: 0xd38
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x25a0
-  __DATA_CONST.__objc_selrefs: 0x960
-  __AUTH_CONST.__cfstring: 0x1ac0
+  __DATA_CONST.__objc_const: 0x2660
+  __DATA_CONST.__objc_selrefs: 0x958
+  __AUTH_CONST.__cfstring: 0x1a40
   __AUTH_CONST.__objc_const: 0x48
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__auth_got: 0x2d8
+  __AUTH_CONST.__auth_got: 0x2e0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_protorefs: 0x38
-  __DATA.__objc_classrefs: 0x170
+  __DATA.__objc_classrefs: 0x168
   __DATA.__objc_superrefs: 0xb0
-  __DATA.__objc_ivar: 0x18c
+  __DATA.__objc_ivar: 0x1a4
   __DATA.__data: 0x660
   __DATA.__bss: 0x62
   __DATA_DIRTY.__const: 0x280

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5C993181-E124-3525-925C-3D814AB75A00
+  UUID: 6A27C07C-5FB6-3D36-A143-9734E51DD79A
   Functions: 491
   Symbols:   1824
-  CStrings:  1385
+  CStrings:  1383
 
Symbols:
+ +[DAUtils decryptVehicleMobilizationData:forKeyWithIdentifier:]
+ -[DAKeyManagementSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]
+ -[DAKeyPairingSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]
+ -[KmlTlv valueAsUnsignedChar]
+ GCC_except_table44
+ GCC_except_table47
+ GCC_except_table50
+ GCC_except_table53
+ GCC_except_table56
+ _OBJC_IVAR_$_KmlDeviceConfigurationData._carSupportsUpdateAttestation
+ _OBJC_IVAR_$_KmlDeviceConfigurationData._initiatorSupportedFrameworkVersionsData
+ _OBJC_IVAR_$_KmlDeviceConfigurationData._maxOfflineAttestationCount
+ _OBJC_IVAR_$_KmlDeviceConfigurationData._onlineBleOOBMasterKeyOverride
+ _OBJC_IVAR_$_KmlDeviceConfigurationData._sharingInAChainTestFromFriend
+ _OBJC_IVAR_$_KmlDeviceConfigurationData._vehicleSupportedFrameworkVersionsData
+ ___78-[DAKeyPairingSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]_block_invoke
+ ___78-[DAKeyPairingSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]_block_invoke_2
+ ___81-[DAKeyManagementSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]_block_invoke
+ ___81-[DAKeyManagementSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]_block_invoke_2
+ _objc_msgSend$consumeTrackingReceipt:otherJSONData:forKeyWithIdentifier:callback:
+ _objc_msgSend$decryptVehicleMobilizationData:forKeyWithIdentifier:
+ _objc_retain_x6
- +[DAUtils decyptVehicleMobilizationData:forKeyWithIdentifier:callback:]
- -[DAKeyManagementSession sendTrackingReceipt:slotIdentifier:confidentialMailboxData:ephemeralPublicKey:productPlanIdentifier:forKeyWithIdentifier:]
- -[DAKeyPairingSession sendTrackingReceipt:slotIdentifier:confidentialMailboxData:ephemeralPublicKey:productPlanIdentifier:forKeyWithIdentifier:]
- GCC_except_table41
- GCC_except_table45
- GCC_except_table48
- GCC_except_table51
- GCC_except_table54
- GCC_except_table57
- _OBJC_CLASS_$_NSJSONSerialization
- ___144-[DAKeyPairingSession sendTrackingReceipt:slotIdentifier:confidentialMailboxData:ephemeralPublicKey:productPlanIdentifier:forKeyWithIdentifier:]_block_invoke
- ___144-[DAKeyPairingSession sendTrackingReceipt:slotIdentifier:confidentialMailboxData:ephemeralPublicKey:productPlanIdentifier:forKeyWithIdentifier:]_block_invoke_2
- ___147-[DAKeyManagementSession sendTrackingReceipt:slotIdentifier:confidentialMailboxData:ephemeralPublicKey:productPlanIdentifier:forKeyWithIdentifier:]_block_invoke
- ___147-[DAKeyManagementSession sendTrackingReceipt:slotIdentifier:confidentialMailboxData:ephemeralPublicKey:productPlanIdentifier:forKeyWithIdentifier:]_block_invoke_2
- ___87-[DAKeyPairingSession setTrackingReceipt:vehicleMobilizationData:forKeyWithIdentifier:]_block_invoke
- ___90-[DAKeyManagementSession setTrackingReceipt:vehicleMobilizationData:forKeyWithIdentifier:]_block_invoke
- ___block_descriptor_64_e8_32r40r48r56r_e49_v40?0"NSData"8"NSData"16"NSData"24"NSData"32lr32l8r40l8r48l8r56l8
- _objc_msgSend$JSONObjectWithData:options:error:
- _objc_msgSend$decyptVehicleMobilizationData:forKeyWithIdentifier:callback:
- _objc_msgSend$updateTrackingReceipt:slotIdentifier:confidentialMailboxData:ephemeralPublicKey:productPlanIdentifier:forKeyWithIdentifier:callback:
CStrings:
+ "\x01-"
+ "+[DAUtils decryptVehicleMobilizationData:forKeyWithIdentifier:]"
+ "-[DAKeyManagementSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]"
+ "-[DAKeyManagementSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]_block_invoke"
+ "-[DAKeyManagementSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]_block_invoke_2"
+ "-[DAKeyManagementSession setTrackingReceipt:slotIdentifier:confidentialMailboxData:ephemeralPublicKey:forKeyWithIdentifier:]"
+ "-[DAKeyPairingSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]"
+ "-[DAKeyPairingSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]_block_invoke"
+ "-[DAKeyPairingSession sendTrackingReceipt:otherJSONData:forKeyWithIdentifier:]_block_invoke_2"
+ "-[DAKeyPairingSession setTrackingReceipt:slotIdentifier:confidentialMailboxData:ephemeralPublicKey:forKeyWithIdentifier:]"
+ "-[KmlTlv valueAsUnsignedChar]"
+ "Deprecated API"
+ "Result of decrypting vehicleMobilizationData: %@"
+ "Vv48@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "_carSupportsUpdateAttestation"
+ "_initiatorSupportedFrameworkVersionsData"
+ "_maxOfflineAttestationCount"
+ "_onlineBleOOBMasterKeyOverride"
+ "_sharingInAChainTestFromFriend"
+ "_vehicleSupportedFrameworkVersionsData"
+ "consumeTrackingReceipt:otherJSONData:forKeyWithIdentifier:callback:"
+ "decryptVehicleMobilizationData:forKeyWithIdentifier:"
- "\x01*"
- "+[DAUtils decyptVehicleMobilizationData:forKeyWithIdentifier:callback:]"
- "-[DAKeyManagementSession sendTrackingReceipt:slotIdentifier:confidentialMailboxData:ephemeralPublicKey:productPlanIdentifier:forKeyWithIdentifier:]"
- "-[DAKeyManagementSession sendTrackingReceipt:slotIdentifier:confidentialMailboxData:ephemeralPublicKey:productPlanIdentifier:forKeyWithIdentifier:]_block_invoke"
- "-[DAKeyManagementSession sendTrackingReceipt:slotIdentifier:confidentialMailboxData:ephemeralPublicKey:productPlanIdentifier:forKeyWithIdentifier:]_block_invoke_2"
- "-[DAKeyPairingSession sendTrackingReceipt:slotIdentifier:confidentialMailboxData:ephemeralPublicKey:productPlanIdentifier:forKeyWithIdentifier:]"
- "-[DAKeyPairingSession sendTrackingReceipt:slotIdentifier:confidentialMailboxData:ephemeralPublicKey:productPlanIdentifier:forKeyWithIdentifier:]_block_invoke"
- "-[DAKeyPairingSession sendTrackingReceipt:slotIdentifier:confidentialMailboxData:ephemeralPublicKey:productPlanIdentifier:forKeyWithIdentifier:]_block_invoke_2"
- "Failed to decrypt vehicleMobilizationData response: %@"
- "JSONObjectWithData:options:error:"
- "Vv72@0:8@\"NSData\"16@\"NSData\"24@\"NSData\"32@\"NSData\"40@\"NSData\"48@\"NSString\"56@?<v@?@\"NSError\">64"
- "Vv72@0:8@16@24@32@40@48@56@?64"
- "confidentialMailBox"
- "confidentialMailboxData"
- "decyptVehicleMobilizationData:forKeyWithIdentifier:callback:"
- "productPlanIdentifier"
- "slot"
- "slotIdentifier"
- "updateTrackingReceipt:slotIdentifier:confidentialMailboxData:ephemeralPublicKey:productPlanIdentifier:forKeyWithIdentifier:callback:"
- "v40@?0@\"NSData\"8@\"NSData\"16@\"NSData\"24@\"NSData\"32"

```
