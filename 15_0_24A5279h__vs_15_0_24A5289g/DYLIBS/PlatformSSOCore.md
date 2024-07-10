## PlatformSSOCore

> `/System/Library/PrivateFrameworks/PlatformSSOCore.framework/Versions/A/PlatformSSOCore`

```diff

-417.0.10.0.1
-  __TEXT.__text: 0xbb14c
+417.0.12.0.0
+  __TEXT.__text: 0xbcbb8
   __TEXT.__auth_stubs: 0x1fa0
-  __TEXT.__objc_methlist: 0x5b04
+  __TEXT.__objc_methlist: 0x5bc4
   __TEXT.__const: 0x1500
-  __TEXT.__cstring: 0xcdcc
-  __TEXT.__oslogstring: 0x350c
-  __TEXT.__gcc_except_tab: 0xe78
+  __TEXT.__cstring: 0xcf1c
+  __TEXT.__oslogstring: 0x362c
+  __TEXT.__gcc_except_tab: 0xe84
   __TEXT.__dlopen_cstrs: 0x294
   __TEXT.__swift5_typeref: 0x1a8
   __TEXT.__constg_swiftt: 0x348

   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_types: 0x34
   __TEXT.__swift5_capture: 0x20
-  __TEXT.__unwind_info: 0x2498
+  __TEXT.__unwind_info: 0x24e8
   __TEXT.__eh_frame: 0x648
   __TEXT.__objc_classname: 0xdd8
-  __TEXT.__objc_methname: 0xc553
-  __TEXT.__objc_methtype: 0x2adb
-  __TEXT.__objc_stubs: 0x7c60
-  __DATA_CONST.__got: 0xa28
+  __TEXT.__objc_methname: 0xc77b
+  __TEXT.__objc_methtype: 0x2b68
+  __TEXT.__objc_stubs: 0x7e40
+  __DATA_CONST.__got: 0xa38
   __DATA_CONST.__const: 0x1f00
   __DATA_CONST.__objc_classlist: 0x4d8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b00
+  __DATA_CONST.__objc_selrefs: 0x2b98
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x200
   __DATA_CONST.__objc_arraydata: 0x58
   __AUTH_CONST.__auth_got: 0xfe0
   __AUTH_CONST.__auth_ptr: 0x1a8
-  __AUTH_CONST.__const: 0x1690
-  __AUTH_CONST.__cfstring: 0x7c20
-  __AUTH_CONST.__objc_const: 0x14fa8
+  __AUTH_CONST.__const: 0x16e0
+  __AUTH_CONST.__cfstring: 0x7d20
+  __AUTH_CONST.__objc_const: 0x150a8
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x3590
   __AUTH.__data: 0x180
-  __DATA.__objc_ivar: 0x5e0
+  __DATA.__objc_ivar: 0x5e8
   __DATA.__data: 0x1070
   __DATA.__bss: 0xfb8
   __DATA.__common: 0x91

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/StorageKit.framework/Versions/A/StorageKit
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3844
-  Symbols:   8640
-  CStrings:  1798
+  Functions: 3874
+  Symbols:   8707
+  CStrings:  1807
 
Symbols:
+ +[POBaseSystemSupport prebootVolumePathForUUID:shouldUnmount:]
+ -[POAgentCoreProcess bypassLoginPolicyForUserName:volume:contextData:completion:]
+ -[POAgentCoreProcess verifySecurityEntitlement]
+ -[POAgentCoreProcess verifySecurityEntitlement].cold.1
+ -[POAuthPluginCoreProcess bypassLoginPolicyForUserName:volume:contextData:]
+ -[POConfigurationCoreManager initWithUserName:identifierProvider:sharedOnly:volume:]
+ -[PODaemonCoreConnection initWithVolume:]
+ -[PODaemonCoreConnection initWithVolume:].cold.1
+ -[PODaemonCoreConnection setVolume:]
+ -[PODaemonCoreConnection useVolume:completion:]
+ -[PODaemonCoreConnection volume]
+ -[PODaemonCoreProcess _volumeConfigurationPathForVolumeUUID:]
+ -[PODaemonCoreProcess _volumeConfigurationPathForVolumeUUID:].cold.1
+ -[PODaemonCoreProcess copyPrebootKeysForVolumeUUID:]
+ -[PODaemonCoreProcess copyPrebootKeysForVolumeUUID:].cold.1
+ -[PODaemonCoreProcess loadKeybagForSystemVolume:]
+ -[PODaemonCoreProcess loadKeybagForSystemVolume:].cold.1
+ -[PODaemonCoreProcess loadKeybagForSystemVolume:].cold.2
+ -[PODaemonCoreProcess loadKeybagForSystemVolume:].cold.3
+ -[PODaemonCoreProcess setVolumeUUID:]
+ -[PODaemonCoreProcess useVolume:completion:]
+ -[PODaemonCoreProcess volumeUUID]
+ -[POLoginUserCore bypassLoginPolicyForUserName:volume:contextData:]
+ -[POServiceCoreConnection bypassLoginPolicyForUserName:volume:contextData:completion:]
+ -[POUserLoginState setLastUpdated:]
+ GCC_except_table14
+ GCC_except_table179
+ GCC_except_table27
+ GCC_except_table29
+ GCC_except_table31
+ GCC_except_table37
+ GCC_except_table39
+ GCC_except_table46
+ GCC_except_table49
+ GCC_except_table53
+ GCC_except_table55
+ GCC_except_table58
+ GCC_except_table61
+ GCC_except_table62
+ GCC_except_table64
+ GCC_except_table65
+ GCC_except_table68
+ GCC_except_table71
+ GCC_except_table74
+ GCC_except_table77
+ GCC_except_table8
+ GCC_except_table82
+ OBJC_IVAR_$_PODaemonCoreConnection._volume
+ OBJC_IVAR_$_PODaemonCoreProcess._volumeUUID
+ _OBJC_CLASS_$_SKAPFSDisk
+ _PO_LOG_POLoginUserCore
+ _SKAPFSVolumeRolePreboot
+ __103-[POAgentCoreProcess exchangeKeyWithPublicKeyData:userName:passwordContext:responseContext:completion:]_block_invoke.138
+ __103-[POAgentCoreProcess exchangeKeyWithPublicKeyData:userName:passwordContext:responseContext:completion:]_block_invoke.140
+ __103-[POAgentCoreProcess exchangeKeyWithPublicKeyData:userName:passwordContext:responseContext:completion:]_block_invoke.140.cold.1
+ __103-[POAgentCoreProcess exchangeKeyWithPublicKeyData:userName:passwordContext:responseContext:completion:]_block_invoke.146
+ __103-[POAgentCoreProcess exchangeKeyWithPublicKeyData:userName:passwordContext:responseContext:completion:]_block_invoke.146.cold.1
+ __103-[POAgentCoreProcess exchangeKeyWithPublicKeyData:userName:passwordContext:responseContext:completion:]_block_invoke.152
+ __103-[POAgentCoreProcess exchangeKeyWithPublicKeyData:userName:passwordContext:responseContext:completion:]_block_invoke.152.cold.1
+ __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.104
+ __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.104.cold.1
+ __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.110
+ __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.110.cold.1
+ __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.114
+ __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.114.cold.1
+ __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.118
+ __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.119
+ __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.119.cold.1
+ __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.123
+ __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.123.cold.1
+ __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.94
+ __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.94.cold.1
+ __43-[PODaemonCoreConnection _connectToService]_block_invoke.88
+ __43-[PODaemonCoreConnection _connectToService]_block_invoke.88.cold.1
+ __43-[PODaemonCoreConnection _connectToService]_block_invoke.90
+ __43-[PODaemonCoreConnection _connectToService]_block_invoke.90.cold.1
+ __43-[PODaemonCoreConnection _connectToService]_block_invoke.93
+ __44-[POServiceCoreConnection _connectToService]_block_invoke.74
+ __44-[POServiceCoreConnection _connectToService]_block_invoke.74.cold.1
+ __47-[PODaemonCoreConnection useVolume:completion:]_block_invoke.cold.1
+ __49-[PODaemonCoreProcess loadKeybagForSystemVolume:]_block_invoke.cold.1
+ __50-[PODaemonCoreProcess writeData:toPath:saveError:]_block_invoke.45
+ __50-[PODaemonCoreProcess writeData:toPath:saveError:]_block_invoke.45.cold.1
+ __50-[PODaemonCoreProcess writeData:toPath:saveError:]_block_invoke.51
+ __50-[PODaemonCoreProcess writeData:toPath:saveError:]_block_invoke.51.cold.1
+ __52-[PODaemonCoreProcess copyPrebootKeysForVolumeUUID:]_block_invoke.19
+ __52-[PODaemonCoreProcess copyPrebootKeysForVolumeUUID:]_block_invoke.19.cold.1
+ __52-[PODaemonCoreProcess copyPrebootKeysForVolumeUUID:]_block_invoke.cold.1
+ __53-[POAgentCoreProcess getLoginTypeForUser:completion:]_block_invoke.24
+ __53-[POAgentCoreProcess getLoginTypeForUser:completion:]_block_invoke.24.cold.1
+ __53-[PODaemonCoreProcess _saveUserLoginStateList:error:]_block_invoke.102
+ __53-[PODaemonCoreProcess _saveUserLoginStateList:error:]_block_invoke.102.cold.1
+ __53-[PODaemonCoreProcess _saveUserLoginStateList:error:]_block_invoke.106
+ __53-[PODaemonCoreProcess _saveUserLoginStateList:error:]_block_invoke.106.cold.1
+ __56-[POAgentCoreProcess insertTokenForUserName:completion:]_block_invoke.cold.1
+ __56-[PODaemonCoreProcess _userLoginStateListDataWithError:]_block_invoke.79
+ __56-[PODaemonCoreProcess _userLoginStateListDataWithError:]_block_invoke.79.cold.1
+ __58-[PODaemonCoreProcess _parseUserLoginStateListData:error:]_block_invoke.86
+ __58-[PODaemonCoreProcess _parseUserLoginStateListData:error:]_block_invoke.86.cold.1
+ __59+[PODaemonCoreProcess createPrebootKey:encryptedKey:error:]_block_invoke.35
+ __59+[PODaemonCoreProcess createPrebootKey:encryptedKey:error:]_block_invoke.35.cold.1
+ __61-[PODaemonCoreProcess _userConfigurationForIdentifier:error:]_block_invoke.72
+ __61-[PODaemonCoreProcess _userConfigurationForIdentifier:error:]_block_invoke.72.cold.1
+ __62+[POBaseSystemSupport prebootVolumePathForUUID:shouldUnmount:]_block_invoke.cold.1
+ __62-[PODaemonCoreProcess saveCachedContextsToDiskWithCompletion:]_block_invoke.138
+ __62-[PODaemonCoreProcess saveCachedContextsToDiskWithCompletion:]_block_invoke.138.cold.1
+ __62-[PODaemonCoreProcess saveCachedContextsToDiskWithCompletion:]_block_invoke.cold.1
+ __63-[PODaemonCoreProcess _saveCachedContextsToDiskWithCompletion:]_block_invoke.149
+ __63-[PODaemonCoreProcess _saveCachedContextsToDiskWithCompletion:]_block_invoke.149.cold.1
+ __63-[PODaemonCoreProcess _saveCachedContextsToDiskWithCompletion:]_block_invoke.150
+ __63-[PODaemonCoreProcess _saveCachedContextsToDiskWithCompletion:]_block_invoke.150.cold.1
+ __63-[PODaemonCoreProcess _saveCachedContextsToDiskWithCompletion:]_block_invoke.151
+ __63-[PODaemonCoreProcess _saveCachedContextsToDiskWithCompletion:]_block_invoke.151.cold.1
+ __67-[POLoginUserCore bypassLoginPolicyForUserName:volume:contextData:]_block_invoke.cold.1
+ __68-[POAgentCoreProcess verifyPasswordUser:passwordContext:completion:]_block_invoke.63
+ __68-[POAgentCoreProcess verifyPasswordUser:passwordContext:completion:]_block_invoke.63.cold.1
+ __68-[POAgentCoreProcess verifyPasswordUser:passwordContext:completion:]_block_invoke.69
+ __68-[POAgentCoreProcess verifyPasswordUser:passwordContext:completion:]_block_invoke.69.cold.1
+ __68-[POAgentCoreProcess verifyPasswordUser:passwordContext:completion:]_block_invoke.73
+ __68-[POAgentCoreProcess verifyPasswordUser:passwordContext:completion:]_block_invoke.80
+ __68-[POAgentCoreProcess verifyPasswordUser:passwordContext:completion:]_block_invoke.80.cold.1
+ __68-[POAgentCoreProcess verifyPasswordUser:passwordContext:completion:]_block_invoke.86
+ __68-[POAgentCoreProcess verifyPasswordUser:passwordContext:completion:]_block_invoke.86.cold.1
+ __69-[POAgentCoreProcess verifyPasswordLogin:passwordContext:completion:]_block_invoke.34
+ __69-[POAgentCoreProcess verifyPasswordLogin:passwordContext:completion:]_block_invoke.34.cold.1
+ __69-[POAgentCoreProcess verifyPasswordLogin:passwordContext:completion:]_block_invoke.41
+ __69-[POAgentCoreProcess verifyPasswordLogin:passwordContext:completion:]_block_invoke.41.cold.1
+ __69-[POAgentCoreProcess verifyPasswordLogin:passwordContext:completion:]_block_invoke.45
+ __69-[POAgentCoreProcess verifyPasswordLogin:passwordContext:completion:]_block_invoke.51
+ __69-[POAgentCoreProcess verifyPasswordLogin:passwordContext:completion:]_block_invoke.51.cold.1
+ __72-[POAgentCoreProcess verifyTokenForUserName:passwordContext:completion:]_block_invoke.163
+ __72-[POAgentCoreProcess verifyTokenForUserName:passwordContext:completion:]_block_invoke.163.cold.1
+ __72-[POAgentCoreProcess verifyTokenForUserName:passwordContext:completion:]_block_invoke.169
+ __72-[POAgentCoreProcess verifyTokenForUserName:passwordContext:completion:]_block_invoke.169.cold.1
+ __73-[PODaemonCoreProcess verifyTokenForUserName:passwordContext:completion:]_block_invoke.159
+ __73-[PODaemonCoreProcess verifyTokenForUserName:passwordContext:completion:]_block_invoke.159.cold.1
+ __81-[POAgentCoreProcess bypassLoginPolicyForUserName:volume:contextData:completion:]_block_invoke.178
+ __81-[POAgentCoreProcess bypassLoginPolicyForUserName:volume:contextData:completion:]_block_invoke.178.cold.1
+ __81-[POAgentCoreProcess bypassLoginPolicyForUserName:volume:contextData:completion:]_block_invoke.186
+ __81-[POAgentCoreProcess bypassLoginPolicyForUserName:volume:contextData:completion:]_block_invoke.186.cold.1
+ __81-[POAgentCoreProcess bypassLoginPolicyForUserName:volume:contextData:completion:]_block_invoke.cold.1
+ __86-[POServiceCoreConnection bypassLoginPolicyForUserName:volume:contextData:completion:]_block_invoke.cold.1
+ ___47-[PODaemonCoreConnection useVolume:completion:]_block_invoke
+ ___49-[PODaemonCoreProcess loadKeybagForSystemVolume:]_block_invoke
+ ___52-[PODaemonCoreProcess copyPrebootKeysForVolumeUUID:]_block_invoke
+ ___56-[POAgentCoreProcess insertTokenForUserName:completion:]_block_invoke
+ ___62+[POBaseSystemSupport prebootVolumePathForUUID:shouldUnmount:]_block_invoke
+ ___67-[POLoginUserCore bypassLoginPolicyForUserName:volume:contextData:]_block_invoke
+ ___75-[POAuthPluginCoreProcess bypassLoginPolicyForUserName:volume:contextData:]_block_invoke
+ ___75-[POAuthPluginCoreProcess bypassLoginPolicyForUserName:volume:contextData:]_block_invoke_2
+ ___81-[POAgentCoreProcess bypassLoginPolicyForUserName:volume:contextData:completion:]_block_invoke
+ ___86-[POServiceCoreConnection bypassLoginPolicyForUserName:volume:contextData:completion:]_block_invoke
+ ___block_descriptor_40_e8_32s_e20_v20?0B8"NSError"12l
+ ___block_descriptor_72_e8_32s40s48s56s64r_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56s64r
+ ___destroy_helper_block_e8_32s40s48s56s64r
+ __block_literal_global.110
+ __block_literal_global.119
+ __block_literal_global.13
+ __block_literal_global.223
+ __block_literal_global.309
+ __block_literal_global.313
+ __block_literal_global.340
+ __block_literal_global.35
+ __block_literal_global.35
+ __block_literal_global.92
+ _objc_msgSend$_volumeConfigurationPathForVolumeUUID:
+ _objc_msgSend$apfsVolumeGroupUUID
+ _objc_msgSend$bypassLoginPolicyForUserName:volume:contextData:
+ _objc_msgSend$bypassLoginPolicyForUserName:volume:contextData:completion:
+ _objc_msgSend$container
+ _objc_msgSend$copyPrebootKeysForVolumeUUID:
+ _objc_msgSend$getAPFSVolumeRole
+ _objc_msgSend$initWithUserName:identifierProvider:sharedOnly:volume:
+ _objc_msgSend$initWithVolume:
+ _objc_msgSend$isCredentialSet:
+ _objc_msgSend$lastUpdated
+ _objc_msgSend$loadKeybagForSystemVolume:
+ _objc_msgSend$mountWithOptionsDictionary:error:
+ _objc_msgSend$prebootVolumePathForUUID:shouldUnmount:
+ _objc_msgSend$unmountWithOptions:error:
+ _objc_msgSend$useVolume:completion:
+ _objc_msgSend$verifySecurityEntitlement
+ _objc_msgSend$volumes
- -[PODaemonCoreConnection init]
- -[PODaemonCoreConnection init].cold.1
- -[PODaemonCoreProcess _volumeConfigurationPath]
- -[PODaemonCoreProcess loadKeybagforSystemVolume]
- -[PODaemonCoreProcess loadKeybagforSystemVolume].cold.1
- -[PODaemonCoreProcess loadKeybagforSystemVolume].cold.2
- -[PODaemonCoreProcess loadKeybagforSystemVolume].cold.3
- -[PODaemonCoreProcess loadPrebootKeys].cold.2
- GCC_except_table174
- GCC_except_table28
- GCC_except_table30
- GCC_except_table34
- GCC_except_table38
- GCC_except_table45
- GCC_except_table48
- GCC_except_table51
- GCC_except_table54
- GCC_except_table57
- GCC_except_table60
- GCC_except_table60
- GCC_except_table63
- GCC_except_table63
- GCC_except_table66
- GCC_except_table69
- GCC_except_table72
- GCC_except_table75
- GCC_except_table81
- __103-[POAgentCoreProcess exchangeKeyWithPublicKeyData:userName:passwordContext:responseContext:completion:]_block_invoke.128
- __103-[POAgentCoreProcess exchangeKeyWithPublicKeyData:userName:passwordContext:responseContext:completion:]_block_invoke.128.cold.1
- __103-[POAgentCoreProcess exchangeKeyWithPublicKeyData:userName:passwordContext:responseContext:completion:]_block_invoke.135
- __103-[POAgentCoreProcess exchangeKeyWithPublicKeyData:userName:passwordContext:responseContext:completion:]_block_invoke.143
- __103-[POAgentCoreProcess exchangeKeyWithPublicKeyData:userName:passwordContext:responseContext:completion:]_block_invoke.143.cold.1
- __103-[POAgentCoreProcess exchangeKeyWithPublicKeyData:userName:passwordContext:responseContext:completion:]_block_invoke.149
- __103-[POAgentCoreProcess exchangeKeyWithPublicKeyData:userName:passwordContext:responseContext:completion:]_block_invoke.149.cold.1
- __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.101.cold.1
- __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.107
- __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.107.cold.1
- __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.111
- __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.111.cold.1
- __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.115
- __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.116
- __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.116.cold.1
- __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.120
- __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.120.cold.1
- __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.91
- __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.91.cold.1
- __143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.98
- __38-[PODaemonCoreProcess loadPrebootKeys]_block_invoke.19
- __38-[PODaemonCoreProcess loadPrebootKeys]_block_invoke.19.cold.1
- __38-[PODaemonCoreProcess loadPrebootKeys]_block_invoke.cold.1
- __43-[PODaemonCoreConnection _connectToService]_block_invoke.86
- __43-[PODaemonCoreConnection _connectToService]_block_invoke.86.cold.1
- __44-[POServiceCoreConnection _connectToService]_block_invoke.71
- __44-[POServiceCoreConnection _connectToService]_block_invoke.71.cold.1
- __50-[PODaemonCoreProcess writeData:toPath:saveError:]_block_invoke.42
- __50-[PODaemonCoreProcess writeData:toPath:saveError:]_block_invoke.42.cold.1
- __50-[PODaemonCoreProcess writeData:toPath:saveError:]_block_invoke.48
- __50-[PODaemonCoreProcess writeData:toPath:saveError:]_block_invoke.48.cold.1
- __53-[POAgentCoreProcess getLoginTypeForUser:completion:]_block_invoke.21
- __53-[POAgentCoreProcess getLoginTypeForUser:completion:]_block_invoke.21.cold.1
- __53-[PODaemonCoreProcess _saveUserLoginStateList:error:]_block_invoke.103
- __53-[PODaemonCoreProcess _saveUserLoginStateList:error:]_block_invoke.103.cold.1
- __53-[PODaemonCoreProcess _saveUserLoginStateList:error:]_block_invoke.99
- __53-[PODaemonCoreProcess _saveUserLoginStateList:error:]_block_invoke.99.cold.1
- __56-[PODaemonCoreProcess _userLoginStateListDataWithError:]_block_invoke.76
- __56-[PODaemonCoreProcess _userLoginStateListDataWithError:]_block_invoke.76.cold.1
- __58-[PODaemonCoreProcess _parseUserLoginStateListData:error:]_block_invoke.83
- __58-[PODaemonCoreProcess _parseUserLoginStateListData:error:]_block_invoke.83.cold.1
- __59+[PODaemonCoreProcess createPrebootKey:encryptedKey:error:]_block_invoke.32
- __59+[PODaemonCoreProcess createPrebootKey:encryptedKey:error:]_block_invoke.32.cold.1
- __61-[PODaemonCoreProcess _userConfigurationForIdentifier:error:]_block_invoke.69
- __61-[PODaemonCoreProcess _userConfigurationForIdentifier:error:]_block_invoke.69.cold.1
- __62-[PODaemonCoreProcess saveCachedContextsToDiskWithCompletion:]_block_invoke_2.cold.1
- __63-[PODaemonCoreProcess _saveCachedContextsToDiskWithCompletion:]_block_invoke.140
- __63-[PODaemonCoreProcess _saveCachedContextsToDiskWithCompletion:]_block_invoke.140.cold.1
- __63-[PODaemonCoreProcess _saveCachedContextsToDiskWithCompletion:]_block_invoke.144
- __63-[PODaemonCoreProcess _saveCachedContextsToDiskWithCompletion:]_block_invoke.144.cold.1
- __63-[PODaemonCoreProcess _saveCachedContextsToDiskWithCompletion:]_block_invoke.146
- __63-[PODaemonCoreProcess _saveCachedContextsToDiskWithCompletion:]_block_invoke.146.cold.1
- __68-[POAgentCoreProcess verifyPasswordUser:passwordContext:completion:]_block_invoke.57
- __68-[POAgentCoreProcess verifyPasswordUser:passwordContext:completion:]_block_invoke.57.cold.1
- __68-[POAgentCoreProcess verifyPasswordUser:passwordContext:completion:]_block_invoke.66
- __68-[POAgentCoreProcess verifyPasswordUser:passwordContext:completion:]_block_invoke.66.cold.1
- __68-[POAgentCoreProcess verifyPasswordUser:passwordContext:completion:]_block_invoke.70
- __68-[POAgentCoreProcess verifyPasswordUser:passwordContext:completion:]_block_invoke.74
- __68-[POAgentCoreProcess verifyPasswordUser:passwordContext:completion:]_block_invoke.74.cold.1
- __68-[POAgentCoreProcess verifyPasswordUser:passwordContext:completion:]_block_invoke.83
- __68-[POAgentCoreProcess verifyPasswordUser:passwordContext:completion:]_block_invoke.83.cold.1
- __69-[POAgentCoreProcess verifyPasswordLogin:passwordContext:completion:]_block_invoke.31
- __69-[POAgentCoreProcess verifyPasswordLogin:passwordContext:completion:]_block_invoke.31.cold.1
- __69-[POAgentCoreProcess verifyPasswordLogin:passwordContext:completion:]_block_invoke.38
- __69-[POAgentCoreProcess verifyPasswordLogin:passwordContext:completion:]_block_invoke.38.cold.1
- __69-[POAgentCoreProcess verifyPasswordLogin:passwordContext:completion:]_block_invoke.42
- __69-[POAgentCoreProcess verifyPasswordLogin:passwordContext:completion:]_block_invoke.48
- __69-[POAgentCoreProcess verifyPasswordLogin:passwordContext:completion:]_block_invoke.48.cold.1
- __72-[POAgentCoreProcess verifyTokenForUserName:passwordContext:completion:]_block_invoke.161
- __72-[POAgentCoreProcess verifyTokenForUserName:passwordContext:completion:]_block_invoke.161.cold.1
- __73-[PODaemonCoreProcess verifyTokenForUserName:passwordContext:completion:]_block_invoke.154
- __73-[PODaemonCoreProcess verifyTokenForUserName:passwordContext:completion:]_block_invoke.154.cold.1
- ___38-[PODaemonCoreProcess loadPrebootKeys]_block_invoke
- ___62-[PODaemonCoreProcess saveCachedContextsToDiskWithCompletion:]_block_invoke_2
- ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8l
- __block_literal_global.103
- __block_literal_global.107
- __block_literal_global.221
- __block_literal_global.281
- __block_literal_global.285
- __block_literal_global.322
- __block_literal_global.33
- _objc_msgSend$_volumeConfigurationPath
- _objc_msgSend$loadKeybagforSystemVolume
- _objc_msgSend$mountWithCompletionBlock:
CStrings:
+ "-[POAuthPluginCoreProcess bypassLoginPolicyForUserName:volume:contextData:]"
+ "-[PODaemonCoreConnection initWithVolume:]"
+ "-[PODaemonCoreProcess copyPrebootKeysForVolumeUUID:]"
+ "/%!@(MISSING)/%!@(MISSING)%!@(MISSING)"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
+ "Error mounting preboot volume"
+ "Error mounting system volume"
+ "Error mounting target volume"
+ "Error unmounting target volume"
+ "Failed to validate recovery information"
+ "Recovery code is not set."
+ "com.apple.private.platformsso.security"
+ "failed to update user policy."
- "-[PODaemonCoreConnection init]"
- "-[PODaemonCoreProcess loadPrebootKeys]"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
- "Failed to mount disk"

```
