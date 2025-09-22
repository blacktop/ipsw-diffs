## SpotlightResources

> `/System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources`

```diff

-2393.100.0.0.0
-  __TEXT.__text: 0x281ec
-  __TEXT.__auth_stubs: 0x740
-  __TEXT.__objc_methlist: 0x1530
-  __TEXT.__const: 0x108
-  __TEXT.__gcc_except_tab: 0xe4c
-  __TEXT.__cstring: 0x23a5
-  __TEXT.__oslogstring: 0x1e6f
-  __TEXT.__unwind_info: 0x8c8
+2400.8.1.0.0
+  __TEXT.__text: 0x28e80
+  __TEXT.__auth_stubs: 0x730
+  __TEXT.__objc_methlist: 0x1570
+  __TEXT.__const: 0x100
+  __TEXT.__gcc_except_tab: 0xee4
+  __TEXT.__cstring: 0x251c
+  __TEXT.__oslogstring: 0x1f2d
+  __TEXT.__unwind_info: 0x8f0
   __TEXT.__objc_classname: 0x207
-  __TEXT.__objc_methname: 0x353d
-  __TEXT.__objc_methtype: 0x614
-  __TEXT.__objc_stubs: 0x3640
+  __TEXT.__objc_methname: 0x35f4
+  __TEXT.__objc_methtype: 0x64a
+  __TEXT.__objc_stubs: 0x36e0
   __DATA_CONST.__got: 0x240
-  __DATA_CONST.__const: 0xb10
+  __DATA_CONST.__const: 0xb50
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xff0
+  __DATA_CONST.__objc_selrefs: 0x1018
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x990
-  __AUTH_CONST.__auth_got: 0x3b0
+  __AUTH_CONST.__auth_got: 0x3a8
   __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x4820
-  __AUTH_CONST.__objc_const: 0x2228
+  __AUTH_CONST.__cfstring: 0x4940
+  __AUTH_CONST.__objc_const: 0x2280
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x194
+  __DATA.__objc_ivar: 0x19c
   __DATA.__data: 0x180
   __DATA.__bss: 0x90
   __DATA_DIRTY.__objc_data: 0x690

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 49C3A704-F031-39E5-9F84-0B096FBB3FFA
-  Functions: 755
-  Symbols:   2715
-  CStrings:  2208
+  UUID: 427F0961-237F-3A7E-B1FF-EA932812DDED
+  Functions: 768
+  Symbols:   2756
+  CStrings:  2243
 
Symbols:
+ +[SRXPCListener handleCommand:info:reply:error:]
+ +[SRXPCListener handleCommand:info:reply:error:].cold.1
+ -[SRAssetBundleCacheEntry onDevice]
+ -[SRAssetBundleCacheEntry onDevice].cold.1
+ -[SRAssetBundleCacheEntry onDevice].cold.2
+ -[SRDefaultsManager requiredAssetsContentVersion]
+ -[SRLanguageConfiguration hasTestAssets]
+ -[SRLanguageConfiguration setHasTestAssets:]
+ -[SRXPCConnection handleReply:completion:]
+ -[SRXPCConnection sendCommand:info:sync:completion:]
+ GCC_except_table0
+ GCC_except_table15
+ GCC_except_table17
+ GCC_except_table5
+ GCC_except_table60
+ _OBJC_IVAR_$_SRDefaultsManager._requiredAssetsContentVersion
+ _OBJC_IVAR_$_SRLanguageConfiguration._hasTestAssets
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _SRAssetAvailabilityString
+ __OBJC_$_PROP_LIST_SRLanguageConfiguration
+ ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke.247
+ ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke.247.cold.1
+ ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.240
+ ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.240.cold.1
+ ___51-[SRDefaultsManager loadDefaultsFromDefaultAssets:]_block_invoke.418
+ ___52-[SRXPCConnection sendCommand:info:sync:completion:]_block_invoke
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.568
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.570
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.570.cold.1
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_2.569
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_2.569.cold.1
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_4.cold.1
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.465
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.470
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.470.cold.1
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.471
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.480
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.482
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.482.cold.1
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.466
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.472
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.481
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.481.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.492.cold.3
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.493
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.495.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.497.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.498
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.498.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.502.cold.3
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.502.cold.4
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.503.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.505.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.507
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.507.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.508
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.508.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.509
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.509.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.509.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke_2.501
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke_2.501.cold.1
+ ___82-[SRDefaultsManager assetsFromResourcePath:deliveryType:assetType:language:force:]_block_invoke.438
+ ___82-[SRDefaultsManager assetsFromResourcePath:deliveryType:assetType:language:force:]_block_invoke.438.cold.1
+ ___82-[SRDefaultsManager assetsFromResourcePath:deliveryType:assetType:language:force:]_block_invoke.439
+ ___SRAreAssetsAvailableForLocale_block_invoke
+ ___SRAreAssetsAvailableForLocale_block_invoke.cold.1
+ ___SRIsAssetAvailable_block_invoke
+ ___SRIsAssetAvailable_block_invoke.cold.1
+ ___block_descriptor_105_e8_32s40s48s56s64s72s80r88r96r_e5_v8?0ls32l8r80l8s40l8s48l8s56l8r88l8s64l8r96l8s72l8
+ ___block_descriptor_121_e8_32s40s48s56s64s72s80s88r96r104r112w_e20_v20?0B8"NSError"12ls32l8w112l8s40l8r88l8s48l8s56l8s64l8r96l8s72l8r104l8s80l8
+ ___block_descriptor_40_e8_32bs_e45_v24?0"NSObject<OS_xpc_object>"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32r_e45_v24?0"NSObject<OS_xpc_object>"8"NSError"16lr32l8
+ ___block_descriptor_56_e8_32s40bs_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8
+ ___block_descriptor_89_e8_32s40s48s56s64r72r80r_e25_v32?0"DDSAsset"8Q16^B24lr64l8s32l8s40l8s48l8r72l8s56l8r80l8
+ _objc_msgSend$handleCommand:info:reply:error:
+ _objc_msgSend$handleReply:completion:
+ _objc_msgSend$onDevice
+ _objc_msgSend$requiredAssetsContentVersion
+ _objc_msgSend$sendCommand:info:sync:completion:
+ _objc_msgSend$setHasTestAssets:
- -[SRAssetBundleCacheEntry makeResultWithBundleVersion:path:loaded:].cold.3
- -[SRAssetBundleCacheEntry makeResultWithBundleVersion:path:loaded:].cold.4
- -[SRXPCConnection sendMessage:sync:completion:]
- GCC_except_table11
- GCC_except_table12
- GCC_except_table59
- GCC_except_table6
- GCC_except_table88
- ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke.248
- ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke.248.cold.1
- ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.241
- ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.241.cold.1
- ___47-[SRXPCConnection sendMessage:sync:completion:]_block_invoke
- ___51-[SRDefaultsManager loadDefaultsFromDefaultAssets:]_block_invoke.415
- ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.565
- ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.565.cold.1
- ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_5
- ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_6
- ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_6.cold.1
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.462
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.467
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.467.cold.1
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.468
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.477
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.479
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.479.cold.1
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.463
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.469
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.478
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.478.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.489
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.489.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.489.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.489.cold.3
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.490
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.494
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.496
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.496.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.496.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.499.cold.3
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.499.cold.4
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.501
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.506.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.506.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke_2.498
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke_2.498.cold.1
- ___82-[SRDefaultsManager assetsFromResourcePath:deliveryType:assetType:language:force:]_block_invoke.435
- ___82-[SRDefaultsManager assetsFromResourcePath:deliveryType:assetType:language:force:]_block_invoke.435.cold.1
- ___82-[SRDefaultsManager assetsFromResourcePath:deliveryType:assetType:language:force:]_block_invoke.436
- ___block_descriptor_105_e8_32s40s48s56s64s72s80r88r96r_e5_v8?0ls32l8r80l8s40l8s48l8s56l8r88l8r96l8s64l8s72l8
- ___block_descriptor_121_e8_32s40s48s56s64s72s80s88r96r104r112w_e20_v20?0B8"NSError"12ls32l8w112l8s40l8r88l8s48l8s56l8s64l8r96l8r104l8s72l8s80l8
- ___block_descriptor_48_e8_32bs40r_e33_v16?0"NSObject<OS_xpc_object>"8lr40l8s32l8
- ___block_descriptor_48_e8_32bs_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8
- ___block_descriptor_89_e8_32s40s48s56s64r72r80r_e25_v32?0"DDSAsset"8Q16^B24lr64l8s32l8s40l8s48l8r72l8r80l8s56l8
- _objc_msgSend$sendMessage:sync:completion:
- _xpc_dictionary_get_array
CStrings:
+ "\n%@ for %@\n"
+ "\n%@ for (%@, %@)\n"
+ "(forceLoad) Couldn't get assets from %@"
+ "@\"NSNumber\""
+ "Asset availability query returned error: %@"
+ "Assets are available"
+ "Assets are not available"
+ "Assets are not supported"
+ "Assets availability query returned error: %@"
+ "Couldn't get assets from %@"
+ "Invalid asset availability status %lu"
+ "Invalid command %llu"
+ "MobileAssetsContentVersion"
+ "TB,N,V_hasTestAssets"
+ "_hasTestAssets"
+ "_requiredAssetsContentVersion"
+ "av"
+ "availability"
+ "c"
+ "c:%llu, sync:%d, qos:%llu"
+ "getAssetBundleInfo(%@, %@) = (%d, %@, %@, %d)"
+ "handleCommand:info:reply:error:"
+ "handleReply:completion:"
+ "onDevice"
+ "requiredAssetsContentVersion"
+ "rid"
+ "searchutil -c asset:availability:<localeIdentifier>[:<deliveryType>]\n\tReturns asset availability for the specified locale or (locale, delivery type).\n"
+ "sendCommand:info:sync:completion:"
+ "setHasTestAssets:"
+ "v24@?0@\"NSObject<OS_xpc_object>\"8@\"NSError\"16"
+ "v44@0:8Q16@24B32@?36"
+ "v48@0:8Q16@24@32^@40"
- "getAssetBundleInfo(%@, %@) = (%d, %@, %@)"
- "qi"
- "qid"
- "ri"
- "sendMessage:sync:completion:"
- "sync:%d, qos:%llu"

```
