## SpotlightResources

> `/System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources`

```diff

-2400.8.1.0.0
-  __TEXT.__text: 0x28e80
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_methlist: 0x1570
-  __TEXT.__const: 0x100
-  __TEXT.__gcc_except_tab: 0xee4
-  __TEXT.__cstring: 0x251c
-  __TEXT.__oslogstring: 0x1f2d
+2400.11.100.0.0
+  __TEXT.__text: 0x29778
+  __TEXT.__auth_stubs: 0x740
+  __TEXT.__objc_methlist: 0x1578
+  __TEXT.__const: 0x108
+  __TEXT.__gcc_except_tab: 0xf58
+  __TEXT.__cstring: 0x2531
+  __TEXT.__oslogstring: 0x2123
   __TEXT.__unwind_info: 0x8f0
   __TEXT.__objc_classname: 0x207
-  __TEXT.__objc_methname: 0x35f4
+  __TEXT.__objc_methname: 0x3632
   __TEXT.__objc_methtype: 0x64a
-  __TEXT.__objc_stubs: 0x36e0
+  __TEXT.__objc_stubs: 0x3720
   __DATA_CONST.__got: 0x240
-  __DATA_CONST.__const: 0xb50
+  __DATA_CONST.__const: 0xb78
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1018
+  __DATA_CONST.__objc_selrefs: 0x1028
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x990
-  __AUTH_CONST.__auth_got: 0x3a8
+  __AUTH_CONST.__auth_got: 0x3b0
   __AUTH_CONST.__const: 0x4a0
   __AUTH_CONST.__cfstring: 0x4940
   __AUTH_CONST.__objc_const: 0x2280

   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x140
+  __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x19c
   __DATA.__data: 0x180
-  __DATA.__bss: 0x90
-  __DATA_DIRTY.__objc_data: 0x690
+  __DATA.__bss: 0x88
+  __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__data: 0x258
-  __DATA_DIRTY.__bss: 0x2a0
+  __DATA_DIRTY.__bss: 0x2b8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 427F0961-237F-3A7E-B1FF-EA932812DDED
-  Functions: 768
-  Symbols:   2756
-  CStrings:  2243
+  UUID: A20960B8-4585-37CD-B7A6-BC04132A0403
+  Functions: 774
+  Symbols:   2774
+  CStrings:  2259
 
Symbols:
+ -[SRDefaultsManager requestCatalogUpdate]
+ -[SRDefaultsManager requestCatalogUpdate].cold.1
+ -[SRDefaultsManager requestCatalogUpdate].cold.2
+ -[SRDefaultsManager requestCatalogUpdate].cold.3
+ -[SRDefaultsManager requestCatalogUpdate].cold.4
+ GCC_except_table100
+ GCC_except_table108
+ GCC_except_table113
+ GCC_except_table116
+ GCC_except_table121
+ GCC_except_table126
+ GCC_except_table127
+ GCC_except_table71
+ GCC_except_table75
+ GCC_except_table80
+ GCC_except_table81
+ GCC_except_table87
+ _CFAbsoluteTimeGetCurrent
+ _SRAreAssetsAvailableForLocale.availableLangs
+ ___41-[SRDefaultsManager requestCatalogUpdate]_block_invoke
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.572
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.572.cold.1
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_2.571
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_2.571.cold.1
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_3.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.494
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.494.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.494.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.494.cold.3
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.497.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.500.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.501
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.501.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.501.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.504.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.504.cold.3
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.504.cold.4
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.506.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.507.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.510
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.510.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.511
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.511.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.511.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke_2.503
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke_2.503.cold.1
+ ___block_descriptor_40_e8_32s_e20_v24?0q8"NSError"16ls32l8
+ ___block_descriptor_97_e8_32s40s48s56s64s72s80bs88w_e5_v8?0ls32l8w88l8s40l8s48l8s56l8s64l8s72l8s80l8
+ _objc_msgSend$fetchAssetUpdateStatusForQuery:callback:
+ _objc_msgSend$requestCatalogUpdate
+ _requestCatalogUpdate.lastUpdate
- GCC_except_table102
- GCC_except_table111
- GCC_except_table114
- GCC_except_table117
- GCC_except_table122
- GCC_except_table123
- GCC_except_table69
- GCC_except_table73
- GCC_except_table78
- GCC_except_table79
- GCC_except_table85
- GCC_except_table94
- ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.568
- ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.570.cold.1
- ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_2.569
- ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_2.569.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.492
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.492.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.492.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.492.cold.3
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.493
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.495.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.495.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.498
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.498.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.499.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.502.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.502.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.502.cold.3
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.502.cold.4
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.503
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.503.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.505.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.508.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.509.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke_2.501
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke_2.501.cold.1
- ___block_descriptor_89_e8_32s40s48s56s64s72bs80w_e5_v8?0ls32l8w80l8s40l8s48l8s56l8s64l8s72l8
- _deliveryTypeString.cold.1
CStrings:
+ "%@ is not supported"
+ "Assets are available for %@"
+ "Assets are available, requesting downloads"
+ "Assets are unavailable for %@"
+ "Assets for %@ are available for the first time, triggering re-load"
+ "Error: %@ when refreshing assets for %@"
+ "Failed to create asset query"
+ "Failed to get asset type com.apple.MobileAsset.SpotlightResources"
+ "Failed to get current asset types"
+ "Skipping OTA asset loading"
+ "Skipping OTA asset loading."
+ "fetchAssetUpdateStatusForQuery:callback:"
+ "lastUpdate = %lf, now = %lf"
+ "loadOTA[%llu] client 4 skipping (%d, %d, %d, %d)"
+ "loadOTA[%llu] server 4 skipping (%d, %d, %d, %d)"
+ "requestCatalogUpdate"
+ "v24@?0q8@\"NSError\"16"
- "Unsupported asset delivery type %ld"

```
