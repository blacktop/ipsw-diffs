## PlatformSSOCore

> `/System/Library/PrivateFrameworks/PlatformSSOCore.framework/PlatformSSOCore`

```diff

-483.100.72.0.0
-  __TEXT.__text: 0x931b8
+483.100.73.0.0
+  __TEXT.__text: 0x937cc
   __TEXT.__auth_stubs: 0x1ab0
-  __TEXT.__objc_methlist: 0x5fd0
+  __TEXT.__objc_methlist: 0x5ff0
   __TEXT.__const: 0x1854
-  __TEXT.__cstring: 0xa40b
+  __TEXT.__cstring: 0xa48b
   __TEXT.__oslogstring: 0x19d7
   __TEXT.__gcc_except_tab: 0x7ec
   __TEXT.__dlopen_cstrs: 0xa6

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_types: 0x38
-  __TEXT.__unwind_info: 0x2108
+  __TEXT.__unwind_info: 0x2120
   __TEXT.__eh_frame: 0x598
   __TEXT.__objc_classname: 0xf93
-  __TEXT.__objc_methname: 0xcd37
+  __TEXT.__objc_methname: 0xce07
   __TEXT.__objc_methtype: 0x2a03
-  __TEXT.__objc_stubs: 0x7160
+  __TEXT.__objc_stubs: 0x71a0
   __DATA_CONST.__got: 0x920
-  __DATA_CONST.__const: 0x2448
+  __DATA_CONST.__const: 0x24a8
   __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b48
+  __DATA_CONST.__objc_selrefs: 0x2b58
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x58
   __AUTH_CONST.__auth_got: 0xd68
   __AUTH_CONST.__const: 0x780
-  __AUTH_CONST.__cfstring: 0x7480
-  __AUTH_CONST.__objc_const: 0x142a0
+  __AUTH_CONST.__cfstring: 0x74e0
+  __AUTH_CONST.__objc_const: 0x142d0
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x3460
   __AUTH.__data: 0x1a0
-  __DATA.__objc_ivar: 0x620
+  __DATA.__objc_ivar: 0x624
   __DATA.__data: 0x1068
   __DATA.__bss: 0xd31
   __DATA.__common: 0x88

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: DB7B117D-E934-312D-9864-ED9B5A20DAF9
-  Functions: 3670
-  Symbols:   12198
-  CStrings:  5101
+  UUID: 233B8A10-88A7-35D7-937D-9EC2E184EC3D
+  Functions: 3676
+  Symbols:   12215
+  CStrings:  5113
 
Symbols:
+ -[POConfigurationCoreManager temporarySessionAccounts]
+ -[PODeviceConfiguration _encryptAndSaveTemporaryAccountCredential:account:key:]
+ -[PODeviceConfiguration _encryptAndSaveTemporaryAccountCredential:account:key:].cold.1
+ -[PODeviceConfiguration decryptTemporaryAccountCredentialForAccount:]
+ -[PODeviceConfiguration decryptTemporaryAccountCredentialForAccount:].cold.1
+ -[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:account:]
+ -[PODeviceConfiguration hasTemporaryAccountCredentialForAccount:]
+ -[PODeviceConfiguration setTemporaryAccountCredentials:]
+ -[PODeviceConfiguration temporaryAccountCredentials]
+ GCC_except_table91
+ _OBJC_IVAR_$_POConfigurationCoreManager._temporarySessionAccounts
+ _OBJC_IVAR_$_PODeviceConfiguration._temporaryAccountCredentials
+ ___38-[PODeviceConfiguration initWithData:]_block_invoke_2
+ ___48-[PODeviceConfiguration setDeviceEncryptionKey:]_block_invoke_2
+ ___48-[PODeviceConfiguration setDeviceEncryptionKey:]_block_invoke_2.cold.1
+ ___54-[POConfigurationCoreManager currentUserConfiguration]_block_invoke.69
+ ___54-[POConfigurationCoreManager currentUserConfiguration]_block_invoke.69.cold.1
+ ___54-[PODeviceConfiguration dataRepresentationForDisplay:]_block_invoke_2
+ ___54-[PODeviceConfiguration dataRepresentationForDisplay:]_block_invoke_2.cold.1
+ ___55-[POConfigurationCoreManager currentLoginConfiguration]_block_invoke.77
+ ___55-[POConfigurationCoreManager currentLoginConfiguration]_block_invoke.77.cold.1
+ ___56-[POConfigurationCoreManager currentDeviceConfiguration]_block_invoke.73
+ ___56-[POConfigurationCoreManager currentDeviceConfiguration]_block_invoke.73.cold.1
+ ___56-[POConfigurationCoreManager userLoginStateForUserName:]_block_invoke.96
+ ___59-[POConfigurationCoreManager userConfigurationForUserName:]_block_invoke.88
+ ___63-[POConfigurationCoreManager savePendingSSOTokens:forUserName:]_block_invoke.111
+ ___63-[POConfigurationCoreManager saveStashedSSOTokens:forUserName:]_block_invoke.119
+ ___66-[POConfigurationCoreManager retrievePendingSSOTokensForUserName:]_block_invoke.115
+ ___66-[POConfigurationCoreManager retrieveStashedSSOTokensForUserName:]_block_invoke.123
+ ___67-[POConfigurationCoreManager updateLoginTypeForUserName:loginType:]_block_invoke.110
+ ___69-[PODeviceConfiguration decryptTemporaryAccountCredentialForAccount:]_block_invoke
+ ___69-[PODeviceConfiguration decryptTemporaryAccountCredentialForAccount:]_block_invoke.62
+ ___69-[PODeviceConfiguration decryptTemporaryAccountCredentialForAccount:]_block_invoke.62.cold.1
+ ___69-[PODeviceConfiguration decryptTemporaryAccountCredentialForAccount:]_block_invoke.cold.1
+ ___79-[PODeviceConfiguration _encryptAndSaveTemporaryAccountCredential:account:key:]_block_invoke
+ ___79-[PODeviceConfiguration _encryptAndSaveTemporaryAccountCredential:account:key:]_block_invoke.46
+ ___79-[PODeviceConfiguration _encryptAndSaveTemporaryAccountCredential:account:key:]_block_invoke.46.cold.1
+ ___79-[PODeviceConfiguration _encryptAndSaveTemporaryAccountCredential:account:key:]_block_invoke.52
+ ___79-[PODeviceConfiguration _encryptAndSaveTemporaryAccountCredential:account:key:]_block_invoke.52.cold.1
+ ___79-[PODeviceConfiguration _encryptAndSaveTemporaryAccountCredential:account:key:]_block_invoke.cold.1
+ ___84-[POConfigurationCoreManager updateLoginStateForUserName:state:loginDate:loginType:]_block_invoke.102
+ ___84-[POConfigurationCoreManager updateLoginStateForUserName:state:loginDate:loginType:]_block_invoke.102.cold.1
+ ___84-[POConfigurationCoreManager updateLoginStateForUserName:state:loginDate:loginType:]_block_invoke.108
+ ___block_descriptor_41_e8_32s_e33_v32?0"NSString"8"NSData"16^B24ls32l8
+ ___block_descriptor_48_e8_32s_e25_v32?0"NSString"8Q16^B24ls32l8
+ ___block_literal_global.482
+ _kTemporaryUserAccountName1
+ _kTemporaryUserAccountName2
+ _objc_msgSend$_encryptAndSaveTemporaryAccountCredential:account:key:
+ _objc_msgSend$decryptTemporaryAccountCredentialForAccount:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$temporarySessionAccounts
- -[PODeviceConfiguration decryptTemporaryAccountCredential]
- -[PODeviceConfiguration decryptTemporaryAccountCredential].cold.1
- -[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]
- -[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:].cold.1
- -[PODeviceConfiguration hasTemporaryAccountCredential]
- -[PODeviceConfiguration setTemporaryAccountCredential:]
- -[PODeviceConfiguration temporaryAccountCredential]
- GCC_except_table90
- _OBJC_IVAR_$_PODeviceConfiguration._temporaryAccountCredential
- ___48-[PODeviceConfiguration setDeviceEncryptionKey:]_block_invoke.cold.1
- ___54-[POConfigurationCoreManager currentUserConfiguration]_block_invoke.68
- ___54-[POConfigurationCoreManager currentUserConfiguration]_block_invoke.68.cold.1
- ___54-[PODeviceConfiguration dataRepresentationForDisplay:]_block_invoke.cold.1
- ___55-[POConfigurationCoreManager currentLoginConfiguration]_block_invoke.76
- ___55-[POConfigurationCoreManager currentLoginConfiguration]_block_invoke.76.cold.1
- ___56-[POConfigurationCoreManager currentDeviceConfiguration]_block_invoke.72
- ___56-[POConfigurationCoreManager currentDeviceConfiguration]_block_invoke.72.cold.1
- ___56-[POConfigurationCoreManager userLoginStateForUserName:]_block_invoke.95
- ___58-[PODeviceConfiguration decryptTemporaryAccountCredential]_block_invoke
- ___58-[PODeviceConfiguration decryptTemporaryAccountCredential]_block_invoke.62
- ___58-[PODeviceConfiguration decryptTemporaryAccountCredential]_block_invoke.62.cold.1
- ___58-[PODeviceConfiguration decryptTemporaryAccountCredential]_block_invoke.cold.1
- ___59-[POConfigurationCoreManager userConfigurationForUserName:]_block_invoke.87
- ___63-[POConfigurationCoreManager savePendingSSOTokens:forUserName:]_block_invoke.110
- ___63-[POConfigurationCoreManager saveStashedSSOTokens:forUserName:]_block_invoke.118
- ___66-[POConfigurationCoreManager retrievePendingSSOTokensForUserName:]_block_invoke.114
- ___66-[POConfigurationCoreManager retrieveStashedSSOTokensForUserName:]_block_invoke.122
- ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke
- ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.46
- ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.46.cold.1
- ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.52
- ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.52.cold.1
- ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.cold.1
- ___67-[POConfigurationCoreManager updateLoginTypeForUserName:loginType:]_block_invoke.109
- ___84-[POConfigurationCoreManager updateLoginStateForUserName:state:loginDate:loginType:]_block_invoke.101
- ___84-[POConfigurationCoreManager updateLoginStateForUserName:state:loginDate:loginType:]_block_invoke.101.cold.1
- ___84-[POConfigurationCoreManager updateLoginStateForUserName:state:loginDate:loginType:]_block_invoke.107
- ___block_literal_global.474
- _objc_msgSend$decryptTemporaryAccountCredential
- _objc_msgSend$encryptAndSaveTemporaryAccountCredential:
CStrings:
+ "T@\"NSArray\",R,V_temporarySessionAccounts"
+ "T@\"NSMutableDictionary\",C,V_temporaryAccountCredentials"
+ "_encryptAndSaveTemporaryAccountCredential:account:key:"
+ "_temporaryAccountCredentials"
+ "_temporarySessionAccounts"
+ "decryptTemporaryAccountCredentialForAccount:"
+ "encryptAndSaveTemporaryAccountCredential:account:"
+ "hasTemporaryAccountCredentialForAccount:"
+ "setTemporaryAccountCredentials:"
+ "temporaryAccountCredentials"
+ "temporarySessionAccounts"
+ "temporary_session1"
+ "temporary_session2"
+ "v32@?0@\"NSString\"8@\"NSData\"16^B24"
+ "v32@?0@\"NSString\"8Q16^B24"
- "T@\"NSData\",C,V_temporaryAccountCredential"
- "_temporaryAccountCredential"
- "encryptAndSaveTemporaryAccountCredential:"
- "hasTemporaryAccountCredential"
- "setTemporaryAccountCredential:"

```
