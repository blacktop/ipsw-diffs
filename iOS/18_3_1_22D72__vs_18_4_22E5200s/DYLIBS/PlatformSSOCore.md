## PlatformSSOCore

> `/System/Library/PrivateFrameworks/PlatformSSOCore.framework/PlatformSSOCore`

```diff

-417.80.4.0.0
-  __TEXT.__text: 0x997ec
-  __TEXT.__auth_stubs: 0x1bf0
-  __TEXT.__objc_methlist: 0x5754
-  __TEXT.__const: 0x14a4
-  __TEXT.__cstring: 0xb504
-  __TEXT.__oslogstring: 0x18ef
-  __TEXT.__gcc_except_tab: 0x754
+417.100.33.0.0
+  __TEXT.__text: 0x99548
+  __TEXT.__auth_stubs: 0x1bd0
+  __TEXT.__objc_methlist: 0x5c28
+  __TEXT.__const: 0x1574
+  __TEXT.__cstring: 0xb7b9
+  __TEXT.__oslogstring: 0x19cf
+  __TEXT.__gcc_except_tab: 0x780
   __TEXT.__dlopen_cstrs: 0xa6
   __TEXT.__swift5_typeref: 0x16e
   __TEXT.__constg_swiftt: 0x348

   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_types: 0x34
   __TEXT.__swift5_capture: 0x20
-  __TEXT.__unwind_info: 0x2098
-  __TEXT.__eh_frame: 0x690
+  __TEXT.__unwind_info: 0x2150
+  __TEXT.__eh_frame: 0x6c0
   __TEXT.__objc_classname: 0xd48
-  __TEXT.__objc_methname: 0xb860
-  __TEXT.__objc_methtype: 0x28ab
-  __TEXT.__objc_stubs: 0x6aa0
-  __DATA_CONST.__got: 0x930
-  __DATA_CONST.__const: 0x2408
+  __TEXT.__objc_methname: 0xbba7
+  __TEXT.__objc_methtype: 0x288e
+  __TEXT.__objc_stubs: 0x6be0
+  __DATA_CONST.__got: 0x938
+  __DATA_CONST.__const: 0x2438
   __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2780
+  __DATA_CONST.__objc_selrefs: 0x28d0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0xe08
+  __AUTH_CONST.__auth_got: 0xdf8
   __AUTH_CONST.__auth_ptr: 0x190
-  __AUTH_CONST.__const: 0x7f0
-  __AUTH_CONST.__cfstring: 0x6f80
-  __AUTH_CONST.__objc_const: 0x14700
+  __AUTH_CONST.__const: 0x7d0
+  __AUTH_CONST.__cfstring: 0x71c0
+  __AUTH_CONST.__objc_const: 0x13e58
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x3450
   __AUTH.__data: 0x180
-  __DATA.__objc_ivar: 0x5b8
-  __DATA.__data: 0xf92
-  __DATA.__bss: 0xd15
+  __DATA.__objc_ivar: 0x5c4
+  __DATA.__data: 0xfa2
+  __DATA.__bss: 0xd18
   __DATA.__common: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3424
-  Symbols:   4534
-  CStrings:  4161
+  Functions: 3767
+  Symbols:   4909
+  CStrings:  4200
 
Symbols:
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _kAttestationCacheTimeInterval
+ _kTemporaryUserAccountName
+ _kTemporaryUserFullName
- _CFRetain
CStrings:
+ "\x02\x19"
+ "%@:%@"
+ "%s file = %{public}@, data = %{public}@, %{public}@ on %@"
+ "%s shared = %{public}@, createUsersEnabled = %{public}@, newUserAuthorizationMode = %{public}@ on %@"
+ "-[POConfigurationCoreManager isTemporaryAccountUserName:]"
+ "-[PODeviceConfiguration supportsCreateTemporaryUsers]"
+ "-[POKeychainHelper _checkForCachedAttestationForExtensionIdentifier:keyHash:]"
+ "-[POKeychainHelper _saveAttestationToKeychain:extensionIdentifier:keyHash:attestationDate:error:]"
+ "-[POKeychainHelper retrieveTokensFromKeychainForService:username:system:returningTokens:metaData:]"
+ "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/backup_serialize.c"
+ "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/shared_crypto.c"
+ "@\"NSObject\""
+ "B\x12\x14##U"
+ "B48@0:8@16@24@32^@40"
+ "B56@0:8@16@24@32@40^@48"
+ "Cached attestation not found."
+ "Cached attestation too old."
+ "Completed saving data to: %{public}@, %{public}@"
+ "Configuriation for: %{public}@"
+ "Deleting cached attestations"
+ "Encryption algorithm not supported."
+ "Failed to deserialize attestation data"
+ "Failed to encrypt temporary account credential when updating encryption key."
+ "Failed to encrypt temporary account credential."
+ "Failed to remove cached attestation."
+ "Failed to remove cached attestations."
+ "Failed to save attestation data in cache."
+ "Failed to serialize attestation data"
+ "Falied to get hash for key."
+ "Missing device encryption public key."
+ "Platform SSO Temporary User"
+ "T@\"NSData\",C,V_temporaryAccountCredential"
+ "T@\"NSString\",&,V_userName"
+ "TB,N,V_allowDeviceIdentifiersInAttestation"
+ "T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},N,V_deviceEncryptionKey"
+ "T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},N,V_deviceSigningKey"
+ "T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},R,N"
+ "Temporary"
+ "User is Platform SSO temporary account"
+ "_allowDeviceIdentifiersInAttestation"
+ "_checkForCachedAttestationForExtensionIdentifier:keyHash:"
+ "_deleteAllCachedAttestations"
+ "_deleteCachedAttestationForExtensionIdentifier:key:"
+ "_deleteCachedAttestationForExtensionIdentifier:keyHash:"
+ "_saveAttestationToKeychain:extensionIdentifier:keyHash:attestationDate:error:"
+ "_saveAttestationToKeychain:extensionIdentifier:keyHash:error:"
+ "_temporaryAccountCredential"
+ "_userLock"
+ "allowDeviceIdentifiersInAttestation"
+ "com.apple.platformsso.attestation"
+ "dataWithPropertyList:format:options:error:"
+ "decryptTemporaryAccountCredential"
+ "encryptAndSaveTemporaryAccountCredential"
+ "encryptAndSaveTemporaryAccountCredential:"
+ "failed to decrypt temporary account credential."
+ "i36@0:8@16@24B32"
+ "i52@0:8@16@24B32^@36^@44"
+ "isTemporaryAccountUserName:"
+ "kAttestationDate"
+ "propertyListWithData:options:format:error:"
+ "publicKeyHashForKey:"
+ "removeTokensFromKeychainWithService:username:system:"
+ "retrieveTokensFromKeychainForService:username:system:returningTokens:metaData:"
+ "setAllowDeviceIdentifiersInAttestation:"
+ "setTemporaryAccountCredential:"
+ "supportsCreateTemporaryUsers"
+ "temporary"
+ "temporaryAccountCredential"
+ "temporary_session"
+ "v32@0:8@16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24"
- "\x01\x19"
- "%s userName = %{public}@, context = %{public}@ on %@"
- "-[POConfigurationCoreManager insertTokenForUserName:]"
- "-[POConfigurationCoreManager retrieveStashedDecryptionContextForUserName:]"
- "-[POConfigurationCoreManager saveCachedContextsToDisk]"
- "-[POConfigurationCoreManager saveStashedDecryptionContext:forUserName:]"
- "-[POConfigurationCoreManager verifyTokenForUserName:passwordContext:]"
- "-[POKeychainHelper retrieveTokensFromKeychainForService:username:returningTokens:metaData:]"
- "2\x12\x14##T"
- "Completed saving data to: %{public}@"
- "PSSOInsertToken"
- "PSSOVerifyToken"
- "T@\"NSString\",R,V_userName"
- "T^{__SecKey=},N,V_deviceEncryptionKey"
- "T^{__SecKey=},N,V_deviceSigningKey"
- "T^{__SecKey=},R,N"
- "i32@0:8@16@24"
- "i48@0:8@16@24^@32^@40"
- "identifier for user not found when saving stashed context"
- "insertTokenForUserName complete"
- "insertTokenForUserName error = %{public}@"
- "insertTokenForUserName:"
- "removeTokensFromKeychainWithService:username:"
- "retrieveStashedDecryptionContextForUserName:"
- "retrieveTokensFromKeychainForService:username:returningTokens:metaData:"
- "saveCachedContextsToDisk"
- "saveStashedDecryptionContext:forUserName:"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
- "v40@0:8@\"NSString\"16@\"NSData\"24@?<v@?B@\"NSError\">32"
- "verifyTokenForUserName:passwordContext:"

```
