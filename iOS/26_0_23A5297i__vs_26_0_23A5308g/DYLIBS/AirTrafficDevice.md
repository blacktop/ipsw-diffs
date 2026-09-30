## AirTrafficDevice

> `/System/Library/PrivateFrameworks/AirTrafficDevice.framework/AirTrafficDevice`

```diff

-4025.100.105.0.0
-  __TEXT.__text: 0x154c58
-  __TEXT.__auth_stubs: 0xcb0
-  __TEXT.__objc_methlist: 0x37d8
+4025.100.126.0.0
+  __TEXT.__text: 0xd7940
+  __TEXT.__auth_stubs: 0xca0
+  __TEXT.__objc_methlist: 0x37c0
   __TEXT.__dlopen_cstrs: 0x202
-  __TEXT.__const: 0x15668
-  __TEXT.__gcc_except_tab: 0xbe4
-  __TEXT.__cstring: 0x2af6
-  __TEXT.__oslogstring: 0x72b8
-  __TEXT.__unwind_info: 0x14a8
-  __TEXT.__eh_frame: 0xb8
+  __TEXT.__const: 0x11738
+  __TEXT.__gcc_except_tab: 0xc58
+  __TEXT.__cstring: 0x2a52
+  __TEXT.__oslogstring: 0x7149
+  __TEXT.__unwind_info: 0x1428
+  __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0x8bc
-  __TEXT.__objc_methname: 0xa368
-  __TEXT.__objc_methtype: 0x24ff
-  __TEXT.__objc_stubs: 0x86a0
+  __TEXT.__objc_methname: 0xa275
+  __TEXT.__objc_methtype: 0x24e6
+  __TEXT.__objc_stubs: 0x85e0
   __DATA_CONST.__got: 0x858
   __DATA_CONST.__const: 0x1518
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a08
+  __DATA_CONST.__objc_selrefs: 0x29d8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__auth_got: 0x668
-  __AUTH_CONST.__const: 0xbbc8
-  __AUTH_CONST.__cfstring: 0x2e00
-  __AUTH_CONST.__objc_const: 0x6278
+  __AUTH_CONST.__auth_got: 0x660
+  __AUTH_CONST.__const: 0x99f0
+  __AUTH_CONST.__cfstring: 0x2de0
+  __AUTH_CONST.__objc_const: 0x6258
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __DATA.__objc_ivar: 0x4b4
-  __DATA.__data: 0xf30
-  __DATA.__bss: 0x160
-  __DATA.__common: 0xa28
-  __DATA_DIRTY.__objc_data: 0x11d0
-  __DATA_DIRTY.__bss: 0x58
+  __AUTH.__objc_data: 0xa50
+  __DATA.__objc_ivar: 0x4b0
+  __DATA.__data: 0xee8
+  __DATA.__bss: 0x100
+  __DATA.__common: 0xa24
+  __DATA_DIRTY.__objc_data: 0x780
+  __DATA_DIRTY.__bss: 0xa8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CB6F55C6-ADF6-312A-AD40-8DAD1CAF4FB8
-  Functions: 1637
-  Symbols:   5714
-  CStrings:  3436
+  UUID: 4AF23664-C018-3975-9166-2B080CE1F8D6
+  Functions: 1621
+  Symbols:   5687
+  CStrings:  3418
 
Symbols:
+ -[ATStorePodcastDownloadAssetsOperation keyLoader]
+ GCC_except_table1369
+ GCC_except_table1373
+ GCC_except_table1380
+ _OBJC_IVAR_$_ATStorePodcastDownloadAssetsOperation._keyLoader
+ ___48-[ATStorePodcastDownloadAssetsOperation execute]_block_invoke.11
+ ___48-[ATStorePodcastDownloadAssetsOperation execute]_block_invoke.21
+ ___48-[ATStorePodcastDownloadAssetsOperation execute]_block_invoke.26
+ ___48-[ATStorePodcastDownloadAssetsOperation execute]_block_invoke.30
+ ___48-[ATStorePodcastDownloadAssetsOperation execute]_block_invoke.33
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls40l8s32l8
+ ___block_descriptor_57_e8_32s40s48s_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48s_e44_v24?0"<PFFairPlayKeySession>"8"NSError"16ls32l8s40l8s48l8
+ ___getPFFairPlayAssetClass_block_invoke
+ ___getPFFairPlayKeyLoaderClass_block_invoke
+ _getPFFairPlayAssetClass.softClass
+ _getPFFairPlayKeyLoaderClass.softClass
+ _objc_msgSend$createSessionWithAsset:completion:
+ _objc_msgSend$initWithAdamID:avAsset:
+ _objc_msgSend$keyLoader
+ _objc_msgSend$startKeyRequestWithSession:completion:
- -[ATStorePodcastDownloadAssetsOperation _deleteHLSKey]
- -[ATStorePodcastDownloadAssetsOperation _getContentKeyForAssetWithCompletionHandler:]
- -[ATStorePodcastDownloadAssetsOperation secureDownloadRenewalManager]
- GCC_except_table1362
- GCC_except_table1374
- GCC_except_table1375
- GCC_except_table1387
- _OBJC_IVAR_$_ATStorePodcastDownloadAssetsOperation._hlsAsset
- _OBJC_IVAR_$_ATStorePodcastDownloadAssetsOperation._renewalManager
- ___48-[ATStorePodcastDownloadAssetsOperation execute]_block_invoke.18
- ___48-[ATStorePodcastDownloadAssetsOperation execute]_block_invoke.19
- ___48-[ATStorePodcastDownloadAssetsOperation execute]_block_invoke.22
- ___48-[ATStorePodcastDownloadAssetsOperation execute]_block_invoke.8
- ___85-[ATStorePodcastDownloadAssetsOperation _getContentKeyForAssetWithCompletionHandler:]_block_invoke
- ___85-[ATStorePodcastDownloadAssetsOperation _getContentKeyForAssetWithCompletionHandler:]_block_invoke.51
- ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
- ___block_descriptor_49_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSArray"8ls48l8s32l8s40l8
- ___getIMAVSecureKeyLoaderClass_block_invoke
- ___getMTDBExtensionAccessClass_block_invoke
- ___getPFMediaItemMetadataLoaderClass_block_invoke
- ___getPFSecureDownloadRenewalManagerClass_block_invoke
- _getIMAVSecureKeyLoaderClass.softClass
- _getMTDBExtensionAccessClass
- _getMTDBExtensionAccessClass.softClass
- _getMTStoreIdentifierClass
- _getPFMediaItemMetadataLoaderClass.softClass
- _getPFSecureDownloadRenewalManagerClass.softClass
- _objc_msgSend$_deleteHLSKey
- _objc_msgSend$_getContentKeyForAssetWithCompletionHandler:
- _objc_msgSend$attemptToFix
- _objc_msgSend$initWithRecipient:useCase:account:urlProtocolDelegate:
- _objc_msgSend$isNotEmptyNumber:
- _objc_msgSend$isReady
- _objc_msgSend$keyIdentifiersFromAsset:completion:
- _objc_msgSend$requestSecureDeletionOfEpisodeWithAdamID:
- _objc_msgSend$secureDownloadRenewalManager
- _objc_msgSend$startKeyLoadingProcessWithKeyIdentifier:contentAdamId:isRenewal:completion:
- _objc_release_x10
- _proc_pidpath
- _strnlen
CStrings:
+ "%{public}@ Beginning HLS download"
+ "%{public}@ Created fairplay session. err=%{public}@"
+ "%{public}@ Download complete. cancelled=%x err=%{public}@"
+ "%{public}@ Started key request. err=%{public}@"
+ "@\"PFFairPlayKeyLoader\""
+ "Class getPFFairPlayAssetClass(void)_block_invoke"
+ "Class getPFFairPlayKeyLoaderClass(void)_block_invoke"
+ "PFFairPlayAsset"
+ "PFFairPlayKeyLoader"
+ "_keyLoader"
+ "createSessionWithAsset:completion:"
+ "initWithAdamID:avAsset:"
+ "keyLoader"
+ "startKeyRequestWithSession:completion:"
+ "v24@?0@\"<PFFairPlayKeySession>\"8@\"NSError\"16"
- "%@"
- "%{public}@: Cannot open Podcasts DB. Will not enqueue assets to sync."
- "@\"AVURLAsset\""
- "@\"PFSecureDownloadRenewalManager\""
- "Attempt to load key for episode asset with adam id: %@ failed with err=%{public}@"
- "Attempt to load key for episode asset with adam id: %@ succeeded"
- "Class getIMAVSecureKeyLoaderClass(void)_block_invoke"
- "Class getMTDBExtensionAccessClass(void)_block_invoke"
- "Class getPFMediaItemMetadataLoaderClass(void)_block_invoke"
- "Class getPFSecureDownloadRenewalManagerClass(void)_block_invoke"
- "Content key could not be acquired, returning early due to error: %{public}@"
- "Content key successfully acquired, proceeding with HLS download"
- "Deleting HLS secure key for asset with adam ID %@"
- "Downloading unprotected HLS content with an adamId is not supported"
- "IMAVSecureKeyLoader"
- "MTDBExtensionAccess"
- "PFMediaItemMetadataLoader"
- "PFSecureDownloadRenewalManager"
- "Unexpected number of keyUris found in asset metadata. Continuing with first keyUri"
- "_deleteHLSKey"
- "_getContentKeyForAssetWithCompletionHandler:"
- "_hlsAsset"
- "_renewalManager"
- "attemptToFix"
- "initWithRecipient:useCase:account:urlProtocolDelegate:"
- "isNotEmptyNumber:"
- "isReady"
- "keyIdentifiersFromAsset:completion:"
- "requestSecureDeletionOfEpisodeWithAdamID:"
- "secureDownloadRenewalManager"
- "startKeyLoadingProcessWithKeyIdentifier:contentAdamId:isRenewal:completion:"
- "v16@?0@\"NSArray\"8"

```
