## CloudServices

> `/System/Library/PrivateFrameworks/CloudServices.framework/CloudServices`

```diff

-638.40.26.0.0
-  __TEXT.__text: 0x2480c
-  __TEXT.__auth_stubs: 0xa20
-  __TEXT.__objc_methlist: 0x19fc
+638.42.1.0.0
+  __TEXT.__text: 0x261e0
+  __TEXT.__auth_stubs: 0xa50
+  __TEXT.__objc_methlist: 0x1b2c
   __TEXT.__const: 0xc90
-  __TEXT.__cstring: 0x1f70
-  __TEXT.__gcc_except_tab: 0x5a8
-  __TEXT.__oslogstring: 0x1fc2
-  __TEXT.__unwind_info: 0x810
-  __TEXT.__objc_classname: 0x27e
-  __TEXT.__objc_methname: 0x43a6
-  __TEXT.__objc_methtype: 0xc8b
-  __TEXT.__objc_stubs: 0x2ea0
-  __DATA_CONST.__got: 0x250
-  __DATA_CONST.__const: 0xa20
-  __DATA_CONST.__objc_classlist: 0x90
+  __TEXT.__cstring: 0x21ad
+  __TEXT.__gcc_except_tab: 0x5b4
+  __TEXT.__oslogstring: 0x20af
+  __TEXT.__unwind_info: 0x858
+  __TEXT.__objc_classname: 0x298
+  __TEXT.__objc_methname: 0x46dc
+  __TEXT.__objc_methtype: 0xcef
+  __TEXT.__objc_stubs: 0x3160
+  __DATA_CONST.__got: 0x268
+  __DATA_CONST.__const: 0xa50
+  __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1108
+  __DATA_CONST.__objc_selrefs: 0x11a0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x78
+  __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x520
+  __AUTH_CONST.__auth_got: 0x538
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x2020
-  __AUTH_CONST.__objc_const: 0x2fc0
+  __AUTH_CONST.__const: 0xe0
+  __AUTH_CONST.__cfstring: 0x2260
+  __AUTH_CONST.__objc_const: 0x3330
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x1e8
+  __DATA.__objc_ivar: 0x214
   __DATA.__data: 0x2a0
-  __DATA.__bss: 0x30
-  __DATA_DIRTY.__objc_data: 0x370
+  __DATA.__bss: 0x38
+  __DATA_DIRTY.__objc_data: 0x3c0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x40
+  __DATA_DIRTY.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 872
-  Symbols:   438
-  CStrings:  1452
+  Functions: 910
+  Symbols:   454
+  CStrings:  1523
 
Symbols:
+ _AppleIDAuthSupportCreateVerifier
+ _AppleIDAuthSupportPBKDF2SRP
+ _CCRandomGenerateBytes
+ _OBJC_CLASS_$_AppleIDPasswordMetadata
+ _OBJC_METACLASS_$_AppleIDPasswordMetadata
+ _SecureBackupIsGuitarfishEnabled
+ _SecureBackupIsGuitarfishEnabledClearOverride
+ _SecureBackupIsGuitarfishEnabledOverride
+ _kAppleIDAuthSupportProtocolSRPGROUP2048SHA256PBKDF
+ _kAppleIDAuthSupportProtocolSRPGROUP2048SHA256PBKDFLegacy
+ _kEscrowServiceGuitarfishLabel
+ _kEscrowServiceGuitarfishTokenLabel
+ _kSecureBackupAppleIDPasswordMetadataKey
+ _kSecureBackupGuitarfishKey
+ _kSecureBackupGuitarfishRecoveryTokenMetadataKey
+ _kSecureBackupGuitarfishTokenKey
CStrings:
+ "\x12"
+ "\x14\x16"
+ "\x15"
+ "?\x0f\n"
+ "@\"AppleIDPasswordMetadata\""
+ "@\"AppleIDPasswordMetadata\"16@0:8"
+ "@32@0:8@16B24i28"
+ "@36@0:8@16@24i32"
+ "@72@0:8@16@24@32@40@48B56@60i68"
+ "AppleIDAuthSupportPBKDF2SRP failed: %!@(MISSING)"
+ "AppleIDPasswordMetadata"
+ "DEMO: enrolling with salt: %!@(MISSING)"
+ "DEMO: recovering with salt: %!@(MISSING)"
+ "DerivedDBRSeedAESPID"
+ "Failed to copy from SRP response"
+ "Failed to get salt from SRP response"
+ "Guitarfish"
+ "Guitarfish ff overridden to %!s(MISSING)"
+ "Guitarfish ff override removed"
+ "Guitarfish set via feature flag to %!s(MISSING)"
+ "GuitarfishDemo"
+ "IdMSPasswordGeneration"
+ "IdMSPasswordVerifierIterations"
+ "IdMSPasswordVerifierProto"
+ "SecureBackupAppleIDPasswordMetadataKey"
+ "SecureBackupGuitarfishKey"
+ "SecureBackupGuitarfishTokenKey"
+ "SecureBackupWrappedKeys"
+ "T@\"AppleIDPasswordMetadata\",&,N,V_appleIDPasswordMetadata"
+ "T@\"AppleIDPasswordMetadata\",R,N"
+ "T@\"AppleIDPasswordMetadata\",R,N,V_appleIDPasswordMetadata"
+ "T@\"NSData\",R,N,V_salt"
+ "T@\"NSString\",R,N,V_proto"
+ "TB,N,V_guitarfish"
+ "TB,N,V_guitarfishToken"
+ "TB,R,N,V_guitarfish"
+ "TB,R,N,V_guitarfishToken"
+ "TB,R,V_useAppleIDPassword"
+ "Ti,R,N,V_iterations"
+ "_appleIDPasswordMetadata"
+ "_guitarfish"
+ "_guitarfishToken"
+ "_iterations"
+ "_proto"
+ "_salt"
+ "_useAppleIDPassword"
+ "appleIDPasswordMetadata"
+ "com.apple.protectedcloudstorage.guitarfish-recovery-token.record"
+ "com.apple.protectedcloudstorage.guitarfish.record"
+ "could not create verifier"
+ "decodeInt32ForKey:"
+ "derivePassword: no password metadata"
+ "derivePasswordGuitarfish"
+ "disabled"
+ "enabled"
+ "encodeInt32:forKey:"
+ "guitarfish"
+ "guitarfishToken"
+ "initWithDSID:escrowRecordContents:recoveryPassphrase:recordID:recordLabel:useAppleIDPassword:appleIDPasswordMetadata:reqVersion:"
+ "initWithLength:"
+ "initWithProto:salt:iterations:"
+ "initWithRequest:validate:reqVersion:"
+ "iterations"
+ "kPCSMetadataiCDPGuitarfish"
+ "kSecureBackupGuitarfishRecoveryTokenMetadataKey"
+ "numberWithInt:"
+ "proto"
+ "salt"
+ "setAppleIDPasswordMetadata:"
+ "setGuitarfish:"
+ "setGuitarfishToken:"
+ "useAppleIDPassword"
+ "validatePassphrasePresentOrPending"
- "\x04"
- "\x13\x16"
- "?\x0f\t"
- "@60@0:8@16@24@32@40@48i56"
- "initWithDSID:escrowRecordContents:recoveryPassphrase:recordID:recordLabel:reqVersion:"

```
