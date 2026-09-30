## SpotlightResources

> `/System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources`

```diff

-2387.1.0.0.0
-  __TEXT.__text: 0x2607c
+2391.1.0.0.0
+  __TEXT.__text: 0x27e30
   __TEXT.__auth_stubs: 0x740
-  __TEXT.__objc_methlist: 0x14b0
-  __TEXT.__const: 0xe8
-  __TEXT.__gcc_except_tab: 0xbac
-  __TEXT.__cstring: 0x2366
-  __TEXT.__oslogstring: 0x1cd3
-  __TEXT.__unwind_info: 0x8a0
-  __TEXT.__objc_classname: 0x1ea
-  __TEXT.__objc_methname: 0x33a1
-  __TEXT.__objc_methtype: 0x5a6
-  __TEXT.__objc_stubs: 0x3560
-  __DATA_CONST.__got: 0x238
-  __DATA_CONST.__const: 0x980
-  __DATA_CONST.__objc_classlist: 0xc0
+  __TEXT.__objc_methlist: 0x1518
+  __TEXT.__const: 0x108
+  __TEXT.__gcc_except_tab: 0xddc
+  __TEXT.__cstring: 0x2373
+  __TEXT.__oslogstring: 0x1e6f
+  __TEXT.__unwind_info: 0x8b8
+  __TEXT.__objc_classname: 0x208
+  __TEXT.__objc_methname: 0x34a7
+  __TEXT.__objc_methtype: 0x614
+  __TEXT.__objc_stubs: 0x3600
+  __DATA_CONST.__got: 0x240
+  __DATA_CONST.__const: 0xae8
+  __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfb8
-  __DATA_CONST.__objc_superrefs: 0x98
-  __DATA_CONST.__objc_arraydata: 0x9a0
+  __DATA_CONST.__objc_selrefs: 0xfe0
+  __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA_CONST.__objc_arraydata: 0x990
   __AUTH_CONST.__auth_got: 0x3b0
-  __AUTH_CONST.__const: 0x4c0
-  __AUTH_CONST.__cfstring: 0x4840
-  __AUTH_CONST.__objc_const: 0x20c8
-  __AUTH_CONST.__objc_dictobj: 0xc8
+  __AUTH_CONST.__const: 0x4a0
+  __AUTH_CONST.__cfstring: 0x4820
+  __AUTH_CONST.__objc_const: 0x21e8
+  __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x184
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x190
   __DATA.__data: 0x180
-  __DATA.__bss: 0x98
+  __DATA.__bss: 0x90
   __DATA_DIRTY.__objc_data: 0x690
   __DATA_DIRTY.__data: 0x258
-  __DATA_DIRTY.__bss: 0x298
+  __DATA_DIRTY.__bss: 0x2a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 49E773E2-3350-3785-845C-77284FBB6562
-  Functions: 733
-  Symbols:   2642
-  CStrings:  2176
+  UUID: 27D976C8-307F-32F5-ACE6-151333C295C6
+  Functions: 751
+  Symbols:   2702
+  CStrings:  2202
 
Symbols:
+ -[SRAssetBundleCache loadFailedForLanguage:assetType:deliveryType:]
+ -[SRAssetBundleCache queryCache:loading:]
+ -[SRAssetBundleCache queryServerCache:force:completion:]
+ -[SRAssetBundleCache updateCacheWithResults:loading:]
+ -[SRAssetBundleCacheEntry loaded]
+ -[SRAssetBundleCacheEntry makeResultWithBundleVersion:path:loaded:]
+ -[SRAssetBundleCacheEntry makeResultWithBundleVersion:path:loaded:].cold.1
+ -[SRAssetBundleCacheEntry makeResultWithBundleVersion:path:loaded:].cold.2
+ -[SRAssetBundleCacheEntry makeResultWithBundleVersion:path:loaded:].cold.3
+ -[SRAssetBundleCacheEntry makeResultWithBundleVersion:path:loaded:].cold.4
+ -[SRAssetBundleCacheEntry setLoaded:]
+ -[SRAssetBundleQuery xpcObject].cold.1
+ -[SRDefaultsManager assetsFromResourcePath:deliveryType:assetType:language:force:]
+ -[SRDefaultsManager assetsFromResourcePath:deliveryType:assetType:language:force:].cold.1
+ -[SRDefaultsManager loadAssetsForLanguage:reload:force:]
+ -[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]
+ -[SRDefaultsManager notifyObserversWithLanguage:bundleVersions:reloadFromCache:force:]
+ -[SRDefaultsManager refreshCacheForLanguages:force:completion:]
+ -[SRDefaultsManager refreshCacheForLanguages:force:completion:].cold.1
+ -[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]
+ -[SRMASandboxExtensionHandler .cxx_destruct]
+ -[SRMASandboxExtensionHandler assetType]
+ -[SRMASandboxExtensionHandler executeBlock:wait:]
+ -[SRMASandboxExtensionHandler initWithAssetType:]
+ -[SRResourcesManager loadAllParametersForClient:locales:options:]
+ -[SRXPCConnection sendMessage:sync:completion:]
+ GCC_except_table102
+ GCC_except_table104
+ GCC_except_table115
+ GCC_except_table121
+ GCC_except_table122
+ GCC_except_table123
+ GCC_except_table20
+ GCC_except_table28
+ GCC_except_table30
+ GCC_except_table32
+ GCC_except_table34
+ GCC_except_table36
+ GCC_except_table44
+ GCC_except_table47
+ GCC_except_table49
+ GCC_except_table51
+ GCC_except_table54
+ GCC_except_table59
+ GCC_except_table73
+ GCC_except_table78
+ GCC_except_table79
+ GCC_except_table88
+ GCC_except_table94
+ GCC_except_table96
+ GCC_except_table98
+ _NSCocoaErrorDomain
+ _OBJC_CLASS_$_SRMASandboxExtensionHandler
+ _OBJC_IVAR_$_SRAssetBundleCacheEntry._loaded
+ _OBJC_IVAR_$_SRDefaultsManager._sandboxExtensionHandlers
+ _OBJC_IVAR_$_SRMASandboxExtensionHandler._assetType
+ _OBJC_IVAR_$_SRMASandboxExtensionHandler._queue
+ _OBJC_METACLASS_$_SRMASandboxExtensionHandler
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __MAensureExtension
+ __OBJC_$_INSTANCE_METHODS_SRMASandboxExtensionHandler
+ __OBJC_$_INSTANCE_VARIABLES_SRMASandboxExtensionHandler
+ __OBJC_$_PROP_LIST_SRMASandboxExtensionHandler
+ __OBJC_CLASS_RO_$_SRMASandboxExtensionHandler
+ __OBJC_METACLASS_RO_$_SRMASandboxExtensionHandler
+ ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke.248
+ ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke.248.cold.1
+ ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.241
+ ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.241.cold.1
+ ___41-[SRAssetBundleCache queryCache:loading:]_block_invoke
+ ___41-[SRAssetBundleCache queryCache:loading:]_block_invoke_2
+ ___41-[SRAssetBundleCache queryCache:loading:]_block_invoke_3
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.1
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.10
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.11
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.12
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.13
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.2
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.3
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.4
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.5
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.6
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.7
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.8
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.447.cold.9
+ ___47-[SRXPCConnection sendMessage:sync:completion:]_block_invoke
+ ___49-[SRMASandboxExtensionHandler executeBlock:wait:]_block_invoke
+ ___49-[SRMASandboxExtensionHandler executeBlock:wait:]_block_invoke_2
+ ___51-[SRDefaultsManager loadDefaultsFromDefaultAssets:]_block_invoke.414
+ ___53-[SRAssetBundleCache updateCacheWithResults:loading:]_block_invoke
+ ___53-[SRAssetBundleCache updateCacheWithResults:loading:]_block_invoke_2
+ ___53-[SRAssetBundleCache updateCacheWithResults:loading:]_block_invoke_3
+ ___56-[SRAssetBundleCache queryServerCache:force:completion:]_block_invoke
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.564
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.564.cold.1
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_2
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_3
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_4
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_5
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_6
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_6.cold.1
+ ___65-[SRResourcesManager loadAllParametersForClient:locales:options:]_block_invoke
+ ___65-[SRResourcesManager loadAllParametersForClient:locales:options:]_block_invoke.cold.1
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.461
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.466
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.466.cold.1
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.467
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.476
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.478
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.478.cold.1
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.462
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.468
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.477
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.477.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.488
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.488.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.488.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.488.cold.3
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.489
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.491
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.491.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.491.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.493
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.494
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.494.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.495
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.495.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.495.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.496
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.498
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.498.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.498.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.498.cold.3
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.498.cold.4
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.499
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.500
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.501
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.501.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.501.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.502
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.503
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.503.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.504
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.504.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.505
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.505.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.505.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke_2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke_2.497
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke_2.497.cold.1
+ ___82-[SRDefaultsManager assetsFromResourcePath:deliveryType:assetType:language:force:]_block_invoke
+ ___82-[SRDefaultsManager assetsFromResourcePath:deliveryType:assetType:language:force:]_block_invoke.434
+ ___82-[SRDefaultsManager assetsFromResourcePath:deliveryType:assetType:language:force:]_block_invoke.434.cold.1
+ ___82-[SRDefaultsManager assetsFromResourcePath:deliveryType:assetType:language:force:]_block_invoke.435
+ ___82-[SRDefaultsManager assetsFromResourcePath:deliveryType:assetType:language:force:]_block_invoke.cold.1
+ ___86-[SRDefaultsManager notifyObserversWithLanguage:bundleVersions:reloadFromCache:force:]_block_invoke
+ ___86-[SRDefaultsManager notifyObserversWithLanguage:bundleVersions:reloadFromCache:force:]_block_invoke_2
+ ___block_descriptor_105_e8_32s40s48s56s64s72s80r88r96r_e5_v8?0ls32l8r80l8s40l8s48l8s56l8r88l8r96l8s64l8s72l8
+ ___block_descriptor_106_e8_32s40s48s56s64r72r80r88w_e5_v8?0lw88l8s32l8s40l8s48l8r64l8r72l8r80l8s56l8
+ ___block_descriptor_121_e8_32s40s48s56s64s72s80s88r96r104r112w_e20_v20?0B8"NSError"12ls32l8w112l8s40l8r88l8s48l8s56l8s64l8r96l8r104l8s72l8s80l8
+ ___block_descriptor_41_e8_32s_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8
+ ___block_descriptor_48_e8_32r40r_e33_v16?0"SRAssetBundleCacheEntry"8lr32l8r40l8
+ ___block_descriptor_48_e8_32r40w_e5_v8?0lw40l8r32l8
+ ___block_descriptor_48_e8_32r_e40_v24?0"SRAssetBundleQuery"8"NSError"16lr32l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_49_e8_32s40s_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_57_e8_32s40s48s_e50_v32?0"NSString"8"SRAssetBundleCacheEntry"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40r48r56w_e5_v8?0ls32l8r40l8w56l8r48l8
+ ___block_descriptor_64_e8_32s40s48r56w_e5_v8?0ls32l8s40l8w56l8r48l8
+ ___block_descriptor_66_e8_32s40s48r56w_e5_v8?0lw56l8r48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e25_v32?0"DDSAsset"8Q16^B24lr56l8s32l8s40l8s48l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56r64w_e5_v8?0lw64l8r56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56r_e40_v24?0"SRAssetBundleQuery"8"NSError"16ls32l8s40l8r56l8s48l8
+ ___block_descriptor_73_e8_32s40s48s56bs64w_e40_v24?0"SRAssetBundleQuery"8"NSError"16lw64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_73_e8_32s40s48s56bs64w_e5_v8?0lw64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_73_e8_32s40s48s56r64r_e33_v16?0"SRAssetBundleCacheEntry"8lr56l8s32l8s40l8s48l8r64l8
+ ___block_descriptor_73_e8_32s40s48s56r64r_e33_v16?0"SRAssetBundleCacheEntry"8ls32l8s40l8s48l8r56l8r64l8
+ ___block_descriptor_80_e8_32s40s48s56r64r72r_e33_v16?0"SRAssetBundleCacheEntry"8lr56l8s32l8s40l8s48l8r64l8r72l8
+ ___block_descriptor_80_e8_32s40s48s56s64r_e5_v8?0ls32l8s40l8r64l8s48l8s56l8
+ ___block_descriptor_81_e8_32s40s48s56s64s72r_e33_v16?0"SRAssetBundleCacheEntry"8lr72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64r72r80r_e25_v32?0"DDSAsset"8Q16^B24lr64l8s32l8s40l8s48l8s56l8r72l8r80l8
+ ___block_descriptor_88_e8_32s40s48s56s64r72w_e5_v8?0lw72l8s32l8s40l8s48l8r64l8s56l8
+ ___block_descriptor_89_e8_32s40s48s56s64r72r80r_e25_v32?0"DDSAsset"8Q16^B24lr64l8s32l8s40l8s48l8r72l8r80l8s56l8
+ ___block_descriptor_89_e8_32s40s48s56s64s72bs80w_e5_v8?0ls32l8w80l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_98_e8_32s40s48s56r64r72r80w_e5_v8?0lw80l8s32l8s40l8r56l8r64l8r72l8s48l8
+ ___block_literal_global.440
+ ___block_literal_global.487
+ ___block_literal_global.507
+ _executeBlock:wait:.onceToken
+ _loadOTAAssetsForLanguage:updateCache:assetTypes:force:.onceToken
+ _objc_msgSend$assetsFromResourcePath:deliveryType:assetType:language:force:
+ _objc_msgSend$domain
+ _objc_msgSend$executeBlock:wait:
+ _objc_msgSend$initWithAssetType:
+ _objc_msgSend$loadAllParametersForClient:locales:options:
+ _objc_msgSend$loadAssetsForLanguage:reload:force:
+ _objc_msgSend$loadFailedForLanguage:assetType:deliveryType:
+ _objc_msgSend$loadOTAAssetsForLanguage:updateCache:assetTypes:force:
+ _objc_msgSend$loaded
+ _objc_msgSend$makeResultWithBundleVersion:path:loaded:
+ _objc_msgSend$notifyObserversWithLanguage:bundleVersions:reloadFromCache:force:
+ _objc_msgSend$queryCache:loading:
+ _objc_msgSend$queryServerCache:force:completion:
+ _objc_msgSend$refreshCacheForLanguages:force:completion:
+ _objc_msgSend$requestAssetsForLanguages:removeExisting:force:
+ _objc_msgSend$sendMessage:sync:completion:
+ _objc_msgSend$setLoaded:
+ _objc_msgSend$updateCacheWithResults:loading:
+ _xpc_connection_send_message_with_reply_sync
- -[SRAssetBundleCache queryCache:]
- -[SRAssetBundleCache queryServerCache:completion:]
- -[SRAssetBundleCache updateCacheWithResults:]
- -[SRAssetBundleCacheEntry makeResultWithBundleVersion:path:]
- -[SRAssetBundleCacheEntry makeResultWithBundleVersion:path:].cold.1
- -[SRAssetBundleCacheEntry makeResultWithBundleVersion:path:].cold.2
- -[SRAssetBundleCacheEntry makeResultWithBundleVersion:path:].cold.3
- -[SRAssetBundleCacheEntry makeResultWithBundleVersion:path:].cold.4
- -[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]
- -[SRDefaultsManager notifyObserversWithLanguage:bundleVersions:]
- -[SRDefaultsManager refreshCacheForLanguages:completion:]
- -[SRDefaultsManager refreshCacheForLanguages:completion:].cold.1
- -[SRDefaultsManager requestAssetsForLanguages:removeExisting:]
- -[SRDefaultsManager shouldReloadLanguage:forBundleVersions:]
- -[SRDefaultsManager updateBundleVersions:forLanguage:]
- -[SRXPCConnection sendMessageAsync:completion:]
- GCC_except_table101
- GCC_except_table106
- GCC_except_table114
- GCC_except_table118
- GCC_except_table119
- GCC_except_table15
- GCC_except_table23
- GCC_except_table25
- GCC_except_table27
- GCC_except_table29
- GCC_except_table31
- GCC_except_table39
- GCC_except_table42
- GCC_except_table45
- GCC_except_table57
- GCC_except_table61
- GCC_except_table65
- GCC_except_table75
- GCC_except_table76
- GCC_except_table83
- GCC_except_table91
- GCC_except_table93
- GCC_except_table95
- GCC_except_table99
- _OBJC_CLASS_$_MAAsset
- _OBJC_IVAR_$_SRDefaultsManager._loadedBundleVersions
- ___33-[SRAssetBundleCache queryCache:]_block_invoke
- ___33-[SRAssetBundleCache queryCache:]_block_invoke_2
- ___33-[SRAssetBundleCache queryCache:]_block_invoke_3
- ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke.242
- ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke.242.cold.1
- ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.235
- ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.235.cold.1
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.1
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.10
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.11
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.12
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.13
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.2
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.3
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.4
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.5
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.6
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.7
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.8
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.9
- ___45-[SRAssetBundleCache updateCacheWithResults:]_block_invoke
- ___45-[SRAssetBundleCache updateCacheWithResults:]_block_invoke_2
- ___45-[SRAssetBundleCache updateCacheWithResults:]_block_invoke_3
- ___47-[SRXPCConnection sendMessageAsync:completion:]_block_invoke
- ___50-[SRAssetBundleCache queryServerCache:completion:]_block_invoke
- ___51-[SRDefaultsManager loadDefaultsFromDefaultAssets:]_block_invoke.392
- ___54-[SRDefaultsManager updateBundleVersions:forLanguage:]_block_invoke
- ___54-[SRDefaultsManager updateBundleVersions:forLanguage:]_block_invoke_2
- ___57-[SRDefaultsManager refreshCacheForLanguages:completion:]_block_invoke
- ___57-[SRDefaultsManager refreshCacheForLanguages:completion:]_block_invoke_2
- ___57-[SRDefaultsManager refreshCacheForLanguages:completion:]_block_invoke_3
- ___57-[SRDefaultsManager refreshCacheForLanguages:completion:]_block_invoke_4
- ___57-[SRDefaultsManager refreshCacheForLanguages:completion:]_block_invoke_5
- ___57-[SRDefaultsManager refreshCacheForLanguages:completion:]_block_invoke_5.cold.1
- ___60-[SRDefaultsManager shouldReloadLanguage:forBundleVersions:]_block_invoke
- ___60-[SRDefaultsManager shouldReloadLanguage:forBundleVersions:]_block_invoke_2
- ___60-[SRDefaultsManager shouldReloadLanguage:forBundleVersions:]_block_invoke_3
- ___62-[SRDefaultsManager requestAssetsForLanguages:removeExisting:]_block_invoke
- ___62-[SRDefaultsManager requestAssetsForLanguages:removeExisting:]_block_invoke.411
- ___62-[SRDefaultsManager requestAssetsForLanguages:removeExisting:]_block_invoke.411.cold.1
- ___62-[SRDefaultsManager requestAssetsForLanguages:removeExisting:]_block_invoke.421
- ___62-[SRDefaultsManager requestAssetsForLanguages:removeExisting:]_block_invoke.421.cold.1
- ___62-[SRDefaultsManager requestAssetsForLanguages:removeExisting:]_block_invoke.422
- ___62-[SRDefaultsManager requestAssetsForLanguages:removeExisting:]_block_invoke.431
- ___62-[SRDefaultsManager requestAssetsForLanguages:removeExisting:]_block_invoke.431.cold.1
- ___62-[SRDefaultsManager requestAssetsForLanguages:removeExisting:]_block_invoke_2
- ___62-[SRDefaultsManager requestAssetsForLanguages:removeExisting:]_block_invoke_2.412
- ___62-[SRDefaultsManager requestAssetsForLanguages:removeExisting:]_block_invoke_2.423
- ___62-[SRDefaultsManager requestAssetsForLanguages:removeExisting:]_block_invoke_3
- ___64-[SRDefaultsManager notifyObserversWithLanguage:bundleVersions:]_block_invoke
- ___64-[SRDefaultsManager notifyObserversWithLanguage:bundleVersions:]_block_invoke_2
- ___64-[SRResourcesManager loadAllParametersForClient:locale:options:]_block_invoke
- ___64-[SRResourcesManager loadAllParametersForClient:locale:options:]_block_invoke.cold.1
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.443
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.443.cold.1
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.443.cold.2
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.443.cold.3
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.443.cold.4
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.444
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.446
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.446.cold.1
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.446.cold.2
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.448
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.450
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.450.cold.1
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.451
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.451.cold.1
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.451.cold.2
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.452
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.454
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.454.cold.1
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.454.cold.2
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.454.cold.3
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.455
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.456
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.458
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.458.cold.1
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.459
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.461
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.461.cold.1
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.449
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.449.cold.1
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.453
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.453.cold.1
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.457
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.457.cold.1
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.460
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.460.cold.1
- ___block_descriptor_40_e8_32r_e33_v16?0"SRAssetBundleCacheEntry"8lr32l8
- ___block_descriptor_56_e8_32s40r48r_e33_v16?0"SRAssetBundleCacheEntry"8lr40l8r48l8s32l8
- ___block_descriptor_56_e8_32s40r_e40_v24?0"SRAssetBundleQuery"8"NSError"16lr40l8s32l8
- ___block_descriptor_56_e8_32s40s48r_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48s_e47_v32?0"NSString"8"SRAssetBundleVersion"16^B24ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s_e40_v24?0"SRAssetBundleQuery"8"NSError"16ls32l8s40l8
- ___block_descriptor_57_e8_32s40r48w_e5_v8?0lw48l8r40l8s32l8
- ___block_descriptor_64_e8_32s40s48bs56w_e40_v24?0"SRAssetBundleQuery"8"NSError"16lw56l8s32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56r_e25_v32?0"DDSAsset"8Q16^B24lr56l8s32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8r56l8s48l8
- ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48r56r_e5_v8?0ls32l8r48l8r56l8s40l8
- ___block_descriptor_72_e8_32s40s48s56bs64w_e5_v8?0lw64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e25_v32?0"DDSAsset"8Q16^B24lr56l8s32l8s40l8r64l8s48l8
- ___block_descriptor_72_e8_32s40s48s56r_e47_v32?0"NSString"8"SRAssetBundleVersion"16^B24ls32l8s40l8s48l8r56l8
- ___block_descriptor_72_e8_32s40s48s56w_e5_v8?0lw56l8s32l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48s56s64s72r_e5_v8?0ls32l8r72l8s40l8s48l8s56l8s64l8
- ___block_descriptor_82_e8_32s40s48r56r64w_e5_v8?0lw64l8s32l8s40l8r48l8r56l8
- ___block_descriptor_88_e8_32s40s48s56s64s72bs80w_e5_v8?0ls32l8w80l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_90_e8_32s40s48s56r64r72w_e5_v8?0lw72l8s32l8s40l8r56l8r64l8s48l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80r88w_e20_v20?0B8"NSError"12ls32l8w88l8s40l8r80l8s48l8s56l8s64l8s72l8
- ___block_literal_global.414
- ___block_literal_global.434
- ___block_literal_global.481
- ___block_literal_global.501
- _dispatch_time
- _loadAssetsFromResourcePath
- _loadAssetsFromResourcePath.cold.1
- _loadOTAAssetsForLanguage:reload:assetTypes:force:.onceToken
- _objc_msgSend$getLocalFileUrl
- _objc_msgSend$initWithAttributes:
- _objc_msgSend$loadOTAAssetsForLanguage:reload:assetTypes:force:
- _objc_msgSend$makeResultWithBundleVersion:path:
- _objc_msgSend$notifyObserversWithLanguage:bundleVersions:
- _objc_msgSend$queryCache:
- _objc_msgSend$queryServerCache:completion:
- _objc_msgSend$refreshCacheForLanguages:completion:
- _objc_msgSend$requestAssetsForLanguages:removeExisting:
- _objc_msgSend$sendMessageAsync:completion:
- _objc_msgSend$shouldReloadLanguage:forBundleVersions:
- _objc_msgSend$updateBundleVersions:forLanguage:
- _objc_msgSend$updateCacheWithResults:
- _objc_release_x3
- _sLastLoadedBundleVersion_block_invoke_2.onceToken1
CStrings:
+ "%zd entries in query"
+ "(%@, %@, %d) for asset (%@, %@, %@)"
+ "(force) Error on retry"
+ "(force) refreshCache %@, notifyLanguages: %@"
+ "(force) requestAssets update for %@, notifyLanguages: %@"
+ ".xctrunner"
+ "@52@0:8@16@24@32@40B48"
+ "B36@0:8@16@24B32"
+ "B56@0:8@16@24@32@40@48"
+ "Error on retry"
+ "Force-"
+ "Got sandbox extension for %@"
+ "Loaded"
+ "Needs sandbox extension"
+ "Null bundle version for (%@, %@, %@)"
+ "Null path for (%@, %@, %@)"
+ "SRMASandboxExtensionHandler"
+ "T@\"NSString\",R,V_assetType"
+ "TB,N,V_loaded"
+ "[%d] %@Loading (%@, %@, %@) assets at %@"
+ "_loaded"
+ "_sandboxExtensionHandlers"
+ "assetsFromResourcePath:deliveryType:assetType:language:force:"
+ "com.apple."
+ "com.apple.spotlightresources.sandboxextension"
+ "domain"
+ "executeBlock:wait:"
+ "initWithAssetType:"
+ "loadAllParametersForClient:locales:options:"
+ "loadAssetsForLanguage:reload:force:"
+ "loadFailedForLanguage:assetType:deliveryType:"
+ "loadOTAAssetsForLanguage:updateCache:assetTypes:force:"
+ "loadOTA[%llu] server 2.2"
+ "loadOTA[%llu] server 3.3"
+ "makeResultWithBundleVersion:path:loaded:"
+ "notifyObserversWithLanguage:bundleVersions:reloadFromCache:force:"
+ "queryCache:loading:"
+ "queryServerCache:force:completion:"
+ "refreshCache %@, notifyLanguages:%@"
+ "refreshCacheForLanguages:force:completion:"
+ "refreshCache[%llu] (%@, %d, %@)"
+ "requestAssets update for %@, notifyLanguages:%@"
+ "requestAssetsForLanguages:removeExisting:force:"
+ "sendMessage:sync:completion:"
+ "setLoaded:"
+ "sync:%d, qos:%llu"
+ "updateCacheWithResults:loading:"
+ "v28@0:8@?16B24"
+ "v32@0:8@16B24B28"
+ "v36@0:8@16B24@?28"
+ "v40@0:8@16@24B32B36"
- "(%@, %@) for asset (%@, %@, %@)"
- "AssetAddedProperties"
- "AssetId"
- "AssetPurpose"
- "AssetState"
- "[%d] Loading (%@, %@) assets at %@"
- "_loadedBundleVersions"
- "getLocalFileUrl"
- "initWithAttributes:"
- "loadOTAAssetsForLanguage:reload:assetTypes:force:"
- "loadOTA[%llu] client 2.3"
- "makeResultWithBundleVersion:path:"
- "notifyObserversWithLanguage:bundleVersions:"
- "queryCache:"
- "queryServerCache:completion:"
- "refreshCacheForLanguages:completion:"
- "requestAssets update for %@"
- "requestAssetsForLanguages:removeExisting:"
- "sendMessageAsync:completion:"
- "shouldReloadLanguage:forBundleVersions:"
- "updateBundleVersions:forLanguage:"
- "updateCacheWithResults:"
- "v56@0:8@16@24@32@40@48"

```
