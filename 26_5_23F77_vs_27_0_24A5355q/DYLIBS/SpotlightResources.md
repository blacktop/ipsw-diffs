## SpotlightResources

> `/System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources`

```diff

-2418.5.9.101.0
-  __TEXT.__text: 0x2bc40
-  __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__objc_methlist: 0x1600
+2444.104.0.0.0
+  __TEXT.__text: 0x2a7f4
+  __TEXT.__objc_methlist: 0x1648
   __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0xe3c
-  __TEXT.__cstring: 0x25e8
-  __TEXT.__oslogstring: 0x21c8
-  __TEXT.__unwind_info: 0x9b8
-  __TEXT.__objc_classname: 0x208
-  __TEXT.__objc_methname: 0x37ca
-  __TEXT.__objc_methtype: 0x669
-  __TEXT.__objc_stubs: 0x37e0
-  __DATA_CONST.__got: 0x248
-  __DATA_CONST.__const: 0xc40
+  __TEXT.__gcc_except_tab: 0xee8
+  __TEXT.__cstring: 0x277f
+  __TEXT.__oslogstring: 0x2456
+  __TEXT.__unwind_info: 0x9c0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xc90
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1080
+  __DATA_CONST.__objc_selrefs: 0x1120
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x990
-  __AUTH_CONST.__auth_got: 0x400
-  __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x4a00
-  __AUTH_CONST.__objc_const: 0x2300
+  __DATA_CONST.__got: 0x278
+  __AUTH_CONST.__const: 0x4e0
+  __AUTH_CONST.__cfstring: 0x4b60
+  __AUTH_CONST.__objc_const: 0x2380
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x1ac
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x1bc
   __DATA.__data: 0x180
-  __DATA.__bss: 0x68
-  __DATA_DIRTY.__objc_data: 0x6e0
+  __DATA.__bss: 0xb0
+  __DATA_DIRTY.__objc_data: 0x640
   __DATA_DIRTY.__data: 0x258
-  __DATA_DIRTY.__bss: 0x2d8
+  __DATA_DIRTY.__bss: 0x2b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/DataDeliveryServices.framework/DataDeliveryServices
   - /System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation
   - /System/Library/PrivateFrameworks/SpotlightLinguistics.framework/SpotlightLinguistics
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/TrialProto.framework/TrialProto
+  - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F9D77071-F6D9-3489-9540-B9DC7E639E3F
-  Functions: 797
-  Symbols:   2857
-  CStrings:  2294
+  UUID: 0D58855B-691D-3DA2-B634-E79FC21DC7AE
+  Functions: 820
+  Symbols:   2930
+  CStrings:  1518
 
Symbols:
+ -[SRDefaultsManager assetNameForContentType:]
+ -[SRDefaultsManager clearUAFCaches]
+ -[SRDefaultsManager dealloc].cold.1
+ -[SRDefaultsManager filePathsFromUAFForContentType:language:]
+ -[SRDefaultsManager filePathsFromUAFForContentType:language:].cold.1
+ -[SRDefaultsManager filePathsFromUAFForContentType:language:].cold.2
+ -[SRDefaultsManager init].cold.1
+ -[SRDefaultsManager loadUAFAssetsForLanguage:fromAssetSet:]
+ -[SRDefaultsManager loadUAFAssetsForLanguages:]
+ -[SRDefaultsManager loadUAFAssetsForLanguages:].cold.1
+ -[SRDefaultsManager notifyObserversWithLanguage:bundleVersions:reloadFromCache:uafUpdate:force:]
+ -[SRDefaultsManager usageDictForLanguage:]
+ -[SRResources didUpdateDefaultsWithBundleVersions:trial:uafUpdate:]
+ -[SRResources didUpdateDefaultsWithBundleVersions:trial:uafUpdate:].cold.1
+ GCC_except_table102
+ GCC_except_table104
+ GCC_except_table106
+ GCC_except_table108
+ GCC_except_table112
+ GCC_except_table114
+ GCC_except_table116
+ GCC_except_table127
+ GCC_except_table133
+ GCC_except_table134
+ GCC_except_table135
+ GCC_except_table136
+ GCC_except_table151
+ GCC_except_table21
+ GCC_except_table30
+ GCC_except_table32
+ GCC_except_table34
+ GCC_except_table36
+ GCC_except_table38
+ GCC_except_table46
+ GCC_except_table49
+ GCC_except_table51
+ GCC_except_table53
+ GCC_except_table56
+ GCC_except_table77
+ GCC_except_table81
+ GCC_except_table86
+ GCC_except_table87
+ GCC_except_table93
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_RBSAssertion
+ _OBJC_CLASS_$_RBSDomainAttribute
+ _OBJC_CLASS_$_RBSProcessHandle
+ _OBJC_CLASS_$_RBSTarget
+ _OBJC_CLASS_$_UAFAssetSetManager
+ _OBJC_IVAR_$_SRDefaultsManager._uafAssetCache
+ _OBJC_IVAR_$_SRDefaultsManager._uafManager
+ _OBJC_IVAR_$_SRDefaultsManager._uafQueue
+ _OBJC_IVAR_$_SRDefaultsManager._uafToken
+ _SRAssetCompatibilityVersion
+ _SRIsManagedByRBS
+ _SRIsManagedByRBS.cold.1
+ _SRIsManagedByRBS.onceToken
+ _SRIsManagedByRBS.sRBSManaged
+ _SRShouldLoadFromUAF
+ _SRShouldLoadFromUAF.cold.1
+ _SRShouldLoadFromUAF.onceToken
+ _SRShouldLoadFromUAF.sUAFEnabled
+ ___25-[SRDefaultsManager init]_block_invoke
+ ___36-[SRDefaultsManager allLoadedAssets]_block_invoke
+ ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke.249
+ ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke.249.cold.1
+ ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.242
+ ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.242.cold.1
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.453
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.453.cold.1
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.453.cold.10
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.453.cold.11
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.453.cold.12
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.453.cold.13
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.453.cold.2
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.453.cold.3
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.453.cold.4
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.453.cold.5
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.453.cold.6
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.453.cold.7
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.453.cold.8
+ ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.453.cold.9
+ ___51-[SRDefaultsManager loadDefaultsFromDefaultAssets:]_block_invoke.503
+ ___59-[SRDefaultsManager loadUAFAssetsForLanguage:fromAssetSet:]_block_invoke
+ ___59-[SRDefaultsManager loadUAFAssetsForLanguage:fromAssetSet:]_block_invoke_2
+ ___61-[SRDefaultsManager filePathsFromUAFForContentType:language:]_block_invoke
+ ___61-[SRDefaultsManager filePathsFromUAFForContentType:language:]_block_invoke.cold.1
+ ___61-[SRDefaultsManager filePathsFromUAFForContentType:language:]_block_invoke.cold.2
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.662
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.664
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.664.cold.1
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_2.663
+ ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_2.663.cold.1
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.550
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.555
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.555.cold.1
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.556
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.565
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.567
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.567.cold.1
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.568
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.551
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.557
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.566
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.566.cold.1
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.569
+ ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.569.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.590
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.590.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.590.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.590.cold.3
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.591
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.593
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.593.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.593.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.595
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.595.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.596
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.596.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.597
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.597.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.597.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.598
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.600
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.600.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.600.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.600.cold.3
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.600.cold.4
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.601
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.601.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.602
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.602.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.603
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.603.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.603.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.604
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.605
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.605.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.606
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.606.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.607
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.607.cold.1
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.607.cold.2
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke_2.599
+ ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke_2.599.cold.1
+ ___82-[SRDefaultsManager assetsFromResourcePath:deliveryType:assetType:language:force:]_block_invoke.523
+ ___82-[SRDefaultsManager assetsFromResourcePath:deliveryType:assetType:language:force:]_block_invoke.523.cold.1
+ ___82-[SRDefaultsManager assetsFromResourcePath:deliveryType:assetType:language:force:]_block_invoke.524
+ ___96-[SRDefaultsManager notifyObserversWithLanguage:bundleVersions:reloadFromCache:uafUpdate:force:]_block_invoke
+ ___96-[SRDefaultsManager notifyObserversWithLanguage:bundleVersions:reloadFromCache:uafUpdate:force:]_block_invoke_2
+ ___96-[SRDefaultsManager notifyObserversWithLanguage:bundleVersions:reloadFromCache:uafUpdate:force:]_block_invoke_3
+ ___96-[SRDefaultsManager notifyObserversWithLanguage:bundleVersions:reloadFromCache:uafUpdate:force:]_block_invoke_4
+ ___SRIsManagedByRBS_block_invoke
+ ___SRShouldLoadFromUAF_block_invoke
+ ___SRShouldLoadFromUAF_block_invoke.cold.1
+ ___block_descriptor_48_e8_32s40s_e35_v32?0"NSString"8"UAFAsset"16^B24ls32l8s40l8
+ ___block_descriptor_58_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e5_v8?0ls32l8s40l8s48l8r64l8s56l8
+ ___block_literal_global.22
+ ___block_literal_global.29
+ ___block_literal_global.446
+ ___block_literal_global.493
+ ___block_literal_global.513
+ ___block_literal_global.81
+ __os_feature_enabled_impl
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$assetNameForContentType:
+ _objc_msgSend$assets
+ _objc_msgSend$attributeWithDomain:name:
+ _objc_msgSend$characterSetWithCharactersInString:
+ _objc_msgSend$clearUAFCaches
+ _objc_msgSend$currentProcess
+ _objc_msgSend$didUpdateDefaultsWithBundleVersions:trial:uafUpdate:
+ _objc_msgSend$filePathsFromUAFForContentType:language:
+ _objc_msgSend$initWithExplanation:target:attributes:
+ _objc_msgSend$invalidateWithError:
+ _objc_msgSend$isManaged
+ _objc_msgSend$loadUAFAssetsForLanguage:fromAssetSet:
+ _objc_msgSend$loadUAFAssetsForLanguages:
+ _objc_msgSend$location
+ _objc_msgSend$notifyObserversWithLanguage:bundleVersions:reloadFromCache:uafUpdate:force:
+ _objc_msgSend$observeAssetSet:queue:handler:
+ _objc_msgSend$rangeOfCharacterFromSet:
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$retrieveAssetSet:usages:
+ _objc_msgSend$sharedManager
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_msgSend$usageDictForLanguage:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _uafAssetSetName_block_invoke.onceToken
- -[SRDefaultsManager notifyObserversWithLanguage:bundleVersions:reloadFromCache:force:]
- -[SRResources didUpdateDefaultsWithBundleVersions:trial:]
- GCC_except_table101
- GCC_except_table103
- GCC_except_table105
- GCC_except_table109
- GCC_except_table111
- GCC_except_table113
- GCC_except_table118
- GCC_except_table126
- GCC_except_table130
- GCC_except_table131
- GCC_except_table132
- GCC_except_table20
- GCC_except_table29
- GCC_except_table31
- GCC_except_table33
- GCC_except_table35
- GCC_except_table37
- GCC_except_table45
- GCC_except_table48
- GCC_except_table50
- GCC_except_table52
- GCC_except_table55
- GCC_except_table74
- GCC_except_table78
- GCC_except_table83
- GCC_except_table84
- GCC_except_table90
- GCC_except_table99
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke.250
- ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke.250.cold.1
- ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.243
- ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.243.cold.1
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.1
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.10
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.11
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.12
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.13
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.2
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.3
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.4
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.5
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.6
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.7
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.8
- ___43+[SRResourcesManager setTrialUpdateHandler]_block_invoke.451.cold.9
- ___51-[SRDefaultsManager loadDefaultsFromDefaultAssets:]_block_invoke.453
- ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.635
- ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.637
- ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke.637.cold.1
- ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_2.636
- ___63-[SRDefaultsManager refreshCacheForLanguages:force:completion:]_block_invoke_2.636.cold.1
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.525
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.530
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.530.cold.1
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.531
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.540
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.542
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke.542.cold.1
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.526
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.532
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.541
- ___68-[SRDefaultsManager requestAssetsForLanguages:removeExisting:force:]_block_invoke_2.541.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.563
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.563.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.563.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.563.cold.3
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.564
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.566
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.566.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.566.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.568
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.568.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.569
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.569.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.570
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.570.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.570.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.571
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.573
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.573.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.573.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.573.cold.3
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.573.cold.4
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.574
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.574.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.575
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.575.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.576
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.576.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.576.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.577
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.578
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.578.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.579
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.579.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.580
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.580.cold.1
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke.580.cold.2
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke_2.572
- ___75-[SRDefaultsManager loadOTAAssetsForLanguage:updateCache:assetTypes:force:]_block_invoke_2.572.cold.1
- ___82-[SRDefaultsManager assetsFromResourcePath:deliveryType:assetType:language:force:]_block_invoke.498
- ___82-[SRDefaultsManager assetsFromResourcePath:deliveryType:assetType:language:force:]_block_invoke.498.cold.1
- ___82-[SRDefaultsManager assetsFromResourcePath:deliveryType:assetType:language:force:]_block_invoke.499
- ___86-[SRDefaultsManager notifyObserversWithLanguage:bundleVersions:reloadFromCache:force:]_block_invoke
- ___86-[SRDefaultsManager notifyObserversWithLanguage:bundleVersions:reloadFromCache:force:]_block_invoke_2
- ___86-[SRDefaultsManager notifyObserversWithLanguage:bundleVersions:reloadFromCache:force:]_block_invoke_3
- ___86-[SRDefaultsManager notifyObserversWithLanguage:bundleVersions:reloadFromCache:force:]_block_invoke_4
- ___block_descriptor_57_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
- ___block_literal_global.444
- ___block_literal_global.47
- ___block_literal_global.491
- ___block_literal_global.511
- ___block_literal_global.72
- _objc_msgSend$didUpdateDefaultsWithBundleVersions:trial:
- _objc_msgSend$notifyObserversWithLanguage:bundleVersions:reloadFromCache:force:
- _sLastLoadedBundleVersion_block_invoke.onceToken
CStrings:
+ "(lazy loading) Acquiring RBSAssertion"
+ "(lazy loading) Failed to invalidate RBSAssertion: %@"
+ "(lazy loading) Released RBSAssertion"
+ "(lazy loading) Retrieved UAF asset set for %@"
+ "(requestAssets) Acquiring RBSAssertion"
+ "(requestAssets) Failed to invalidate RBSAssertion: %@"
+ "(requestAssets) Released RBSAssertion"
+ "(requestAssets) Retrieved UAF asset set for %@"
+ "-_"
+ "Assets update from UAF for resource (%@, %@)"
+ "EnableUAFAssetDelivery"
+ "Fetching from UAF for (%@, %@)"
+ "FinishTaskUninterruptable"
+ "Found cached UAF assets (%@, %@) = %@"
+ "Geo"
+ "Loaded and cached UAF asset (%@, %@) = %@"
+ "QueryParser"
+ "Registered observer for UAF"
+ "Skipping fetching from UAF for (%@, %@)"
+ "SpotlightResources UAF asset loading"
+ "UAF enabled: %d"
+ "Unregistered observer for UAF"
+ "com.apple.campo"
+ "com.apple.common"
+ "com.apple.search.queryparser"
+ "com.apple.search.queryunderstanding.embedding"
+ "com.apple.search.queryunderstanding.geo"
+ "com.apple.spotlightknowledged"
+ "com.apple.spotlightresources.uafLoading"
+ "requestAssets uaf update for %@"
+ "sqp.language"
+ "v32@?0@\"NSString\"8@\"UAFAsset\"16^B24"
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSBundle\""
- "@\"NSDictionary\""
- "@\"NSHashTable\""
- "@\"NSLocale\""
- "@\"NSLocale\"16@0:8"
- "@\"NSMutableData\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSObject\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"SRAssetBundle\""
- "@\"SRAssetBundleVersion\""
- "@\"SRAssetConfiguration\""
- "@\"SRLanguageConfiguration\""
- "@\"SRParameter\""
- "@\"SRTrialConfiguration\""
- "@\"TRIClient\""
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@28@0:8@16I24"
- "@28@0:8B16@20"
- "@28@0:8I16@20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@32@0:8d16@24"
- "@32@0:8q16@24"
- "@36@0:8@16B24B28B32"
- "@36@0:8B16q20@28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24B32B36"
- "@40@0:8@16B24@28B36"
- "@40@0:8@16^q24^@32"
- "@40@0:8@16q24@32"
- "@40@0:8d16q24@32"
- "@40@0:8q16@24@32"
- "@40@0:8q16@24q32"
- "@40@0:8q16q24@32"
- "@48@0:8@16@24q32@40"
- "@52@0:8@16@24@32@40B48"
- "@56@0:8@16@24q32@40@48"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B20@0:8B16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8d16"
- "B24@0:8q16"
- "B28@0:8@16B24"
- "B28@0:8I16@20"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B36@0:8@16@24B32"
- "B48@0:8@16@24@32@40"
- "B56@0:8@16@24@32@40@48"
- "DDSAssetCenterDelegate"
- "I"
- "I16@0:8"
- "JSONObjectWithData:options:error:"
- "NSCopying"
- "NSObject"
- "PlistReader"
- "Q"
- "Q16@0:8"
- "SRAssertion"
- "SRAsset"
- "SRAssetBundle"
- "SRAssetBundleCache"
- "SRAssetBundleCacheEntry"
- "SRAssetBundleQuery"
- "SRAssetBundleVersion"
- "SRAssetCommand"
- "SRAssetConfiguration"
- "SRAssetType"
- "SRDefaultsManager"
- "SRDefaultsManagerDelegate"
- "SRLanguageConfiguration"
- "SRMASandboxExtensionHandler"
- "SRNamespaceType"
- "SRPARSession"
- "SRParameter"
- "SRResources"
- "SRResourcesManager"
- "SRTrialCommand"
- "SRTrialConfiguration"
- "SRTrialParameter"
- "SRXPCConnection"
- "SRXPCListener"
- "SSTrialManager"
- "T#,R"
- "T@\"NSArray\",R,N"
- "T@\"NSBundle\",R,N,V_customBundle"
- "T@\"NSDictionary\",C,N,V_contentTypeMap"
- "T@\"NSDictionary\",C,N,V_deliveryTypeMap"
- "T@\"NSDictionary\",R,N"
- "T@\"NSHashTable\",R,N,V_delegates"
- "T@\"NSLocale\",R,N"
- "T@\"NSLocale\",R,N,V_locale"
- "T@\"NSMutableDictionary\",R,N,V_queryEntries"
- "T@\"NSMutableSet\",R,N,V_cachedOTALanguages"
- "T@\"NSMutableSet\",R,N,V_requestedOTALanguages"
- "T@\"NSObject\",R,N,V_value"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_ddsQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_defaultsQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_delegatesQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_notifyQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_notifyQueueNonBlocking"
- "T@\"NSSet\",C,N,V_deliveryTypes"
- "T@\"NSSet\",C,N,V_parameterNames"
- "T@\"NSString\",&,N,V_irisName"
- "T@\"NSString\",&,V_experimentId"
- "T@\"NSString\",&,V_experimentNamespaceId"
- "T@\"NSString\",&,V_experimentTreatmentId"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_assetType"
- "T@\"NSString\",C,N,V_namespaceId"
- "T@\"NSString\",C,N,V_namespaceName"
- "T@\"NSString\",C,N,V_xpcName"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_assetType"
- "T@\"NSString\",R,N,V_client"
- "T@\"NSString\",R,N,V_contentType"
- "T@\"NSString\",R,N,V_deliveryType"
- "T@\"NSString\",R,N,V_experimentId"
- "T@\"NSString\",R,N,V_language"
- "T@\"NSString\",R,N,V_localeIdentifier"
- "T@\"NSString\",R,N,V_name"
- "T@\"NSString\",R,N,V_namespaceId"
- "T@\"NSString\",R,N,V_path"
- "T@\"NSString\",R,N,V_rolloutId"
- "T@\"NSString\",R,N,V_treatmentId"
- "T@\"NSString\",R,N,V_version"
- "T@\"NSString\",R,V_assetType"
- "T@\"SRAssetBundleVersion\",R,N,V_bundleVersion"
- "T@\"SRParameter\",R,N,V_parameter"
- "T@?,C,N,V_parameterUpdates"
- "TB,N,V_hasTestAssets"
- "TB,N,V_hasValueFromTrial"
- "TB,N,V_loaded"
- "TB,N,V_wasLoadedSinceLaunch"
- "TB,R,N"
- "TB,R,N,V_isResult"
- "TB,V_autoUpdatingLocale"
- "TI,V_experimentVersion"
- "TQ,R"
- "Ti,R,N,V_experimentDeploymentId"
- "Ti,R,N,V_rolloutDeploymentId"
- "Ti,V_experimentDeploymentId"
- "Tq,N,V_compatibilityVersion"
- "Tq,R,N,V_assetType"
- "Tq,R,N,V_deliveryType"
- "Tq,R,N,V_flag"
- "Tq,R,N,V_type"
- "URLByDeletingLastPathComponent"
- "URLWithString:"
- "UTF8String"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_assertionID"
- "_assetConfig"
- "_assetType"
- "_assets"
- "_autoUpdatingLocale"
- "_bundleVersion"
- "_bundleVersions"
- "_cache"
- "_cachedOTALanguages"
- "_cachedValuesForFactor"
- "_client"
- "_clientMap"
- "_compatibilityVersion"
- "_contentType"
- "_contentTypeMap"
- "_contents"
- "_contentsLock"
- "_customBundle"
- "_ddsQueue"
- "_defaultsQueue"
- "_delegates"
- "_delegatesQueue"
- "_deliveryType"
- "_deliveryTypeMap"
- "_deliveryTypes"
- "_experimentDeploymentId"
- "_experimentId"
- "_experimentNamespaceId"
- "_experimentTreatmentId"
- "_experimentVersion"
- "_feedbackData"
- "_fetchedLanguagesOTA"
- "_fetchedLanguagesSystem"
- "_fetchedRootOTA"
- "_fetchedRootSystem"
- "_flag"
- "_forceLoad"
- "_hasActiveExperiment"
- "_hasOverride"
- "_hasRollout"
- "_hasTestAssets"
- "_hasUpdates"
- "_hasValueFromTrial"
- "_ignoreOTAEmbeddings"
- "_irisName"
- "_isResult"
- "_isSR"
- "_langConfig"
- "_language"
- "_liveAssetBundle"
- "_loadAssets:shouldUpdate:merge:"
- "_loaded"
- "_locale"
- "_localeIdentifier"
- "_name"
- "_namespaceDescription"
- "_namespaceId"
- "_namespaceMap"
- "_namespaceName"
- "_noOTA"
- "_notifyQueue"
- "_notifyQueueNonBlocking"
- "_options"
- "_otherParameters"
- "_overrides"
- "_parameter"
- "_parameterMap"
- "_parameterNames"
- "_parameterUpdates"
- "_parameters"
- "_path"
- "_paths"
- "_plist"
- "_properties"
- "_queryEntries"
- "_queue"
- "_requestedOTALanguages"
- "_requiredAssetsContentVersion"
- "_rolloutDeploymentId"
- "_rolloutId"
- "_sandboxExtensionHandlers"
- "_spid"
- "_supportedLanguageMap"
- "_treatmentId"
- "_trialClient"
- "_trialConfig"
- "_type"
- "_unloadAssetsForLocale:"
- "_value"
- "_version"
- "_wasLoadedSinceLaunch"
- "_xpcName"
- "addAllowedValue:forKey:"
- "addAssertionForAssetsWithQuery:policy:assertionID:clientID:"
- "addFetchForLanguage:ota:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:selector:name:object:"
- "addParameterName:"
- "addQueryEntriesForLanguage:assetType:deliveryTypes:"
- "addUpdateHandlerForNamespaceName:usingBlock:"
- "allKeys"
- "allLoadedAssets"
- "allObjects"
- "allValues"
- "appendData:"
- "appendFeedbackData:"
- "appendFormat:"
- "appendString:"
- "array"
- "arrayWithObjects:count:"
- "assertionID"
- "assertionIDsForClientID:assetType:"
- "assertionsDump"
- "assetBundleForLocale:client:force:noOTA:"
- "assetConfig"
- "assetConfigDump"
- "assetPathsForContentType:"
- "assetType"
- "assetTypeString"
- "assetTypes"
- "assetWithLocaleIdentifier:contentType:deliveryType:path:"
- "assetWithLocaleIdentifier:contentType:deliveryType:resourceRoot:pathNames:"
- "assetsForQuery:error:"
- "assetsFromResourcePath:deliveryType:assetType:language:force:"
- "assetsWithContentType:"
- "attributeFilter"
- "attributes"
- "autoUpdatingLocale"
- "autorelease"
- "boolForKey:"
- "boolNil"
- "boolNo"
- "boolValue"
- "boolYes"
- "booleanForKey:"
- "booleanForKey:didFailWithError:"
- "booleanValue"
- "bundleIdentifier"
- "bundleVersion"
- "bundleWithIdentifier:"
- "bundleWithPath:"
- "bytes"
- "cacheFilePath"
- "cachedOTALanguages"
- "capitalizedString"
- "class"
- "clear"
- "client"
- "clientWithIdentifier:"
- "clientsForNamespace:"
- "code"
- "compare:"
- "compatibilityVersion"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "configuration"
- "conformsToProtocol:"
- "connection"
- "containsObject:"
- "containsString:"
- "contentNames"
- "contentPaths"
- "contentType"
- "contentTypeMap"
- "contentTypes"
- "contentTypesForClient:"
- "contentsOfDirectoryAtPath:error:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countryCode"
- "createFileAtPath:contents:attributes:"
- "currentAssetTypes"
- "currentExperimentTrialManager"
- "currentLocale"
- "currentNamespaceDescription"
- "currentNamespaces"
- "currentNamespacesForClient:"
- "currentTrialManagerForClient:"
- "customBundle"
- "d24@0:8@16"
- "d32@0:8@16^@24"
- "data"
- "dataUsingEncoding:"
- "dataWithContentsOfFile:"
- "ddsQueue"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "defaultManager"
- "defaultParameterWithType:value:name:"
- "defaultProperties"
- "defaultValueWithKey:"
- "defaultsQueue"
- "delegates"
- "delegatesQueue"
- "deliveryType"
- "deliveryTypeMap"
- "deliveryTypeString"
- "deliveryTypes"
- "deploymentId"
- "description"
- "dictionary"
- "dictionaryRepresentation"
- "dictionaryWithContentsOfFile:"
- "dictionaryWithContentsOfURL:"
- "dictionaryWithContentsOfURL:error:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "didAllNamespacesLoadForClient:"
- "didFetchForLanguage:ota:"
- "didUpdateAssetsWithType:"
- "didUpdateDefaultsWithBundleVersions:trial:"
- "didUpdateTrialNamespace:"
- "domain"
- "doubleForKey:"
- "doubleForKey:didFailWithError:"
- "doubleMin"
- "doubleNil"
- "doubleValue"
- "dumpCache"
- "dumpParameterList:"
- "enumerateEntriesForLanguage:block:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
- "errorWithDomain:code:userInfo:"
- "executeBlock:wait:"
- "experimentDeploymentId"
- "experimentId"
- "experimentIdentifiersWithNamespaceName:"
- "experimentNamespaceId"
- "experimentTreatmentId"
- "experimentVersion"
- "factorLevelsWithNamespaceName:"
- "fetchAllParametersForLanguages:"
- "fetchAssetUpdateStatusForQuery:callback:"
- "fetchBooleanParameter:"
- "fetchDoubleParameter:"
- "fetchFilePathParameter:"
- "fetchLongParameter:"
- "fetchOverrideList"
- "fetchParameter:checkForPositive:"
- "fetchParameterList"
- "fetchStringParameter:"
- "fetchUserDefaults"
- "fetchedLanguages:"
- "fileExistsAtPath:"
- "fileExistsAtPath:isDirectory:"
- "filePathArrayForKey:"
- "filePathArrayForKey:didFailWithError:"
- "filePathForKey:"
- "filePathForKey:didFailWithError:"
- "filePathNil"
- "fileURLWithPath:"
- "fileURLWithPath:isDirectory:"
- "fileValue"
- "firstObject"
- "flag"
- "flushCacheToFile"
- "getBooleanValue"
- "getDoubleValue"
- "getFactorDictionary"
- "getFeedbackData"
- "getFilePathNameValue"
- "getFilePathValue"
- "getLevelForFactor:"
- "getLongValue"
- "getStringValue"
- "getTTRLogs"
- "getTTRLogsForClient:"
- "getTrialExperimentDeploymentId"
- "getTrialExperimentId"
- "getTrialNamespaceId"
- "getTrialRolloutDeploymentId"
- "getTrialRolloutId"
- "getTrialTreatmentId"
- "handleAssetsCommand:"
- "handleCommand:info:reply:error:"
- "handleMessage:error:"
- "handleReply:completion:"
- "hasActiveExperiment"
- "hasActiveRollout"
- "hasOverride"
- "hasPrefix:"
- "hasSuffix:"
- "hasTestAssets"
- "hasUpdates"
- "hasValueFromTrial"
- "hash"
- "i16@0:8"
- "identifier"
- "infoDictionary"
- "init"
- "initWithArray:"
- "initWithAssertionID:"
- "initWithAssetType:"
- "initWithAssetType:filter:"
- "initWithAssetType:language:deliveryType:"
- "initWithBool:"
- "initWithBoolean:flags:name:"
- "initWithBundleVersion:"
- "initWithCapacity:"
- "initWithClient:locale:options:"
- "initWithDomain:code:userInfo:"
- "initWithDouble:"
- "initWithDouble:flags:name:"
- "initWithFilePath:flags:name:"
- "initWithFormat:"
- "initWithId:userAgent:factory:"
- "initWithLocale:bundleVersions:"
- "initWithLocaleIdentifier:"
- "initWithLocaleIdentifier:contentType:deliveryType:paths:"
- "initWithLong:"
- "initWithLong:flags:name:"
- "initWithMachServiceName:"
- "initWithNameSpace:forClient:"
- "initWithOptions:"
- "initWithParameter:"
- "initWithPlist:"
- "initWithString:"
- "initWithString:flags:name:"
- "initWithSuiteName:"
- "initWithType:flags:name:"
- "initWithUUIDString:"
- "initWithXPCObject:isResult:"
- "initWithXPCServiceName:assertionStorageDirectoryURL:"
- "initialize"
- "integerValue"
- "irisName"
- "isBool"
- "isDouble"
- "isEqual:"
- "isEqualToSet:"
- "isEqualToString:"
- "isFilePath"
- "isKindOfClass:"
- "isLong"
- "isMemberOfClass:"
- "isNamespaceLoaded:"
- "isNil"
- "isPositiveLong"
- "isProxy"
- "isResult"
- "isResultNone"
- "isString"
- "isSupportedLanguage:deliveryType:"
- "isValidNamespace:forClient:"
- "langConfig"
- "langConfigDump"
- "language"
- "languageCode"
- "lastLoadedBundleVersion"
- "lastPathComponent"
- "length"
- "level"
- "loadAllParameters"
- "loadAllParametersForClient:"
- "loadAllParametersForClient:locale:"
- "loadAllParametersForClient:locale:options:"
- "loadAllParametersForClient:locales:options:"
- "loadAssetsForLanguage:reload:force:noOTA:"
- "loadAssetsWithContentType:contentName:contentPath:"
- "loadCacheFromFile"
- "loadDataSource:force:"
- "loadDefaultsForLocale:reload:force:noOTA:"
- "loadDefaultsFromDefaultAssets:"
- "loadFactorsAtPath:namespaceId:"
- "loadFailedForLanguage:assetType:deliveryType:"
- "loadInternalAssetsForLanguage:assetTypes:"
- "loadNamespace:"
- "loadOTAAssetsForLanguage:updateCache:assetTypes:force:"
- "loadSupportedLanguages:"
- "loadSystemAssetsForLanguage:assetTypes:"
- "loadTestAssetsForLanguage:assetTypes:"
- "loadWithUpdateHandler:"
- "localURL"
- "locale"
- "localeIdentifier"
- "localeWithLocaleIdentifier:"
- "logForTrigger:queryID:"
- "longForKey:"
- "longForKey:didFailWithError:"
- "longNil"
- "longValue"
- "longZero"
- "lowercaseString"
- "mainBundle"
- "makeNil"
- "makeResultNone"
- "makeResultWithBundleVersion:path:loaded:"
- "mergeWithAsset:"
- "mutableCopy"
- "name"
- "namespaceDescription"
- "namespaceNameFromId:"
- "namespaceTypes"
- "namespaceTypesForClient:"
- "namespacesForClient:"
- "nilParameterWithType:"
- "notifyObserversWithLanguage:bundleVersions:reloadFromCache:force:"
- "notifyQueue"
- "notifyQueueNonBlocking"
- "numberFromString:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithLong:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKey:didFailWithError:"
- "objectForKey:withType:didFailWithError:"
- "objectForKeyedSubscript:"
- "onDevice"
- "otaBundleVersion"
- "overrideFactor:client:type:value:"
- "parameter"
- "parameterNames"
- "parameterTypeFromString:"
- "parameterTypeFromTypeString:"
- "parameterUpdates"
- "parameterWithBoolean:name:"
- "parameterWithDouble:name:"
- "parameterWithFilePath:name:"
- "parameterWithLong:name:"
- "parameterWithString:name:"
- "parameterWithValue:name:typeString:"
- "parametersOfContentTypeWithName:client:"
- "parametersOfNamespaceWithName:"
- "parametersOfNamespaceWithName:client:"
- "parsecEnabled"
- "pathForResource:ofType:"
- "pathWithName:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "plist"
- "plistReaderWithResourcePath:"
- "preferredLanguages"
- "processInfo"
- "processName"
- "q16@0:8"
- "q24@0:8@16"
- "q32@0:8@16^@24"
- "queryCache:loading:"
- "queryEntries"
- "queryServerCache:force:completion:"
- "refresh"
- "refreshCacheForLanguages:force:completion:"
- "refreshTrackingId"
- "refreshTrial"
- "refreshTrialForClient:"
- "registerDelegate:"
- "release"
- "removeAllObjects"
- "removeAssertionWithIdentifier:assetType:"
- "removeAssetBundleWithAssetType:language:deliveryType:"
- "removeDefaults"
- "removeFetchForLanguage:ota:"
- "removeKey:"
- "removeObject:"
- "removeObjectForKey:"
- "removePersistentDomainForName:"
- "reportEvent:"
- "requestAssetsForLanguages:removeExisting:force:"
- "requestCatalogUpdate"
- "requestedOTALanguages"
- "requiredAssetsContentVersion"
- "resetStandardUserDefaults"
- "resolveMultipleSpotlightExperiments"
- "resourceBundle"
- "resourcePath"
- "resourcesForClient:locale:options:"
- "resourcesForClient:options:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "rolloutDeploymentId"
- "rolloutId"
- "rolloutIdentifiersWithNamespaceName:"
- "runAssetCommand:"
- "runTrialCommand:"
- "scriptCode"
- "self"
- "sendCommand:info:sync:completion:"
- "sessionWithConfiguration:"
- "set"
- "setAssetType:"
- "setAssetTypesForDelegates:"
- "setAutoUpdatingLocale:"
- "setCachedOnly:"
- "setCodepathId:"
- "setCompatabilityVersion:forAssetType:"
- "setCompatibilityVersion:"
- "setContentTypeMap:"
- "setDefaultWithKey:value:"
- "setDeliveryTypeMap:"
- "setDeliveryTypes:"
- "setExperimentDeploymentId:"
- "setExperimentId:"
- "setExperimentNamespaceId:"
- "setExperimentTreatmentId:"
- "setExperimentVersion:"
- "setFlag:"
- "setHasTestAssets:"
- "setHasValueFromTrial:"
- "setInstalledOnly:"
- "setIrisName:"
- "setLatestOnly:"
- "setLoaded:"
- "setLocalOnly:"
- "setLocale:"
- "setName:"
- "setNamespaceId:"
- "setNamespaceName:"
- "setNumber:"
- "setNumberStyle:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setParameterName:namespaceId:"
- "setParameterNames:"
- "setParameterUpdates:"
- "setProperties:client:"
- "setQueryId:"
- "setString:"
- "setTrialOverridePath"
- "setTrialUpdateHandler"
- "setTrialUpdateHandler:"
- "setType:"
- "setValue:forKey:"
- "setVersionWithValue:"
- "setWasLoadedSinceLaunch:"
- "setWithArray:"
- "setXPCServiceName:forAssetType:"
- "setXpcName:"
- "sharedConnection"
- "sharedDefaultsManager"
- "sharedInstance"
- "sharedInstanceWithConfiguration:"
- "sharedResourcesManager"
- "sharedSpotlightKnowledgeTrialClient"
- "sharedSpotlightKnowledgeTrialManager"
- "sharedSpotlightMailTrialManager"
- "sharedSpotlightModelTrialManager"
- "sharedSpotlightPolicyTrialManager"
- "sharedSpotlightRankingTrialManager"
- "sharedSpotlightTrialClient"
- "sharedSpotlightUITrialManager"
- "shouldUpdateForBundleVersions:"
- "spotlightResourcesPARSessionForClient:flags:"
- "spotlightResourcesPARSessionMail"
- "spotlightResourcesPARSessionSpotlight"
- "standardUserDefaults"
- "stringByDeletingLastPathComponent"
- "stringByDeletingPathExtension"
- "stringForKey:"
- "stringForKey:didFailWithError:"
- "stringNil"
- "stringValue"
- "stringWithFormat:"
- "stringWithString:"
- "stringWithUTF8String:"
- "substringFromIndex:"
- "substringToIndex:"
- "substringWithRange:"
- "superclass"
- "treatmentId"
- "trialConfigDump"
- "trialDidReceiveAsset:forQuery:"
- "trialDidStopForQuery:"
- "trialManagerForNamespaceId:"
- "trialManagerForNamespaceName:"
- "trialOverrideList"
- "trialParameterList"
- "trialSpotlightRolloutID"
- "trialSpotlightTreatmentID"
- "type"
- "typeString"
- "typeStringFromParameterType:"
- "unloadDefaultsForLocale:"
- "unregisterDelegate:"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "updateAssetForQuery:callback:"
- "updateCacheWithResults:loading:"
- "updateDefaultParameter:withValue:"
- "updateFetchedLanguages:ota:"
- "updateLocale"
- "updateParameter:inNamespace:withValue:"
- "updateWithBoolean:"
- "updateWithDouble:"
- "updateWithFilePath:"
- "updateWithLong:"
- "updateWithNewOptions:"
- "updateWithString:"
- "uppercaseString"
- "upsertAssetBundleWithAssetType:language:deliveryType:bundleVersion:path:"
- "usageInformationForSubcommand:"
- "userDefaults"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8i16"
- "v24@0:8@\"DDSTrialQuery\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8q16"
- "v28@0:8@\"NSDictionary\"16B24"
- "v28@0:8@16B24"
- "v28@0:8@?16B24"
- "v32@0:8@\"DDSTrialAsset\"16@\"DDSTrialQuery\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16B24B28"
- "v32@0:8@16^@24"
- "v32@0:8@16q24"
- "v36@0:8@16B24@?28"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24B32B36"
- "v44@0:8Q16@24B32@?36"
- "v48@0:8Q16@24@32^@40"
- "value"
- "version"
- "wasLoadedSinceLaunch"
- "weakObjectsHashTable"
- "writeToURL:error:"
- "xpcName"
- "xpcObject"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
