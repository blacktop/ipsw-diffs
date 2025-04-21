## AuthenticationServices

> `/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices`

```diff

-621.2.3.10.3
-  __TEXT.__text: 0x89828
+621.2.4.10.2
+  __TEXT.__text: 0x89a1c
   __TEXT.__auth_stubs: 0x1b20
-  __TEXT.__objc_methlist: 0x6d98
+  __TEXT.__objc_methlist: 0x6dc0
   __TEXT.__const: 0x5094
-  __TEXT.__gcc_except_tab: 0x10e4
-  __TEXT.__cstring: 0x5ed6
+  __TEXT.__gcc_except_tab: 0x1138
+  __TEXT.__cstring: 0x6156
   __TEXT.__oslogstring: 0x2438
   __TEXT.__dlopen_cstrs: 0x2a8
   __TEXT.__ustring: 0x751e

   __TEXT.__swift_as_ret: 0x30
   __TEXT.__swift5_mpenum: 0x48
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0x2b30
+  __TEXT.__unwind_info: 0x2b40
   __TEXT.__eh_frame: 0x1200
-  __TEXT.__objc_classname: 0x1e43
-  __TEXT.__objc_methname: 0x146ae
+  __TEXT.__objc_classname: 0x1e3f
+  __TEXT.__objc_methname: 0x1478f
   __TEXT.__objc_methtype: 0x3cda
-  __TEXT.__objc_stubs: 0xcf20
+  __TEXT.__objc_stubs: 0xcf60
   __DATA_CONST.__got: 0xcb0
-  __DATA_CONST.__const: 0x1a00
+  __DATA_CONST.__const: 0x1a28
   __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4530
+  __DATA_CONST.__objc_selrefs: 0x4548
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x330
   __DATA_CONST.__objc_arraydata: 0x140

   __AUTH_CONST.__auth_ptr: 0x478
   __AUTH_CONST.__const: 0x2f10
   __AUTH_CONST.__cfstring: 0x4280
-  __AUTH_CONST.__objc_const: 0xd5a0
+  __AUTH_CONST.__objc_const: 0xd5c0
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x2a10
   __AUTH.__data: 0x8a8
-  __DATA.__objc_ivar: 0x6d0
+  __DATA.__objc_ivar: 0x6d4
   __DATA.__data: 0x1fe8
   __DATA.__bss: 0x5410
   __DATA.__common: 0x68

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3865
-  Symbols:   9634
-  CStrings:  4251
+  Functions: 3868
+  Symbols:   9645
+  CStrings:  4254
 
Symbols:
+ +[_ASWebsiteNameProvider debug_fetchWebsiteNameForDomain:completionHandler:]
+ -[_ASWebsiteNameProvider _cacheFetchedAndKeychainBackedWebsiteName:forDomain:dateLastRefreshed:]
+ -[_ASWebsiteNameProvider _canRefreshDataForDateLastRefreshed:]
+ -[_ASWebsiteNameProvider _fetchDataForDomainIfNeeded:metadataEntry:]
+ -[_ASWebsiteNameProvider _processMetadataEntryFetchedFromKeychain:forDomain:allowRefreshingDataFromNetwork:]
+ -[_ASWebsiteNameProvider _processMetadataEntryFetchedFromKeychain:forDomain:allowRefreshingDataFromNetwork:].cold.1
+ GCC_except_table16
+ GCC_except_table19
+ GCC_except_table61
+ GCC_except_table64
+ GCC_except_table66
+ GCC_except_table68
+ GCC_except_table70
+ GCC_except_table76
+ GCC_except_table77
+ GCC_except_table78
+ _OBJC_IVAR_$__ASWebsiteNameProvider._cachedDomainToDateLastRefreshed
+ ___33-[_ASWebsiteNameProvider prewarm]_block_invoke.95
+ ___52-[_ASWebsiteNameProvider knownWebsiteNameForDomain:]_block_invoke_5
+ ___68-[_ASWebsiteNameProvider _fetchDataForDomainIfNeeded:metadataEntry:]_block_invoke
+ ___96-[_ASWebsiteNameProvider _cacheFetchedAndKeychainBackedWebsiteName:forDomain:dateLastRefreshed:]_block_invoke
+ ___block_descriptor_64_ea8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.106
+ ___block_literal_global.139
+ ___block_literal_global.141
+ _objc_msgSend$_cacheFetchedAndKeychainBackedWebsiteName:forDomain:dateLastRefreshed:
+ _objc_msgSend$_canRefreshDataForDateLastRefreshed:
+ _objc_msgSend$_fetchDataForDomainIfNeeded:metadataEntry:
+ _objc_msgSend$_processMetadataEntryFetchedFromKeychain:forDomain:allowRefreshingDataFromNetwork:
- -[_ASWebsiteNameProvider _cacheFetchedAndKeychainBackedWebsiteName:forDomain:]
- -[_ASWebsiteNameProvider _processFetchedMetadataEntry:forDomain:]
- -[_ASWebsiteNameProvider _processFetchedMetadataEntry:forDomain:].cold.1
- GCC_except_table15
- GCC_except_table21
- GCC_except_table60
- GCC_except_table62
- GCC_except_table67
- GCC_except_table73
- GCC_except_table74
- GCC_except_table75
- __ZL42getWBSPrivacyProxyAvailabilityManagerClassv
- ___33-[_ASWebsiteNameProvider prewarm]_block_invoke.97
- ___65-[_ASWebsiteNameProvider _processFetchedMetadataEntry:forDomain:]_block_invoke
- ___78-[_ASWebsiteNameProvider _cacheFetchedAndKeychainBackedWebsiteName:forDomain:]_block_invoke
- ___block_literal_global.104
- ___block_literal_global.108
- ___block_literal_global.143
- ___block_literal_global.145
- _objc_msgSend$_cacheFetchedAndKeychainBackedWebsiteName:forDomain:
- _objc_msgSend$_processFetchedMetadataEntry:forDomain:
CStrings:
+ "Your iPad needs to connect to this device in order to save a passkey.\n\nYou should only connect to the other device if you scanned a QR code in order to save a passkey."
+ "Your iPad needs to connect to this device in order to sign in with a passkey.\n\nYou should only connect to the other device if you scanned a QR code in order to sign in with a passkey."
+ "Your iPad needs to connect to this device in order to sign in with or save a passkey.\n\nYou should only connect to the other device if you scanned a QR code in order to sign in with or save a passkey."
+ "Your iPhone needs to connect to this device in order to save a passkey.\n\nYou should only connect to the other device if you scanned a QR code in order to save a passkey."
+ "Your iPhone needs to connect to this device in order to sign in with a passkey.\n\nYou should only connect to the other device if you scanned a QR code in order to sign in with a passkey."
+ "Your iPhone needs to connect to this device in order to sign in with or save a passkey.\n\nYou should only connect to the other device if you scanned a QR code in order to sign in with or save a passkey."
+ "_cacheFetchedAndKeychainBackedWebsiteName:forDomain:dateLastRefreshed:"
+ "_cachedDomainToDateLastRefreshed"
+ "_canRefreshDataForDateLastRefreshed:"
+ "_fetchDataForDomainIfNeeded:metadataEntry:"
+ "_processMetadataEntryFetchedFromKeychain:forDomain:allowRefreshingDataFromNetwork:"
+ "debug_fetchWebsiteNameForDomain:completionHandler:"
- "\x02\x18\x11"
- "Your iPad needs to connect to this device in order to save a passkey."
- "Your iPad needs to connect to this device in order to sign in with a passkey."
- "Your iPad needs to connect to this device in order to sign in with or save a passkey."
- "Your iPhone needs to connect to this device in order to save a passkey."
- "Your iPhone needs to connect to this device in order to sign in with a passkey."
- "Your iPhone needs to connect to this device in order to sign in with or save a passkey."
- "_cacheFetchedAndKeychainBackedWebsiteName:forDomain:"
- "_processFetchedMetadataEntry:forDomain:"

```
