## SpotlightResources

> `/System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources`

```diff

-2374.0.1.0.0
-  __TEXT.__text: 0x22e44
-  __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__objc_methlist: 0x1420
-  __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0x968
-  __TEXT.__cstring: 0x1743
-  __TEXT.__oslogstring: 0x1ab9
-  __TEXT.__unwind_info: 0x748
-  __TEXT.__objc_classname: 0x1c9
-  __TEXT.__objc_methname: 0x326b
-  __TEXT.__objc_methtype: 0x595
-  __TEXT.__objc_stubs: 0x3340
-  __DATA_CONST.__got: 0x230
-  __DATA_CONST.__const: 0x958
-  __DATA_CONST.__objc_classlist: 0xb0
+2381.0.1.0.0
+  __TEXT.__text: 0x25ddc
+  __TEXT.__auth_stubs: 0x6f0
+  __TEXT.__objc_methlist: 0x14a8
+  __TEXT.__const: 0xe8
+  __TEXT.__gcc_except_tab: 0xbac
+  __TEXT.__cstring: 0x2340
+  __TEXT.__oslogstring: 0x1cbf
+  __TEXT.__unwind_info: 0x7d0
+  __TEXT.__objc_classname: 0x1ea
+  __TEXT.__objc_methname: 0x3381
+  __TEXT.__objc_methtype: 0x5a4
+  __TEXT.__objc_stubs: 0x3520
+  __DATA_CONST.__got: 0x238
+  __DATA_CONST.__const: 0x980
+  __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf40
+  __DATA_CONST.__objc_selrefs: 0xfa8
   __DATA_CONST.__objc_superrefs: 0x98
-  __DATA_CONST.__objc_arraydata: 0x990
-  __AUTH_CONST.__auth_got: 0x380
+  __DATA_CONST.__objc_arraydata: 0x9a0
+  __AUTH_CONST.__auth_got: 0x388
   __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x3ea0
-  __AUTH_CONST.__objc_const: 0x1f68
-  __AUTH_CONST.__objc_dictobj: 0xa0
+  __AUTH_CONST.__cfstring: 0x4820
+  __AUTH_CONST.__objc_const: 0x20a8
+  __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x17c
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x180
   __DATA.__data: 0x180
-  __DATA.__bss: 0x70
+  __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0x690
   __DATA_DIRTY.__data: 0x258
-  __DATA_DIRTY.__bss: 0x2a8
+  __DATA_DIRTY.__bss: 0x2a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 49DB50F9-D9F0-39A6-A3C7-EC4288BAFF52
-  Functions: 698
-  Symbols:   2514
-  CStrings:  1977
+  UUID: A6A34F02-1F93-38E3-B121-21911DC3D896
+  Functions: 732
+  Symbols:   2630
+  CStrings:  2165
 
Symbols:
+ +[SRAssetCommand runAssetCommand:]
+ +[SRAssetCommand usageInformationForSubcommand:]
+ +[SRResourcesManager trialOverrideList]
+ +[SRResourcesManager trialParameterList]
+ +[SRTrialCommand runTrialCommand:]
+ +[SRTrialCommand usageInformationForSubcommand:]
+ +[SSTrialManager trialManagerForNamespaceId:]
+ -[SRDefaultsManager assertionsDump]
+ -[SRDefaultsManager langConfigDump]
+ -[SRDefaultsManager langConfig]
+ -[SRDefaultsManager requestAssetsForLanguages:removeExisting:]
+ -[SRResources didUpdateDefaultsWithBundleVersions:trial:]
+ -[SRResourcesManager loadDataSource:force:]
+ GCC_except_table11
+ GCC_except_table112
+ GCC_except_table118
+ GCC_except_table119
+ GCC_except_table12
+ GCC_except_table120
+ GCC_except_table14
+ GCC_except_table6
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$_SRAssetCommand
+ _OBJC_CLASS_$_SRTrialCommand
+ _OBJC_IVAR_$_SRAssetBundle._contentsLock
+ _OBJC_METACLASS_$_SRAssetCommand
+ _OBJC_METACLASS_$_SRTrialCommand
+ _SRAreAssetsAvailableForLocale
+ _SRIsAssetAvailable
+ _SRIsAssetAvailable.cold.1
+ _SRIsAssetAvailable.cold.2
+ _SRIsAssetAvailable.cold.3
+ _SRIsAssetAvailable.cold.4
+ _SRLogCategoryTool
+ _SRLogCategoryTool.cold.1
+ _SRLogCategoryTool.onceToken
+ _SRLogCategoryTool.toolLog
+ __OBJC_$_CLASS_METHODS_SRAssetCommand
+ __OBJC_$_CLASS_METHODS_SRTrialCommand
+ __OBJC_CLASS_RO_$_SRAssetCommand
+ __OBJC_CLASS_RO_$_SRTrialCommand
+ __OBJC_METACLASS_RO_$_SRAssetCommand
+ __OBJC_METACLASS_RO_$_SRTrialCommand
+ ___34+[SRAssetCommand runAssetCommand:]_block_invoke
+ ___34+[SRTrialCommand runTrialCommand:]_block_invoke
+ ___34+[SRTrialCommand runTrialCommand:]_block_invoke_2
+ ___34+[SRTrialCommand runTrialCommand:]_block_invoke_3
+ ___34+[SRTrialCommand runTrialCommand:]_block_invoke_4
+ ___35-[SRDefaultsManager assertionsDump]_block_invoke
+ ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke.242
+ ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke.242.cold.1
+ ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.235
+ ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.235.cold.1
+ ___51-[SRDefaultsManager loadDefaultsFromDefaultAssets:]_block_invoke.395
+ ___57-[SRDefaultsManager refreshCacheForLanguages:completion:]_block_invoke_5.cold.1
+ ___62-[SRDefaultsManager requestAssetsForLanguages:removeExisting:]_block_invoke
+ ___62-[SRDefaultsManager requestAssetsForLanguages:removeExisting:]_block_invoke.414
+ ___62-[SRDefaultsManager requestAssetsForLanguages:removeExisting:]_block_invoke.414.cold.1
+ ___62-[SRDefaultsManager requestAssetsForLanguages:removeExisting:]_block_invoke.424
+ ___62-[SRDefaultsManager requestAssetsForLanguages:removeExisting:]_block_invoke.424.cold.1
+ ___62-[SRDefaultsManager requestAssetsForLanguages:removeExisting:]_block_invoke.425
+ ___62-[SRDefaultsManager requestAssetsForLanguages:removeExisting:]_block_invoke.434
+ ___62-[SRDefaultsManager requestAssetsForLanguages:removeExisting:]_block_invoke.434.cold.1
+ ___62-[SRDefaultsManager requestAssetsForLanguages:removeExisting:]_block_invoke_2
+ ___62-[SRDefaultsManager requestAssetsForLanguages:removeExisting:]_block_invoke_2.415
+ ___62-[SRDefaultsManager requestAssetsForLanguages:removeExisting:]_block_invoke_2.426
+ ___62-[SRDefaultsManager requestAssetsForLanguages:removeExisting:]_block_invoke_3
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.446.cold.3
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.446.cold.4
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.447
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.449
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.449.cold.1
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.449.cold.2
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.453
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.453.cold.1
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.457
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.457.cold.1
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.457.cold.2
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.457.cold.3
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.462
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.464
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.464.cold.1
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.452
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.452.cold.1
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.456
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.456.cold.1
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.463
+ ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.463.cold.1
+ ___SRLogCategoryTool_block_invoke
+ ___block_descriptor_48_e8_32s40r_e25_v32?0"NSString"816^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e38_v32?0"NSString"8"SRParameter"16^B24ls32l8r40l8
+ ___block_descriptor_57_e8_32s40r48w_e5_v8?0lw48l8r40l8s32l8
+ ___block_literal_global.15
+ ___block_literal_global.417
+ ___block_literal_global.501
+ _deliveryTypeFromLowerCaseString
+ _deliveryTypeFromLowerCaseString.cold.1
+ _getAssetBundleInfo
+ _getAssetBundleInfo.cold.1
+ _getAssetBundleInfo.cold.2
+ _getAssetBundleInfo.cold.3
+ _getAssetBundleInfo.cold.4
+ _getAssetBundleInfo.cold.5
+ _getAssetBundleInfo.cold.6
+ _languageFromLowerCaseString
+ _languageFromLowerCaseString.cold.1
+ _objc_msgSend$assertionsDump
+ _objc_msgSend$capitalizedString
+ _objc_msgSend$didUpdateDefaultsWithBundleVersions:trial:
+ _objc_msgSend$initWithUUIDString:
+ _objc_msgSend$isEqual:
+ _objc_msgSend$langConfig
+ _objc_msgSend$langConfigDump
+ _objc_msgSend$loadDataSource:force:
+ _objc_msgSend$logForTrigger:queryID:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$overrideFactor:client:type:value:
+ _objc_msgSend$preferredLanguages
+ _objc_msgSend$requestAssetsForLanguages:removeExisting:
+ _objc_msgSend$resourcesForClient:options:
+ _objc_msgSend$substringWithRange:
+ _objc_msgSend$trialManagerForNamespaceId:
+ _objc_msgSend$trialOverrideList
+ _objc_msgSend$trialParameterList
+ _objc_msgSend$usageInformationForSubcommand:
+ _objc_release_x3
- +[SRResourcesManager fetchOverrideList].cold.1
- -[SRDefaultsManager requestAssetsForLanguages:]
- -[SRResources didUpdateDefaultsWithLanguage:bundleVersions:trial:]
- -[SRResourcesManager loadDataSource:]
- GCC_except_table111
- GCC_except_table115
- GCC_except_table116
- ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke.240
- ___38-[SRAssetBundleCache flushCacheToFile]_block_invoke.240.cold.1
- ___39+[SRResourcesManager fetchOverrideList]_block_invoke
- ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.233
- ___39-[SRAssetBundleCache loadCacheFromFile]_block_invoke.233.cold.1
- ___47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke
- ___47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke.411
- ___47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke.411.cold.1
- ___47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke.421
- ___47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke.421.cold.1
- ___47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke.422
- ___47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke.431
- ___47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke.431.cold.1
- ___47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke_2
- ___47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke_2.412
- ___47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke_2.423
- ___47-[SRDefaultsManager requestAssetsForLanguages:]_block_invoke_3
- ___51-[SRDefaultsManager loadDefaultsFromDefaultAssets:]_block_invoke.392
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.443
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.443.cold.1
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.443.cold.2
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.443.cold.3
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.443.cold.4
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.444
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.448
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.450
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.450.cold.1
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.451.cold.1
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.451.cold.2
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.452
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.454.cold.3
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.456
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke.458.cold.1
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.449
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.449.cold.1
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.453
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.453.cold.1
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.457
- ___70-[SRDefaultsManager loadOTAAssetsForLanguage:reload:assetTypes:force:]_block_invoke_2.457.cold.1
- ___block_descriptor_56_e8_32s40r48w_e5_v8?0lw48l8r40l8s32l8
- ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_literal_global.414
- ___block_literal_global.484
- ___block_literal_global.503
- _fetchOverrideList.overridesPlistOnceToken
- _objc_msgSend$didUpdateDefaultsWithLanguage:bundleVersions:trial:
- _objc_msgSend$lastObject
- _objc_msgSend$loadDataSource:
- _objc_msgSend$requestAssetsForLanguages:
CStrings:
+ "\t\t332 (SPOTLIGHT_BLENDING_MODEL)\n"
+ "\t\t333 (SPOTLIGHT_UI)\n"
+ "\t\t334 (SPOTLIGHT_RANKING_RULES)\n"
+ "\t\t335 (SPOTLIGHT_RANKING_POLICY)\n"
+ "\t\t336 (SPOTLIGHT_KNOWLEDGE_BEHAVIOR)\n"
+ "\t\t337 (SPOTLIGHT_MAIL_APP)\n"
+ "\tdeliveryType: Required, Optional, Delta, OptionalTest, or DeltaTest\n"
+ "\tkey: path, compatibilityversion, contentversion, or bundleversion; anything else will dump all MobileAsset properties\n"
+ "\tnamespaceID:\n"
+ "\n"
+ "\n%@\n"
+ "\n%@ OTA assets for %@.\n"
+ "\nAsset bundle could not be found or was not cached.\n"
+ "\nFactor %@ not found.\n"
+ "\nInvalid namespaceID %@\n"
+ "\nInvoked log trigger logic for (%@, %llu, %@); check feedback stream with 'parsec_tool feedback --dump --pretty'.\n"
+ "\nLoaded namespace %@.\n"
+ "\nOverride for factor %@ %@.\n"
+ "\nRemoved any DDS assertions added by searchutil -c assets:load.\n"
+ "%@-Override"
+ "Assets update for resource (%p, %@, %@)"
+ "Bundle Version"
+ "Compatibility Version"
+ "Content Version"
+ "Deployment ID"
+ "Experiment ID"
+ "Force-loaded"
+ "Kicked off loading of"
+ "MobileAsset Properties"
+ "No asset for (%@, %@)"
+ "Non-OTA"
+ "OTA"
+ "Rollout ID"
+ "SRAssetCommand"
+ "SRTrialCommand"
+ "Set bundle version %@"
+ "Set compatibility version %@"
+ "Set content version %@"
+ "Set path %@"
+ "Tool"
+ "Treatment ID"
+ "Trial update for resource (%p, %@, %@)"
+ "TriggerLogging"
+ "Yes asset for (%@, %@)"
+ "_ContentVersion"
+ "_contentsLock"
+ "assertions"
+ "assertionsDump"
+ "assetBundleInfo %@"
+ "bundleversion"
+ "cache"
+ "capitalizedString"
+ "compatibilityversion"
+ "config"
+ "content"
+ "contentversion"
+ "defaults"
+ "deliveryTypeFromLowerCaseString %@ = 0x%lx"
+ "delta"
+ "didUpdateDefaultsWithBundleVersions:trial:"
+ "dump"
+ "experiment"
+ "failed"
+ "fetch"
+ "force"
+ "getAssetBundleInfo(%@, %@) = (%d, %@, %@)"
+ "getAssetBundleInfo(%@, %@) failed to get path"
+ "getAssetBundleInfo(%@, %@) failed to get resource bundle"
+ "getAssetBundleInfo(%@, %@, %d)"
+ "initWithUUIDString:"
+ "langConfig"
+ "langConfigDump"
+ "languageFromLowerCaseString %@ = %@"
+ "load"
+ "loadDataSource:force:"
+ "loaded"
+ "locales"
+ "namespace"
+ "numberWithInt:"
+ "optional"
+ "optionaltest"
+ "override"
+ "preferredLanguages"
+ "requestAssetsForLanguages:removeExisting:"
+ "required"
+ "reset"
+ "runAssetCommand:"
+ "runTrialCommand:"
+ "searchutil -c asset:<subcommand>[:options]\n\tsubcommands: dump, bundle, content, load, reset\n"
+ "searchutil -c asset:bundle:<deliveryType>:<language>:<key>\n\tDump information about an asset bundle on device.\n"
+ "searchutil -c asset:content:<contentType>:<language>\n\tDump all loaded assets for a content type and language.\n"
+ "searchutil -c asset:dump:assertions\n\tDump DDS assertions currently held by SpotlightResources.\n"
+ "searchutil -c asset:dump:cache\n\tDump %@'s OTA asset bundle cache.\n"
+ "searchutil -c asset:dump:config\n\tDump asset configuration loaded from RequiredAsset_root.bundle.\n"
+ "searchutil -c asset:dump:defaults\n\tDump user defaults used internally by SpotlightResources framework.\n"
+ "searchutil -c asset:dump:loaded\n\tDump all assets loaded by %@.\n"
+ "searchutil -c asset:dump:locales\n\tDump asset locales that SpotlightResources knows to load assets for.\n"
+ "searchutil -c asset:load[:force]:<language>\n\tRequests a specified asset bundle to be loaded/downloaded.\n"
+ "searchutil -c asset:reset\n\tSpotlightResources will no longer hold on to assertions for requests from 'searchutil -c asset:load'.\n"
+ "searchutil -c trial:<subcommand>[:options]\n\nsubcommands: factor, namespace, trigger\n\n"
+ "searchutil -c trial:factor:fetch:<factorName>\n\tDump all trial factor values for factors with the name <factorName>.\n"
+ "searchutil -c trial:factor:override:<factorName>:<client>:<type>:<value>\n\tOverride factor for <client> and <factorName> with (<type>, <value>)\n"
+ "searchutil -c trial:namespace:experiment:<namespaceID>\n\tDump any trial experiment metadata for namespace <namespaceID>.\n"
+ "searchutil -c trial:namespace:factors:<namespaceID>\n\tDump all factors for namespace <namespaceID>.\n"
+ "searchutil -c trial:namespace:load:<namespaceID>\n\tReload trial namespace <namespaceID>.\n"
+ "searchutil -c trial:trigger:<client>:<queryID>:<codepathID>\n\tEmit a log trigger for <queryID> if the value of 'codepathIDs' for <client> includes <codepathID>.\n"
+ "substringWithRange:"
+ "succeeded"
+ "test"
+ "trialManagerForNamespaceId:"
+ "trialOverrideList"
+ "trialParameterList"
+ "trigger"
+ "unload"
+ "updating locale to %@"
+ "usageInformationForSubcommand:"
+ "v28@0:8@\"NSDictionary\"16B24"
+ "v32@?0@\"NSString\"8@16^B24"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "%@\nAssertions:%@\n"
- "%@\nSupported Languages:\n%@\nCache:\n%@\n"
- "BundleVersion:%@\n\n%@"
- "didUpdateDefaultsWithLanguage:bundleVersions:trial:"
- "lastObject"
- "loadDataSource:"
- "requestAssetsForLanguages:"
- "v36@0:8@\"NSString\"16@\"NSDictionary\"24B32"
- "v36@0:8@16@24B32"

```
