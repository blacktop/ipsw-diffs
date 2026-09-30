## SpotlightResources

> `/System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources`

```diff

-2418.4.8.2.100
-  __TEXT.__text: 0x2b5d0
+2418.4.10.1.0
+  __TEXT.__text: 0x2bb80
   __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__objc_methlist: 0x15e8
+  __TEXT.__objc_methlist: 0x1600
   __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0xe2c
-  __TEXT.__cstring: 0x258c
-  __TEXT.__oslogstring: 0x216f
-  __TEXT.__unwind_info: 0x9c0
-  __TEXT.__objc_classname: 0x207
-  __TEXT.__objc_methname: 0x372f
-  __TEXT.__objc_methtype: 0x64a
-  __TEXT.__objc_stubs: 0x37a0
+  __TEXT.__gcc_except_tab: 0xe48
+  __TEXT.__cstring: 0x25e8
+  __TEXT.__oslogstring: 0x21a3
+  __TEXT.__unwind_info: 0x9b8
+  __TEXT.__objc_classname: 0x208
+  __TEXT.__objc_methname: 0x37ca
+  __TEXT.__objc_methtype: 0x669
+  __TEXT.__objc_stubs: 0x37e0
   __DATA_CONST.__got: 0x240
-  __DATA_CONST.__const: 0xbc8
+  __DATA_CONST.__const: 0xc40
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1070
+  __DATA_CONST.__objc_selrefs: 0x1080
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x990
   __AUTH_CONST.__auth_got: 0x3e8
   __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x49a0
-  __AUTH_CONST.__objc_const: 0x22a0
+  __AUTH_CONST.__cfstring: 0x4a00
+  __AUTH_CONST.__objc_const: 0x2300
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x1a0
+  __DATA.__objc_ivar: 0x1ac
   __DATA.__data: 0x180
   __DATA.__bss: 0x68
   __DATA_DIRTY.__objc_data: 0x6e0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 45E46E6F-0EA8-3007-A3CD-7A4DAB6C8DF7
-  Functions: 792
-  Symbols:   2833
-  CStrings:  2278
+  UUID: 6D3D6C0A-344E-3E3C-AFC6-061411CF85F9
+  Functions: 796
+  Symbols:   2849
+  CStrings:  2293
 
Symbols:
+ -[SRAsset mergeWithAsset:]
+ -[SRDefaultsManager _loadAssets:shouldUpdate:merge:]
+ -[SRDefaultsManager addFetchForLanguage:ota:]
+ -[SRDefaultsManager assetBundleForLocale:client:force:noOTA:]
+ -[SRDefaultsManager didFetchForLanguage:ota:]
+ -[SRDefaultsManager fetchedLanguages:]
+ -[SRDefaultsManager loadAssetsForLanguage:reload:force:noOTA:]
+ -[SRDefaultsManager loadDefaultsForLocale:reload:force:noOTA:]
+ -[SRDefaultsManager loadInternalAssetsForLanguage:assetTypes:]
+ -[SRDefaultsManager removeFetchForLanguage:ota:]
+ -[SRDefaultsManager updateFetchedLanguages:ota:]
+ GCC_except_table105
+ GCC_except_table113
+ GCC_except_table118
+ GCC_except_table121
+ GCC_except_table126
+ GCC_except_table131
+ GCC_except_table132
+ GCC_except_table26
+ GCC_except_table62
+ GCC_except_table74
+ GCC_except_table78
+ GCC_except_table83
+ GCC_except_table84
+ GCC_except_table90
+ _OBJC_IVAR_$_SRDefaultsManager._fetchedLanguagesOTA
+ _OBJC_IVAR_$_SRDefaultsManager._fetchedLanguagesSystem
+ _OBJC_IVAR_$_SRDefaultsManager._fetchedRootOTA
+ _OBJC_IVAR_$_SRDefaultsManager._fetchedRootSystem
+ _OBJC_IVAR_$_SRResources._noOTA
+ ___26-[SRAsset mergeWithAsset:]_block_invoke
+ ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke.250
+ ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke.250.cold.1
+ ___38-[SRDefaultsManager fetchedLanguages:]_block_invoke
+ ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.243
+ ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.243.cold.1
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.1
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.10
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.11
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.12
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.13
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.2
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.3
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.4
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.5
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.6
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.7
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.8
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.9
+ ___45-[SRDefaultsManager addFetchForLanguage:ota:]_block_invoke
+ ___45-[SRDefaultsManager didFetchForLanguage:ota:]_block_invoke
+ ___48-[SRDefaultsManager removeFetchForLanguage:ota:]_block_invoke
+ ___48-[SRDefaultsManager updateFetchedLanguages:ota:]_block_invoke
+ ___52-[SRDefaultsManager _loadAssets:shouldUpdate:merge:]_block_invoke
+ ___61-[SRDefaultsManager assetBundleForLocale:client:force:noOTA:]_block_invoke
+ ___62-[SRDefaultsManager loadInternalAssetsForLanguage:assetTypes:]_block_invoke
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.634
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.636
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.636.cold.1
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_2.635
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_2.635.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.562.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.562.cold.3
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.565
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.565.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.565.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.572.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.572.cold.3
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.572.cold.4
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.574
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.574.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.575
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.575.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.575.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.576
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.577
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.577.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.578
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.578.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.579
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.579.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.579.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke_2.571
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke_2.571.cold.1
+ ___block_descriptor_42_e8_32s_e24_v32?0"SRAsset"8Q16^B24ls32l8
+ ___block_descriptor_48_e8_32s40s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8
+ ___block_descriptor_49_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_57_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_literal_global.444
+ ___block_literal_global.491
+ ___block_literal_global.511
+ _objc_msgSend$_loadAssets:shouldUpdate:merge:
+ _objc_msgSend$addFetchForLanguage:ota:
+ _objc_msgSend$assetBundleForLocale:client:force:noOTA:
+ _objc_msgSend$didFetchForLanguage:ota:
+ _objc_msgSend$fetchedLanguages:
+ _objc_msgSend$loadAssetsForLanguage:reload:force:noOTA:
+ _objc_msgSend$loadDefaultsForLocale:reload:force:noOTA:
+ _objc_msgSend$loadInternalAssetsForLanguage:assetTypes:
+ _objc_msgSend$mergeWithAsset:
+ _objc_msgSend$removeFetchForLanguage:ota:
+ _objc_msgSend$updateFetchedLanguages:ota:
- -[SRDefaultsManager _loadAssets:shouldUpdate:]
- -[SRDefaultsManager addFetchForLanguage:]
- -[SRDefaultsManager assetBundleForLocale:client:force:]
- -[SRDefaultsManager didFetchForLanguage:]
- -[SRDefaultsManager fetchedLanguages]
- -[SRDefaultsManager loadAssetsForLanguage:reload:force:]
- -[SRDefaultsManager loadDefaultsForLocale:reload:force:]
- -[SRDefaultsManager removeFetchForLanguage:]
- -[SRDefaultsManager updateFetchedLanguages:]
- GCC_except_table107
- GCC_except_table116
- GCC_except_table119
- GCC_except_table122
- GCC_except_table127
- GCC_except_table128
- GCC_except_table24
- GCC_except_table60
- GCC_except_table72
- GCC_except_table76
- GCC_except_table81
- GCC_except_table82
- GCC_except_table88
- GCC_except_table97
- _OBJC_IVAR_$_SRDefaultsManager._fetchedLanguages
- _OBJC_IVAR_$_SRDefaultsManager._fetchedRoot
- ___37-[SRDefaultsManager fetchedLanguages]_block_invoke
- ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke.247
- ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke.247.cold.1
- ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.240
- ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.240.cold.1
- ___41-[SRDefaultsManager addFetchForLanguage:]_block_invoke
- ___41-[SRDefaultsManager didFetchForLanguage:]_block_invoke
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.1
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.10
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.11
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.12
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.13
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.2
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.3
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.4
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.5
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.6
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.7
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.8
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.9
- ___44-[SRDefaultsManager removeFetchForLanguage:]_block_invoke
- ___44-[SRDefaultsManager updateFetchedLanguages:]_block_invoke
- ___46-[SRDefaultsManager _loadAssets:shouldUpdate:]_block_invoke
- ___55-[SRDefaultsManager assetBundleForLocale:client:force:]_block_invoke
- ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.628
- ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.630
- ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.630.cold.1
- ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_2.629
- ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_2.629.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.556
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.556.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.556.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.556.cold.3
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.557
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.559
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.559.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.559.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.561
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.561.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.563.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.563.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.564
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.566
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.566.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.566.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.566.cold.3
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.566.cold.4
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.571
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.571.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.573.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke_2.565
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke_2.565.cold.1
- ___block_descriptor_41_e8_32s_e24_v32?0"SRAsset"8Q16^B24ls32l8
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
- ___block_literal_global.440
- ___block_literal_global.487
- ___block_literal_global.507
- _objc_msgSend$_loadAssets:shouldUpdate:
- _objc_msgSend$addFetchForLanguage:
- _objc_msgSend$assetBundleForLocale:client:force:
- _objc_msgSend$didFetchForLanguage:
- _objc_msgSend$fetchedLanguages
- _objc_msgSend$loadAssetsForLanguage:reload:force:
- _objc_msgSend$loadDefaultsForLocale:reload:force:
- _objc_msgSend$removeFetchForLanguage:
- _objc_msgSend$updateFetchedLanguages:
CStrings:
+ "%@/RequiredAssets_%@.bundle"
+ "(fetchedLanguages) add fetch for language(%d): %s"
+ "(fetchedLanguages) remove fetch for language(%d): %s"
+ "(fetchedLanguages) update fetched languages (%d): %@ --> %@"
+ "/AppleInternal/Spotlight/Assets"
+ "@20@0:8B16"
+ "@36@0:8@16B24B28B32"
+ "@40@0:8@16@24B32B36"
+ "B28@0:8@16B24"
+ "Loading internal assets from path <%s>"
+ "NoOTA"
+ "_fetchedLanguagesOTA"
+ "_fetchedLanguagesSystem"
+ "_fetchedRootOTA"
+ "_fetchedRootSystem"
+ "_loadAssets:shouldUpdate:merge:"
+ "_noOTA"
+ "addFetchForLanguage:ota:"
+ "assetBundleForLocale:client:force:noOTA:"
+ "didFetchForLanguage:ota:"
+ "fetchedLanguages:"
+ "loadAssetsForLanguage:reload:force:noOTA:"
+ "loadDefaultsForLocale:reload:force:noOTA:"
+ "loadInternalAssetsForLanguage:assetTypes:"
+ "mergeWithAsset:"
+ "removeFetchForLanguage:ota:"
+ "updateFetchedLanguages:ota:"
+ "v32@?0@\"NSString\"8Q16^B24"
- "(fetchedLanguages) add fetch for language: %s"
- "(fetchedLanguages) remove fetch for language: %s"
- "(fetchedLanguages) update fetched languages: %@ --> %@"
- "@32@0:8@16B24B28"
- "@36@0:8@16@24B32"
- "_fetchedLanguages"
- "_fetchedRoot"
- "_loadAssets:shouldUpdate:"
- "addFetchForLanguage:"
- "assetBundleForLocale:client:force:"
- "didFetchForLanguage:"
- "fetchedLanguages"
- "loadAssetsForLanguage:reload:force:"
- "loadDefaultsForLocale:reload:force:"
- "removeFetchForLanguage:"
- "updateFetchedLanguages:"

```
