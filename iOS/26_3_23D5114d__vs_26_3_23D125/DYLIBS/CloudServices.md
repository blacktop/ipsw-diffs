## CloudServices

> `/System/Library/PrivateFrameworks/CloudServices.framework/CloudServices`

```diff

 694.80.7.0.0
-  __TEXT.__text: 0x29a84
-  __TEXT.__auth_stubs: 0xb80
-  __TEXT.__objc_methlist: 0x2394
+  __TEXT.__text: 0x2b388
+  __TEXT.__auth_stubs: 0xbb0
+  __TEXT.__objc_methlist: 0x2464
   __TEXT.__const: 0xd00
-  __TEXT.__cstring: 0x2223
-  __TEXT.__gcc_except_tab: 0x6c8
-  __TEXT.__oslogstring: 0x20b6
-  __TEXT.__unwind_info: 0x970
+  __TEXT.__cstring: 0x23f6
+  __TEXT.__gcc_except_tab: 0x6d4
+  __TEXT.__oslogstring: 0x2176
+  __TEXT.__unwind_info: 0x9b0
   __TEXT.__objc_classname: 0x353
-  __TEXT.__objc_methname: 0x4b7d
-  __TEXT.__objc_methtype: 0xec4
-  __TEXT.__objc_stubs: 0x3280
-  __DATA_CONST.__got: 0x278
-  __DATA_CONST.__const: 0xb10
+  __TEXT.__objc_methname: 0x4ca8
+  __TEXT.__objc_methtype: 0xeeb
+  __TEXT.__objc_stubs: 0x3440
+  __DATA_CONST.__got: 0x288
+  __DATA_CONST.__const: 0xb50
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12d0
+  __DATA_CONST.__objc_selrefs: 0x1318
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x5d0
-  __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x2180
-  __AUTH_CONST.__objc_const: 0x32e8
+  __AUTH_CONST.__auth_got: 0x5e8
+  __AUTH_CONST.__const: 0x140
+  __AUTH_CONST.__cfstring: 0x2380
+  __AUTH_CONST.__objc_const: 0x3450
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x24c
+  __DATA.__objc_ivar: 0x264
   __DATA.__data: 0x2d0
-  __DATA.__bss: 0x58
+  __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0x5f0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x48
+  __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 551A9149-D93D-39EC-9B88-30D97CA9D573
-  Functions: 1044
-  Symbols:   489
-  CStrings:  1833
+  UUID: A7620A67-E35F-348E-B3DE-CB9B6D584C10
+  Functions: 1073
+  Symbols:   505
+  CStrings:  1891
 
Symbols:
+ _AppleIDAuthSupportCreateVerifier
+ _AppleIDAuthSupportPBKDF2SRP
+ _CCRandomGenerateBytes
+ _SecureBackupIsDBREnabled
+ _SecureBackupIsDBREnabledClearOverride
+ _SecureBackupIsDBREnabledOverride
+ _kAppleIDAuthSupportProtocolSRPGROUP2048SHA256PBKDF
+ _kAppleIDAuthSupportProtocolSRPGROUP2048SHA256PBKDFLegacy
+ _kEscrowServiceDBRFDELabel
+ _kEscrowServiceDBRLabel
+ _kSecureBackupContainsFDEiCloudIdentityKey
+ _kSecureBackupDBRFDEKey
+ _kSecureBackupDBRKey
+ _kSecureBackupFDEMetadataHashKey
+ _kSecureBackupFDEMetadataKey
+ _kSecureBackupKeybagFDESHA256Key
CStrings:
+ "@\"AppleIDPasswordMetadata\"16@0:8"
+ "@80@0:8@16@24@32@40@48@56B64@68i76"
+ "AppleIDAuthSupportPBKDF2SRP failed: %@"
+ "BackupKeybagFDESHA256"
+ "DBR"
+ "DBR ff overridden to %s"
+ "DBR ff override removed"
+ "DBR set via feature flag to %s"
+ "Failed to copy from SRP response"
+ "Failed to get salt from SRP response"
+ "IdMSPasswordGeneration"
+ "IdMSPasswordVerifierIterations"
+ "IdMSPasswordVerifierProto"
+ "SecureBackupContainsFDEiCloudIdentity"
+ "SecureBackupDBRFDEKey"
+ "SecureBackupDBRKey"
+ "SecureBackupFDEMetadata"
+ "SecureBackupFDEMetadataHash"
+ "SecureBackupWrappedKeys"
+ "T@\"AppleIDPasswordMetadata\",R,N"
+ "TB,N,V_dbr"
+ "TB,N,V_dbrFDE"
+ "TB,R,N,V_dbr"
+ "TB,R,N,V_dbrFDE"
+ "TB,R,V_useAppleIDPassword"
+ "_dbr"
+ "_dbrFDE"
+ "_useAppleIDPassword"
+ "com.apple.protectedcloudstorage.dbrv2.record"
+ "com.apple.protectedcloudstorage.fde.record"
+ "could not create verifier"
+ "dbr"
+ "dbrFDE"
+ "derivePassword: no password metadata"
+ "derivePasswordDBR"
+ "failed to parse FDE key registry: %@"
+ "initWithDSID:escrowRecordContents:passcodeStashSecret:recoveryPassphrase:recordID:recordLabel:useAppleIDPassword:appleIDPasswordMetadata:reqVersion:"
+ "initWithLength:"
+ "integerValue"
+ "kPCSMetadataiCDPDBRv2"
+ "numberWithInt:"
+ "setDbr:"
+ "setDbrFDE:"
+ "useAppleIDPassword"
- "@68@0:8@16@24@32@40@48@56i64"
- "initWithDSID:escrowRecordContents:passcodeStashSecret:recoveryPassphrase:recordID:recordLabel:reqVersion:"

```
