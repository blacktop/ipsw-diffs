## NanoRegistry

> `/System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry`

```diff

-920.4.0.0.0
-  __TEXT.__text: 0x5033c
+921.9.0.0.0
+  __TEXT.__text: 0x50c2c
   __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_methlist: 0x42e4
-  __TEXT.__cstring: 0x3c50
+  __TEXT.__objc_methlist: 0x43e4
+  __TEXT.__cstring: 0x3c9b
   __TEXT.__const: 0x40
   __TEXT.__gcc_except_tab: 0x9f4
-  __TEXT.__oslogstring: 0x1c09
+  __TEXT.__oslogstring: 0x1cbe
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x18b0
-  __TEXT.__objc_classname: 0x8a6
-  __TEXT.__objc_methname: 0x6ded
-  __TEXT.__objc_methtype: 0x1398
-  __TEXT.__objc_stubs: 0x4fc0
+  __TEXT.__unwind_info: 0x18dc
+  __TEXT.__objc_classname: 0x8e3
+  __TEXT.__objc_methname: 0x7267
+  __TEXT.__objc_methtype: 0x13f8
+  __TEXT.__objc_stubs: 0x5060
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__const: 0x1c80
-  __DATA_CONST.__objc_classlist: 0x270
+  __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5500
-  __DATA_CONST.__objc_selrefs: 0x1c08
+  __DATA_CONST.__objc_const: 0x56e0
+  __DATA_CONST.__objc_selrefs: 0x1ca0
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_classrefs: 0x300
+  __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__cfstring: 0x44a0
-  __AUTH_CONST.__objc_const: 0x2300
+  __AUTH_CONST.__cfstring: 0x44e0
+  __AUTH_CONST.__objc_const: 0x2420
   __AUTH_CONST.__const: 0xac0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x4b8
   __AUTH.__data: 0x18
-  __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x2f0
-  __DATA.__objc_superrefs: 0x1b0
-  __DATA.__objc_ivar: 0x348
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x36c
   __DATA.__data: 0x740
   __DATA.__bss: 0x30
   __DATA.__common: 0x0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 87A4D8D5-4584-3B21-AD74-500CCAC109B2
-  Functions: 2043
-  Symbols:   6356
-  CStrings:  2848
+  UUID: 7039AF59-4EBD-3D8D-86DE-CF9E3375B215
+  Functions: 2062
+  Symbols:   6424
+  CStrings:  2900
 
Symbols:
+ +[WatchSetupAdvertisementIdentifier _consistencyCheckForAdvertisingIdentifier:pairingStrategy:deviceSize:enclosureMaterial:]
+ +[WatchSetupExtendedMetadata _consistencyCheckForPairingVersion:productVersionMajor:productVersionMinor:postFailSafeObliteration:encodedSystemVersion:]
+ -[WatchSetupAdvertisementIdentifier advertisingIdentifier]
+ -[WatchSetupAdvertisementIdentifier deviceSize]
+ -[WatchSetupAdvertisementIdentifier enclosureMaterial]
+ -[WatchSetupAdvertisementIdentifier humanReadableName]
+ -[WatchSetupAdvertisementIdentifier initWithAdvertisingIdentifier:pairingStrategy:deviceSize:enclosureMaterial:]
+ -[WatchSetupAdvertisementIdentifier initWithPackedIdentifierData:]
+ -[WatchSetupAdvertisementIdentifier packedIdentifierData]
+ -[WatchSetupAdvertisementIdentifier pairingStrategy]
+ -[WatchSetupExtendedMetadata encodedSystemVersion]
+ -[WatchSetupExtendedMetadata initWithPackedExtendedMetadataData:]
+ -[WatchSetupExtendedMetadata initWithPairingVersion:productVersionMajor:productVersionMinor:postFailSafeObliteration:encodedSystemVersion:]
+ -[WatchSetupExtendedMetadata packedExtendedMetadataData]
+ -[WatchSetupExtendedMetadata pairingVersion]
+ -[WatchSetupExtendedMetadata postFailSafeObliteration]
+ -[WatchSetupExtendedMetadata productVersionMajor]
+ -[WatchSetupExtendedMetadata productVersionMinor]
+ _OBJC_CLASS_$_WatchSetupAdvertisementIdentifier
+ _OBJC_CLASS_$_WatchSetupExtendedMetadata
+ _OBJC_IVAR_$_WatchSetupAdvertisementIdentifier._advertisingIdentifier
+ _OBJC_IVAR_$_WatchSetupAdvertisementIdentifier._deviceSize
+ _OBJC_IVAR_$_WatchSetupAdvertisementIdentifier._enclosureMaterial
+ _OBJC_IVAR_$_WatchSetupAdvertisementIdentifier._pairingStrategy
+ _OBJC_IVAR_$_WatchSetupExtendedMetadata._encodedSystemVersion
+ _OBJC_IVAR_$_WatchSetupExtendedMetadata._pairingVersion
+ _OBJC_IVAR_$_WatchSetupExtendedMetadata._postFailSafeObliteration
+ _OBJC_IVAR_$_WatchSetupExtendedMetadata._productVersionMajor
+ _OBJC_IVAR_$_WatchSetupExtendedMetadata._productVersionMinor
+ _OBJC_METACLASS_$_WatchSetupAdvertisementIdentifier
+ _OBJC_METACLASS_$_WatchSetupExtendedMetadata
+ __NRStringRepresentationFromInteger
+ __OBJC_$_CLASS_METHODS_WatchSetupAdvertisementIdentifier
+ __OBJC_$_CLASS_METHODS_WatchSetupExtendedMetadata
+ __OBJC_$_INSTANCE_METHODS_WatchSetupAdvertisementIdentifier
+ __OBJC_$_INSTANCE_METHODS_WatchSetupExtendedMetadata
+ __OBJC_$_INSTANCE_VARIABLES_WatchSetupAdvertisementIdentifier
+ __OBJC_$_INSTANCE_VARIABLES_WatchSetupExtendedMetadata
+ __OBJC_$_PROP_LIST_WatchSetupAdvertisementIdentifier
+ __OBJC_$_PROP_LIST_WatchSetupExtendedMetadata
+ __OBJC_CLASS_RO_$_WatchSetupAdvertisementIdentifier
+ __OBJC_CLASS_RO_$_WatchSetupExtendedMetadata
+ __OBJC_METACLASS_RO_$_WatchSetupAdvertisementIdentifier
+ __OBJC_METACLASS_RO_$_WatchSetupExtendedMetadata
+ __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ue170006Ev
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ ___65-[NRTermsAcknowledgementRegistry add:forDeviceID:withCompletion:]_block_invoke.186
+ ___85-[NRTermsAcknowledgementRegistry checkForAcknowledgement:forDeviceID:withCompletion:]_block_invoke.188
+ ___block_literal_global.234
+ ___block_literal_global.54
+ _objc_msgSend$_consistencyCheckForAdvertisingIdentifier:pairingStrategy:deviceSize:enclosureMaterial:
+ _objc_msgSend$_consistencyCheckForPairingVersion:productVersionMajor:productVersionMinor:postFailSafeObliteration:encodedSystemVersion:
+ _objc_msgSend$initWithBytes:length:
+ _objc_msgSend$initWithFormat:
+ _objc_msgSend$substringWithRange:
- __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB7v160006Ev
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- ___65-[NRTermsAcknowledgementRegistry add:forDeviceID:withCompletion:]_block_invoke.185
- ___85-[NRTermsAcknowledgementRegistry checkForAcknowledgement:forDeviceID:withCompletion:]_block_invoke.186
- ___block_literal_global.233
- ___block_literal_global.53
CStrings:
+ "%05lu%@%@%@"
+ "@32@0:8I16C20C24C28"
+ "@36@0:8C16C20C24B28I32"
+ "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
+ "B32@0:8I16C20C24C28"
+ "B36@0:8C16C20C24B28I32"
+ "C16@0:8"
+ "Incorrect size of packed extended metadata, expecting >= %lu but got %lu"
+ "Incorrect size of packed identifier data, expecting %lu but got %lu"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,N"
+ "TB,R,N,V_postFailSafeObliteration"
+ "TC,R,N,V_deviceSize"
+ "TC,R,N,V_enclosureMaterial"
+ "TC,R,N,V_pairingStrategy"
+ "TC,R,N,V_pairingVersion"
+ "TC,R,N,V_productVersionMajor"
+ "TC,R,N,V_productVersionMinor"
+ "TI,R,N,V_advertisingIdentifier"
+ "TI,R,N,V_encodedSystemVersion"
+ "Tried to create out-off-bound char rep!"
+ "WatchSetupAdvertisementIdentifier"
+ "WatchSetupExtendedMetadata"
+ "_advertisingIdentifier"
+ "_consistencyCheckForAdvertisingIdentifier:pairingStrategy:deviceSize:enclosureMaterial:"
+ "_consistencyCheckForPairingVersion:productVersionMajor:productVersionMinor:postFailSafeObliteration:encodedSystemVersion:"
+ "_deviceSize"
+ "_enclosureMaterial"
+ "_pairingStrategy"
+ "_postFailSafeObliteration"
+ "_productVersionMajor"
+ "_productVersionMinor"
+ "advertisingIdentifier"
+ "deviceSize"
+ "humanReadableName"
+ "initWithAdvertisingIdentifier:pairingStrategy:deviceSize:enclosureMaterial:"
+ "initWithBytes:length:"
+ "initWithFormat:"
+ "initWithPackedExtendedMetadataData:"
+ "initWithPackedIdentifierData:"
+ "initWithPairingVersion:productVersionMajor:productVersionMinor:postFailSafeObliteration:encodedSystemVersion:"
+ "packedExtendedMetadataData"
+ "packedIdentifierData"
+ "pairingStrategy"
+ "postFailSafeObliteration"
+ "productVersionMajor"
+ "productVersionMinor"
+ "substringWithRange:"

```
