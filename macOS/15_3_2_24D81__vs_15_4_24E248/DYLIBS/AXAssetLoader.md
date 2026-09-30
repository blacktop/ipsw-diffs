## AXAssetLoader

> `/System/Library/PrivateFrameworks/AXAssetLoader.framework/Versions/A/AXAssetLoader`

```diff

-3148.7.15.0.0
+3148.15.11.1.0
   __TEXT.__text: 0x12e98
   __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__objc_methlist: 0xe48
+  __TEXT.__objc_methlist: 0x1054
   __TEXT.__const: 0xb8
   __TEXT.__cstring: 0xcc7
   __TEXT.__oslogstring: 0xd7a
   __TEXT.__gcc_except_tab: 0x648
   __TEXT.__dlopen_cstrs: 0xfc
-  __TEXT.__unwind_info: 0x5f8
+  __TEXT.__unwind_info: 0x610
   __TEXT.__objc_classname: 0x276
   __TEXT.__objc_methname: 0x2e08
   __TEXT.__objc_methtype: 0x5b5

   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xad0
+  __DATA_CONST.__objc_selrefs: 0xb58
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __AUTH_CONST.__auth_got: 0x1f0
   __AUTH_CONST.__const: 0x930
   __AUTH_CONST.__cfstring: 0xd00
-  __AUTH_CONST.__objc_const: 0x1c20
+  __AUTH_CONST.__objc_const: 0x1868
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0x5f0
   __DATA.__objc_ivar: 0xd4

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 755FED42-0420-3CD6-A665-863CE83489B9
-  Functions: 477
-  Symbols:   1190
+  UUID: 01D253B3-DC3C-3162-8EAB-2C3113983C69
+  Functions: 481
+  Symbols:   1194
   CStrings:  879
 
Symbols:
+ +[AXAssetMetadataStore store].cold.1
+ AXAssetBundle.cold.1
+ __66-[AXAssetController _updateCatalogWithOverrideTimeout:completion:]_block_invoke.349.cold.1
Functions:
~ -[AXAssetUpdateMonitor _workerQueue_refreshAssetsAfterDelay:canRefreshCatalog:] : 344 -> 340
~ -[AXAssetUpdateMonitor assetController:didFinishRefreshingAssets:wasSuccessful:error:] : 616 -> 612
~ +[AXAssetMetadataStore store] : 84 -> 68
~ -[AXAssetMetadataStore heldAssertionsForAssetType:] : 240 -> 236
~ ___53-[AXAssetMetadataStore setValue:forKey:forAssetType:]_block_invoke : 184 -> 196
~ ___126+[AXAsset(ImageCaptionModel) newsestCompatibleImageCaptionModelAssetFromAssets:withStage:language:isInstalled:isDownloadable:]_block_invoke : 296 -> 304
~ -[AXAssetPolicy isAssetContentVersion:greatherThanInstalledAssets:] : 328 -> 324
~ -[AXAssetPolicy _isAssetSupportedBasedOnMinMaxFormatVersion:] : 264 -> 260
~ -[AXAssetPolicy(MobileAsset) newAssetQuery] : 296 -> 292
~ -[AXAssetPolicy(MobileAsset) downloadOptionsForOperation:userInitiated:] : 332 -> 328
~ -[AXAsset resetPropertiesFromMAAsset:] : 1096 -> 1092
~ -[AXAsset downloadSize] : 320 -> 316
~ -[AXAsset unarchivedFileSize] : 320 -> 316
~ _AXAssetBundle : 84 -> 68
~ -[AXAssetsService xpcConnection] : 212 -> 208
~ ___32-[AXAssetsService xpcConnection]_block_invoke : 444 -> 432
~ -[AXAssetController _initWithAssetPolicy:qosClass:shouldRefreshForAssetInstallNotifications:] : 832 -> 824
~ -[AXAssetController _registerForNotifications] : 536 -> 532
~ ___122-[AXAssetController refreshAssetsByForceUpdatingCatalog:updatingCatalogIfNeeded:catalogRefreshOverrideTimeout:completion:]_block_invoke : 232 -> 228
~ _MAStringForMADownloadResultSoft : 288 -> 284
~ ___76-[AXAssetController refreshAssetsWithAttributesSynchronously:installedOnly:]_block_invoke : 480 -> 484
~ -[AXAssetController downloadAssets:successStartBlock:completionBlock:] : 1164 -> 1156
~ -[AXAssetController setUserInitiated:] : 160 -> 164
~ -[AXAssetController _replaceCachedAssetsWithAssets:error:completion:] : 1148 -> 1140
~ -[AXAssetController _queue_refreshAssets:completion:] : 1536 -> 1532
~ -[AXAssetController _updateCatalogWithOverrideTimeout:completion:] : 936 -> 928
~ __66-[AXAssetController _updateCatalogWithOverrideTimeout:completion:]_block_invoke.349 : 620 -> 500
~ -[AXAssetController _queue_downloadAssets:successStartBlock:completionBlock:] : 1748 -> 1716
~ ___77-[AXAssetController _queue_downloadAssets:successStartBlock:completionBlock:]_block_invoke : 168 -> 164
~ -[AXAssetController _queue_updateDownloadPriorityIfNecessary] : 856 -> 852
~ -[AXAssetController setProductionServerURL] : 1424 -> 1416
+ _OUTLINED_FUNCTION_1
+ +[AXAssetMetadataStore store].cold.1
~ -[AXAsset copyLocally].cold.1 : 160 -> 104
~ -[AXAsset copyLocally].cold.4 : 104 -> 160
+ AXAssetBundle.cold.1
~ -[AXAssetController _initWithAssetPolicy:qosClass:shouldRefreshForAssetInstallNotifications:].cold.1 : 68 -> 176
~ -[AXAssetController _initWithAssetPolicy:qosClass:shouldRefreshForAssetInstallNotifications:].cold.2 : 176 -> 68
~ __122-[AXAssetController refreshAssetsByForceUpdatingCatalog:updatingCatalogIfNeeded:catalogRefreshOverrideTimeout:completion:]_block_invoke_2.cold.1 : 204 -> 188
~ -[AXAssetController _queue_refreshAssets:completion:].cold.1 : 124 -> 120
~ -[AXAssetController _queue_refreshAssets:completion:].cold.2 : 120 -> 124
+ __66-[AXAssetController _updateCatalogWithOverrideTimeout:completion:]_block_invoke.349.cold.1

```
