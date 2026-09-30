## HomeKitDiagnosticExtension

> `/System/Library/Frameworks/HomeKit.framework/PlugIns/HomeKitDiagnosticExtension.appex/HomeKitDiagnosticExtension`

```diff

-1241.4.11.0.0
-  __TEXT.__text: 0x19dd8
-  __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__objc_stubs: 0x3600
-  __TEXT.__objc_methlist: 0x18a0
+1278.5.8.2.0
+  __TEXT.__text: 0x1b498
+  __TEXT.__auth_stubs: 0x810
+  __TEXT.__objc_stubs: 0x3780
+  __TEXT.__objc_methlist: 0x1eac
+  __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__const: 0x50
   __TEXT.__gcc_except_tab: 0x57c
-  __TEXT.__cstring: 0x15a1
-  __TEXT.__objc_classname: 0x84e
-  __TEXT.__objc_methname: 0x3733
-  __TEXT.__objc_methtype: 0x5ff
-  __TEXT.__oslogstring: 0x1404
-  __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x6f0
-  __DATA_CONST.__auth_got: 0x408
-  __DATA_CONST.__got: 0x390
+  __TEXT.__cstring: 0x1640
+  __TEXT.__oslogstring: 0x14be
+  __TEXT.__objc_methname: 0x3c08
+  __TEXT.__objc_classname: 0x880
+  __TEXT.__objc_methtype: 0x60b
+  __TEXT.__unwind_info: 0x728
+  __DATA_CONST.__auth_got: 0x418
+  __DATA_CONST.__got: 0x3b0
   __DATA_CONST.__const: 0x8d0
-  __DATA_CONST.__cfstring: 0x1ee0
-  __DATA_CONST.__objc_classlist: 0x1e8
+  __DATA_CONST.__cfstring: 0x1f60
+  __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xd8
-  __DATA_CONST.__objc_intobj: 0x48
+  __DATA_CONST.__objc_superrefs: 0xe0
+  __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x4350
-  __DATA.__objc_selrefs: 0xf60
-  __DATA.__objc_ivar: 0x108
-  __DATA.__objc_data: 0x1310
+  __DATA.__objc_const: 0x43c8
+  __DATA.__objc_selrefs: 0x1200
+  __DATA.__objc_ivar: 0x118
+  __DATA.__objc_data: 0x13b0
   __DATA.__data: 0x4e0
   __DATA.__bss: 0x170
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/Frameworks/Matter.framework/Matter
   - /System/Library/Frameworks/MediaPlayer.framework/MediaPlayer
   - /System/Library/Frameworks/Network.framework/Network
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 539
-  Symbols:   256
-  CStrings:  1205
+  Functions: 607
+  Symbols:   262
+  CStrings:  1285
 
Symbols:
+ _OBJC_CLASS_$_NSMutableData
+ _SecKeyCopyExternalRepresentation
+ _SecKeyCreateRandomKey
+ _kSecAttrKeySizeInBits
+ _kSecAttrKeyType
+ _kSecAttrKeyTypeECSECPrimeRandom
CStrings:
+ "%{public}@Failed to copy nfc reader key external representation: %@"
+ "%{public}@Failed to create nfc reader key: %@"
+ "%{public}@Time to reach next transition point is negative: %lldms"
+ "%{public}@Unexpected nfc reader key external representation length %lu"
+ "@\"NSNumber\""
+ "HMDHomeNFCReaderIdentifierCodingKey"
+ "HMDHomeNFCReaderKey"
+ "HMDHomeNFCReaderPublicKeyExternalRepresentationCodingKey"
+ "HMDValueTransformerAdapter"
+ "Has Private Key"
+ "Public Key External Representation"
+ "T@\"HMDHomeKitVersion\",R,C"
+ "T@\"NSData\",R,C,V_identifier"
+ "T@\"NSData\",R,C,V_privateKey"
+ "T@\"NSData\",R,C,V_publicKeyExternalRepresentation"
+ "T@\"NSDictionary\",R,C"
+ "T@\"NSNumber\",&,N,V_woWLANDarkPollMinimumInterval"
+ "_privateKey"
+ "_publicKeyExternalRepresentation"
+ "_woWLANDarkPollMinimumInterval"
+ "appendData:"
+ "createRandomKey"
+ "createWithDictionaryRepresentation:"
+ "createWithExternalRepresentation:"
+ "dictionaryRepresentation"
+ "externalRepresentation"
+ "hmf_dataForKey:"
+ "hmf_hexadecimalRepresentation"
+ "identifierForKey:"
+ "initWithIdentifier:privateKey:publicKeyExternalRepresentation:"
+ "initWithMajorVersion:minorVersion:updateVersion:"
+ "isEqualToRPIdentity:"
+ "key-identifier"
+ "privateKey"
+ "publicKey"
+ "publicKeyExternalRepresentation"
+ "publicKeyWithPublicKeyExternalRepresentation:"
+ "setWoWLANDarkPollMinimumInterval:"
+ "subdataWithRange:"
+ "transitionPointsWithMillisecondsElapsedSinceStartOfDay:"
+ "version10_0"
+ "version10_1"
+ "version10_2"
+ "version10_3"
+ "version10_3_1"
+ "version10_4"
+ "version10_5"
+ "version10_6"
+ "version11_1"
+ "version11_2"
+ "version11_4"
+ "version12_0"
+ "version12_1"
+ "version12_2"
+ "version12_4"
+ "version1_0"
+ "version2_0"
+ "version2_1"
+ "version2_2"
+ "version3_0"
+ "version3_1"
+ "version3_2"
+ "version4_0"
+ "version4_1"
+ "version4_1_1"
+ "version4_2"
+ "version4_3"
+ "version5_0"
+ "version5_1"
+ "version5_2"
+ "version6_0"
+ "version6_1"
+ "version6_2"
+ "version6_3"
+ "version7_0"
+ "version7_0_1"
+ "version7_1"
+ "version7_2"
+ "version7_3"
+ "version8_0"
+ "version8_1"
+ "version8_2"
+ "version9_0"
+ "version9_1"
+ "woWLANDarkPollMinimumInterval"
- "%{public}@Time to reach next transiton point is negative: %lldms"
- "HMDValueTransformerAdapater"
- "T@\"HMDHomeKitVersion\",R"
- "initWithVersionString:"
- "isEqualToRPIndentity:"
- "transitionPointsWithmillisecondsElapsedSinceStartOfDay:"

```
