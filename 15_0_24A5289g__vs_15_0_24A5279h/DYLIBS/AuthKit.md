## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit`

```diff

-488.2.0.0.0
-  __TEXT.__text: 0x1929a4
+486.0.0.0.0
+  __TEXT.__text: 0x1930d0
   __TEXT.__auth_stubs: 0xbb0
-  __TEXT.__objc_methlist: 0xa910
+  __TEXT.__objc_methlist: 0xa8c0
   __TEXT.__const: 0x44c21
-  __TEXT.__cstring: 0xc5c8
-  __TEXT.__oslogstring: 0xf784
-  __TEXT.__gcc_except_tab: 0x50e4
+  __TEXT.__cstring: 0xc6b0
+  __TEXT.__oslogstring: 0xf682
+  __TEXT.__gcc_except_tab: 0x544c
   __TEXT.__ustring: 0x1b8
   __TEXT.__dlopen_cstrs: 0xb4
-  __TEXT.__unwind_info: 0x37b8
+  __TEXT.__unwind_info: 0x3848
   __TEXT.__eh_frame: 0x88
   __TEXT.__objc_classname: 0x1710
-  __TEXT.__objc_methname: 0x1d23d
-  __TEXT.__objc_methtype: 0x3c37
-  __TEXT.__objc_stubs: 0xc580
-  __DATA_CONST.__got: 0x7c0
-  __DATA_CONST.__const: 0x3a48
+  __TEXT.__objc_methname: 0x1d268
+  __TEXT.__objc_methtype: 0x3c45
+  __TEXT.__objc_stubs: 0xc560
+  __DATA_CONST.__got: 0x7c8
+  __DATA_CONST.__const: 0x3a58
   __DATA_CONST.__objc_classlist: 0x4f0
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5eb0
+  __DATA_CONST.__objc_selrefs: 0x5ea8
   __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x338
-  __DATA_CONST.__objc_arraydata: 0x130
+  __DATA_CONST.__objc_arraydata: 0x140
   __AUTH_CONST.__auth_got: 0x5e8
   __AUTH_CONST.__auth_ptr: 0x20
   __AUTH_CONST.__const: 0xc9f0
-  __AUTH_CONST.__cfstring: 0xd160
+  __AUTH_CONST.__cfstring: 0xd140
   __AUTH_CONST.__objc_const: 0x21708
-  __AUTH_CONST.__objc_intobj: 0x198
+  __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x3160
   __DATA.__objc_ivar: 0xe04
   __DATA.__data: 0x1668
-  __DATA.__bss: 0x7d0
+  __DATA.__bss: 0x7e8
   __DATA.__common: 0xa10
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/MultiverseSupport.framework/Versions/A/MultiverseSupport
   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/Versions/A/RemoteServiceDiscovery
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
-  - /System/Library/PrivateFrameworks/URLFormatting.framework/Versions/A/URLFormatting
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5517
-  Symbols:   12772
-  CStrings:  1973
+  Functions: 5514
+  Symbols:   12793
+  CStrings:  1977
 
Symbols:
+ -[AKAccountManager _iCloudAccounts].cold.1
+ -[AKAccountManager allAuthKitAccounts].cold.1
+ -[AKAccountManager appleIDAccountWithAltDSID:].cold.1
+ -[AKAccountManager appleIDAccountWithAppleID:].cold.1
+ -[AKAccountManager authKitAccountForActiveStoreAccount]
+ -[AKAccountManager authKitAccountForActiveStoreAccount].cold.1
+ -[AKAccountManager authKitAccountType].cold.1
+ -[AKAccountManager authKitAccountWithAltDSID:].cold.1
+ -[AKAccountManager authKitAccountWithAppleID:].cold.1
+ -[AKAccountManager authKitAccountWithDSID:].cold.1
+ -[AKAccountManager mostRecentlyUsedAuthKitAccount].cold.1
+ -[AKAccountManager preferredAccountUsingStoreService]
+ -[AKAccountManager saveAccount:error:].cold.1
+ -[AKAccountManager saveAccount:error:].cold.2
+ -[AKAccountStore isAccountDeamonConnectionError:]
+ -[AKMediaServicesController activeStoreAccount]
+ -[AKMediaServicesController activeStoreAccount].cold.1
+ -[AKMediaServicesController isAccount:activeForMediaType:]
+ AppleMediaServicesLibraryCore.frameworkLibrary
+ GCC_except_table112
+ GCC_except_table113
+ GCC_except_table123
+ GCC_except_table133
+ GCC_except_table138
+ GCC_except_table139
+ GCC_except_table141
+ GCC_except_table142
+ GCC_except_table143
+ GCC_except_table146
+ GCC_except_table160
+ GCC_except_table161
+ GCC_except_table166
+ GCC_except_table173
+ GCC_except_table191
+ GCC_except_table194
+ GCC_except_table196
+ GCC_except_table198
+ GCC_except_table200
+ GCC_except_table201
+ GCC_except_table202
+ GCC_except_table203
+ GCC_except_table205
+ GCC_except_table206
+ GCC_except_table210
+ GCC_except_table215
+ GCC_except_table217
+ GCC_except_table237
+ GCC_except_table238
+ GCC_except_table257
+ GCC_except_table270
+ GCC_except_table271
+ GCC_except_table272
+ GCC_except_table273
+ GCC_except_table274
+ GCC_except_table275
+ GCC_except_table303
+ GCC_except_table304
+ GCC_except_table332
+ GCC_except_table77
+ GCC_except_table83
+ GCC_except_table92
+ _AppleMediaServicesLibrary
+ _AppleMediaServicesLibraryCore
+ __44-[AKURLSession _unsafe_retryTaskIfPossible:]_block_invoke.103
+ __64-[AKMediaServicesController _appMetadataForBundleID:completion:]_block_invoke.55
+ __64-[AKMediaServicesController _appMetadataForBundleID:completion:]_block_invoke_2.56
+ __64-[AKMediaServicesController _appMetadataForBundleID:completion:]_block_invoke_2.56.cold.1
+ __64-[AKMediaServicesController _appMetadataForBundleID:completion:]_block_invoke_2.56.cold.2
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.39
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.41
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.41.cold.1
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.41.cold.10
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.41.cold.2
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.41.cold.3
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.41.cold.4
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.41.cold.5
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.41.cold.6
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.41.cold.7
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.41.cold.8
+ __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.41.cold.9
+ __64-[AKMediaServicesController appMetadataForBundleIDs:completion:]_block_invoke.54
+ ___38-[AKAccountManager saveAccount:error:]_block_invoke
+ ___AppleMediaServicesLibraryCore_block_invoke
+ ___block_descriptor_128_e8_32s40s48s56s64r72r80r88r96r104r112r_e5_v8?0l
+ ___getAMSAccountMediaTypeAppStoreSymbolLoc_block_invoke
+ ___getAMSAccountMediaTypeiTunesSymbolLoc_block_invoke
+ _getAMSAccountMediaTypeAppStore
+ _getAMSAccountMediaTypeAppStoreSymbolLoc
+ _getAMSAccountMediaTypeiTunes
+ _getAMSAccountMediaTypeiTunesSymbolLoc
+ _objc_msgSend$accountsWithAccountType:
+ _objc_msgSend$activeStoreAccount
+ _objc_msgSend$ams_activeiTunesAccount
+ _objc_msgSend$ams_isActiveForMediaType:
+ _objc_msgSend$ams_sharedAccountStoreForMediaType:
+ _objc_msgSend$authKitAccountForActiveStoreAccount
+ _objc_msgSend$isAccountDeamonConnectionError:
+ getAMSAccountMediaTypeAppStore.cold.1
+ getAMSAccountMediaTypeAppStoreSymbolLoc.ptr
+ getAMSAccountMediaTypeiTunes.cold.1
+ getAMSAccountMediaTypeiTunesSymbolLoc.ptr
- -[AKAccountManager _fetchAllAccountsWithType:error:]
- -[AKAccountManager _fetchAllAccountsWithType:error:].cold.1
- -[AKAccountManager _fetchAllAccountsWithType:error:].cold.2
- -[AKAccountManager _saveAccount:error:]
- -[AKAccountManager _saveAccount:error:].cold.1
- -[AKAccountManager _saveAccount:error:].cold.2
- -[AKAccountManager allAuthKitAccountsWithError:]
- -[AKAccountManager authKitAccountTypeWithError:]
- -[AKAccountManager authKitAccountTypeWithError:].cold.1
- -[AKAccountManager authKitAccountWithAltDSID:error:]
- -[AKAccountManager authKitAccountWithAppleID:error:]
- -[AKAccountStore isAccountDaemonConnectionError:]
- -[AKAuthorizationCredential setAuthorizationCode:]
- -[AKAuthorizationCredential setAuthorizedScopes:]
- -[AKAuthorizationCredential setIdentityToken:]
- -[AKAuthorizationCredential setState:]
- -[AKAuthorizationCredential setUserInformation:]
- -[AKCommandLineUtilities errorFromServerResponseBody:].cold.1
- -[AKCommandLineUtilities errorFromServerResponseBody:].cold.2
- -[AKCommandLineUtilities errorFromServerResponseBody:].cold.3
- -[AKTokenManager tokenWithIdentifier:altDSID:forAccount:shouldSync:error:].cold.4
- GCC_except_table120
- GCC_except_table135
- GCC_except_table147
- GCC_except_table149
- GCC_except_table152
- GCC_except_table157
- GCC_except_table170
- GCC_except_table174
- GCC_except_table175
- GCC_except_table176
- GCC_except_table177
- GCC_except_table178
- GCC_except_table179
- GCC_except_table182
- GCC_except_table183
- GCC_except_table184
- GCC_except_table186
- GCC_except_table189
- GCC_except_table190
- GCC_except_table231
- GCC_except_table232
- GCC_except_table248
- GCC_except_table251
- GCC_except_table259
- GCC_except_table261
- GCC_except_table262
- GCC_except_table263
- GCC_except_table264
- GCC_except_table282
- GCC_except_table299
- GCC_except_table300
- GCC_except_table305
- GCC_except_table306
- GCC_except_table307
- GCC_except_table308
- GCC_except_table336
- GCC_except_table90
- GCC_except_table95
- _AKMDMInfoRequiredHeaderKey
- __44-[AKURLSession _unsafe_retryTaskIfPossible:]_block_invoke.99
- __64-[AKMediaServicesController _appMetadataForBundleID:completion:]_block_invoke.49
- __64-[AKMediaServicesController _appMetadataForBundleID:completion:]_block_invoke_2.50
- __64-[AKMediaServicesController _appMetadataForBundleID:completion:]_block_invoke_2.50.cold.1
- __64-[AKMediaServicesController _appMetadataForBundleID:completion:]_block_invoke_2.50.cold.2
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.33
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.35
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.35.cold.1
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.35.cold.10
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.35.cold.2
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.35.cold.3
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.35.cold.4
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.35.cold.5
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.35.cold.6
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.35.cold.7
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.35.cold.8
- __64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.35.cold.9
- __64-[AKMediaServicesController appMetadataForBundleIDs:completion:]_block_invoke.48
- __74-[AKTokenManager tokenWithIdentifier:altDSID:forAccount:shouldSync:error:]_block_invoke.cold.9
- ___39-[AKAccountManager _saveAccount:error:]_block_invoke
- ___block_descriptor_129_e8_32s40s48s56s64r72r80r88r96r104r112r_e5_v8?0l
- _objc_msgSend$_fetchAllAccountsWithType:error:
- _objc_msgSend$_saveAccount:error:
- _objc_msgSend$allAuthKitAccountsWithError:
- _objc_msgSend$authKitAccountTypeWithError:
- _objc_msgSend$authKitAccountWithAltDSID:error:
- _objc_msgSend$authKitAccountWithAppleID:error:
- _objc_msgSend$fetchURLBagForAltDSID:fromCache:completion:
- _objc_msgSend$isAccountDaemonConnectionError:
CStrings:
+ "/AppleInternal/Library/Frameworks/AppleMediaServices.framework/AppleMediaServices"
+ "/System/Library/Frameworks/AppleMediaServices.framework/AppleMediaServices"
+ "/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices"
+ "<%!@(MISSING): %!p(MISSING)> Auth Request %!@(MISSING) \nPassword Request: %!@(MISSING) \nProxied Bundle: %!@(MISSING)\nProxied Team: %!@(MISSING) \nSession ID: %!@(MISSING)"
+ "AMSAccountMediaTypeAppStore"
+ "AMSAccountMediaTypeiTunes"
- "<%!@(MISSING): %!p(MISSING)> \nAuthorization Request %!@(MISSING) \nPassword Request: %!@(MISSING) \nProxied App Name: %!@(MISSING)\nProxied BundleID: %!@(MISSING)\nProxied Team: %!@(MISSING) \nSession ID: %!@(MISSING)"
- "X-Apple-I-MDM-Info-Required"

```
