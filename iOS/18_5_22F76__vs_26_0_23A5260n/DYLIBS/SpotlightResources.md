## SpotlightResources

> `/System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources`

```diff

-2333.50.1.0.0
-  __TEXT.__text: 0x225ac
-  __TEXT.__auth_stubs: 0x710
-  __TEXT.__objc_methlist: 0x13e8
-  __TEXT.__const: 0xd8
-  __TEXT.__gcc_except_tab: 0x95c
-  __TEXT.__cstring: 0x169f
-  __TEXT.__oslogstring: 0x1aca
-  __TEXT.__unwind_info: 0x750
-  __TEXT.__objc_classname: 0x1b4
-  __TEXT.__objc_methname: 0x321d
-  __TEXT.__objc_methtype: 0x57f
-  __TEXT.__objc_stubs: 0x32e0
-  __DATA_CONST.__got: 0x220
-  __DATA_CONST.__const: 0x960
-  __DATA_CONST.__objc_classlist: 0xa8
+2374.0.1.0.0
+  __TEXT.__text: 0x22e44
+  __TEXT.__auth_stubs: 0x6e0
+  __TEXT.__objc_methlist: 0x1420
+  __TEXT.__const: 0xe0
+  __TEXT.__gcc_except_tab: 0x968
+  __TEXT.__cstring: 0x1743
+  __TEXT.__oslogstring: 0x1ab9
+  __TEXT.__unwind_info: 0x748
+  __TEXT.__objc_classname: 0x1c9
+  __TEXT.__objc_methname: 0x326b
+  __TEXT.__objc_methtype: 0x595
+  __TEXT.__objc_stubs: 0x3340
+  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__const: 0x958
+  __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf28
-  __DATA_CONST.__objc_superrefs: 0x90
-  __DATA_CONST.__objc_arraydata: 0x980
-  __AUTH_CONST.__auth_got: 0x398
+  __DATA_CONST.__objc_selrefs: 0xf40
+  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA_CONST.__objc_arraydata: 0x990
+  __AUTH_CONST.__auth_got: 0x380
   __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x3d80
-  __AUTH_CONST.__objc_const: 0x1e98
+  __AUTH_CONST.__cfstring: 0x3ea0
+  __AUTH_CONST.__objc_const: 0x1f68
+  __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x178
-  __DATA.__data: 0x310
-  __DATA.__bss: 0xf0
-  __DATA_DIRTY.__objc_data: 0x460
-  __DATA_DIRTY.__data: 0xc8
-  __DATA_DIRTY.__bss: 0x220
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x17c
+  __DATA.__data: 0x180
+  __DATA.__bss: 0x70
+  __DATA_DIRTY.__objc_data: 0x690
+  __DATA_DIRTY.__data: 0x258
+  __DATA_DIRTY.__bss: 0x2a8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 897D3EE0-1352-335E-8897-601B02EF023E
-  Functions: 691
-  Symbols:   2495
-  CStrings:  1950
+  UUID: 49DB50F9-D9F0-39A6-A3C7-EC4288BAFF52
+  Functions: 698
+  Symbols:   2514
+  CStrings:  1977
 
Symbols:
+ +[SRDefaultsManager lastLoadedBundleVersion]
+ +[SRPARSession spotlightResourcesPARSessionForClient:flags:]
+ +[SRResourcesManager lastLoadedBundleVersion]
+ -[SRAssetBundle initWithLocale:bundleVersions:]
+ -[SRAssetBundle shouldUpdateForBundleVersions:]
+ -[SRAssetBundleCache upsertAssetBundleWithAssetType:language:deliveryType:bundleVersion:path:]
+ -[SRAssetBundleCacheEntry bundleVersion]
+ -[SRAssetBundleCacheEntry makeResultWithBundleVersion:path:]
+ -[SRAssetBundleCacheEntry makeResultWithBundleVersion:path:].cold.1
+ -[SRAssetBundleCacheEntry makeResultWithBundleVersion:path:].cold.2
+ -[SRAssetBundleCacheEntry makeResultWithBundleVersion:path:].cold.3
+ -[SRAssetBundleCacheEntry makeResultWithBundleVersion:path:].cold.4
+ -[SRAssetBundleVersion .cxx_destruct]
+ -[SRAssetBundleVersion compare:]
+ -[SRAssetBundleVersion compare:].cold.1
+ -[SRAssetBundleVersion compare:].cold.2
+ -[SRAssetBundleVersion initWithBundleVersion:]
+ -[SRAssetBundleVersion version]
+ -[SRDefaultsManager notifyObserversWithLanguage:bundleVersions:]
+ -[SRDefaultsManager shouldReloadLanguage:forBundleVersions:]
+ -[SRDefaultsManager updateBundleVersions:forLanguage:]
+ -[SRResources didUpdateDefaultsWithLanguage:bundleVersions:trial:]
+ GCC_except_table24
+ GCC_except_table57
+ GCC_except_table85
+ _OBJC_CLASS_$_NSNumberFormatter
+ _OBJC_CLASS_$_SRAssetBundleVersion
+ _OBJC_IVAR_$_SRAssetBundle._bundleVersions
+ _OBJC_IVAR_$_SRAssetBundleCacheEntry._bundleVersion
+ _OBJC_IVAR_$_SRAssetBundleVersion._version
+ _OBJC_IVAR_$_SRDefaultsManager._loadedBundleVersions
+ _OBJC_METACLASS_$_SRAssetBundleVersion
+ __OBJC_$_INSTANCE_METHODS_SRAssetBundleVersion
+ __OBJC_$_INSTANCE_VARIABLES_SRAssetBundleVersion
+ __OBJC_$_PROP_LIST_SRAssetBundleVersion
+ __OBJC_CLASS_RO_$_SRAssetBundleVersion
+ __OBJC_METACLASS_RO_$_SRAssetBundleVersion
+ ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke.240
+ ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke.240.cold.1
+ ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.233
+ ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.233.cold.1
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.1
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.10
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.11
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.12
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.13
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.2
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.3
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.4
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.5
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.6
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.7
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.8
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.441.cold.9
+ ___47-[SRAssetBundle shouldUpdateForBundleVersions:]_block_invoke
+ ___47-[SRAssetBundle shouldUpdateForBundleVersions:]_block_invoke_2
+ ___47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke.431
+ ___47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke.431.cold.1
+ ___47-[SRResources fetchParameter:checkForPositive:]_block_invoke
+ ___54-[SRDefaultsManager updateBundleVersions:forLanguage:]_block_invoke
+ ___54-[SRDefaultsManager updateBundleVersions:forLanguage:]_block_invoke_2
+ ___60-[SRDefaultsManager shouldReloadLanguage:forBundleVersions:]_block_invoke
+ ___60-[SRDefaultsManager shouldReloadLanguage:forBundleVersions:]_block_invoke_2
+ ___60-[SRDefaultsManager shouldReloadLanguage:forBundleVersions:]_block_invoke_3
+ ___64-[SRDefaultsManager notifyObserversWithLanguage:bundleVersions:]_block_invoke
+ ___64-[SRDefaultsManager notifyObserversWithLanguage:bundleVersions:]_block_invoke_2
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.443
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.443.cold.1
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.443.cold.2
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.443.cold.3
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.443.cold.4
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.446.cold.2
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.451.cold.1
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.451.cold.2
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.454.cold.2
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.454.cold.3
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.456
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.458
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.458.cold.1
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.459
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.461
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.461.cold.1
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.457
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.457.cold.1
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.460
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.460.cold.1
+ ___block_descriptor_41_e8_32s_e24_v32?0"SRAsset"8Q16^B24ls32l8
+ ___block_descriptor_44_e8_32s_e38_v32?0"NSString"8"SRParameter"16^B24ls32l8
+ ___block_descriptor_48_e8_32s40r_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48s_e47_v32?0"NSString"8"SRAssetBundleVersion"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48r_e47_v32?0"NSString"8"SRAssetBundleVersion"16^B24ls32l8s40l8r48l8
+ ___block_descriptor_72_e8_32s40s48s56r_e47_v32?0"NSString"8"SRAssetBundleVersion"16^B24ls32l8s40l8s48l8r56l8
+ ___block_literal_global.434
+ ___block_literal_global.481
+ ___block_literal_global.484
+ ___block_literal_global.503
+ ___block_literal_global.66
+ _deliveryTypeID.cold.1
+ _getBundleVersionFromPath
+ _getBundleVersionFromPath.cold.1
+ _objc_msgSend$attributes
+ _objc_msgSend$bundleVersion
+ _objc_msgSend$compare:
+ _objc_msgSend$didUpdateDefaultsWithLanguage:bundleVersions:trial:
+ _objc_msgSend$initWithBundleVersion:
+ _objc_msgSend$initWithLocale:bundleVersions:
+ _objc_msgSend$lastLoadedBundleVersion
+ _objc_msgSend$lastObject
+ _objc_msgSend$makeResultWithBundleVersion:path:
+ _objc_msgSend$notifyObserversWithLanguage:bundleVersions:
+ _objc_msgSend$numberFromString:
+ _objc_msgSend$setNumberStyle:
+ _objc_msgSend$shouldReloadLanguage:forBundleVersions:
+ _objc_msgSend$shouldUpdateForBundleVersions:
+ _objc_msgSend$spotlightResourcesPARSessionForClient:flags:
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$updateBundleVersions:forLanguage:
+ _objc_msgSend$upsertAssetBundleWithAssetType:language:deliveryType:bundleVersion:path:
+ _sLastLoadedBundleVersion
+ _sLastLoadedBundleVersion_block_invoke.onceToken
+ _sLastLoadedBundleVersion_block_invoke_2.onceToken1
- +[SRDefaultsManager lastLoadedContentVersion]
- +[SRPARSession spotlightResourcesPARSessionForClient:]
- +[SRResourcesManager lastLoadedContentVersion]
- -[SRAssetBundle initWithLocale:contentVersions:]
- -[SRAssetBundle shouldUpdateForContentVersions:]
- -[SRAssetBundleCache upsertAssetBundleWithAssetType:language:deliveryType:contentVersion:path:]
- -[SRAssetBundleCacheEntry contentVersion]
- -[SRAssetBundleCacheEntry makeResultWithContentVersion:path:]
- -[SRAssetBundleCacheEntry makeResultWithContentVersion:path:].cold.1
- -[SRAssetBundleCacheEntry makeResultWithContentVersion:path:].cold.2
- -[SRAssetBundleCacheEntry makeResultWithContentVersion:path:].cold.3
- -[SRAssetBundleCacheEntry makeResultWithContentVersion:path:].cold.4
- -[SRDefaultsManager notifyObserversWithLanguage:contentVersions:]
- -[SRDefaultsManager shouldReloadLanguage:forContentVersions:]
- -[SRDefaultsManager updateContentVersions:forLanguage:]
- -[SRResources didUpdateDefaultsWithLanguage:contentVersions:trial:]
- -[SRResources fetchParameter:checkForPositive:].cold.6
- GCC_except_table13
- GCC_except_table46
- GCC_except_table74
- _OBJC_IVAR_$_SRAssetBundle._contentVersions
- _OBJC_IVAR_$_SRAssetBundleCacheEntry._contentVersion
- _OBJC_IVAR_$_SRDefaultsManager._loadedContentVersions
- ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke.176
- ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke.176.cold.1
- ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.169
- ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.169.cold.1
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434.cold.1
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434.cold.10
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434.cold.11
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434.cold.12
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434.cold.13
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434.cold.2
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434.cold.3
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434.cold.4
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434.cold.5
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434.cold.6
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434.cold.7
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434.cold.8
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.434.cold.9
- ___47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke.427
- ___47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke.427.cold.1
- ___48-[SRAssetBundle shouldUpdateForContentVersions:]_block_invoke
- ___48-[SRAssetBundle shouldUpdateForContentVersions:]_block_invoke_2
- ___55-[SRDefaultsManager updateContentVersions:forLanguage:]_block_invoke
- ___55-[SRDefaultsManager updateContentVersions:forLanguage:]_block_invoke_2
- ___61-[SRDefaultsManager shouldReloadLanguage:forContentVersions:]_block_invoke
- ___61-[SRDefaultsManager shouldReloadLanguage:forContentVersions:]_block_invoke_2
- ___61-[SRDefaultsManager shouldReloadLanguage:forContentVersions:]_block_invoke_3
- ___65-[SRDefaultsManager notifyObserversWithLanguage:contentVersions:]_block_invoke
- ___65-[SRDefaultsManager notifyObserversWithLanguage:contentVersions:]_block_invoke_2
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.439
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.439.cold.1
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.439.cold.2
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.439.cold.3
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.439.cold.4
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.440
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.442
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.442.cold.1
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.442.cold.2
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.447
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.447.cold.1
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.447.cold.2
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.450.cold.2
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.450.cold.3
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.457
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.457.cold.1
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.445
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.445.cold.1
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.456
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.456.cold.1
- ___block_descriptor_42_e8_32s_e24_v32?0"SRAsset"8Q16^B24ls32l8
- ___block_descriptor_56_e8_32s40s48r_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8r48l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e35_v32?0"NSString"8"NSNumber"16^B24ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48r_e35_v32?0"NSString"8"NSNumber"16^B24ls32l8s40l8r48l8
- ___block_descriptor_72_e8_32s40s48s56r_e35_v32?0"NSString"8"NSNumber"16^B24ls32l8s40l8s48l8r56l8
- ___block_literal_global.107
- ___block_literal_global.427
- ___block_literal_global.470
- ___block_literal_global.473
- ___block_literal_global.492
- __xpc_runtime_is_app_sandboxed
- _getContentVersionFromPath
- _getContentVersionFromPath.cold.1
- _objc_msgSend$contentVersion
- _objc_msgSend$didUpdateDefaults
- _objc_msgSend$didUpdateDefaultsWithLanguage:contentVersions:trial:
- _objc_msgSend$initWithLocale:contentVersions:
- _objc_msgSend$intValue
- _objc_msgSend$lastLoadedContentVersion
- _objc_msgSend$makeResultWithContentVersion:path:
- _objc_msgSend$notifyObserversWithLanguage:contentVersions:
- _objc_msgSend$numberWithUnsignedInteger:
- _objc_msgSend$numberWithUnsignedLongLong:
- _objc_msgSend$shouldReloadLanguage:forContentVersions:
- _objc_msgSend$shouldUpdateForContentVersions:
- _objc_msgSend$spotlightResourcesPARSessionForClient:
- _objc_msgSend$updateContentVersions:forLanguage:
- _objc_msgSend$upsertAssetBundleWithAssetType:language:deliveryType:contentVersion:path:
- _sAssetServer_block_invoke.onceToken
- _sAssetServer_block_invoke_2.onceToken1
- _xpc_dictionary_get_uint64
- _xpc_dictionary_set_uint64
CStrings:
+ "(%@, %@) for asset (%@, %@, %@)"
+ "."
+ "336"
+ "337"
+ "@\"SRAssetBundleVersion\""
+ "@28@0:8@16I24"
+ "Asset is from roots: %@"
+ "BundleVersion"
+ "BundleVersion:%@\n\n%@"
+ "Delta2025"
+ "Delta2025Test"
+ "Invalid query entry type"
+ "Invalid query type"
+ "Malformed bundle version %@"
+ "No results"
+ "Null bundle version for asset (%@, %@, %@)"
+ "Optional2025"
+ "Optional2025Test"
+ "SRAssetBundleVersion"
+ "SRBundleVersion"
+ "Status"
+ "T@\"NSString\",R,N,V_version"
+ "T@\"SRAssetBundleVersion\",R,N,V_bundleVersion"
+ "Unsupported asset delivery type %ld"
+ "Unsupported asset deliveryType %@"
+ "Unsupported asset type %ld"
+ "[%d] Error loading (%@, %@) assets"
+ "[%d] Loading %ld assets for (%@, %@)"
+ "[%d] Loading (%@, %@) assets at %@"
+ "_bundleVersion"
+ "_bundleVersions"
+ "_loadedBundleVersions"
+ "_version"
+ "attributes"
+ "b"
+ "bundleVersion"
+ "com.apple.dt.xctest"
+ "com.apple.spotlightui.cli"
+ "compare:"
+ "default_factors_%@_fbs.bin"
+ "didUpdateDefaultsWithLanguage:bundleVersions:trial:"
+ "initWithBundleVersion:"
+ "initWithLocale:bundleVersions:"
+ "lastLoadedBundleVersion"
+ "lastObject"
+ "makeResultWithBundleVersion:path:"
+ "malformed bundle version %@"
+ "n"
+ "notifyObserversWithLanguage:bundleVersions:"
+ "numberFromString:"
+ "setNumberStyle:"
+ "shouldReloadLanguage:forBundleVersions:"
+ "shouldUpdateForBundleVersions:"
+ "spotlightResourcesPARSessionForClient:flags:"
+ "unsignedLongLongValue"
+ "updateBundleVersions:forLanguage:"
+ "upsertAssetBundleWithAssetType:language:deliveryType:bundleVersion:path:"
+ "v32@?0@\"NSString\"8@\"SRAssetBundleVersion\"16^B24"
+ "v32@?0@\"NSString\"8@\"SRParameter\"16^B24"
+ "v56@0:8@16@24@32@40@48"
- "!!"
- "(%llu, %@) for asset (%@, %@, %@)"
- "B32@0:8Q16@24"
- "ContentVersion"
- "ContentVersion:%llu\n\n%@"
- "DeltaTest"
- "Has SRA roots installed, setting content version to 9999 for %@"
- "Invalid asset delivery type %ld"
- "Invalid query entry type %d"
- "Invalid query type %d"
- "Null content version for asset (%@, %@, %@)"
- "Optional2024Test"
- "Parameter %@ not found in defaults manager."
- "Q"
- "Sandboxed client"
- "TQ,R,N,V_contentVersion"
- "Unknown asset type %ld"
- "[%d, %d] Error loading (%@, %@) assets"
- "[%d, %d] Loading %ld assets for (%@, %@)"
- "[%d, %d] Loading (%@, %@) assets at %@"
- "_contentVersion"
- "_contentVersions"
- "_loadedContentVersions"
- "contentVersion"
- "defaults2024.plist"
- "didUpdateDefaults"
- "didUpdateDefaultsWithLanguage:contentVersions:trial:"
- "initWithLocale:contentVersions:"
- "intValue"
- "lastLoadedContentVersion"
- "legacyOTA"
- "makeResultWithContentVersion:path:"
- "notifyObserversWithLanguage:contentVersions:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "shouldReloadLanguage:forContentVersions:"
- "shouldUpdateForContentVersions:"
- "spotlightResourcesPARSessionForClient:"
- "updateContentVersions:forLanguage:"
- "upsertAssetBundleWithAssetType:language:deliveryType:contentVersion:path:"
- "v"
- "v32@?0@\"NSString\"8@\"NSNumber\"16^B24"
- "v56@0:8@16@24@32Q40@48"

```
